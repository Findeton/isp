# Relativistic ISP V3 Paper 21: `SEL2` Tree-Rate Source Or Falsification

Author: Felix Robles Elvira

## Abstract

Paper 20 reduced the actual direct-witness confinement route to one parked
same-record source gate on the strict reduced `SEL2` branch:

```math
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}RATE\text{-}GATE}
:=
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(\rho)
+
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
(V_\rho,\gamma_\rho,q_\rho).
```

Paper 21 attacks that gate directly. It is not a synthesis paper and it is not
allowed to import a Wilson-loop area law, a mass gap, or an already-existing
continuum Yang-Mills measure. Its job is narrower: decide whether the frozen
`SEL2` block-plaquette scalar record has enough normalized sheet rate to beat
the rooted surface-polymer entropy left by Paper 20, or else falsify the
strict reduced `SEL2` direct-witness route.

The two live inequalities are:

```math
T_-^{SEL2}>\Theta_T^{tree}(\rho),
\qquad
q_\rho\gamma_\rho>\Theta_{esc}^{tree}.
```

If both pass, Paper 21 then tests the remaining
\(\mathrm{P20\text{-}SEL2\text{-}SURF\text{-}PREF\text{-}CAP}\). If either
fails on the same frozen record law, this `SEL2` route fails without falsifying
every possible confinement strategy.

## 0. Barandes-Aligned Boundary

The primitive object remains the whole-process law of scalar records. Paper 21
uses only:

1. the frozen `SEL2` pushed-forward scalar record law from Paper 20;
2. block-plaquette central character records;
3. finite block-time and escape-window inequalities;
4. one disjoint debit ledger inherited from Paper 20.

Paper 21 does not permit:

1. hidden flux tubes as ontology;
2. gauge-fixed fields as primitive states;
3. unrecorded partial Markov kernels;
4. a Wilson-loop area law as an input to the tree-rate source;
5. a mass gap or continuum Yang-Mills measure as an input.

Surfaces, sheets, collars, and polymers are auxiliary estimates. They must be
eliminated into scalar inequalities before any final theorem is stated.

## 0A. Imports From Paper 20

Paper 21 imports Paper 20 only as a completed reduction and obstruction
ledger. The inherited frozen data are:

```math
\mathrm{P20\text{-}SEL2}(\eta_{ch,20}^{SEL2},20),
\qquad
\mathrm{P20\text{-}SEL2\text{-}NOSMUGGLE},
```

```math
\mathrm{P20\text{-}SEL2\text{-}TR\text{-}COMMON},
\qquad
T_j^{SEL2,conv},
```

```math
\widehat\eta_{*,20},
\qquad
\underline M_{pre13}^{SEL2,20},
\qquad
M_{13}^{surf,SEL2}.
```

It also imports the rooted tree thresholds:

```math
D_{13,dec}^{SEL2,20}
:=
20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
```

```math
G_{13,tree}^{SEL2}
:=
1+\log 19+D_{13,dec}^{SEL2,20},
```

```math
\Theta_{esc}^{tree}
:=
1-\exp(-G_{13,tree}^{SEL2}),
```

and

```math
\Theta_T^{tree}(\rho)
:=
{2G_{13,tree}^{SEL2}\over C_2(\rho)}.
```

The final Paper-20 pass condition, before the global Paper-19 import, is:

```math
\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(\rho)
+
\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}
(V_\rho,\gamma_\rho,q_\rho)
+
\mathrm{P20\text{-}SEL2\text{-}SURF\text{-}PREF\text{-}CAP}.
```

## 0B. Main Claim Form

Paper 21 has three possible honest outcomes.

1. **Pass.** It proves both tree-rate subgates on the frozen `SEL2` law and
   proves the prefactor cap. Then the strict reduced `SEL2` branch supplies
   the missing Paper-20 loss pass.
2. **Falsification of this branch.** It proves either the time gate or the
   escape gate cannot pass on the frozen `SEL2` branch, or that the prefactor
   cap fails after the rate gate. This falsifies the strict reduced `SEL2`
   direct-witness route, not confinement itself.
3. **Parked source obstruction.** It reduces the gate to a sharper scalar
   source estimate that the current corpus still does not prove or disprove.

## 0C. Current Working Status

As of Sections 98--130, Paper 21 is in the parked-source outcome:

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}^{+}
\quad+\quad
\mathrm{PARK\text{-}SDSRC}^{+}
\quad+\quad
\mathrm{PARK\text{-}CMPSRC}^{+}.
}
```

The constructor row classes are filled, and the minimal `SU(2)` fusion
subtable for the literal probe is enumerated.  Section 100 prints the maximal
same-record package currently licensed by the corpus: the fusion multiplicity
subpackage is literal, while the `SD`, `act`, `cmp`, and target/increment
parts remain parked at the finite row-map package.  Section 101 sharpens this:
the row-map obstruction starts already at the vertex-representative list

```math
\overline V_{99}^{lit}.
```

Section 102 supplies a conservative over-refined vertex cover.  With that
cover as the working convention, the active obstruction moves back to the row
maps.  The exact minimal quotient list remains at `PARK-VERT`, but no scalar
record is collapsed by the cover, so the finite audit may proceed on the
over-refined universe.

Section 103 prints the retained `SU(2)` fusion row map
\(R_{fus}^{99,+}\) on that over-refined universe.  These rows are exact
same-record channel bookkeeping rows with \(\Delta_X=0\); on the strict
branch they are assigned to the `CMSSI`/channel ledger rather than counted as
reduced escaping pass rows.  The remaining unprinted row maps are therefore
`SD`, `act`, and `cmp`.

Section 104 prints the structural `act` row map on the same over-refined
universe.  This closes the action target/increment bookkeeping, but not the
numeric local-action coefficient and off-diagonal inverse slots.  Those
finite entries are now isolated as `PARK-ACTVAL+`.  The remaining unprinted
row maps are `SD` and `cmp`.

Section 105 prints the finite action-value ledger shape, the retained
`SU(2)` channel-projection scalars, the safe envelopes, and the carried
completion.  Thus the action-value obstruction is no longer a missing
definition; it is an explicit source-table obstruction, denoted
`PARK-ACTSRC+`.

Section 106 prints the structural compact-group Schwinger-Dyson/Casimir row
map \(R_{SD}^{99,+}\) and its finite source ledger.  The only row-map still
unprinted is now \(R_{cmp}^{99,+}\).  The `SD` coefficients and inverse slots
are isolated as `PARK-SDSRC+`.

Section 107 prints the structural common-comparison row map
\(R_{cmp}^{99,+}\).  All four structural row maps are now printed on the
over-refined cover.  What remains parked is source/value data: `ACTSRC`,
`SDSRC`, and `CMPSRC`.

Section 108 assembles the carried finite table obtained by combining the four
printed row maps with the safe carried source completions.  On that strict
carried branch the certified pass graph is empty, so the zero-growth pass SCC
test is closed vacuously; every possible nontrivial cycle remains outside the
pass graph in `CMSSI`, `BTQ`, `cmpbat`, or an explicit carried source ledger.

Section 109 audits `ACTSRC+` against Papers 16 and 20.  It proves that the
current corpus supplies the exact `SEL2` scalar row freeze, the finite
heat-kernel actual law, and a same-record `HK-SF-YM2` local envelope route.
It does not yet supply the literal action-value row table needed by Section
105.  Thus `PARK-ACTSRC+` remains, now split into four sharper subgates:
pushforward, row values, inverse/off-diagonal slots, and exact zero/carry
classification.

Section 110 prints the first finite `YM2 -> act` pushforward object: an
over-refined carrier relation from the Paper-16 `HK-SF-YM2` labels to the
Section-104 action atoms, together with a coarse projection-norm bound.  This
closes the envelope version of the pushforward gate, but not the literal
monomial selector; the remaining action-source obstruction is therefore
row-value, inverse-slot, derivative/product selector, and literal
zero/carry data.

Section 111 tests whether that coarse over-refined envelope can plausibly be
spent in the reduced decay inequality.  The verdict is negative as a
certified route: the carrier norm alone has a safe logarithmic size about
\(104.57\), before geometry, inverse growth, and the Paper-16 local constant
are added.  This does not falsify the real branch, because the bound is an
over-cover, but it shows that the next useful action-source step is the
literal selector, not blind spending of the coarse carrier.

Section 112 prints the selector as far as the current source corpus permits:
the `YM2` label kind is fixed, impossible `plaq`/`prod` branches are removed
on the strict connected-cumulant branch, and the coarse carrier is replaced
by a much smaller monomial-selector package.  The actual monomial support
and word lists are finite but still unprinted, so `ACTSRC+` remains parked at
`PARK-ACTSRC-MON+ROWVAL+INV+ZC`.

Section 113 replaces the symbolic monomial package by a finite root-coordinate
alphabet and coupled monomial graphs.  The action selector norm is now
polynomial in the number \(n_A^{113}\) of root axial-tree coordinates:
\[
\Pi_{act}^{113,mon}
\le
3\binom{n_A^{113}+3}{4}
+45\binom{n_A^{113}+2}{3}^{2}
+\binom{n_A^{113}+1}{2}.
\]
The remaining monomial obstruction is no longer an all-word/all-support
over-cover; it is the concrete derivative-tensor and covariance-pair table of
the actual root chart.

Section 114 computes the active root-coordinate count under the printed
Section-102 local-stencil convention.  For the full connected \(3^4\) root
stencil, axial-tree gauge leaves at most \(136\) non-tree links, hence
\(n_A^{113}\le408\).  This gives the polynomial selector surcharge
\(\log\Pi_{act}^{113,mon}\le36.31\), with a fully cover-based fallback
\(\log\Pi_{act}^{113,mon}\le39.08\).  Thus `ROOTCOUNT` is no longer the
dominant obstruction; the remaining action-source work is derivative-tensor,
covariance-pair, row-value, inverse, and zero/carry data.

Section 115 freezes the exact analytic margin that must be sourced before the
derivative tensor table is worth printing.  On the connected strict branch,
the current primitive reduced-decay target is
\[
\Theta_{red}^{115}
=
\log C_{geom}^{cert}+g_q^{cert}
+\max\{\log A_{nonact}^{cert},
\log^+(B_{act}^{110}C_v^{YM2,min})+36.31\}.
\]
The strict branch needs \(m_{red}^{act}>\Theta_{red}^{115}\), or an
already-amplified shell-tail theorem.  In the artificial best case this still
requires \(m_{red}^{act}>\log^+C_v^{YM2,min}+36.31\).

Section 116 audits all plausible sources for \(m_{red}^{act}\).  Papers
10--12 and 20 provide finite/projective, loop-readout, and coefficient
scaffolding but not a reduced forced-tail decay rate.  Paper 16's clean
finite-template KP worksheet is the only existing source technology that
could produce a primitive exponent, but it must still be transferred to the
actual reduced \(E_{14}/X_{13}\) tower through a same-record finite table,
coverage, size-growth, and row-value/inverse data.  Thus the live source fork
is: prove a direct shell-tail theorem, prove the Paper-16-to-Paper-21 reduced
KP transfer, or keep \(m_{red}^{act}\) parked.

Section 117 carries out the first item of that source fork: it classifies the
only structural `SD` and `act` rows that could contribute to a reduced
decay exponent.  The classification is closed, but the current carried
completion still licenses no pass rows, because `ACTSRC+` and `SDSRC+`
remain unsupplied.  Thus \(\mu_0\) must not be computed on the carried
graph; it can only be computed after the structural candidate rows receive
literal source values and inverse/zero/carry decisions.

Section 118 prints the finite candidate-row generator promised by Section
117.  For each over-refined vertex it lists exactly which retained fusion
channels, local supports, trace words, and local atom kinds generate
structural action or SD decay candidates.  This is still a structural table:
it identifies every row on which `ACTSRC+` and `SDSRC+` must act, but it does
not turn missing coefficients into pass rows.

Section 119 sources `ACTSRC+` as far as the current corpus permits.  On the
strict `YM2` branch, non-stencil action candidates are zero as `YM2` sources,
stencil candidates outside the coupled root monomial graphs are zero, and
stencil candidates inside the quartic, connected double-cubic, or Jacobian
graphs receive finite same-record coefficient envelopes from Paper 16.  This
closes the row-by-row coefficient-envelope part of `ACTSRC+`; it does not
close literal row values, covariance-pair membership, derivative-tensor
membership, or inverse slots.  Hence the licensed action pass graph remains
empty until those entries are printed.

Section 120 sources `SDSRC+` row by row.  The exact compact-group
Schwinger-Dyson identity supplies the algebraic source functional, the
retained `SU(2)` cutoff supplies the Casimir/channel scalars, and the
support-growing Casimir self-row over-cover is deleted as an inactive formal
row.  The live `SDdiv` and `loop` rows are reduced to finite projected
compact-group multipliers and same-shell inverse slots.  Thus `SDSRC+` is
reduced to `SDPROJ`, `SDINV`, and literal zero/carry tags; it still does not
license SD pass rows on the carried branch.

Section 121 classifies the `SD` candidates after that source reduction.  For
the support-growing decay candidates, `SD-CMSSI` and `SD-BTQ` are empty by
construction; support-growing `Cas` candidates are zero, derivative-channel
rows with \(\Gamma_{SD}^{99}=0\) are zero, and the only live nonzero
structural candidates are `SDdiv/loop` rows in the nontrivial retained
channels \(F_5,F_6,F_7,F_9,F_{10},F_{11}\).  Since `PROJ` and `INV` are still
unprinted, those live rows are carried, not pass rows.

Section 122 answers the survival question.  Structurally, yes: whenever the
source channel is \(\alpha=1/2\) or \(\alpha=1\) and the local frontier does
not already fill the over-refined stencil, there are support-growing
`SDdiv/loop` survivors.  On the current licensed branch, no: every such
survivor is still carried because the projected multiplier and inverse
tables are unprinted.

Sections 123--125 close the `SDSRC+` audit as far as the current corpus
allows.  Section 123 proves the sharp support-growing projected-coefficient
envelope under the explicit minimal retained-word projection convention:
all live `SDdiv/loop` survivor coefficients are bounded by \(8\), with the
channelwise values printed.  If that convention is not adopted, the finite
projected multiplier table remains the named obstruction.  Section 124 then
checks every available inverse source and proves that the same-shell inverse
slots \(\mathcal O_{SD}^{99,+}\) are not supplied by Papers 10--16, 20, or the
earlier sections of Paper 21.  Section 125 gives the final verdict:
the decay-eligible `SDSRC+` branch is not mysterious anymore; it is either a
conditional finite certificate requiring the projected multiplier and inverse
tables, or, on the present corpus, a parked inverse/projection obstruction
with no licensed `SD-pass` rows.

Sections 126--129 perform the analogous final audit for `ACTSRC+`.  The
result is stricter than the earlier coarse tests: the envelope action source
is closed on the strict `YM2` branch with the polynomial selector surcharge
already bounded in Section 114, so `DTENS` and `COVPAIR` are no longer needed
for the envelope route.  They remain necessary only for a literal signed
row-value table.  Papers 16 and 20 do not print that literal table, and they
also do not print the same-shell action inverse slots
\(\mathcal O_{act}^{99,+}\).  Therefore the current corpus still licenses no
`act-pass` rows, but the obstruction is now exactly finite:
print `ACTINV` and admissibility/zero-carry tags if the envelope route is
accepted, or additionally print `DTENS/COVPAIR/ROWVAL-LIT` if literal row
values are demanded.

Section 130 freezes the export boundary to Paper 22.  Paper 21 is not a
global synthesis paper: it exports printed structural row maps, closed
finite-envelope audits for `SDSRC+` and `ACTSRC+`, and an empty licensed pass
graph on the current corpus.  The remaining work is a continuation problem:
print the common inverse/admissibility package, close `CMPSRC+`, rerun the
pass graph, or replace the finite-table route by a direct reduced-tail source
theorem.

## 1. Frozen Tree-Time Data

### Definition 1.1: `SEL2` Tree-Time Parameter Record

The tree-time parameter record is the tuple

```math
\mathrm{TTIME\text{-}DATA}
(\rho,s,\epsilon_A,\chi,\widehat\eta_{*,20})
```

where:

1. `rho` is the fixed nontrivial representation channel from the frozen
   `SEL2` selector;
2. `C_2(rho)>0`;
3. `s>0` is the AF-area parameter in `S_j/H_j -> s`;
4. `0<epsilon_A<1` is the AF-area slack;
5. `0<chi<1` is the heat-time scheme slack;
6. \(0\le\widehat\eta_{*,20}<1\) is the frozen Paper-20 activity ceiling.

The clean finite-template time window is

```math
T_{clean,-}^{SEL2}:=s(1-\epsilon_A)(1-\chi),
\qquad
T_{clean,+}^{SEL2}:=s(1+\epsilon_A)(1+\chi).
```

### Definition 1.2: Paper-20 Tree-Time Threshold

Given

```math
\mathrm{TTIME\text{-}DATA}
(\rho,s,\epsilon_A,\chi,\widehat\eta_{*,20}),
```

define

```math
\Theta_T^{tree}(\rho)
:=
{2\over C_2(\rho)}
\left(
1+\log 19
 +20{\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right).
```

The time gate is:

```math
\mathrm{P21\text{-}TTREE}(\rho):
\qquad
T_-^{SEL2}>\Theta_T^{tree}(\rho).
```

This is the same statement as
\(\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}TIME}(\rho)\), renamed only to
make Paper 21's local proof labels shorter.

### Theorem 1.3: Exact Tree-Time Trichotomy

Assume
\(\mathrm{TTIME\text{-}DATA}(\rho,s,\epsilon_A,\chi,\widehat\eta_{*,20})\)
and the standard `SEL2` sheet-time scaling audit imported from Paper 20.

1. If

   ```math
   T_{clean,-}^{SEL2}>\Theta_T^{tree}(\rho),
   ```

   then \(\mathrm{P21\text{-}TTREE}(\rho)\) passes.

2. If

   ```math
   T_{clean,+}^{SEL2}\le\Theta_T^{tree}(\rho),
   ```

   then \(\mathrm{P21\text{-}TTREE}(\rho)\) fails for the frozen standard
   `SEL2` template.

3. If

   ```math
   T_{clean,-}^{SEL2}
   \le
   \Theta_T^{tree}(\rho)
   <
   T_{clean,+}^{SEL2},
   ```

   then the current finite-template window is inconclusive.

Proof.

Paper 20 Theorem 4.3A.160BB gives

```math
T_j^{SEL2,conv}=S_jt_{i(j)}+o(1)
```

and the cofinal window

```math
T_{clean,-}^{SEL2}
\le
\liminf_jT_j^{SEL2,conv}
\le
\limsup_jT_j^{SEL2,conv}
\le
T_{clean,+}^{SEL2}.
```

The three cases are exactly the pass/falsification/inconclusive alternatives
of Paper 20 Theorem 4.3A.160BH.40T.6. `square`

### Corollary 1.4: First Time-Gate Investigation Verdict

The finite block pushforward does not create hidden extra block time. It
computes the clean window

```math
s(1-\epsilon_A)(1-\chi)
\le
T_j^{SEL2,conv}
\le
s(1+\epsilon_A)(1+\chi)
```

cofinally up to endpoint slack.

Therefore Paper 21 cannot prove \(\mathrm{P21\text{-}TTREE}\) by
bookkeeping alone. It must do one of the following:

1. freeze \(s,\epsilon_A,\chi,\widehat\eta_{*,20},\rho\) so that the pass
   inequality in Theorem 1.3 holds;
2. freeze them so that the falsifier in Theorem 1.3 holds;
3. prove a sharper same-record lower bound for
   `liminf_jT_j^{SEL2,conv}`;
4. lower \(\Theta_T^{tree}\) by a sharper same-record surface-growth theorem.

## 2. The `s`-Window Tension

### Definition 2.1: Tree-Time Lower Bound On `s`

The selector parameter `s` passes the clean tree-time gate if

```math
s>S_T^{pass}(\rho)
:=
{2\left(
1+\log 19
+20\widehat\eta_{*,20}/(1-\widehat\eta_{*,20})
\right)
\over
C_2(\rho)(1-\epsilon_A)(1-\chi)}.
```

It is cleanly falsified if

```math
s\le S_T^{fail}(\rho)
:=
{2\left(
1+\log 19
+20\widehat\eta_{*,20}/(1-\widehat\eta_{*,20})
\right)
\over
C_2(\rho)(1+\epsilon_A)(1+\chi)}.
```

Between `S_T^{fail}` and `S_T^{pass}`, the current slack window does not
decide the gate.

### Definition 2.2: Decoration-Signal Compatibility Window

Paper 20's `SEL2` decoration pass with `C_area=20` requires

```math
\eta_{19}^{res}< {L_{sig}^{SEL2}(s)\over20+L_{sig}^{SEL2}(s)},
```

where

```math
L_{sig}^{SEL2}(s):=\log(1+Sig_{AFM}^{SEL2}(s)).
```

The signal is inherited from the clean matched-time coefficient selector:

```math
Sig_{AFM}^{SEL2}(s)
=
\exp\left(
-[2(1-\alpha)+\epsilon_G]
{(1+\chi)s(1+\epsilon_A)C_2(\rho)\over2}
\right)
\left[
1-\exp\left(
-[\alpha^2-\epsilon_G]
{(1-\chi)s(1-\epsilon_A)C_2(\rho)\over2}
\right)
\right].
```

Thus increasing `s` helps the tree-time gate but can shrink the signal floor
through the first exponential factor. The `TREE-TIME` gate and the decoration
gate are therefore coupled; Paper 21 may not choose `s` for time without
rerunning the decoration and pre-surface margin checks.

### Lemma 2.3: Large `s` Is Not A Free Pass

For fixed admissible `alpha,epsilon_G,epsilon_A,chi,rho`,

```math
Sig_{AFM}^{SEL2}(s)\to0
\qquad(s\to\infty).
```

Consequently

```math
{L_{sig}^{SEL2}(s)\over20+L_{sig}^{SEL2}(s)}\to0.
```

If `eta_19^{res}>0` is fixed, then sufficiently large `s` violates the
decoration-signal compatibility inequality of Definition 2.2.

Proof.

The bracketed term in `Sig_AFM^{SEL2}` is bounded by `1`, while the leading
factor is `exp(-c s)` with `c>0`. Hence `Sig_AFM^{SEL2}(s)->0`. Since
`log(1+x)/(20+log(1+x))->0` as `x->0`, the second claim follows. If
`eta_19^{res}>0`, the right-hand side is eventually smaller than
`eta_19^{res}`. `square`

### Corollary 2.4: First Paper-21 Feasibility Problem

The first real Paper-21 calculation is not just

```math
s>S_T^{pass}(\rho).
```

It is the simultaneous feasibility problem:

```math
s>S_T^{pass}(\rho),
```

```math
\eta_{19}^{res}< {L_{sig}^{SEL2}(s)\over20+L_{sig}^{SEL2}(s)},
```

and

```math
U_{pre13}^{SEL2}(s)
<
\underline M_{loss}^{SEL2,20}(s),
```

with all quantities evaluated on the same frozen record law.

If no `s` and representation channel `rho` satisfy this system, then the
strict reduced `SEL2` route fails before the escape gate is even charged. If
the system has a feasible window, Paper 21 may proceed to `ESC-MASS`.

## 3. Escape-Mass Target

### Definition 3.1: Paper-21 Escape-Mass Gate

The local Paper-21 name for
\(\mathrm{P20\text{-}SEL2\text{-}ESC\text{-}MASS}\) is
\(\mathrm{P21\text{-}ESC\text{-}MASS}
(V_\rho,\gamma_\rho,q_\rho)\). It holds when:

```math
1-{\Phi_\rho(U)\over d_\rho}\ge\gamma_\rho>0
\qquad(U\in V_\rho),
```

```math
\liminf_j\nu_{p,j}^{SEL2}(V_\rho)\ge q_\rho>0,
```

and

```math
q_\rho\gamma_\rho>\Theta_{esc}^{tree}.
```

Paper 20 already proved that the existing positive-escape theorem supplies at
most a product below `1/8`, while the rooted tree threshold is at least
`1-1/(19e)>0.98`. Paper 21 therefore needs a genuinely stronger
anti-concentration theorem or a lower surface-growth threshold.

### Definition 3.2: Near-Maximal Escape Source

\(\mathrm{P21\text{-}NEARMAX\text{-}ESC}(\delta_{esc})\) holds when there is
a central set \(V_\rho\) such that

```math
q_\rho\gamma_\rho\ge1-\delta_{esc}
```

and

```math
\delta_{esc}
<
\exp(-G_{13,tree}^{SEL2}).
```

This is exactly strong enough to prove
\(\mathrm{P21\text{-}ESC\text{-}MASS}\).

### Theorem 3.3: Near-Maximal Escape Closes The Escape Half

If \(\mathrm{P21\text{-}NEARMAX\text{-}ESC}(\delta_{esc})\) holds, then
\(\mathrm{P21\text{-}ESC\text{-}MASS}
(V_\rho,\gamma_\rho,q_\rho)\) holds.

Proof.

The second inequality in Definition 3.2 gives

```math
1-\delta_{esc}>1-\exp(-G_{13,tree}^{SEL2})
=\Theta_{esc}^{tree}.
```

Since \(q_\rho\gamma_\rho\ge1-\delta_{esc}\), the escape product beats
\(\Theta_{esc}^{tree}\). `square`

### Honest Boundary 3.4

\(\mathrm{P21\text{-}NEARMAX\text{-}ESC}\) is much stronger than the positive
noncollapse theorem of Paper 20. It is a real dynamical anti-concentration
estimate for the actual `SEL2` block-plaquette scalar record. It cannot be
imported from rowwise Peter-Weyl regularity, large-field upper bounds, or
residual upper bounds.

## 4. Next Execution Order

Paper 21 should now proceed in this order:

1. solve or bound the simultaneous `s`-window feasibility problem of Corollary
   2.4;
2. if feasible, try to prove
   \(\mathrm{P21\text{-}NEARMAX\text{-}ESC}\) or show it is impossible for the
   active `SEL2` law;
3. if escape is impossible at the rooted tree threshold, attack the
   surface-connective constant before trying more coefficient estimates;
4. if both time and escape pass, evaluate the prefactor cap;
5. state pass, falsification, or parked obstruction.

## 5. Scalar Feasibility Worksheet And Exact `s`-Window

This section performs the first execution step. It does not use a Wilson-loop
area law, a mass gap, or any continuum Yang-Mills measure. It asks only whether
the scalar worksheet already frozen in Paper 20 leaves a nonempty range of AF
area parameters `s` on one same-record `SEL2` branch.

### Definition 5.1: One-Branch Signal Profile

Fix one representation channel `rho` and the loss-side slacks

```math
0<\alpha<1,\qquad
0<\epsilon_G<\min\{\alpha^2,2(1-\alpha)\},
```

```math
0<\epsilon_A<1,\qquad 0<\chi<1,
\qquad C_2(\rho)>0.
```

Define the two positive scalar rates

```math
a_\rho
:=
\left[2(1-\alpha)+\epsilon_G\right]
{(1+\chi)(1+\epsilon_A)C_2(\rho)\over2},
```

```math
b_\rho
:=
\left[\alpha^2-\epsilon_G\right]
{(1-\chi)(1-\epsilon_A)C_2(\rho)\over2}.
```

The `SEL2` signal profile is

```math
F_\rho(s)
:=
Sig_{AFM}^{SEL2}(s)
=
e^{-a_\rho s}\left(1-e^{-b_\rho s}\right).
```

The logarithmic signal is

```math
L_\rho(s):=\log(1+F_\rho(s)).
```

### Lemma 5.2: The Signal Profile Has One Peak

The function \(F_\rho\) is strictly increasing on
\((0,s_\rho^{pk})\), strictly decreasing on
\((s_\rho^{pk},\infty)\), and has the unique maximum

```math
s_\rho^{pk}
=
{1\over b_\rho}
\log\left({a_\rho+b_\rho\over a_\rho}\right).
```

The peak value is

```math
F_\rho^{pk}
=
{b_\rho\over a_\rho+b_\rho}
\left({a_\rho\over a_\rho+b_\rho}\right)^{a_\rho/b_\rho}.
```

Proof.

Differentiate:

```math
F_\rho'(s)
=
e^{-a_\rho s}\left[-a_\rho+(a_\rho+b_\rho)e^{-b_\rho s}\right].
```

Thus \(F_\rho'(s)=0\) exactly when

```math
e^{-b_\rho s}={a_\rho\over a_\rho+b_\rho},
```

which gives the displayed \(s_\rho^{pk}\). The sign of \(F_\rho'\) is positive
before this point and negative after it. Substituting
\(e^{-b_\rho s_\rho^{pk}}=a_\rho/(a_\rho+b_\rho)\) gives the peak value.
`square`

### Definition 5.3: Frozen-Activity Feasibility Worksheet

For a single frozen branch with activity ceiling \(\widehat\eta_{*,20}\) and
pre-surface upper debit \(U_{pre13}^{SEL2}\ge0\), set

```math
D_{20}
:=
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}},
```

```math
Y_{res}
:=
\exp\left({20\eta_{19}^{res}\over1-\eta_{19}^{res}}\right)-1,
```

and

```math
Y_{pre}
:=
\exp(D_{20})-1+U_{pre13}^{SEL2}.
```

The tree-time lower endpoint is

```math
S_T^{pass}(\rho)
:=
{2(1+\log 19+D_{20})
\over
C_2(\rho)(1-\epsilon_A)(1-\chi)}.
```

The frozen-activity scalar feasibility window is

```math
\mathcal W_{fr}(\rho)
:=
\left\{
s>S_T^{pass}(\rho):
F_\rho(s)>Y_{res},
\quad
F_\rho(s)>Y_{pre}
\right\}.
```

On the Paper-20 `SEL2` branch
\(\widehat\eta_{*,20}\ge\eta_{19}^{res}\), and \(U_{pre13}^{SEL2}\ge0\).
Therefore \(Y_{pre}\ge Y_{res}\). The residual inequality is then redundant,
and

```math
\mathcal W_{fr}(\rho)
=
\left\{
s>S_T^{pass}(\rho):
F_\rho(s)>Y_{pre}
\right\}.
```

### Theorem 5.4: Exact Solution Of The Frozen-Activity `s`-Window

Let \(Y:=Y_{pre}\). If

```math
Y\ge F_\rho^{pk},
```

then \(\mathcal W_{fr}(\rho)=\varnothing\).

If

```math
0\le Y<F_\rho^{pk},
```

let \(s_\rho^-(Y)<s_\rho^{pk}<s_\rho^+(Y)\) be the two roots of

```math
F_\rho(s)=Y.
```

Then

```math
\mathcal W_{fr}(\rho)
=
\left(
\max\{S_T^{pass}(\rho),s_\rho^-(Y)\},
\ s_\rho^+(Y)
\right),
```

and the frozen branch has a nonempty scalar feasibility window if and only if

```math
S_T^{pass}(\rho)<s_\rho^+(Y).
```

Proof.

By Lemma 5.2, \(F_\rho\) is one-humped. If \(Y\ge F_\rho^{pk}\), the strict
inequality \(F_\rho(s)>Y\) is never satisfied. If \(Y<F_\rho^{pk}\), the
one-hump structure gives exactly two roots and
\(F_\rho(s)>Y\) precisely between them. Intersecting this interval with the
strict tree-time half-line \(s>S_T^{pass}(\rho)\) gives the displayed window.
It is nonempty exactly when its left endpoint is strictly below
\(s_\rho^+(Y)\). `square`

### Definition 5.5: Adaptive Paper-20 Worksheet

The previous theorem solves a branch after the activity ceiling and
pre-surface upper debit have been frozen. To search over possible `s` values
without changing record laws mid-proof, Paper 21 uses the following
one-parameter family of frozen branches.

For every candidate \(s>0\), set

```math
L_{20}(s):=L_\rho(s)=\log(1+F_\rho(s)),
\qquad
\tau_{20}(s):={L_{20}(s)\over20+L_{20}(s)}.
```

For a fixed large-field excess choice \(\epsilon_{lf}>0\), put

```math
\delta_{20}(s)
:=
\log\left(1+{2C_{KP}\over\tau_{20}(s)}\right)
+\epsilon_{lf},
```

```math
\bar\eta_{res,20}(s)
:=
2C_{KP}
{\exp(-\delta_{20}(s)r_{res}^{clean})
\over
1-\exp(-\delta_{20}(s))},
```

and

```math
\widehat\eta_{*,20}(s)
:=
{1\over2}
\left(\tau_{20}(s)+\bar\eta_{res,20}(s)\right).
```

The branch is admissible at \(s\) only if

```math
0<\bar\eta_{res,20}(s)<\tau_{20}(s).
```

When it is admissible, define

```math
\underline M_{loss}^{SEL2,20}(s)
:=
1+F_\rho(s)
-
\exp\left(
{20\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}
\right).
```

For a declared same-record nonsurface upper envelope
\(U_{pre13}^{SEL2}(s)\ge0\), the adaptive `SEL2` feasibility set is

```math
\mathcal W_{ad}(\rho)
:=
\left\{
s>0:
\begin{array}{l}
0<\bar\eta_{res,20}(s)<\tau_{20}(s),\\[2mm]
s>
{2(1+\log19+
20\widehat\eta_{*,20}(s)/(1-\widehat\eta_{*,20}(s)))
\over C_2(\rho)(1-\epsilon_A)(1-\chi)},\\[3mm]
U_{pre13}^{SEL2}(s)<\underline M_{loss}^{SEL2,20}(s)
\end{array}
\right\}.
```

### Theorem 5.6: The `s`-Window Is Solved By A One-Variable Scalar Test

For the strict reduced `SEL2` route, the branch reaches the escape-mass
problem if and only if

```math
\mathcal W_{ad}(\rho)\ne\varnothing.
```

Equivalently, after choosing a candidate \(s\), the exact pass test is the
three-line scalar check in Definition 5.5. If the set is empty for every
allowed \(\rho\), the strict reduced `SEL2` route fails before the escape-mass
gate. If it is nonempty, choose any

```math
s\in\mathcal W_{ad}(\rho)
```

and freeze the corresponding same-record branch before attacking
\(\mathrm{P21\text{-}ESC\text{-}MASS}\).

Proof.

The first line in \(\mathcal W_{ad}\) is exactly the Paper-20 worksheet
admissibility condition \(0<\bar\eta_{res,20}<\tau_{20}\). The second line is
Theorem 1.3 written with the activity ceiling recomputed for that candidate
branch. The third line is precisely the pre-surface margin inequality of
Paper 20 Definition 4.3A.57 and Theorem 4.3A.58. All three are scalar
inequalities on the pushed-forward record law. Their conjunction is therefore
equivalent to reaching the escape-mass gate without changing the branch or
charging any hidden debit. `square`

### Corollary 5.7: Current Paper-21 `s`-Window Verdict

Paper 21 has now reduced the `s`-window to the explicit scalar set
\(\mathcal W_{ad}(\rho)\). This is a solved feasibility problem in the
following precise sense:

1. for a fixed upper debit \(U_{pre13}^{SEL2}\), Theorem 5.4 gives the exact
   two-root window;
2. for the adaptive Paper-20 branch, Theorem 5.6 gives a one-variable scalar
   test with no hidden continuum or area-law input.

The current text does not yet certify that \(\mathcal W_{ad}(\rho)\) is
nonempty, because it has not supplied numerical values or sharp functions for
\(U_{pre13}^{SEL2}(s)\), \(C_{KP}\), \(r_{res}^{clean}\), the allowed channel
\(\rho\), and the large-field excess \(\epsilon_{lf}\). It also does not
falsify the route, because no matching lower bound has shown
\(\mathcal W_{ad}(\rho)=\varnothing\) for every allowed channel.

The next Paper-21 calculation is therefore finite and concrete: instantiate
these scalar inputs, compute \(\mathcal W_{ad}(\rho)\), and only then attempt
the near-maximal escape source.

## 6. Best-Case Feasibility Probe

The preceding section solves the \(s\)-window but does not say whether the
window is empty for the actual strict reduced branch. Before optimizing inside
an unknown set, Paper 21 first runs the cheapest possible probe: keep the
Paper-20 adaptive decoration worksheet, but set the nonsurface transport debit
to zero. This is only a necessary sanity check. It is not a proof of the full
branch, because the actual branch may have positive carried debits.

### Definition 6.1: Optimistic Zero-Debit Probe

Fix the same data as Definition 5.5, with

```math
C_{KP}>0,\qquad r_{res}^{clean}\ge1,\qquad \epsilon_{lf}>0.
```

The optimistic probe is the adaptive worksheet of Definition 5.5 with

```math
U_{pre13}^{SEL2}(s)\equiv0.
```

No other gate is erased: the residual activity, character-tail budget,
activity ceiling, decoration debit, and tree-time threshold are still the
Paper-20 adaptive quantities

```math
\tau_{20}(s),\quad
\bar\eta_{res,20}(s),\quad
\widehat\eta_{*,20}(s),\quad
\underline M_{loss}^{SEL2,20}(s).
```

### Lemma 6.2: The Adaptive Activity Is Strictly Admissible

For every \(s>0\), the optimistic adaptive worksheet satisfies

```math
0<\bar\eta_{res,20}(s)<\tau_{20}(s),
\qquad
0<\widehat\eta_{*,20}(s)<\tau_{20}(s).
```

Proof.

Since \(F_\rho(s)>0\), one has \(L_{20}(s)>0\) and
\(\tau_{20}(s)>0\). Let

```math
x_s:=\exp(-\delta_{20}(s)).
```

By Definition 5.5,

```math
x_s
=
e^{-\epsilon_{lf}}
{\tau_{20}(s)\over\tau_{20}(s)+2C_{KP}}.
```

Using \(r_{res}^{clean}\ge1\),

```math
\bar\eta_{res,20}(s)
\le
2C_{KP}{x_s\over1-x_s}
=
{2C_{KP}e^{-\epsilon_{lf}}\tau_{20}(s)
\over
2C_{KP}+(1-e^{-\epsilon_{lf}})\tau_{20}(s)}
<
\tau_{20}(s).
```

Positivity is immediate from \(C_{KP}>0\), \(x_s>0\). Therefore the average
\(\widehat\eta_{*,20}(s)=(\tau_{20}(s)+\bar\eta_{res,20}(s))/2\) is also
strictly between \(0\) and \(\tau_{20}(s)\). `square`

### Lemma 6.3: The Zero-Debit Post-Decoration Margin Is Positive

Under the optimistic probe,

```math
\underline M_{loss}^{SEL2,20}(s)>0
\qquad(s>0).
```

Proof.

Lemma 6.2 gives \(\widehat\eta_{*,20}(s)<\tau_{20}(s)\). The map
\(\eta\mapsto20\eta/(1-\eta)\) is strictly increasing on \([0,1)\), hence

```math
{20\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}
<
{20\tau_{20}(s)\over1-\tau_{20}(s)}
=
L_{20}(s).
```

Exponentiating gives

```math
\exp\left(
{20\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}
\right)
<
\exp(L_{20}(s))
=
1+F_\rho(s).
```

This is exactly
\(\underline M_{loss}^{SEL2,20}(s)>0\). `square`

### Theorem 6.4: The Best-Case Adaptive `s`-Window Is Nonempty

Under the optimistic zero-debit probe,

```math
\mathcal W_{ad}^{0}(\rho)\ne\varnothing.
```

More explicitly, every \(s\) satisfying

```math
s>
{2(1+\log19+\log2)\over C_2(\rho)(1-\epsilon_A)(1-\chi)}
```

belongs to the time side of the adaptive window, and Lemmas 6.2--6.3 supply
the admissibility and zero-debit margin sides.

Proof.

Since \(0<F_\rho(s)<1\), one has

```math
0<L_{20}(s)<\log2.
```

By Lemma 6.2,

```math
{20\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}
<
L_{20}(s)
<
\log2.
```

Therefore the adaptive tree-time threshold at \(s\) is bounded above by

```math
{2(1+\log19+\log2)\over C_2(\rho)(1-\epsilon_A)(1-\chi)}.
```

Choosing \(s\) strictly larger than this constant gives the second line of
Definition 5.5. Lemma 6.2 gives the first line, and Lemma 6.3 gives the third
line when \(U_{pre13}^{SEL2}(s)=0\). Hence the optimistic adaptive window is
nonempty. `square`

### Corollary 6.5: Fundamental-Channel Benchmarks

With zero decoration, zero slack, and the fundamental representation of
`SU(N)`,

```math
C_2(F)={N^2-1\over2N},
```

the asymptotic tree-time lower endpoint is

```math
S_0(N)
:=
{2(1+\log19)\over C_2(F)}
=
{4N(1+\log19)\over N^2-1}.
```

Numerically,

```math
S_0(2)=10.5185\ldots,\qquad
S_0(3)=5.9167\ldots,\qquad
S_0(4)=4.2074\ldots.
```

Adding positive decoration activity or positive slacks only raises these lower
endpoints; adding actual nonsurface debit may also create a finite upper
endpoint through the signal decay.

### Corollary 6.6: Best-Case Probe Verdict

The strict reduced `SEL2` route is not killed by the \(s\)-window algebra under
the zero-nonsurface-debit optimistic probe. Thus Paper 21 should not spend the
next iteration optimizing \(s\) in the abstract. The next meaningful task is
to insert the actual carried upper envelope

```math
U_{pre13}^{SEL2}(s)
```

or a sharp enough lower floor for it. Only after that insertion does an
interior optimization problem become mathematically relevant.

## 7. Actual Carried Pre-Surface Envelope

The best-case probe deliberately erased nonsurface transport. The actual
strict reduced `SEL2` branch may not do that. Paper 20's active carried ledger
leaves six nonnegative buckets before the final surface-leading-rate test.
This section inserts those buckets into the Paper-21 \(s\)-window.

### Definition 7.1: Active Carried Nonsurface Envelope

On the same frozen `SEL2` scalar record law, and using the later reductions
carried out in Sections 8--15, define the active carried pre-surface envelope
by

```math
U_{pre13}^{car,SEL2}(s)
:=
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
```

```math
\qquad
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

The six terms have the following ledger homes:

```math
E_{14}^{park}
\quad\text{is the parked Paper-14 export debit;}
```

```math
16
\quad\text{is the certified endpoint/corner debit of Section 8;}
```

```math
X_{13}^{car,SEL2}
\quad\text{is the cutoff-to-exact/readout debit;}
```

```math
U_{12}^{red,car,SEL2}
=
U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+U_{12}^{smear,SEL2}
+U_{12}^{P12,SEL2}
+U_{12}^{appLC,SEL2}
+U_{12}^{binLC,SEL2};
```

```math
U_{11}^{act,SEL2}
=
U_{11}^{loc,SEL2}
+U_{11}^{RP,SEL2}
+U_{11}^{Cov,SEL2}
+U_{11}^{gauge,SEL2};
```

and

```math
U_{13}^{entry,act,SEL2}
=
U_{13}^{BC,car}
+U_{13}^{CE,car}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car}.
```

The reduced-branch `SUB` term is not included here; it is paid only in the
final surface-leading-rate inequality.

### Definition 7.2: Carried `s`-Window

Replace the abstract upper envelope \(U_{pre13}^{SEL2}(s)\) in Definition 5.5
by the active carried envelope \(U_{pre13}^{car,SEL2}(s)\). The carried
feasibility set is

```math
\mathcal W_{car}(\rho)
:=
\left\{
s>0:
\begin{array}{l}
0<\bar\eta_{res,20}(s)<\tau_{20}(s),\\[2mm]
s>
{2(1+\log19+
20\widehat\eta_{*,20}(s)/(1-\widehat\eta_{*,20}(s)))
\over C_2(\rho)(1-\epsilon_A)(1-\chi)},\\[3mm]
U_{pre13}^{car,SEL2}(s)<\underline M_{loss}^{SEL2,20}(s)
\end{array}
\right\}.
```

Equivalently, after the reduced \(T_{12}\) assembly, the third line is

```math
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s)
<
\underline M_{loss}^{SEL2,20}(s).
```

### Theorem 7.3: Carried-Envelope Pass Certificate

Assume the six carried buckets in Definition 7.1 are evaluated on the same
pushed-forward `SEL2` record law and that each is a genuine upper bound for
its corresponding Paper-20 nonsurface debit. Then the strict reduced branch is
certified to reach \(\mathrm{P21\text{-}ESC\text{-}MASS}\) whenever

```math
\mathcal W_{car}(\rho)\ne\varnothing.
```

If the six carried buckets are proved to be the exact same-record limsup
debits, then this criterion is exact. If they are only upper bounds, emptiness
of \(\mathcal W_{car}(\rho)\) means only that the current upper-bound package
does not certify passage; it is not a falsification without the lower-floor
test of Definition 7.4.

If the set is nonempty, any chosen

```math
s\in\mathcal W_{car}(\rho)
```

freezes a same-record branch with positive pre-surface margin

```math
\mathcal M_{pre13}^{car,SEL2}(s)
:=
\underline M_{loss}^{SEL2,20}(s)
-U_{pre13}^{car,SEL2}(s)>0.
```

Proof.

Definition 7.1 is exactly Paper 20's active post-entry carried ledger:
Paper-14 export, corner debit, exact-comparison/readout debit, reduced
loop-readout debit, reduced \(T_{11}\) debit, and exact-entry debit. The
third line of Definition 7.2 is therefore precisely the Paper-20 post-entry
surplus inequality. The first two lines are the same admissibility and
tree-time lines from Definition 5.5. Thus the conjunction certifies a positive
pre-surface margin on the same record law. If the inserted envelope equals the
actual limsup debit, the same algebra gives equivalence. `square`

### Definition 7.4: Matching Lower-Floor Falsifier

A matching lower-floor package is a nonnegative function
\(L_{pre13}^{-,SEL2}(s)\) such that the actual nonsurface debit on the same
branch satisfies

```math
L_{pre13}^{actual,SEL2}(s)
\ge
L_{pre13}^{-,SEL2}(s).
```

It is sharp enough to falsify the branch before escape when, for every
candidate \(s\) satisfying the first two lines of Definition 7.2,

```math
L_{pre13}^{-,SEL2}(s)
\ge
\underline M_{loss}^{SEL2,20}(s).
```

### Theorem 7.5: Lower-Floor Falsification Before Escape

If a matching lower-floor package satisfies the inequality of Definition 7.4
for every activity-admissible and tree-time-admissible \(s\), then the strict
reduced `SEL2` branch cannot reach the escape-mass gate, regardless of any
future improvement in \(\mathrm{P21\text{-}ESC\text{-}MASS}\).

Proof.

For every candidate \(s\), the actual nonsurface debit is at least
\(L_{pre13}^{-,SEL2}(s)\), hence at least
\(\underline M_{loss}^{SEL2,20}(s)\). The actual pre-surface margin is
therefore nonpositive. Since all later surface estimates are nonnegative
debits, no leading-rate or escape estimate can repair a failed pre-surface
margin on the same branch. `square`

### Corollary 7.6: Inserted-Envelope Verdict

Paper 21 has now inserted the actual carried envelope. The next step is no
longer abstract optimization. It is one of two concrete same-record tasks:

1. prove

   ```math
   \mathcal W_{car}(\rho)\ne\varnothing
   ```

   by sharpening the six carried upper buckets of Definition 7.1; or

2. prove the lower-floor falsifier of Definition 7.4.

Until one of these is done, the strict reduced `SEL2` route is undecided before
the escape-mass problem. The best-case Section 6 probe shows that the scalar
window itself is not the obstruction; the live obstruction is the size of the
actual carried nonsurface envelope.

## 8. Endpoint/Corner Debit Decision

The cheapest live carried term in Definition 7.1 is the endpoint/corner debit.
Paper 20 already reduced it to finite template bookkeeping:

```math
E_{corn}^{car,SEL2}
\le
(16+N_{conc}^{SEL2})v_{corn}^{max}.
```

This section freezes the active Paper-21 convention.

### Definition 8.1: Pure Rectangular-Corner Convention

The active Paper-21 `SEL2` branch uses the pure rectangular-corner convention:

1. the four Creutz slots are the four nondegenerate rectangles

   ```math
   (L_j,L_j),\quad
   (L_j-\sigma_j,L_j-\sigma_j),\quad
   (L_j-\sigma_j,L_j),\quad
   (L_j,L_j-\sigma_j);
   ```

2. each rectangular slot contributes only its four ordinary convex
   endpoint/corner occurrences to \(E_{corn}^{car,SEL2}\);
3. Creutz-overlap concave subtraction corners are not separately charged to
   \(E_{corn}^{car,SEL2}\); their signed local loop-readout effect remains in
   the reduced \(T_{12}\) ledger, through the cusp/app/readout terms already
   contained in \(U_{12}^{red,car,SEL2}\).

Thus no corner contribution is erased. The convention only prevents the same
local Creutz-overlap mismatch from being charged both as an endpoint/corner
template and again inside the reduced loop-readout bucket.

### Lemma 8.2: The Active Concave-Corner Count Is Zero

On the pure rectangular-corner convention,

```math
N_{conc}^{SEL2}=0.
```

Proof.

By Definition 8.1, the endpoint/corner register contains exactly the ordinary
convex endpoint/corner occurrences of the four nondegenerate rectangular
slots. Concave Creutz-overlap subtraction corners are assigned to the signed
loop-readout ledger, not to the endpoint/corner register. Therefore the number
of separately charged concave endpoint/corner occurrences is zero. `square`

### Definition 8.3: Certified Corner Weight

The active branch keeps Paper 20's standard unit-counted endpoint/corner
normalization:

```math
v_{corn}^{max}=1.
```

A smaller value

```math
v_{corn}^{max}\le v_*<1
```

is allowed only after a same-record normalization audit proving that every
endpoint/corner scalar transport weight \(v_\upsilon\) on the pushed-forward
`SEL2` record law obeys \(v_\upsilon\le v_*\). No such audit is currently
part of the Paper-20 import.

### Theorem 8.4: Active Endpoint/Corner Bound

On the active Paper-21 pure rectangular-corner unit-counted branch,

```math
0\le E_{corn}^{car,SEL2}\le16.
```

Moreover this is the current certified bound; Paper 21 may not replace it by
zero or by a smaller uniform number without one of the following additional
same-record audits:

```math
E_{corn}^{car,SEL2}=0
```

from a zero-weight or empty-template audit, or

```math
E_{corn}^{car,SEL2}\le16v_*
\qquad(0\le v_*<1)
```

from a sharper corner-weight normalization audit.

Proof.

Paper 20 Lemma 4.3A.93 gives sixteen ordinary convex endpoint/corner
occurrences for the four nondegenerate rectangular Creutz slots. Lemma 8.2
sets \(N_{conc}^{SEL2}=0\). Definition 8.3 sets \(v_{corn}^{max}=1\).
Substituting these into the finite-template bound of Paper 20 Theorem
4.3A.94 gives \(E_{corn}^{car,SEL2}\le16\). Nonnegativity is part of the
carried-debit convention. The final statement is Paper 20's zero decision
specialized to this convention: smaller or zero corner debit is not
bookkeeping; it requires a new same-record scalar audit. `square`

### Corollary 8.5: Updated Carried Envelope

For the active Paper-21 branch, the carried envelope of Definition 7.1 may be
bounded by

```math
U_{pre13}^{car,SEL2}(s)
\le
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

This is now the envelope to use in \(\mathcal W_{car}(\rho)\). It is still an
upper certificate, not a lower-floor falsifier.

## 9. Paper-14 Export Debit Parking

The next carried term is the Paper-14 whole-process finite-block export debit.
Paper 20 already investigated the zero route and found the honest fork: the
finite export ceiling is available, but zero requires the stronger nine-rate
component audit on the same `SEL2` tower. Paper 21 therefore freezes the
parked convention.

### Definition 9.1: Parked Paper-14 Export Constant

On the active Paper-21 branch, set

```math
E_{14}^{car,SEL2}
:=
E_{14}^{park},
```

where

```math
E_{14}^{park}
:=
E_{14}^{SEL2}
<\infty
```

is the same finite scalar exported by
\(\mathrm{P19\text{-}P14\text{-}EXPORT}(E_{14}^{SEL2})\) on the frozen
`SEL2` batteries.

This is a carried nonsurface debit. It is not part of the surface-polymer
entropy, not part of the endpoint/corner debit, and not part of the
coefficient escape-mass source.

### Definition 9.2: Paper-14 Zero Replacement Gate

The proposed replacement

```math
E_{14}^{park}\mapsto 0
```

is permitted only if the same frozen record law proves
\(\mathrm{P20\text{-}SEL2\text{-}P14\text{-}COMP}\), equivalently the
same-record Paper-14 export-zero audit whose component rates control:

```math
\text{identity},\quad
\text{projection},\quad
\text{coefficient-window},\quad
\text{representation-tail},
```

```math
\text{chart},\quad
\text{counterterm},\quad
\text{finite-volume},\quad
\text{covariance},\quad
\text{reflection-positivity},
```

together with a cofinal row-tail map \(n(j)\to\infty\).

Finite total Paper-14 export alone does not imply this zero gate.

### Theorem 9.3: No Silent Paper-14 Zero Spending

On the active Paper-21 branch,

```math
E_{14}^{car,SEL2}=E_{14}^{park}
```

must be carried in \(\mathcal W_{car}(\rho)\) unless the zero replacement gate
of Definition 9.2 is proved on the same pushed-forward scalar record law.

Proof.

Paper 20 Corollary 4.3A.91 parks the Paper-14 zero route behind the component
audit and defines \(E_{14}^{SEL2,park}:=E_{14}^{SEL2}<\infty\). Paper 20
Corollary 4.3A.90 states that the current source papers do not prove the
actual nine Paper-14 component estimates for four-dimensional `SU(N)` on the
active `SEL2` tower. Therefore the active Paper-21 branch may import the
finite carried ceiling, but it may not replace it by zero unless the component
audit is explicitly reopened and proved. `square`

### Corollary 9.4: Updated Envelope After Paper-14 Parking

With the endpoint/corner decision of Section 8 and the Paper-14 parked
convention of this section,

```math
U_{pre13}^{car,SEL2}(s)
\le
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

This is the active carried envelope for the next Paper-21 step. Any later
proof of \(\mathrm{P20\text{-}SEL2\text{-}P14\text{-}COMP}\) may delete
\(E_{14}^{park}\), but until then it remains an ordinary finite debit in the
pre-surface window.

## 10. Exact-Comparison Debit Decision

The next nonsurface debit is the cutoff-to-exact scalar comparison appearing in
the reduced `T_13` ledger. This section does not try to hide it inside the
surface-polymer rate, and it does not charge projective, chart, volume, or
Paper-14 terms a second time. It only measures whether the finite block-row
scalar records used by the exact-entry proof agree with their exact pushed-
forward limits.

### Definition 10.1: Rowwise Exact-Comparison Split

For the row-\(j\) exact-entry battery
\(B_{13,j}^{exact,SEL2}\), write

```math
B_{13,j}^{exact,SEL2}
=
B_{13,j}^{Creutz}
\cup
B_{13,j}^{conn}
\cup
B_{13,j}^{const},
```

where \(B_{13,j}^{Creutz}\) contains the four Creutz records,
\(B_{13,j}^{conn}\) contains the finite connected-entry records used by the
surface-entry proof, and \(B_{13,j}^{const}\) contains the scalar records used
to read the finite constants in the same-entry ledger.

Define

```math
D_{13,j}^{cut,SEL2}
:=
\sup_{F\in B_{13,j}^{exact,SEL2}}
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|
```

and

```math
R_{13,j}^{read,SEL2}
:=
\epsilon_{read,j}^{(13),SEL2}.
```

The exact-comparison row debit is

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
\right),
```

and the separated finite bounds are

```math
U_{13}^{cut,SEL2}
:=
\limsup_jD_{13,j}^{cut,SEL2},
\qquad
U_{13}^{read,SEL2}
:=
\limsup_jR_{13,j}^{read,SEL2}.
```

When the separated limsups are finite,

```math
X_{13}^{sharp,SEL2}
\le
U_{13}^{cut,SEL2}+U_{13}^{read,SEL2}.
```

### Definition 10.2: Zero And Carried-Bound Audits

The zero audit for the cutoff-to-exact component is
\(\mathrm{P20\text{-}SEL2\text{-}X13\text{-}BC0}\). It asserts that the
moving row batteries \(B_{13,j}^{exact,SEL2}\) are finite before the cutoff is
chosen, use the same pushed-forward scalar law as the transport common-record
audit, and admit a diagonal cutoff choice such that

```math
D_{13,j}^{cut,SEL2}\to0.
```

The zero audit for the readout component is
\(\mathrm{P20\text{-}SEL2\text{-}X13\text{-}READ0}\). It asserts that the
scalar records are read exactly on a cofinal tail, equivalently

```math
R_{13,j}^{read,SEL2}\to0.
```

The carried-bound alternatives are

```math
\limsup_jD_{13,j}^{cut,SEL2}
\le
U_{13}^{cut,SEL2}
<\infty,
\qquad
\limsup_jR_{13,j}^{read,SEL2}
\le
U_{13}^{read,SEL2}
<\infty.
```

### Theorem 10.3: Exact-Comparison Zero Or Carried Bound

On the active `SEL2` scalar record law:

1. If
   \(\mathrm{P20\text{-}SEL2\text{-}X13\text{-}BC0}\) and
   \(\mathrm{P20\text{-}SEL2\text{-}X13\text{-}READ0}\) both hold, then

   ```math
   X_{13}^{sharp,SEL2}=0.
   ```

2. If only the separated finite bounds of Definition 10.2 hold, then

   ```math
   X_{13}^{sharp,SEL2}
   \le
   U_{13}^{cut,SEL2}+U_{13}^{read,SEL2}.
   ```

Proof.

Definition 10.1 gives the rowwise identity

```math
X_{13,j}^{exact,SEL2}
=
D_{13,j}^{cut,SEL2}
+R_{13,j}^{read,SEL2}.
```

If both summands tend to zero, the limsup is zero. If only finite component
limsups are available, limsup subadditivity gives the displayed carried bound.
`square`

### Corollary 10.4: Active Paper-21 `X_13` Convention

Current Paper-13/Paper-19 imports do not by themselves prove
\(\mathrm{P20\text{-}SEL2\text{-}X13\text{-}BC0}\) on the moving `SEL2`
exact-entry batteries. Therefore Paper 21 may not spend
\(X_{13}^{car,SEL2}\) as zero unless that diagonal moving-battery convergence
audit is supplied.

The active carried value is fixed by the priority rule

```math
X_{13}^{car,SEL2}
:=
\begin{cases}
0,
&
\mathrm{P20\text{-}SEL2\text{-}X13\text{-}BC0}
\ \text{and}\
\mathrm{P20\text{-}SEL2\text{-}X13\text{-}READ0}
\ \text{are proved},
\\[4pt]
X_{13}^{sharp,SEL2},
&
\text{if the sharp rowwise limsup is directly evaluated},
\\[4pt]
U_{13}^{cut,SEL2}+U_{13}^{read,SEL2},
&
\text{if only separated component bounds are proved}.
\end{cases}
```

In all cases the branch must satisfy

```math
0
\le
X_{13}^{exact,SEL2}
\le
X_{13}^{car,SEL2}
<\infty.
```

Thus the envelope used in \(\mathcal W_{car}(\rho)\) is now

```math
U_{pre13}^{car,SEL2}(s)
\le
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

The exact-comparison debit is therefore attacked, but not annihilated. Zero is
a theorem only after the same-record moving-battery convergence and exact
readout audits are proved.

## 11. Executing The `X_13` Audit

This section carries out the five remaining `X_13` steps. The result is
deliberately sharp: the scalar readout half can be zeroed on the strict exact
record branch, while the cutoff-to-exact half remains a moving-battery
convergence source unless a diagonal block-limit uniqueness estimate is proved.

### Definition 11.1: Frozen Exact-Entry Battery

For each row \(j\), freeze the exact-entry battery before choosing the cutoff
\(a_j\):

```math
B_{13,j}^{exact,SEL2}
:=
B_{13,j}^{Creutz}
\cup
B_{13,j}^{conn}
\cup
B_{13,j}^{const}.
```

The three parts are:

```math
B_{13,j}^{Creutz}
:=
\{W(C_{RT}),W(C_{R-\sigma,T-\sigma}),
  W(C_{R-\sigma,T}),W(C_{R,T-\sigma})\}_{j,SEL2},
```

the four scalar closed-loop records used by the centered Creutz slot;

```math
B_{13,j}^{conn}
:=
\{F_{j,\alpha}^{conn}:1\le\alpha\le n_{conn}(j)\},
```

the finite connected-entry products used by the row-\(j\) surface-entry proof;
and

```math
B_{13,j}^{const}
:=
\{u_{\rho,s_0,j},A_{C,j},B_{C,j},\xi_{C,j},
  \xi'_{C,j},N_j(C): C\in\mathcal C_j^{Creutz}\}.
```

Every element of \(B_{13,j}^{exact,SEL2}\) is a scalar record observable on the
same pushed-forward whole-process law. Gauge-fixed fields, partial transition
kernels, projective drift, chart drift, finite-volume exhaustion, and Paper-14
export errors are excluded by ledger assignment.

The row battery is finite:

```math
|B_{13,j}^{exact,SEL2}|
\le
4+n_{conn}(j)+6|\mathcal C_j^{Creutz}|
<\infty.
```

### Lemma 11.2: Exact Scalar Readout Closes The Readout Half

On the strict exact scalar-record branch,

```math
R_{13,j}^{read,SEL2}=0
```

for every sufficiently large \(j\). Hence

```math
\mathrm{P20\text{-}SEL2\text{-}X13\text{-}READ0}
```

holds and

```math
U_{13}^{read,SEL2}=0.
```

Proof.

By Definition 11.1, the constants entering \(B_{13,j}^{const}\) are included as
scalar records, not reconstructed from an external mesh. On the strict exact
record branch the readout map is evaluation of those declared records under the
same pushed-forward law. Therefore the finite readout tolerance
\(\epsilon_{read,j}^{(13),SEL2}\) is identically zero on the cofinal tail, which
is exactly \(R_{13,j}^{read,SEL2}=0\). `square`

If a later operational branch replaces exact scalar records by finite meshes,
Lemma 11.2 is not available. Then the paper must carry
\(U_{13}^{read,SEL2}\) from Definition 10.2.

### Definition 11.3: Diagonal Moving-Battery Block Convergence

Let

```math
D_{13,j}^{cut,SEL2}
:=
\sup_{F\in B_{13,j}^{exact,SEL2}}
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|.
```

The diagonal moving-battery convergence gate
\(\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}\) asserts that the exact block
law \(\mu_{s_0}^{blk,SEL2}\) is the unique subsequential block limit on every
row battery and that the cutoff sequence can be chosen so that

```math
D_{13,j}^{cut,SEL2}\to0.
```

Equivalently, for every \(\varepsilon>0\) there are cutoffs \(a_j\downarrow0\)
with

```math
\sup_{F\in B_{13,j}^{exact,SEL2}}
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|
<\varepsilon
```

for all sufficiently large \(j\).

### Lemma 11.4: Fixed-Battery Convergence Does Not Imply The Moving Gate

The fixed finite-battery convergence supplied by Paper 13 Theorem 7.30AC does
not, by itself, prove
\(\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}\).

Proof.

The point is purely logical. Consider scalar records \(f_n\) on a compact
record space with two states \(\omega_j\) and \(\omega_\infty\) such that

```math
\omega_j(f_n)\to\omega_\infty(f_n)
```

for every fixed \(n\), but

```math
\sup_{1\le n\le j}
|\omega_j(f_n)-\omega_\infty(f_n)|
\not\to0.
```

For example, on the compact product space \(\{0,1\}^{\mathbb N}\), let
\(\omega_\infty\) be the point mass at the all-zero sequence, let \(\omega_j\)
be the point mass at the sequence whose only nonzero coordinate is \(j\), and
let \(f_n(x)=x_n\). Then every fixed coordinate converges to zero, but the
moving battery \(\{f_1,\ldots,f_j\}\) has supremum discrepancy \(1\) for every
\(j\).

Paper 13 Theorem 7.30AC converts compactness plus uniqueness into convergence
on a declared finite battery. It does not provide a uniform rate over a battery
whose contents grow with \(j\). Therefore the moving-battery diagonal estimate
of Definition 11.3 is an additional same-record source estimate, not a formal
consequence of fixed-battery convergence. `square`

### Theorem 11.5: `X_13` Decision On The Active Branch

On the strict exact scalar-record branch, Lemma 11.2 gives
\(U_{13}^{read,SEL2}=0\). Therefore:

1. If \(\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}\) is proved, then

   ```math
   X_{13}^{car,SEL2}=0.
   ```

2. If instead one proves a finite cutoff-to-exact ceiling

   ```math
   \limsup_jD_{13,j}^{cut,SEL2}
   \le
   U_{13}^{cut,SEL2}
   <\infty,
   ```

   then the active carried value is

   ```math
   X_{13}^{car,SEL2}=U_{13}^{cut,SEL2}.
   ```

3. Without either a zero gate or a finite ceiling, the carried-window branch is
   not certified because \(X_{13}^{car,SEL2}<\infty\) has not been supplied.

Proof.

By Lemma 11.2, \(R_{13,j}^{read,SEL2}=0\) cofinally. Hence

```math
X_{13,j}^{exact,SEL2}
=
D_{13,j}^{cut,SEL2}
```

on the strict exact branch. Clause 1 is Definition 11.3 plus Corollary 10.4.
Clause 2 is the carried-bound alternative of Corollary 10.4 with
\(U_{13}^{read,SEL2}=0\). Clause 3 is the admissibility condition
\(X_{13}^{car,SEL2}<\infty\) from Corollary 10.4. `square`

### Corollary 11.6: Carried Window After Executing `X_13`

After executing the `X_13` audit, the active carried envelope is

```math
U_{pre13}^{car,SEL2}(s)
\le
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s),
```

with

```math
X_{13}^{car,SEL2}
=
\begin{cases}
0,
&
\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}\ \text{is proved},
\\[4pt]
U_{13}^{cut,SEL2},
&
\limsup_jD_{13,j}^{cut,SEL2}
\le U_{13}^{cut,SEL2}<\infty\ \text{is proved}.
\end{cases}
```

Thus \(\mathcal W_{car}(\rho)\) is updated by replacing the previous formal
\(X_{13}^{car,SEL2}\) slot with the actual zero-or-carried cutoff convergence
decision above. The exact-readout half is closed on the strict scalar-record
branch; the moving-battery cutoff convergence half remains the real `X_13`
source.

## 12. Reduced `T_12`: Signed Creutz Slots And Perimeter/Cusp Cancellation

With `X_13` reduced to a readout-closed moving-battery source, the next
cheapest nonsurface terms are the calibrated perimeter and cusp transports in
the reduced `T_12` bucket. This section freezes the four signed Creutz slots and
decides exactly when the perimeter/cusp debit vanishes.

### Definition 12.1: Frozen Four-Slot Creutz Row

For the active `SEL2` row \(j\), freeze the four nondegenerate rectangular
closed-loop records

```math
C_{++}:=C(L_j,L_j),
\qquad
C_{--}:=C(L_j-\sigma_j,L_j-\sigma_j),
```

```math
C_{+-}:=C(L_j,L_j-\sigma_j),
\qquad
C_{-+}:=C(L_j-\sigma_j,L_j),
```

with

```math
L_j>\sigma_j>0
```

on the cofinal tail. The signed Creutz coefficients are

```math
s_{++}=s_{--}=+1,
\qquad
s_{+-}=s_{-+}=-1.
```

The signed scalar Creutz record is

```math
\Xi_j^{SEL2}
:=
\sum_{\alpha\in\{++,--,+-,-+\}}
s_\alpha\,
W_\rho(C_\alpha).
```

The four records are read on the same pushed-forward scalar law, use the same
representation \(\rho\), the same block scale \(s_0\), and the same Paper-12
perimeter/cusp calibration branches. Projective, chart, finite-volume,
Paper-14, endpoint/corner, smearing, and loop-approximant debits are excluded
from this reduced perimeter/cusp slot and remain in their assigned buckets.

### Definition 12.2: Signed Perimeter And Cusp Residuals

Define the signed perimeter residual

```math
\Pi_j^{per}
:=
\left|
\sum_{\alpha\in\{++,--,+-,-+\}}
s_\alpha\,{\rm Per}(C_\alpha)
\right|.
```

For each cusp angle \(\theta\), let \(n_\alpha(\theta)\) be the number of cusps
of angle \(\theta\) in \(C_\alpha\). Define

```math
\Pi_j^{cusp}
:=
\sum_{\theta}
\left|
\sum_{\alpha\in\{++,--,+-,-+\}}
s_\alpha\,n_\alpha(\theta)
\right|.
```

The same-record perimeter/cusp cancellation audit
\(\mathrm{P21\text{-}T12\text{-}PC\text{-}CANCEL}\) asserts:

1. the four slots of Definition 12.1 use the same Paper-12 calibrated
   perimeter and cusp counterterm branches;
2. the perimeter/cusp `T_12` contribution is only the signed scalar Creutz
   record \(\Xi_j^{SEL2}\);
3. no residual perimeter/cusp mismatch is assigned to this bucket after
   endpoint/corner, loop-approximant, smearing, projective, chart, volume, and
   Paper-14 debits have been removed.

This audit is a scalar-record statement. It does not zero \(E_{corn}^{car,SEL2}\)
and does not affect \(E_{14}^{park}\).

### Lemma 12.3: Four-Slot Geometry Cancels Perimeter And Cusps

For the frozen rectangular Creutz row of Definition 12.1,

```math
\Pi_j^{per}=0,
\qquad
\Pi_j^{cusp}=0.
```

Proof.

For a rectangle \(C(R,S)\),

```math
{\rm Per}(C(R,S))=2R+2S.
```

Therefore

```math
\begin{aligned}
&{\rm Per}(C(L_j,L_j))
+{\rm Per}(C(L_j-\sigma_j,L_j-\sigma_j))\\
&\quad
-{\rm Per}(C(L_j,L_j-\sigma_j))
-{\rm Per}(C(L_j-\sigma_j,L_j))
=0.
\end{aligned}
```

Each frozen slot is a nondegenerate rectangle with exactly four right-angle
cusps and no other cusp angle in the scalar perimeter/cusp counterterm ledger.
The signed right-angle cusp count is

```math
4+4-4-4=0,
```

and every other angle contributes zero in all four slots. Thus
\(\Pi_j^{cusp}=0\). `square`

### Definition 12.4: Perimeter/Cusp Tail Bounds

Let \(\eta_{perLC,j,k}^{SEL2}\) and
\(\eta_{cuspLC,j,k}^{SEL2}\) be the reduced Paper-12 loop-continuity tails for
the signed perimeter and cusp counterterm transports, with \(k\ge j\). A finite
carried-bound audit
\(\mathrm{P21\text{-}T12\text{-}PC\text{-}BOUND}
(U_{12}^{per,SEL2},U_{12}^{cusp,SEL2})\) asserts that there are nonnegative
row-shell bounds \(b_{per,j,k}^{SEL2}\) and \(b_{cusp,j,k}^{SEL2}\) such that

```math
\eta_{perLC,j,k}^{SEL2}\le b_{per,j,k}^{SEL2},
\qquad
\eta_{cuspLC,j,k}^{SEL2}\le b_{cusp,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{per,j,k}^{SEL2}
\le
U_{12}^{per,SEL2}
<\infty,
```

```math
\limsup_j\sum_{k\ge j}b_{cusp,j,k}^{SEL2}
\le
U_{12}^{cusp,SEL2}
<\infty.
```

The zero-strength audit
\(\mathrm{P21\text{-}T12\text{-}PC\text{-}ZERO}\) asserts

```math
\sum_{k\ge j}b_{per,j,k}^{SEL2}\to0,
\qquad
\sum_{k\ge j}b_{cusp,j,k}^{SEL2}\to0.
```

A source-realized sufficient form is

```math
b_{per,j,k}^{SEL2}
=
\Pi_j^{per}v_{per,j,k}^{SEL2}+r_{per,j,k}^{SEL2},
```

```math
b_{cusp,j,k}^{SEL2}
=
\Pi_j^{cusp}v_{cusp,j,k}^{SEL2}+r_{cusp,j,k}^{SEL2},
```

where the \(v\)-terms measure the one-shell variation of the calibrated
Paper-12 perimeter/cusp branches and the residuals \(r_{per},r_{cusp}\) are
allowed only for explicitly declared perimeter/cusp mismatch not already
assigned to \(U_{12}^{app}\), \(E_{corn}^{car,SEL2}\), \(U_{11}^{act}\), or
\(E_{14}^{park}\).

### Theorem 12.5: Perimeter/Cusp Debit Is Zero Or Carried

On the active `SEL2` scalar record law:

1. If
   \(\mathrm{P21\text{-}T12\text{-}PC\text{-}BOUND}
   (U_{12}^{per,SEL2},U_{12}^{cusp,SEL2})\) holds, then

   ```math
   U_{12}^{per,SEL2}
   \quad\text{and}\quad
   U_{12}^{cusp,SEL2}
   ```

   are admissible finite carried ceilings for the reduced perimeter/cusp
   transport slots.

2. If \(\mathrm{P21\text{-}T12\text{-}PC\text{-}ZERO}\) holds, then

   ```math
   U_{12}^{per,SEL2}=U_{12}^{cusp,SEL2}=0.
   ```

3. In particular, \(\mathrm{P21\text{-}T12\text{-}PC\text{-}CANCEL}\), Lemma
   12.3, and

   ```math
   r_{per,j,k}^{SEL2}=r_{cusp,j,k}^{SEL2}=0
   ```

   on a cofinal tail imply

   ```math
   \sum_{k\ge j}\eta_{perLC,j,k}^{SEL2}\to0,
   \qquad
   \sum_{k\ge j}\eta_{cuspLC,j,k}^{SEL2}\to0,
   ```

   hence the reduced perimeter/cusp debit vanishes.

Proof.

Paper 20 Theorem 4.3A.104 identifies the reduced `SEL2` perimeter and cusp
entries with the limsups of the two displayed `HK-LC-TRANSPORT` tails. The
finite bounds in Definition 12.4 dominate those tails shell by shell, so the
carried ceilings in clause 1 follow by limsup monotonicity.

Clause 2 is the zero-tail specialization. For clause 3, Lemma 12.3 gives
\(\Pi_j^{per}=\Pi_j^{cusp}=0\). If the four slots use the same Paper-12
calibration branches and no unassigned residuals remain, then the source-
realized bounds \(b_{per,j,k}^{SEL2}\) and \(b_{cusp,j,k}^{SEL2}\) vanish on a
cofinal tail. Thus the perimeter/cusp transport sums vanish. `square`

### Corollary 12.6: Envelope After Perimeter/Cusp Attack

After steps 1--2 of the reduced `T_12` attack,

```math
U_{12}^{red,SEL2}(s)
=
U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+U_{12}^{smear,SEL2}(s)
+U_{12}^{P12,SEL2}(s)
+U_{12}^{appLC,SEL2}(s)
+U_{12}^{binLC,SEL2}(s).
```

On the strict same-record calibrated Creutz branch of Theorem 12.5 clause 3,
this reduces to

```math
U_{12}^{red,SEL2}(s)
=
U_{12}^{smear,SEL2}(s)
+U_{12}^{P12,SEL2}(s)
+U_{12}^{appLC,SEL2}(s)
+U_{12}^{binLC,SEL2}(s).
```

If the calibration-cancellation audit is not proved, the two finite carried
terms \(U_{12}^{per,SEL2}\) and \(U_{12}^{cusp,SEL2}\) remain in
\(\mathcal W_{car}(\rho)\). Geometry alone cancels the formal perimeter and
cusp counts; it does not by itself prove the same-record transport tails vanish
unless the Paper-12 calibration residuals are also controlled.

## 13. Reduced `T_12`: Smearing-Removal Debit

The next reduced `T_12` term is the smearing-removal debit. It is cheaper than
the loop-approximant/readout bucket because it has only two honest branches:
either the active scalar records are already exact renormalized unsmeared loop
records, or Paper 12 must supply a collar-safe de-smearing tail.

### Definition 13.1: Smearing Battery And Collar Window

Let \(B_{12,j}^{smear,SEL2}\) be the finite row-\(j\) loop battery on which the
reduced smearing-removal comparison is used. It contains only the scalar closed
loop records and finite products needed by the reduced `T_12` smearing slot.
It does not contain projective, chart, finite-volume, endpoint/corner,
Paper-14, or exact-entry records.

Let \(r_{min,j}^{SEL2}>0\) be the minimum admissible separation in this finite
battery: the minimum distance between distinct nonadjacent arcs, distinct loops
in any tested product, and nonincident cusp collars. Let \(c_{sm}\) be the
fixed support constant of the gauge-covariant smearing kernel.

The collar-safe smearing audit
\(\mathrm{P21\text{-}T12\text{-}SMEAR\text{-}COL}\) asserts that for \(k\ge j\)
there are smearing radii \(\tau_{j,k}^{SEL2}\) such that

```math
a_k\ll \tau_{j,k}^{SEL2},
\qquad
c_{sm}\tau_{j,k}^{SEL2}
\le {1\over4}r_{min,j}^{SEL2},
\qquad
\tau_{j,k}^{SEL2}\to0
```

as \(k\to\infty\), and that the same Paper-12 perimeter/cusp calibration
branches fixed in Section 12 are used. Thus the smearing kernel stays inside
the declared loop collars and cannot mix distinct nonadjacent arcs, distinct
loops, or nonincident cusp collars.

### Definition 13.2: Smearing Tail Bound

Assume \(\mathrm{P21\text{-}T12\text{-}SMEAR\text{-}COL}\). For each row-shell
pair \(k\ge j\), define the finite-row Paper-12 smearing modulus

```math
\Delta_{sm,j,k}^{SEL2}
:=
\max_{\alpha\in B_{12,j}^{smear,SEL2}}
\left(
\epsilon_{\alpha}^{cal}(\tau_{j,k}^{SEL2})
+\Omega_{\alpha}(\tau_{j,k}^{SEL2})
\right),
```

where \(\epsilon_{\alpha}^{cal}\) is the smeared-versus-unsmeared calibration
error and \(\Omega_\alpha\) is the renormalized connected-cluster convergence
modulus from Paper 12 Definition 3.11.

The carried-bound audit
\(\mathrm{P21\text{-}T12\text{-}SMEAR\text{-}BOUND}
(U_{12}^{smear,SEL2})\) asserts that there are nonnegative row-shell bounds
\(b_{smear,j,k}^{SEL2}\) such that

```math
\eta_{smearLC,j,k}^{SEL2}
\le
b_{smear,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{smear,j,k}^{SEL2}
\le
U_{12}^{smear,SEL2}
<\infty.
```

A source-realized bound has the form

```math
b_{smear,j,k}^{SEL2}
=
w_{sm,j,k}^{SEL2}\Delta_{sm,j,k}^{SEL2}
+r_{sm,j,k}^{SEL2},
```

where \(w_{sm,j,k}^{SEL2}\) is the finite product/cumulant multiplicity in the
row battery and \(r_{sm,j,k}^{SEL2}\) is allowed only for explicitly declared
smearing-readout mismatch not assigned to \(U_{12}^{app}\),
\(E_{corn}^{car,SEL2}\), \(U_{11}^{act}\), or \(E_{14}^{park}\).

The zero-strength audit
\(\mathrm{P21\text{-}T12\text{-}SMEAR\text{-}ZERO}\) asserts

```math
\sum_{k\ge j}b_{smear,j,k}^{SEL2}\to0.
```

### Lemma 13.3: Exact Unsmeared Records Give Zero Smearing Debit

If the active `SEL2` branch reads exact renormalized unsmeared scalar loop
records directly on \(B_{12,j}^{smear,SEL2}\), and no positive-smearing
intermediate is used in the reduced `T_12` smearing slot, then

```math
U_{12}^{smear,SEL2}=0.
```

Proof.

Under this strict convention the record compared by the reduced smearing slot
is already the target renormalized unsmeared scalar record. Therefore there is
no smeared-minus-unsmeared replacement in this bucket:
\(\eta_{smearLC,j,k}^{SEL2}=0\) on the cofinal tail. The limsup of the row-tail
sum is zero. `square`

### Lemma 13.4: Collar-Safe De-Smearing Gives Zero Under A Diagonal Tail

Assume \(\mathrm{P21\text{-}T12\text{-}SMEAR\text{-}COL}\). If the smearing
radii can be chosen so that

```math
w_{sm,j,k}^{SEL2}\Delta_{sm,j,k}^{SEL2}
+r_{sm,j,k}^{SEL2}
\le
2^{-(j+k)}
```

for all \(k\ge j\) on a cofinal tail, then

```math
\sum_{k\ge j}\eta_{smearLC,j,k}^{SEL2}\to0,
```

and hence \(U_{12}^{smear,SEL2}=0\).

Proof.

Paper 12 Definition 3.11 and Theorem 3.12 bound the smeared-versus-unsmeared
finite-row difference by
\(\epsilon_{\alpha}^{cal}(\tau)+\Omega_\alpha(\tau)\), provided the smearing
support stays in the clean collar window. Definition 13.1 supplies that collar
window, and Definition 13.2 turns the Paper-12 modulus into a row-shell bound.
The displayed diagonal choice gives

```math
\sum_{k\ge j}b_{smear,j,k}^{SEL2}
\le
\sum_{k\ge j}2^{-(j+k)}
\le
2^{-2j+1}
\to0.
```

Since \(\eta_{smearLC,j,k}^{SEL2}\le b_{smear,j,k}^{SEL2}\), the smearing tail
vanishes. `square`

### Theorem 13.5: Smearing Debit Is Zero Or Carried

On the active `SEL2` scalar record law:

1. If Lemma 13.3 applies, then

   ```math
   U_{12}^{smear,SEL2}=0.
   ```

2. If Lemma 13.4 applies, then again

   ```math
   U_{12}^{smear,SEL2}=0.
   ```

3. If only
   \(\mathrm{P21\text{-}T12\text{-}SMEAR\text{-}BOUND}
   (U_{12}^{smear,SEL2})\) is proved, then \(U_{12}^{smear,SEL2}\) remains as a
   finite carried debit.

4. If neither a zero audit nor a finite carried-bound audit is supplied, the
   carried-window branch is not certified at the smearing step.

Proof.

Clauses 1 and 2 are Lemmas 13.3 and 13.4. Clause 3 is Definition 13.2 and the
Paper-20/Paper-19 identification of the smearing entry with
\(\limsup_j\sum_{k\ge j}\eta_{smearLC,j,k}^{SEL2}\). Clause 4 is the
admissibility requirement that every live term in
\(\mathcal W_{car}(\rho)\) be finite. `square`

### Corollary 13.6: Envelope After Smearing Attack

After the smearing attack,

```math
U_{12}^{red,SEL2}(s)
=
U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+U_{12}^{smear,SEL2}
+U_{12}^{P12,SEL2}(s)
+U_{12}^{appLC,SEL2}(s)
+U_{12}^{binLC,SEL2}(s).
```

On the strict branch where Sections 12 and 13 both zero their terms,

```math
U_{12}^{red,SEL2}(s)
=
U_{12}^{P12,SEL2}(s)
+U_{12}^{appLC,SEL2}(s)
+U_{12}^{binLC,SEL2}(s).
```

Thus the only reduced `T_12` terms still live on the strict scalar branch are
the Paper-12 residual loop modulus, loop-approximant replacement, and finite
record-binning tails.

## 14. Reduced `T_12`: Loop Approximant And Readout Bucket

The last reduced `T_12` bucket is the loop approximant/readout debit. It splits
into three independent scalar tails:

```math
U_{12}^{app,SEL2}
=
U_{12}^{P12,SEL2}
+U_{12}^{appLC,SEL2}
+U_{12}^{binLC,SEL2}.
```

They are, respectively, the residual Paper-12 loop-modulus/connected-tail loss,
the loop representative replacement loss, and the finite scalar record
binning/battery-restriction loss. None of these terms contains perimeter/cusp,
smearing, endpoint/corner, Paper-14 export, projective, chart, finite-volume,
reflection-positivity, or covariance debit.

### Definition 14.1: Three App/Readout Tails

On the frozen `SEL2` scalar record law, define

```math
L_{12}^{P12,SEL2}
:=
\limsup_j
\sum_{k\ge j}\eta_{P12,j,k}^{SEL2},
```

```math
L_{12}^{appLC,SEL2}
:=
\limsup_j
\sum_{k\ge j}
\eta_{appLC,j,k}^{(12),SEL2},
```

and

```math
L_{12}^{binLC,SEL2}
:=
\limsup_j
\sum_{k\ge j}
\eta_{binLC,j,k}^{(12),SEL2}.
```

The reduced loop-app/readout entry is bounded by

```math
U_{12}^{app,SEL2}
\le
L_{12}^{P12,SEL2}
+L_{12}^{appLC,SEL2}
+L_{12}^{binLC,SEL2}.
```

### Definition 14.2: Paper-12 Residual Modulus Tail

The finite-bound audit
\(\mathrm{P21\text{-}T12\text{-}P12\text{-}BOUND}
(U_{12}^{P12,SEL2})\) asserts that there are nonnegative row-shell bounds
\(b_{P12,j,k}^{SEL2}\) such that

```math
\eta_{P12,j,k}^{SEL2}
\le
b_{P12,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{P12,j,k}^{SEL2}
\le
U_{12}^{P12,SEL2}
<\infty.
```

A source-realized bound has the form

```math
b_{P12,j,k}^{SEL2}
=
\theta_{P12,j,k}^{tail,SEL2}
+\theta_{P12,j,k}^{conn,SEL2},
```

where \(\theta_{P12}^{tail}\) is the omitted Paper-12 AF loop-variation tail
after the finite-battery modulus is extracted, and \(\theta_{P12}^{conn}\) is
the remaining connected-polymer tail on the same admissible loop stratum.

The zero-strength audit
\(\mathrm{P21\text{-}T12\text{-}P12\text{-}ZERO}\) asserts

```math
\sum_{k\ge j}b_{P12,j,k}^{SEL2}\to0.
```

### Definition 14.3: Loop Representative Replacement Tail

Let \(\ell_{j,k}^{SEL2}\) be the declared level-\(k\) lattice/block
representative map for loops in the finite row battery \(B_{12,j}^{app,SEL2}\),
and set

```math
\delta_{app,j,k}^{SEL2}
:=
\sup_{\alpha\in B_{12,j}^{app,SEL2}}
d_{adm}^{(m)}
(\alpha,\ell_{j,k}^{SEL2}\alpha).
```

The finite-bound audit
\(\mathrm{P21\text{-}T12\text{-}APPLC\text{-}BOUND}
(U_{12}^{appLC,SEL2})\) asserts that there are nonnegative bounds
\(b_{appLC,j,k}^{SEL2}\) such that

```math
\eta_{appLC,j,k}^{(12),SEL2}
\le
b_{appLC,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{appLC,j,k}^{SEL2}
\le
U_{12}^{appLC,SEL2}
<\infty.
```

A source-realized bound is

```math
b_{appLC,j,k}^{SEL2}
=
\omega_j(\delta_{app,j,k}^{SEL2})
+\epsilon_{app,j,k}^{(12),SEL2},
```

where \(\omega_j\) is the finite-row Paper-12 renormalized loop modulus and
\(\epsilon_{app}^{(12)}\) is the representative equivariance defect inside the
reduced loop-readout slot.

The zero-strength audit
\(\mathrm{P21\text{-}T12\text{-}APPLC\text{-}ZERO}\) asserts

```math
\sum_{k\ge j}b_{appLC,j,k}^{SEL2}\to0.
```

Pointwise representative refinement for each fixed row is not enough; the row
tail must vanish cofinally.

### Definition 14.4: Finite Scalar Binning Tail

Let \(Q_{j,k}^{SEL2}\) be the scalar finite-record binning map used for the
row-\(j\) loop-readout battery at shell \(k\), and let

```math
\beta_{bin,j,k}^{SEL2}
:=
\sup_{F\in B_{12,j}^{app,SEL2}}
\|F-Q_{j,k}^{SEL2}F\|_\infty.
```

The finite-bound audit
\(\mathrm{P21\text{-}T12\text{-}BINLC\text{-}BOUND}
(U_{12}^{binLC,SEL2})\) asserts that there are nonnegative bounds
\(b_{binLC,j,k}^{SEL2}\) such that

```math
\eta_{binLC,j,k}^{(12),SEL2}
\le
b_{binLC,j,k}^{SEL2},
```

and

```math
\limsup_j\sum_{k\ge j}b_{binLC,j,k}^{SEL2}
\le
U_{12}^{binLC,SEL2}
<\infty.
```

A source-realized bound is

```math
b_{binLC,j,k}^{SEL2}
=
\nu_j(\beta_{bin,j,k}^{SEL2})
+\epsilon_{bin,j,k}^{(12),SEL2},
```

where \(\nu_j\) is the finite-row scalar readout modulus and
\(\epsilon_{bin}^{(12)}\) is the declared battery-restriction defect.

The zero-strength audit
\(\mathrm{P21\text{-}T12\text{-}BINLC\text{-}ZERO}\) asserts

```math
\sum_{k\ge j}b_{binLC,j,k}^{SEL2}\to0.
```

Again, bin refinement on each fixed row does not suffice without a cofinal
moving-row tail estimate.

### Lemma 14.5: Exact Scalar-Record Conventions Zero The App/Readout Bucket

On the strict exact scalar-record branch, if:

1. the finite row battery uses exact renormalized loop records in the Paper-12
   admissible loop metric;
2. the loop representatives are the declared records themselves, so
   \(\delta_{app,j,k}^{SEL2}=0\) and
   \(\epsilon_{app,j,k}^{(12),SEL2}=0\) cofinally;
3. the scalar readout is exact, so
   \(\beta_{bin,j,k}^{SEL2}=0\) and
   \(\epsilon_{bin,j,k}^{(12),SEL2}=0\) cofinally;
4. the residual Paper-12 AF loop-variation and connected tails are truncated
   diagonally so that

   ```math
   \sum_{k\ge j}b_{P12,j,k}^{SEL2}\to0,
   ```

then

```math
U_{12}^{P12,SEL2}
=
U_{12}^{appLC,SEL2}
=
U_{12}^{binLC,SEL2}
=0.
```

Proof.

Clauses 2 and 3 make the source-realized bounds in Definitions 14.3 and 14.4
vanish on a cofinal tail. Clause 4 is exactly
\(\mathrm{P21\text{-}T12\text{-}P12\text{-}ZERO}\). Therefore all three
component row-tail sums vanish. `square`

### Theorem 14.6: App/Readout Bucket Is Zero Or Carried

On the active `SEL2` scalar record law:

1. If the three zero-strength audits

   ```math
   \mathrm{P21\text{-}T12\text{-}P12\text{-}ZERO},
   \quad
   \mathrm{P21\text{-}T12\text{-}APPLC\text{-}ZERO},
   \quad
   \mathrm{P21\text{-}T12\text{-}BINLC\text{-}ZERO}
   ```

   hold, then

   ```math
   U_{12}^{app,SEL2}=0.
   ```

2. If only the finite component bounds of Definitions 14.2--14.4 are proved,
   then

   ```math
   U_{12}^{app,SEL2}
   \le
   U_{12}^{P12,SEL2}
   +U_{12}^{appLC,SEL2}
   +U_{12}^{binLC,SEL2}.
   ```

3. If any of the three component bounds is not finite, the carried-window
   branch is not certified before the \(T_{11}\) attack.

Proof.

Paper 20 Theorem 4.3A.114 identifies the reduced app/readout slot with exactly
these three nonnegative tails. Vanishing of all three tails gives clause 1.
Limsup subadditivity and the finite component bounds give clause 2. Clause 3 is
the admissibility requirement that every term in
\(\mathcal W_{car}(\rho)\) be finite. `square`

### Corollary 14.7: Reduced `T_12` Assembly

The full reduced loop-readout debit is now

```math
U_{12}^{red,car,SEL2}
=
U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+U_{12}^{smear,SEL2}
+U_{12}^{P12,SEL2}
+U_{12}^{appLC,SEL2}
+U_{12}^{binLC,SEL2}.
```

On the strict same-record branch where Sections 12, 13, and Lemma 14.5 all
apply,

```math
U_{12}^{red,car,SEL2}=0.
```

Otherwise Paper 21 carries precisely the finite component bounds that have
been proved. The carried worksheet becomes

```math
U_{pre13}^{car,SEL2}(s)
\le
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

The next execution step is therefore the reduced \(T_{11}\) block; no
perimeter/cusp, smearing, loop-approximant/readout, Paper-14, endpoint/corner,
or exact-comparison debit is allowed to migrate into \(T_{11}\).

## 15. Post-`T_12` Carried Worksheet

The reduced `T_12` bucket has now been fully decomposed. Paper 21 therefore
freezes the post-`T_12` branch value before moving to \(T_{11}\).

### Definition 15.1: Active Reduced `T_12` Value

Define the active reduced loop-readout debit by

```math
U_{12}^{red,car,SEL2}
:=
U_{12}^{per,SEL2}
+U_{12}^{cusp,SEL2}
+U_{12}^{smear,SEL2}
+U_{12}^{P12,SEL2}
+U_{12}^{appLC,SEL2}
+U_{12}^{binLC,SEL2}.
```

On the strict same-record branch of Sections 12--14,

```math
U_{12}^{red,car,SEL2}=0.
```

On any non-strict branch, \(U_{12}^{red,car,SEL2}\) is the sum of exactly the
finite component bounds that have actually been proved. If any component is not
finite, the carried branch is not certified.

### Definition 15.2: Pre-`T_11` Reserve

For a candidate tree-time parameter \(s\), define the reserve left after the
already settled Paper-14, corner, exact-comparison, and reduced `T_12` debits:

```math
\mathcal M_{pre11}^{car,SEL2}(s)
:=
\underline M_{loss}^{SEL2,20}(s)
-E_{14}^{park}
-16
-X_{13}^{car,SEL2}
-U_{12}^{red,car,SEL2}.
```

This is not the final pre-surface margin. It is the budget available for the
two remaining nonsurface buckets:

```math
U_{11}^{act,SEL2}(s)
\quad\text{and}\quad
U_{13}^{entry,act,SEL2}(s).
```

### Theorem 15.3: Post-`T_12` Pass Criterion

After the reduced `T_12` assembly, the carried branch can reach the reduced
\(T_{11}\) attack only if

```math
\mathcal M_{pre11}^{car,SEL2}(s)>0.
```

If this holds, the remaining pre-surface pass condition is exactly

```math
U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s)
<
\mathcal M_{pre11}^{car,SEL2}(s).
```

Proof.

Substitute Definition 15.1 into the carried envelope of Corollary 14.7:

```math
U_{pre13}^{car,SEL2}(s)
\le
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

The carried-window inequality from Definition 7.2 is

```math
U_{pre13}^{car,SEL2}(s)
<
\underline M_{loss}^{SEL2,20}(s).
```

Moving the settled debits to the right-hand side gives the displayed reserve
and the remaining inequality. If the reserve is nonpositive, no nonnegative
choice of \(U_{11}^{act,SEL2}\) and \(U_{13}^{entry,act,SEL2}\) can make the
strict inequality hold. `square`

### Corollary 15.4: Strict `T_12` Shortcut

On the strict same-record branch where

```math
U_{12}^{red,car,SEL2}=0,
```

the pre-\(T_{11}\) reserve simplifies to

```math
\mathcal M_{pre11}^{strict,SEL2}(s)
=
\underline M_{loss}^{SEL2,20}(s)
-E_{14}^{park}
-16
-X_{13}^{car,SEL2}.
```

If \(X_{13}\) is also zeroed by
\(\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}\), then

```math
\mathcal M_{pre11}^{strictX0,SEL2}(s)
=
\underline M_{loss}^{SEL2,20}(s)
-E_{14}^{park}
-16.
```

Thus the exact status after the reduced `T_12` work is:

```math
E_{14}^{park}
\quad\text{and}\quad
16
```

are unavoidable carried debits on the current branch, \(X_{13}^{car,SEL2}\) is
zero only under the diagonal moving-battery audit, and reduced \(T_{12}\) is
zero only under the strict same-record loop-readout audits of Sections 12--14.

## 16. Reduced `T_11`: Active Transport Ledger

The reduced `T_12` ledger is now closed as a separate bucket. The next
execution step is therefore the genuine `T_11` transport block. This section
freezes what is allowed to enter \(U_{11}^{act,SEL2}\) before any component is
bounded.

### Definition 16.1: Active `T_11` Debit

On the same pushed-forward `SEL2` scalar record law, define

```math
U_{11}^{act,SEL2}(s)
:=
U_{11}^{loc,SEL2}(s)
+U_{11}^{RP,SEL2}(s)
+U_{11}^{Cov,SEL2}(s)
+U_{11}^{gauge,SEL2}(s).
```

The four terms mean:

```math
U_{11}^{loc,SEL2}
\quad\text{local block/collar transport not already assigned elsewhere;}
```

```math
U_{11}^{RP,SEL2}
\quad\text{record-projective or refinement transport from the Paper-16 ledger;}
```

```math
U_{11}^{Cov,SEL2}
\quad\text{covariance transport on the same scalar record tower;}
```

and

```math
U_{11}^{gauge,SEL2}
\quad\text{chart/gauge reconstruction transport for closed scalar records.}
```

All four are nonnegative carried debits. A component may be set to zero only by
a same-record zero theorem for that component.

### Definition 16.2: `T_11` No-Double-Charge Rule

The active `T_11` block is not a remainder bin. It may not contain any debit
already assigned to one of the settled ledgers:

```math
E_{14}^{park},\quad
16,\quad
X_{13}^{car,SEL2},\quad
U_{12}^{red,car,SEL2},\quad
U_{13}^{entry,act,SEL2}.
```

Equivalently:

1. perimeter, cusp, smearing, loop-approximant, and bin/readout tails remain
   in \(U_{12}^{red,car,SEL2}\);
2. moving-battery cutoff-to-exact and exact-readout comparison remain in
   \(X_{13}^{car,SEL2}\);
3. Paper-14 export remains in \(E_{14}^{park}\);
4. endpoint/corner bookkeeping remains in the carried debit \(16\);
5. block convergence, character-expansion regularity, RPF, KP-decoration, and
   Wilson-polymer entry terms remain in \(U_{13}^{entry,act,SEL2}\).

This is the Barandes-aligned same-record discipline: every comparison is made
between scalar records obtained from the same pushed-forward law, not between
extra gauge-fixed state descriptions.

### Lemma 16.3: Updated Carried Window After `T_12`

With Definitions 15.1 and 16.1, the active carried window is exactly

```math
\mathcal W_{car}(\rho)
=
\left\{
s>0:
\begin{array}{l}
0<\bar\eta_{res,20}(s)<\tau_{20}(s),\\[2mm]
s>
{2(1+\log19+
20\widehat\eta_{*,20}(s)/(1-\widehat\eta_{*,20}(s)))
\over C_2(\rho)(1-\epsilon_A)(1-\chi)},\\[3mm]
E_{14}^{park}
+16
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s)
<
\underline M_{loss}^{SEL2,20}(s)
\end{array}
\right\}.
```

Proof.

Substitute Definition 15.1 and Definition 16.1 into Definition 7.1. The first
two lines are unchanged admissibility and tree-time requirements. The third
line is the carried pre-surface inequality with the already settled \(T_{12}\)
debit inserted. `square`

### Corollary 16.4: Next Execution Target

The next proof obligation is to produce same-record bounds

```math
U_{11}^{loc,SEL2}(s),\quad
U_{11}^{RP,SEL2}(s),\quad
U_{11}^{Cov,SEL2}(s),\quad
U_{11}^{gauge,SEL2}(s),
```

and then reassemble

```math
U_{11}^{act,SEL2}(s)
<
\mathcal M_{pre11}^{car,SEL2}(s)
-U_{13}^{entry,act,SEL2}(s).
```

Until \(U_{13}^{entry,act,SEL2}\) is also bounded, a successful \(T_{11}\)
bound leaves a reserve; it does not by itself close the pre-surface pass.

## 17. Reduced `T_11`: Component Audit And Reassembly

This section executes the six-step `T_11` audit promised after the reduced
`T_12` assembly. The goal is not to make projective, covariance, or gauge
transport disappear by notation. The goal is to decide which parts are exact
on the frozen `SEL2` scalar records and which parts must remain carried.

### Definition 17.1: `T_11` Source Imports

The four active `T_11` components are sourced as follows.

```math
U_{11}^{loc,SEL2}
\quad\text{uses Paper 10 finite same-record pushforward and perfect-block
identity.}
```

The relevant Paper-10 import is exact only for the declared finite battery and
only when the coarse law is literally the pushed-forward fine law. If a local
Wilson/heat-kernel ansatz replaces the perfect block, the difference is a
local-action residual and is not zero by definition.

```math
U_{11}^{RP,SEL2}
\quad\text{uses Paper 16 `HK-RP-LEDGER` / `HK-RPCOV-CLOSE`.}
```

Only the `T_11`-exclusive part of the RP ledger is allowed here. Counterterm,
binning, perimeter/cusp, and loop-readout defects already assigned to
\(U_{12}^{red,car,SEL2}\) are not charged again.

```math
U_{11}^{Cov,SEL2}
\quad\text{uses Paper 16 `HK-COV-LEDGER` / `HK-RPCOV-CLOSE`.}
```

For exact hypercubic symmetries of a finite cutoff law, the exact cutoff
covariance defect is zero. For continuum Euclidean motions, the approximant,
boundary, block/collar, projective, regulator, and volume defects remain
genuine same-record transport terms unless separately proved to vanish.

```math
U_{11}^{gauge,SEL2}
\quad\text{uses Paper 10 gauge-compatible finite batteries and Paper 11
gauge-invariant scalar Wilson-loop completion.}
```

On closed scalar loop records, gauge invariance is an equality before any
gauge chart is chosen. A gauge-chart or axial-tree coordinate can be used as a
proof coordinate, but it may not be exported as an extra state description.

### Definition 17.2: Local Block/Collar Debit

For the active `SEL2` row, define

```math
L_{11,loc}^{SEL2}(s)
:=
\limsup_j\sum_{k\ge j}\eta_{11,loc;j,k}^{SEL2}(s),
```

where \(\eta_{11,loc;j,k}^{SEL2}\) is the same-record local block/collar
transport residual after removing all terms already assigned to
\(U_{12}^{red,car,SEL2}\), \(X_{13}^{car,SEL2}\), \(E_{14}^{park}\), the
corner debit \(16\), and \(U_{13}^{entry,act,SEL2}\).

The local slot is bounded by this ceiling:

```math
0\le U_{11}^{loc,SEL2}(s)\le L_{11,loc}^{SEL2}(s),
```

whenever \(L_{11,loc}^{SEL2}(s)<\infty\).

### Lemma 17.3: Exact Same-Record Perfect Blocking Zeros `loc`

If the active `SEL2` local block/collar comparison is the Paper-10 perfect
pushforward comparison on the frozen finite scalar battery, and no local
action replacement is made, then

```math
U_{11}^{loc,SEL2}(s)=0.
```

If the comparison instead inserts a local Wilson/heat-kernel ansatz, then the
honest carried bound is

```math
0\le
U_{11}^{loc,SEL2}(s)
\le
L_{11,loc}^{SEL2}(s),
```

provided this ceiling is finite.

Proof.

Paper 10's perfect block is defined by pushing the fine finite record law
forward to the coarse finite battery. For every scalar record \(F\) in that
battery,

```math
\omega_k(F\circ B_{k,j})=\omega_j^{perf}(F)
```

by definition of the pushed-forward law. Hence every local block/collar
residual in the reduced `T_11` slot is zero. If a local action ansatz replaces
the perfect pushed-forward law, this identity is no longer definitional; the
remaining difference is exactly \(\eta_{11,loc;j,k}^{SEL2}\), and limsup
subadditivity gives the displayed carried bound. `square`

### Definition 17.4: Reduced RP Debit

For each fixed finite OS battery and shell \(k\ge j\), define the reduced
reflection-positivity transport defect

```math
D_{11;j,k}^{RP,SEL2}
:=
\eta_{projRP,j,k}^{SEL2}
+\eta_{regRP,j,k}^{SEL2}
+\eta_{volRP,j,k}^{SEL2}
+\eta_{ctRP,j,k}^{11,SEL2}
+\eta_{binRP,j,k}^{11,SEL2}.
```

Here the superscript \(11\) means "not already charged to the reduced
loop-readout ledger." On the strict exact scalar-record branch,
\(\eta_{ctRP}^{11}=\eta_{binRP}^{11}=0\). Set

```math
U_{11}^{RP,SEL2}(s)
:=
\limsup_j\sum_{k\ge j}D_{11;j,k}^{RP,SEL2}(s).
```

### Lemma 17.5: RP Slot Is Zero Or Carried By The Reduced RP Tail

If

```math
\sum_{k\ge j}D_{11;j,k}^{RP,SEL2}(s)\to0,
```

then

```math
U_{11}^{RP,SEL2}(s)=0.
```

Otherwise the active branch may carry \(U_{11}^{RP,SEL2}(s)\) only when the
limsup in Definition 17.4 is finite.

Proof.

Paper 16 `HK-RP-LEDGER` states that all RP loss after exact heat-kernel cutoff
reflection positivity is contained in the declared transport/readout ledger.
Definition 17.4 removes the parts already assigned to \(T_{12}\). Therefore
the reduced `T_11` RP debit is exactly the tail of \(D_{11}^{RP}\). A
vanishing tail gives zero; a finite limsup gives the carried upper bound.
`square`

### Definition 17.6: Reduced Covariance Debit

For an admissible Euclidean motion \(g\), define

```math
D_{11;j,k}^{Cov,SEL2}(g)
:=
\eta_{exactCov,j,k}^{11,SEL2}(g)
+\eta_{blockCov,j,k}^{11,SEL2}(g)
+\eta_{projCov,j,k}^{SEL2}(g)
+\eta_{regCov,j,k}^{SEL2}(g)
+\eta_{volCov,j,k}^{SEL2}(g)
+\eta_{appCov,j,k}^{11,SEL2}(g)
+\eta_{binCov,j,k}^{11,SEL2}(g)
+\eta_{ctCov,j,k}^{11,SEL2}(g).
```

The superscript \(11\) again denotes the residual part not already paid by
the loop-readout, endpoint/corner, Paper-14, exact-comparison, or entry
ledgers. Set

```math
U_{11}^{Cov,SEL2}(s)
:=
\sup_{g\in Euc_{adm}^{SEL2}}
\limsup_j\sum_{k\ge j}D_{11;j,k}^{Cov,SEL2}(g;s).
```

For the restricted hypercubic-symmetry branch, \(Euc_{adm}^{SEL2}\) may be
replaced by the finite hypercubic symmetry set. For a continuum Euclidean
motion branch, the approximant and volume-buffer terms must be present unless
proved to vanish on the same scalar records.

### Lemma 17.7: Covariance Slot Is Zero Or Carried By The Reduced Covariance Tail

If

```math
\sup_{g\in Euc_{adm}^{SEL2}}
\sum_{k\ge j}D_{11;j,k}^{Cov,SEL2}(g;s)
\to0,
```

then

```math
U_{11}^{Cov,SEL2}(s)=0.
```

Otherwise \(U_{11}^{Cov,SEL2}(s)\) is certified only by a finite value of the
limsup in Definition 17.6.

Proof.

Paper 16 `HK-COV-LEDGER` states that covariance transport is bounded by the
declared covariance defect \(D^{Cov}\). Definition 17.6 is the disjoint
`T_11` part of that ledger. Exact finite hypercubic covariance contributes no
\(\eta_{exactCov}\); continuum motions contribute only through the declared
approximant and transport defects. The conclusion follows from the same
tail-limsup argument as Lemma 17.5. `square`

### Definition 17.8: Gauge/Chart Reconstruction Debit

Define

```math
U_{11}^{gauge,SEL2}(s)
:=
\limsup_j\sum_{k\ge j}\eta_{11,gauge;j,k}^{SEL2}(s),
```

where \(\eta_{11,gauge}\) is the scalar-record defect left after forgetting
all gauge charts, axial trees, and proof-coordinate gauge choices.

### Lemma 17.9: Closed Scalar Records Zero The Gauge Slot

On the strict closed-loop scalar-record branch,

```math
U_{11}^{gauge,SEL2}(s)=0.
```

If the branch compares two nonidentical gauge-chart reconstructions before
forgetting to scalar records, then the zero statement is invalid and the
finite carried bound is the limsup in Definition 17.8.

Proof.

Closed Wilson-loop scalar records are gauge invariant at every finite cutoff.
Paper 10's gauge-compatible battery maps preserve the gauge-invariant
subspace, and Paper 11's gauge-invariant completion preserves gauge
invariance by multiplying by gauge-invariant local densities. Therefore, once
the record is pushed to the scalar closed-loop algebra, gauge transformations
act trivially on the tested records. Any axial tree or gauge chart is only a
proof coordinate; after the gauge-forgetting map no scalar defect remains.
If two chart-dependent reconstructions are compared before this forgetting,
the comparison is not the strict scalar branch and must be carried as
\(\eta_{11,gauge}\). `square`

### Theorem 17.10: Reduced `T_11` Reassembly

On the active `SEL2` branch,

```math
U_{11}^{act,SEL2}(s)
\le
L_{11,loc}^{SEL2}(s)
+U_{11}^{RP,SEL2}(s)
+U_{11}^{Cov,SEL2}(s)
+U_{11}^{gauge,SEL2}(s),
```

with the following strict-branch simplification:

```math
U_{11}^{act,SEL2}(s)
\le
U_{11}^{RP,SEL2}(s)
+U_{11}^{Cov,SEL2}(s),
```

whenever exact same-record perfect blocking and closed scalar-loop gauge
forgetting are used.

If, in addition, the reduced RP and covariance tails vanish cofinally, then

```math
U_{11}^{act,SEL2}(s)=0.
```

Proof.

Definition 16.1 decomposes \(U_{11}^{act}\) into the local, RP, covariance,
and gauge slots. Lemma 17.3 evaluates the local slot, Lemma 17.5 evaluates
the RP slot, Lemma 17.7 evaluates the covariance slot, and Lemma 17.9
evaluates the gauge slot. The no-double-charge rule of Definition 16.2 makes
these four slots disjoint from the already settled \(T_{12}\), \(X_{13}\),
Paper-14, corner, and \(T_{13}\)-entry ledgers. Summing the four bounds gives
the first display. The strict-branch simplification deletes the local and
gauge terms. If the two remaining reduced tails vanish, the sum is zero.
`square`

### Corollary 17.11: Post-`T_11` Reserve

After the reduced `T_11` audit, define

```math
\mathcal M_{post11}^{car,SEL2}(s)
:=
\mathcal M_{pre11}^{car,SEL2}(s)
-U_{11}^{act,SEL2}(s).
```

The branch can proceed to the `T_13` entry audit only if

```math
\mathcal M_{post11}^{car,SEL2}(s)>0.
```

The remaining pre-surface condition is then exactly

```math
U_{13}^{entry,act,SEL2}(s)
<
\mathcal M_{post11}^{car,SEL2}(s).
```

Thus the next live bucket after `T_11` is

```math
U_{13}^{entry,act,SEL2}
=
U_{13}^{BC,car}
+U_{13}^{CE,car}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car},
```

with no `T_11`-assigned projective/RP, covariance, gauge, loop-readout,
endpoint/corner, Paper-14, or exact-comparison debit allowed to migrate into
it.

## 18. Reduced `T_13`: Exact-Entry Component Audit

The branch has now paid or parked all nonsurface debits before the Paper-13
actual-entry chain. The remaining pre-surface bucket is
\(U_{13}^{entry,act,SEL2}\). On the standard reduced route, the surface
subcriticality residual `SUB` is not charged here; it is paid later in the
surface-leading-rate inequality. Thus the active entry bucket has five, not
six, components.

### Definition 18.1: Active Exact-Entry Residuals

On the same frozen `SEL2` scalar record law, define rowwise residuals

```math
\epsilon_{BC,j}^{SEL2},\quad
\epsilon_{CE,j}^{SEL2},\quad
\epsilon_{RPF,j}^{SEL2},\quad
\epsilon_{KPdec,j}^{SEL2},\quad
\epsilon_{WP,j}^{SEL2}.
```

They mean:

```math
\epsilon_{BC,j}^{SEL2}
\quad\text{block-convergence residual on the actual finite entry battery;}
```

```math
\epsilon_{CE,j}^{SEL2}
\quad\text{central-character extraction residual for exact entry;}
```

```math
\epsilon_{RPF,j}^{SEL2}
\quad\text{residual-factorization defect on the same scalar records;}
```

```math
\epsilon_{KPdec,j}^{SEL2}
\quad\text{entry-level KP/decorrelation comparison residual;}
```

and

```math
\epsilon_{WP,j}^{SEL2}
\quad\text{whole-process compatibility residual for the Paper-13 entry chain.}
```

The entry-level `CE` residual is not the leading coefficient rate
\(\kappa_{13}^{CE}\). The `KPdec` residual is not a second copy of the already
paid decoration debit. The `WP` residual is not the Paper-14 export debit.

### Definition 18.2: Component Ceilings

Define the active carried component ceilings by

```math
U_{13}^{BC,car}
:=
\limsup_j\epsilon_{BC,j}^{SEL2},
\qquad
U_{13}^{CE,car}
:=
\limsup_j\epsilon_{CE,j}^{SEL2},
```

```math
U_{13}^{RPF,car}
:=
\limsup_j\epsilon_{RPF,j}^{SEL2},
\qquad
U_{13}^{KPdec,car}
:=
\limsup_j\epsilon_{KPdec,j}^{SEL2},
```

and

```math
U_{13}^{WP,car}
:=
\limsup_j\epsilon_{WP,j}^{SEL2}.
```

The reduced entry bucket is certified only if all five limsups are finite. If
one is infinite or undefined on the frozen same-record tower, the branch is
not certified through exact entry.

### Definition 18.3: Reduced-Route `SUB` Placement

On the active reduced route,

```math
\epsilon_{SUB,j}^{SEL2}=0
```

inside \(U_{13}^{entry,act,SEL2}\), because surface subcriticality is charged
only through the final \(T_{13}\) leading-rate test. If a future branch does
not pay subcriticality there, then the entry bucket must be enlarged by
\(\limsup_j\epsilon_{SUB,j}^{SEL2}\). It may not be omitted from both places.

### Lemma 18.4: Block-Convergence Entry Fork

The `BC` component obeys the zero-or-carried fork:

```math
U_{13}^{BC,car}=0
\quad\Longleftrightarrow\quad
\epsilon_{BC,j}^{SEL2}\to0.
```

In Paper-20 language, the zero branch is the moving-battery block-limit
uniqueness audit. Without that audit, compactness gives only a finite carried
ceiling, for normalized records of the form

```math
0\le U_{13}^{BC,car}\le 2B_{BC}^{SEL2}.
```

This finite carry is not a proof of block-limit uniqueness.

### Lemma 18.5: Central-Extraction Entry Fork

The entry-level central-character extraction component obeys

```math
U_{13}^{CE,car}=0
\quad\Longleftrightarrow\quad
\epsilon_{CE,j}^{SEL2}\to0.
```

A finite nonzero value of \(U_{13}^{CE,car}\) is allowed only as the exact-entry
central-extraction transport residual. It cannot be used as evidence for, or
against, the later positive leading surface rate \(\kappa_{13}^{CE}\).

### Lemma 18.6: Residual-Factorization Entry Fork

The residual-factorization component obeys

```math
U_{13}^{RPF,car}=0
\quad\Longleftrightarrow\quad
\epsilon_{RPF,j}^{SEL2}\to0.
```

If the factorization is proved only up to a finite same-record comparison norm,
that limsup is carried as \(U_{13}^{RPF,car}\). It may not be reassigned to
projective, covariance, or gauge transport after Section 17 has closed those
ledgers.

### Lemma 18.7: Entry KP/Decoration Fork

The entry-level KP/decorrelation component obeys

```math
U_{13}^{KPdec,car}=0
\quad\Longleftrightarrow\quad
\epsilon_{KPdec,j}^{SEL2}\to0.
```

If finite but nonzero, \(U_{13}^{KPdec,car}\) is a comparison residual between
the exact-entry KP/decorrelation statement and the scalar entry battery. It is
not an additional decoration debit and may not recharge \(D_{dec}^{SEL2,20}\),
\(\eta_{ch}^{SEL2}\), or the finite-template collar constant.

### Lemma 18.8: Whole-Process Entry Fork

The whole-process entry component obeys

```math
U_{13}^{WP,car}=0
\quad\Longleftrightarrow\quad
\epsilon_{WP,j}^{SEL2}\to0.
```

If finite but nonzero, it is carried only as the Paper-13 actual-entry
whole-process compatibility residual. It is distinct from the parked Paper-14
export \(E_{14}^{park}\).

### Theorem 18.9: Exact-Entry Reassembly

On the active reduced `SEL2` branch,

```math
U_{13}^{entry,act,SEL2}
\le
U_{13}^{BC,car}
+U_{13}^{CE,car}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car}.
```

If the five residuals vanish cofinally, then

```math
U_{13}^{entry,act,SEL2}=0.
```

If any of the five residual ceilings is not finite, the exact-entry source
route does not certify the branch.

Proof.

Paper 19 Definition 8L.11A.24 and Paper 20 Definition 4.3A.72 identify the
actual-entry transport loss with the sum of the Paper-13 entry residuals
`BC`, `CE`, `RPF`, `KPdec`, `SUB`, and `WP`. Definition 18.3 removes `SUB`
from the entry bucket only because it is paid later in the surface
leading-rate test. Limsup subadditivity gives the displayed five-term bound.
If all five residuals vanish cofinally, the bound is zero. If any limsup is
not finite, no finite carried ceiling has been supplied. `square`

### Corollary 18.10: Post-Entry Surplus

Define the post-entry surplus by

```math
\Pi_{postentry}^{car,SEL2}(s)
:=
\mathcal M_{post11}^{car,SEL2}(s)
-U_{13}^{entry,act,SEL2}(s).
```

Equivalently,

```math
\Pi_{postentry}^{car,SEL2}(s)
=
\underline M_{loss}^{SEL2,20}(s)
-E_{14}^{park}
-16
-X_{13}^{car,SEL2}
-U_{12}^{red,car,SEL2}
-U_{11}^{act,SEL2}(s)
-U_{13}^{entry,act,SEL2}(s).
```

The branch reaches the final \(T_{13}\) surface-leading-rate comparison only if

```math
\Pi_{postentry}^{car,SEL2}(s)>0.
```

When this holds, the remaining obstruction is no longer nonsurface transport.
It is the surface rate gate: the parked
\(\mathrm{P20\text{-}SEL2\text{-}TREE\text{-}RATE\text{-}GATE}\), together with
the associated surface prefactor cap.

### Corollary 18.11: Next Live Decision

The next execution decision is therefore:

1. prove the five same-record entry zero tests

   ```math
   \epsilon_{BC,j}^{SEL2},
   \epsilon_{CE,j}^{SEL2},
   \epsilon_{RPF,j}^{SEL2},
   \epsilon_{KPdec,j}^{SEL2},
   \epsilon_{WP,j}^{SEL2}
   \to0,
   ```

   or carry their finite limsups explicitly; then

2. test \(\Pi_{postentry}^{car,SEL2}(s)>0\); then

3. only if that surplus is positive, return to the final surface-leading-rate
   inequality.

This is the honest boundary of the current nonsurface worksheet: `BC`, `CE`,
`RPF`, `KPdec`, and `WP` are real same-record source gates, not notation to be
erased.

## 19. Symbolic Post-Entry Surplus Evaluation

The post-entry expression can now be evaluated without opening the final
surface-rate gate. This section performs that scalar evaluation and records
the immediate consequence of the current unit-counted corner debit.

### Definition 19.1: Expanded Carried Surplus

Set

```math
D_{20}(s)
:=
{20\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}.
```

Using the signal profile of Definition 5.1,

```math
F_\rho(s)
=
e^{-a_\rho s}\left(1-e^{-b_\rho s}\right),
```

and the reduced entry assembly of Theorem 18.9, the certified carried
post-entry surplus is

```math
\Pi_{postentry}^{car,SEL2}(s)
=
1+F_\rho(s)-e^{D_{20}(s)}
-E_{14}^{park}
-16
-X_{13}^{car,SEL2}
-U_{12}^{red,car,SEL2}
-U_{11}^{act,SEL2}(s)
```

```math
\qquad
-U_{13}^{BC,car}
-U_{13}^{CE,car}
-U_{13}^{RPF,car}
-U_{13}^{KPdec,car}
-U_{13}^{WP,car}.
```

Equivalently, if

```math
\mathcal R_{noncorn}^{SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
```

```math
\qquad
+U_{13}^{BC,car}
+U_{13}^{CE,car}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car},
```

then

```math
\Pi_{postentry}^{car,SEL2}(s)
=
1+F_\rho(s)-e^{D_{20}(s)}
-16
-\mathcal R_{noncorn}^{SEL2}(s).
```

Every term in \(\mathcal R_{noncorn}^{SEL2}\) is nonnegative on the carried
ledger.

### Lemma 19.2: Universal Signal Ceiling

For every admissible \(s>0\),

```math
0<F_\rho(s)<1.
```

Consequently, since \(D_{20}(s)\ge0\),

```math
1+F_\rho(s)-e^{D_{20}(s)}
\le
F_\rho(s)
<1.
```

Proof.

The parameters \(a_\rho,b_\rho\) are positive on the active selector branch.
Thus \(0<e^{-a_\rho s}<1\) and \(0<1-e^{-b_\rho s}<1\), so
\(0<F_\rho(s)<1\). Also \(D_{20}(s)\ge0\), hence \(e^{D_{20}(s)}\ge1\).
Substitution gives the displayed bound. `square`

### Theorem 19.3: The Current Unit-Corner Carried Package Cannot Pass

With the current Paper-21 carried substitution of the endpoint/corner debit by
the unit-counted value \(16\),

```math
\Pi_{postentry}^{car,SEL2}(s)<-15
```

for every admissible \(s\). Therefore the current certified carried package
cannot prove

```math
\Pi_{postentry}^{car,SEL2}(s)>0.
```

Proof.

By Definition 19.1 and nonnegativity of
\(\mathcal R_{noncorn}^{SEL2}(s)\),

```math
\Pi_{postentry}^{car,SEL2}(s)
\le
1+F_\rho(s)-e^{D_{20}(s)}-16.
```

Lemma 19.2 bounds the first three terms by a number strictly less than \(1\).
Hence \(\Pi_{postentry}^{car,SEL2}(s)<1-16=-15\). `square`

### Corollary 19.4: What The Symbolic Evaluation Falsifies

Theorem 19.3 falsifies the current **upper-bound certificate** with the
additive unit-corner replacement \(E_{corn}^{car,SEL2}\leadsto16\). It does
not by itself falsify the underlying `SEL2` physical route, because \(16\) was
introduced as a coarse carried endpoint/corner ceiling.

To make the post-entry surplus certifiable, one must replace the unit-counted
corner charge by a same-record normalized corner debit \(C_{corn}^{sharp,SEL2}\)
and prove the scalar inequality

```math
C_{corn}^{sharp,SEL2}
+\mathcal R_{noncorn}^{SEL2}(s)
<
1+F_\rho(s)-e^{D_{20}(s)}.
```

Since the right-hand side is \(<1\), any additive corner convention with a
fixed lower bound at or above \(1\) is already too large. Thus the next
mathematical task is not the surface-rate gate; it is a same-record
normalization audit for endpoint/corner transport, or a proof that the corner
term is zero on the strict scalar branch.

## 20. Reopened Endpoint/Corner Strict-Zero Audit

Section 19 shows that the coarse unit-counted replacement
\(E_{corn}^{car,SEL2}\leadsto16\) makes the carried post-entry certificate
fail before the surface-rate gate is reached. This section reopens that debit
and tries the strict-zero route. The audit is deliberately same-record: an
endpoint/corner term may disappear only because the pushed-forward scalar
record law makes its rowwise contribution vanish, not because a proof
coordinate has been silently renamed.

### Definition 20.1: Sharp Rowwise Corner Debit

For the active pure rectangular-corner `SEL2` branch, let
\(\mathcal D_{corn}^{SEL2}\) be the finite endpoint/corner template list from
Paper 20 Definition 4.3A.92. For row \(j\), define the sharp rowwise corner
debit by

```math
E_{corn,j}^{sharp,SEL2}
:=
\sum_{\upsilon\in\mathcal D_{corn}^{SEL2}}
M_{\upsilon,j}\,v_{\upsilon,j}^{SEL2},
```

where \(M_{\upsilon,j}\) is the occurrence count in the four-slot Creutz
battery and \(v_{\upsilon,j}^{SEL2}\ge0\) is the scalar transport weight of one
such occurrence on the same pushed-forward `SEL2` record law. Set

```math
C_{corn}^{sharp,SEL2}
:=
\limsup_j E_{corn,j}^{sharp,SEL2}.
```

The old unit-counted substitution \(16\) is only the coarse ceiling

```math
C_{corn}^{sharp,SEL2}\le16
```

under Definition 8.1--Theorem 8.4. The strict-zero problem is therefore the
separate question

```math
C_{corn}^{sharp,SEL2}=0.
```

### Definition 20.2: Strict Corner-Zero Gate

`P21-SEL2-ECORN-ZERO` is the same-record assertion

```math
C_{corn}^{sharp,SEL2}=0.
```

Since every summand in \(E_{corn,j}^{sharp,SEL2}\) is nonnegative, this is
equivalent to

```math
\sum_{\upsilon\in\mathcal D_{corn}^{SEL2}}
M_{\upsilon,j}\,v_{\upsilon,j}^{SEL2}
\longrightarrow0
```

along the selected cofinal tail. The gate can close by any of the following
routes.

1. **Empty-template route:**

   ```math
   M_{\upsilon,j}=0
   \qquad
   \text{for every }\upsilon\in\mathcal D_{corn}^{SEL2}
   ```

   cofinally.

2. **Zero-weight route:**

   ```math
   \max_{\upsilon\in\mathcal D_{corn}^{SEL2}}
   v_{\upsilon,j}^{SEL2}
   \longrightarrow0.
   ```

3. **No-corner selector route:** a different finite selector/readout convention
   keeps endpoint/corner normalization inside the scalar readout or the
   multiplicative decoration ledger, with the selector, no-smuggling audit,
   decoration constant, and transport worksheet all recomputed.

The third route is not a deletion of the present debit. It is a different
branch of the construction.

### Lemma 20.3: The Empty-Template Route Fails On The Active Branch

On the active four-slot pure rectangular-corner branch,

```math
\sum_{\upsilon\in\mathcal D_{corn}^{SEL2}}M_{\upsilon,j}=16
```

on a cofinal tail. Hence the empty-template route in Definition 20.2 cannot
prove `P21-SEL2-ECORN-ZERO`.

Proof.

Paper 20 Lemma 4.3A.93 proves that the four Creutz slots are nondegenerate
rectangles cofinally and that each rectangle has four ordinary convex
endpoint/corner occurrences. Definition 8.1 assigns exactly these ordinary
convex occurrences to the endpoint/corner register and assigns concave
Creutz-overlap subtraction corners elsewhere. Therefore the active register
has \(4\cdot4=16\) occurrences cofinally. Aggregating occurrences into finitely
many template types changes the type labels but not the total occurrence count.
Thus the endpoint/corner template register is not empty cofinally. `square`

### Lemma 20.4: The Current Source Package Does Not Prove Zero Weight

The current Paper-20/Paper-21 imports do not prove

```math
\max_{\upsilon\in\mathcal D_{corn}^{SEL2}}
v_{\upsilon,j}^{SEL2}\to0.
```

Consequently the zero-weight route in Definition 20.2 is not closed on the
active branch.

Proof.

The imported endpoint/corner audit is Paper 20 Theorem 4.3A.94, specialized in
Paper 21 Theorem 8.4. It provides the finite bound

```math
0\le E_{corn}^{car,SEL2}\le16
```

under the unit-counted pure rectangular-corner convention. It does not assert
that endpoint/corner scalar transport weights decay with \(j\). Paper 20
Theorem 4.3A.95 explicitly lists a zero-weight audit as an additional source
condition not present in the standard branch. Therefore zero weight is not a
consequence of the current source package. `square`

### Lemma 20.5: A No-Corner Selector Is A New Branch

The no-corner route can make the **separate** endpoint/corner debit equal to
zero only after changing the selector/readout convention and re-auditing all
ledgers touched by that change. In particular, it must reprove:

```math
\mathrm{P20\text{-}SEL2\text{-}NOSMUGGLE},
\qquad
C_{dec,act}^{SEL2},
\qquad
U_{12}^{red,car,SEL2},
\qquad
\mathcal W_{car}(\rho).
```

It cannot be used inside the current corner-separated branch.

Proof.

The active branch declares endpoint/corner collars outside the multiplicative
decoration debit and inside the reduced loop-readout side. Moving those
records back into the scalar readout or decoration ledger changes the
pushforward record map and the debit partition. In Barandes-aligned terms, this
is a change in the operational record coarse-graining, not an invisible
ontological rearrangement. The no-smuggling and scalar-budget audits are exactly
the checks that such a change has not imported area-law information or hidden a
finite cost. Thus the no-corner route is legitimate only as a fresh branch with
its own source worksheet. `square`

### Theorem 20.6: Strict Corner Zero Is Not Proved On The Current Branch

On the current standard corner-separated `SEL2` branch, Paper 21 cannot certify

```math
C_{corn}^{sharp,SEL2}=0.
```

Equivalently, the replacement

```math
E_{corn}^{car,SEL2}\leadsto0
```

is not available for the post-entry surplus worksheet.

Proof.

By Definition 20.2, strict zero needs the empty-template route, the zero-weight
route, or a new no-corner selector. Lemma 20.3 rules out the empty-template
route on the active four-slot branch. Lemma 20.4 shows that the current source
package does not prove the zero-weight route. Lemma 20.5 shows that the
no-corner route is a different branch requiring a fresh selector and ledger
audit. Therefore strict corner zero is not proved for the current branch. `square`

### Corollary 20.7: Reopened Corner Verdict

The strict-zero attempt has the following honest outcome.

1. The coarse \(16\) ceiling is too large for the post-entry surplus by
   Theorem 19.3.
2. The current source package also does not prove the strict zero
   \(C_{corn}^{sharp,SEL2}=0\).
3. The remaining viable corner work is therefore one of:

   ```math
   \text{prove }C_{corn}^{sharp,SEL2}<1
   \text{ sharply enough for Corollary 19.4,}
   ```

   ```math
   \text{prove the missing zero-weight theorem,}
   ```

   or

   ```math
   \text{declare a no-corner selector and re-audit the full carried worksheet.}
   ```

Until one of these is done, the endpoint/corner debit remains a genuine
same-record obstruction before the final surface-rate gate.

## 21. Balanced No-Corner Selector And Re-Audited Worksheet

The sharp-bound route would need

```math
C_{corn}^{sharp,SEL2}
<
1+F_\rho(s)-e^{D_{20}(s)}-\mathcal R_{noncorn}^{SEL2}(s),
```

and the right-hand side is always \(<1\). On the unit-counted
corner-separated branch this is not the natural target: the finite template
enumeration has nonempty endpoint/corner occurrences cofinally, and the current
source package does not provide subunit endpoint/corner weights. This section
therefore takes the other legitimate route from Corollary 20.7: define a new
no-corner scalar readout and re-audit the carried worksheet.

### Definition 21.1: Balanced Creutz No-Corner Selector

`P21-SEL2-NCORN` is the following replacement selector for the active four-slot
`SEL2` battery.

1. The four geometric loop records are unchanged:

   ```math
   C_{++}=(L_j,L_j),\quad
   C_{--}=(L_j-\sigma_j,L_j-\sigma_j),
   ```

   ```math
   C_{+-}=(L_j,L_j-\sigma_j),\quad
   C_{-+}=(L_j-\sigma_j,L_j).
   ```

2. Endpoint/corner finite-template factors are not moved into
   \(D_{dec}^{SEL2,20}\) and are not charged as a separate additive debit.
   They remain inside the four scalar loop records until the signed Creutz
   readout is formed.

3. The scalar readout is the signed four-slot additive loop-readout coordinate

   ```math
   \mathfrak C_j^{NC}
   :=
   \ell(C_{++})
   +\ell(C_{--})
   -\ell(C_{+-})
   -\ell(C_{-+}),
   ```

   where \(\ell(C)\) is the scalar log/counterterm readout coordinate of the
   loop record. When the four loop expectations are positive and the logarithm
   is literally available, this is the logarithm of the usual multiplicative
   Creutz ratio.

4. Endpoint/corner templates are indexed by oriented convex corner type
   \(\tau\). For one occurrence of type \(\tau\), the scalar corner weight on
   row \(j\) is \(v_{\tau,j}^{SEL2}\). This weight is a function of the finite
   endpoint/corner template type and the row, not of which of the four congruent
   rectangular slots contains that occurrence.

Clause 4 is the finite-template invariance already implicit in Paper 20
Definition 4.3A.92: the weight is attached to the pushed-forward scalar
template type, not to an unobserved continuum surface.

### Lemma 21.2: Signed Corner Incidence Cancels

For every oriented convex endpoint/corner type \(\tau\),

```math
M_{\tau,++}
+M_{\tau,--}
-M_{\tau,+-}
-M_{\tau,-+}
=0
```

on the cofinal nondegenerate four-slot branch.

Proof.

Each \(C_{\alpha\beta}\) is an axis-aligned nondegenerate rectangle on a
cofinal tail. Such a rectangle contains the same oriented convex corner
multiset: one northeast, one northwest, one southeast, and one southwest
corner. Therefore, for every oriented corner type \(\tau\),

```math
M_{\tau,++}=M_{\tau,--}=M_{\tau,+-}=M_{\tau,-+}=1.
```

The signed Creutz incidence is \(1+1-1-1=0\). `square`

### Theorem 21.3: Endpoint/Corner Debit Is Zero On The Balanced Selector

Assume `P21-SEL2-NCORN`. Then the separate endpoint/corner debit of the carried
worksheet is zero:

```math
U_{corn}^{NC,SEL2}=0.
```

Proof.

The endpoint/corner contribution to the signed readout is

```math
\sum_{\tau}
\left(
M_{\tau,++}
+M_{\tau,--}
-M_{\tau,+-}
-M_{\tau,-+}
\right)
v_{\tau,j}^{SEL2}.
```

By Lemma 21.2, the signed incidence coefficient of each template type
\(\tau\) is zero. The entire endpoint/corner term therefore cancels before
any absolute-value transport ceiling is formed. No finite endpoint/corner
register remains outside the scalar readout, so the carried worksheet has
\(U_{corn}^{NC,SEL2}=0\). `square`

### Lemma 21.4: No-Smuggling Re-Audit

`P21-SEL2-NCORN` does not import a continuum measure, an area law, or a hidden
gauge-sector state. It is a deterministic scalar readout map from the same four
finite loop records used by the corner-separated branch.

Proof.

The selector changes only the order of finite bookkeeping operations. The
corner-separated branch first separates endpoint/corner factors and then upper
bounds their absolute contribution. The balanced no-corner branch first forms
the signed Creutz scalar record and uses the finite incidence identity of Lemma
21.2. Both branches use the same four loop records and the same rowwise
pushforward law. The proof uses only finite template equality, so it cannot
smuggle confinement, a Wilson-loop area law, or a continuum Yang-Mills measure
into the source package. `square`

### Lemma 21.5: Decoration And `T_12` Re-Audit

On `P21-SEL2-NCORN`,

```math
C_{dec,act}^{NC,SEL2}=C_{dec,act}^{SEL2},
```

and

```math
U_{12}^{NC,red,SEL2}=U_{12}^{red,car,SEL2}.
```

Proof.

The no-corner selector does not move endpoint/corner factors into
\(D_{dec}^{SEL2,20}\); it cancels them inside the signed scalar readout.
Therefore the active multiplicative decoration constant is unchanged. It also
does not change the already reduced perimeter/cusp, smearing, and
loop-approximant/readout tails. Those tails remain exactly the
\(U_{12}^{red,car,SEL2}\) package assembled in Sections 12--15. The only
removed term is the separate endpoint/corner debit, already shown zero in
Theorem 21.3. `square`

### Definition 21.6: No-Corner Carried Worksheet

For the balanced no-corner branch, define

```math
U_{pre13}^{NC,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

Equivalently, the endpoint/corner term \(+16\) in the carried worksheet is
deleted and no replacement corner debit is inserted.

Define the no-corner carried feasibility window by

```math
\mathcal W_{NC}(\rho)
:=
\left\{
s\in\mathcal W_{ad}(\rho):
U_{pre13}^{NC,SEL2}(s)
<
\underline M_{loss}^{SEL2,20}(s)
\right\}.
```

### Theorem 21.7: Re-Audited Post-Entry Surplus

On `P21-SEL2-NCORN`, the post-entry surplus is

```math
\Pi_{postentry}^{NC,SEL2}(s)
=
1+F_\rho(s)-e^{D_{20}(s)}
-\mathcal R_{noncorn}^{SEL2}(s),
```

where

```math
\mathcal R_{noncorn}^{SEL2}(s)
=
E_{14}^{park}
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
```

```math
\qquad
+U_{13}^{BC,car}
+U_{13}^{CE,car}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car}.
```

Thus the no-corner branch reaches the final surface-rate gate exactly when

```math
\mathcal R_{noncorn}^{SEL2}(s)
<
1+F_\rho(s)-e^{D_{20}(s)}
```

for some admissible \(s\in\mathcal W_{ad}(\rho)\).

Proof.

Start from Definition 19.1 and remove the only term changed by
`P21-SEL2-NCORN`, namely the separate endpoint/corner debit. Theorem 21.3
justifies replacing it by zero; Lemmas 21.4 and 21.5 prove that no new
decoration or reduced `T_12` debit is created by doing so. The remaining terms
are precisely \(\mathcal R_{noncorn}^{SEL2}(s)\). Positivity of the post-entry
surplus is therefore equivalent to the displayed strict inequality. `square`

### Corollary 21.8: What The No-Corner Branch Achieves

The no-corner selector removes the endpoint/corner obstruction that caused
Theorem 19.3. It does **not** prove the full `SEL2` route by itself. The live
pre-surface obstruction is now reduced to the non-corner package
\(\mathcal R_{noncorn}^{SEL2}(s)\), especially \(E_{14}^{park}\),
\(X_{13}^{car,SEL2}\), the reduced `T_11` terms, and the five exact-entry
residuals.

If the strict inequality in Theorem 21.7 is proved, the branch may return to
the final surface-leading-rate gate. If it fails only by upper bounds, the
certificate fails but the underlying route is not falsified without a matching
same-record lower floor.

## 22. Active No-Corner Branch And Scalar Margin Optimization

The live Paper-21 branch is now the balanced no-corner branch
`P21-SEL2-NCORN`. The older corner-separated branch remains a valid parked
branch, but it cannot pass with the coarse \(+16\) corner ceiling by Theorem
19.3 and it does not currently prove strict corner zero by Theorem 20.6. The
active worksheet is therefore:

```math
U_{pre13}^{NC,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

No endpoint/corner term appears in this worksheet.

### Definition 22.1: Structural No-Corner Admissible Set

The debit-free structural admissible set for the no-corner branch is

```math
\mathcal A_{NC}(\rho)
:=
\left\{
s>0:
\begin{array}{l}
0<\bar\eta_{res,20}(s)<\tau_{20}(s),\\[2mm]
s>
{2(1+\log19+D_{20}(s))
\over C_2(\rho)(1-\epsilon_A)(1-\chi)}
\end{array}
\right\},
```

where

```math
D_{20}(s)
:=
{20\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}.
```

This is Definition 5.5 with the debit inequality removed. The actual
no-corner pass condition will be imposed by comparing the non-corner debit to
the available margin.

### Definition 22.2: Available No-Corner Margin

For \(s\in\mathcal A_{NC}(\rho)\), define

```math
S_{NC}(s)
:=
1+F_\rho(s)-e^{D_{20}(s)}.
```

The no-corner branch has positive nonsurface margin at \(s\) exactly when

```math
S_{NC}(s)>0
```

and it passes the post-entry worksheet exactly when

```math
\mathcal R_{noncorn}^{SEL2}(s)<S_{NC}(s).
```

Define the optimized available no-corner margin by

```math
S_{NC}^{max}(\rho)
:=
\sup_{s\in\mathcal A_{NC}(\rho)}S_{NC}(s).
```

If \(\mathcal A_{NC}(\rho)=\varnothing\), set \(S_{NC}^{max}(\rho):=-\infty\).

### Lemma 22.3: Basic Bounds On The No-Corner Margin

For every \(s\in\mathcal A_{NC}(\rho)\),

```math
S_{NC}(s)\le F_\rho(s)<1.
```

Consequently,

```math
S_{NC}^{max}(\rho)\le F_\rho^{pk}<1.
```

Proof.

Since \(D_{20}(s)\ge0\), \(e^{D_{20}(s)}\ge1\). Hence

```math
S_{NC}(s)
=1+F_\rho(s)-e^{D_{20}(s)}
\le F_\rho(s).
```

Lemma 19.2 gives \(0<F_\rho(s)<1\), and Lemma 5.2 gives the global peak
\(F_\rho(s)\le F_\rho^{pk}\). Taking the supremum over
\(\mathcal A_{NC}(\rho)\) gives the result. `square`

### Theorem 22.4: One-Variable Optimization Criterion

The balanced no-corner branch can pass the post-entry nonsurface worksheet only
if

```math
S_{NC}^{max}(\rho)>0.
```

If \(S_{NC}^{max}(\rho)\le0\), then no choice of \(s\) reaches the final
surface-rate gate. If \(S_{NC}^{max}(\rho)>0\), the exact remaining test is:
find \(s\in\mathcal A_{NC}(\rho)\) such that

```math
\mathcal R_{noncorn}^{SEL2}(s)<S_{NC}(s).
```

Equivalently,

```math
\inf_{s\in\mathcal A_{NC}(\rho)}
\left[
\mathcal R_{noncorn}^{SEL2}(s)-S_{NC}(s)
\right]
<0.
```

Proof.

Theorem 21.7 proves that the post-entry surplus is positive exactly when
\(\mathcal R_{noncorn}^{SEL2}(s)<S_{NC}(s)\) for an admissible \(s\). If
\(S_{NC}^{max}\le0\), the right-hand side is nonpositive everywhere while
\(\mathcal R_{noncorn}^{SEL2}(s)\ge0\), so the strict inequality is impossible.
If \(S_{NC}^{max}>0\), no further formal reduction is available: the branch
passes precisely when the displayed one-variable strict inequality holds for at
least one \(s\). `square`

### Corollary 22.5: Next Computation After Freezing `NCORN`

The active branch is frozen. The next computation is not the surface-rate gate
yet. It is the finite scalar optimization

```math
S_{NC}^{max}(\rho)
=
\sup_{s\in\mathcal A_{NC}(\rho)}
\left[
1+F_\rho(s)-e^{D_{20}(s)}
\right],
```

followed by componentwise comparison of
\(\mathcal R_{noncorn}^{SEL2}(s)\) against this margin. The priority order is:

1. \(X_{13}^{car,SEL2}\) and \(U_{12}^{red,car,SEL2}\), because these are the
   cheapest reduced readout/exact-comparison tails;
2. \(U_{11}^{act,SEL2}(s)\), especially its local and gauge slots;
3. the five exact-entry residuals in \(U_{13}^{entry,act,SEL2}\);
4. the parked Paper-14 export debit \(E_{14}^{park}\), unless the nine-rate
   export audit is reopened.

Only after this comparison succeeds should Paper 21 return to
`P20-SEL2-TREE-RATE-GATE`.

## 23. Componentwise Evaluation Of The Non-Corner Envelope

The active no-corner envelope is

```math
\mathcal R_{noncorn}^{SEL2}(s)
=
E_{14}^{park}
+X_{13}^{car,SEL2}
+U_{12}^{red,car,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,act,SEL2}(s).
```

This section evaluates each term using only the same-record audits already
proved or explicitly parked in Paper 21.

### Definition 23.1: Evaluated Non-Corner Components

The evaluated component values are fixed by the following priority rules.

1. **Paper-14 export.**

   ```math
   E_{14}^{eval}:=E_{14}^{park}.
   ```

   It is zero only if the nine-rate Paper-14 component audit
   \(\mathrm{P20\text{-}SEL2\text{-}P14\text{-}COMP}\) is later proved on the
   same `SEL2` tower.

2. **Exact-comparison debit.** On the strict exact scalar-record branch,
   Section 11 closes the readout half. Hence

   ```math
   X_{13}^{eval}
   :=
   \begin{cases}
   0,
   &
   \mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}
   \text{ is proved},\\[3pt]
   U_{13}^{cut,SEL2},
   &
   \limsup_jD_{13,j}^{cut,SEL2}
   \le U_{13}^{cut,SEL2}<\infty
   \text{ is proved}.
   \end{cases}
   ```

   If neither clause is proved, the no-corner branch is not certified.

3. **Reduced loop-readout debit.** Define

   ```math
   U_{12}^{eval}
   :=
   U_{12}^{per,SEL2}
   +U_{12}^{cusp,SEL2}
   +U_{12}^{smear,SEL2}
   +U_{12}^{P12,SEL2}
   +U_{12}^{appLC,SEL2}
   +U_{12}^{binLC,SEL2}.
   ```

   On the strict exact loop-record branch, Sections 12--14 reduce this to

   ```math
   U_{12}^{eval}=U_{12}^{P12,SEL2},
   ```

   and it becomes zero only if the remaining Paper-12 residual loop/connected
   tail satisfies

   ```math
   \sum_{k\ge j}b_{P12,j,k}^{SEL2}\to0.
   ```

4. **Reduced `T_11` debit.** Define

   ```math
   U_{11}^{eval}(s)
   :=
   U_{11}^{loc,SEL2}(s)
   +U_{11}^{RP,SEL2}(s)
   +U_{11}^{Cov,SEL2}(s)
   +U_{11}^{gauge,SEL2}(s).
   ```

   On the strict perfect-block closed-scalar branch, Lemmas 17.3 and 17.9 give

   ```math
   U_{11}^{eval}(s)
   \le
   U_{11}^{RP,SEL2}(s)
   +U_{11}^{Cov,SEL2}(s).
   ```

   It becomes zero only if the reduced RP and covariance tails vanish
   cofinally.

5. **Exact-entry debit.** Define

   ```math
   U_{13}^{entry,eval}
   :=
   U_{13}^{BC,car}
   +U_{13}^{CE,car}
   +U_{13}^{RPF,car}
   +U_{13}^{KPdec,car}
   +U_{13}^{WP,car}.
   ```

   It becomes zero only if all five same-record entry residuals vanish
   cofinally. In particular, compactness alone does not zero
   \(U_{13}^{BC,car}\), and the entry-level `CE` residual is not the later
   leading coefficient rate.

### Theorem 23.2: Evaluated Non-Corner Envelope

On the active balanced no-corner branch, the certified evaluated envelope is

```math
\mathcal R_{noncorn}^{eval,SEL2}(s)
=
E_{14}^{eval}
+X_{13}^{eval}
+U_{12}^{eval}
+U_{11}^{eval}(s)
+U_{13}^{entry,eval}.
```

The branch passes the nonsurface worksheet exactly if, for some
\(s\in\mathcal A_{NC}(\rho)\),

```math
\mathcal R_{noncorn}^{eval,SEL2}(s)
<
S_{NC}(s).
```

If any component in Definition 23.1 lacks both a zero theorem and a finite
carried ceiling, the no-corner branch is not certified. If the inequality fails
only with these upper ceilings, the certificate fails but the route is not
mathematically falsified without a same-record lower floor.

Proof.

The identity is Definition 22.2 and Theorem 21.7 with the five active
non-corner slots replaced by their evaluated zero-or-carried values from
Definition 23.1. Each component is nonnegative and disjoint by the ledger rules
proved in Sections 9--18 and re-audited for the no-corner selector in Lemmas
21.4--21.5. Therefore the strict pass test is exactly the displayed comparison
with \(S_{NC}(s)\). `square`

### Corollary 23.3: Strict-Branch Reduced Envelope

On the strict exact scalar branch where:

```math
\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}
```

holds, the reduced `T_12` zero audits of Sections 12--14 hold, exact perfect
blocking and scalar gauge-forgetting are used, and the Paper-12 residual
loop/connected tail vanishes, the envelope reduces to

```math
\mathcal R_{noncorn}^{strict,SEL2}(s)
=
E_{14}^{park}
+U_{11}^{RP,SEL2}(s)
+U_{11}^{Cov,SEL2}(s)
+U_{13}^{entry,eval}.
```

If the reduced RP/covariance tails and all five entry residuals also vanish,
then

```math
\mathcal R_{noncorn}^{strict,SEL2}(s)=E_{14}^{park}.
```

Thus, even on the most favorable strict no-corner branch currently written,
Paper 21 still cannot delete \(E_{14}^{park}\) without the Paper-14 nine-rate
audit.

### Corollary 23.4: Current Component Verdict

The componentwise status is:

```math
E_{14}^{park}
\quad\text{carried;}
```

```math
X_{13}^{car,SEL2}
\quad\text{zero only under moving-battery diagonal block convergence;}
```

```math
U_{12}^{red,car,SEL2}
\quad\text{zero only under the reduced Paper-12 tail audits;}
```

```math
U_{11}^{act,SEL2}
\quad\text{reduced on the strict branch to RP plus covariance tails;}
```

```math
U_{13}^{entry,act,SEL2}
\quad\text{the main remaining exact-entry source package.}
```

The next cheapest attack is therefore \(X_{13}^{car,SEL2}\) and
\(U_{12}^{red,car,SEL2}\). The deepest remaining attack is
\(U_{13}^{entry,act,SEL2}\), especially the `BC`, `CE`, `RPF`, `KPdec`, and
`WP` residuals.

## 24. Cheap Reductions And The Reduced `T_11` Attack

This section executes the cheap reductions requested after freezing the
no-corner branch. The rule is the same throughout: set a component to zero only
if the same-record zero audit has actually been proved; otherwise keep the
sharp carried value.

### Lemma 24.1: `X_13` Cannot Yet Be Set To Zero

On the strict exact scalar-record branch, the readout half of \(X_{13}\) is
zero, but the cutoff-to-exact half is zero only under

```math
\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}.
```

The current source package does not prove this gate. Therefore the active
no-corner branch must use

```math
X_{13}^{cheap,SEL2}
:=
\begin{cases}
0,
&
\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}
\text{ is proved},\\[3pt]
U_{13}^{cut,SEL2},
&
\limsup_jD_{13,j}^{cut,SEL2}\le U_{13}^{cut,SEL2}<\infty
\text{ is proved}.
\end{cases}
```

If neither line applies, the branch is not certified.

Proof.

Lemma 11.2 proves \(R_{13,j}^{read,SEL2}=0\) on the strict exact scalar-record
branch. Lemma 11.4 shows that fixed finite-battery convergence does not imply
the moving-battery diagonal convergence needed for
\(\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}\). Theorem 11.5 gives exactly
the displayed zero-or-carried fork. `square`

### Lemma 24.2: Reduced `T_12` Collapses To The Paper-12 Residual Tail

On the active no-corner strict scalar branch, assume:

1. the four Creutz slots use the same Paper-12 calibrated perimeter/cusp
   branches and no unassigned perimeter/cusp residual remains;
2. the readout uses exact renormalized unsmeared loop records, so no smearing
   replacement is made;
3. the loop representatives are the declared scalar records themselves and the
   scalar binning/readout is exact.

Then

```math
U_{12}^{per,SEL2}
=U_{12}^{cusp,SEL2}
=U_{12}^{smear,SEL2}
=U_{12}^{appLC,SEL2}
=U_{12}^{binLC,SEL2}
=0,
```

and

```math
U_{12}^{red,car,SEL2}
=
U_{12}^{P12,SEL2}.
```

Consequently,

```math
U_{12}^{red,car,SEL2}=0
```

is justified only if the remaining Paper-12 residual loop/connected tail obeys

```math
\sum_{k\ge j}b_{P12,j,k}^{SEL2}\to0.
```

Proof.

The perimeter/cusp cancellation is Theorem 12.5 clause 3. The exact unsmeared
record convention is Lemma 13.3. Exact representatives and exact scalar binning
are the `appLC` and `binLC` zero clauses in Lemma 14.5. After those zeroes,
Definition 15.1 leaves only \(U_{12}^{P12,SEL2}\). Lemma 14.5 and Theorem 14.6
show that this final term vanishes exactly when the displayed Paper-12 residual
tail vanishes. `square`

### Corollary 24.3: Cheap Reduction After `X_13` And `T_12`

After the cheap `X_13` and reduced `T_12` attacks, the no-corner envelope is

```math
\mathcal R_{noncorn}^{cheap,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{cheap,SEL2}
+U_{12}^{P12,SEL2}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,eval}.
```

If both

```math
\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}
```

and

```math
\sum_{k\ge j}b_{P12,j,k}^{SEL2}\to0
```

are proved, then this further reduces to

```math
\mathcal R_{noncorn}^{cheap,SEL2}(s)
=
E_{14}^{park}
+U_{11}^{act,SEL2}(s)
+U_{13}^{entry,eval}.
```

Without these two same-record zero audits, \(X_{13}^{cheap,SEL2}\) and/or
\(U_{12}^{P12,SEL2}\) remain carried.

### Lemma 24.4: Local And Gauge `T_11` Slots Are Zero On The Strict Branch

On the active no-corner strict scalar branch,

```math
U_{11}^{loc,SEL2}(s)=0,
\qquad
U_{11}^{gauge,SEL2}(s)=0.
```

Proof.

The local comparison is the Paper-10 perfect same-record pushforward
comparison on the frozen finite scalar battery, so Lemma 17.3 applies and
zeros \(U_{11}^{loc,SEL2}\). The records are closed scalar Wilson-loop records
after gauge-forgetting, so Lemma 17.9 applies and zeros
\(U_{11}^{gauge,SEL2}\). This uses no gauge-fixed state ontology: gauge charts
are proof coordinates only. `square`

### Definition 24.5: Reduced RP/Covariance Remainder

Define the surviving strict-branch `T_11` remainder by

```math
U_{11}^{RPCov,SEL2}(s)
:=
U_{11}^{RP,SEL2}(s)
+U_{11}^{Cov,SEL2}(s).
```

Equivalently,

```math
U_{11}^{act,SEL2}(s)
\le
U_{11}^{RPCov,SEL2}(s)
```

on the strict no-corner scalar branch.

### Theorem 24.6: Reduced `T_11` Is Zero Or Carried By RP/Cov Tails

On the active no-corner strict scalar branch:

1. if

   ```math
   \sum_{k\ge j}D_{11;j,k}^{RP,SEL2}(s)\to0
   ```

   and

   ```math
   \sup_{g\in Euc_{adm}^{SEL2}}
   \sum_{k\ge j}D_{11;j,k}^{Cov,SEL2}(g;s)\to0,
   ```

   then

   ```math
   U_{11}^{act,SEL2}(s)=0;
   ```

2. otherwise the strict branch may carry

   ```math
   U_{11}^{act,SEL2}(s)
   \le
   U_{11}^{RPCov,SEL2}(s)
   ```

   only if both RP and covariance limsups are finite.

Proof.

Lemma 24.4 zeros the local and gauge slots. Lemma 17.5 gives the RP
zero-or-carried fork, and Lemma 17.7 gives the covariance zero-or-carried fork.
Summing the two surviving terms gives the displayed remainder. `square`

### Corollary 24.7: Envelope After Cheap Reductions And `T_11`

The active no-corner envelope is now reduced to

```math
\mathcal R_{noncorn}^{24,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{cheap,SEL2}
+U_{12}^{P12,SEL2}
+U_{11}^{RPCov,SEL2}(s)
+U_{13}^{entry,eval}.
```

It passes the nonsurface worksheet at \(s\in\mathcal A_{NC}(\rho)\) exactly if

```math
\mathcal R_{noncorn}^{24,SEL2}(s)
<
S_{NC}(s).
```

The strict optimistic subbranch is obtained by adding the zero audits
\(\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}\),
\(\sum_{k\ge j}b_{P12,j,k}^{SEL2}\to0\), and the two RP/Cov tail vanishing
conditions. On that subbranch,

```math
\mathcal R_{noncorn}^{24,SEL2}(s)
=
E_{14}^{park}
+U_{13}^{entry,eval}.
```

Thus the cheap reductions do not yet reach the final surface gate unless the
parked Paper-14 export and exact-entry package also fit inside \(S_{NC}(s)\).

## 25. Step 1 Decision: Diagonal Block Convergence For `X_13`

The first cheap live decision is whether \(X_{13}^{cheap,SEL2}\) can be set to
zero. The readout half is already zero by Lemma 11.2. The only remaining issue
is whether cutoff block convergence holds on the moving row batteries
\(B_{13,j}^{exact,SEL2}\).

### Definition 25.1: Rowwise Fixed-Battery Block Convergence

`P21-X13-ROWBC` is the assertion that every row battery
\(B_{13,j}^{exact,SEL2}\) is a declared finite Paper-13 block battery and that,
for each fixed row \(j\),

```math
\lim_{a\downarrow0}
\sup_{F\in B_{13,j}^{exact,SEL2}}
\left|
\mathbb E_{\mu_{a,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|
=0.
```

Equivalently, Paper 13's `BC(s_0,L_j)` gate holds on each row battery.

### Lemma 25.2: Rowwise Convergence Implies The Diagonal Moving Gate

If `P21-X13-ROWBC` holds, then

```math
\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}
```

holds.

Proof.

For each \(j\), Definition 25.1 gives a cutoff threshold
\(a_j^{(0)}>0\) such that for all \(0<a<a_j^{(0)}\),

```math
\sup_{F\in B_{13,j}^{exact,SEL2}}
\left|
\mathbb E_{\mu_{a,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|
< {1\over j}.
```

Choose the actual diagonal cutoff recursively by

```math
a_j
<
\min\{a_j^{(0)},a_{j-1}/2,1/j\}
```

for \(j\ge2\), with \(a_1<a_1^{(0)}\). Then \(a_j\downarrow0\) and

```math
D_{13,j}^{cut,SEL2}
\le {1\over j}
\to0.
```

This is exactly Definition 11.3. `square`

### Lemma 25.3: Source Audit For `P21-X13-ROWBC`

Paper 13 does not prove `P21-X13-ROWBC` unconditionally. It reduces it to the
rowwise block-limit uniqueness gates

```math
\mathrm{BLU}(s_0,L_j)
\qquad
\text{for every row }j,
```

or to rowwise determining finite-block identity ledgers.

Proof.

Paper 13 Theorem 7.30AC proves, for a fixed finite-volume target, that block
convergence `BC(s_0,L)` is equivalent to block-limit uniqueness
`BLU(s_0,L)`. Paper 13 Theorem 7.30AN proves `BLU(s_0,L)` from a determining
finite-block identity ledger with vanishing defect. Applying these theorems to
each \(B_{13,j}^{exact,SEL2}\) would prove Definition 25.1, but the current
Paper-21 source package has not supplied the determining identity ledger and
vanishing-defect estimate for all row batteries. Therefore `P21-X13-ROWBC` is a
real source gate, not a theorem already imported for free. `square`

### Definition 25.4: Finite Carried Fallback For `X_13`

If `P21-X13-ROWBC` is not proved, define the normalized exact-battery envelope

```math
B_X^{SEL2}
:=
\limsup_j
\sup_{F\in B_{13,j}^{exact,SEL2}}
\|F\|_\infty.
```

The finite carried fallback `P21-X13-CARRY(B_X^{SEL2})` asserts

```math
B_X^{SEL2}<\infty.
```

Under this fallback,

```math
0\le X_{13}^{cheap,SEL2}\le 2B_X^{SEL2}.
```

Proof.

For every bounded scalar record \(F\),

```math
\left|
\mathbb E_{\mu_{a,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|
\le
2\|F\|_\infty.
```

Taking the supremum over \(B_{13,j}^{exact,SEL2}\) and then the limsup gives the
displayed bound. If \(B_X^{SEL2}\) is not finite, even the carried `X_13`
fallback has not been certified. `square`

### Theorem 25.5: `X_13` Step-1 Verdict

The exact step-1 decision is:

```math
X_{13}^{cheap,SEL2}
=
\begin{cases}
0,
&
\mathrm{P21\text{-}X13\text{-}ROWBC}\ \text{is proved},\\[4pt]
\le 2B_X^{SEL2},
&
\mathrm{P21\text{-}X13\text{-}CARRY}(B_X^{SEL2})\ \text{is proved}.
\end{cases}
```

The current Paper-21 text proves the diagonal implication

```math
\mathrm{P21\text{-}X13\text{-}ROWBC}
\Longrightarrow
\mathrm{P21\text{-}X13\text{-}DIAG\text{-}BC0}
\Longrightarrow
X_{13}^{cheap,SEL2}=0,
```

but it does not prove `P21-X13-ROWBC` unconditionally. Therefore \(X_{13}\) is
zero only if the rowwise `BC/BLU` source gate is supplied; otherwise it must be
carried by a finite normalized battery envelope.

### Corollary 25.6: Updated Envelope After Step 1

After step 1, the no-corner envelope is

```math
\mathcal R_{noncorn}^{25,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(25),SEL2}
+U_{12}^{P12,SEL2}
+U_{11}^{RPCov,SEL2}(s)
+U_{13}^{entry,eval},
```

where

```math
X_{13}^{(25),SEL2}
=0
```

on the rowwise block-convergence branch, and

```math
0\le X_{13}^{(25),SEL2}\le2B_X^{SEL2}
```

on the finite carried fallback branch. The next cheap decision is therefore the
remaining Paper-12 residual tail \(U_{12}^{P12,SEL2}\), unless the rowwise
`BC/BLU` gate is reopened to eliminate \(X_{13}\) completely.

## 26. Step 1 Freeze: Finite `X_13` Carry On The Dynamic Battery

Section 25 left two honest branches for \(X_{13}\): zero from rowwise
block-convergence, or a finite carry. This section freezes the finite-carry
branch without accidentally charging raw scalar constants whose expectation
discrepancy is identically zero.

### Definition 26.1: Dynamic Exact-Entry Battery

Split the exact-entry battery of Definition 11.1 as

```math
B_{13,j}^{exact,SEL2}
=
B_{13,j}^{dyn,SEL2}
\cup
B_{13,j}^{const,SEL2},
```

where

```math
B_{13,j}^{dyn,SEL2}
:=
B_{13,j}^{Creutz}\cup B_{13,j}^{conn}
```

and \(B_{13,j}^{const,SEL2}\) is the constant-record part containing
\(u_{\rho,s_0,j}, A_{C,j}, B_{C,j}, \xi_{C,j}, \xi'_{C,j}\), and
\(N_j(C)\). Define the dynamic normalized envelope

```math
B_{X,dyn}^{SEL2}
:=
\limsup_j
\sup_{F\in B_{13,j}^{dyn,SEL2}}
\|F\|_\infty.
```

The dynamic finite-carry gate
\(\mathrm{P21\text{-}X13\text{-}DYNCARRY}(B_{X,dyn}^{SEL2})\) asserts

```math
B_{X,dyn}^{SEL2}<\infty.
```

### Lemma 26.2: Constant Records Do Not Enter The Cutoff Discrepancy

For every \(G\in B_{13,j}^{const,SEL2}\),

```math
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}G
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}G
\right|
=0.
```

Consequently

```math
D_{13,j}^{cut,SEL2}
=
\sup_{F\in B_{13,j}^{dyn,SEL2}}
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|.
```

Proof.

The members of \(B_{13,j}^{const,SEL2}\) are declared scalar constants in the
row ledger. They may depend on \(j\) and on the chosen Creutz loop, but once
the row is frozen they are not random variables whose value depends on the
pushed-forward block configuration. Both laws therefore integrate the same
constant. In particular the raw area count \(N_j(C)\) is not charged through a
sup-norm estimate for \(X_{13}\); if it is large, its expectation discrepancy is
still zero. `square`

### Lemma 26.3: Dynamic Battery Has A Finite Uniform Sup-Norm Envelope

Assume the strict scalar `SEL2` branch uses normalized Wilson-loop records
\(|W(C)|\le1\), and that the connected-entry records in
\(B_{13,j}^{conn}\) have uniformly bounded product degree
\(p_{13}^{SEL2}<\infty\) and uniformly bounded scalar coefficient envelope
\(C_{13}^{conn,SEL2}<\infty\). Then

```math
B_{X,dyn}^{SEL2}
\le
\max\{1,\ C_{13}^{conn,SEL2}\,{\mathfrak B}_{p_{13}^{SEL2}}\}
<\infty,
```

where \({\mathfrak B}_p\) is the Bell number bounding a \(p\)-point cumulant of
bounded scalar variables.

Proof.

The four Creutz records are normalized closed Wilson-loop traces, hence have
sup norm at most \(1\). A connected-entry product of at most
\(p_{13}^{SEL2}\) normalized scalar loop records has sup norm at most \(1\).
If \(F_{j,\alpha}^{conn}\) is written as a finite cumulant or connected
linear combination of such products, the universal moment-cumulant expansion
contains at most \({\mathfrak B}_{p_{13}^{SEL2}}\) partition terms. Multiplying
by the declared coefficient envelope gives
\(\|F_{j,\alpha}^{conn}\|_\infty\le
C_{13}^{conn,SEL2}{\mathfrak B}_{p_{13}^{SEL2}}\), uniformly in \(j\) and
\(\alpha\). Taking the supremum over the dynamic battery and then the limsup
gives the displayed bound. `square`

### Theorem 26.4: Frozen `X_13` Branch

On the active exact scalar-record branch,

```math
X_{13}^{(26),SEL2}
=
\begin{cases}
0,
&
\mathrm{P21\text{-}X13\text{-}ROWBC}\ \text{is proved},
\\[4pt]
\le
2B_{X,dyn}^{SEL2},
&
\mathrm{P21\text{-}X13\text{-}DYNCARRY}(B_{X,dyn}^{SEL2})\ \text{is proved}.
\end{cases}
```

Under the normalized finite-product hypotheses of Lemma 26.3, the second
branch is certified with

```math
X_{13}^{(26),SEL2}
\le
2\max\{1,\ C_{13}^{conn,SEL2}{\mathfrak B}_{p_{13}^{SEL2}}\}.
```

Proof.

The zero branch is Theorem 25.5. On the finite-carry branch, Lemma 26.2 removes
the constant records from the cutoff discrepancy. For every dynamic record,

```math
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|
\le2\|F\|_\infty.
```

Taking the supremum over \(B_{13,j}^{dyn,SEL2}\) and the limsup gives
\(X_{13}^{(26),SEL2}\le2B_{X,dyn}^{SEL2}\). Lemma 26.3 supplies the displayed
explicit finite ceiling on the strict normalized branch. `square`

The Barandes-aligned interpretation is narrow: this is not block convergence
and not a source estimate for confinement. It is only the certification that,
if the moving-row convergence gate is not closed, the exact-comparison slot can
still be carried as a finite same-record scalar debit.

## 27. Step 2 Decision: Paper-12 Residual Tail

After Sections 14, 15, and 24, the reduced \(T_{12}\) bucket has collapsed to
one live term:

```math
U_{12}^{red,car,SEL2}=U_{12}^{P12,SEL2}.
```

The perimeter, cusp, smearing, loop-representative, and scalar-binning pieces
are zero on the strict exact scalar-record branch. The only remaining question
is whether the Paper-12 residual AF loop-variation and connected-polymer tails
vanish on the moving `SEL2` row schedule.

### Definition 27.1: Rowwise Paper-12 Residual Tail Gate

`P21-T12-P12-ROWSUM` is the assertion that every row loop battery
\(B_{12,j}^{app,SEL2}\) is a finite admissible Paper-12 loop battery and that
there are nonnegative same-record residual bounds

```math
b_{P12,j,k}^{SEL2}
=
\theta_{P12,j,k}^{tail,SEL2}
+\theta_{P12,j,k}^{conn,SEL2}
```

such that, for each fixed row \(j\),

```math
\sum_{k\ge K}b_{P12,j,k}^{SEL2}\to0
\qquad(K\to\infty).
```

The diagonal zero-strength version `P21-T12-P12-DIAG0` asserts that the row
schedule has been chosen so that

```math
\sum_{k\ge j}b_{P12,j,k}^{SEL2}\to0.
```

### Lemma 27.2: Paper-12 Applies To The Strict `SEL2` Loop Rows

On the strict no-corner `SEL2` branch, each row \(B_{12,j}^{app,SEL2}\) is a
finite admissible Paper-12 loop battery, provided the active Creutz rectangles
are nondegenerate and the row keeps the declared positive separation and cusp
angle margins.

Proof.

The active Creutz records are scalar closed Wilson-loop records on
axis-aligned nondegenerate rectangles. Each such rectangle is a piecewise
\(C^2\) embedded loop with four right-angle cusps, finite perimeter, no
self-intersection, and positive separation between nonadjacent arcs whenever
the rectangle side lengths stay in the declared nondegenerate window. Finite
products and cumulants of the row records remain a finite Paper-12 battery
with bounded representation and bounded product degree. These are exactly the
finite admissible loop-battery hypotheses used by Paper 12 Theorem 6.1. `square`

### Lemma 27.3: Rowwise Paper-12 Summability Gives The Diagonal Zero Tail

If `P21-T12-P12-ROWSUM` holds, then after passing to a cofinal diagonal row
schedule, `P21-T12-P12-DIAG0` holds.

Proof.

For each fixed row \(j\), Definition 27.1 gives a shell threshold \(K_j\) such
that

```math
\sum_{k\ge K_j}b_{P12,j,k}^{SEL2}< {1\over j}.
```

Refine the row schedule cofinally so that the displayed shell threshold is the
new row index lower bound. Relabeling this cofinal subsequence gives

```math
\sum_{k\ge j}b_{P12,j,k}^{SEL2}\le {1\over j}\to0.
```

This is precisely `P21-T12-P12-DIAG0`. `square`

### Theorem 27.4: `U_12^{P12}` Is Zero Or Explicitly Carried

On the strict exact scalar-record branch:

1. If the Paper-12 finite-battery hypotheses of Theorem 6.1 hold rowwise and
   the residual bounds satisfy `P21-T12-P12-ROWSUM`, then

   ```math
   U_{12}^{P12,SEL2}=0
   ```

   on the cofinal diagonal row schedule.

2. If only a finite residual ceiling is proved,

   ```math
   \limsup_j\sum_{k\ge j}b_{P12,j,k}^{SEL2}
   \le
   U_{12}^{P12,bd,SEL2}
   <\infty,
   ```

   then

   ```math
   U_{12}^{P12,SEL2}
   \le
   U_{12}^{P12,bd,SEL2}.
   ```

3. If neither the diagonal zero tail nor a finite residual ceiling is proved,
   the non-corner carried worksheet is not certified.

Proof.

Clause 1 combines Lemma 27.2, Paper 12 Theorem 6.1 on each finite row battery,
and Lemma 27.3. Clause 2 is Definition 14.2. Clause 3 is the finite-ledger
requirement: every debit in \(\mathcal W_{car}\) must be a proved zero or a
proved finite scalar ceiling. `square`

### Corollary 27.5: Envelope After Steps 1--2

After freezing the \(X_{13}\) branch and deciding the Paper-12 residual tail,
the active no-corner envelope is

```math
\mathcal R_{noncorn}^{27,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,SEL2}(s)
+U_{13}^{entry,eval},
```

where

```math
X_{13}^{(26),SEL2}
\in
\left\{0,\ [0,2B_{X,dyn}^{SEL2}]\right\}
```

according to the rowwise block-convergence or dynamic-carry branch, and

```math
U_{12}^{(27),SEL2}
=
\begin{cases}
0,
&
\mathrm{P21\text{-}T12\text{-}P12\text{-}DIAG0}\ \text{is proved},
\\[4pt]
\le U_{12}^{P12,bd,SEL2},
&
\text{a finite Paper-12 residual ceiling is proved}.
\end{cases}
```

Thus the next live nonsurface terms are exactly
\(U_{11}^{RPCov,SEL2}\) and \(U_{13}^{entry,eval}\), plus the parked
Paper-14 export and whichever branch value is selected for \(X_{13}\).

## 28. Attack \(U_{11}^{RPCov,SEL2}\)

The strict scalar branch has already zeroed the local and gauge slots:

```math
U_{11}^{loc,SEL2}=U_{11}^{gauge,SEL2}=0.
```

Thus the remaining `T_11` debit is exactly

```math
U_{11}^{RPCov,SEL2}(s)
=
U_{11}^{RP,SEL2}(s)+U_{11}^{Cov,SEL2}(s).
```

This section evaluates that remainder against Paper 16's `HK-RP-LEDGER` and
`HK-COV-LEDGER`, with all perimeter/cusp, smearing, loop-readout, binning, and
Paper-12 residual tails excluded from `T_11`.

### Definition 28.1: Strict Reduced RP Defect

On the strict exact scalar-record branch, the `T_11`-exclusive RP defect is

```math
D_{11;j,k}^{RP,red,SEL2}(s)
:=
\eta_{projRP,j,k}^{SEL2}(s)
+\eta_{regRP,j,k}^{SEL2}(s)
+\eta_{volRP,j,k}^{SEL2}(s).
```

The counterterm and binning RP defects in Paper 16 are not included:

```math
\eta_{ctRP,j,k}^{11,SEL2}
=
\eta_{binRP,j,k}^{11,SEL2}
=0
```

on this branch, because perimeter/cusp/counterterm and readout debts have
already been assigned to the reduced Paper-12/T12 ledger or eliminated by exact
scalar records.

Define the carried RP ceiling

```math
U_{11}^{RP,bd,SEL2}(s)
:=
\limsup_j
\sum_{k\ge j}
D_{11;j,k}^{RP,red,SEL2}(s).
```

The zero-strength RP tail gate `P21-U11-RP-DIAG0` asserts

```math
\sum_{k\ge j}
D_{11;j,k}^{RP,red,SEL2}(s)\to0.
```

### Definition 28.2: Strict Reduced Covariance Defect

Let \(G_{adm}^{SEL2}\) be the Euclidean-motion family demanded by the active
branch. For the exact hypercubic subbranch, \(G_{adm}^{SEL2}\) is the finite
set of hypercubic symmetries preserving the row battery, block/collar
template, finite volume, and reflection structure. For a continuum Euclidean
motion branch, \(G_{adm}^{SEL2}\) also contains the declared continuum motions
and their lattice/block approximant maps.

Define

```math
D_{11;j,k}^{Cov,red,SEL2}(g;s)
:=
\eta_{exactCov,j,k}^{11,SEL2}(g;s)
+\eta_{blockCov,j,k}^{11,SEL2}(g;s)
+\eta_{projCov,j,k}^{SEL2}(g;s)
+\eta_{regCov,j,k}^{SEL2}(g;s)
+\eta_{volCov,j,k}^{SEL2}(g;s)
+\eta_{appCov,j,k}^{11,SEL2}(g;s).
```

The readout and counterterm covariance defects are excluded:

```math
\eta_{binCov,j,k}^{11,SEL2}(g)
=
\eta_{ctCov,j,k}^{11,SEL2}(g)
=0
```

on the strict exact scalar-record branch. In the exact hypercubic subbranch,
\(\eta_{exactCov}^{11}=\eta_{appCov}^{11}=0\). If the hypercubic symmetry
also preserves the chosen block/collar template, then
\(\eta_{blockCov}^{11}=0\) as well. Continuum rotations/translations are not
given this zero for free; their approximant, block, and volume-buffer terms
remain part of \(D_{11}^{Cov,red}\).

Define the carried covariance ceiling

```math
U_{11}^{Cov,bd,SEL2}(s)
:=
\sup_{g\in G_{adm}^{SEL2}}
\limsup_j
\sum_{k\ge j}
D_{11;j,k}^{Cov,red,SEL2}(g;s).
```

The zero-strength covariance tail gate `P21-U11-COV-DIAG0` asserts

```math
\sup_{g\in G_{adm}^{SEL2}}
\sum_{k\ge j}
D_{11;j,k}^{Cov,red,SEL2}(g;s)\to0.
```

### Lemma 28.3: Paper 16 Supplies The Correct Ledger, Not Automatic Zero

Paper 16 proves that the RP and covariance losses are contained in the
declared ledgers. It does not by itself prove the moving-row diagonal limits
`P21-U11-RP-DIAG0` and `P21-U11-COV-DIAG0` on the active `SEL2` row schedule.

Proof.

Paper 16 Definition 9W.1C defines \(D_{j,k}^{RP}\) as the sum of counterterm,
binning, projective, regulator, and volume RP defects. Theorem 9W.1D proves
that this ledger gives the RP half of `HK-RPCOV-CLOSE`. On the strict scalar
branch, Definition 28.1 removes the counterterm and binning pieces because
they are already either exact or paid outside `T_11`.

Similarly, Paper 16 Definition 9W.1G defines \(D_{j,k}^{Cov}(g)\) as the sum
of exact-symmetry, approximant, binning, counterterm, block/collar,
projective, regulator, and volume defects. Theorem 9W.1H proves that this
ledger gives the covariance half of `HK-RPCOV-CLOSE`. Definition 28.2 keeps
only the disjoint `T_11` pieces.

Those Paper-16 theorems identify the correct operational debit. They do not
turn a finite-row or pointwise defect statement into the moving-row diagonal
tail \(\sum_{k\ge j}D_{j,k}\to0\) without a cofinal tail estimate on the same
row schedule. `square`

### Lemma 28.4: Rowwise Paper-16 Tails Give The Diagonal RP/Cov Zero Gates

Assume that, for every fixed row battery, the reduced Paper-16 RP and
covariance tails are summable and satisfy:

```math
\sum_{k\ge K}D_{11;j,k}^{RP,red,SEL2}(s)\to0,
\qquad K\to\infty,
```

and

```math
\sup_{g\in G_{adm}^{SEL2}}
\sum_{k\ge K}D_{11;j,k}^{Cov,red,SEL2}(g;s)\to0,
\qquad K\to\infty.
```

If the `SEL2` selector permits the usual cofinal diagonal pairing of row
batteries with cutoff shells, then `P21-U11-RP-DIAG0` and
`P21-U11-COV-DIAG0` hold on the relabeled cofinal schedule.

Proof.

For each fixed row \(j\), choose a shell threshold \(K_j^{RP}\) such that the
reduced RP tail is \(<1/(2j)\), and choose \(K_j^{Cov}\) such that the
uniform reduced covariance tail is \(<1/(2j)\). Use the cofinal selector to
pair the row battery with a cutoff shell lower bound at least
\(\max\{K_j^{RP},K_j^{Cov}\}\). Relabel this cofinal subsequence as the new
row schedule. Then both displayed row tails are bounded by \(1/(2j)\), hence
both diagonal tails vanish. `square`

This lemma is a diagonal scheduling result, not a proof of the rowwise
Paper-16 estimates themselves.

### Theorem 28.5: `U_11^{RPCov}` Is Zero Or Explicitly Carried

On the active no-corner strict scalar branch:

1. If `P21-U11-RP-DIAG0` and `P21-U11-COV-DIAG0` hold, then

   ```math
   U_{11}^{RPCov,SEL2}(s)=0.
   ```

2. If finite ceilings are proved,

   ```math
   U_{11}^{RP,bd,SEL2}(s)<\infty,
   \qquad
   U_{11}^{Cov,bd,SEL2}(s)<\infty,
   ```

   then

   ```math
   U_{11}^{RPCov,SEL2}(s)
   \le
   U_{11}^{RP,bd,SEL2}(s)
   +U_{11}^{Cov,bd,SEL2}(s).
   ```

3. If either finite ceiling is not proved, the `T_11` branch is not certified.

Proof.

Lemma 24.4 gives \(U_{11}^{loc}=U_{11}^{gauge}=0\). Lemma 28.3 identifies the
surviving disjoint RP and covariance defects from Paper 16. If the two
diagonal zero gates hold, Lemmas 17.5 and 17.7 give
\(U_{11}^{RP}=U_{11}^{Cov}=0\). Otherwise Definitions 28.1 and 28.2 give the
finite carried ceilings, and the displayed inequality follows by summing the
two nonnegative components. `square`

### Corollary 28.6: Envelope After The `T_11` Attack

After the \(U_{11}^{RPCov}\) audit, the no-corner envelope becomes

```math
\mathcal R_{noncorn}^{28,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{(28),SEL2}(s)
+U_{13}^{entry,eval},
```

where

```math
U_{11}^{(28),SEL2}(s)
=
\begin{cases}
0,
&
\mathrm{P21\text{-}U11\text{-}RP\text{-}DIAG0}
\ \text{and}\
\mathrm{P21\text{-}U11\text{-}COV\text{-}DIAG0}\ \text{hold},
\\[4pt]
\le
U_{11}^{RP,bd,SEL2}(s)
+U_{11}^{Cov,bd,SEL2}(s),
&
\text{finite reduced RP/Cov ceilings are proved}.
\end{cases}
```

No perimeter/cusp, smearing, loop-readout, binning, or Paper-12 residual term
appears in \(U_{11}^{(28),SEL2}\). The next genuinely live nonsurface bucket is
therefore \(U_{13}^{entry,eval}\), unless one first reopens the Paper-16
rowwise RP/Cov tail estimates to turn the carried \(U_{11}\) ceiling into zero.

## 29. Decision: Carry \(U_{11}^{RPCov,SEL2}\) On The Present Source Package

Section 28 identified the exact zero gates for the reduced RP/covariance
transport slot. This section decides whether the present paper actually
reopens those gates. It does not: the available Paper-16 import supplies the
correct fixed-battery ledgers, but not the moving-row rate data needed to prove
the `SEL2` diagonal zero tails.

### Definition 29.1: Missing Moving-Row RP/Cov Rate Data

`P21-U11-RPCOV-RATEDATA` is the assertion that there are explicit nonnegative
row-shell envelopes \(r_{RP;j,k}^{SEL2}(s)\) and
\(r_{Cov;j,k}^{SEL2}(g;s)\) such that

```math
D_{11;j,k}^{RP,red,SEL2}(s)
\le
r_{RP;j,k}^{SEL2}(s),
```

```math
D_{11;j,k}^{Cov,red,SEL2}(g;s)
\le
r_{Cov;j,k}^{SEL2}(g;s),
```

and

```math
\sum_{k\ge j}r_{RP;j,k}^{SEL2}(s)\to0,
\qquad
\sup_{g\in G_{adm}^{SEL2}}
\sum_{k\ge j}r_{Cov;j,k}^{SEL2}(g;s)\to0.
```

This is stronger than fixed-row Paper-16 summability. It is the actual
same-record rate data required to prove `P21-U11-RP-DIAG0` and
`P21-U11-COV-DIAG0` on the moving `SEL2` row schedule.

### Lemma 29.2: Paper 16 Does Not Supply `P21-U11-RPCOV-RATEDATA`

The Paper-16 `HK-RP-LEDGER` and `HK-COV-LEDGER` do not, as written, supply
`P21-U11-RPCOV-RATEDATA`.

Proof.

Paper 16 Definition 9W.1C states the reflection-positivity ledger for every
fixed finite OS battery \(B_j\), with a defect \(D_{j,k}^{RP}\), fixed-row
summability, and \(D_{j,k}^{RP}\to0\) along the refinement shell. Paper 16
Definition 9W.1G states the analogous covariance ledger
\(D_{j,k}^{Cov}(g)\) for fixed finite batteries and admissible motions.

Those statements identify and control the correct defect family for a fixed
finite battery. They do not provide an explicit envelope uniform enough in the
moving row index \(j\) to conclude

```math
\sum_{k\ge j}D_{11;j,k}^{RP,red,SEL2}\to0,
\qquad
\sup_g\sum_{k\ge j}D_{11;j,k}^{Cov,red,SEL2}(g)\to0.
```

Such a conclusion requires either the envelopes of Definition 29.1 or an
equivalent diagonal rate theorem on the same `SEL2` scalar record tower.
Therefore Paper 16 gives the ledger source, not the present moving-row zero
proof. `square`

### Definition 29.3: Carried RP/Cov Ceiling

On the present source package define the carried `T_11` ceiling by

```math
U_{11}^{RPCov,car,SEL2}(s)
:=
U_{11}^{RP,bd,SEL2}(s)
+U_{11}^{Cov,bd,SEL2}(s).
```

The carried branch is certified only under the finite-ceiling gate
`P21-U11-RPCOV-CARRY`, namely

```math
U_{11}^{RP,bd,SEL2}(s)<\infty,
\qquad
U_{11}^{Cov,bd,SEL2}(s)<\infty.
```

If this finite-ceiling gate fails, the `SEL2` no-corner carried worksheet is
not even finitely certified.

### Theorem 29.4: Present Decision For \(U_{11}^{RPCov,SEL2}\)

On the current Paper-21 source package, \(U_{11}^{RPCov,SEL2}\) is carried,
not zeroed:

```math
U_{11}^{RPCov,SEL2}(s)
\le
U_{11}^{RPCov,car,SEL2}(s)
=
U_{11}^{RP,bd,SEL2}(s)
+U_{11}^{Cov,bd,SEL2}(s),
```

provided `P21-U11-RPCOV-CARRY` holds. The zero alternative is parked as the
separate future source gate

```math
\mathrm{P21\text{-}U11\text{-}RPCOV\text{-}RATEDATA}.
```

Proof.

By Lemma 29.2, the present imports do not prove the two diagonal zero gates.
Theorem 28.5 then leaves only the finite carried branch. Definition 29.3 names
the carried ceiling. No loop-readout, perimeter/cusp, smearing, binning,
Paper-12 residual, or exact-entry term is included in it. `square`

### Corollary 29.5: Envelope After Carrying \(U_{11}^{RPCov}\)

The active no-corner envelope for the next stage is

```math
\mathcal R_{noncorn}^{29,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{entry,eval}.
```

Equivalently, substituting the carried ceiling,

```math
\mathcal R_{noncorn}^{29,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RP,bd,SEL2}(s)
+U_{11}^{Cov,bd,SEL2}(s)
+U_{13}^{entry,eval}.
```

Thus the next proof target is \(U_{13}^{entry,eval}\), unless a new
moving-row Paper-16 rate theorem is supplied and the paper deliberately
reopens `P21-U11-RPCOV-RATEDATA`.

## 30. Attack \(U_{13}^{entry,eval}\): `BC` And `CE`

The exact-entry bucket is now the main live nonsurface term:

```math
U_{13}^{entry,eval}
=
U_{13}^{BC}
+U_{13}^{CE}
+U_{13}^{RPF}
+U_{13}^{KPdec}
+U_{13}^{WP}.
```

This section attacks the first two components. `BC` decides whether the exact
block law being used downstream is really the same same-record limit of the
cutoff block pushforwards. `CE` decides whether the exact block plaquette
marginal is a legitimate central character object before any surface-rate
claim is made.

### Definition 30.1: Entry `BC` Battery And The No-Double-Charge Split

Let \(\mathcal B_{BC,j}^{SEL2}\) be the Paper-13 exact-entry block battery used
by row \(j\). It contains the active Creutz records, the connected-entry
products, and the scalar plaquette/coefficient records required by `CE`,
`RPF`, `KPdec`, and `WP`.

The \(X_{13}\) audit already compares cutoff and exact expectations on
\(B_{13,j}^{exact,SEL2}\). Therefore define the genuinely additional entry
block-convergence battery by

```math
\mathcal B_{BC,j}^{add,SEL2}
:=
\mathcal B_{BC,j}^{SEL2}
\setminus
B_{13,j}^{exact,SEL2},
```

where equality is understood modulo records that are literally the same
declared scalar function on the same pushed-forward row law. The reduced
entry `BC` residual is

```math
\epsilon_{BC,j}^{add,SEL2}
:=
\sup_{F\in\mathcal B_{BC,j}^{add,SEL2}}
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|.
```

If \(\mathcal B_{BC,j}^{add,SEL2}=\varnothing\), the supremum is \(0\). Define

```math
U_{13}^{BC,add}
:=
\limsup_j\epsilon_{BC,j}^{add,SEL2}.
```

The active envelope must use \(U_{13}^{BC,add}\), not a second copy of the
same block-convergence discrepancy already carried by \(X_{13}^{(26),SEL2}\).

### Lemma 30.2: `BC` Is Zero On The Covered-Battery Branch

If, cofinally,

```math
\mathcal B_{BC,j}^{SEL2}
\subseteq
B_{13,j}^{exact,SEL2}
```

as same-record scalar functions, then

```math
U_{13}^{BC,add}=0.
```

Proof.

Under the displayed inclusion, the additional battery
\(\mathcal B_{BC,j}^{add,SEL2}\) is empty cofinally. The reduced residual in
Definition 30.1 is therefore zero for every sufficiently large row. `square`

This does not prove block convergence. It says only that the block-convergence
debit has already been paid or carried in \(X_{13}^{(26),SEL2}\) and must not
be paid again inside \(U_{13}^{entry,eval}\).

### Definition 30.3: Additional `BC` Carry And Zero Gate

If the covered-battery branch of Lemma 30.2 does not hold, define

```math
B_{BC,add}^{SEL2}
:=
\limsup_j
\sup_{F\in\mathcal B_{BC,j}^{add,SEL2}}\|F\|_\infty.
```

The finite carry gate `P21-U13-BC-ADDCARRY` asserts

```math
B_{BC,add}^{SEL2}<\infty,
```

in which case

```math
0\le U_{13}^{BC,add}\le2B_{BC,add}^{SEL2}.
```

The zero gate `P21-U13-BC-ADDBLU` asserts block-limit uniqueness on the
additional finite record algebra:

```math
\epsilon_{BC,j}^{add,SEL2}\to0.
```

By Paper 13 Theorem 7.30AC, this is equivalent to `BLU` on the additional
finite block-record algebra; by Paper 13 Theorem 7.30AN, it follows from a
determining finite-block identity ledger with vanishing defect on the same
additional records.

### Theorem 30.4: Present `BC` Decision

On the active no-corner `SEL2` branch,

```math
U_{13}^{BC}
\rightsquigarrow
U_{13}^{BC,add}.
```

Moreover:

1. if the entry `BC` battery is covered by \(B_{13,j}^{exact,SEL2}\) cofinally,
   then \(U_{13}^{BC,add}=0\);
2. if `P21-U13-BC-ADDBLU` is proved, then \(U_{13}^{BC,add}=0\);
3. if only `P21-U13-BC-ADDCARRY` is proved, then

   ```math
   U_{13}^{BC,add}\le2B_{BC,add}^{SEL2};
   ```

4. otherwise the exact-entry bucket is not finitely certified.

Proof.

Definition 30.1 removes the part of `BC` already included in the \(X_{13}\)
cutoff-to-exact comparison. Lemma 30.2 proves the covered-battery zero branch.
The `ADDBLU` branch is Paper 13 Theorem 7.30AC applied to the remaining
finite record algebra. The finite carry is the elementary bounded-expectation
estimate
\(|\mathbb E_\mu F-\mathbb E_\nu F|\le2\|F\|_\infty\). `square`

### Definition 30.5: Entry `CE` Split

Split the central-extraction entry residual into a regularity part and a
coefficient-window part:

```math
\epsilon_{CE,j}^{SEL2}
\le
\epsilon_{CE\text{-}reg,j}^{SEL2}
+\epsilon_{CE\text{-}win,j}^{SEL2}.
```

The regularity part asserts that the row-\(j\) block plaquette marginal has a
central Haar density \(K_{p,j}^{SEL2}\) with a Peter-Weyl expansion and a
rowwise finite weighted character tail. The coefficient-window part contains
the remaining exact-entry character data:

```math
0<k_{\rho,j}^{SEL2}<1,
```

and a finite non-leading character tail sufficient for Paper 13 `CE`:

```math
\sum_{\lambda\ne0,\rho}d_\lambda |k_{\lambda,j}^{SEL2}|
<\infty
```

with whatever cofinal limsup bound the active entry ledger requires. This
coefficient-window residual is not the later surface-leading rate
\(\kappa_{13}^{CE}\), although the later rate gate may use the same
coefficients.

Define

```math
U_{13}^{CE,reg}
:=
\limsup_j\epsilon_{CE\text{-}reg,j}^{SEL2},
\qquad
U_{13}^{CE,win}
:=
\limsup_j\epsilon_{CE\text{-}win,j}^{SEL2}.
```

Then

```math
U_{13}^{CE,car}
\le
U_{13}^{CE,reg}+U_{13}^{CE,win}.
```

### Lemma 30.6: Finite Heat-Kernel Rows Close `CE-REG`, Not `CE-WIN`

On the finite heat-kernel row branch of Paper 20 Theorem 4.3A.147,

```math
U_{13}^{CE,reg}=0.
```

This does not imply

```math
U_{13}^{CE,win}=0.
```

Proof.

Paper 20 Theorem 4.3A.147 proves `P20-SEL2-CE-REG^+` for finite heat-kernel
rows: the block plaquette readout is a smooth submersion of a compact finite
link space carrying a smooth heat-kernel density, so its pushforward has a
central smooth Haar density. Paper 20 Lemma 4.3A.146 then gives the
heat-regularized Peter-Weyl expansion and rowwise finite weighted character
tail. Therefore the regularity residual vanishes on that branch.

But Paper 20 Corollary 4.3A.148 explicitly separates regularity from the
coefficient-window content: sign, subunit, positive rate, and the cofinal
non-leading tail bound are not consequences of smoothness alone. `square`

### Lemma 30.7: Exact Weak-Limit `CE-REG` Is Not Automatic

If the active block plaquette marginal is interpreted as an already-taken
weak continuum limit rather than a finite heat-kernel row marginal, then
`CE-REG` is a source gate unless a same-record regularity theorem is supplied.

Proof.

Weak limits of absolutely continuous probability measures on a compact group
can be singular. Positivity, normalization, and centrality therefore do not
imply an \(L^1\) Haar density, let alone a Peter-Weyl expansion with finite
weighted tail. Paper 20 Honest Boundary 4.3A.149 records the needed
replacement sources: uniform integrability, total-variation convergence, or a
uniform Sobolev bound strong enough to pass the density and tail to the
limit. `square`

### Definition 30.8: Present `CE` Branch

The active Paper-21 source package chooses the finite heat-kernel row
regularity branch for the entry `CE` audit:

```math
U_{13}^{CE,reg}=0.
```

The remaining coefficient-window carry is

```math
U_{13}^{CE,car}
\le
U_{13}^{CE,win,car},
```

where `P21-U13-CE-WIN-CARRY` asserts

```math
U_{13}^{CE,win,car}<\infty.
```

The zero branch `P21-U13-CE-WIN0` asserts

```math
\epsilon_{CE\text{-}win,j}^{SEL2}\to0.
```

This zero branch requires same-record coefficient-window estimates: positivity
and subunitness of the selected channel, plus a cofinal finite non-leading
character-tail budget. It may not be inferred from `CE-REG^+` alone.

### Theorem 30.9: `BC/CE` Entry Status After The Attack

After the `BC/CE` attack, the active exact-entry bucket is bounded by

```math
U_{13}^{entry,eval}
\le
U_{13}^{BC,add}
+U_{13}^{CE,win,car}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car},
```

on the finite heat-kernel row `CE-REG` branch and the reduced `SUB` placement
branch.

The `BC` term is zero if either the entry `BC` battery is already covered by
the \(X_{13}\) exact-entry battery, or the additional block-limit uniqueness
gate `P21-U13-BC-ADDBLU` is proved. Otherwise it is carried by
\(2B_{BC,add}^{SEL2}\), if finite.

The `CE` regularity term is zero on finite heat-kernel rows, but the
coefficient-window term remains carried unless `P21-U13-CE-WIN0` is proved.

Proof.

The `BC` clauses are Theorem 30.4. The `CE` clauses are Lemmas 30.6--30.7 and
Definition 30.8. Substituting them into the five-term exact-entry bound of
Theorem 18.9 gives the displayed reduced entry ceiling. `square`

### Corollary 30.10: Envelope After The `BC/CE` Attack

The active no-corner envelope is now

```math
\mathcal R_{noncorn}^{30,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,add}
+U_{13}^{CE,win,car}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car}.
```

The next exact-entry targets are \(RPF\), \(KPdec\), and \(WP\). The paper
should not return to the final surface-leading-rate inequality until those
three terms are either zeroed or finitely carried on the same scalar record
law.

## 31. Decisions For \(U_{13}^{BC,add}\) And \(U_{13}^{CE,win}\)

This section executes the two cheap decisions left by Section 30. The outcome
is deliberately conservative: the part of `BC` already present in the
\(X_{13}\) battery is zero, but the additional entry records are not declared
zero without a new block-limit uniqueness theorem; and `CE-REG` remains closed
while `CE-WIN` is carried as the exact coefficient-window obstruction.

### Definition 31.1: Covered And New `BC` Records

Split the additional entry `BC` battery into the part literally covered by
Definition 11.1 and the part not yet covered:

```math
\mathcal B_{BC,j}^{SEL2}
=
\mathcal B_{BC,j}^{cov,SEL2}
\cup
\mathcal B_{BC,j}^{new,SEL2}.
```

The covered part is the same-record scalar subbattery

```math
\mathcal B_{BC,j}^{cov,SEL2}
:=
\mathcal B_{BC,j}^{SEL2}
\cap
B_{13,j}^{exact,SEL2},
```

where equality means equality as scalar functions on the same pushed-forward
row law. Concretely, this includes:

1. the four active Creutz loop records;
2. the connected-entry products \(F_{j,\alpha}^{conn}\);
3. the already declared surface constants
   \(u_{\rho,s_0,j},A_{C,j},B_{C,j},\xi_{C,j},\xi'_{C,j},N_j(C)\), when used
   only as scalar constants.

The new part is

```math
\mathcal B_{BC,j}^{new,SEL2}
:=
\mathcal B_{BC,j}^{SEL2}
\setminus
\mathcal B_{BC,j}^{cov,SEL2}.
```

It contains only scalar records required for the entry `CE`, `RPF`, `KPdec`,
or `WP` audits that are not literally in \(B_{13,j}^{exact,SEL2}\). If a new
record is assigned to one of those component slots with its own
cutoff-to-exact tolerance, it is removed from the free `BC` carry to avoid a
second charge.

### Lemma 31.2: The Covered `BC` Part Has Zero Additional Debit

The covered part contributes no new entry `BC` debit:

```math
U_{13}^{BC,cov}=0.
```

Proof.

Every element of \(\mathcal B_{BC,j}^{cov,SEL2}\) is already an element of the
exact-entry battery \(B_{13,j}^{exact,SEL2}\). The cutoff-to-exact discrepancy
for these records is exactly the discrepancy already paid or carried in
\(X_{13}^{(26),SEL2}\). The reduced `BC` definition removes this covered
subbattery, so its residual supremum is empty after the no-double-charge
projection. `square`

### Definition 31.3: Free New `BC` Carry

Let

```math
\epsilon_{BC,j}^{new,SEL2}
:=
\sup_{F\in\mathcal B_{BC,j}^{new,SEL2}}
\left|
\mathbb E_{\mu_{a_j,s_0}^{blk,SEL2}}F
-
\mathbb E_{\mu_{s_0}^{blk,SEL2}}F
\right|,
```

after deleting records whose cutoff-to-exact tolerance is already assigned to
`CE`, `RPF`, `KPdec`, or `WP`. Define

```math
U_{13}^{BC,new}
:=
\limsup_j\epsilon_{BC,j}^{new,SEL2},
\qquad
B_{BC,new}^{SEL2}
:=
\limsup_j
\sup_{F\in\mathcal B_{BC,j}^{new,SEL2}}\|F\|_\infty .
```

The zero gate `P21-U13-BC-NEWBLU` asserts

```math
\epsilon_{BC,j}^{new,SEL2}\to0.
```

The finite carry gate `P21-U13-BC-NEWCARRY` asserts

```math
B_{BC,new}^{SEL2}<\infty.
```

Under `P21-U13-BC-NEWCARRY`,

```math
0\le U_{13}^{BC,new}\le2B_{BC,new}^{SEL2}.
```

### Theorem 31.4: Present `BC` Decision

On the current `SEL2` source package,

```math
U_{13}^{BC,add}
\rightsquigarrow
U_{13}^{BC,new}.
```

Moreover:

1. the covered `BC` subbattery is zero by Lemma 31.2;
2. \(U_{13}^{BC,new}=0\) only if `P21-U13-BC-NEWBLU` is proved, or if
   \(\mathcal B_{BC,j}^{new,SEL2}=\varnothing\) cofinally after the component
   slot assignment;
3. without that zero gate, the honest bound is

   ```math
   U_{13}^{BC,new}\le2B_{BC,new}^{SEL2}
   ```

   under `P21-U13-BC-NEWCARRY`;
4. if neither `NEWBLU` nor `NEWCARRY` is supplied, the exact-entry theorem is
   not finitely certified.

Proof.

Definition 31.1 and Lemma 31.2 remove the part already handled by the
\(X_{13}\) cutoff-to-exact comparison. The only remaining `BC` debit is the
new finite scalar battery of Definition 31.3. The zero clause is precisely
block-limit uniqueness on that battery. The finite carry follows from
\(|\mathbb E_\mu F-\mathbb E_\nu F|\le2\|F\|_\infty\). `square`

### Definition 31.5: Coefficient-Window Carry

The active `CE` regularity branch has already been closed on finite
heat-kernel rows:

```math
U_{13}^{CE,reg}=0.
```

The remaining coefficient-window carry is split as

```math
U_{13}^{CE,win,park}
:=
U_{13}^{CE,sign,park}
+U_{13}^{CE,unit,park}
+U_{13}^{CE,tail,park}
+U_{13}^{CE,desmear,park}.
```

Here:

1. \(U_{13}^{CE,sign,park}\) is the carried debit for proving
   \(k_{\rho,j}^{SEL2}>0\) cofinally;
2. \(U_{13}^{CE,unit,park}\) is the carried debit for proving
   \(k_{\rho,j}^{SEL2}<1\) cofinally;
3. \(U_{13}^{CE,tail,park}\) is the carried debit for the cofinal finite
   non-leading character-tail budget;
4. \(U_{13}^{CE,desmear,park}=0\) only on the exact unsmoothed finite-row
   branch or under a proved exact de-smearing/tail-tightness theorem.

Thus

```math
U_{13}^{CE,win,car}
\rightsquigarrow
U_{13}^{CE,win,park}.
```

The zero gate `P21-U13-CE-WIN0` is the conjunction

```math
U_{13}^{CE,sign,park}
=U_{13}^{CE,unit,park}
=U_{13}^{CE,tail,park}
=U_{13}^{CE,desmear,park}
=0.
```

### Theorem 31.6: Present `CE` Decision

The current Paper-21 source package proves only the regularity part of `CE`.
It does not prove `P21-U13-CE-WIN0`. Therefore the active exact-entry ledger
must carry

```math
U_{13}^{CE,win,park}
```

unless a later source theorem proves sign, subunitness, non-leading tail
tightness, and exact de-smearing on the same `SEL2` scalar record law.

Proof.

Section 30 proves \(U_{13}^{CE,reg}=0\) from the finite heat-kernel row
regularity theorem. Paper 20 explicitly separates this from the
coefficient-window estimates: smooth central \(L^1\) density and rowwise
Peter-Weyl expansion do not imply positivity of the chosen coefficient,
subunitness of that coefficient, a cofinal non-leading weighted-tail ceiling,
or exact de-smearing. These are distinct scalar source statements. Hence the
only honest current action is to carry \(U_{13}^{CE,win,park}\). `square`

### Corollary 31.7: Envelope After The Two Decisions

After deciding the free `BC` and `CE-WIN` slots, the active no-corner envelope
is

```math
\mathcal R_{noncorn}^{31,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,car}
+U_{13}^{KPdec,car}
+U_{13}^{WP,car}.
```

The next work is therefore not another `BC/CE` pass. It is to evaluate the
remaining exact-entry terms \(RPF\), \(KPdec\), and \(WP\), unless the project
chooses to reopen the hard coefficient-window problem directly.

## 32. Closing The Remaining Exact-Entry Nonsurface Terms

The remaining exact-entry nonsurface terms are

```math
U_{13}^{RPF,car},\qquad
U_{13}^{KPdec,car},\qquad
U_{13}^{WP,car}.
```

They are structurally different. `RPF` and `KPdec` are real analytic source
estimates: they ask for a residual polymer factorization and a compatible KP
decoration gas for the exact block law after the central plaquette factors
have been extracted. `WP` is a ledger consistency condition: it asks whether
the entry certificate is written on the same whole-process scalar record law
already frozen by Paper 20.

### Definition 32.1: Joint `RPF/KPdec` Source Defect

Assume the `BC` and `CE` branches have supplied an exact block law and central
plaquette factors \(K_p\). Write the residual block density formally as

```math
d\mu_{s_0}^{blk,SEL2}
=
Z^{-1}
\left(\prod_p K_p(U_p)\right)
{\mathcal R}^{SEL2}(U)\,dU.
```

The joint connected-cumulant/KP defect is the pair

```math
\Delta_{RPF,j}^{SEL2},
\qquad
\Delta_{KPdec,j}^{SEL2},
```

where:

1. \(\Delta_{RPF,j}^{SEL2}\) measures the failure of the residual
   \({\mathcal R}^{SEL2}\) to admit a compatible local polymer factorization
   on the row-\(j\) finite block battery;
2. \(\Delta_{KPdec,j}^{SEL2}\) measures the failure of the residual polymers,
   together with the non-leading character insertions from `CE`, to satisfy a
   single KP activity bound on the same finite battery.

The zero source gate `P21-U13-CKP0(A,\mu,m)` asserts the Paper-13
connected-cumulant criterion on the same pushed-forward scalar law:

```math
|\kappa_X^{SEL2}|
\le
A e^{-\mu{\rm diam}(X)}e^{-\mu|X|}
```

for the connected residual cumulants, and

```math
\sup_x
\sum_{\Gamma\ni x}
|\psi^{SEL2}(\Gamma)|e^{m|\Gamma|}
<1
```

for the resulting combined residual-plus-character polymer activities.

The finite carry gate `P21-U13-CKP-CARRY` asserts

```math
U_{13}^{RPF,park}
:=
\limsup_j\Delta_{RPF,j}^{SEL2}<\infty,
\qquad
U_{13}^{KPdec,park}
:=
\limsup_j\Delta_{KPdec,j}^{SEL2}<\infty.
```

These defects are entry-level comparison residuals. They are not a second
copy of the global decoration debit, the character-tail budget, or the final
surface subcriticality test.

### Lemma 32.2: Connected-Cumulant KP Zeroes `RPF` And `KPdec`

If `P21-U13-CKP0(A,\mu,m)` holds, then

```math
U_{13}^{RPF,car}=0,
\qquad
U_{13}^{KPdec,car}=0.
```

Proof.

Paper 13 Definition 7.30AR states the connected-cumulant KP criterion as an
estimate of the exact block record functional, not as a Markov or subprocess
factorization. Paper 13 Theorem 7.30AS proves that this criterion gives both
the residual factorization gate `RPF` and the combined decoration gate
`KP_dec`. Therefore the row defects
\(\epsilon_{RPF,j}^{SEL2}\) and \(\epsilon_{KPdec,j}^{SEL2}\) vanish
cofinally on the same scalar record law. Taking limsups gives the result.
`square`

### Theorem 32.3: Present `RPF/KPdec` Decision

The current Paper-21 source package does not prove `P21-U13-CKP0(A,\mu,m)`.
Therefore the active strict reduced branch may not set
\(U_{13}^{RPF,car}\) or \(U_{13}^{KPdec,car}\) to zero. The honest closure is
the zero-or-carried fork

```math
U_{13}^{RPF,car}
\rightsquigarrow
U_{13}^{RPF,park},
\qquad
U_{13}^{KPdec,car}
\rightsquigarrow
U_{13}^{KPdec,park},
```

with both terms finite only under `P21-U13-CKP-CARRY`. If that finite carry
gate is not supplied, the exact-entry source route is not certified.

Proof.

Paper 20 Lemma 4.3A.133 identifies the source route for `RPF` and `KPdec` as
the connected-cumulant KP criterion of Paper 13 Theorem 7.30AS. Paper 21 has
not proved the connected residual cumulant decay or the resulting KP
smallness on the active `SEL2` block law. Thus zero would be a smuggled
factorization theorem. The only current legal alternatives are the zero gate
of Lemma 32.2 or the finite carried defects of Definition 32.1. `square`

### Definition 32.4: Strict Whole-Process Entry Clause

The strict whole-process entry clause `P21-U13-WP0` asserts:

1. the exact-entry law is the same pushed-forward scalar law
   \(\Gamma_j^{SEL2}=\rho_j(Law_*^{SEL2})\) used by
   `P20-SEL2-TR-COMMON`;
2. all chart, regulator, blocking, polymer, and gauge coordinates used in the
   entry proof are proof coordinates only;
3. every constant appearing in the entry certificate is either already in the
   common debit ledger or is assigned exactly once in Sections 31--32;
4. no partial kernel, Markov composition, gauge-fixed subprocess, or
   independent finite-volume law is introduced.

Equivalently,

```math
\epsilon_{WP,j}^{SEL2}=0
```

for every sufficiently large \(j\).

### Lemma 32.5: The Active Strict Branch Closes `WP`

On the active Paper-21 strict reduced branch,

```math
U_{13}^{WP,car}=0.
```

Proof.

Paper 21 imports `P20-SEL2-TR-COMMON` in Section 0A. Paper 20 Theorem 4.3A.37
proves that this common-record audit identifies the Paper-16 heat-kernel
tower, the Paper-19 direct-witness tower, and the Paper-14 export after
pushforward, with one disjoint debit register and no independent local-field
or polymer subprocess. Paper 16 Definition 9Z.4 and Theorem 9Z.5 are exactly
the corresponding heat-kernel whole-process certificate.

The strict entry branch in Sections 30--32 does not add any new law. It uses
the same exact block law, same scalar batteries, same constants, and same
debit register. Thus the rowwise whole-process compatibility residual is
identically zero. Taking the limsup gives \(U_{13}^{WP,car}=0\). `square`

If a future branch uses an auxiliary entry law, chart-dependent certificate,
or an unshared decoration/counterterm constant, Lemma 32.5 no longer applies.
That branch must restore a carried term \(U_{13}^{WP,park}\).

### Theorem 32.6: Remaining Exact-Entry Nonsurface Closure

On the active strict reduced `SEL2` branch,

```math
U_{13}^{entry,eval}
\le
U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,park}
+U_{13}^{KPdec,park}.
```

The omitted `WP` term is zero by Lemma 32.5. The omitted `SUB` term remains
outside the exact-entry bucket by the reduced-route placement convention and
is paid only in the final surface-leading-rate test.

If `P21-U13-CKP0(A,\mu,m)` is later proved, then

```math
U_{13}^{RPF,park}=U_{13}^{KPdec,park}=0
```

and the exact-entry nonsurface obstruction reduces to the `BC` new-battery
term and the `CE` coefficient-window term. Without that connected-cumulant KP
source, the two finite parked terms remain part of the scalar feasibility
worksheet.

Proof.

Corollary 31.7 gives the exact-entry envelope after the `BC/CE` decisions.
Theorem 32.3 replaces the remaining `RPF` and `KPdec` slots by their parked
finite source ceilings. Lemma 32.5 zeroes the whole-process slot on the active
strict common-record branch. Substitution gives the displayed bound.
`square`

### Corollary 32.7: Updated Non-Corner Envelope

The active no-corner envelope after closing the exact-entry nonsurface terms
is

```math
\mathcal R_{noncorn}^{32,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,park}
+U_{13}^{KPdec,park}.
```

This is the current honest scalar worksheet. The remaining live sources are:

1. the new-battery block-limit uniqueness or finite carry for `BC`;
2. the coefficient-window package for `CE`;
3. the connected-cumulant KP package for `RPF/KPdec`;
4. the already parked \(E_{14}\), \(X_{13}\), \(U_{12}\), and \(U_{11}^{RPCov}\)
   terms.

The paper should now either evaluate this envelope against the residual
surface margin or choose one of the remaining live source packages and attack
it directly.

## 33. Start With `RPF`: Record Availability And Finite Carry

This section isolates the first remaining exact-entry analytic source. The
question is not whether the `RPF` proof may use local polymer coordinates as
a calculation device. It may. The question is whether every quantity exported
from that calculation is a scalar record of the same frozen `SEL2` law, and
whether the residual factorization defect is actually zero or merely finite.

### Definition 33.1: Finite `RPF` Scalar Battery

For each row \(j\), let \({\mathcal X}_{RPF,j}^{SEL2}\) be the finite set of
connected block-cell templates used by the row-\(j\) residual factorization
test. For \(X\in{\mathcal X}_{RPF,j}^{SEL2}\), let
\({\mathcal O}_{X,j}^{SEL2}\) be the finite list of normalized scalar block
records entering the residual cumulant on \(X\). These records are products
of:

1. the central plaquette character records supplied by the entry `CE` branch;
2. the finite connected products already declared for the exact-entry battery;
3. deterministic local block-template factors used by the cumulant-to-polymer
   transform.

The row-\(j\) `RPF` scalar battery is

```math
B_{RPF,j}^{SEL2}
:=
\left\{
\prod_{O\in S}O:
S\subseteq{\mathcal O}_{X,j}^{SEL2},
\ X\in{\mathcal X}_{RPF,j}^{SEL2}
\right\}.
```

The connected residual cumulant is the usual moment-cumulant polynomial in
this battery:

```math
\kappa_X^{SEL2}
=
\sum_{\pi\in\Pi(X)}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}
\mathbb E_{\Gamma_j^{SEL2}}
\left[
\prod_{O\in{\mathcal O}_{B,j}^{SEL2}}O
\right].
```

Thus every `RPF` cumulant is a scalar functional of the same pushed-forward
record law \(\Gamma_j^{SEL2}\).

### Lemma 33.2: `RPF` Records Are Available On The Strict Scalar Branch

On the active strict `SEL2` branch,

```math
U_{13}^{RPF,rec}=0.
```

Proof.

Definition 33.1 writes the `RPF` inputs as finite products and cumulants of
the scalar block records already used by the exact-entry battery, together
with deterministic local template factors. The strict branch imports
`P20-SEL2-TR-COMMON`, so these records are evaluated under the same
pushed-forward law \(\Gamma_j^{SEL2}\); no gauge-fixed field law, local
subprocess, or independent polymer measure is introduced.

If a particular cumulant product is not literally one of the records in
\(B_{13,j}^{exact,SEL2}\), it is a finite scalar record assigned to the `RPF`
battery before the cutoff is chosen. That is a battery extension, not a
projective, covariance, or regulator comparison. Therefore the record
availability/readout residual for `RPF` is zero. `square`

This lemma does not prove residual factorization. It only proves that the
objects whose factorization is being tested live on the strict scalar record
law.

### Definition 33.3: Pure `RPF` Factorization Defect

Let \(\epsilon_{RPF,j}^{fact,SEL2}\) be the remaining same-law factorization
defect after Lemma 33.2 removes record availability:

```math
\epsilon_{RPF,j}^{SEL2}
=
\epsilon_{RPF,j}^{fact,SEL2}.
```

It is measured only inside the exact block law. It excludes:

```math
D_{11;j,k}^{RP,red,SEL2},
\qquad
D_{11;j,k}^{Cov,red,SEL2}(g),
```

and every projective, covariance, gauge, regulator, and finite-volume tail
already assigned to \(U_{11}^{RPCov,car,SEL2}\).

The zero gate `P21-U13-RPF-FACT0` asserts

```math
\epsilon_{RPF,j}^{fact,SEL2}\to0.
```

The finite carry gate `P21-U13-RPF-BD` asserts a finite template bound. More
explicitly, if the cumulant-to-polymer transform has finite coefficients
\(c_{\Gamma,X}^{tpl}\) on the row templates, define

```math
C_{RPF,j}^{tpl}
:=
\sum_{\Gamma}
\sum_{X\subseteq\Gamma}
|c_{\Gamma,X}^{tpl}|\,
|\kappa_X^{SEL2}|.
```

Then

```math
\epsilon_{RPF,j}^{fact,SEL2}
\le
C_{RPF,j}^{tpl}.
```

The carried bound is

```math
U_{13}^{RPF,bd}
:=
\limsup_j C_{RPF,j}^{tpl},
```

provided the limsup is finite.

For normalized scalar records one may use the crude moment-cumulant ceiling

```math
|\kappa_X^{SEL2}|
\le
{\mathfrak B}_{|X|},
```

where \({\mathfrak B}_{|X|}\) is the Bell-number moment-cumulant bound. Hence
a sufficient finite-template certificate is

```math
\limsup_j
\sum_{\Gamma}
\sum_{X\subseteq\Gamma}
|c_{\Gamma,X}^{tpl}|\,{\mathfrak B}_{|X|}
<\infty.
```

This is a finite bound, not a locality or KP-smallness theorem.

### Theorem 33.4: Present `RPF` Decision

On the active strict `SEL2` branch, the `RPF` record part is closed, but the
factorization part is not proved zero. Therefore the present exact-entry
ledger must use

```math
U_{13}^{RPF,car}
\le
U_{13}^{RPF,bd}
```

under `P21-U13-RPF-BD`. The stronger zero conclusion

```math
U_{13}^{RPF,car}=0
```

is available only under `P21-U13-RPF-FACT0`, for example as a consequence of
the connected-cumulant KP source `P21-U13-CKP0(A,\mu,m)`.

Proof.

Lemma 33.2 proves that no record-availability debit remains. Definition 33.3
then identifies the whole `RPF` residual with the pure same-law factorization
defect. If `P21-U13-RPF-FACT0` holds, this defect tends to zero, so the limsup
ceiling is zero. If only the finite template estimate holds, the row defect is
bounded by \(C_{RPF,j}^{tpl}\), and taking the limsup gives
\(U_{13}^{RPF,car}\le U_{13}^{RPF,bd}\).

No Paper-16 RP/covariance tail appears in this proof. Those tails are already
parked in \(U_{11}^{RPCov,car,SEL2}\), and moving them into `RPF` would double
charge the same comparison loss. `square`

### Corollary 33.5: Envelope After The `RPF` Decision

After the `RPF` audit, the no-corner envelope becomes

```math
\mathcal R_{noncorn}^{33,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,bd}
+U_{13}^{KPdec,park}.
```

The next analytic exact-entry target is \(KPdec\). Its audit should start from
the same strict scalar records, but it must not recharge
\(U_{13}^{RPF,bd}\), \(D_{dec}^{SEL2,20}\), or the character-tail budget.

## 34. Attack `KPdec`: Same Decoration Ledger Or New Cost

The `KPdec` slot is dangerous because its name sounds like a decoration debit.
On the `SEL2` branch there is already a decoration debit:

```math
D_{dec}^{SEL2,20}
=
\exp\left(
{20\widehat\eta_{*,20}\over1-\widehat\eta_{*,20}}
\right)-1,
```

with

```math
\widehat\eta_{*,20}
=
\eta_{res}^{SEL2}+\eta_{ch}^{SEL2}
```

up to the certified upper estimate used in Paper 20. The present question is
therefore:

```math
\text{Does entry }KPdec\text{ use the same decoration ledger, or a new one?}
```

If it uses the same ledger, there is no additional exact-entry decoration
cost. If it introduces new activities, they must be carried as a separate
finite surface-entry decoration bound.

### Definition 34.1: The `SEL2` Paid Decoration Ledger

Let \({\mathfrak D}_{dec,j}^{SEL2}\) denote the paid `SEL2` decoration ledger.
It consists of:

1. the residual-decoration activities imported through the same-record
   analytic residual audit;
2. the non-leading character insertions controlled by
   `P19-CHTAIL-AUDIT(eta_ch,20^{SEL2})`;
3. the area-charged collar templates counted by the finite
   `C_area=20` audit;
4. the corner-separated convention placing endpoint/corner collars outside
   the multiplicative decoration debit;
5. the same pushed-forward scalar law \(\Gamma_j^{SEL2}\).

This is the ledger used by Paper 20 Theorem 4.3A.35 to close
\(D_{dec}^{SEL2,20}\). It is also the ledger used by Paper 19
Theorem 8L.11A.22F.2 to obtain the surface-collar decoration growth bound
without adding a second decoration debit.

### Definition 34.2: Same-Decoration Inclusion Gate

The gate `P21-U13-KPDEC-INDEC` holds when every entry-level `KPdec` activity
required by Paper 13 Definition 7.30AG is either:

1. an activity already in \({\mathfrak D}_{dec,j}^{SEL2}\);
2. a deterministic restriction of such an activity to the finite
   exact-entry battery; or
3. a non-leading character insertion already charged to
   \(\eta_{ch}^{SEL2}\).

The gate also requires that the row uses the same representation cutoff, same
surface/collar templates, same endpoint/corner separation, and same scalar
record law as the paid `SEL2` decoration ledger.

Define the new part of the entry decoration ledger by

```math
{\mathfrak D}_{KPdec,j}^{new,SEL2}
:=
{\mathfrak D}_{KPdec,j}^{entry,SEL2}
\setminus
{\mathfrak D}_{dec,j}^{SEL2}.
```

Then `P21-U13-KPDEC-INDEC` is equivalently the cofinal assertion

```math
{\mathfrak D}_{KPdec,j}^{new,SEL2}=\varnothing.
```

### Lemma 34.3: Same-Decoration Inclusion Gives Zero Incremental `KPdec`

If `P21-U13-KPDEC-INDEC` holds, then

```math
U_{13}^{KPdec,car}=0
```

as an additional exact-entry decoration cost.

Proof.

Under `P21-U13-KPDEC-INDEC`, the entry `KPdec` gas is not a new gas. It is the
same residual-plus-character decoration gas already counted in
\({\mathfrak D}_{dec,j}^{SEL2}\). Paper 20 Theorem 4.3A.35 pays its
finite-battery decoration loss through \(D_{dec}^{SEL2,20}\), while Paper 19
Theorem 8L.11A.22F.2 uses the same activity to obtain the surface-collar
growth constant without adding a second debit. Since no activity remains in
\({\mathfrak D}_{KPdec,j}^{new,SEL2}\), the incremental entry-level `KPdec`
comparison residual is zero cofinally. `square`

This lemma does not erase \(U_{13}^{RPF,bd}\). If the residual has not been
factorized into a scalar polymer gas, that failure remains in `RPF`; `KPdec`
only asks whether the resulting residual-plus-character decorations require a
new activity budget.

### Definition 34.4: New `KPdec` Surface-Entry Decoration Bound

If `P21-U13-KPDEC-INDEC` fails, define the new activity and collar
multiplicity of the unaccounted entry decoration gas by

```math
\eta_{KP,new,j}^{SEL2}
:=
\sup_x
\sum_{\Gamma\ni x,\ \Gamma\in{\mathfrak D}_{KPdec,j}^{new,SEL2}}
\|\psi(\Gamma)\|_\infty e^{m|\Gamma|},
```

and

```math
\Lambda_{KP,new,j}^{SEL2}
:=
\text{the maximal new collar-anchor multiplicity per unit excess area}.
```

The finite new-decoration gate `P21-U13-KPDEC-BD` asserts

```math
\eta_{KP,new}^{SEL2}
:=
\limsup_j\eta_{KP,new,j}^{SEL2}<1,
\qquad
\Lambda_{KP,new}^{SEL2}
:=
\limsup_j\Lambda_{KP,new,j}^{SEL2}<\infty.
```

Then define the finite carried surface-entry decoration bound

```math
U_{13}^{KPdec,bd}
:=
\exp\left(
{\Lambda_{KP,new}^{SEL2}\eta_{KP,new}^{SEL2}
\over
1-\eta_{KP,new}^{SEL2}}
\right)-1.
```

This is paid only for the new activities outside
\({\mathfrak D}_{dec,j}^{SEL2}\). It may not include the already-paid
\(\eta_{res}^{SEL2}\), \(\eta_{ch}^{SEL2}\), `C_area=20` collar templates,
or endpoint/corner collars.

### Theorem 34.5: Present `KPdec` Decision

On the active strict `SEL2` same-decoration branch,

```math
P21\text{-}U13\text{-}KPDEC\text{-}INDEC
```

holds. Consequently

```math
U_{13}^{KPdec,car}=0.
```

For any future branch that does not prove same-decoration inclusion, the
honest replacement is

```math
U_{13}^{KPdec,car}
\le
U_{13}^{KPdec,bd},
```

provided `P21-U13-KPDEC-BD` holds.

Proof.

Paper 20 Definition 1.10 freezes the `SEL2` selector with a disjoint debit
register: area-collar multiplicative growth is charged only in
\(D_{dec}\), endpoint/corner collars are outside that multiplicative register,
and the surface-polymer decoration growth uses the same character-tail
activity. Paper 20 Theorem 4.3A.35 then closes the `SEL2` decoration debit
with `C_area=20` and the chosen \(\eta_{ch,20}^{SEL2}\). Paper 19
Theorem 8L.11A.22F.2 states the corresponding no-double-charge fact: the
surface-collar decoration growth imports the same residual and character-tail
KP activity used by the decoration ledger.

Thus, on the active branch, entry `KPdec` has no decoration activity outside
\({\mathfrak D}_{dec,j}^{SEL2}\). Lemma 34.3 gives zero incremental `KPdec`.
If a later branch adds a new decoration gas, Definition 34.4 gives the finite
KP bound that must be carried instead. `square`

### Corollary 34.6: Envelope After The `KPdec` Decision

On the active strict same-decoration branch, the no-corner envelope reduces to

```math
\mathcal R_{noncorn}^{34,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,bd}.
```

If the same-decoration inclusion gate is not used, replace the final display
by the fallback envelope

```math
\mathcal R_{noncorn}^{34,fb,SEL2}(s)
=
\mathcal R_{noncorn}^{34,SEL2}(s)
+U_{13}^{KPdec,bd}.
```

The next nonsurface action is to evaluate this reduced envelope against the
remaining pre-surface margin, unless the project chooses to attack one of the
three live sources directly: `BC` new-battery uniqueness, `CE` coefficient
window, or `RPF` factorization.

## 35. Attack `WP`: Same Pushed-Forward Law Or Mismatch Carry

The `WP` slot is the whole-process compatibility slot for exact entry. It is
not a new analytic estimate and it is not the Paper-14 export norm. It asks
whether the finite scalar records used by the Paper-13 entry certificate are
evaluated under the same pushed-forward law already fixed by the `SEL2`
selector.

### Definition 35.1: Entry Whole-Process Battery

Let \(B_{WP,j}^{entry,SEL2}\) be the finite scalar battery consisting of every
record whose expectation is used by the row-\(j\) exact-entry certificate:

```math
B_{WP,j}^{entry,SEL2}
:=
B_{13,j}^{exact,SEL2}
\cup
B_{RPF,j}^{SEL2}
\cup
B_{CE,j}^{win,SEL2}
\cup
B_{KPdec,j}^{entry,SEL2},
```

where duplicate records are identified as the same scalar function. Here
\(B_{CE,j}^{win,SEL2}\) denotes the finite coefficient-window records used by
`CE`, and \(B_{KPdec,j}^{entry,SEL2}\) denotes the finite entry-level
decoration records after the same-decoration projection of Section 34.

The strict `SEL2` law for this battery is

```math
\Gamma_j^{SEL2}
=
\rho_j(Law_*^{SEL2}).
```

Let \({\mathbb E}_{entry,j}^{SEL2}\) denote the expectation functional actually
used by the entry certificate. The rowwise whole-process mismatch is

```math
\epsilon_{WP,j}^{mis,SEL2}
:=
\sup_{F\in B_{WP,j}^{entry,SEL2}}
\left|
{\mathbb E}_{entry,j}^{SEL2}F
-
{\mathbb E}_{\Gamma_j^{SEL2}}F
\right|.
```

Then

```math
U_{13}^{WP,mis}
:=
\limsup_j\epsilon_{WP,j}^{mis,SEL2}.
```

The exact-entry `WP` residual is identified with this mismatch:

```math
U_{13}^{WP,car}
=
U_{13}^{WP,mis}.
```

### Lemma 35.2: Strict `SEL2` Evaluates Entry Records Under One Law

On the active strict `SEL2` branch,

```math
\epsilon_{WP,j}^{mis,SEL2}=0
```

for every row \(j\). Hence

```math
U_{13}^{WP,car}=0.
```

Proof.

Paper 21 imports `P20-SEL2-TR-COMMON` in Section 0A. Paper 20 Definition
4.3A.36 states that every exported quantity on `SEL2` is a scalar inequality
for the same finite record laws

```math
\Gamma_j^{SEL2}=\rho_j(Law_*^{SEL2}).
```

Paper 20 Theorem 4.3A.37 proves that this common-record audit instantiates
the Paper-19 transport compatibility audit on the frozen `SEL2` selector.
Sections 31--34 do not introduce any independent law: `BC` uses the same
block-record law, `CE` uses the same block plaquette marginal, `RPF` uses
finite cumulants of scalar records under \(\Gamma_j^{SEL2}\), and `KPdec`
uses the same paid decoration ledger.

Therefore, for every \(F\in B_{WP,j}^{entry,SEL2}\),

```math
{\mathbb E}_{entry,j}^{SEL2}F
=
{\mathbb E}_{\Gamma_j^{SEL2}}F.
```

The supremum in Definition 35.1 is zero. Taking the limsup gives
\(U_{13}^{WP,car}=0\). `square`

### Definition 35.3: Finite Whole-Process Mismatch Carry

If a future branch uses an auxiliary entry functional
\({\mathbb E}_{aux,j}\), a chart-dependent block law, an unshared
counterterm/decorrelation constant, or any entry expectation not literally
equal to \({\mathbb E}_{\Gamma_j^{SEL2}}\) on
\(B_{WP,j}^{entry,SEL2}\), define

```math
\epsilon_{WP,j}^{aux,SEL2}
:=
\sup_{F\in B_{WP,j}^{entry,SEL2}}
\left|
{\mathbb E}_{aux,j}F
-
{\mathbb E}_{\Gamma_j^{SEL2}}F
\right|.
```

The finite mismatch gate `P21-U13-WP-BD` asserts

```math
U_{13}^{WP,bd}
:=
\limsup_j\epsilon_{WP,j}^{aux,SEL2}
<\infty.
```

A sufficient crude certificate is

```math
B_{WP}^{SEL2}
:=
\limsup_j
\sup_{F\in B_{WP,j}^{entry,SEL2}}\|F\|_\infty
<\infty,
```

which gives

```math
U_{13}^{WP,bd}\le2B_{WP}^{SEL2}.
```

For normalized scalar records, \(B_{WP}^{SEL2}\le1\), hence the crude fallback
is \(U_{13}^{WP,bd}\le2\). This is only a finite mismatch bound; it is not a
same-law certificate.

### Theorem 35.4: Present `WP` Decision

On the active strict `SEL2` branch,

```math
U_{13}^{WP,car}=0.
```

If a future non-strict branch fails the same-law identity in Lemma 35.2, then
the exact-entry envelope must instead carry

```math
U_{13}^{WP,car}\le U_{13}^{WP,bd},
```

provided `P21-U13-WP-BD` holds.

Proof.

The strict branch is Lemma 35.2. The fallback branch is Definition 35.3 and
the elementary estimate
\(|{\mathbb E}_\mu F-{\mathbb E}_\nu F|\le2\|F\|_\infty\).

The mismatch carry is disjoint from all previously assigned debits. If the
difference between two entry functionals is caused by projective,
regulator/chart, RP/covariance, or finite-volume transport, that loss belongs
to \(U_{11}^{RPCov,car,SEL2}\), \(E_{14}^{park}\), or the relevant already
declared transport bucket. `WP` carries only the failure to evaluate the same
finite entry records under the same pushed-forward scalar law. `square`

### Corollary 35.5: Envelope After The `WP` Audit

The active strict no-corner envelope remains

```math
\mathcal R_{noncorn}^{35,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,bd}.
```

For a non-strict branch with only finite whole-process mismatch control, use

```math
\mathcal R_{noncorn}^{35,fb,SEL2}(s)
=
\mathcal R_{noncorn}^{35,SEL2}(s)
+U_{13}^{WP,bd}.
```

Thus `WP` is closed on the active branch. The live exact-entry sources are
now `BC` new-battery uniqueness, the `CE` coefficient window, and the pure
`RPF` factorization bound.

## 36. Reassembled Non-Corner Envelope

Sections 25--35 progressively reduced the no-corner worksheet. This section
collects the current result into one expression. It is the envelope to use
for the next scalar feasibility comparison.

### Definition 36.1: Current Exact-Entry Upper Envelope

On the active strict same-record `SEL2` branch, define

```math
U_{13}^{entry,36,SEL2}
:=
U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,bd}.
```

The absent terms are absent for specific reasons:

```math
U_{13}^{KPdec,car}=0
```

by the same-decoration inclusion gate of Theorem 34.5, and

```math
U_{13}^{WP,car}=0
```

by the same pushed-forward law audit of Theorem 35.4. The reduced-route
`SUB` term is still not part of exact entry; it is reserved for the final
surface-leading-rate comparison.

### Definition 36.2: Current Non-Corner Upper Envelope

The current certified non-corner upper envelope is

```math
\mathcal R_{noncorn}^{36,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{entry,36,SEL2}.
```

Equivalently,

```math
\mathcal R_{noncorn}^{36,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,bd}.
```

This formula supersedes the earlier historical envelopes
\(\mathcal R_{noncorn}^{30}\) through \(\mathcal R_{noncorn}^{35}\) on the
active strict branch.

### Lemma 36.3: Disjointness Of The Reassembled Envelope

No term in \(\mathcal R_{noncorn}^{36,SEL2}\) double-charges another term in
the active ledger.

Proof.

The endpoint/corner debit is absent by the no-corner selector and Theorem
21.7. The global multiplicative decoration debit is already subtracted inside
\(\underline M_{loss}^{SEL2,20}\), so it is not present in
\(\mathcal R_{noncorn}^{36,SEL2}\). The Paper-14 export is represented only
by \(E_{14}^{park}\). The cutoff-to-exact/readout comparison is represented
only by \(X_{13}^{(26),SEL2}\). The reduced loop-readout bucket is represented
only by \(U_{12}^{(27),SEL2}\). The surviving Paper-16 RP/covariance transport
tails are represented only by \(U_{11}^{RPCov,car,SEL2}\).

Inside exact entry, \(U_{13}^{BC,new}\) contains only the new battery not
already in \(X_{13}\) or the component slots. \(U_{13}^{CE,win,park}\) contains
only the sign/subunit/tail/desmearing coefficient window, not `CE-REG`.
\(U_{13}^{RPF,bd}\) contains only the pure residual factorization defect and
explicitly excludes RP/covariance transport tails. `KPdec` is zero on the
same-decoration branch, and `WP` is zero on the same-law branch. `square`

### Theorem 36.4: Reassembled No-Corner Pass Test

For \(s\in\mathcal A_{NC}(\rho)\), the active strict no-corner branch is
certified through the nonsurface worksheet whenever

```math
\mathcal R_{noncorn}^{36,SEL2}(s)<S_{NC}(s).
```

Equivalently,

```math
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{CE,win,park}
+U_{13}^{RPF,bd}
<
1+F_\rho(s)-e^{D_{20}(s)}.
```

If this inequality holds for some \(s\in\mathcal A_{NC}(\rho)\), the branch
may proceed to the final surface-leading-rate and escape-mass gates. If it
fails only for this upper envelope, the certificate fails but the route is not
falsified without matching lower floors for the carried terms.

Proof.

The no-corner pass test is Theorem 21.7 with the current evaluated envelope.
Sections 26, 27, 29, 31, 33, 34, and 35 provide the substitutions for
\(X_{13}\), \(T_{12}\), \(T_{11}\), `BC/CE`, `RPF`, `KPdec`, and `WP`,
respectively. Lemma 36.3 proves that those substitutions are disjoint. The
right-hand side is Definition 22.2:

```math
S_{NC}(s)=1+F_\rho(s)-e^{D_{20}(s)}.
```

Substitution gives the displayed scalar inequality. `square`

### Definition 36.5: Fallback Add-Ons For Non-Strict Branches

For bookkeeping, define the fallback add-on

```math
\Delta_{fb}^{36,SEL2}
:=
U_{13}^{KPdec,bd}
+U_{13}^{WP,bd},
```

with the convention that a term is included only when its corresponding
strict zero theorem is not used. The non-strict fallback envelope is

```math
\mathcal R_{noncorn}^{36,fb,SEL2}(s)
:=
\mathcal R_{noncorn}^{36,SEL2}(s)
+\Delta_{fb}^{36,SEL2}.
```

If a future branch also declines the strict zero/carry decisions for \(X_{13}\),
\(U_{12}\), \(U_{11}^{RPCov}\), `BC`, `CE`, or `RPF`, the corresponding
replacement term must be added explicitly rather than hidden inside
\(\Delta_{fb}^{36,SEL2}\).

### Corollary 36.6: Current Live Sources

After reassembly, the active strict no-corner branch has exactly seven carried
terms:

```math
E_{14}^{park},\quad
X_{13}^{(26),SEL2},\quad
U_{12}^{(27),SEL2},\quad
U_{11}^{RPCov,car,SEL2}(s),
```

```math
U_{13}^{BC,new},\quad
U_{13}^{CE,win,park},\quad
U_{13}^{RPF,bd}.
```

The cheapest next action is to compare this reassembled envelope against
\(S_{NC}(s)\). If it is too large, choose one live term to sharpen; if it fits,
freeze the passing \(s\) and return to the final \(T_{13}\) rate gate.

## 37. Feasibility Test For The Reassembled Envelope

Section 36 leaves a single scalar comparison. This section performs the
comparison at the level currently justified by the paper: symbolic in the
seven live carried terms, exact in the no-corner bookkeeping, and explicit
about what would count as a pass, a certificate failure, or a true
falsification.

### Definition 37.1: Current Feasibility Functional

For \(s\in\mathcal A_{NC}(\rho)\), define

```math
\Phi_{36}^{SEL2}(s)
:=
S_{NC}(s)-\mathcal R_{noncorn}^{36,SEL2}(s).
```

Equivalently,

```math
\Phi_{36}^{SEL2}(s)
=
1+F_\rho(s)-e^{D_{20}(s)}
-E_{14}^{park}
-X_{13}^{(26),SEL2}
-U_{12}^{(27),SEL2}
-U_{11}^{RPCov,car,SEL2}(s)
```

```math
\qquad
-U_{13}^{BC,new}
-U_{13}^{CE,win,park}
-U_{13}^{RPF,bd}.
```

The optimized feasibility surplus is

```math
\Pi_{36}^{max}(\rho)
:=
\sup_{s\in\mathcal A_{NC}(\rho)}
\Phi_{36}^{SEL2}(s),
```

with the convention \(\Pi_{36}^{max}(\rho)=-\infty\) when
\(\mathcal A_{NC}(\rho)=\varnothing\).

### Lemma 37.2: Universal Unit Barrier

For every admissible \(s\),

```math
S_{NC}(s)<1.
```

Consequently, the reassembled no-corner certificate cannot pass unless

```math
\inf_{s\in\mathcal A_{NC}(\rho)}
\mathcal R_{noncorn}^{36,SEL2}(s)
<1.
```

More sharply, it cannot pass unless

```math
\inf_{s\in\mathcal A_{NC}(\rho)}
\mathcal R_{noncorn}^{36,SEL2}(s)
<
S_{NC}^{max}(\rho).
```

Proof.

Lemma 22.3 gives

```math
S_{NC}(s)\le F_\rho(s)<1.
```

The two necessary conditions are immediate from
\(\mathcal R_{noncorn}^{36,SEL2}(s)<S_{NC}(s)\). `square`

### Definition 37.3: Lower-Floor Falsification Data

A lower-floor package for the current envelope is a same-record family

```math
\mathcal L_{noncorn}^{36,SEL2}(s)
\le
\mathcal D_{noncorn}^{36,SEL2}(s)
\le
\mathcal R_{noncorn}^{36,SEL2}(s)
```

where \(\mathcal D_{noncorn}^{36,SEL2}(s)\) denotes the actual non-corner
nonsurface debit on the same frozen pushed-forward `SEL2` scalar law. The
terms of \(\mathcal L_{noncorn}^{36,SEL2}\) must be genuine lower bounds for
the corresponding actual debits and must be disjoint in the same sense as
Lemma 36.3.

The associated lower-floor surplus is

```math
\Lambda_{36}^{max}(\rho)
:=
\sup_{s\in\mathcal A_{NC}(\rho)}
\left[
S_{NC}(s)-\mathcal L_{noncorn}^{36,SEL2}(s)
\right].
```

### Theorem 37.4: Exact Feasibility Alternatives At Section 36

The Section-36 worksheet has the following three honest outcomes.

1. **Pass certificate.** If

```math
\Pi_{36}^{max}(\rho)>0,
```

and every term in \(\mathcal R_{noncorn}^{36,SEL2}\) is a certified upper
bound for the matching same-record debit, then the strict no-corner `SEL2`
branch passes the nonsurface feasibility test. Any \(s\) with
\(\Phi_{36}^{SEL2}(s)>0\) may be frozen for the final surface-leading-rate
test.

2. **Upper-envelope certificate failure.** If

```math
\Pi_{36}^{max}(\rho)\le0,
```

then the current upper-bound package does not certify the branch. This is not
a falsification of the branch unless the upper envelope is known to be sharp
or matching lower floors are also supplied.

3. **Lower-floor falsification.** If a lower-floor package exists and

```math
\Lambda_{36}^{max}(\rho)\le0,
```

then no admissible \(s\) can pass the Section-36 nonsurface test on the strict
no-corner `SEL2` branch.

Proof.

The pass statement is exactly Theorem 36.4 optimized over
\(\mathcal A_{NC}(\rho)\). The second statement records that an upper bound
can fail to certify even when the actual debit is smaller. The third statement
uses the lower-floor inequality
\(\mathcal L_{noncorn}^{36,SEL2}(s)\le\mathcal D_{noncorn}^{36,SEL2}(s)\):
if even the lower floor is never below the available margin, then the actual
debit cannot be below the available margin. `square`

### Corollary 37.5: Current Paper-21 Verdict

With the data presently proved in Paper 21, the feasibility test is reduced
but not numerically decided:

```math
\mathrm{P21\text{-}FEAS36\text{-}PASS}
\quad\text{is not proved;}
```

```math
\mathrm{P21\text{-}FEAS36\text{-}LOWFAIL}
\quad\text{is not proved.}
```

The reason is precise. The current strict no-corner envelope still contains
seven live carried terms:

```math
E_{14}^{park},\quad
X_{13}^{(26),SEL2},\quad
U_{12}^{(27),SEL2},\quad
U_{11}^{RPCov,car,SEL2}(s),
```

```math
U_{13}^{BC,new},\quad
U_{13}^{CE,win,park},\quad
U_{13}^{RPF,bd}.
```

Paper 21 has not supplied numerical or closed analytic ceilings for this
entire seven-term family as functions of \(s\), and it has not supplied a
matching lower-floor family. Therefore the honest status is

```math
\mathrm{P21\text{-}FEAS36\text{-}UNDECIDED}.
```

This is not a retreat to an implicit continuum field picture. It is a
same-record scalar obstruction: the only missing data are the seven displayed
finite or limsup debits on the frozen `SEL2` scalar law.

### Corollary 37.6: Next Sharpening Order

The next estimates should be attacked in the order that most rapidly changes
\(\Phi_{36}^{SEL2}\):

1. \(E_{14}^{park}\), because a nonzero lower floor near the unit scale can
   kill the pass by Lemma 37.2, while a proved zero would immediately enlarge
   the available margin.
2. \(U_{13}^{CE,win,park}\), because it is the coefficient-window obstruction
   closest to the original Paper-20 rate gate.
3. \(U_{13}^{RPF,bd}\), because it is the remaining pure exact-entry
   factorization defect after `KPdec` and `WP` have been zeroed.
4. \(U_{11}^{RPCov,car,SEL2}(s)\), only if Paper-16 rowwise projective and
   covariance transport rates can be supplied without recharging T12 or RPF.
5. \(X_{13}^{(26),SEL2}\) and \(U_{12}^{(27),SEL2}\), if a strict finite
   readout convention can reduce the already-carried finite constants further.

The feasibility worksheet should not be optimized numerically before these
terms are either assigned actual upper ceilings or given lower floors. An
abstract optimum of \(S_{NC}(s)\) alone is not evidence for or against the
actual `SEL2` branch.

## 38. Reopening The Paper-14 Export Debit

The first live term in Corollary 37.6 is \(E_{14}^{park}\). This section
reopens it against Paper 14 and Paper 20. The result is not a zero theorem:
Paper 14 supplies a conditional nine-rate route, not an unconditional
four-dimensional `SU(N)` component-rate proof on the active `SEL2` tower.

### Definition 38.1: Actual Paper-14 Debit On The `SEL2` Row

Let

```math
\mathcal D_{14}^{SEL2}
```

denote the actual Paper-14 whole-process export debit read by the active
strict no-corner `SEL2` row. It is the rowwise limsup of the Paper-14
transport norm from Definitions 14.1--14.2 of Paper 14, after pushing every
quantity to the same finite scalar battery:

```math
E_{14}(\eta)
=
(E_{ID},E_{proj},E_{CE},E_{tail},E_{chart},E_{ct},E_{vol},E_{cov},E_{RP})(\eta),
```

```math
\|E_{14}(\eta)\|_{tr}
=
\alpha_{ID}E_{ID}
+\alpha_{proj}E_{proj}
+\alpha_{CE}E_{CE}
+\alpha_{tail}E_{tail}
+\alpha_{chart}E_{chart}
+\alpha_{ct}E_{ct}
+\alpha_{vol}E_{vol}
+\alpha_{cov}E_{cov}
+\alpha_{RP}E_{RP}.
```

The imported Paper-19/Paper-20 export gives only the same-record upper
ceiling

```math
0\le \mathcal D_{14}^{SEL2}\le E_{14}^{park}<\infty.
```

This upper ceiling is the term currently appearing in
\(\mathcal R_{noncorn}^{36,SEL2}\).

### Definition 38.2: Paper-14 Zero Audit Restated

The replacement

```math
E_{14}^{park}\mapsto0
```

requires a cofinal row-tail reading of a summable nine-component certificate.
Concretely, there must be a standard Paper-14 chain \(\eta_m\), a cofinal map
\(n(j)\to\infty\), and nonnegative component bounds

```math
\epsilon_{ID,m},\epsilon_{proj,m},\epsilon_{CE,m},\epsilon_{tail,m},
\epsilon_{chart,m},\epsilon_{ct,m},\epsilon_{vol,m},
\epsilon_{cov,m},\epsilon_{RP,m},
```

such that the active `SEL2` row reads the remaining tail

```math
\mathcal D_{14,j}^{SEL2}
\le
\sum_{m\ge n(j)}
\big(
\alpha_{ID}\epsilon_{ID,m}
+\alpha_{proj}\epsilon_{proj,m}
+\alpha_{CE}\epsilon_{CE,m}
+\alpha_{tail}\epsilon_{tail,m}
+\alpha_{chart}\epsilon_{chart,m}
```

```math
\qquad
+\alpha_{ct}\epsilon_{ct,m}
+\alpha_{vol}\epsilon_{vol,m}
+\alpha_{cov}\epsilon_{cov,m}
+\alpha_{RP}\epsilon_{RP,m}
\big),
```

and the weighted component series is summable. This is exactly
\(\mathrm{P20\text{-}SEL2\text{-}P14\text{-}COMP}\) in Paper 20.

### Lemma 38.3: Paper 14 Supplies A Conditional Route, Not The Active Zero

Paper 14 does not, by itself, prove \(E_{14}^{park}=0\) on the active
four-dimensional `SEL2` branch.

Proof.

Paper 14 Theorem 14.3 proves whole-process certificate independence from a
summable transport norm. Paper 14 Definition 20.2 defines a rate certificate
for the nine entries of \(E_{14}\), and Theorem 20.3 proves that such a rate
certificate gives `WP`. Paper 14 Definition 31.1 and Theorem 31.2 give
admissible polynomial/exponential rate classes sufficient for that
certificate.

But Paper 14 Corollary 32.2 states that Paper 14 is complete as a reduction
paper and is not an unconditional four-dimensional Yang-Mills construction
unless its closure assumptions are proved for actual continuum `SU(N)`.
Therefore Paper 14 names the nine component estimates needed for the zero
audit; it does not prove those estimates on the active `SEL2` tower. `square`

### Theorem 38.4: Current Decision For \(E_{14}^{park}\)

On the present Paper-21 branch,

```math
\mathrm{P21\text{-}E14\text{-}ZERO}
\quad\text{is not proved.}
```

The sharpest upper carry currently justified by the imported corpus is

```math
U_{14}^{car,SEL2}:=E_{14}^{park}.
```

The current lower-floor package supplies only the trivial lower floor

```math
L_{14}^{floor,SEL2}:=0.
```

Thus the Paper-14 contribution to the Section-37 worksheet is

```math
0
\le
\mathcal D_{14}^{SEL2}
\le
E_{14}^{park},
```

with no licensed replacement of \(E_{14}^{park}\) by zero.

Proof.

The upper bound is Definition 38.1, imported from
\(\mathrm{P19\text{-}P14\text{-}EXPORT}(E_{14}^{SEL2})\) and Paper 20
Corollary 4.3A.91. Lemma 38.3 rules out spending the zero replacement from
the current Paper-14 imports alone. Nonnegativity of the Paper-14 transport
norm gives the trivial lower floor. No positive lower floor for the actual
same-record debit is proved in Papers 14, 20, or the previous sections of
Paper 21. `square`

### Corollary 38.5: Feasibility Consequences Of The Paper-14 Carry

Because all other live terms are nonnegative,

```math
\Pi_{36}^{max}(\rho)
\le
S_{NC}^{max}(\rho)-E_{14}^{park}.
```

Therefore, if

```math
E_{14}^{park}\ge S_{NC}^{max}(\rho),
```

then the current upper-envelope package cannot certify the branch. Since
\(S_{NC}^{max}(\rho)<1\), the simpler sufficient certificate-failure test is

```math
E_{14}^{park}\ge1.
```

Neither test is a branch falsification. A falsification from Paper-14 alone
would require a positive lower floor satisfying

```math
L_{14}^{floor,SEL2}\ge S_{NC}^{max}(\rho),
```

or the corresponding lower-floor sum with the other live debits. The current
lower floor is \(0\), so Paper 21 has not falsified the branch through
Paper-14 export.

### Corollary 38.6: Updated Next Target

The coarse \(E_{14}^{park}\) audit is now exhausted at the current source
level:

```math
\mathrm{P21\text{-}E14\text{-}STATUS}
=
\mathrm{carry}(E_{14}^{park})
\quad\text{with trivial lower floor }0.
```

The next high-leverage term is therefore

```math
U_{13}^{CE,win,park}
=
U_{13}^{CE,sign,park}
+U_{13}^{CE,unit,park}
+U_{13}^{CE,tail,park}
+U_{13}^{CE,desmear,park}.
```

Returning to \(E_{14}^{park}\) is useful only if new same-record Paper-14
component-rate data are supplied, or if a genuine positive lower floor for
\(\mathcal D_{14}^{SEL2}\) is proved.

## 39. Sharper Attack Routes For \(E_{14}^{park}\)

Section 38 treats \(E_{14}^{park}\) as one carried scalar. That is safe but
too coarse. This section records every currently available way to attack the
term without smuggling in a continuum Yang-Mills measure or double-charging
other buckets.

### Definition 39.1: Componentwise Paper-14 Row Ledger

Let

```math
\mathfrak I_{14}
:=
\{ID,proj,CE,tail,chart,ct,vol,cov,RP\}.
```

For \(i\in\mathfrak I_{14}\), let \(e_{i,j}^{SEL2}\) be the row-\(j\)
pushed-forward scalar defect corresponding to the \(i\)-th entry of Paper 14
Definition 14.1, read on the active `SEL2` finite battery. The component
transport debit is

```math
\mathcal D_{14,j}^{SEL2}
:=
\sum_{i\in\mathfrak I_{14}}\alpha_i e_{i,j}^{SEL2}.
```

The actual Paper-14 debit is

```math
\mathcal D_{14}^{SEL2}
:=
\limsup_j\mathcal D_{14,j}^{SEL2}.
```

The parked scalar satisfies

```math
\mathcal D_{14}^{SEL2}\le E_{14}^{park}.
```

Thus \(E_{14}^{park}\) may be sharpened by proving component zeros,
component transfers, sharper component upper bounds, or component lower
floors.

### Definition 39.2: Structural-Zero Components

A component \(i\in\mathfrak I_{14}\) is structurally zero on the active
`SEL2` branch if

```math
e_{i,j}^{SEL2}=0
```

for all sufficiently large \(j\), by exact finite-record convention rather
than by asymptotic continuum analysis.

The admissible structural-zero tests are:

1. `ID-zero`: the identities used in the Paper-14 export are exact identities
   of the pushed-forward finite cutoff law on the active scalar battery.
2. `proj-zero`: the Paper-14 battery and the active `SEL2` battery are the
   same finite scalar battery, so no projection or restriction map is applied.
3. `chart-zero`: chart changes act only on proof coordinates and leave every
   declared scalar record in the battery unchanged.
4. `ct-zero`: counterterm reparametrization leaves the pushed-forward scalar
   battery law unchanged, not merely close.
5. `vol-zero`: the finite-volume comparison is exactly invisible to the
   declared battery, not merely exponentially small in the buffer.
6. `cov-zero`: the covariance comparison is an exact symmetry of the finite
   scalar battery actually used in the row.
7. `RP-zero`: the reflection-positivity comparison is evaluated within the
   same reflected finite battery and requires no transport.

The `CE` and `tail` components are not structural-zero candidates here; they
belong to the coefficient-window transfer test below.

### Lemma 39.3: Structural-Zero Reduction

Let \(Z\subset\mathfrak I_{14}\) be a set of components proved structurally
zero on the active branch. Then

```math
\mathcal D_{14}^{SEL2}
\le
\limsup_j
\sum_{i\in\mathfrak I_{14}\setminus Z}
\alpha_i e_{i,j}^{SEL2}.
```

Therefore the Section-36 envelope may replace \(E_{14}^{park}\) by any
certified upper bound for the reduced live sum.

Proof.

For \(i\in Z\), the row component is zero cofinally. Removing finitely many
zero terms does not change the limsup. Nonnegativity gives the displayed
upper bound. `square`

### Definition 39.4: Coefficient-Window Transfer Gate

The Paper-14 `CE` and representation-tail components may be transferred out
of \(E_{14}^{park}\) only under the gate

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}TRANSFER}.
```

This gate requires that, on the same row and same scalar battery,

```math
\limsup_j
\left(
\alpha_{CE}e_{CE,j}^{SEL2}
+\alpha_{tail}e_{tail,j}^{SEL2}
\right)
\le
U_{13}^{CE,win,park},
```

and that the transferred records are not counted again inside any other
Paper-14 component.

When this gate holds, define the `CE`-reduced Paper-14 carry

```math
E_{14}^{noCE,SEL2}
:=
\limsup_j
\sum_{i\in\mathfrak I_{14}\setminus\{CE,tail\}}
\alpha_i e_{i,j}^{SEL2}.
```

The corresponding envelope replaces

```math
E_{14}^{park}+U_{13}^{CE,win,park}
```

by

```math
E_{14}^{noCE,SEL2}+U_{13}^{CE,win,park}.
```

This is not a zero theorem. It is a no-double-charge theorem.

### Lemma 39.5: Coefficient Transfer Is Sound

Assume `P21-E14-CE-TRANSFER`. Then the Section-36 envelope remains an upper
bound for the actual nonsurface debit after replacing
\(E_{14}^{park}\) by \(E_{14}^{noCE,SEL2}\).

Proof.

The actual Paper-14 component sum is the live non-CE sum plus the `CE/tail`
sum. The transfer gate bounds the `CE/tail` sum by
\(U_{13}^{CE,win,park}\), which is already present in
\(\mathcal R_{noncorn}^{36,SEL2}\). Because the transfer gate also requires
record disjointness, the transferred terms are paid once and only once.
`square`

### Definition 39.6: Tail-Normalized Scheduling Attack

Suppose the nine Paper-14 component sequences have a summable weighted majorant

```math
w_m
:=
\sum_{i\in\mathfrak I_{14}}\alpha_i\epsilon_{i,m},
\qquad
\sum_m w_m<\infty.
```

For any chosen null sequence \(\delta_j\downarrow0\), define

```math
n(j)
:=
\min\left\{
n:
\sum_{m\ge n}w_m\le\delta_j
\right\}.
```

If the active `SEL2` row is allowed to read the Paper-14 remaining tail after
this \(n(j)\), then

```math
\mathcal D_{14,j}^{SEL2}\le\delta_j,
```

and hence

```math
E_{14}^{park}\mapsto0
```

is licensed for that row schedule.

This is the cleanest zero route. Its missing input is not the scheduling
argument; it is the actual same-record summable majorant \(w_m\) for
four-dimensional `SU(N)`.

### Definition 39.7: No-Paper14-Export Bypass Selector

Define the selector

```math
\mathrm{P21\text{-}E14\text{-}BYPASS}.
```

It holds when the active `SEL2` proof no longer imports Paper 14 as a
transported external certificate. Instead, every record-level assertion that
Paper 14 would export is proved directly on the frozen `SEL2` scalar law and
assigned to one of the already visible Paper-21 buckets:

```math
BC,\quad CE,\quad RPF,\quad KPdec,\quad WP,\quad RPCov,\quad X_{13},\quad T_{12}.
```

Any Paper-14 component not covered by those buckets is placed in a residual
bypass debit

```math
\Delta_{14}^{byp,SEL2}
:=
U_{14}^{ID}
+U_{14}^{proj}
+U_{14}^{chart}
+U_{14}^{ct}
+U_{14}^{vol}
+U_{14}^{cov}
+U_{14}^{RP}.
```

On a bypass branch, the non-corner envelope becomes

```math
\mathcal R_{noncorn}^{36,byp,SEL2}(s)
:=
\mathcal R_{noncorn}^{36,SEL2}(s)
-E_{14}^{park}
+\Delta_{14}^{byp,SEL2}.
```

The bypass gives a real gain only if

```math
\Delta_{14}^{byp,SEL2}<E_{14}^{park}.
```

It gives a zero replacement only if every component of
\(\Delta_{14}^{byp,SEL2}\) is structurally zero or already paid in a disjoint
bucket.

### Lemma 39.8: Bypass Does Not Smuggle Paper-14 Data

If `P21-E14-BYPASS` holds, then deleting \(E_{14}^{park}\) is not a silent
zero spend; it is a change of proof route.

Proof.

The bypass selector forbids importing the Paper-14 whole-process export as a
transport theorem. Every assertion previously supplied by that theorem must
appear as a same-law scalar estimate in another named Paper-21 bucket or in
\(\Delta_{14}^{byp,SEL2}\). Hence no Paper-14 defect is erased; it is either
unneeded, structurally zero, transferred to an already counted bucket, or
carried in \(\Delta_{14}^{byp,SEL2}\). `square`

### Definition 39.9: Dual Lower-Floor Witness

A Paper-14 lower-floor witness is a declared scalar record
\(F\in B_{14}^{SEL2}\) with comparison Lipschitz constant \(L_F>0\), together
with two same-row pushed-forward laws \(\mu_j,\nu_j\) used in the Paper-14
transport comparison, such that

```math
\left|
\int F\,d\mu_j-\int F\,d\nu_j
\right|
\ge\delta_j.
```

If the transport norm dominates \(F\) with constant \(L_F\), then

```math
\mathcal D_{14,j}^{SEL2}
\ge
{\delta_j\over L_F}.
```

Thus any cofinal lower bound \(\liminf_j\delta_j/L_F\ge L_{14}>0\) supplies

```math
L_{14}^{floor,SEL2}\ge L_{14}.
```

If \(L_{14}\ge S_{NC}^{max}(\rho)\), the strict no-corner `SEL2` branch is
falsified by the Paper-14 export mismatch alone.

### Theorem 39.10: Exhaustive Honest Attack Menu For \(E_{14}^{park}\)

At the current source level, \(E_{14}^{park}\) has exactly five honest attack
routes.

1. **Component structural zeros:** prove some \(e_{i,j}^{SEL2}=0\) cofinally
   and replace \(E_{14}^{park}\) by the reduced live component sum.
2. **Coefficient-window transfer:** prove `P21-E14-CE-TRANSFER` and stop
   paying the `CE/tail` components both inside \(E_{14}\) and inside
   \(U_{13}^{CE,win,park}\).
3. **Tail-normalized summability:** prove the nine-component summable
   majorant and choose a cofinal row-tail schedule, which gives
   \(E_{14}^{park}\mapsto0\).
4. **No-Paper14-export bypass:** reprove the needed Paper-14 assertions
   directly on the frozen `SEL2` scalar law and replace \(E_{14}^{park}\) by
   \(\Delta_{14}^{byp,SEL2}\).
5. **Dual lower-floor witness:** prove a positive same-record mismatch lower
   floor, which can falsify the branch if it exceeds the available no-corner
   margin.

None of these routes is currently closed unconditionally. The immediate
lowest-cost next test is the structural-zero census for
`ID`, `proj`, and `chart`, followed by the `CE/tail` transfer test. Those
two tests can strictly reduce the carried envelope without requiring the full
nine-rate Paper-14 summability theorem.

## 40. First Structural-Zero Census For \(E_{14}\)

Section 39 identifies `ID`, `proj`, and `chart` as the cheapest structural
tests. This section performs that census. The outcome is deliberately
conservative: none of the three can be erased from the active Paper-14 export
without an additional same-record clause.

### Lemma 40.1: `ID-zero` Is Not Yet Proved

The current papers do not prove

```math
e_{ID,j}^{SEL2}=0
```

for the Paper-14 export component on the active `SEL2` row.

Proof.

Paper 14 contains exact finite-cutoff Schwinger-Dyson identities before
projection, but the Paper-14 certificate does not export only those raw
group-integration identities. Paper 14 Definition 7.1 includes finite
identity defects `Def_ID(eta)` in the certificate, Definition 7.2 requires
their summability, Theorem 24.7 requires vanishing projected finite-identity
defects on every finite tower battery, and Theorem 32.1 lists finite
projected identity-defect convergence as an assumption of the final reduction.

Thus the exact raw integration-by-parts identity is not enough to set the
Paper-14 `ID` export component to zero. The missing statement is that the
specific projected finite identity ledger used by the active `SEL2` row has
zero defect, not merely vanishing or summable defect. `square`

### Lemma 40.2: `proj-zero` Is Not Implied By Same-Battery Compatibility

The current same-battery compatibility audit does not prove

```math
e_{proj,j}^{SEL2}=0.
```

Proof.

Paper 20 `P20-SEL2-TR-COMMON` identifies the Paper-14 export chain with the
same pushed-forward scalar record laws used by the rest of the `SEL2`
transport ledger. This prevents a second external battery from being used.
It does not remove the internal Paper-14 projection problem.

Paper 14 Definition 10.4 defines the finite-battery projection defect because
the exact identities may contain differentiated loop products or local action
insertions outside the chosen finite battery. Paper 14 Theorem 10.5 and
Theorem 24.7 require those projection defects to vanish or be controlled.
Therefore even on a shared `SEL2` battery, an off-battery expression generated
by the identity ledger may still require projection back to the finite
battery. Same battery kills external restriction mismatch; it does not kill
the internal off-battery projection defect. `square`

### Lemma 40.3: `chart-zero` Requires A Stronger Scalar-Forgetting Clause

The strict scalar branch proves that gauge/chart reconstruction does not add
a separate \(U_{11}^{gauge}\) debit, but it does not by itself prove

```math
e_{chart,j}^{SEL2}=0
```

inside the Paper-14 export vector.

Proof.

Paper 21 Lemma 17.9 proves that closed scalar records have zero
gauge/chart reconstruction debit after gauge charts and axial trees are
forgotten. That theorem concerns the reduced `T_11` gauge slot.

The Paper-14 component \(e_{chart,j}^{SEL2}\) is different: it is the
gauge-chart transition defect inside the whole-process certificate ledger of
Paper 14. To set it to zero, one must prove that the Paper-14 certificate
comparison is performed only after both chart choices have been pushed to the
same scalar battery and that every declared scalar record is literally
unchanged by the chart transition. `P20-SEL2-TR-COMMON` says all exported
quantities are scalar inequalities on one pushed-forward law, but it does not
state this stronger component-level chart-collapse identity. `square`

### Definition 40.4: Minimal Structural-Zero Add-On

Define

```math
\mathrm{P21\text{-}E14\text{-}STRUCT0}(Z)
```

to mean that a subset \(Z\subset\{ID,proj,chart\}\) has passed the
component-level structural-zero tests of Definition 39.2 on the active
`SEL2` scalar law.

The three currently needed add-on clauses are:

```math
\mathrm{P21\text{-}E14\text{-}ID0},\qquad
\mathrm{P21\text{-}E14\text{-}PROJ0},\qquad
\mathrm{P21\text{-}E14\text{-}CHART0}.
```

They respectively assert zero projected identity defect, zero internal
off-battery projection defect, and zero Paper-14 chart-transition defect on
the active row.

### Theorem 40.5: Structural Census Verdict

At the current source level,

```math
\mathrm{P21\text{-}E14\text{-}STRUCT0}(\{ID,proj,chart\})
```

is not proved.

More precisely, the currently certified statement is only

```math
0
\le
\limsup_j
\left(
\alpha_{ID}e_{ID,j}^{SEL2}
+\alpha_{proj}e_{proj,j}^{SEL2}
+\alpha_{chart}e_{chart,j}^{SEL2}
\right)
\le
E_{14}^{park}.
```

If any of the three add-on clauses in Definition 40.4 is later proved, Lemma
39.3 removes that component from the live Paper-14 carry. Until then, the
three components stay inside \(E_{14}^{park}\).

Proof.

Lemmas 40.1--40.3 rule out the three structural-zero conclusions from the
currently imported sources. Nonnegativity and Definition 38.1 give the
displayed bound. The reduction under future add-on clauses is Lemma 39.3.
`square`

### Corollary 40.6: Next \(E_{14}\) Attack After The Census

The structural-zero census does not shrink the envelope yet. The next
nontrivial \(E_{14}\) attack is therefore the coefficient-window transfer
gate

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}TRANSFER}.
```

It is more plausible than full nine-rate summability because the active
envelope already carries \(U_{13}^{CE,win,park}\). If the Paper-14 `CE/tail`
components are exactly the same rowwise coefficient-window records already
covered there, then \(E_{14}^{park}\) can be reduced without proving
\(E_{14}^{park}=0\).

## 41. Attack The \(E_{14}\)-To-\(CE\) Transfer Gate

Section 40 leaves the coefficient-window transfer as the next possible
sharpening. This section tests it carefully. The result is a conditional
overlap theorem and a negative current verdict: same pushed-forward law is
necessary, but it is not enough to prove transfer.

### Definition 41.1: Rowwise Paper-14 `CE/tail` Debit

Define the rowwise Paper-14 coefficient-window subdebit

```math
C_{14,j}^{CEtail,SEL2}
:=
\alpha_{CE}e_{CE,j}^{SEL2}
+\alpha_{tail}e_{tail,j}^{SEL2}.
```

Its cofinal upper value is

```math
C_{14}^{CEtail,SEL2}
:=
\limsup_j C_{14,j}^{CEtail,SEL2}.
```

The non-CE Paper-14 carry is

```math
E_{14}^{noCE,SEL2}
:=
\limsup_j
\sum_{i\in\mathfrak I_{14}\setminus\{CE,tail\}}
\alpha_i e_{i,j}^{SEL2}.
```

Thus the actual Paper-14 export debit satisfies

```math
\mathcal D_{14}^{SEL2}
\le
E_{14}^{noCE,SEL2}
+C_{14}^{CEtail,SEL2}.
```

### Definition 41.2: Rowwise Paper-21 `CE-WIN` Debit

Let

```math
C_{13,j}^{CEwin,SEL2}
```

be the rowwise coefficient-window debit whose limsup is the active carried
quantity

```math
U_{13}^{CE,win,park}
=
\limsup_j C_{13,j}^{CEwin,SEL2}.
```

It decomposes as

```math
C_{13,j}^{CEwin,SEL2}
=
C_{sign,j}^{SEL2}
+C_{unit,j}^{SEL2}
+C_{tail,j}^{SEL2}
+C_{desmear,j}^{SEL2},
```

where the four entries correspond to the four summands in Definition 31.5.

### Definition 41.3: Same-Seminorm Transfer Gate

The exact transfer gate

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}SAMESEM}
```

holds when all of the following are true on the active cofinal `SEL2` rows.

1. **Same coefficient records.** The Paper-14 `CE/tail` tests and the
   Paper-21 `CE-WIN` tests are functions of the same block-plaquette
   character coefficients \(k_{\lambda,j}^{SEL2}\) on the same finite scalar
   battery.
2. **Same cutoff and reference window.** The representation cutoff
   \(\Lambda_j\), selected channel \(\rho\), paired-real convention, and
   coefficient window thresholds used by Paper 14 are the ones used by the
   Paper-21 `CE-WIN` ledger.
3. **Weight domination.** The Paper-14 weighted certificate norm is dominated
   by the Paper-21 coefficient-window row debit:

   ```math
   C_{14,j}^{CEtail,SEL2}
   \le
   C_{13,j}^{CEwin,SEL2}
   ```

   cofinally.
4. **No second de-smearing convention.** If Paper 14 uses a smeared or
   approximated coefficient readout, its de-smearing/readout tolerance is
   exactly the \(C_{desmear,j}^{SEL2}\) term in Definition 41.2.

This gate is stronger than common-record compatibility. It says the two
ledgers use the same seminorm on the same scalar coefficient records.

### Lemma 41.4: Same-Seminorm Transfer Proves No Double Charge

Assume `P21-E14-CE-SAMESEM`. Then

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}TRANSFER}
```

holds, and the Section-36 envelope may replace

```math
E_{14}^{park}+U_{13}^{CE,win,park}
```

by

```math
E_{14}^{noCE,SEL2}+U_{13}^{CE,win,park}.
```

Proof.

By Definition 41.3,
\(C_{14,j}^{CEtail,SEL2}\le C_{13,j}^{CEwin,SEL2}\) cofinally, and the two
quantities are seminorms of the same scalar coefficient records. Therefore
the Paper-14 `CE/tail` defect is already paid by the Paper-21 `CE-WIN` debit.
The non-CE Paper-14 entries remain in \(E_{14}^{noCE,SEL2}\). Record identity
and weight domination prevent a second charge of the same scalar records.
`square`

### Definition 41.5: Partial Transfer With A Residual

A weaker residual transfer gate

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}TRANSFER}(R_{14\to13}^{CE})
```

holds if the same-record and same-seminorm clauses 1, 2, and 4 of Definition
41.3 hold and there is a nonnegative row residual \(r_j\) such that

```math
C_{14,j}^{CEtail,SEL2}
\le
C_{13,j}^{CEwin,SEL2}+r_j,
\qquad
\limsup_j r_j\le R_{14\to13}^{CE}.
```

Then the envelope replacement is

```math
E_{14}^{park}+U_{13}^{CE,win,park}
\rightsquigarrow
E_{14}^{noCE,SEL2}
+U_{13}^{CE,win,park}
+R_{14\to13}^{CE}.
```

The residual \(R_{14\to13}^{CE}\) is useful only if it is smaller than the
Paper-14 `CE/tail` part already included in \(E_{14}^{park}\).

### Lemma 41.6: Residual Transfer Is Sound

Assume `P21-E14-CE-TRANSFER(R_{14->13}^{CE})`. Then the residual replacement
in Definition 41.5 is a valid upper envelope for the actual nonsurface debit.

Proof.

The same-record clauses identify the Paper-14 `CE/tail` component and the
Paper-21 `CE-WIN` component as estimates of one coefficient-window record
family, not two independent debits. The rowwise domination with residual pays
the Paper-14 seminorm by the Paper-21 row debit plus \(r_j\). Taking limsups
and leaving all non-CE Paper-14 entries in \(E_{14}^{noCE,SEL2}\) gives the
displayed replacement. `square`

### Lemma 41.7: Common Law Alone Does Not Prove Transfer

`P20-SEL2-TR-COMMON` and the strict same-law `WP` audit do not imply
`P21-E14-CE-SAMESEM`.

Proof.

`P20-SEL2-TR-COMMON` says that the Paper-14 export, Paper-19 transport ledger,
and Paper-20/Paper-21 coefficient records are pushed to the same scalar laws
and assigned disjoint debit homes. It prevents comparing different hidden
processes.

The transfer gate requires more: it requires that the Paper-14 `CE/tail`
certificate norm and the Paper-21 `CE-WIN` debit be the same seminorm, or that
one dominate the other, with the same representation cutoff, same threshold
window, same paired-character convention, and same de-smearing convention.
Common law does not determine the numerical weights \(\alpha_{CE}\),
\(\alpha_{tail}\), the Paper-14 exported reserve convention, or the exact
relation between Paper-14's `RGCE/cRGCE` certificate and the four Paper-21
`CE-WIN` slots. `square`

### Theorem 41.8: Current \(CE/tail\) Transfer Verdict

At the current source level,

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}TRANSFER}
```

is not proved.

The certified statement is the conditional fork:

1. if `P21-E14-CE-SAMESEM` is later proved, replace

   ```math
   E_{14}^{park}+U_{13}^{CE,win,park}
   ```

   by

   ```math
   E_{14}^{noCE,SEL2}+U_{13}^{CE,win,park};
   ```

2. if the residual transfer gate of Definition 41.5 is later proved, use

   ```math
   E_{14}^{noCE,SEL2}
   +U_{13}^{CE,win,park}
   +R_{14\to13}^{CE};
   ```

3. otherwise the active envelope must continue to carry

   ```math
   E_{14}^{park}+U_{13}^{CE,win,park}.
   ```

Proof.

Lemmas 41.4 and 41.6 prove the two transfer routes. Lemma 41.7 proves that
the current common-law audits do not supply the stronger same-seminorm
identification. Therefore the transfer is not currently licensed. `square`

### Corollary 41.9: Next Honest Action

The next useful action is not another global \(E_{14}^{park}\) estimate. It is
one of the following finite scalar checks:

1. prove that Paper-14's `RGCE/cRGCE` coefficient seminorm is exactly the
   Paper-21 `CE-WIN` seminorm on the active row;
2. rescale or normalize the Paper-14 weights \(\alpha_{CE},\alpha_{tail}\)
   so that they are dominated by \(C_{13,j}^{CEwin,SEL2}\);
3. prove a finite residual \(R_{14\to13}^{CE}\) and update the envelope;
4. abandon transfer and attack \(U_{13}^{CE,win,park}\) directly through sign,
   subunit, tail, and exact de-smearing.

Until one of these is done, \(E_{14}^{park}\) remains unreduced by the
coefficient-window overlap.

## 42. Execute The Same-Seminorm And Residual Transfer Tests

This section carries out the first two actions after Section 41: decide
`SAMESEM`, then try the residual transfer. The conclusion is that the active
raw `SEL2` branch does not yet supply either transfer. The obstruction is not
the record law; it is the coefficient normalization, window convention, and
unknown weight domination.

### Lemma 42.1: Paper-14 And Active Paper-21 Use Different Leading Normalizations

Paper 14's `CE` coefficient is the normalized central coefficient

```math
u_{\lambda,j}^{P14}
=
{1\over d_\lambda}
\int\overline{\chi_\lambda(U)}\,K_{p,j}^{SEL2}(U)\,dU.
```

The active Paper-20/Paper-21 raw surface branch uses the scalar coefficient

```math
a_{\lambda,j}^{SEL2}
=
\int\Phi_\lambda(U)\,d\nu_{p,j}^{SEL2}(U),
```

which, in the self-conjugate convention and after identifying
\(\Phi_\lambda=\chi_\lambda\), satisfies

```math
a_{\lambda,j}^{SEL2}=d_\lambda u_{\lambda,j}^{P14}.
```

Thus Paper-14 `cRGCE` and active Paper-21 `CE-WIN` are not literally the same
seminorm unless a normalization conversion is inserted.

Proof.

Paper 14 Definition 6.2 defines \(u_\lambda\) with the prefactor
\(1/d_\lambda\). Paper 20 Definition 4.3A.155 freezes the active raw scalar
coefficient by direct integration of the scalar character record. In the
self-conjugate case, orthogonality and the central density expansion give the
displayed factor \(d_\lambda\). In the non-self-conjugate case the same issue
appears in the real paired scalar convention. `square`

### Lemma 42.2: Exact `SAMESEM` Is Not Currently Proved

At the current source level,

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}SAMESEM}
```

is not proved.

Proof.

Definition 41.3 requires same coefficient records, same cutoff/reference
window, weight domination, and no second de-smearing convention. Lemma 42.1
shows that the active raw branch already needs a normalization conversion
between Paper-14's \(u_\lambda\) and Paper-21's \(a_\lambda\). Paper 14
Definition 30.1 uses the finite-character seminorm

```math
\max_{\lambda\in\Lambda_*}|u_\lambda(\nu)-u_\lambda(\nu_{ref})|
+Tail_{\Lambda_*}(\nu),
```

whereas Definition 31.5 of this paper splits the active `CE-WIN` debit into
sign, raw subunitness, non-leading tail, and de-smearing. The current text has
not proved domination of Paper-14's weights
\(\alpha_{CE},\alpha_{tail}\) by this four-slot raw debit, and it has not
proved that the same representation cutoff and de-smearing convention are
used. Hence exact same-seminorm transfer is unavailable. `square`

### Definition 42.3: Normalization-Converted Residual Transfer

A normalization-converted residual transfer is the gate

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}NRES}
(R_{14\to13}^{CE,norm}).
```

It holds if the Paper-14 normalized coefficients are converted to the active
raw convention by \(a_\lambda=d_\lambda u_\lambda\), the same representation
cutoff and de-smearing convention are used, and there are nonnegative row
residuals \(r_j^{norm}\) such that

```math
C_{14,j}^{CEtail,SEL2}
\le
C_{13,j}^{CEwin,SEL2}
+r_j^{norm},
\qquad
\limsup_j r_j^{norm}
\le
R_{14\to13}^{CE,norm}.
```

This is weaker than `SAMESEM` but still stronger than common-law
compatibility.

### Lemma 42.4: Residual Transfer Is Also Not Currently Proved

At the current source level, no finite value
\(R_{14\to13}^{CE,norm}\) has been proved for Definition 42.3.

Proof.

The paper has not supplied the rowwise constants comparing Paper-14's
finite-character seminorm, after dimension conversion, to the four-slot
Paper-21 `CE-WIN` debit. In particular, the raw subunit/rate slot of
`CE-WIN` depends on the block-time lift or collapse fork, while Paper-14's
`cRGCE` uses a positive-time normalized heat-kernel reference and a finite
character tail. Without a proved conversion inequality, the residual
\(r_j^{norm}\) is only a symbol. `square`

### Theorem 42.5: Transfer Status After Actions 1--2

The first two actions have the following exact outcome:

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}SAMESEM}
\quad\text{is not proved,}
```

and

```math
\mathrm{P21\text{-}E14\text{-}CE\text{-}NRES}
(R_{14\to13}^{CE,norm})
\quad\text{is not proved for any finite certified }R_{14\to13}^{CE,norm}.
```

Therefore the active Section-36 envelope still contains

```math
E_{14}^{park}+U_{13}^{CE,win,park}.
```

The lawful future reductions are exactly those of Theorem 41.8, with the
normalization conversion of Definition 42.3 added when the active raw surface
branch is used.

## 43. Direct Attack On \(U_{13}^{CE,win,park}\)

Since the Paper-14 transfer is not currently licensed, we now attack the
active coefficient-window carry directly.

### Definition 43.1: Refined Active `CE-WIN` Split

On the active raw exact scalar branch, define

```math
U_{13}^{CE,win,43}
:=
U_{13}^{CE,sign,park}
+U_{13}^{CE,unit,park}
+U_{13}^{CE,tail,park}
+U_{13}^{CE,desmear,park}.
```

The rowwise coefficient is the exact unsmoothed scalar record

```math
a_{\rho,j}^{SEL2}
=
\int_G\Phi_\rho(U)\,d\nu_{p,j}^{SEL2}(U),
```

with the raw convention of Paper 20 Definition 4.3A.155.

### Lemma 43.2: Exact Unsmoothed Branch Zeros The De-Smearing Slot

On the active raw exact scalar branch,

```math
U_{13}^{CE,desmear,park}=0.
```

Proof.

The active coefficient-window tests use the exact unsmoothed scalar
coefficient \(a_{\rho,j}^{SEL2}\) of Definition 43.1. No heat-smoothed
coefficient, loop-smoothed coefficient, or approximating coefficient is
substituted into the surface ledger. Therefore there is no de-smearing
comparison to pay inside the `CE-WIN` bucket. This is a convention-zero
statement for the active branch, not a regularity or tail theorem. `square`

### Definition 43.3: Reduced Active `CE-WIN` Carry

After Lemma 43.2, the active coefficient-window carry reduces to

```math
U_{13}^{CE,win,43}
:=
U_{13}^{CE,sign,park}
+U_{13}^{CE,unit,park}
+U_{13}^{CE,tail,park}.
```

The corresponding exact-entry envelope replaces
\(U_{13}^{CE,win,park}\) by \(U_{13}^{CE,win,43}\).

### Lemma 43.4: Sign Remains A Live Scalar Source

The current sources do not prove

```math
U_{13}^{CE,sign,park}=0.
```

Equivalently, they do not prove a cofinal lower bound

```math
\liminf_j a_{\rho,j}^{SEL2}>0.
```

Proof.

Paper 20 Lemma 4.3A.156 shows that central \(L^1\) regularity, smoothness,
and rowwise finite weighted character tail do not imply positivity of a
chosen nontrivial coefficient. Paper 20 Definition 4.3A.157 supplies a
possible collar-mass witness for sign, but the present Paper-21 imports do
not prove that witness on the active `SEL2` row law. Therefore the sign slot
cannot be set to zero. `square`

### Lemma 43.5: Unit And Positive Rate Remain The Main Raw Obstruction

The current sources do not prove

```math
U_{13}^{CE,unit,park}=0.
```

More sharply, the active raw branch is undecided between the block-time lift
and microscopic-collapse alternatives.

Proof.

Paper 20 Definition 4.3A.160E identifies the raw unit/rate test with the
intrinsic block time

```math
t_{\rho,j}^{blk}
=
{2\over C_2(\rho)}
\log\left({d_\rho\over a_{\rho,j}^{SEL2}}\right).
```

The raw subunit and positive-rate branch requires

```math
\liminf_j t_{\rho,j}^{blk}>\theta_\rho
:=
{2\log d_\rho\over C_2(\rho)}.
```

Paper 20 Corollary 4.3A.160I states that the current imports prove neither
the block-time lift nor the microscopic collapse. Hence the unit/rate slot is
not closed. `square`

### Lemma 43.6: The Non-Leading Tail Is Finite Rowwise But Not Uniformly Closed

The current sources prove rowwise weighted character-tail finiteness on the
finite heat-kernel row branch, but they do not prove the cofinal uniform
non-leading tail ceiling required to set

```math
U_{13}^{CE,tail,park}=0.
```

Proof.

Paper 20 Theorem 4.3A.147 gives `CE-REG^+`: each finite row has a smooth
central density and a finite weighted character tail. Corollary 4.3A.148
separates this rowwise finiteness from the later coefficient-window content,
including the cofinal non-leading character-tail budget. A finite value for
each row does not by itself bound the limsup over the moving cofinal rows.
`square`

### Theorem 43.7: Direct `CE-WIN` Attack Verdict

The direct attack proves the exact de-smearing zero

```math
U_{13}^{CE,desmear,park}=0,
```

but leaves three live coefficient-window sources:

```math
U_{13}^{CE,win,43}
=
U_{13}^{CE,sign,park}
+U_{13}^{CE,unit,park}
+U_{13}^{CE,tail,park}.
```

The largest live source is the raw unit/rate gate, equivalently the block-time
lift

```math
\liminf_j t_{\rho,j}^{blk}>\theta_\rho.
```

Proof.

Lemma 43.2 proves the de-smearing zero. Lemmas 43.4--43.6 prove that the
remaining sign, unit/rate, and non-leading tail slots are not closed by the
current source imports. `square`

## 44. Revisit The Non-CE Paper-14 Components

After the failed transfer and the reduced `CE-WIN` attack, the non-CE
Paper-14 components are

```math
ID,\quad proj,\quad chart,\quad ct,\quad vol,\quad cov,\quad RP.
```

Section 40 already handled `ID`, `proj`, and `chart`. This section records
the remaining four.

### Lemma 44.1: `ct-zero` Is Not Proved

The current sources do not prove

```math
e_{ct,j}^{SEL2}=0.
```

Proof.

The frozen `SEL2` branch fixes a counterterm convention for its scalar law,
but the Paper-14 export component \(e_{ct,j}^{SEL2}\) measures
counterterm-reparametrization defect inside the Paper-14 whole-process
certificate ledger. A fixed convention prevents hidden convention changes in
Paper 21; it does not prove that the Paper-14 counterterm comparison defect
is identically zero along the standard chain. `square`

### Lemma 44.2: `vol-zero` Is Not Proved

The current sources do not prove

```math
e_{vol,j}^{SEL2}=0.
```

Proof.

Paper-14 finite-volume defects compare pushed-forward finite-volume laws with
larger-volume or limiting laws on a common finite battery. A large buffer or
finite-volume exhaustion may make this defect small or summable, but exact
zero would require a finite-volume Markov/shielding identity for the declared
records. No such exact identity is supplied by the current source package.
`square`

### Lemma 44.3: `cov-zero` And `RP-zero` Are Not Proved Inside Paper 14

The current sources do not prove

```math
e_{cov,j}^{SEL2}=0,
\qquad
e_{RP,j}^{SEL2}=0.
```

Proof.

The reduced \(U_{11}^{RPCov}\) bucket already carries or zeros the Paper-16
projective/covariance transport tails assigned to `T_11`. The Paper-14
components \(e_{cov}\) and \(e_{RP}\) are different entries in the
whole-process finite-block export certificate. To set them to zero, one must
prove that the exact same finite covariance and reflection-positive batteries
are used before any transport comparison is made. The current common-record
audit prevents double-charging but does not prove those Paper-14 component
defects vanish. `square`

### Theorem 44.4: Non-CE Paper-14 Component Verdict

At the current source level, no component of

```math
ID,\quad proj,\quad chart,\quad ct,\quad vol,\quad cov,\quad RP
```

is proved structurally zero inside the Paper-14 export debit. Therefore the
current non-CE Paper-14 carry remains

```math
E_{14}^{noCE,SEL2}
\le
E_{14}^{park},
```

with possible future reductions only through component-level structural-zero,
tail-normalized summability, or bypass gates.

## 45. Updated Feasibility Worksheet After Actions 1--5

The previous four sections execute the requested five-step audit. We now
rerun the Section-37 feasibility worksheet with the only actually earned
improvement: exact de-smearing contributes zero on the active raw exact branch.

### Definition 45.1: Updated Envelope

Define

```math
U_{13}^{CE,win,45}
:=
U_{13}^{CE,sign,park}
+U_{13}^{CE,unit,park}
+U_{13}^{CE,tail,park}.
```

The updated strict no-corner envelope is

```math
\mathcal R_{noncorn}^{45,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{CE,win,45}
+U_{13}^{RPF,bd}.
```

Equivalently,

```math
\mathcal R_{noncorn}^{45,SEL2}(s)
=
\mathcal R_{noncorn}^{36,SEL2}(s)
-U_{13}^{CE,desmear,park}.
```

On the active exact unsmoothed branch, Lemma 43.2 makes the final subtraction
zero as an evaluated debit, so Section 45 is a bookkeeping sharpening rather
than a new analytic estimate.

### Definition 45.2: Updated Feasibility Surplus

For \(s\in\mathcal A_{NC}(\rho)\), set

```math
\Phi_{45}^{SEL2}(s)
:=
S_{NC}(s)-\mathcal R_{noncorn}^{45,SEL2}(s),
```

and

```math
\Pi_{45}^{max}(\rho)
:=
\sup_{s\in\mathcal A_{NC}(\rho)}
\Phi_{45}^{SEL2}(s).
```

### Theorem 45.3: Feasibility Status After Actions 1--5

The current paper still does not prove

```math
\Pi_{45}^{max}(\rho)>0.
```

It also does not prove a lower-floor falsification. The honest status remains

```math
\mathrm{P21\text{-}FEAS45\text{-}UNDECIDED}.
```

The live carried terms are now

```math
E_{14}^{park},\quad
X_{13}^{(26),SEL2},\quad
U_{12}^{(27),SEL2},\quad
U_{11}^{RPCov,car,SEL2}(s),
```

```math
U_{13}^{BC,new},\quad
U_{13}^{CE,sign,park},\quad
U_{13}^{CE,unit,park},\quad
U_{13}^{CE,tail,park},\quad
U_{13}^{RPF,bd}.
```

Proof.

Sections 42 and 44 do not reduce \(E_{14}^{park}\). Section 43 zeros only the
de-smearing slot of `CE-WIN`, leaving sign, unit/rate, and tail. No numerical
upper ceilings or lower floors for the full displayed family have been
proved. Therefore neither the pass certificate nor the lower-floor
falsification alternative of Theorem 37.4 applies. `square`

### Corollary 45.4: Next Target After The Five-Step Audit

The next genuinely high-leverage target is

```math
U_{13}^{CE,unit,park},
```

equivalently the raw block-time lift/collapse fork

```math
\liminf_j t_{\rho,j}^{blk}>\theta_\rho
\quad\text{or}\quad
t_{\rho,j}^{blk}\to0.
```

If the lift is proved, the raw coefficient route can continue. If collapse is
proved, the raw route fails and the normalized surface fork must be developed
as a new same-record theorem rather than silently substituted.

## 46. Raw Block-Time Fork On The Exact `SEL2` Scalar Law

Section 45 isolates the live raw `CE-UNIT` source. We now freeze it as a
same-record block-time fork, so that the branch cannot quietly borrow a
heat-kernel time from a different row, a Wilson-loop readout, or a continuum
Yang-Mills measure.

### Definition 46.1: Exact Raw `SEL2` Block-Time Observable

Let \(\rho\) be the fixed nontrivial representation used by the surface
polymer branch. On the active exact `SEL2` scalar pushed-forward law, define

```math
a_{\rho,j}^{SEL2}
:=
\int_G \Phi_\rho(U)\,d\nu_{p,j}^{SEL2}(U).
```

On every row for which \(a_{\rho,j}^{SEL2}>0\), define the intrinsic raw
block time

```math
t_{\rho,j}^{blk}
:=
{2\over C_2(\rho)}
\log\left({d_\rho\over a_{\rho,j}^{SEL2}}\right),
```

and the raw unit threshold

```math
\theta_\rho
:=
{2\log d_\rho\over C_2(\rho)}.
```

If \(a_{\rho,j}^{SEL2}\le0\) on a cofinal subsequence, the raw branch already
fails the sign slot \(U_{13}^{CE,sign,park}\). Thus the block-time fork is
evaluated only on sign-positive cofinal rows.

### Lemma 46.2: Raw Unit Is Exactly The Threshold \(t_{\rho,j}^{blk}>\theta_\rho\)

On sign-positive rows,

```math
a_{\rho,j}^{SEL2}<1
\quad\Longleftrightarrow\quad
t_{\rho,j}^{blk}>\theta_\rho.
```

Moreover, if

```math
\liminf_j t_{\rho,j}^{blk}>\theta_\rho,
```

then the raw branch has a cofinal strict subunit gap. If

```math
t_{\rho,j}^{blk}\to0,
```

then the raw branch fails the unit slot for every nontrivial \(\rho\).

Proof.

By Definition 46.1,

```math
a_{\rho,j}^{SEL2}
=
d_\rho
\exp\left(-{1\over2}C_2(\rho)t_{\rho,j}^{blk}\right).
```

Therefore \(a_{\rho,j}^{SEL2}<1\) is equivalent to

```math
d_\rho
\exp\left(-{1\over2}C_2(\rho)t_{\rho,j}^{blk}\right)<1,
```

which is equivalent to

```math
t_{\rho,j}^{blk}>
{2\log d_\rho\over C_2(\rho)}
=\theta_\rho.
```

If \(t_{\rho,j}^{blk}\to0\), then
\(a_{\rho,j}^{SEL2}\to d_\rho\). Since \(\rho\) is nontrivial for
`SU(N)`, \(d_\rho>1\), so \(a_{\rho,j}^{SEL2}<1\) eventually fails. `square`

### Lemma 46.3: Papers 10--12 Do Not Decide The Fork

The current imports from Papers 10--12 prove neither

```math
\liminf_j t_{\rho,j}^{blk}>\theta_\rho
```

nor

```math
t_{\rho,j}^{blk}\to0.
```

Proof.

Paper 10 supplies a projective nonabelian continuum framework and conditional
same-record pushforward language. It does not compute the exact `SEL2`
block-plaquette scalar coefficient \(a_{\rho,j}^{SEL2}\), and it does not
produce a cofinal lower or upper asymptotic for \(t_{\rho,j}^{blk}\).

Paper 11 Theorem 1A.2 explicitly states that Paper 11 does not supply
`P20-SEL2-TREE-RATE-GATE`. Its allowed exports are conditional RG residual
summability and trajectory tracking, not the same-record `SEL2`
block-plaquette coefficient-time lower bound. In particular, it does not
prove a cofinal inequality placing \(t_{\rho,j}^{blk}\) above
\(\theta_\rho\), and it also does not prove that the active pushed-forward
block coefficient collapses to the microscopic AF time.

Paper 12 Theorem 1B.2 explicitly separates calibrated Wilson-loop readout
records from the active `SEL2` block-plaquette central coefficient. It may
export perimeter/cusp, smearing-removal, and loop-approximant ledgers, but it
does not compute \(a_{\rho,j}^{SEL2}\), \(T_-^{SEL2}\), or the tree-rate
source.

Thus Papers 10--12 do not decide either side of the raw block-time fork.
`square`

### Lemma 46.4: Paper 20 Reduces But Does Not Close The Fork

Paper 20 gives the correct raw block-time reduction, but it does not prove
either fork alternative for the active `SEL2` branch.

Proof.

Paper 20 Definition 4.3A.160A freezes the same threshold

```math
\theta_\rho={2\log d_\rho\over C_2(\rho)}.
```

Theorems 4.3A.160B--4.3A.160C prove the model implication: if the effective
block time is cofinally above the threshold with enough comparison margin,
raw `CE-UNIT` passes; if the effective time is cofinally below the threshold,
and especially if it is the microscopic AF time tending to zero with
vanishing comparison error, raw `CE-UNIT` fails.

Definitions 4.3A.160E--4.3A.160F then replace the model time by the intrinsic
block time \(t_{\rho,j}^{blk}\). Theorems 4.3A.160G--4.3A.160H give the exact
lift-versus-collapse fork, and Corollary 4.3A.160I records the current
decision: the available imports prove neither lift nor collapse. Lemma
4.3A.160J further shows that finite block pushforward bookkeeping alone
underdetermines the fork; compatible comparison rows can realize either
lifted block time or microscopic collapse.

Therefore Paper 20 supplies the right decision problem, but not the missing
source theorem. `square`

### Theorem 46.5: Current Raw Block-Time Verdict

For the active exact `SEL2` scalar pushed-forward law, the present corpus does
not prove

```math
\liminf_j t_{\rho,j}^{blk}>\theta_\rho,
```

and it also does not prove

```math
t_{\rho,j}^{blk}\to0.
```

The honest status is

```math
\mathrm{P21\text{-}RAW\text{-}BTIME\text{-}UNDECIDED}.
```

Consequently,

```math
U_{13}^{CE,unit,park}
```

remains live in the Section-45 envelope.

Proof.

Lemma 46.2 proves that the raw unit condition is exactly the threshold
inequality for \(t_{\rho,j}^{blk}\), once the sign slot is positive. Lemma
46.3 proves that Papers 10--12 do not decide either branch. Lemma 46.4 proves
that Paper 20 reduces the problem to the same fork and explicitly leaves it
open for the present sources. Hence neither the lift theorem nor the collapse
theorem is currently available. The carried unit debit cannot be set to zero,
and the raw branch cannot be declared dead by collapse. `square`

### Corollary 46.6: Next Source Target

The next source target is not another bookkeeping reduction. It is one of the
following two same-record coefficient-time statements:

```math
\exists\Delta_\rho>0
\quad
\liminf_j t_{\rho,j}^{blk}
\ge
\theta_\rho+\Delta_\rho,
```

which closes the raw unit/rate side, or

```math
t_{\rho,j}^{blk}\to0,
```

which kills the raw route and forces the normalized surface fork to be built
as a new theorem rather than substituted by convention.

## 47. Finite-Tree Attempt To Source The Raw Block-Time Lower Bound

Section 46 leaves the raw block-time fork undecided. We now test the most
direct possible source: the finite `SEL2` tree expansion itself. The point is
to separate two statements that are easy to conflate:

1. the finite convolution tree has an explicit heat time \(T_j^{SEL2,conv}\);
2. the actual four-dimensional pushed-forward scalar coefficient is close to
   that convolution-tree coefficient.

Only the conjunction can prove the raw block-time lower bound.

### Definition 47.1: Same-Record Raw Tree Coefficient Comparison

Let \(T_j^{SEL2,conv}\) be the finite convolution time imported from Paper 20:

```math
T_j^{SEL2,conv}
=
\sum_{b\in\mathscr S_j^{SEL2}}\tau_{b,j}.
```

The raw tree coefficient comparison
\(\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}(\varepsilon_{\rho,j})\)
asserts, on the exact same pushed-forward `SEL2` scalar row law, that

```math
\left|
{a_{\rho,j}^{SEL2}\over d_\rho}
-
\exp\left(-{C_2(\rho)\over2}T_j^{SEL2,conv}\right)
\right|
\le
\varepsilon_{\rho,j},
```

with \(\varepsilon_{\rho,j}\to0\) on a cofinal tail.

This is the normalized form of the raw coefficient comparison. It is the same
scalar observable as Definition 46.1, divided by \(d_\rho\). It is not a
Wilson-loop readout and not a continuum Yang-Mills measure.

### Lemma 47.2: The Finite Tree Computes The Reference Coefficient

For the independent finite heat-kernel convolution reference on the `SEL2`
tree,

```math
{a_{\rho,j}^{conv}\over d_\rho}
=
\exp\left(-{C_2(\rho)\over2}T_j^{SEL2,conv}\right).
```

Proof.

This is Paper 20 Lemma 4.3A.160AT in Paper-21 notation. The finite sheet
increments have heat-kernel laws \(H_{\tau_{b,j}}\). Heat kernels on compact
`SU(N)` are central, inversion-invariant, and satisfy

```math
H_s*H_t=H_{s+t}.
```

Thus the ordered product of the independent finite tree increments has law
\(H_{T_j^{SEL2,conv}}\). The Peter-Weyl coefficient of the normalized central
character \(\Phi_\rho/d_\rho\) under \(H_T\) is
\(\exp(-TC_2(\rho)/2)\). `square`

### Lemma 47.3: Conditional Raw Lower-Time Bound From The Tree

Assume
\(\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}(\varepsilon_{\rho,j})\), with
\(\varepsilon_{\rho,j}\to0\). If a strict cofinal endpoint
\(T_-^{SEL2}\) satisfies

```math
T_-^{SEL2}\le T_j^{SEL2,conv}
```

on a cofinal tail, then on that tail

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
\le
\exp\left(-{C_2(\rho)\over2}T_-^{SEL2}\right)
+\varepsilon_{\rho,j}.
```

Proof.

The comparison gate gives

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
\le
\exp\left(-{C_2(\rho)\over2}T_j^{SEL2,conv}\right)
+\varepsilon_{\rho,j}.
```

Since \(T_j^{SEL2,conv}\ge T_-^{SEL2}\) and the exponential is decreasing in
time, the displayed bound follows. `square`

### Theorem 47.4: Raw Unit And Rate From A Strict Tree-Time Margin

Assume the hypotheses of Lemma 47.3. Suppose there is a strict margin
\(\Delta_\rho>0\) such that

```math
T_-^{SEL2}\ge\theta_\rho+\Delta_\rho.
```

Then the raw branch closes the unit/rate slot. More precisely,

```math
\limsup_j a_{\rho,j}^{SEL2}
\le
\exp\left(-{C_2(\rho)\over2}\Delta_\rho\right)
<1,
```

and hence every strict

```math
0<\kappa_{\rho}^{raw}
<
{C_2(\rho)\over2}\Delta_\rho
```

is an admissible raw leading-rate lower bound on the cofinal positive branch.

Proof.

By Lemma 47.3,

```math
\limsup_j {a_{\rho,j}^{SEL2}\over d_\rho}
\le
\exp\left(-{C_2(\rho)\over2}T_-^{SEL2}\right).
```

Using \(T_-^{SEL2}\ge\theta_\rho+\Delta_\rho\) and
\(\theta_\rho=2\log d_\rho/C_2(\rho)\),

```math
\exp\left(-{C_2(\rho)\over2}T_-^{SEL2}\right)
\le
{1\over d_\rho}
\exp\left(-{C_2(\rho)\over2}\Delta_\rho\right).
```

Multiplying by \(d_\rho\) gives

```math
\limsup_j a_{\rho,j}^{SEL2}
\le
\exp\left(-{C_2(\rho)\over2}\Delta_\rho\right)
<1.
```

On sign-positive cofinal rows, \(-\log\) is continuous and decreasing on
\((0,1)\), so every strict rate below
\(C_2(\rho)\Delta_\rho/2\) is certified. `square`

### Corollary 47.5: Selector-Window Version

Assume
\(\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}(\varepsilon_{\rho,j})\), with
\(\varepsilon_{\rho,j}\to0\), and the standard `SEL2` sheet-time scaling audit.
If

```math
T_{clean,-}^{SEL2}
=
s(1-\epsilon_A)(1-\chi)
>
\theta_\rho,
```

then the finite-tree route closes raw `CE-UNIT/RATE`. Quantitatively, for any
strict

```math
0<\Delta_\rho
<
s(1-\epsilon_A)(1-\chi)-\theta_\rho,
```

Theorem 47.4 applies with that \(\Delta_\rho\).

Proof.

Paper 20 Theorem 4.3A.160BB gives

```math
\liminf_jT_j^{SEL2,conv}
\ge
s(1-\epsilon_A)(1-\chi).
```

Choose \(T_-^{SEL2}\) strictly between
\(\theta_\rho+\Delta_\rho\) and \(s(1-\epsilon_A)(1-\chi)\). Then
\(T_-^{SEL2}\le T_j^{SEL2,conv}\) cofinally, and Theorem 47.4 applies.
`square`

### Lemma 47.6: What Is Actually Missing

The finite tree expansion supplies the reference coefficient and the
candidate time window. It does not, by itself, prove
\(\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}(\varepsilon_{\rho,j})\).

Proof.

Lemma 47.2 is a statement about the independent heat-kernel convolution
reference. The actual `SEL2` block plaquette marginal includes the same finite
record's Bianchi constraints, off-sheet variables, collar replacements,
counterterm/scheme corrections, and projective/readout effects. Paper 20
names the required scalar comparison as the weakened same-record coefficient
source `P20-SEL2-SCONV-CLOSE` or, in the five-term four-dimensional ledger,
`P20-SEL2-4DCOEFF-CLOSE`. Those are scalar finite-row estimates against the
same pushed-forward law; they are not consequences of the reference tree
identity alone.

Thus deleting the defect term would switch from the actual four-dimensional
`SEL2` row to the independent two-dimensional sheet reference unless the
displayed scalar comparison is proved. `square`

### Theorem 47.7: Verdict Of The Finite-Tree Raw Attempt

The finite-tree attempt proves the following conditional source theorem:

```math
\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}
(\varepsilon_{\rho,j}),\quad
\varepsilon_{\rho,j}\to0,
\qquad
\mathrm{P21\text{-}SEL2\text{-}SHEET\text{-}TIME},
\qquad
T_{clean,-}^{SEL2}>\theta_\rho
```

imply

```math
\liminf_j t_{\rho,j}^{blk}>\theta_\rho
```

with the explicit raw rate margin of Theorem 47.4.
Here \(\mathrm{P21\text{-}SEL2\text{-}SHEET\text{-}TIME}\) denotes the
standard `SEL2` sheet-time scaling audit imported from Paper 20.

However, Section 47 alone does not prove
\(\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}\). Therefore this section,
before the five-term source audit is imported, does not close

```math
U_{13}^{CE,unit,park}=0.
```

It reduces that live debit to the same-record scalar coefficient comparison
between the actual four-dimensional `SEL2` pushforward and the finite
heat-kernel convolution tree. Section 48 audits whether the strict
Paper-20 five-term scalar source supplies exactly this comparison.

Proof.

The standard sheet-time scaling gives both the lower window used in Corollary
47.5 and a finite upper cofinal window
`T_j^{SEL2,conv}\le T_+^{SEL2}<\infty`. The comparison gate therefore also
gives cofinal positivity:

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
\ge
\exp\left(-{C_2(\rho)\over2}T_+^{SEL2}\right)
-\varepsilon_{\rho,j}
>0
```

on a sufficiently far tail. Thus \(t_{\rho,j}^{blk}\) is defined cofinally.
Corollary 47.5 and Theorem 47.4 then give the strict raw subunit bound, which
is equivalent to
\(\liminf_jt_{\rho,j}^{blk}>\theta_\rho\) by Lemma 46.2.

Lemma 47.6 identifies the comparison estimate that must be supplied by a
separate five-term scalar source audit. No Wilson-loop area law, mass gap,
continuum Yang-Mills measure, or gauge-fixed field ontology is used anywhere
in the argument. `square`

## 48. Five-Term Scalar Source Audit For `P21-RAW-TREE-CMP`

Section 47 reduced the raw block-time source to a single scalar comparison.
Paper 20 contains a later five-term audit for this comparison on the strict
exact-record branch. We now import it carefully, with every strict convention
visible, so that no non-strict branch inherits a zero it has not earned.

### Definition 48.1: Strict Five-Term Branch Hypotheses

Let `P21-SEL2-STRICT-5TERM` denote the conjunction of the following
same-record hypotheses.

1. `P20-SEL2-ACTROW`: the actual finite `SEL2` row, scalar readout
   \(\psi_\rho=\Phi_\rho/d_\rho\), axial-tree block/collar chart, and
   Radon-Nikodym correction are frozen.
2. The standard `SEL2` sheet-time scaling audit holds.
3. The strict exact-record, clean-minimal-counterterm,
   collar-refined large-field branch of `P20-SEL2-CLEAN-SRC` is used.
4. The strict reduced clean-collar convention of Paper 20 Definition
   4.3A.160BH.8A is used.
5. The actual strict reduced normalized interior root branch of Paper 20
   Definition 4.3A.160BH.37 is used, with exact root covariance and no
   projective/readout replacement.

These are finite pushed-forward scalar-record conventions. They are not a
continuum Yang-Mills measure, a Wilson-loop area law, or a mass-gap input.

### Lemma 48.2: `P20-SEL2-4DCOEFF-CLOSE` Is Exactly `RAW-TREE-CMP`

On `P21-SEL2-STRICT-5TERM`, Paper 20's scalar coefficient source

```math
P20\text{-}SEL2\text{-}4DCOEFF\text{-}CLOSE(\epsilon_{\rho,j}),
\qquad
\epsilon_{\rho,j}\to0,
```

implies

```math
\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}
(\epsilon_{\rho,j}).
```

Proof.

Paper 20 Definition 4.3A.160BH defines the scalar four-dimensional
coefficient defect as

```math
\left|
\widetilde a_{\rho,j}^{SEL2}
-
\exp\left(-{C_2(\rho)\over2}T_j^{SEL2,conv}\right)
\right|,
```

where

```math
\widetilde a_{\rho,j}^{SEL2}
=
{a_{\rho,j}^{SEL2}\over d_\rho}
=
\int_G{\Phi_\rho(U)\over d_\rho}\,d\nu_{p,j}^{SEL2}(U).
```

This is exactly the comparison in Definition 47.1. The only change of name is
that Paper 20 calls the normalized scalar coefficient
\(\widetilde a_{\rho,j}^{SEL2}\), while Section 47 writes it as
\(a_{\rho,j}^{SEL2}/d_\rho\). `square`

### Lemma 48.3: Nonbulk Scalar Terms Vanish On The Strict Branch

Under `P21-SEL2-STRICT-5TERM`,

```math
E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}
\to0.
```

Proof.

This is Paper 20 Corollary 4.3A.160BH.2G. The clean minimal counterterm
convention absorbs local relevant/marginal pure-gauge counterterms into the
heat-time tangent, scalar normalization, or finite boundary scalar factor.
The clean collar branch assigns collar-transition derivatives and bad collars
to their declared collar/large-field ledger and proves the residual scalar
size vanishes. The exact finite scalar-record branch has no projective/readout
replacement, so the readout distance, bad-event probability, and scalar
transport debit are zero. The common-record clause prevents these terms from
being charged again in \(U_{11}^{RPCov}\), \(E_{14}^{park}\), or loop-readout
transport. `square`

### Lemma 48.4: Boundary Bianchi/Off-Sheet Roots Vanish On The Strict Branch

Under `P21-SEL2-STRICT-5TERM`,

```math
B_j^{sheet}\zeta_{\rho,bd,j}^{SEL2}\to0.
```

Proof.

This is Paper 20 Corollary 4.3A.160BH.9A. The finite good-collar boundary root
census proves a rooted estimate

```math
\zeta_{\rho,bd,j}^{SEL2}
\le
C_{\rho,bd}^{SEL2}g_{i(j)}^2+o(g_{i(j)}^2).
```

Since \(B_j^{sheet}=O(H_j^{1/2})\) and \(g_{i(j)}^2=H_j^{-1}\), the product
is \(o(1)\). `square`

### Lemma 48.5: Interior Bianchi/Off-Sheet Roots Vanish On The Strict Branch

Under `P21-SEL2-STRICT-5TERM`,

```math
S_j\zeta_{\rho,bulk,j}^{SEL2}\to0.
```

Proof.

Paper 20 proves the finite rootwise chain

```math
\mathrm{HKSD\text{-}TPL}
\Rightarrow
\mathrm{GENMATCH}
\Rightarrow
\mathrm{INTBULK\text{-}FOC}.
```

The ingredients are compact-group heat-kernel integration by parts, the
actual finite `SEL2` axial-tree root census, and the fact that the only
nonabsorbed second-order interior labels are `{4,33,J2}`. Paper 20 Theorem
4.3A.160BH.39 verifies `HKSD-TPL`; Corollary 4.3A.160BH.40 closes
`GENMATCH`; and Theorem 4.3A.160BH.40A gives

```math
\zeta_{\rho,bulk,j}^{SEL2}=o(H_j^{-1}).
```

Since \(S_j=O(H_j)\), the displayed interior contribution tends to zero.
`square`

### Theorem 48.6: `P21-RAW-TREE-CMP` Is Closed On The Strict Five-Term Branch

Under `P21-SEL2-STRICT-5TERM`, there exists
\(\epsilon_{\rho,j}\to0\) such that

```math
\left|
{a_{\rho,j}^{SEL2}\over d_\rho}
-
\exp\left(-{C_2(\rho)\over2}T_j^{SEL2,conv}\right)
\right|
\le
\epsilon_{\rho,j}.
```

Hence

```math
\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}
(\epsilon_{\rho,j})
```

holds on the strict branch.

Proof.

Paper 20 Corollary 4.3A.160BH.1C reduces
`P20-SEL2-4DCOEFF-CLOSE` to the five scalar terms

```math
E_{\rho,Bianchi,j}^{SEL2}
+E_{\rho,off,j}^{SEL2}
+E_{\rho,col,j}^{SEL2}
+E_{\rho,ct,j}^{SEL2}
+E_{\rho,proj,j}^{SEL2}.
```

Lemma 48.3 removes the nonbulk terms. Lemma 48.4 removes the boundary part of
the Bianchi/off-sheet envelope. Lemma 48.5 removes the interior part. Thus all
five scalar terms tend to zero. Paper 20 Corollary 4.3A.160BH.40B therefore
gives `P20-SEL2-4DCOEFF-CLOSE(\epsilon_{\rho,j})` with
\(\epsilon_{\rho,j}\to0\). Lemma 48.2 identifies this with
`P21-RAW-TREE-CMP`. `square`

### Theorem 48.7: Raw Block-Time Pass/Falsification Window On The Strict Branch

Assume `P21-SEL2-STRICT-5TERM`.

1. If

   ```math
   T_{clean,-}^{SEL2}>\theta_\rho,
   ```

   then

   ```math
   \liminf_jt_{\rho,j}^{blk}>\theta_\rho,
   ```

   and \(U_{13}^{CE,unit,park}\) may be set to zero on this strict branch.

2. If there is a strict upper gap

   ```math
   T_{clean,+}^{SEL2}<\theta_\rho,
   ```

   then the raw unit route fails on this strict branch:

   ```math
   \limsup_jt_{\rho,j}^{blk}<\theta_\rho.
   ```

3. If

   ```math
   T_{clean,-}^{SEL2}
   \le
   \theta_\rho
   \le
   T_{clean,+}^{SEL2},
   ```

   then the strict five-term audit closes the coefficient comparison but the
   coarse `SEL2` time window is inconclusive. The route then requires a sharper
   same-record liminf/limsup estimate for \(T_j^{SEL2,conv}\).

Proof.

Theorem 48.6 gives `P21-RAW-TREE-CMP`. Clause 1 is Corollary 47.5.

For clause 2, the comparison and the finite lower time window give cofinal
positivity, so \(t_{\rho,j}^{blk}\) is defined. Moreover,

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
=
\exp\left(-{C_2(\rho)\over2}T_j^{SEL2,conv}\right)+o(1).
```

The same positivity and boundedness make the logarithm continuous on the
cofinal range, hence

```math
t_{\rho,j}^{blk}
=
T_j^{SEL2,conv}+o(1).
```

If \(T_{clean,+}^{SEL2}<\theta_\rho\), then
\(\limsup_jT_j^{SEL2,conv}<\theta_\rho\), and therefore
\(\limsup_jt_{\rho,j}^{blk}<\theta_\rho\). By Lemma 46.2 the raw unit
condition eventually fails.

Clause 3 is the remaining straddling case. The comparison is closed, but the
coarse time window alone does not place \(t_{\rho,j}^{blk}\) on either side of
\(\theta_\rho\). `square`

### Corollary 48.8: Settled Status Of The Obstruction

The obstruction exposed in Section 47 is settled on the strict exact-record
branch:

```math
\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP}
```

is proved there by the five-term scalar source audit.

What remains is not the scalar comparison. It is the scalar selector
inequality

```math
T_{clean,-}^{SEL2}>\theta_\rho
```

or a sharper actual lower bound for \(T_j^{SEL2,conv}\). If that inequality
passes, the raw unit/rate slot closes. If the strict upper gap
\(T_{clean,+}^{SEL2}<\theta_\rho\) holds, the raw route fails. If the window
straddles \(\theta_\rho\), Paper 21 must sharpen the selector-time estimate
rather than revisit Bianchi/off-sheet, collar, counterterm, or projective
corrections.

## 49. Post-Audit Status Of The Raw Unit Slot

Sections 47--48 settle the obstruction requested there: the five-term scalar
comparison is closed on the strict exact-record branch. The raw unit slot now
has a clean scalar trichotomy.

### Definition 49.1: Evaluated Raw Unit Debit

On `P21-SEL2-STRICT-5TERM`, define

```math
U_{13}^{CE,unit,eval}
```

by the following same-record alternatives.

1. **Pass branch.** If \(T_{clean,-}^{SEL2}>\theta_\rho\), set

   ```math
   U_{13}^{CE,unit,eval}:=0.
   ```

2. **Failure branch.** If \(T_{clean,+}^{SEL2}<\theta_\rho\), set

   ```math
   \mathrm{P21\text{-}RAW\text{-}UNIT\text{-}FAIL}.
   ```

   No finite debit can repair the raw route under this upper-gap condition,
   because the coefficient itself is eventually larger than one.
3. **Straddling branch.** If

   ```math
   T_{clean,-}^{SEL2}\le\theta_\rho\le T_{clean,+}^{SEL2},
   ```

   replace \(U_{13}^{CE,unit,park}\) by the sharper time-window source

   ```math
   U_{13}^{CE,unit,time}
   ```

   whose sole content is to prove or falsify

   ```math
   \liminf_jT_j^{SEL2,conv}>\theta_\rho.
   ```

No other scalar correction is hidden inside \(U_{13}^{CE,unit,time}\):
Bianchi/off-sheet, collar, counterterm, projective/readout, and boundary
root corrections have already been paid in Section 48 on the strict branch.

### Theorem 49.2: `RAW-TREE-CMP` Is No Longer A Live Obstruction On The Strict Branch

Assume `P21-SEL2-STRICT-5TERM`. Then the live raw unit obstruction is exactly
the scalar selector-time trichotomy of Definition 49.1.

In particular:

```math
U_{13}^{CE,unit,park}
\quad\leadsto\quad
\begin{cases}
0, & T_{clean,-}^{SEL2}>\theta_\rho,\\
\mathrm{RAW\text{-}UNIT\text{-}FAIL}, & T_{clean,+}^{SEL2}<\theta_\rho,\\
U_{13}^{CE,unit,time}, &
T_{clean,-}^{SEL2}\le\theta_\rho\le T_{clean,+}^{SEL2}.
\end{cases}
```

Proof.

Theorem 48.6 proves `P21-RAW-TREE-CMP` on the strict branch. Theorem 48.7
then gives the pass, failure, and straddling alternatives. The straddling
case cannot be improved by re-opening the five scalar correction terms,
because those terms are already zero on the strict branch. It can only be
improved by sharpening the actual lower or upper asymptotics of
\(T_j^{SEL2,conv}\), or by changing the frozen selector. `square`

### Corollary 49.3: Next Irreducible Action

The next action is to instantiate or sharpen the selector-time data:

```math
T_j^{SEL2,conv}=S_jt_{i(j)}+o(1),
\qquad
{S_j\over H_j}\to s,
\qquad
{t_{i(j)}\over g_{i(j)}^2}\to1,
```

well enough to decide whether

```math
\liminf_jT_j^{SEL2,conv}>\theta_\rho.
```

If the existing clean window already gives
\(T_{clean,-}^{SEL2}>\theta_\rho\), raw `CE-UNIT/RATE` is closed. If the
existing upper window gives \(T_{clean,+}^{SEL2}<\theta_\rho\), the raw route
is falsified. If neither holds, the remaining work is a scalar selector-time
sharpening, not a coefficient-comparison, finite-tree, or area-law problem.

## 50. Selector-Time Inequality And The Three Cases

Sections 47--49 settle the finite-tree comparison on the strict exact-record
branch. The next step is purely scalar: decide where the frozen selector
parameter \(s\) places the actual block time relative to the raw unit
threshold \(\theta_\rho\).

### Definition 50.1: Raw Selector-Time Endpoints

Assume `TTIME-DATA`
\((\rho,s,\epsilon_A,\chi,\widehat\eta_{*,20})\). Define

```math
S_{raw}^{pass}(\rho)
:=
{\theta_\rho\over(1-\epsilon_A)(1-\chi)}
=
\frac{2\log d_\rho}{C_2(\rho)(1-\epsilon_A)(1-\chi)},
```

and

```math
S_{raw}^{fail}(\rho)
:=
{\theta_\rho\over(1+\epsilon_A)(1+\chi)}
=
\frac{2\log d_\rho}{C_2(\rho)(1+\epsilon_A)(1+\chi)}.
```

The first endpoint is the certified pass line for the coarse clean lower
window. The second is the certified failure line for the coarse clean upper
window. The closed interval between them is a genuine resolution gap of the
coarse time audit, not an analytic defect in the coefficient comparison.

### Lemma 50.2: Selector-Time Trichotomy In The Variable \(s\)

Assume `P21-SEL2-STRICT-5TERM`.

1. If

   ```math
   s>S_{raw}^{pass}(\rho),
   ```

   then raw `CE-UNIT/RATE` passes.

2. If

   ```math
   s<S_{raw}^{fail}(\rho),
   ```

   then the raw unit route fails.

3. If

   ```math
   S_{raw}^{fail}(\rho)
   \le s\le
   S_{raw}^{pass}(\rho),
   ```

   then the strict five-term audit is not the bottleneck; the remaining
   problem is a sharper lower or upper asymptotic for
   \(T_j^{SEL2,conv}\).

Proof.

The inequalities are exactly

```math
s(1-\epsilon_A)(1-\chi)>\theta_\rho
```

and

```math
s(1+\epsilon_A)(1+\chi)<\theta_\rho,
```

rewritten in the variable \(s\). Theorem 48.7 then gives the pass, failure,
and straddling alternatives. Equality is deliberately assigned to the
straddling case, because a strict raw subunit gap requires a strict time
margin. `square`

### Definition 50.3: Combined Tree-Time And Raw-Unit Time Floor

On any branch where the Paper-20 tree-time gate and the raw unit gate are
both required, define the combined lower endpoint

```math
S_{time}^{tree+raw}(\rho)
:=
\max\{S_T^{pass}(\rho),S_{raw}^{pass}(\rho)\}.
```

For the adaptive worksheet of Section 5, the same formula is interpreted
pointwise: the tree-time endpoint uses the local value
\(\widehat\eta_{*,20}(s)\), while the raw endpoint is independent of the
decoration activity.

### Lemma 50.4: When Tree-Time Automatically Implies Raw Unit

At a fixed candidate \(s\), suppose the tree-time numerator satisfies

```math
G_{13,tree}^{SEL2}(s)
\ge
\log d_\rho,
```

where

```math
G_{13,tree}^{SEL2}(s)
:=
1+
\log 19
+20{\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}.
```

Then the tree-time pass inequality at that same \(s\) implies the raw unit
pass inequality.

In particular, on the fundamental channel of `SU(N)`, this automatic
implication holds whenever

```math
\log N\le
1+
\log19
+20{\widehat\eta_{*,20}(s)\over1-\widehat\eta_{*,20}(s)}.
```

Proof.

The tree-time lower endpoint is

```math
{2G_{13,tree}^{SEL2}(s)
\over C_2(\rho)(1-\epsilon_A)(1-\chi)},
```

whereas the raw unit lower endpoint is

```math
{2\log d_\rho
\over C_2(\rho)(1-\epsilon_A)(1-\chi)}.
```

The denominators are identical and positive. Hence the displayed numerator
inequality makes the tree-time endpoint at least as large as the raw endpoint.
The fundamental-channel statement is the specialization \(d_\rho=N\).
`square`

### Theorem 50.5: Selector-Time Status

On `P21-SEL2-STRICT-5TERM`, the raw unit obstruction is no longer a finite
tree, Bianchi/off-sheet, collar, counterterm, projective/readout, or
whole-process problem. It is exactly the scalar decision

```math
s>S_{raw}^{pass}(\rho),
\qquad
s<S_{raw}^{fail}(\rho),
\qquad
S_{raw}^{fail}(\rho)\le s\le S_{raw}^{pass}(\rho).
```

The first alternative closes raw `CE-UNIT/RATE`; the second falsifies the raw
route; the third parks only the selector-time sharpness source.

Proof.

Theorem 48.6 closes the coefficient comparison. Lemma 50.2 rewrites Theorem
48.7 as an explicit inequality in \(s\). The terms forbidden by the statement
are exactly the five scalar correction classes already shown to vanish in
Section 48 on the strict branch. `square`

## 51. Raw `CE` Sign, Unit, And Rate On The Pass Branch

The old Section-43 verdict was correct before the strict five-term audit was
performed. On the strict branch, Sections 48--50 sharpen it: sign is a
consequence of the same comparison and finite upper time window, while unit
and positive rate are consequences of the strict selector-time pass.

### Lemma 51.1: Cofinal Positivity Of The Raw Leading Coefficient

Assume `P21-SEL2-STRICT-5TERM` and finite clean upper time window
\(T_{clean,+}^{SEL2}<\infty\). Then

```math
\liminf_j {a_{\rho,j}^{SEL2}\over d_\rho}>0.
```

In particular,

```math
U_{13}^{CE,sign,park}=0
```

on the strict exact-record branch.

Proof.

By Theorem 48.6,

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
=
\exp\left(-{C_2(\rho)\over2}T_j^{SEL2,conv}\right)
+o(1).
```

The standard sheet-time audit gives
\(T_j^{SEL2,conv}\le T_{clean,+}^{SEL2}+o(1)\) on a cofinal tail. Hence, for
all sufficiently large \(j\),

```math
{a_{\rho,j}^{SEL2}\over d_\rho}
\ge
{1\over2}
\exp\left(-{C_2(\rho)\over2}(T_{clean,+}^{SEL2}+1)\right)>0.
```

This proves cofinal positivity and removes the sign debit. `square`

### Lemma 51.2: Raw Unit And Rate With Explicit Margin

Assume `P21-SEL2-STRICT-5TERM` and

```math
s>S_{raw}^{pass}(\rho).
```

Let

```math
0<\Delta_\rho<
s(1-\epsilon_A)(1-\chi)-\theta_\rho.
```

Then

```math
\limsup_j a_{\rho,j}^{SEL2}
\le
\exp\left(-{C_2(\rho)\over2}\Delta_\rho\right)<1,
```

and therefore

```math
\liminf_j -\log a_{\rho,j}^{SEL2}
\ge
{C_2(\rho)\over2}\Delta_\rho>0.
```

Proof.

This is Theorem 47.4 with
\(T_-^{SEL2}\) chosen strictly between
\(\theta_\rho+\Delta_\rho\) and
\(s(1-\epsilon_A)(1-\chi)\). The strict inequality in the hypothesis ensures
such a choice exists. Lemma 51.1 supplies cofinal positivity, so the logarithm
is defined on the same cofinal tail. `square`

### Definition 51.3: Evaluated Raw `CE-WIN` Without Tail

On the strict pass branch

```math
\mathrm{P21\text{-}SEL2\text{-}STRICT\text{-}5TERM}
\quad\text{and}\quad
s>S_{raw}^{pass}(\rho),
```

define the evaluated sign/unit/rate contribution by

```math
U_{13}^{CE,signunit,eval}:=0.
```

Equivalently,

```math
U_{13}^{CE,sign,park}=0,
\qquad
U_{13}^{CE,unit,park}=0.
```

The only coefficient-window term not decided by sign/unit/rate is the
non-leading character-tail ledger.

### Theorem 51.4: Raw Sign/Unit/Rate Pass Verdict

On the strict exact-record branch, if

```math
s>S_{raw}^{pass}(\rho),
```

then raw `CE-SIGN`, raw `CE-UNIT`, and the positive raw leading-rate estimate
all pass on the same pushed-forward scalar law. The certified lower rate can
be any strict value

```math
0<\kappa_{\rho}^{raw}
<
{C_2(\rho)\over2}
\left(s(1-\epsilon_A)(1-\chi)-\theta_\rho\right).
```

No Wilson-loop area law, mass gap, or continuum Yang-Mills measure appears in
this proof.

Proof.

Lemma 51.1 proves sign. Lemma 51.2 proves strict subunitness and the displayed
positive lower bound for \(-\log a_{\rho,j}^{SEL2}\). The hypotheses are
exactly same-record finite scalar hypotheses from Section 48 plus the scalar
selector-time inequality. `square`

## 52. Non-Leading Character Tail: What Is Closed And What Is Not

The raw leading coefficient window has two different parts. Sections 50--51
settle the leading sign/unit/rate on the strict time-pass branch. They do not
by themselves close the non-leading representation tail. That tail is a
separate Peter-Weyl summability statement.

### Definition 52.1: Same-Record Tail Gates

Let \(\widetilde a_{\lambda,j}^{SEL2}\) denote the normalized central
coefficient of the active exact `SEL2` plaquette row law in channel \(\lambda\).
The finite cofinal tail gate is

```math
\mathrm{P21\text{-}CE\text{-}TAIL\text{-}FIN}(E_\rho):
\qquad
\limsup_j
\sum_{\substack{\lambda\ne0\\ \lambda\ne\rho}}
d_\lambda|\widetilde a_{\lambda,j}^{SEL2}|
\le E_\rho<\infty.
```

The no-double-charge inclusion gate is

```math
\mathrm{P21\text{-}CE\text{-}TAIL\text{-}INCH}:
```

the exact seminorm in `P21-CE-TAIL-FIN` is already included in the active
Paper-19/Paper-20 character-tail or decoration ledger, with the same
representation cutoff, same normalization, and same pushed-forward row law.

The strict tail-tightness gate is

```math
\mathrm{P21\text{-}CE\text{-}TAIL\text{-}TIGHT}:
\qquad
\lim_{R\to\infty}\limsup_j
\sum_{\substack{\lambda\ne0\\ \lambda\ne\rho\\ C_2(\lambda)>R}}
d_\lambda|\widetilde a_{\lambda,j}^{SEL2}|=0.
```

### Lemma 52.2: Rowwise Peter-Weyl Regularity Does Not Close The Cofinal Tail

The finite-row central \(L^1\) density and rowwise Peter-Weyl expansion prove
that every row has a well-defined tail. They do not imply
`P21-CE-TAIL-FIN(E_rho)` for any finite certified \(E_\rho\), and they do not
imply `P21-CE-TAIL-TIGHT`.

Proof.

Rowwise finiteness is a statement at fixed \(j\). The gates in Definition
52.1 are moving-row limsup statements. A sequence of finite numbers may have
infinite limsup, and even a uniformly finite partial cutoff need not imply
high-representation tightness. This is the same separation recorded in Paper
20 Corollaries 4.3A.165C--4.3A.165C.3. `square`

### Lemma 52.3: How The Tail Debit Is Evaluated

On the strict sign/unit/rate pass branch, the remaining tail debit is

```math
U_{13}^{CE,tail,eval}
=
\begin{cases}
0,
&\mathrm{P21\text{-}CE\text{-}TAIL\text{-}FIN}(E_\rho)
\text{ and }
\mathrm{P21\text{-}CE\text{-}TAIL\text{-}INCH},\\[1mm]
E_\rho,
&\mathrm{P21\text{-}CE\text{-}TAIL\text{-}FIN}(E_\rho)
\text{ but not }
\mathrm{P21\text{-}CE\text{-}TAIL\text{-}INCH},\\[1mm]
U_{13}^{CE,tail,park},
&\mathrm{P21\text{-}CE\text{-}TAIL\text{-}FIN}(E_\rho)
\text{ is not proved.}
\end{cases}
```

If `P21-CE-TAIL-TIGHT` is also proved under the exact same seminorm, it
licenses exact de-smearing and cutoff removal; it still does not permit a
zero debit unless `P21-CE-TAIL-INCH` verifies that the finite remaining tail
has already been paid elsewhere.

Proof.

The tail is either already part of an existing disjoint ledger, in which case
charging it again would double-count it, or it is a new nonsurface entry cost,
in which case the finite cofinal bound is the honest carried value. If no
finite cofinal bound is proved, the parked symbol remains. Tightness controls
the high-representation cutoff but is not the same as proving that the finite
tail budget is already included in another ledger. `square`

### Theorem 52.4: Exact Status Of The `CE` Window After The Strict Time Pass

Assume `P21-SEL2-STRICT-5TERM` and \(s>S_{raw}^{pass}(\rho)\). Then

```math
U_{13}^{CE,win,park}
\leadsto
U_{13}^{CE,tail,eval}.
```

Thus the leading sign/unit/rate obstruction is settled. The only remaining
`CE-WIN` obstruction is the non-leading tail, evaluated by Definition 52.1
and Lemma 52.3.

Proof.

Lemma 43.2 already set the de-smearing slot to zero on the exact unsmoothed
branch. Theorem 51.4 sets the sign and unit/rate slots to zero on the strict
time-pass branch. Lemma 52.3 gives the remaining tail alternatives. `square`

## 53. Feasibility Rerun With The Evaluated `CE` Slots

We now rerun the active non-corner feasibility ledger after the strict
five-term comparison and selector-time pass have been used. This does not
pretend that the entire branch is closed; it only removes the `CE` pieces
that have actually been earned.

### Definition 53.1: Evaluated Non-Corner Envelope

Assume the strict exact-record branch and \(s>S_{raw}^{pass}(\rho)\). Define

```math
\mathcal R_{noncorn}^{53,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{RPF,bd}
+U_{13}^{CE,tail,eval}.
```

Equivalently, relative to Section 45,

```math
\mathcal R_{noncorn}^{53,SEL2}(s)
=
\mathcal R_{noncorn}^{45,SEL2}(s)
-U_{13}^{CE,sign,park}
-U_{13}^{CE,unit,park}
-U_{13}^{CE,tail,park}
+U_{13}^{CE,tail,eval}.
```

This replacement is legal only under the strict five-term hypotheses and the
raw selector-time pass. Outside that branch, Section 45 remains the active
ledger.

### Definition 53.2: Evaluated Feasibility Surplus

For candidates satisfying both the non-corner admissibility conditions and the
raw selector-time pass, set

```math
\Phi_{53}^{SEL2}(s)
:=
S_{NC}(s)-\mathcal R_{noncorn}^{53,SEL2}(s),
```

and

```math
\Pi_{53}^{max}(\rho)
:=
\sup_{\substack{
s\in\mathcal A_{NC}(\rho)\\ s>S_{raw}^{pass}(\rho)}}
\Phi_{53}^{SEL2}(s).
```

### Theorem 53.3: Feasibility Verdict After Steps 1--5

The requested five-step pass settles the raw leading-coefficient obstruction
on the strict time-pass branch, but it does not yet prove full non-corner
feasibility. The exact current verdict is:

1. If \(s<S_{raw}^{fail}(\rho)\), the raw route is falsified.
2. If \(S_{raw}^{fail}(\rho)\le s\le S_{raw}^{pass}(\rho)\), the route is
   parked only on selector-time sharpness.
3. If \(s>S_{raw}^{pass}(\rho)\), sign/unit/rate are closed, and the active
   feasibility test becomes

   ```math
   \Phi_{53}^{SEL2}(s)>0.
   ```

At the present source level, Paper 21 still does not prove

```math
\Pi_{53}^{max}(\rho)>0,
```

because the remaining displayed envelope contains the unevaluated or carried
terms

```math
E_{14}^{park},\quad
X_{13}^{(26),SEL2},\quad
U_{12}^{(27),SEL2},\quad
U_{11}^{RPCov,car,SEL2}(s),
```

```math
U_{13}^{BC,new},\quad
U_{13}^{RPF,bd},\quad
U_{13}^{CE,tail,eval}.
```

Proof.

Lemma 50.2 gives the three selector-time alternatives. Theorem 51.4 closes
the sign/unit/rate part of the raw coefficient window on the pass branch.
Theorem 52.4 leaves exactly the evaluated tail debit. Substituting these
results into Section 45 gives Definition 53.1. No theorem in the current
source package supplies finite sharp bounds, zero theorems, or lower floors
for all seven remaining envelope terms. Hence neither a pass certificate nor
a falsification certificate follows. `square`

### Corollary 53.4: What Is Settled For Good By This Iteration

On the strict exact-record branch, the following issues are no longer live:

```math
\mathrm{P21\text{-}RAW\text{-}TREE\text{-}CMP},
\qquad
U_{13}^{CE,sign,park},
\qquad
U_{13}^{CE,unit,park}
```

provided \(s>S_{raw}^{pass}(\rho)\). The remaining live `CE` issue is only the
non-leading tail/no-double-charge audit. The remaining live feasibility
issues outside `CE` are the seven terms displayed in Theorem 53.3.

## 54. Six-Step Closure Pass: Time, Tail, Envelope, And Transport

Sections 50--53 settled the raw leading coefficient on the strict time-pass
branch. This section executes the promised remaining pass through the six
active questions:

1. lock the time branch;
2. close or carry the non-leading `CE` tail;
3. rerun the feasibility surplus;
4. recheck \(E_{14}^{park}\);
5. reduce the cheap finite-battery terms;
6. decide \(U_{11}^{RPCov}\).

The point is not to rename old parked symbols. The point is to remove every
debit that the strict same-record branch really has paid and to identify the
small final list that is still not settled by the current corpus.

### Definition 54.1: Active Time-Locked Domain

Define the strict raw-time admissible domain by

```math
\mathcal A_{raw}^{SEL2}(\rho)
:=
\{s\in\mathcal A_{NC}(\rho):s>S_{raw}^{pass}(\rho)\}.
```

Equivalently, \(s\in\mathcal A_{raw}^{SEL2}(\rho)\) means that the no-corner
non-surface worksheet is admissible and the raw leading coefficient has the
strict selector-time margin required by Theorem 51.4.

The complementary coarse failure domain is

```math
\mathcal F_{raw}^{SEL2}(\rho)
:=
\{s>0:s<S_{raw}^{fail}(\rho)\}.
```

The remaining coarse straddling band is

```math
\mathcal S_{raw}^{SEL2}(\rho)
:=
\{s>0:S_{raw}^{fail}(\rho)\le s\le S_{raw}^{pass}(\rho)\}.
```

### Lemma 54.2: Time Branch Decision

On `P21-SEL2-STRICT-5TERM`:

1. If \(s\in\mathcal A_{raw}^{SEL2}(\rho)\), then raw sign, raw unit, and a
   positive raw rate are closed.
2. If \(s\in\mathcal F_{raw}^{SEL2}(\rho)\), the raw route is falsified for
   that selector.
3. If \(s\in\mathcal S_{raw}^{SEL2}(\rho)\), the route is parked only on the
   selector-time sharpness source.

Proof.

This is Definition 54.1 plus Lemma 50.2 and Theorem 51.4. The statement is
purely scalar in \(s\); it uses no Wilson-loop area law and no continuum
Yang-Mills measure. `square`

### Corollary 54.3: Automatic Raw Pass Under The Tree-Time Numerator

If a candidate \(s\in\mathcal A_{NC}(\rho)\) also satisfies

```math
G_{13,tree}^{SEL2}(s)\ge\log d_\rho,
```

then \(s\in\mathcal A_{raw}^{SEL2}(\rho)\). Hence, for such candidates, the
Paper-20 tree-time pass automatically locks the raw unit/rate branch.

Proof.

This is Lemma 50.4 restricted to the already admissible no-corner domain.
`square`

## 55. Closing The Incremental `CE` Tail Debit

The remaining `CE` issue in Section 53 was deliberately phrased as a
no-double-charge problem. Paper 20 already contains the needed source: the
same `P19-CHTAIL-AUDIT` used by the `SEL2` decoration ledger bounds the
non-leading `CE` tail. Therefore the tail is not a new exact-entry debit on
the active `SEL2` branch.

### Lemma 55.1: Paper 20 Supplies The Same-Record Finite Tail

On the frozen `P20-SEL2(\eta_{ch,20}^{SEL2},20)` selector,

```math
\mathrm{P21\text{-}CE\text{-}TAIL\text{-}FIN}
(\eta_{ch,20}^{SEL2})
```

holds.

Proof.

Paper 20 Theorem 3.2 states that `P20-DEC-SRC` gives

```math
\epsilon_{13}^{CE}\le\eta_{ch}^*<\infty
```

on the same character/decorrelation ledger. For the active selector,
\(\eta_{ch}^*=\eta_{ch,20}^{SEL2}\). Paper 19
Theorem 8L.11A.22G.4D.22 identifies this \(\epsilon_{13}^{CE}\) with the
non-leading weighted `CE` character tail

```math
\limsup_j
\sum_{\substack{\lambda\ne0\\ \lambda\ne\rho}}
d_\lambda|\widetilde a_{\lambda,j}^{SEL2}|.
```

This is exactly Definition 52.1 with
\(E_\rho=\eta_{ch,20}^{SEL2}\). `square`

### Lemma 55.2: The Same Tail Is Already Paid In The Decoration Ledger

On the active strict `SEL2` branch,

```math
\mathrm{P21\text{-}CE\text{-}TAIL\text{-}INCH}
```

holds.

Proof.

Paper 20 Definition 1.10 freezes the `SEL2` selector with a declared
character-tail budget

```math
P19\text{-}CHTAIL\text{-}AUDIT(\eta_{ch,20}^{SEL2})
```

and the same finite area-collar enumeration `C_area=20`. Paper 20 Theorem
4.3A.35 pays the decoration debit using this character-tail activity, and
Paper 20 Lemma 4.3A.160AA says that non-leading representation insertions
remain in that same character-tail/decorrelation ledger rather than becoming
a new leading-sheet surcharge.

The seminorm in Lemma 55.1 is the same weighted character-tail seminorm:
same representation cutoff schedule, same normalized central coefficients,
and same pushed-forward `SEL2` plaquette law. Hence charging it again inside
the exact-entry `CE` window would double-count the object already included in
the `D_{20}(s)` decoration subtraction. `square`

### Theorem 55.3: Incremental `CE` Tail Debit Is Zero

On the active strict raw-time branch,

```math
U_{13}^{CE,tail,eval}=0.
```

The non-leading tail itself is not zero. What is zero is the additional
exact-entry debit after the already-paid character-tail/decorrelation ledger
has been identified.

Proof.

Lemma 55.1 proves `P21-CE-TAIL-FIN` with
\(E_\rho=\eta_{ch,20}^{SEL2}\). Lemma 55.2 proves the inclusion gate
`P21-CE-TAIL-INCH`. The first case of Lemma 52.3 then applies. `square`

### Corollary 55.4: `CE-WIN` Is Closed On The Strict Raw-Time Branch

If `P21-SEL2-STRICT-5TERM` holds and
\(s\in\mathcal A_{raw}^{SEL2}(\rho)\), then

```math
U_{13}^{CE,win,park}\leadsto0.
```

Proof.

Theorem 51.4 zeros sign and unit/rate. Lemma 43.2 zeros the de-smearing slot
on the exact unsmoothed branch. Theorem 55.3 zeros the incremental
non-leading tail debit by no-double-charge inclusion. `square`

## 56. Feasibility Rerun After Closing `CE-WIN`

With `CE-WIN` closed on the active strict raw-time branch, the non-corner
worksheet shrinks by one full live bucket.

### Definition 56.1: Post-`CE` Non-Corner Envelope

For \(s\in\mathcal A_{raw}^{SEL2}(\rho)\), define

```math
\mathcal R_{noncorn}^{56,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{BC,new}
+U_{13}^{RPF,bd}.
```

Equivalently,

```math
\mathcal R_{noncorn}^{56,SEL2}(s)
=
\mathcal R_{noncorn}^{53,SEL2}(s)
-U_{13}^{CE,tail,eval}.
```

### Definition 56.2: Post-`CE` Surplus

Set

```math
\Phi_{56}^{SEL2}(s)
:=
S_{NC}(s)-\mathcal R_{noncorn}^{56,SEL2}(s),
```

and

```math
\Pi_{56}^{max}(\rho)
:=
\sup_{s\in\mathcal A_{raw}^{SEL2}(\rho)}
\Phi_{56}^{SEL2}(s).
```

### Theorem 56.3: Post-`CE` Feasibility Status

The coefficient-entry bucket is now closed on the strict raw-time branch, but
the branch is not yet certified through the full non-corner worksheet. The
current pass certificate is exactly

```math
\Pi_{56}^{max}(\rho)>0.
```

The current corpus does not prove this inequality, because the six terms in
\(\mathcal R_{noncorn}^{56,SEL2}\) still lack simultaneous sharp certified
ceilings. It also does not prove a lower-floor falsification for those six
terms.

Proof.

Theorem 55.3 removes the last `CE` term from Definition 53.1. The resulting
envelope is Definition 56.1. A positive supremum is precisely the no-corner
pass certificate of Theorem 36.4 restricted to the raw-time domain. No current
section proves all six remaining terms small enough, and no matching lower
floor proves they must exceed \(S_{NC}\). `square`

## 57. Rechecking \(E_{14}^{park}\) After The `CE` Closure

Closing the `CE` window does not automatically close the Paper-14 export
debit. This distinction matters: `CE-WIN` is a coefficient-window source for
the active Paper-13 entry chain, while \(E_{14}^{park}\) is a Paper-14 export
comparison debit.

### Lemma 57.1: The `CE` Tail Inclusion Does Not Delete \(E_{14}^{park}\)

The proof of Theorem 55.3 does not imply

```math
E_{14}^{park}=0.
```

Proof.

Theorem 55.3 uses the Paper-19/Paper-20 character-tail ledger to show that
the non-leading `CE` tail has already been paid inside the `SEL2` decoration
debit. The Paper-14 export debit is a different finite-process comparison
ledger with components for identity, projective, chart, counterterm, volume,
covariance, reflection positivity, `CE`, and tail transport. Sections 38--44
already show that those Paper-14 component rates are not proved zero on the
active moving `SEL2` row.

Thus deleting the incremental `CE` tail from the Paper-13 exact-entry bucket
does not prove that the Paper-14 export comparison has zero defect. `square`

### Definition 57.2: Current Honest Paper-14 Fork

The Paper-14 term remains

```math
E_{14}^{park}
```

unless one of the following same-record gates is proved:

```math
\mathrm{P21\text{-}E14\text{-}NINE0},
\qquad
\mathrm{P21\text{-}E14\text{-}RED}(E_{14}^{red}),
\qquad
\mathrm{P21\text{-}E14\text{-}BYPASS}.
```

Here `NINE0` is the full nine-component zero audit, `RED` is a componentwise
reduced finite ceiling, and `BYPASS` is a direct Paper-13/Paper-20 source
that avoids the Paper-14 export theorem on the active scalar law.

### Theorem 57.3: \(E_{14}^{park}\) Is Still Live

At the current source level,

```math
E_{14}^{park}
```

remains in the post-`CE` envelope. The strongest honest replacement currently
available is symbolic:

```math
E_{14}^{park}\rightsquigarrow E_{14}^{red}
```

only under `P21-E14-RED(E_{14}^{red})`; otherwise no reduction is licensed.

Proof.

This is Theorem 39.10 and Theorem 44.4, with Lemma 57.1 excluding the only
new possible confusion created by the `CE` closure. `square`

## 58. Cheap Finite-Battery Reductions After `CE`

The next cheapest reductions are finite-battery bookkeeping terms. We can
strengthen one of them now: the free `BC` bucket can be eliminated by a
saturated component assignment. The other finite-battery buckets remain on
their already proved zero-or-carry forks.

### Definition 58.1: Saturated Exact-Entry Component Assignment

The saturated assignment is the convention that every scalar record needed by
the Paper-13 exact-entry chain is assigned to exactly one of the following
disjoint homes:

1. the exact-entry dynamic battery already charged through \(X_{13}^{(26),SEL2}\);
2. the coefficient-entry `CE` window, now closed by Sections 51 and 55;
3. the residual-factorization battery charged through \(U_{13}^{RPF,bd}\);
4. the already-paid `SEL2` decoration ledger, for `KPdec` records;
5. the same-law whole-process clause, for `WP` records.

After this assignment, no scalar record is left in the free new `BC` battery:

```math
\mathcal B_{BC,j}^{new,SEL2}=\varnothing
```

cofinally.

### Lemma 58.2: Saturation Zeros The Free `BC` Debit

Under the saturated exact-entry assignment,

```math
U_{13}^{BC,new}=0.
```

Proof.

Definition 31.1 placed in \(\mathcal B_{BC,j}^{new,SEL2}\) only those records
not literally covered by the \(X_{13}\) exact battery and not assigned to
`CE`, `RPF`, `KPdec`, or `WP`. Definition 58.1 assigns every remaining record
to one of those component homes. Therefore the residual supremum defining
\(U_{13}^{BC,new}\) is over the empty family cofinally. `square`

### Lemma 58.3: \(X_{13}\), \(U_{12}\), And `RPF` Stay On Their Existing Forks

After the `CE` closure and saturated `BC` assignment, the remaining cheap
finite-battery terms are exactly

```math
X_{13}^{(26),SEL2},\qquad
U_{12}^{(27),SEL2},\qquad
U_{13}^{RPF,bd}.
```

Their current evaluations are:

```math
X_{13}^{(26),SEL2}=0
```

only under `P21-X13-ROWBC`, otherwise

```math
X_{13}^{(26),SEL2}\le2B_{X,dyn}^{SEL2}
```

under the dynamic finite-carry gate;

```math
U_{12}^{(27),SEL2}=0
```

only under `P21-T12-P12-DIAG0`, otherwise

```math
U_{12}^{(27),SEL2}\le U_{12}^{P12,bd,SEL2}
```

under a finite Paper-12 residual ceiling; and

```math
U_{13}^{RPF,bd}=0
```

only under `P21-U13-RPF-FACT0`, otherwise it remains the finite template
factorization carry of Definition 33.3.

Proof.

The \(X_{13}\) statement is Theorem 26.4. The \(U_{12}\) statement is Theorem
27.4. The `RPF` statement is Theorem 33.4. The `CE` and `BC` changes do not
alter those hypotheses and do not create new convergence, Paper-12, or
factorization estimates. `square`

### Corollary 58.4: Envelope After Cheap Reductions

On the active strict raw-time saturated branch,

```math
\mathcal R_{noncorn}^{58,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

The terms `CE-WIN` and `BC-new` are absent for proved reasons: `CE-WIN` by
Corollary 55.4 and `BC-new` by Lemma 58.2.

## 59. Final Decision For \(U_{11}^{RPCov}\) In This Pass

The last requested item is \(U_{11}^{RPCov}\). It cannot be zeroed by the
coefficient, decoration, or finite-battery arguments above. It is a moving-row
Paper-16 RP/covariance transport tail.

### Lemma 59.1: Current Sources Still Do Not Prove RP/Cov Diagonal Vanishing

The current Paper-21 source package does not prove

```math
\sum_{k\ge j}D_{11;j,k}^{RP,red,SEL2}(s)\to0,
\qquad
\sup_g\sum_{k\ge j}D_{11;j,k}^{Cov,red,SEL2}(g;s)\to0.
```

Proof.

Sections 28--29 already isolate the missing data as
`P21-U11-RPCOV-RATEDATA`: row-shell envelopes whose moving-row tails vanish on
the active `SEL2` schedule. None of Sections 50--58 supplies such Paper-16
rate data. The strict coefficient comparison, character-tail inclusion,
Paper-14 audit, and saturated finite-entry assignment are disjoint ledgers;
none is an RP or covariance transport theorem. `square`

### Theorem 59.2: \(U_{11}^{RPCov}\) Is Carried, Not Zeroed

At the end of this six-step pass, the only licensed evaluation is

```math
U_{11}^{RPCov,car,SEL2}(s)\le
U_{11}^{RP,bd,SEL2}(s)+U_{11}^{Cov,bd,SEL2}(s),
```

provided the two finite ceilings are proved. The zero conclusion is licensed
only if the two moving-row diagonal limits in Lemma 59.1 are proved.

Proof.

This is Theorem 28.5 plus Lemma 59.1. The no-double-charge rule prevents
moving perimeter/cusp, smearing, loop-readout, `X_13`, `CE`, Paper-14, or
decoration costs into this slot. `square`

## 60. Settled Six-Step Status

Combining Sections 54--59 gives the sharp current endpoint of Paper 21.

### Definition 60.1: Final Six-Step Envelope

On the active strict raw-time saturated branch, define

```math
\mathcal R_{noncorn}^{60,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

The associated surplus is

```math
\Phi_{60}^{SEL2}(s)
:=
S_{NC}(s)-\mathcal R_{noncorn}^{60,SEL2}(s),
```

with optimized value

```math
\Pi_{60}^{max}(\rho)
:=
\sup_{s\in\mathcal A_{raw}^{SEL2}(\rho)}
\Phi_{60}^{SEL2}(s).
```

### Theorem 60.2: Six-Step Pass Verdict

The issues settled by this pass are:

```math
U_{13}^{CE,win,park}=0,
\qquad
U_{13}^{BC,new}=0
```

on the active strict raw-time saturated branch.

The remaining live nonsurface terms are exactly

```math
E_{14}^{park},\quad
X_{13}^{(26),SEL2},\quad
U_{12}^{(27),SEL2},\quad
U_{11}^{RPCov,car,SEL2}(s),\quad
U_{13}^{RPF,bd}.
```

The branch is certified through the non-corner worksheet if

```math
\Pi_{60}^{max}(\rho)>0.
```

The present source package still does not prove this pass inequality and does
not prove a matching lower-floor falsification. Therefore the honest final
status after the requested six-step audit is

```math
\mathrm{P21\text{-}SIXSTEP\text{-}REDUCED\text{-}UNDECIDED},
```

with only the five displayed terms still live.

Proof.

Time is settled by Lemma 54.2. The `CE` window is closed by Corollary 55.4.
The surplus rerun is Definition 56.2. Paper-14 remains live by Theorem 57.3.
The saturated finite-battery assignment zeros `BC-new` by Lemma 58.2 and
leaves \(X_{13}\), \(U_{12}\), and `RPF` on the forks of Lemma 58.3.
\(U_{11}^{RPCov}\) remains carried by Theorem 59.2. Substituting these results
gives Definition 60.1. No theorem in the current paper proves the optimized
surplus positive or proves lower floors forcing it nonpositive. `square`

### Corollary 60.3: Next Irreducible Work

After this pass, further progress must attack one of the five remaining terms
directly. In order of leverage:

1. prove `P21-E14-NINE0`, `P21-E14-RED`, or `P21-E14-BYPASS`;
2. prove `P21-X13-ROWBC` or sharpen \(B_{X,dyn}^{SEL2}\);
3. prove `P21-T12-P12-DIAG0` or sharpen \(U_{12}^{P12,bd,SEL2}\);
4. prove the Paper-16 moving-row RP/Cov rate data;
5. prove `P21-U13-RPF-FACT0` or sharpen \(U_{13}^{RPF,bd}\).

No remaining item is a hidden `CE` coefficient-window problem, and no remaining
item may be discharged by importing an area law, a mass gap, or a continuum
Yang-Mills measure.

## 61. Common \(E_{14}/X_{13}\) Finite-Battery `BLU` Bypass

Sections 57--60 leave \(E_{14}^{park}\) and \(X_{13}^{(26),SEL2}\) as two
separate live terms. They are separate in the debit ledger, but they share one
possible proof source: finite-battery block-limit uniqueness. Paper 13 proves
that a determining finite-block identity ledger gives `BLU`, hence `BC`.
Paper 14 proves exact compact-group Schwinger-Dyson identities before
projection and then reduces `BLU` to projection control and a determining
identity system. This section packages the common source without pretending
that it is already proved.

### Definition 61.1: Common Dynamic Battery

For each active `SEL2` row \(j\), define the common dynamic finite battery

```math
\mathcal B_{61,j}^{SEL2}
:=
B_{13,j}^{dyn,SEL2}
\cup
B_{14,j}^{ID/proj,SEL2}
\cup
B_{14,j}^{forced,SEL2}.
```

Here:

1. \(B_{13,j}^{dyn,SEL2}\) is the dynamic exact-entry battery of Definition
   26.1.
2. \(B_{14,j}^{ID/proj,SEL2}\) is the finite scalar record battery on which the
   Paper-14 identity and projection defects \(e_{ID,j}^{SEL2}\) and
   \(e_{proj,j}^{SEL2}\) are evaluated.
3. \(B_{14,j}^{forced,SEL2}\) is the finite list of records generated from
   \(\mathcal B_{61,j}^{SEL2}\) by one projected Schwinger-Dyson or loop
   identity step, after applying the same degree and representation cutoffs as
   the active row.

The battery is admissible only if all three pieces are read from the same
pushed-forward law

```math
\Gamma_j^{SEL2}=\rho_j(Law_*^{SEL2})
```

and no member is evaluated under a second regulator, chart, or comparison law.

### Definition 61.2: `BLU`-Visible And Transport-Visible Paper-14 Components

Split the Paper-14 component set as

```math
\mathfrak I_{14}
=
\mathfrak I_{14}^{BLU}
\sqcup
\mathfrak I_{14}^{tr}
```

with

```math
\mathfrak I_{14}^{BLU}
:=
\{ID,proj\},
```

and

```math
\mathfrak I_{14}^{tr}
:=
\{CE,tail,chart,ct,vol,cov,RP\}.
```

The `BLU`-visible components are those whose only remaining obstruction is
whether the active finite projected identities determine the common battery
law with vanishing projection defect. The transport-visible components require
additional coefficient, representation-tail, chart, counterterm, volume,
covariance, or reflection-positivity estimates. They are not zeroed by `BLU`
alone.

For a set \(Z\subseteq\mathfrak I_{14}^{BLU}\), define the reduced Paper-14
carry

```math
E_{14}^{red,Z,SEL2}
:=
\limsup_j
\sum_{i\in\mathfrak I_{14}\setminus Z}
\alpha_i e_{i,j}^{SEL2}.
```

### Definition 61.3: Common `BLU` Bypass Gate

The gate

```math
\mathrm{P21\text{-}E14X13\text{-}COMBLU}(Z)
```

holds when the following same-record conditions are proved on
\(\mathcal B_{61,j}^{SEL2}\).

1. **Projected identity ledger.** There is a finite ledger
   \(\mathfrak I_{61,j}\) built from Paper-14 projected
   Schwinger-Dyson/loop identities, normalization, centrality, covariance
   identities internal to the battery, and reflection-positivity inequalities
   internal to the battery.
2. **Vanishing defect.** The cutoff row satisfies

   ```math
   \max_{\mathfrak I\in\mathfrak I_{61,j}}
   |\mathfrak I(\Gamma_j^{SEL2})|
   \le \delta_{61,j},
   \qquad
   \delta_{61,j}\to0.
   ```

3. **Determining property.** Every two normalized positive gauge-invariant
   states on \(\mathcal B_{61,j}^{SEL2}\) satisfying the zero-defect ledger
   have the same values on \(B_{13,j}^{dyn,SEL2}\) and on all Paper-14
   component records in \(Z\).
4. **Projection meaning.** For each \(i\in Z\), the component \(e_{i,j}^{SEL2}\)
   is exactly the defect controlled by \(\delta_{61,j}\), not a separate
   chart, volume, covariance, reflection, coefficient, or tail transport
   defect.

The maximal bypass gate is

```math
\mathrm{P21\text{-}E14X13\text{-}COMBLU}^{max}
:=
\mathrm{P21\text{-}E14X13\text{-}COMBLU}(\{ID,proj\}).
```

### Lemma 61.4: Common `BLU` Zeros \(X_{13}\)

If `P21-E14X13-COMBLU(Z)` holds for any
\(Z\subseteq\mathfrak I_{14}^{BLU}\), then

```math
\mathrm{P21\text{-}X13\text{-}ROWBC}
```

holds, and therefore

```math
X_{13}^{(26),SEL2}=0.
```

Proof.

The common battery contains \(B_{13,j}^{dyn,SEL2}\). By Definition 61.3, the
zero-defect ledger determines all values on this dynamic battery. Paper 13
Theorem 7.30AN says that a determining finite-block identity ledger with
vanishing defect proves `BLU`; Paper 13 Theorem 7.30AC identifies `BLU` with
`BC` on the fixed finite target. Applying this row by row gives
`P21-X13-ROWBC`. The diagonal implication is Lemma 25.2, and the resulting
zero conclusion is Theorem 26.4. `square`

### Lemma 61.5: Common `BLU` Reduces The Paper-14 Carry

If `P21-E14X13-COMBLU(Z)` holds, then the Paper-14 parked term may be replaced
by

```math
E_{14}^{red,Z,SEL2}.
```

In particular, under the maximal gate,

```math
E_{14}^{park}
\rightsquigarrow
E_{14}^{red,\{ID,proj\},SEL2}
```

where

```math
E_{14}^{red,\{ID,proj\},SEL2}
=
\limsup_j
\sum_{i\in\{CE,tail,chart,ct,vol,cov,RP\}}
\alpha_i e_{i,j}^{SEL2}.
```

Proof.

For \(i\in Z\), Definition 61.3 identifies \(e_{i,j}^{SEL2}\) with a
zero-defect consequence of the common determining ledger. Hence
\(e_{i,j}^{SEL2}\to0\) for \(i\in Z\). Removing cofinally vanishing
nonnegative terms from the Paper-14 component sum gives the displayed reduced
limsup. The transport-visible components remain because Definition 61.2 does
not classify them as `BLU` consequences. `square`

### Theorem 61.6: Common Bypass Envelope

Assume `P21-E14X13-COMBLU(Z)`. Then the Section-60 non-corner envelope may be
replaced by

```math
\mathcal R_{noncorn}^{61,Z,SEL2}(s)
:=
E_{14}^{red,Z,SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

The associated surplus is

```math
\Phi_{61}^{Z,SEL2}(s)
:=
S_{NC}(s)-\mathcal R_{noncorn}^{61,Z,SEL2}(s).
```

On the maximal common-`BLU` branch this becomes

```math
\mathcal R_{noncorn}^{61,max,SEL2}(s)
:=
E_{14}^{red,\{ID,proj\},SEL2}
+U_{12}^{(27),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

Proof.

Lemma 61.4 removes \(X_{13}^{(26),SEL2}\). Lemma 61.5 replaces
\(E_{14}^{park}\) by the reduced Paper-14 carry. The other three terms in
Definition 60.1 are disjoint: \(U_{12}^{(27),SEL2}\) is a Paper-12
loop-readout tail, \(U_{11}^{RPCov,car,SEL2}\) is a Paper-16
RP/covariance moving-row tail, and \(U_{13}^{RPF,bd}\) is an exact-entry
residual-factorization term. Substitution gives the displayed envelope.
`square`

### Lemma 61.7: Current Papers Do Not Yet Prove The Common Gate

The current corpus does not prove

```math
\mathrm{P21\text{-}E14X13\text{-}COMBLU}^{max}.
```

Proof.

Paper 13 proves the implication from a determining finite-block identity
ledger to `BLU`. Paper 14 proves the exact compact-group
Schwinger-Dyson identity before projection and defines projected identity
ledgers. But Paper 14 Honest Boundary 12.5 leaves three constructive estimates
open: off-battery projection defects must vanish, the projected identities
must be compatible across enlargements, and the limiting identities must
determine the battery moments. Paper 14 Theorem 17.2 gives a triangular
closure route to the determining property, but Honest Boundary 17.4 states
that triangular closure itself is a structural fact still to be proved or
falsified for the declared finite loop identity system.

Therefore the common gate is a precise proof target, not an imported theorem.
`square`

### Definition 61.8: Rootwise Triangular Test For The Common Gate

To decide the common gate, form the ordered moment vector

```math
x_{61,j}
=
(x_\alpha)_{\alpha\in A_{61,j}}
```

for all monomials in \(\mathcal B_{61,j}^{SEL2}\) up to the declared degree and
representation cutoff. Let the projected identity basis be written as

```math
M_{61,j}x_{61,j}
=
b_{61,j}+R_{61,j}(x_{61,j})
+\varepsilon_{61,j}.
```

The rootwise triangular test asserts that, after ordering by degree, total
Casimir, support diameter, and reflection depth:

```math
|\operatorname{diag}_\alpha(M_{61,j})|
\ge \kappa_{61,j}>0,
\qquad
\operatorname{Lip}_{tri}(R_{61,j})
\le r_{61,j}<\kappa_{61,j},
```

and

```math
{\|\varepsilon_{61,j}\|\over \kappa_{61,j}-r_{61,j}}
\to0.
```

If the test fails because \(M_{61,j}\) has an uncovered kernel direction, the
kernel direction must be either fixed by positivity, centrality, covariance,
or reflection positivity, or added as a new forced record. If neither is
possible, the common `BLU` bypass fails on that row family.

### Theorem 61.9: Rootwise Triangular Test Proves The Bypass

If the rootwise triangular test of Definition 61.8 holds cofinally and the
identified `BLU`-visible Paper-14 components are precisely
\(Z\subseteq\{ID,proj\}\), then

```math
\mathrm{P21\text{-}E14X13\text{-}COMBLU}(Z)
```

holds.

Proof.

The strict triangular gap
\(\kappa_{61,j}-r_{61,j}>0\) makes the finite projected moment system
uniquely solvable, up to an error bounded by
\(\|\varepsilon_{61,j}\|/(\kappa_{61,j}-r_{61,j})\). The displayed ratio tends
to zero, so any two subsequential row limits agree on the common dynamic
battery and on the certified \(Z\)-component records. This is exactly the
determining property and vanishing-defect part of Definition 61.3. The
same-record and projection-meaning clauses are hypotheses of the test. Hence
`P21-E14X13-COMBLU(Z)` holds. `square`

### Corollary 61.10: New Immediate Work Item

The common bypass converts two separate live terms into one finite algebra
test. The next concrete execution step is:

```math
\text{expand } \mathcal B_{61,j}^{SEL2},
\quad
\text{write } M_{61,j},
\quad
\text{test the triangular gap or exhibit a kernel.}
```

If the triangular test passes, \(X_{13}^{(26),SEL2}=0\) and
\(E_{14}^{park}\) is reduced to the transport-visible remainder. If the test
fails with an unavoidable kernel, the common bypass is falsified and Paper 21
must carry \(X_{13}^{(26),SEL2}\) and \(E_{14}^{park}\) separately.

## 62. Executing The First Finite-Algebra Test

Section 61 defined the common bypass. This section runs the first finite
algebra test against Paper 14's forced-record analysis. The outcome is
decisive but not fatal: the literal one-step finite battery does not close.
The correct replacement is an all-depth forced-tower certificate.

### Definition 62.1: Seed, One-Step, And Two-Step Common Batteries

Let

```math
\mathcal B_{61,j}^{(0)}
:=
B_{13,j}^{dyn,SEL2}
\cup
B_{14,j}^{ID/proj,SEL2}
```

be the common seed battery. Let

```math
\mathcal F_{61,j}^{(1)}
```

be the primitive records generated by applying one projected
Schwinger-Dyson/loop identity to records in \(\mathcal B_{61,j}^{(0)}\). These
include exterior one-staple deformations, reflected copies, representation
channels generated by the local action, and finite products up to the declared
degree. Set

```math
\mathcal B_{61,j}^{(1)}
:=
\mathcal B_{61,j}^{(0)}\cup\mathcal F_{61,j}^{(1)}.
```

Similarly, let \(\mathcal F_{61,j}^{(2)}\) be the primitive records generated
by applying one projected identity step to the primitive records in
\(\mathcal F_{61,j}^{(1)}\), and set

```math
\mathcal B_{61,j}^{(2)}
:=
\mathcal B_{61,j}^{(1)}\cup\mathcal F_{61,j}^{(2)}.
```

The Section-61 battery \(\mathcal B_{61,j}^{SEL2}\) is the one-step battery
\(\mathcal B_{61,j}^{(1)}\) unless an all-depth forced tower is explicitly
declared.

### Lemma 62.2: The Seed Battery Forces One-Staple Records

For a four-dimensional local plaquette-containing `SU(N)` cutoff action,
the projected Schwinger-Dyson/loop identities for
\(\mathcal B_{61,j}^{(0)}\) generate exterior one-staple deformation records
in \(\mathcal F_{61,j}^{(1)}\) which are not functions of
\(\mathcal B_{61,j}^{(0)}\).

Proof.

The dynamic exact-entry battery contains Creutz loop records. Paper 14 Lemma
22.3 proves that differentiating a nontrivial Creutz loop record produces
exterior one-staple deformation records whenever the local action has nonzero
adjacent plaquette coefficients. Paper 14 Lemma 22.4 proves that these
exterior one-staple records are not measurable with respect to the original
Creutz-character battery. The same argument applies to
\(\mathcal B_{61,j}^{(0)}\): the additional \(ID/proj\) scalar records do not
contain the exterior link variables used only by the one-staple deformation.
Thus the seed does not close; it forces \(\mathcal F_{61,j}^{(1)}\). `square`

### Lemma 62.3: The One-Step Battery Forces A Second Shell

For the same action class, the projected identities for
\(\mathcal B_{61,j}^{(1)}\) generate two-staple, corner,
rectangle-extension, transverse-sheet, or local action-density records in
\(\mathcal F_{61,j}^{(2)}\) which are not functions of
\(\mathcal B_{61,j}^{(1)}\) in general.

Proof.

Paper 14 Lemma 23.3 proves that differentiating a one-staple loop record
generates the listed second-shell record types and that at least one such
record is not a function of the one-staple battery in a generic
four-dimensional local plaquette-containing action. Since
\(\mathcal B_{61,j}^{(1)}\) contains precisely the one-step forced records
needed by Section 61, the same obstruction appears here. `square`

### Theorem 62.4: The Literal One-Step Test Does Not Prove The Common Bypass

The finite matrix \(M_{61,j}\) associated with the literal one-step battery
\(\mathcal B_{61,j}^{(1)}\) does not satisfy the exact rootwise triangular
test of Definition 61.8 by identities internal to
\(\mathcal B_{61,j}^{(1)}\) alone.

Equivalently,

```math
\mathrm{P21\text{-}E14X13\text{-}COMBLU}^{max}
```

is not proved by the one-step finite algebra test.

Proof.

Lemma 62.3 says that identities applied to one-step records produce
second-shell records not determined by the one-step battery. Therefore the
projected identity system has an off-battery remainder:

```math
M_{61,j}^{(1)}x_{61,j}^{(1)}
=
b_{61,j}^{(1)}
+R_{61,j}^{(1)}(x_{61,j}^{(1)})
+T_{61,j}^{(>1)}
+\varepsilon_{61,j}^{(1)},
```

where \(T_{61,j}^{(>1)}\) is the contribution of records in shells beyond the
one-step battery. Unless \(T_{61,j}^{(>1)}\) is proved to vanish or is absorbed
by enlarging the battery, the equation is not a closed triangular system on
\(\mathcal B_{61,j}^{(1)}\). Thus the one-step finite algebra test does not
prove Definition 61.8. `square`

### Definition 62.5: All-Depth Common Forced Tower

Define inductively

```math
\mathcal B_{61,j}^{(K)}
:=
\mathcal B_{61,j}^{(K-1)}
\cup
\mathcal F_{61,j}^{(K)},
\qquad K\ge1,
```

where \(\mathcal F_{61,j}^{(K)}\) is the finite primitive shell first generated
by applying one projected Schwinger-Dyson/loop identity step to
\(\mathcal B_{61,j}^{(K-1)}\). Let

```math
\mathcal B_{61,j}^{(\infty)}
:=
\bigcup_{K\ge0}\mathcal B_{61,j}^{(K)}.
```

For each shell \(K\), let \(N_{61,K,j}\) be the number of primitive shell
records and \(A_{61,K,j}\) be the canonical forced weight, defined as the
maximum of the projection, connected-cumulant, and transport tail norms with
the largest absolute identity coefficient included. The all-depth forced-tail
budget is

```math
\Theta_{61,j}(K)
:=
\sum_{\ell>K}N_{61,\ell,j}A_{61,\ell,j}.
```

### Definition 62.6: Common Forced-Tail Summability Gate

The gate

```math
\mathrm{P21\text{-}E14X13\text{-}FTS}
```

holds if there is a cofinal depth schedule \(K(j)\to\infty\) such that

```math
\Theta_{61,j}(K(j))\to0
```

and the projected identity defects on \(\mathcal B_{61,j}^{(K(j))}\) satisfy

```math
\operatorname{Def}_{proj,61,j}(K(j))\to0.
```

This is the common-battery version of Paper 14's forced-tail summability
target. It is a statement about records in one pushed-forward law, not about
hidden subprocesses.

### Definition 62.7: Common Shell-Invertibility Gate

The gate

```math
\mathrm{P21\text{-}E14X13\text{-}SIC}
```

holds if every shell \(1\le K\le K(j)\) satisfies a constrained shell
invertibility certificate:

```math
\operatorname{Ker}_{phys}(M_{61,K,j})=0,
```

and there are right inverses \(Q_{61,K,j}\) and nonlinear shell Lipschitz
constants \(r_{61,K,j}\) such that

```math
\|Q_{61,K,j}\|\,r_{61,K,j}<1
```

uniformly on the cofinal schedule. The physical kernel quotients by directions
fixed by normalization, centrality, conjugation, internal covariance,
reflection positivity, positivity, and declared sector labels.

### Theorem 62.8: Forced-Tower Certificate Proves The Common Bypass

Assume:

```math
\mathrm{P21\text{-}E14X13\text{-}FTS},
\qquad
\mathrm{P21\text{-}E14X13\text{-}SIC},
```

and assume the same-record projection-meaning clause of Definition 61.3 for
\(Z\subseteq\{ID,proj\}\). Then

```math
\mathrm{P21\text{-}E14X13\text{-}COMBLU}(Z)
```

holds.

Proof.

The forced-tail gate makes every shell beyond \(K(j)\) invisible in the
cofinal row limit, and it also makes the projected identity defects vanish.
The shell-invertibility gate determines each retained shell recursively from
lower shells, because the physical kernel is zero and the nonlinear remainder
is a contraction after applying the shell right inverse. Thus any two
subsequential limits satisfying the projected identities agree on every
record in \(\mathcal B_{61,j}^{(K(j))}\), up to an error tending to zero.
The forced tail then removes the dependence on the truncation depth. Hence
the common identity ledger determines \(B_{13,j}^{dyn,SEL2}\) and the
certified \(Z\)-component Paper-14 records. This is precisely
`P21-E14X13-COMBLU(Z)`. `square`

### Lemma 62.9: The Current Corpus Does Not Prove The Forced-Tower Certificate

The current Papers 13, 14, 20, and 21 do not prove the conjunction

```math
\mathrm{P21\text{-}E14X13\text{-}FTS}
\quad+\quad
\mathrm{P21\text{-}E14X13\text{-}SIC}
```

on the active `SEL2` row.

Proof.

Paper 14 proves the forced-record growth mechanism and gives sufficient
routes to forced-tail summability: forced-collar decay, KP forced-polymer
control, collar-factorizing clustering, or an area-law forced-detour bound.
It explicitly does not prove any of these for actual four-dimensional
`SU(N)`. The area-law route is forbidden here because it would import the
confinement conclusion. The KP/clustering routes remain legitimate but have
not been proved on the same active `SEL2` pushed-forward law.

Paper 14 also defines shell invertibility and physical kernels, but it does
not prove that every shell in the common \(E_{14}/X_{13}\) forced tower has
zero physical kernel. Therefore neither `FTS` nor `SIC` is currently
available as a theorem. `square`

### Corollary 62.10: Finite-Algebra Test Verdict

The finite algebra test has settled the following.

1. The one-step common battery does not close exactly.
2. The common bypass is not falsified; it is upgraded to the forced-tower
   certificate

   ```math
   \mathrm{P21\text{-}E14X13\text{-}FTS}
   +
   \mathrm{P21\text{-}E14X13\text{-}SIC}.
   ```

3. Until that certificate is proved, the Section-60 live terms remain

   ```math
   E_{14}^{park},
   \qquad
   X_{13}^{(26),SEL2}.
   ```

The next rigorous alternatives are therefore:

```math
\text{prove same-record KP/collar forced-tail decay and shell invertibility,}
```

or carry the two terms separately and continue with the other live debits.

## 63. Forced-Tail Feasibility Worksheet

Section 62 reduces the common \(E_{14}/X_{13}\) bypass to two gates:
forced-tail summability and shell invertibility. This section evaluates the
forced-tail side. The conclusion is sharp: finite local geometry supplies the
branching part, but the required decay is a new same-record dynamical source.

### Definition 63.1: Common Forced-Tail Scalar Data

For the common tower \(\mathcal B_{61,j}^{(K)}\), define scalar data

```math
\mathfrak W_{61}^{FTS}
:=
(N_0^{61},C_{geom}^{61},C_c^{61},g_c^{61},C_F^{61},m_F^{61}).
```

They mean:

```math
N_{61,K,j}\le N_0^{61}(C_{geom}^{61})^K,
```

```math
|c_f|\le C_c^{61}e^{g_c^{61}K}
\quad\text{for every primitive shell coefficient }c_f,
```

and

```math
a(f)\le C_F^{61}e^{-m_F^{61}K}
\quad\text{for every primitive }f\in\mathcal F_{61,j}^{(K)}.
```

Here \(a(f)\) is the maximum of the projection, connected-cumulant, and
transport tail norms, as in Paper 14 Definition 25.5.

The scalar pass inequality is

```math
m_F^{61}>g_c^{61}+\log C_{geom}^{61}.
```

### Lemma 63.2: The Deterministic Growth Side Is Available Under Finite-Stencil Data

Assume the active row has:

1. a finite plaquette-collar action range \(r_A\);
2. a finite local action stencil;
3. a finite representation-action channel list after the declared row cutoff;
4. a finite coefficient-growth bound
   \(|c_f|\le C_c^{61}e^{g_c^{61}K}\).

Then there are finite constants \(N_0^{61}\) and \(C_{geom}^{61}\) such that

```math
N_{61,K,j}\le N_0^{61}(C_{geom}^{61})^K
```

cofinally.

Proof.

Paper 14 Theorem 23.7 proves the one-step locality-growth bound: one
Schwinger-Dyson/loop differentiation expands depth, length, staple number,
and representation weight by bounded amounts and generates at most
\(C_{geom}(4,r_A,A_{stencil})\) primitive records. Paper 14 Theorem 24.3
iterates this to give \(N_K\le N_0C_{geom}^K\). The active common tower is a
subtower of the same forced-record construction, enlarged only by the finite
dynamic \(X_{13}\) and \(ID/proj\) seed records; this changes \(N_0\), not the
exponential branching rate. The coefficient-growth hypothesis supplies
\(C_c^{61},g_c^{61}\). `square`

### Lemma 63.3: The Scalar Pass Inequality Proves Common `FTS`

Assume the scalar data of Definition 63.1 exist and satisfy

```math
m_F^{61}>g_c^{61}+\log C_{geom}^{61}.
```

Then

```math
\mathrm{P21\text{-}E14X13\text{-}FTS}
```

holds.

Proof.

For shell \(K\),

```math
N_{61,K,j}A_{61,K,j}
\le
N_0^{61}C_F^{61}C_c^{61}
\exp[-(m_F^{61}-g_c^{61}-\log C_{geom}^{61})K].
```

The exponent is negative by hypothesis. Therefore
\(\sum_KN_{61,K,j}A_{61,K,j}\) converges uniformly along the cofinal row, and
the tail after \(K(j)\to\infty\) tends to zero. This is exactly Definition
62.6. `square`

### Definition 63.4: Allowed Same-Record Decay Sources

The decay constant \(m_F^{61}\) may be sourced only by one of the following
same-record estimates.

1. **KP forced-polymer decay:**

   ```math
   \sum_{\gamma\ touching\ f}|z_\gamma|e^{\alpha|\gamma|}
   \le C_{KP}e^{-\mu_{KP}K},
   \qquad
   \mu_{KP}>g_c^{61}+\log C_{geom}^{61}.
   ```

2. **Collar-factorizing clustering:**

   ```math
   f=f_{near}f_{far}+r_f,
   \qquad
   \|r_f\|_{tail}\le C_re^{-m_rK},
   ```

   and

   ```math
   |\kappa(f_{far};G_1,\ldots,G_s)|
   \le C_{cl}e^{-M c_dK},
   ```

   with

   ```math
   \min(m_r,Mc_d)>g_c^{61}+\log C_{geom}^{61}.
   ```

3. **A direct projection-tail theorem:**

   ```math
   \operatorname{Tail}_{proj}(f)
   +\operatorname{Tail}_{conn}(f)
   +\operatorname{Tail}_{tr}(f)
   \le C_Fe^{-m_FK}
   ```

   with the same scalar pass inequality.

The area-law forced-detour route from Paper 14 is not admissible in Paper 21:
it would import the confinement conclusion being tested.

### Lemma 63.5: Distance Clustering Alone Is Not Enough

Ordinary exponential clustering in physical distance from the original Creutz
sheet does not by itself prove Definition 63.4.

Proof.

Forced depth \(K\) counts identity-generation depth, not necessarily physical
separation from the original sheet. Forced records can retract, run along the
same finite collar, form corners, or generate local action-density insertions
whose support remains at bounded collar distance for several forced steps.
For such records, a bound of the form \(e^{-M\,dist}\) need not decay as
\(e^{-mK}\). Paper 14 therefore uses collar-factorizing clustering rather than
ordinary two-point clustering: the newly forced part must be separated after
removing the already-declared near factor, and the remainder must have its own
tail bound. `square`

### Theorem 63.6: Forced-Tail Feasibility Verdict

The current corpus proves the deterministic growth half of the forced-tail
worksheet under finite-stencil and finite-channel row data. It does not prove
the decay half

```math
a(f)\le C_F^{61}e^{-m_F^{61}K}
```

with

```math
m_F^{61}>g_c^{61}+\log C_{geom}^{61}
```

on the active `SEL2` same-record law.

Therefore

```math
\mathrm{P21\text{-}E14X13\text{-}FTS}
```

is not closed by Sections 61--63. It is parked as the explicit source gate

```math
\mathrm{P21\text{-}E14X13\text{-}FTS\text{-}SRC}
(C_F^{61},m_F^{61})
```

with the scalar requirement above.

Proof.

Lemma 63.2 imports Paper 14's finite local growth theorem. Lemma 63.3 proves
the scalar sufficiency. Definition 63.4 lists the only admissible non-area-law
decay sources. Papers 13, 14, 20, and the preceding sections of Paper 21 do
not prove any of those sources for the common forced tower on the active
`SEL2` law. The area-law route is explicitly excluded. Hence the forced-tail
gate is a named source obstruction, not a proved theorem. `square`

## 64. First Shell-Invertibility Audit

The second half of the common bypass is shell invertibility. This section runs
the first-shell audit far enough to decide what the current corpus can and
cannot prove.

### Definition 64.1: First-Shell Moment Vector

Let \(\mathcal F_{61,j}^{(1)}\) be the one-staple shell. Define

```math
x_{61,1,j}
:=
\left(
\int m\,d\nu
\right)_{m\in Mon(\mathcal F_{61,j}^{(1)};\mathcal B_{61,j}^{(0)},D,\Lambda_*)},
```

where the monomials contain at least one primitive one-staple record, any
number of seed records, total degree at most \(D\), and representation labels
inside the active cutoff \(\Lambda_*\).

The projected shell identity system is

```math
M_{61,1,j}x_{61,1,j}
=
b_{61,1,j}(x_{61,<1,j})
+R_{61,1,j}(x_{61,1,j},x_{61,<1,j})
+\tau_{61,1,j}.
```

### Definition 64.2: First-Shell Kernel Tests

The first-shell invertibility audit consists of four tests.

1. **Raw kernel:** compute \(\ker M_{61,1,j}\).
2. **Symmetry quotient:** quotient by centrality, conjugation, and internal
   lattice covariance directions.
3. **Reflection/positivity quotient:** remove directions forced by
   reflection-positivity inequalities, positivity, normalization, and
   declared sector labels.
4. **Contraction gap:** prove a right inverse \(Q_{61,1,j}\) and a nonlinear
   Lipschitz constant \(r_{61,1,j}\) with

   ```math
   \|Q_{61,1,j}\|r_{61,1,j}<1.
   ```

If all four pass cofinally, shell \(1\) satisfies the common `SIC` condition.

### Lemma 64.3: Shell One Is Not Decided By Forced-Record Generation Alone

The fact that \(\mathcal B_{61,j}^{(0)}\) forces
\(\mathcal F_{61,j}^{(1)}\) does not decide whether shell \(1\) is invertible.

Proof.

Forced-record generation shows that the seed battery is incomplete. After the
one-staple records are added, the shell-one identities may or may not
determine their moments. Paper 14 separates these questions: forced-tail
summability controls off-shell tails, while shell invertibility is the
condition \(\operatorname{Ker}_{phys}(M_k)=0\) plus a contraction gap. The
existence of shell \(2\) records proves that the one-step battery is not a
complete exact closure, but it does not prove that shell \(1\) has a physical
kernel. `square`

### Lemma 64.4: Current Corpus Does Not Prove First-Shell `SIC`

The current corpus does not prove

```math
\operatorname{Ker}_{phys}(M_{61,1,j})=0,
\qquad
\|Q_{61,1,j}\|r_{61,1,j}<1
```

cofinally on the active `SEL2` row.

Proof.

Paper 14 defines shell kernels, physical kernels, and the shell
invertibility certificate. It does not compute the first-shell matrix
\(M_{61,1,j}\) for the active common \(E_{14}/X_{13}\) battery, nor does it
prove that centrality, covariance, reflection positivity, positivity, and
sector labels remove every kernel direction. It also does not provide a
cofinal right-inverse norm or nonlinear Lipschitz gap for this battery.
Papers 20 and 21 close coefficient and decoration subledgers, but those
subledgers do not compute \(M_{61,1,j}\). Hence first-shell `SIC` is open.
`square`

### Definition 64.5: First-Shell Failure-Or-Certificate Ledger

The next concrete shell-invertibility work item is the finite linear-algebra
ledger

```math
\mathcal K_{61,1}
:=
(
M_{61,1,j},
\ker M_{61,1,j},
\ker_{phys}M_{61,1,j},
Q_{61,1,j},
r_{61,1,j}
).
```

It has three possible outcomes:

1. `SIC1-pass`: \(\ker_{phys}M_{61,1,j}=0\) and
   \(\|Q_{61,1,j}\|r_{61,1,j}<1\).
2. `SIC1-enlarge`: a kernel direction is a genuine new operational record or
   sector label; enlarge the shell ledger and rerun.
3. `SIC1-fail`: a nonzero physical kernel remains and cannot be removed by
   record enlargement without changing the target battery. Then the common
   bypass fails.

### Theorem 64.6: Shell-Invertibility Verdict

At the current source level,

```math
\mathrm{P21\text{-}E14X13\text{-}SIC}
```

is not proved and not falsified. It is reduced to the explicit finite
first-shell ledger \(\mathcal K_{61,1}\) plus the corresponding all-shell
extension.

Proof.

Lemma 64.4 proves that shell one is not currently certified. Lemma 64.3
prevents a false negative: forced growth alone is not a physical-kernel
falsification. Therefore the correct status is an explicit finite
linear-algebra source gate. The all-shell `SIC` gate cannot be proved until
shell one and all later shells satisfy the same certificate, and cannot be
falsified until a non-removable physical kernel is exhibited. `square`

## 65. Common Bypass Decision After Steps 1--5

We can now settle the common bypass as far as the current corpus allows.

### Theorem 65.1: Common \(E_{14}/X_{13}\) Bypass Is Parked

The common bypass is currently neither proved nor falsified. The precise
parked gate is

```math
\mathrm{P21\text{-}E14X13\text{-}FTS\text{-}SRC}
(C_F^{61},m_F^{61})
\quad+\quad
\mathcal K_{61,1}
\quad+\quad
\mathrm{P21\text{-}E14X13\text{-}SIC}_{K\ge2}.
```

Until this gate is supplied, the Section-60 live terms remain:

```math
E_{14}^{park},
\qquad
X_{13}^{(26),SEL2}.
```

Proof.

Section 62 proves that the one-step finite algebra test does not close the
common bypass. Section 63 proves that the forced-tail gate reduces to an
explicit scalar decay inequality and that the required non-area-law decay
source is not proved. Section 64 proves that first-shell invertibility is not
certified and not falsified. Thus the common bypass has a precise parked
source gate, but no current theorem closes it. Consequently no envelope update
from Theorem 61.6 is licensed. `square`

### Corollary 65.2: Updated Execution Order

After exhausting the common bypass pass, there are two honest paths.

1. Reopen the parked common gate only if one has:

   ```math
   m_F^{61}>g_c^{61}+\log C_{geom}^{61}
   ```

   from same-record KP/collar decay, and the first-shell matrix ledger
   \(\mathcal K_{61,1}\).

2. Otherwise carry \(E_{14}^{park}\) and \(X_{13}^{(26),SEL2}\) separately and
   continue with the next live debit:

   ```math
   U_{12}^{(27),SEL2}.
   ```

This is not a retreat. It is the end of the common finite-algebra attack at
the present source level.

## 66. Paper-12 Moving-Row Residual Audit For \(U_{12}^{(27),SEL2}\)

Section 65 leaves the common \(E_{14}/X_{13}\) bypass parked. The next live
debit is the reduced Paper-12 residual

```math
U_{12}^{(27),SEL2}=U_{12}^{P12,SEL2}.
```

Earlier sections already zeroed the perimeter, cusp, smearing,
loop-representative, and scalar-binning pieces on the strict exact
scalar-record branch. This section decides the remaining Paper-12 residual
tail.

### Definition 66.1: Strict Paper-12 Row Package

The strict Paper-12 row package

```math
\mathrm{P21\text{-}T12\text{-}P12\text{-}FIXROW}
```

holds when, for every active row \(j\):

1. the four Creutz loops of Definition 12.1 are nondegenerate embedded
   rectangles, with right-angle cusps and positive separation between
   nonadjacent arcs;
2. the row battery \(B_{12,j}^{app,SEL2}\) has finite product degree, finite
   representation list, and finite tuple cardinality;
3. the active records are exact renormalized unsmeared scalar Wilson-loop
   records;
4. the same real nonzero perimeter/cusp calibration branches used in Sections
   12--14 are used in the Paper-12 residual calculation;
5. the Paper-12 local connected-polymer criterion applies to the row, giving
   nonnegative residual bounds

   ```math
   b_{P12,j,k}^{SEL2}
   =
   \theta_{P12,j,k}^{tail,SEL2}
   +
   \theta_{P12,j,k}^{conn,SEL2}
   ```

   with fixed-row tail convergence

   ```math
   R_{P12,j}(K)
   :=
   \sum_{k\ge K}b_{P12,j,k}^{SEL2}
   \to0
   \qquad(K\to\infty).
   ```

This package uses only Paper-12 loop-readout data. It does not assert a
block-plaquette coefficient estimate, an area law, a mass gap, or the
`SEL2` tree-rate gate.

### Lemma 66.2: Paper 12 Supplies The Fixed-Row Package On Strict Rows

On the strict no-corner exact scalar-record branch, the current Paper-12
imports prove `P21-T12-P12-FIXROW`, provided the finite Paper-11 AF hypotheses
used in Paper 12 Lemmas 3.6B--3.6C hold for each row battery.

Proof.

Lemma 27.2 already proves that each strict row battery is a finite admissible
Paper-12 loop battery: the active records are scalar closed Wilson-loop
records on nondegenerate rectangles with four right-angle cusps and positive
separation between nonadjacent arcs. Paper 12 Lemma 3.6B identifies the only
UV singular loop contributions on such finite admissible batteries as the
declared perimeter and cusp terms, and bounds the remaining connected
clusters by the Paper-11 AF residual tail. Paper 12 Lemma 3.6C converts this
into the local connected-polymer criterion. Paper 12 Theorem 3.7 then gives
the finite cumulant envelope and product-boundedness.

For a fixed row \(j\), those estimates give a summable residual series after
the finite row modulus is extracted. Its tail is exactly
\(R_{P12,j}(K)\), and tails of a convergent nonnegative series tend to zero.
Thus Definition 66.1 holds row by row. `square`

### Definition 66.3: Paper-12 Cofinal Reselection Audit

The cofinal reselection audit

```math
\mathrm{P21\text{-}T12\text{-}P12\text{-}COFSEL}
```

allows replacing the active cofinal index by a further cofinal subsequence
only if:

1. the pushed-forward law remains the same law restricted to the new cofinal
   row;
2. every earlier proved zero remains zero on subsequences;
3. every earlier carried limsup upper bound is not increased;
4. no lower-floor falsification is being discarded;
5. the reselection rule depends only on the Paper-12 residual tail bounds
   \(R_{P12,j}(K)\), not on an area-law, mass-gap, or confinement observable.

This is a no-smuggling audit for diagonalizing the loop-readout residual.

### Lemma 66.4: The Paper-12 Diagonal Reselection Is Harmless

Assume `P21-T12-P12-FIXROW`. Then `P21-T12-P12-COFSEL` holds for the
Paper-12 residual tail.

Proof.

For each row \(j\), fixed-row convergence gives a threshold \(K_j\) such that

```math
R_{P12,j}(K_j)<2^{-j}.
```

Choose a further cofinal row index \(n(j)\) with \(n(j)\ge K_j\) and
\(n(j)>n(j-1)\). This uses only the Paper-12 residual bounds, which are
operational loop-readout estimates on the same pushed-forward law. Passing to
a cofinal subsequence preserves cofinal zero statements and cannot increase
any limsup upper debit. It also does not erase a proved positive lower floor:
no lower-floor falsification for \(U_{12}^{P12}\) has been proved in the
current text. Thus the reselection satisfies Definition 66.3. `square`

### Theorem 66.5: The Paper-12 Residual Tail Vanishes On The Diagonal Branch

Assume:

```math
\mathrm{P21\text{-}T12\text{-}P12\text{-}FIXROW},
\qquad
\mathrm{P21\text{-}T12\text{-}P12\text{-}COFSEL}.
```

Then

```math
\mathrm{P21\text{-}T12\text{-}P12\text{-}DIAG0}
```

holds and hence

```math
U_{12}^{(27),SEL2}=U_{12}^{P12,SEL2}=0.
```

Proof.

After the cofinal reselection of Lemma 66.4,

```math
\sum_{k\ge j}b_{P12,j,k}^{SEL2}
\le
R_{P12,j}(K_j)
<2^{-j}
\to0.
```

This is exactly `P21-T12-P12-DIAG0`. Theorem 27.4 then gives
\(U_{12}^{P12,SEL2}=0\). Since Section 27 identifies
\(U_{12}^{(27),SEL2}\) with \(U_{12}^{P12,SEL2}\) on the strict branch, the
displayed zero follows. `square`

### Definition 66.6: Non-Diagonal Carry Fallback

If the cofinal diagonal branch is not used, define the finite carry

```math
U_{12}^{P12,bd,SEL2}
:=
\limsup_j R_{P12,j}(j)
```

whenever this limsup is finite. The fallback gate

```math
\mathrm{P21\text{-}T12\text{-}P12\text{-}CARRY}
(U_{12}^{P12,bd,SEL2})
```

asserts that

```math
U_{12}^{P12,bd,SEL2}<\infty.
```

If this gate holds, then

```math
U_{12}^{(27),SEL2}
\le
U_{12}^{P12,bd,SEL2}.
```

### Theorem 66.7: \(U_{12}^{(27),SEL2}\) Decision

On the strict exact scalar-record branch, the Paper-12 residual has the
following complete decision.

1. If the fixed-row Paper-12 source and cofinal reselection audit hold, then

   ```math
   U_{12}^{(27),SEL2}=0.
   ```

2. If cofinal reselection is not used but
   `P21-T12-P12-CARRY(U_{12}^{P12,bd,SEL2})` holds, then

   ```math
   U_{12}^{(27),SEL2}
   \le
   U_{12}^{P12,bd,SEL2}.
   ```

3. If neither branch holds, the non-corner worksheet is not certified.

Proof.

Clause 1 is Theorem 66.5. Clause 2 is Definition 66.6 and Theorem 27.4 clause
2. Clause 3 is the finite-debit requirement: every term in the carried
worksheet must be either zeroed or bounded by a finite same-record scalar.
`square`

### Corollary 66.8: Updated Non-Corner Envelope

On the strict Paper-12 diagonal branch, the Section-60 envelope reduces to

```math
\mathcal R_{noncorn}^{66,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

The associated surplus is

```math
\Phi_{66}^{SEL2}(s)
:=
S_{NC}(s)-\mathcal R_{noncorn}^{66,SEL2}(s).
```

If the fallback branch is used instead, replace the right-hand side by

```math
\mathcal R_{noncorn}^{66,carry,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{12}^{P12,bd,SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

Thus \(U_{12}^{(27),SEL2}\) is no longer an irreducible obstruction on the
strict diagonal Paper-12 branch. The remaining live debits are
\(E_{14}^{park}\), \(X_{13}^{(26),SEL2}\),
\(U_{11}^{RPCov,car,SEL2}\), and \(U_{13}^{RPF,bd}\).

### Corollary 66.9: Alignment With The Earlier \(U_{11}^{RPCov}\) Decision

After the Paper-12 diagonal branch, the remaining Paper-16 RP/covariance
debit is still

```math
U_{11}^{RPCov,car,SEL2}(s)
=
U_{11}^{RP,bd,SEL2}(s)
+U_{11}^{Cov,bd,SEL2}(s),
```

but this term is not a new Section-66 target. Sections 28--29 isolate its
reduced RP/covariance ledgers, and Theorem 59.2 gives the current decision:
it is carried unless the moving-row Paper-16 diagonal rate data

```math
\sum_{k\ge j}D_{11;j,k}^{RP,red,SEL2}(s)\to0,
\qquad
\sup_g\sum_{k\ge j}D_{11;j,k}^{Cov,red,SEL2}(g;s)\to0
```

are proved on the same `SEL2` scalar law. Therefore Section 66 only removes
the Paper-12 loop-readout residual from the Section-60 envelope. The remaining
execution choices are:

1. supply the missing Paper-16 moving-row RP/covariance rate data;
2. supply the same-record forced-tail and shell-invertibility data for the
   parked common \(E_{14}/X_{13}\) bypass;
3. continue carrying \(U_{11}^{RPCov,car,SEL2}\), \(E_{14}^{park}\), and
   \(X_{13}^{(26),SEL2}\) while attacking the separate tree-rate source gate.

## 67. Five-Step Execution Lock And Source-Data Frontier

Sections 61--66 execute the requested five-step route against the actual
previous papers. This section records the result in a form that prevents
future passes from re-opening already decided bookkeeping slots without new
same-record source data.

### Definition 67.1: The Five-Item State Vector

On the strict raw-time saturated `SEL2` branch, define the post-Section-66
state vector

```math
\mathfrak S_{67}^{SEL2}
:=
\left(
\mathcal G_{E14X13}^{SEL2},
U_{12}^{diag,SEL2},
U_{11}^{RPCov,car,SEL2},
U_{13}^{RPF,bd},
\mathcal T_{raw}^{SEL2}
\right),
```

where:

1. the common finite-battery bypass gate is

   ```math
   \mathcal G_{E14X13}^{SEL2}
   :=
   \mathrm{P21\text{-}E14X13\text{-}FTS\text{-}SRC}
   (C_F^{61},m_F^{61})
   +\mathcal K_{61,1}
   +\mathrm{P21\text{-}E14X13\text{-}SIC}_{K\ge2};
   ```

2. \(U_{12}^{diag,SEL2}=0\) on the strict Paper-12 diagonal branch of
   Theorem 66.5, and otherwise equals the fallback carry
   \(U_{12}^{P12,bd,SEL2}\) of Definition 66.6 when that finite ceiling is
   proved;
3. \(U_{11}^{RPCov,car,SEL2}\) is the Paper-16 RP/covariance moving-row carry
   of Theorem 59.2;
4. \(U_{13}^{RPF,bd}\) is the exact-entry residual-factorization carry left by
   Sections 32--33;
5. \(\mathcal T_{raw}^{SEL2}\) is the raw selector-time trichotomy of
   Lemma 54.2. On the active raw-time saturated branch,
   \(s\in\mathcal A_{raw}^{SEL2}(\rho)\), it contributes no additional
   leading coefficient debit.

Every entry in \(\mathfrak S_{67}^{SEL2}\) is evaluated on the same
pushed-forward scalar law. There is no Wilson-loop area-law input, mass-gap
input, or continuum Yang-Mills measure input in this state vector.

### Lemma 67.2: The Common \(E_{14}/X_{13}\) Bypass Is Settled To A Source Gate

The common finite-battery bypass has been pushed as far as the present corpus
allows:

```math
E_{14}^{park}+X_{13}^{(26),SEL2}
\quad\leadsto\quad
\mathcal G_{E14X13}^{SEL2}.
```

More explicitly, the one-step finite algebra test fails as an exact closure
test, and the all-depth tower route is neither proved nor falsified without
\(\mathcal G_{E14X13}^{SEL2}\).

Proof.

Section 61 identifies the common `BLU` source shared by \(E_{14}\) and
\(X_{13}\). Section 62 uses Paper 14 Lemmas 22.3--23.5 to show that the seed
and one-staple batteries force higher shells, so literal one-step closure is
not available. Sections 63 and 64 reduce the all-depth route to forced-tail
summability and shell invertibility. Section 65 states exactly the parked
gate \(\mathcal G_{E14X13}^{SEL2}\). No later section supplies same-record KP
forced-polymer decay, collar-factorizing forced-tail decay, or shell
invertibility data. `square`

### Lemma 67.3: The Finite Algebra Test Cannot Be Executed Numerically From The Current Text Alone

The current text contains the structural finite algebra test, but not the
actual finite matrices needed to decide the shell kernels:

```math
M_{61,K,j},\qquad
\ker M_{61,K,j},\qquad
Q_{61,K,j},\qquad
r_{61,K,j}.
```

Consequently the current corpus cannot honestly assert either

```math
\mathrm{P21\text{-}E14X13\text{-}SIC}
```

or its negation.

Proof.

Paper 14 Sections 22--28 give the forced-record generation rules, branching
estimates, forced-tail norms, and shell-invertibility criteria. They do not
tabulate the actual shell identity matrices for the common `SEL2`
\(E_{14}/X_{13}\) battery. Paper 21 Section 64 accordingly defines the
finite ledger \(\mathcal K_{61,1}\), rather than claiming that its raw kernel,
physical kernel, right inverse, and nonlinear Lipschitz gap have been
computed. Without those finite matrices, declaring shell invertibility would
be a hidden assumption. Declaring failure would also be unjustified, because
a forced second shell proves only that the one-step battery is incomplete,
not that the first shell has a non-removable physical kernel. `square`

### Lemma 67.4: \(U_{12}\) Is Closed Only On The Strict Diagonal Branch

On the strict Paper-12 diagonal branch,

```math
U_{12}^{diag,SEL2}=0.
```

If the branch is changed so that the cofinal Paper-12 diagonal reselection is
not used, the only licensed replacement is

```math
U_{12}^{diag,SEL2}=U_{12}^{P12,bd,SEL2}
```

provided `P21-T12-P12-CARRY` is proved.

Proof.

This is Theorem 66.7. Paper 12 supplies finite-row perimeter/cusp and
loop-readout control for admissible finite loop batteries, but it does not
supply a block-plaquette coefficient theorem, a mass gap, or an area law.
Therefore the zero is exactly a strict diagonal loop-readout zero, not a
general permission to remove other moving-row or coefficient debits.
`square`

### Lemma 67.5: \(U_{11}^{RPCov}\) Must Stay Carried Without Paper-16 Moving-Row Rates

The current corpus licenses only

```math
U_{11}^{RPCov,car,SEL2}(s)
\le
U_{11}^{RP,bd,SEL2}(s)+U_{11}^{Cov,bd,SEL2}(s),
```

unless the Paper-16 moving-row diagonal limits

```math
\sum_{k\ge j}D_{11;j,k}^{RP,red,SEL2}(s)\to0,
\qquad
\sup_g\sum_{k\ge j}D_{11;j,k}^{Cov,red,SEL2}(g;s)\to0
```

are proved on the same active `SEL2` scalar law.

Proof.

Paper 16 Definitions 9W.1C and 9W.1G give the correct RP and covariance
transport ledgers. Those ledgers require summability and vanishing of the
corresponding defects, but they do not by themselves provide the moving-row
rate data for the active `SEL2` schedule. Theorem 59.2 therefore carries the
term. No part of the common \(E_{14}/X_{13}\) bypass, the Paper-12 diagonal
loop-readout zero, or the raw coefficient comparison is an RP/covariance
moving-row theorem. `square`

### Lemma 67.6: Raw Block-Time Is Not The Current Finite-Battery Bottleneck

On the strict five-term, raw-time saturated branch
\(s\in\mathcal A_{raw}^{SEL2}(\rho)\), the leading raw sign/unit/rate debit is
already closed. Outside that branch, the exact alternatives are the
selector-time trichotomy of Lemma 54.2.

Proof.

Sections 47--48 prove the same-record comparison between the actual
four-dimensional `SEL2` scalar coefficient and the finite heat-kernel
convolution tree on `P21-SEL2-STRICT-5TERM`. Sections 50--51 then reduce
raw sign/unit/rate to the scalar inequality
\(s>S_{raw}^{pass}(\rho)\). Section 54 locks the pass, failure, and
straddling alternatives. Therefore raw block-time should not be re-opened as
a finite-battery `BLU` problem. Its only remaining role is through the
already-declared selector-time branch. `square`

### Theorem 67.7: Final Five-Step Execution Verdict

On the active strict Paper-12 diagonal and raw-time saturated branch, the
post-Section-66 non-corner envelope is

```math
\mathcal R_{noncorn}^{67,SEL2}(s)
:=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

The branch passes the non-corner worksheet only if

```math
\Phi_{67}^{SEL2}(s)
:=
S_{NC}(s)-\mathcal R_{noncorn}^{67,SEL2}(s)>0
```

for some admissible

```math
s\in\mathcal A_{raw}^{SEL2}(\rho).
```

At the current source level, Paper 21 proves neither this strict positivity
nor its lower-floor falsification. The honest terminal status of the five
items is

```math
\mathrm{P21\text{-}FIVEITEM\text{-}SOURCE\text{-}FRONTIER}.
```

Proof.

Lemma 67.2 settles items 1--2: the common \(E_{14}/X_{13}\) attack is reduced
to \(\mathcal G_{E14X13}^{SEL2}\), and the present text lacks the finite
matrices and decay data needed to decide it. Lemma 67.4 settles item 3:
\(U_{12}\) is zero only on the strict diagonal branch. Lemma 67.5 settles item
4: \(U_{11}^{RPCov}\) remains carried without Paper-16 moving-row rates.
Lemma 67.6 settles item 5: raw block-time is locked by the scalar
selector-time branch, not by the finite-battery bypass. Substituting the
strict diagonal value \(U_{12}^{diag,SEL2}=0\) into Corollary 66.8 gives the
displayed envelope. No theorem in Papers 10--16, 20, or Sections 61--66 of
this paper supplies all four remaining finite ceilings or lower floors.
`square`

### Corollary 67.8: What Can Actually Move The Paper Now

After the five-step execution lock, progress requires one of the following
new same-record source packages.

1. **Common \(E_{14}/X_{13}\) source data:**

   ```math
   \mathcal G_{E14X13}^{SEL2}.
   ```

   This means non-area-law forced-tail decay plus shell invertibility data.

2. **Paper-16 RP/covariance moving-row data:**

   ```math
   \sum_{k\ge j}D_{11;j,k}^{RP,red,SEL2}\to0,
   \qquad
   \sup_g\sum_{k\ge j}D_{11;j,k}^{Cov,red,SEL2}(g)\to0.
   ```

3. **Exact-entry residual-factorization zero or sharp bound:**

   ```math
   U_{13}^{RPF,bd}=0
   \quad\text{or}\quad
   U_{13}^{RPF,bd}<S_{NC}(s)
   -E_{14}^{park}-X_{13}^{(26),SEL2}
   -U_{11}^{RPCov,car,SEL2}(s).
   ```

4. **A strict surplus certificate or falsifying lower floor** for
   \(\Phi_{67}^{SEL2}\).

Repeating coefficient normalization, Paper-12 loop-readout, or raw
block-time work without changing the branch cannot move the proof: those
ledgers have already been decided on the active branch.

## 68. First-Shell Template Atlas For \(\mathcal K_{61,1}\)

Corollary 67.8 says that the most informative next move is not another
scalar feasibility rerun. It is the finite first-shell algebra test inside
the common \(E_{14}/X_{13}\) bypass. This section builds the executable
template atlas for that test and records what can and cannot be decided from
the current papers.

### Definition 68.1: First-Shell Primitive Labels

Let \(B_{61,j}^{(0)}\) be the common seed battery of Definition 62.1. Its
loop part contains the four Creutz loops \(C_\alpha\) with
\(\alpha\in\{11,21,12,22\}\), the active sheet plaquette character records,
the \(E_{14}\) `ID/proj` scalar records, and the reflected copies already
declared in Sections 61--62.

A first-shell primitive label is a tuple

```math
u=(\alpha,e,p,\lambda,\sigma),
```

where:

1. \(e\) is an oriented link on \(C_\alpha\);
2. \(p\) is an adjacent plaquette sharing \(e\), not already represented as a
   sheet plaquette record in \(B_{61,j}^{(0)}\);
3. \(\lambda\in\Lambda_{\rm act}\) is an action representation channel with
   nonzero local action coefficient;
4. \(\sigma\in\{+,-\}\) records orientation/conjugation.

The corresponding primitive scalar record is the one-staple record

```math
Y_u
:=
W_{\rho\otimes\lambda^\sigma}(C_\alpha\triangleleft_e p)
```

or its paired real-character version when the operational battery stores real
central records. The first shell is

```math
\mathcal F_{61,j}^{(1)}
:=
\{Y_u:u\in\mathcal U_{61,1,j}\},
```

together with reflected copies and finite products up to the declared degree.

### Definition 68.2: Physical Template Orbits

Let \(\mathfrak G_{61,1}\) be the finite groupoid generated by:

1. hypercubic symmetries preserving the \(2\times2\) sheet template and the
   declared test box;
2. the reflections used in the OS-positive battery;
3. conjugation and orientation reversal of paired real records;
4. internal relabelings of representation channels that are declared
   operationally identical by the active cutoff action;
5. endpoint/corner labels that survive the no-corner selector as genuine
   sector labels rather than symmetries.

The physical first-shell orbit set is

```math
\mathcal O_{61,1,j}
:=
\mathcal U_{61,1,j}/\mathfrak G_{61,1}.
```

No quotient is allowed unless it is an equality of scalar records under the
same pushed-forward law or a declared sector identification. In particular,
two different exterior plaquettes are not identified merely because they
look similar in a drawing; the corresponding finite readout law must be
carried by the declared symmetry.

### Definition 68.3: First-Shell Moment Coordinates

For fixed degree cutoff \(D\) and representation cutoff \(\Lambda_*\), define

```math
\mathrm{Mon}_{61,1,j}
:=
\mathrm{Mon}(\mathcal F_{61,j}^{(1)};B_{61,j}^{(0)},D,\Lambda_*),
```

the finite list of monomials containing at least one first-shell primitive
record, any number of seed records, total degree at most \(D\), and
representation labels in \(\Lambda_*\). The first-shell moment vector is

```math
x_{61,1,j}
:=
\left(\int m\,d\nu_{j}^{SEL2}\right)_{m\in\mathrm{Mon}_{61,1,j}},
```

modulo the physical orbit quotient of Definition 68.2. This is the concrete
version of the vector already named in Definition 64.1.

### Definition 68.4: Row Families In The First-Shell Matrix

The template matrix \(M_{61,1,j}^{tpl}\) has the following row families.

1. **Seed Schwinger-Dyson rows.** Differentiating \(C_\alpha\) along a link
   \(e\) gives the staple-sum row

   ```math
   \sum_{p,\lambda,\sigma}
   c_{\lambda,p,\sigma}\,
   \Gamma_{\rho,\lambda,\sigma}^{\mu}\,
   x_{\alpha,e,p,\lambda,\sigma,\mu}
   =
   b_{\alpha,e}(x_{<1})+\tau_{\alpha,e},
   ```

   where \(c_{\lambda,p,\sigma}\) is the local action coefficient and
   \(\Gamma_{\rho,\lambda,\sigma}^{\mu}\) is the compact-group contraction
   coefficient coming from \(\sum_A T_\rho^A\otimes T_\lambda^A\).

2. **One-staple Schwinger-Dyson rows.** Differentiating \(Y_u\) gives
   retraction terms in \(B_{61,j}^{(0)}\), first-shell self terms, and
   second-shell terms:

   ```math
   M_{u}^{self}x_{61,1,j}
   =
   b_u(x_{<1})+\tau_{u}^{(2+)}.
   ```

   The \(\tau_u^{(2+)}\) terms are precisely the \(B_2\)-type records of
   Paper 14 Definition 23.2 and cannot be dropped unless forced-tail
   summability is available.

3. **Centrality and conjugation rows.** These impose the paired real-character
   identities and identify conjugate orientations only when the active record
   convention declares the paired real scalar.

4. **Template covariance rows.** These identify records in the same
   \(\mathfrak G_{61,1}\)-orbit and leave distinct sector labels untouched.

5. **Reflection/positivity rows and inequalities.** Reflection positivity and
   positivity are used only to quotient kernel directions that are actually
   forced by the finite battery inequalities. They are not equations unless
   the relevant inequality is saturated or extremal on the tested shell.

The concrete shell system is

```math
M_{61,1,j}^{tpl}x_{61,1,j}
=
b_{61,1,j}(x_{<1,j})
+R_{61,1,j}(x_{61,1,j},x_{<1,j})
+\tau_{61,1,j}^{(2+)}.
```

### Lemma 68.5: The Template Matrix Is A Finite Same-Record Object

For every finite row \(j\), finite \(D\), and finite \(\Lambda_*\), the atlas
of Definitions 68.1--68.4 defines a finite matrix over the declared scalar
record law.

Proof.

The seed battery is finite. Paper 14 Theorem 23.7 bounds the number of
one-step forced records from any finite local action stencil and finite
action-channel list. Taking finite products up to degree \(D\) and
representation labels in \(\Lambda_*\) preserves finiteness. The row families
are finite because the seed links, adjacent plaquettes, action channels,
reflections, and template symmetries are finite. Every row is an identity or
inequality among expectations of declared scalar records pushed forward from
the same `SEL2` law. `square`

### Lemma 68.6: Seed Rows Determine Only Staple Sums

The seed Schwinger-Dyson rows alone do not determine the first-shell
coordinates unless every nonzero first-shell label in each seed row lies in a
single physical orbit with a fixed nonzero coefficient ratio.

Equivalently, if two labels \(u,u'\) occur in the same seed row with nonzero
coefficients and are not identified in \(\mathcal O_{61,1,j}\), then the
seed-row submatrix has a nonzero raw kernel direction supported on
\(\{u,u'\}\).

Proof.

For a fixed seed row \(r=(\alpha,e)\), the first-shell part is a linear
functional

```math
L_r(x)=\sum_{u\in U_r}a_u x_u,
```

with \(a_u=c_{\lambda,p,\sigma}\Gamma_{\rho,\lambda,\sigma}^{\mu}\). If
\(u\) and \(u'\) are distinct physical orbit labels with \(a_u,a_{u'}\ne0\),
then the vector \(v\) with

```math
v_u=a_{u'},\qquad v_{u'}=-a_u,
```

and all other coordinates zero satisfies \(L_r(v)=0\). Extending by zero on
other seed rows gives a raw kernel direction of the seed-row submatrix unless
another row family removes it. Thus seed identities determine weighted staple
sums, not individual first-shell moments. `square`

### Definition 68.7: Orbit-Collapse And Shell-Row Closure Tests

The first-shell template passes the purely algebraic pretest only if both of
the following hold.

1. **Orbit-collapse test `OC_61,1`:** every seed-row raw kernel direction of
   Lemma 68.6 is removed by a declared physical symmetry, sector quotient, or
   an additional shell row.
2. **Shell-row closure test `SRC_61,1`:** the second-shell tail
   \(\tau_{61,1,j}^{(2+)}\) in Definition 68.4 is controlled by the same
   forced-tail norm used in `P21-E14X13-FTS-SRC`.

If `OC_61,1` fails, the first shell has an unresolved finite algebra kernel.
If `SRC_61,1` fails, the first-shell matrix cannot be evaluated as a closed
system because Paper 14 Lemma 23.3 forces genuine \(B_2\)-type records.

### Lemma 68.8: First-Shell Closure Requires Both Orbit And Tail Data

The first-shell invertibility certificate cannot be proved from seed-row
identities alone, and it cannot be proved from one-staple rows without a
second-shell tail control.

Proof.

The first statement is Lemma 68.6. The second is Paper 14 Lemma 23.3 in the
present notation: differentiating one-staple records produces retractions
but also two-staple, corner, rectangle-extension, transverse-sheet, and local
action-density records. Paper 14 Theorem 23.5 says that \(B_1\) does not
close exactly. Therefore one-staple rows become usable for `SIC(1)` only
after their \(B_2\)-type contribution is placed into a certified tail
\(\tau_{61,1,j}^{(2+)}\). `square`

### Definition 68.9: Minimal Specialization Data For \(\mathcal K_{61,1}\)

To actually compute the first-shell ledger one must supply the finite data

```math
\mathfrak D_{68}
:=
(N,\rho,D,\Lambda_*,
\Lambda_{\rm act},
c_{\lambda,p,\sigma},
\mathfrak G_{61,1},
\Pi_{\rm proj},
\mathcal P_{\rm phys},
C_{\rm tail}^{(2+)},r_{61,1}).
```

Here:

1. \(N,\rho,D,\Lambda_*\) fix the group, representation, monomial degree, and
   finite representation window;
2. \(\Lambda_{\rm act}\) and \(c_{\lambda,p,\sigma}\) fix the actual finite
   cutoff action channels appearing in the shell identities;
3. \(\mathfrak G_{61,1}\) fixes the allowed physical orbit quotient;
4. \(\Pi_{\rm proj}\) fixes the finite projected identity basis;
5. \(\mathcal P_{\rm phys}\) specifies which positivity/reflection/covariance
   constraints remove kernel directions;
6. \(C_{\rm tail}^{(2+)}\) and \(r_{61,1}\) give the second-shell tail and
   nonlinear Lipschitz data needed for the contraction gap.

No item in \(\mathfrak D_{68}\) may be replaced by an area law, mass gap, or
unconstructed continuum Yang-Mills measure.

### Theorem 68.10: First-Shell Audit Verdict

The current corpus proves the finite first-shell atlas and the seed-row
kernel diagnostic, but it does not prove `SIC1-pass` or `SIC1-fail`.

The exact outcome is:

1. If \(\mathfrak D_{68}\) specializes \(M_{61,1,j}^{tpl}\) so that

   ```math
   \ker_{\rm phys}M_{61,1,j}=0,
   \qquad
   \|Q_{61,1,j}\|\,r_{61,1,j}<1,
   ```

   with the \(B_2\)-tail controlled by `P21-E14X13-FTS-SRC`, then shell one
   passes.

2. If the specialized matrix has a nonzero physical kernel not removed by
   \(\mathcal P_{\rm phys}\), then the common bypass either requires a new
   declared sector/record or fails on that branch.

3. Without \(\mathfrak D_{68}\), the shell-one audit is structurally reduced
   but not decided.

Proof.

Lemma 68.5 constructs the finite atlas. Lemma 68.6 proves that seed rows
alone generally leave weighted staple-sum kernels, so shell one cannot be
certified without the additional row families and quotient data. Lemma 68.8
shows that one-staple rows require a certified second-shell tail. Definition
68.9 lists exactly the finite data needed to specialize the template into the
ledger \(\mathcal K_{61,1}\) of Definition 64.5. With those data, the
alternatives are precisely the shell-invertibility alternatives of Paper 14
Definition 28.4 and Proposition 28.8. Without those data, asserting pass or
failure would add hidden information. `square`

### Corollary 68.11: Next Actual Work Item

The next executable task is to instantiate \(\mathfrak D_{68}\) for the
smallest active branch:

```math
\rho=\rho_{\rm fund},
\qquad
\Lambda_{\rm act}=\{\rho_{\rm fund},\bar\rho_{\rm fund}\}
\quad\text{or the actual declared action channel list},
```

with the active \(D\), \(\Lambda_*\), no-corner selector, reflection battery,
and projection basis. Then compute the orbit table and the matrix
\(M_{61,1,j}^{tpl}\). The first concrete output should be one of:

```math
\mathrm{SIC1\text{-}pass},\qquad
\mathrm{SIC1\text{-}enlarge},\qquad
\mathrm{SIC1\text{-}fail}.
```

Until that finite table is supplied, the common \(E_{14}/X_{13}\) bypass
remains parked at \(\mathcal G_{E14X13}^{SEL2}\).

## 69. Minimal Fundamental First-Shell Instantiation

Section 68 left one concrete task: specialize the first-shell template to the
smallest active branch and see whether the finite algebra already decides
`SIC1`. This section performs that specialization as far as the previous
papers justify it. The result is deliberately narrow: the minimal fundamental
branch does not pass by orbit-collapse alone, but it is not falsified without
the one-staple self rows and their \(B_2\)-tail control.

### Definition 69.1: Minimal Fundamental Branch Data

The minimal first-shell branch is

```math
\mathfrak D_{69}^{min}
:=
\left(
N,\rho_{\rm fund},D,\Lambda_*,
\Lambda_{\rm act}^{min},
c_{\lambda,p,\sigma},
\mathfrak G_{61,1}^{min},
\Pi_{\rm proj}^{min},
\mathcal P_{\rm phys}^{min}
\right),
```

where

```math
\Lambda_{\rm act}^{min}
:=
\{\rho_{\rm fund},\bar\rho_{\rm fund}\}
```

unless the active cutoff action declares a smaller nonzero action-channel
list. If the scalar record battery stores paired real characters, the two
fundamental channels are paired into the real central coordinate. If it stores
complex characters, conjugation rows are retained as part of
\(\mathcal P_{\rm phys}^{min}\).

The branch is still subject to the Paper-20 selector discipline: the group,
representation channel, finite row \(j\), cutoff degree \(D\), representation
window \(\Lambda_*\), no-corner selector, and pushed-forward law are fixed
before any estimate is evaluated.

### Definition 69.2: Primitive Geometric Shell Types

Use the \(2\times2\) Creutz sheet \(S_{2\times2}\) from Paper 14. Let
\(C_{22}\) be the outer \(2\times2\) loop and let \(e\) be a boundary link of
\(C_{22}\). Exterior adjacent plaquettes sharing \(e\) split into at least the
following relative types:

1. **Planar exterior staples**

   ```math
   p_{\parallel}\subset \operatorname{span}(S_{2\times2}),
   \qquad
   p_{\parallel}\not\subset S_{2\times2};
   ```

2. **Transverse staples**

   ```math
   p_{\perp}\subset \operatorname{span}(e,\nu),
   \qquad
   \nu\perp \operatorname{span}(S_{2\times2}).
   ```

In four dimensions there is at least one transverse plaquette of this type at
each boundary link of \(C_{22}\). For the usual isotropic plaquette-containing
cutoff action, both the planar exterior and transverse staple coefficients
are nonzero. If a nonstandard active action removes one of these coefficients,
the corresponding row must be recomputed from the actual nonzero
\(c_{\lambda,p,\sigma}\) list; no coefficient may be silently restored by
symmetry.

### Lemma 69.3: Planar And Transverse Staples Are Not The Same Physical Orbit

Under the admissible first-shell groupoid
\(\mathfrak G_{61,1}^{min}\), a planar exterior staple and a transverse
staple attached to the same \(C_{22}\) boundary link are not the same
physical orbit unless the active record law explicitly declares an additional
sector identification that forgets the distinction between tangent and normal
plaquettes.

Proof.

The quotient in Definition 68.2 is generated by symmetries preserving the
declared \(2\times2\) sheet template, OS reflections, conjugation/orientation
reversal, declared channel identifications, and declared sector labels. These
operations preserve the incidence relation

```math
p\subset \operatorname{span}(S_{2\times2})
```

versus

```math
p\not\subset \operatorname{span}(S_{2\times2}).
```

Reflections and transverse rotations may identify transverse staples with
other transverse staples, and planar reflections may identify planar exterior
staples with other planar exterior staples. They do not turn a tangent
plaquette into a normal plaquette while preserving the same sheet-relative
record. Therefore the two relative types remain distinct physical labels
unless the active selector adds a new non-geometric sector quotient. Such a
quotient is not present in the no-corner strict scalar branch. `square`

### Lemma 69.4: The Fundamental Contraction Coefficients Are Nonzero

For `SU(N)` and \(\rho=\rho_{\rm fund}\), the compact-group contraction
coefficients generated by a nonzero fundamental or antifundamental plaquette
action channel are nonzero in at least one generated representation channel.

Proof.

On an irreducible summand \(\mu\subset\rho\otimes\lambda\), the contraction
\(\sum_A T_\rho^A\otimes T_\lambda^A\) acts by the scalar

```math
{1\over2}
\left(
C_2(\mu)-C_2(\rho)-C_2(\lambda)
\right).
```

For \(\lambda=\bar\rho_{\rm fund}\),
\(\rho_{\rm fund}\otimes\bar\rho_{\rm fund}=1\oplus{\rm Ad}\). The scalar is
\(-C_2(\rho_{\rm fund})\) on the singlet and \(1/(2N)\) on the adjoint, so it
is nonzero. For \(\lambda=\rho_{\rm fund}\), the symmetric and antisymmetric
summands likewise have nonzero exchange scalars for the nontrivial generated
channels, with the usual low-rank degeneracies handled by deleting empty
summands from \(\Lambda_*\). Thus an active nonzero fundamental or
antifundamental plaquette coefficient produces a nonzero first-shell row
coefficient. `square`

### Proposition 69.5: The Minimal Seed Row Has A Raw Kernel

Assume the active local action has nonzero adjacent plaquette coefficients
for both a planar exterior staple and a transverse staple at some boundary
link of \(C_{22}\), in a fundamental or paired fundamental action channel.
Then the seed Schwinger-Dyson row for \((C_{22},e)\) has a nonzero raw kernel
direction after the admissible physical orbit quotient.

Proof.

Let \(u_\parallel\) and \(u_\perp\) be first-shell labels for the planar
exterior and transverse staples at \(e\), with a nonzero generated
fundamental-channel contraction. Lemma 69.3 says these labels are not in the
same physical orbit under \(\mathfrak G_{61,1}^{min}\). Lemma 69.4 and the
nonzero action-coefficient hypothesis say that both appear in the same seed
row with nonzero coefficients:

```math
a_\parallel x_{u_\parallel}
+a_\perp x_{u_\perp}
+\sum_{u\ne u_\parallel,u_\perp}a_u x_u
=b_{22,e}(x_{<1})+\tau_{22,e}.
```

The vector

```math
v_{u_\parallel}=a_\perp,
\qquad
v_{u_\perp}=-a_\parallel,
\qquad
v_u=0\quad(u\ne u_\parallel,u_\perp)
```

annihilates the first-shell part of this seed row. It is not a pure symmetry
direction because the two labels are not physically identified. Therefore the
seed-row submatrix has a nonzero raw kernel direction. This is exactly the
kernel diagnostic of Lemma 68.6. `square`

### Corollary 69.6: Orbit-Collapse Alone Cannot Prove `SIC1-pass`

On the minimal fundamental branch with the usual nonzero four-dimensional
plaquette adjacency, the orbit-collapse test `OC_61,1` does not by itself
prove first-shell invertibility.

Equivalently, the output of the orbit-only specialization is not

```math
\mathrm{SIC1\text{-}pass}.
```

Proof.

Proposition 69.5 gives a raw kernel direction in the seed-row submatrix that
is not removed by the admissible orbit quotient. First-shell invertibility
could still be recovered by one-staple self rows, reflection/positivity rows,
or a declared sector enlargement, but it is not a consequence of orbit
collapse alone. `square`

### Definition 69.7: Minimal First-Shell Row Package Still Needed

To decide the full first-shell certificate on the minimal branch, one must
now supply the row package

```math
\mathfrak R_{69}^{min}
:=
\left(
M_{u}^{self},
\tau_{u}^{(2+)},
C_{\rm tail}^{(2+)},
r_{61,1},
Q_{61,1},
\mathcal P_{\rm refl/pos}^{min}
\right)_{u\in\mathcal U_{61,1}^{min}/\mathfrak G_{61,1}^{min}}.
```

Here \(M_u^{self}\) is the one-staple Schwinger-Dyson row from Definition
68.4, \(\tau_u^{(2+)}\) is its second-shell remainder, and
\(\mathcal P_{\rm refl/pos}^{min}\) records the finite reflection-positivity
and positivity constraints actually available on the same pushed-forward
scalar law.

The package must decide:

```math
\ker_{\rm phys}M_{61,1,j}^{min}=0,
\qquad
\|Q_{61,1,j}^{min}\|\,r_{61,1,j}^{min}<1,
\qquad
\tau_{61,1,j}^{(2+)}\to0
\text{ on the chosen cofinal schedule.}
```

Without these data, replacing the seed-row kernel by zero would be an
unlicensed closure assumption.

### Theorem 69.8: Minimal Fundamental First-Shell Verdict

For the minimal fundamental branch
\(\mathfrak D_{69}^{min}\), the current papers prove the following and no
more:

```math
\mathrm{SIC1\text{-}pass}
\quad\text{is not proved by orbit collapse or seed rows,}
```

```math
\mathrm{SIC1\text{-}fail}
\quad\text{is not proved,}
```

and the active output is

```math
\mathrm{SIC1\text{-}enlarge/source}
```

meaning: include the one-staple self rows and source their \(B_2\)-tail and
contraction data via \(\mathfrak R_{69}^{min}\), or enlarge the declared
record/sector battery and rerun the finite ledger.

Proof.

Corollary 69.6 rules out an orbit-only pass. It does not rule out a full pass,
because Paper 14 separates forced-record generation from shell
invertibility: one-staple rows may remove the seed-row kernel once their
second-shell tails are controlled. But Paper 14 Theorem 23.5 says \(B_1\)
does not close exactly; differentiating one-staple records forces \(B_2\)-type
records. Therefore those rows cannot be used as a closed finite linear system
until \(\tau^{(2+)}\) is controlled by a same-record forced-tail source.
Definition 69.7 lists the missing finite data. Hence the only justified
verdict is enlarge/source, not pass or fail. `square`

### Corollary 69.9: Updated Next Work Item

The next actual computation is not another scalar \(s\)-window test. It is
the minimal first-shell row package:

```math
\text{compute }M_u^{self}\text{ for the planar and transverse first-shell orbits,}
```

```math
\text{compute or bound }\tau_u^{(2+)},
```

```math
\text{then test }\ker_{\rm phys}M_{61,1,j}^{min}=0
\text{ and }
\|Q_{61,1,j}^{min}\|r_{61,1,j}^{min}<1.
```

If this succeeds, the first shell can enter the common
\(E_{14}/X_{13}\) bypass. If it fails by a genuine physical kernel, the
minimal branch is falsified and the project must either enlarge the scalar
record law or carry \(E_{14}^{park}\) and \(X_{13}^{(26),SEL2}\) separately.

## 70. Minimal One-Staple Self-Row Audit

Section 69 found a concrete seed-row kernel between planar exterior and
transverse first-shell staples. The only legitimate way to remove that kernel
inside the current record ontology is to use the one-staple self rows and then
control their \(B_2\)-type remainders. This section writes the exact finite
test.

### Definition 70.1: Two-Orbit First-Shell Subsystem

Fix a boundary link \(e\) of \(C_{22}\) and choose one planar exterior orbit
\(\parallel\) and one transverse orbit \(\perp\) as in Definition 69.2. Let

```math
x_\parallel
:=
\int Y_\parallel\,d\nu_j^{SEL2},
\qquad
x_\perp
:=
\int Y_\perp\,d\nu_j^{SEL2}.
```

The seed row has the form

```math
a_\parallel x_\parallel+a_\perp x_\perp
=b_0(x_{<1})+\tau_0+\mathrm{other}_{1},
```

where \(a_\parallel,a_\perp\ne0\) under the hypotheses of Proposition 69.5,
and \(\mathrm{other}_{1}\) denotes first-shell orbit coordinates not in the
two-orbit subblock.

For \(\alpha\in\{\parallel,\perp\}\), the one-staple self row obtained by
differentiating \(Y_\alpha\) is written after projection as

```math
m_{\alpha\parallel}x_\parallel
+m_{\alpha\perp}x_\perp
=
b_\alpha(x_{<1})
+\tau_\alpha^{(2+)}
+\mathrm{other}_{\alpha,1}.
```

Here:

1. \(b_\alpha(x_{<1})\) contains retractions to \(B_{61,j}^{(0)}\) and
   earlier-shell scalar records;
2. \(\mathrm{other}_{\alpha,1}\) contains first-shell orbit coordinates
   outside the chosen planar/transverse two-orbit subblock;
3. \(\tau_\alpha^{(2+)}\) contains two-staple, corner, rectangle-extension,
   transverse-sheet, and local action-density records from Paper 14
   Definition 23.2.

This subsystem is not a replacement for the full \(M_{61,1,j}^{min}\). It is
the smallest block that can test whether the explicit seed-row kernel from
Proposition 69.5 is removable by first-shell self rows.

### Definition 70.2: Two-Orbit Rank Test

Let

```math
M_{70}^{2orb}
:=
\begin{pmatrix}
a_\parallel & a_\perp\\
m_{\parallel\parallel} & m_{\parallel\perp}\\
m_{\perp\parallel} & m_{\perp\perp}
\end{pmatrix}.
```

Define the two minors

```math
\Delta_\parallel
:=
a_\parallel m_{\parallel\perp}
-a_\perp m_{\parallel\parallel},
```

```math
\Delta_\perp
:=
a_\parallel m_{\perp\perp}
-a_\perp m_{\perp\parallel}.
```

The two-orbit rank gate is

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}RANK}
\quad\Longleftrightarrow\quad
|\Delta_\parallel|+|\Delta_\perp|>0
```

after all coefficients are evaluated on the same finite row, projection
basis, action-channel list, and physical orbit quotient.

If this gate fails, the planar/transverse seed-kernel direction is not
removed by the two displayed self rows. It may still be removed by other
first-shell rows, but not by this minimal two-orbit block.

### Lemma 70.3: Nonzero Second-Shell Remainders Are Forced At Finite Row

For the usual four-dimensional local plaquette-containing action, the
one-staple self rows in Definition 70.1 contain \(B_2\)-type records with
nonzero coefficients at finite cutoff, unless the active projection
explicitly deletes those terms and pays the corresponding projection defect.

Proof.

Paper 14 Lemma 23.3 applies to each primitive one-staple record
\(Y_\alpha\). Differentiating \(Y_\alpha\) along a link of its deformed loop
and contracting against the local action derivative produces either a
retraction to the seed battery or a second local detour. The non-retracting
detours are precisely the \(B_2\)-type records listed in Paper 14 Definition
23.2. Paper 14 Theorem 23.5 then says that \(B_1\) does not close exactly.
Therefore those terms are present in the exact finite identity unless they
are moved into a declared projection defect. In either case, they cannot be
set to zero without a same-record estimate. `square`

### Definition 70.4: Minimal \(B_2\)-Tail Gate

The two-orbit self-row tail gate is

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}TAIL}
(C_{70},m_{70})
```

and asserts that, on the active cofinal schedule,

```math
\max_{\alpha\in\{\parallel,\perp\}}
\left\|\tau_\alpha^{(2+)}\right\|
\le C_{70}e^{-m_{70}K(j)}
\quad\text{with}\quad
K(j)\to\infty,
```

or, more generally,

```math
\max_{\alpha\in\{\parallel,\perp\}}
\left\|\tau_\alpha^{(2+)}\right\|\to0.
```

The norm is the canonical forced-record norm of Paper 14 Definition 25.5, or
any stronger same-record norm that dominates projection, connected-cumulant,
and transport tails. An area-law forced-detour bound is not an admissible
source for this gate in Paper 21.

### Definition 70.5: Two-Orbit Gap Gate

Assume `P21-SIC1-2ORB-RANK`. Let \(Q_{70}^{2orb}\) be the least-norm right
inverse of \(M_{70}^{2orb}\) on the constrained two-orbit range, after
removing only the physical quotients licensed by Definitions 68.2 and 28.3.
Let \(r_{70}^{2orb}\) be the Lipschitz constant of the same-shell nonlinear
remainder restricted to the two-orbit subblock. The gap gate is

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}GAP}
\quad\Longleftrightarrow\quad
\|Q_{70}^{2orb}\|\,r_{70}^{2orb}<1.
```

This is a genuine finite matrix/norm condition. It is not implied by rank
alone.

### Theorem 70.6: Sufficient Two-Orbit Kernel Removal

Assume:

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}RANK},
\qquad
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}TAIL},
\qquad
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}GAP}.
```

Assume also that the outside first-shell coordinates
\(\mathrm{other}_{1}\) and \(\mathrm{other}_{\alpha,1}\) are either already
determined by other first-shell rows or included in the same finite matrix
before the right inverse is computed. Then the planar/transverse raw kernel
from Proposition 69.5 is removed in the physical first-shell quotient.

Proof.

The rank gate makes the displayed planar/transverse columns injective on the
two-orbit constrained range after the licensed physical quotients. The tail
gate sends the \(B_2\)-type remainders to zero along the cofinal row, so the
self rows become legitimate first-shell equations in the limiting shell
system. The gap gate gives the contraction estimate of Paper 14 Definition
28.4. Paper 14 Theorem 28.5 then applies to this subblock, or to the enlarged
finite first-shell matrix if the outside first-shell coordinates are included.
Hence two compatible candidate laws agreeing on earlier shells and tails
cannot differ along the planar/transverse seed-kernel direction. `square`

### Theorem 70.7: Current Source Verdict For The Minimal Self-Row Package

The current Paper-21 source package does not prove the minimal two-orbit
kernel removal certificate.

More precisely:

1. `P21-SIC1-2ORB-RANK` is not evaluated, because the actual projected
   coefficients \(m_{\alpha\beta}\) have not been computed from the active
   action-channel list, projection basis, and physical orbit quotient.
2. `P21-SIC1-2ORB-TAIL` is not proved; Lemma 70.3 shows that a nonzero
   \(B_2\)-type remainder is forced at finite row, and the current corpus has
   not supplied a same-record forced-tail decay theorem for this two-orbit
   package.
3. `P21-SIC1-2ORB-GAP` is not proved, because neither a rowwise right-inverse
   norm nor a same-shell nonlinear Lipschitz bound has been computed for the
   active first-shell matrix.

Therefore the minimal branch remains parked at

```math
\mathrm{SIC1\text{-}enlarge/source},
```

not at `SIC1-pass` and not at `SIC1-fail`.

Proof.

Item 1 is a finite coefficient audit that has not been performed in Papers
14, 20, or 21. Item 2 follows from Lemma 70.3 together with the forced-tail
status of Theorem 63.6. Item 3 follows from Paper 14 Definition 28.4: a
positive shell gap requires an actual right inverse and a nonlinear Lipschitz
bound, neither of which is part of the existing source package. Since Theorem
70.6 needs all three gates, the certificate is not closed. Since no
non-removable full first-shell physical kernel has been exhibited, failure is
also not proved. `square`

### Corollary 70.8: Next Concrete Computation

The next executable finite-algebra task is now completely specified:

```math
\text{compute }
m_{\alpha\beta}
\quad
(\alpha,\beta\in\{\parallel,\perp\})
```

from the active projected Schwinger-Dyson identities, then evaluate

```math
\Delta_\parallel,\qquad \Delta_\perp.
```

If the two-orbit rank gate fails, enlarge the subblock by the remaining
first-shell orbits and recompute the physical kernel. If the rank gate passes,
the next task is the same-record \(B_2\)-tail estimate for
\(\tau_\parallel^{(2+)}\) and \(\tau_\perp^{(2+)}\), followed by the
right-inverse/Lipschitz gap audit.

## 71. Casimir Self-Row Resolution Of The Two-Orbit Rank Gate

Section 70 left six concrete tasks: freeze the row data, compute
\(m_{\alpha\beta}\), evaluate the minors, enlarge if rank fails, attack the
\(B_2\)-tail if rank passes, and then compute the shell gap. This section
executes that list as far as the current papers allow.

The main point is useful: the planar/transverse **rank** obstruction is not
the hard part if the projected ledger includes the Casimir-contracted
one-staple self row. The hard part moves immediately to the \(B_2\)-tail and
nonlinear gap.

### Definition 71.1: Casimir-Row Projection Convention

The Casimir-row projection convention for the minimal first shell adds, for
each primitive one-staple record \(Y_u\), the compact-group identity obtained
from Theorem 10.2 of Paper 14 by applying it to

```math
F=L_\ell^A Y_u
```

and summing over the Lie algebra index \(A\) and over the selected loop links
\(\ell\) in the one-staple path. Equivalently, it includes the projected
closed scalar identity

```math
\mathbb E_{\nu_j^{SEL2}}
\left[
\sum_{\ell\in E_u^{sel}}\sum_A L_\ell^A L_\ell^A Y_u
\right]
=
\mathbb E_{\nu_j^{SEL2}}
\left[
\sum_{\ell\in E_u^{sel}}\sum_A
(L_\ell^A Y_u)(L_\ell^A S_j)
\right],
```

with every term evaluated before pushforward and then projected onto the same
finite scalar battery. Here \(E_u^{sel}\) is a nonempty selected link set in
the one-staple loop. The convention is legal only if
\(\Pi_{\rm proj}^{min}\) includes these Casimir-contracted rows and charges
their off-battery remainders to the same \(\tau^{(2+)}\) ledger.

This is a projection-basis enlargement, not a new observable law. It uses the
same pushed-forward `SEL2` record law and the same one-staple scalar records.

### Lemma 71.2: Linkwise Casimir Diagonal

Let \(Y_u\) be a one-staple scalar Wilson-loop record in irreducible channel
\(\mu(u)\), or in the paired real-character scalar built from that channel.
If \(\ell\) is a link appearing once in the reduced one-staple loop path, then

```math
\sum_A L_\ell^A L_\ell^A Y_u
=
-C_2(\mu(u))\,Y_u
```

up to the harmless global sign convention for the chosen Schwinger-Dyson
ledger. In particular the coefficient of \(Y_u\) is nonzero whenever
\(\mu(u)\) is nontrivial.

Proof.

On a single link occurrence, the left-invariant group Laplacian acts on the
matrix coefficient of an irreducible representation \(\mu\) by the scalar
\(-C_2(\mu)\). Taking the trace around the closed loop and then the real or
paired real central scalar does not change the eigenvalue. Since the
fundamental branch deletes empty or trivial generated channels from the
active nontrivial shell coordinates, \(C_2(\mu(u))>0\). `square`

### Lemma 71.3: Action Terms Are Retractions Or \(B_2\)-Type Terms

For the minimal planar/transverse two-orbit block, the action side of the
Casimir-row identity for \(Y_\parallel\) or \(Y_\perp\) contributes no new
coefficient to the other two-orbit first-shell coordinate unless the active
projection basis explicitly identifies a second local detour with a
first-shell record.

With the standard Paper-14 forced-record taxonomy, the action-side terms are:

1. retractions to \(B_{61,j}^{(0)}\);
2. two-staple records;
3. corner or bent nonplanar records;
4. rectangle-extension records;
5. transverse-sheet records;
6. local action-density records for improved action terms.

The non-retraction terms are part of \(\tau_u^{(2+)}\).

Proof.

This is Paper 14 Definition 23.2 and Lemma 23.3 applied to the two primitive
one-staple records. If the adjacent action plaquette cancels the existing
staple, the loop retracts to the seed battery. If it does not cancel, the
result has a second local detour or a local action-density insertion. Such a
record is not a primitive first-shell one-staple record in the
\((\parallel,\perp)\) block. Therefore it is assigned to the \(B_2\)-type
tail unless the projection convention declares a special identification. No
such identification is present in the strict minimal branch. `square`

### Definition 71.4: Computed Two-Orbit Coefficients

Under the Casimir-row projection convention and the strict minimal
planar/transverse quotient, define

```math
\kappa_\parallel
:=
\sum_{\ell\in E_\parallel^{sel}} C_2(\mu_\parallel),
\qquad
\kappa_\perp
:=
\sum_{\ell\in E_\perp^{sel}} C_2(\mu_\perp).
```

Both are strictly positive. After choosing the global row sign so that the
diagonal entries are positive, Lemmas 71.2 and 71.3 give the evaluated
two-orbit coefficients:

```math
m_{\parallel\parallel}=\kappa_\parallel,
\qquad
m_{\parallel\perp}=0,
```

```math
m_{\perp\parallel}=0,
\qquad
m_{\perp\perp}=\kappa_\perp.
```

All non-retraction action-side terms are carried by
\(\tau_\parallel^{(2+)}\) and \(\tau_\perp^{(2+)}\).

### Theorem 71.5: Two-Orbit Rank Gate Closes Under Casimir Rows

Assume:

1. the active projection basis includes the Casimir-row convention of
   Definition 71.1;
2. \(a_\parallel,a_\perp\ne0\), as in Proposition 69.5;
3. the active generated channels \(\mu_\parallel,\mu_\perp\) are nontrivial.

Then

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}RANK}
```

holds. More explicitly,

```math
\Delta_\parallel
=
-a_\perp\kappa_\parallel,
\qquad
\Delta_\perp
=
a_\parallel\kappa_\perp,
```

so

```math
|\Delta_\parallel|+|\Delta_\perp|>0.
```

Proof.

Insert the coefficients from Definition 71.4 into the minors of Definition
70.2. Since \(a_\parallel,a_\perp\) are nonzero and
\(\kappa_\parallel,\kappa_\perp>0\), at least one minor is nonzero; in fact
both displayed absolute values are positive. `square`

### Corollary 71.6: If Casimir Rows Are Excluded, Rank Remains A Projection-Basis Gate

If \(\Pi_{\rm proj}^{min}\) excludes the Casimir-contracted self rows, the
current papers do not determine \(m_{\alpha\beta}\). In that convention the
rank gate remains exactly the unevaluated finite audit of Corollary 70.8.

Thus the branch has two honest options:

```math
\text{include Casimir rows and close the two-orbit rank gate,}
```

or

```math
\text{keep a smaller projection basis and carry }
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}RANK}
\text{ as an open finite audit.}
```

The first option is the natural Barandes-aligned move because it declares the
operational identity actually being used instead of hiding it inside a
symbolic matrix entry.

### Lemma 71.7: Finite Right-Inverse Bound For The Rank-Closed Block

Assume the Casimir-row convention and let

```math
\kappa_{\min}:=\min(\kappa_\parallel,\kappa_\perp)>0.
```

For the two-orbit matrix \(M_{70}^{2orb}\) of Definition 70.2, with the
evaluated coefficients of Definition 71.4, there is a right inverse
\(Q_{70}^{2orb}\) satisfying

```math
\|Q_{70}^{2orb}\|\le {1\over \kappa_{\min}}.
```

Proof.

For any vector \(v=(v_\parallel,v_\perp)\),

```math
\|M_{70}^{2orb}v\|^2
=
|a_\parallel v_\parallel+a_\perp v_\perp|^2
+\kappa_\parallel^2|v_\parallel|^2
+\kappa_\perp^2|v_\perp|^2
\ge
\kappa_{\min}^2\|v\|^2.
```

Therefore the smallest singular value of the two-column matrix is at least
\(\kappa_{\min}\), and the Moore-Penrose right inverse on the constrained
range has norm at most \(1/\kappa_{\min}\). `square`

### Definition 71.8: Remaining Tail And Gap Source Gates

After the Casimir-row rank closure, the remaining two gates are:

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}TAIL}
:
\max_{\alpha\in\{\parallel,\perp\}}
\|\tau_\alpha^{(2+)}\|\to0,
```

and

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}NLIP}
:
r_{70}^{2orb}<\kappa_{\min}.
```

The second gate is a sufficient form of `P21-SIC1-2ORB-GAP` by Lemma 71.7.
Both gates must be evaluated on the same pushed-forward scalar law and the
same projection convention.

### Theorem 71.9: Six-Step Verdict

For the minimal fundamental first-shell branch, the six tasks from Corollary
70.8 have the following status.

1. **Freeze row data:** closed modulo explicitly choosing the Casimir-row
   projection convention.
2. **Compute \(m_{\alpha\beta}\):** closed under that convention by
   Definition 71.4.
3. **Evaluate rank minors:** closed by Theorem 71.5.
4. **Enlarge if rank fails:** not needed on the Casimir-row branch; still
   required on any branch that excludes those rows and then fails the finite
   rank audit.
5. **Attack the \(B_2\)-tail:** not closed. Paper 14 proves the exact
   \(B_2\)-forcing and gives KP, collar-clustering, or direct-tail sufficient
   routes; Papers 11--12 do not supply this same-record tail theorem for the
   active branch.
6. **Compute the gap:** partially reduced. Lemma 71.7 gives a finite inverse
   ceiling, but the nonlinear Lipschitz bound
   \(r_{70}^{2orb}<\kappa_{\min}\) is not proved.

Therefore the planar/transverse rank issue is settled on the declared
Casimir-row branch, but full `SIC1-pass` is still not proved. The remaining
obstruction is exactly

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}TAIL}
+
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}NLIP}.
```

Proof.

Items 1--3 are Definitions 71.1 and 71.4 plus Theorem 71.5. Item 4 is
Corollary 71.6. Item 5 follows from Paper 14 Lemma 23.3 and Theorem 23.5
together with the forced-tail status in Theorem 63.6. Item 6 is Lemma 71.7
and the definition of the shell gap in Paper 14 Definition 28.4. `square`

### Corollary 71.10: Next Nontrivial Work Item

The next task is no longer the two-orbit rank calculation. It is to prove or
falsify the same-record \(B_2\)-tail gate:

```math
\max_{\alpha\in\{\parallel,\perp\}}
\|\tau_\alpha^{(2+)}\|\to0.
```

The admissible attacks are:

1. prove a direct projection/connected/transport tail bound for the
   second-shell records;
2. prove a KP forced-polymer bound with exponent beating the Paper-14
   branching and coefficient-growth rate;
3. prove collar-factorizing clustering for the two-orbit \(B_2\) records.

The area-law forced-detour route remains forbidden here because it would
import the confinement conclusion into the source estimate.

## 72. \(B_2\)-Tail-Zero Audit And Forced-Shell Enlargement Fork

Section 71 settles the planar/transverse rank obstruction on the declared
Casimir-row branch. This section executes the next six steps. The purpose is
to decide whether the remaining \(B_2\)-tail can honestly be set to zero at
fixed first shell, or whether the record law forces a second shell and then an
all-depth tower.

The answer is sharp. There is no finite-algebra proof of fixed-shell
\(B_2\)-tail zero in the present corpus. Retractions are harmless, but the
non-retracting \(B_2\) records are genuine operational records. A cofinal
zero theorem would therefore have to be a same-record dynamical tail theorem,
not a bookkeeping identity. In the absence of that theorem, the
Barandes-aligned move is to declare the forced second shell.

### Definition 72.1: Active Casimir-Row Branch

For the remainder of the first-shell audit, the active branch is the
Casimir-row branch of Definition 71.1. Thus:

1. the two-orbit first-shell matrix includes the Casimir-contracted self rows;
2. the planar/transverse rank gate is closed by Theorem 71.5;
3. the finite inverse ceiling is the one in Lemma 71.7;
4. all off-battery action-side terms are assigned to the same forced-record
   ledger used in Paper 14 Sections 23--25.

The remaining first-shell gate is therefore not rank. It is

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}TAIL}
:
\max_{\alpha\in\{\parallel,\perp\}}
\|\tau_\alpha^{(2+)}\|\to0,
```

together with the nonlinear gap source

```math
\mathrm{P21\text{-}SIC1\text{-}2ORB\text{-}NLIP}
:
r_{70}^{2orb}<\kappa_{\min}.
```

### Definition 72.2: The \(B_2\) Remainder Split

Let

```math
\mathcal Z_{70}^{(2)}
:=
\{Z_{\alpha,\zeta}:
\alpha\in\{\parallel,\perp\},
\zeta\in\mathrm{B2Types}\}
```

be the list of second-shell records generated by the Casimir self rows for
the planar and transverse one-staple records. The type set is

```math
\mathrm{B2Types}
=
\{\mathrm{ret},\mathrm{2st},\mathrm{corn},
\mathrm{rect},\mathrm{trans},\mathrm{act}\},
```

corresponding respectively to retractions, two-staple records, corner or bent
records, rectangle-extension records, transverse-sheet records, and local
action-density records in Paper 14 Definition 23.2.

Split

```math
\mathcal Z_{70}^{(2)}
=
\mathcal Z_{70}^{ret}
\sqcup
\mathcal Z_{70}^{nr},
```

where \(\mathcal Z_{70}^{ret}\) consists of retractions to
\(\mathcal B_{61,j}^{(0)}\) and \(\mathcal Z_{70}^{nr}\) consists of all
non-retracting \(B_2\)-type records.

The fixed-depth zero gate is

```math
\mathrm{P21\text{-}SIC1\text{-}B2ZERO}
:
\limsup_j
\max_{\alpha\in\{\parallel,\perp\}}
\|\tau_{\alpha,j}^{(2+)}\|=0
```

with the norm understood as the Paper-14 canonical forced-record norm, or any
stronger same-record norm that dominates projection, connected-cumulant, and
transport tails.

### Lemma 72.3: Retractions Are Not Tail

The records in \(\mathcal Z_{70}^{ret}\) do not contribute to
\(\tau_\alpha^{(2+)}\). They are already lower-shell records and must be moved
to the lower-shell right-hand side \(b_\alpha(x_{<1})\).

Proof.

A retraction is exactly the case in Paper 14 Definition 23.2 where the new
plaquette cancels the previous staple and returns to a loop already in the
seed battery. Section 71 uses the same taxonomy. Such a term is not an
unresolved second-shell coordinate. Charging it to the \(B_2\)-tail would
double count a lower-shell record and would weaken the row artificially.
`square`

### Lemma 72.4: Non-Retraction \(B_2\) Records Are Not First-Shell Algebra

For a four-dimensional local plaquette-containing `SU(N)` action with
nonzero adjacent plaquette coefficients, the generic records in
\(\mathcal Z_{70}^{nr}\) are not measurable with respect to the first-shell
battery \(\mathcal B_{61,j}^{(1)}\).

Consequently, the finite algebra internal to \(\mathcal B_{61,j}^{(1)}\)
cannot prove

```math
\tau_{\alpha,j}^{(2+)}=0
```

as an identity.

Proof.

Paper 14 Lemma 23.3 proves that differentiating a primitive one-staple record
generates two-staple, corner, rectangle-extension, transverse-sheet, or local
action-density records, and that at least one such generated record is not a
function of the one-staple battery in a generic four-dimensional local
plaquette action. The planar/transverse records of Section 70 are precisely
primitive one-staple records in this sense. Lemma 71.3 already identifies the
action-side non-retractions with the \(B_2\)-type ledger. Therefore a
fixed-shell algebraic rewrite cannot make all of
\(\mathcal Z_{70}^{nr}\) disappear. `square`

### Theorem 72.5: Fixed-Shell \(B_2\)-Tail Zero Is Not Proved By The Current Corpus

The current Papers 10--14, 20, and 21 do not prove

```math
\mathrm{P21\text{-}SIC1\text{-}B2ZERO}.
```

More precisely:

1. retractions are zero-cost lower-shell terms by Lemma 72.3;
2. non-retracting \(B_2\) records are genuine new records by Lemma 72.4;
3. Papers 11--12 supply locality and loop-readout ledgers, but not a
   same-record decay theorem for these \(B_2\) forced records;
4. Paper 14 supplies the forced-record growth mechanism and sufficient
   non-area-law routes to tail summability, but does not prove those routes
   for the active `SEL2` pushed-forward law;
5. Paper 20 closes several clean scalar coefficient and collar ledgers, but
   does not identify the non-retracting \(B_2\) records with already-paid
   scalar coefficient terms.

Thus fixed-shell \(B_2\)-tail zero is parked as an external source theorem,
not a proved result.

Proof.

Items 1 and 2 are Lemmas 72.3 and 72.4. Items 3--5 are the import status
already recorded in Theorems 62.9, 63.6, 67.2, and 71.9. The only way to set
\(\tau^{(2+)}\) to zero without declaring the new records would be to prove a
same-record dynamical estimate making their canonical forced-record norm
vanish cofinally. No such theorem appears in the cited papers. The area-law
forced-detour route is explicitly forbidden here because it would import the
desired confinement conclusion. `square`

This does not prove that the actual continuum dynamics cannot make the
\(B_2\)-tail vanish. It proves the narrower and necessary point: the current
finite algebra and existing source lemmas do not license spending it as zero.

### Definition 72.6: Forced Second-Shell Enlargement

If `P21-SIC1-B2ZERO` is not supplied as a new source theorem, the active
record law must enlarge to the forced second shell:

```math
\mathcal B_{61,j}^{[2]}
:=
\mathcal B_{61,j}^{(1)}
\cup
\mathcal Z_{70}^{nr}.
```

Equivalently, the first-shell row is rewritten as

```math
M_{61,1,j}x_{61,1,j}
=
b_{61,1,j}(x_{<1})
+L_{61,2,j}x_{61,2,j}
+T_{61,j}^{(>2)}
+\varepsilon_{61,1,j},
```

where \(x_{61,2,j}\) are the newly declared non-retracting \(B_2\) moments,
and \(T_{61,j}^{(>2)}\) is the tail beyond the second shell.

This is not a new physical assumption. It is the operational declaration of
the records already demanded by the compact-group identities.

### Lemma 72.7: Shell-2 Casimir Rows Give The Natural Rank Attack

For every nontrivial primitive record \(Z\in\mathcal Z_{70}^{nr}\), the same
Casimir-row construction used in Section 71 gives a diagonal self coefficient

```math
\kappa_Z
:=
\sum_{\ell\in E_Z^{sel}} C_2(\mu_Z)>0
```

provided the selected link set \(E_Z^{sel}\) is nonempty and the generated
channel \(\mu_Z\) is nontrivial.

The corresponding shell-2 row has the form

```math
\kappa_Z z_Z
=
b_Z(x_{\le1})
+L_{Z,3}x_{61,3,j}
+R_Z(x_{\le2})
+\varepsilon_Z,
```

after moving retractions to \(b_Z\).

Proof.

The proof is the same compact-group Casimir argument as Lemma 71.2, applied
to the new primitive loop or local action-density record. The Laplacian on a
nontrivial irreducible channel acts by a nonzero Casimir. Action-side
non-retractions generated from this row are next-shell records by the Paper
14 forced-record taxonomy. `square`

### Definition 72.8: All-Depth Replacement For Fixed \(B_2\)-Zero

The replacement for `P21-SIC1-B2ZERO` is the all-depth forced tower

```math
\mathcal B_{61,j}^{[\infty]}
=
\bigcup_{K\ge0}\mathcal B_{61,j}^{[K]},
```

with two source gates:

```math
\mathrm{P21\text{-}E14X13\text{-}FTS\text{-}SRC}
(C_F^{61},m_F^{61})
```

and

```math
\mathrm{P21\text{-}E14X13\text{-}SSI}
:
\sup_K \|Q_{61,K}\|\,r_{61,K}<1.
```

Here `SSI` is shell-by-shell invertibility. It is the uniform all-depth form
of the `P21-E14X13-SIC` gate in Definition 62.7 and the
`SIC_{K\ge2}` component of Definition 67.1. The forced-tail source must obey
the scalar pass inequality

```math
m_F^{61}>g_c^{61}+\log C_{geom}^{61}.
```

Equivalently, every tail beyond a cofinal shell depth \(K(j)\to\infty\) must
vanish in a norm dominating the Paper-14 projection, connected, and transport
tail norms.

### Theorem 72.9: Six-Step Settlement Of The \(B_2\)-Tail Issue

The six-step execution from Section 71 has the following rigorous verdict.

1. **Declare active branch.** The active finite-rank branch is the
   Casimir-row branch of Definition 72.1.
2. **Audit fixed \(B_2\)-zero.** The current corpus does not prove
   `P21-SIC1-B2ZERO`; by Lemma 72.4 the non-retracting \(B_2\) terms are not
   first-shell algebra.
3. **Enlarge if zero is unavailable.** Without a new same-record dynamical
   tail theorem, the valid next record law is the forced second-shell
   enlargement of Definition 72.6.
4. **Run the same rank strategy on shell 2.** Lemma 72.7 gives the natural
   Casimir-row diagonal attack for the new shell-2 primitive records.
5. **Replace fixed-depth zero by forced-tail summability.** The correct
   all-depth source is Definition 72.8, with scalar inequality
   \(m_F^{61}>g_c^{61}+\log C_{geom}^{61}\).
6. **Only then audit the nonlinear gap.** The first-shell bound
   \(\|Q_{70}^{2orb}\|\le1/\kappa_{\min}\) is useful, but full
   shell-invertibility needs
   \(\sup_K\|Q_{61,K}\|r_{61,K}<1\), or a declared finite-shell substitute
   with a vanishing forced tail beyond it.

Therefore the issue is settled at the present source level:

```math
\mathrm{fixed\ first\ shell\ SIC1\text{-}pass}
\quad\text{is not licensed,}
```

and the active rigorous route is

```math
\mathrm{B_2\text{-}enlarge}
+
\mathrm{FTS\text{-}SRC}
+
\mathrm{SSI}.
```

Proof.

Step 1 is Definition 72.1 and Theorem 71.5. Step 2 is Theorem 72.5. Step 3
is the operational consequence of Paper 14 Theorem 23.5: if a forced record
is not controlled as tail, it must be declared. Step 4 is Lemma 72.7. Step 5
is Paper 14 Definitions 23.8 and 25.5, specialized in Definitions 62.6 and
63.1--63.4. Step 6 is Paper 14 Definition 28.4 and the first-shell bound in
Lemma 71.7. No step imports an area law, mass gap, virtual hidden dynamics, or
a continuum Yang-Mills measure. `square`

### Corollary 72.10: Next Concrete Execution

The next executable work is no longer to ask whether the first-shell
\(B_2\)-tail is "probably small." The ordered execution is:

1. instantiate \(\mathcal Z_{70}^{nr}\) for the active `SEL2` first-shell
   template list;
2. compute the shell-2 Casimir diagonal constants \(\kappa_Z\);
3. classify shell-2 physical quotients under normalization, centrality,
   conjugation, covariance, reflection positivity, and positivity;
4. compute or bound the shell-2 right inverse \(Q_{61,2}\);
5. compute the shell-2 nonlinear Lipschitz bound \(r_{61,2}\);
6. source all-depth forced-tail decay by a same-record KP, collar-factorizing,
   or direct projection-tail theorem satisfying
   \(m_F^{61}>g_c^{61}+\log C_{geom}^{61}\).

If item 6 cannot be supplied, the common \(E_{14}/X_{13}\) bypass remains
parked as \(\mathcal G_{E14X13}^{SEL2}\), and the Paper-21 non-corner
worksheet must carry \(E_{14}^{park}+X_{13}^{(26),SEL2}\) or a separately
proved sharp bound. If item 6 is supplied and the shell invertibility audit
passes, then the common finite-battery `BLU` bypass can be reopened with real
source data rather than optimism.

## 73. Shell-2 Instantiation, Linear Bounds, And Forced-Tail Source Verdict

This section executes the six tasks in Corollary 72.10. The output is mixed
but useful:

1. the non-retracting shell-2 atlas can be instantiated from the Paper-14
   local taxonomy;
2. the Casimir diagonals have a uniform positive lower bound on nontrivial
   `SU(N)` channels;
3. the physical quotient is finite and explicit;
4. the primitive shell-2 right inverse is bounded by a Casimir gap, with a
   finite off-diagonal dominance correction for the full moment-lifted
   matrix;
5. the same-shell nonlinear remainder can be removed by using moment
   coordinates, leaving a finite matrix audit rather than an analytic
   nonlinearity;
6. the all-depth forced-tail decay is still not sourced by Papers 10--14,
   20, or the previous sections of Paper 21.

Thus the shell-2 linear algebra is no longer the main conceptual obstruction.
The irreducible source gate is the non-area-law forced-tail decay exponent.

### Definition 73.1: Instantiated Non-Retraction Shell-2 Labels

Fix the minimal fundamental branch data of Definition 69.1 and the
Casimir-row branch of Definition 72.1. A primitive non-retracting shell-2
label is a tuple

```math
Z=
(\alpha,e,p_1;\ell,p_2,\zeta;
\lambda_1,\sigma_1,\lambda_2,\sigma_2;\mu),
```

where:

1. \(\alpha\in\{\parallel,\perp\}\) is the first-shell planar/transverse
   type;
2. \(e\) is the boundary link of \(C_{22}\) used by the first staple;
3. \(p_1\) is the first exterior staple plaquette;
4. \(\ell\) is a selected link of the one-staple loop
   \(C_{22}\triangleleft_e p_1\);
5. \(p_2\) is a plaquette, or more generally a local action stencil, touching
   \(\ell\);
6. \(\zeta\) is one of

   ```math
   \mathrm{2st},\quad
   \mathrm{corn},\quad
   \mathrm{rect},\quad
   \mathrm{trans},\quad
   \mathrm{act};
   ```

7. \(\lambda_i\in\Lambda_{\rm act}^{min}\) and
   \(\sigma_i\in\{+,-\}\) record the action channel and orientation generated
   at the two identity steps;
8. \(\mu\in\Lambda_*\) is a nontrivial irreducible channel appearing in the
   generated tensor product after deleting empty and lower-shell trivial
   summands.

The retraction case is excluded:

```math
p_2\ne p_1^{-1}
\quad\text{as a cancelling local detour.}
```

The instantiated non-retracting shell is

```math
\mathcal Z_{70}^{nr,min}
:=
\{Z\text{ satisfying the preceding finite constraints}\}/\mathfrak G_{61,2}^{min},
```

where \(\mathfrak G_{61,2}^{min}\) is generated by the physical quotients in
Definition 73.5 below.

This is finite for each fixed row \(j\), degree cutoff \(D\), representation
cutoff \(\Lambda_*\), and local action stencil.

### Lemma 73.2: The Instantiation Exhausts The Paper-14 \(B_2\) Types

The set \(\mathcal Z_{70}^{nr,min}\) contains exactly the primitive
non-retracting \(B_2\) records forced by the planar/transverse one-staple
Casimir rows on the minimal branch, up to the declared row cutoffs and
physical quotients.

Proof.

Paper 14 Definition 23.2 lists the six second-step types. Lemma 72.3 removes
the retraction type. The remaining five types are precisely the values of
\(\zeta\) in Definition 73.1. The tuple records the first staple, the selected
link being differentiated, the second local action plaquette or stencil, the
two action channels, and the generated irreducible channel. These data are
exactly what Paper 14 Lemma 23.3 uses to construct the non-retracting
two-staple, corner, rectangle-extension, transverse-sheet, and local
action-density records. The row cutoffs delete only channels or monomials
outside the active finite battery, assigning them to the representation or
forced tail. `square`

### Definition 73.3: Shell-2 Casimir Diagonals

For \(Z\in\mathcal Z_{70}^{nr,min}\), let \(Y_Z\) be the corresponding
primitive scalar record in nontrivial channel \(\mu(Z)\). Choose a nonempty
selected link set \(E_Z^{sel}\) in the newly declared non-retracting detour.
Define

```math
\kappa_Z
:=
\sum_{\ell\in E_Z^{sel}} C_2(\mu_\ell(Z)).
```

For a single-channel Wilson loop coordinate this is simply

```math
\kappa_Z=|E_Z^{sel}|\,C_2(\mu(Z)).
```

For a local action-density record with several nontrivial factors, the sum is
taken over the selected nontrivial factors. Trivial factors are lower-shell
constants and are not part of \(x_{61,2}\).

Set

```math
\kappa_{2,\min}^{SEL2}
:=
\min_{Z\in\mathcal Z_{70}^{nr,min}}\kappa_Z.
```

If \(\mathcal Z_{70}^{nr,min}\ne\varnothing\), then

```math
\kappa_{2,\min}^{SEL2}\ge C_{\rm fund}(N)
:={N^2-1\over 2N},
```

where \(C_{\rm fund}(N):=(N^2-1)/(2N)\) is the fundamental `SU(N)`
quadratic Casimir in the standard normalization.

### Lemma 73.4: Casimir Diagonal Evaluation

For every \(Z\in\mathcal Z_{70}^{nr,min}\), the shell-2 Casimir row contains

```math
\kappa_Z z_Z
```

with \(\kappa_Z>0\), after choosing the row sign and moving retractions and
trivial factors to the lower-shell side.

Proof.

This is Lemma 71.2 applied to the second-shell primitive record. Every
retained coordinate has at least one nontrivial irreducible factor, because
Definition 73.1 deletes trivial generated summands from the shell unknowns.
For `SU(N)`, every nontrivial irreducible representation has quadratic
Casimir at least that of the fundamental representation. Hence each selected
nontrivial factor contributes at least \(C_{\rm fund}(N)>0\). `square`

### Definition 73.5: Physical Quotient At Shell 2

The physical quotient \(\mathfrak G_{61,2}^{min}\) is generated by the
following identifications and only these identifications unless an additional
sector quotient is explicitly declared.

1. **Centrality and conjugation.** \(Z\) is paired with its conjugate
   orientation/channel label. In a real-character battery, the pair is stored
   as one real coordinate; in a complex battery, conjugation rows remain in
   the matrix.
2. **Sheet-preserving covariance.** Hypercubic symmetries preserving the
   declared \(2\times2\) sheet identify templates with the same incidence
   type. They may rotate transverse directions into each other, but they do
   not identify planar exterior records with transverse records.
3. **Reflection.** OS reflection identifies reflected records only when the
   reflected support and channel data are in the active positive-time
   battery. Otherwise it supplies an inequality or a paired row, not a
   quotient.
4. **Normalization.** Constant and trivial-channel records are not shell-2
   coordinates.
5. **Positivity and reflection positivity.** These are constraints on the
   moment functional. They remove a kernel direction only after a concrete
   saturation or extremality statement is proved on the same finite battery.
   No such saturation is assumed here.
6. **No-corner selector.** The no-corner surface selector does not delete
   shell-2 corner records generated by Schwinger-Dyson identities unless the
   active record law explicitly routes them into a separate corner/collar
   ledger with a proved bound. Without such a route, corner records remain in
   \(\mathcal Z_{70}^{nr,min}\).

### Lemma 73.6: Quotient Does Not Kill The Casimir Gap

After quotienting by \(\mathfrak G_{61,2}^{min}\), every retained shell-2
orbit \(O\) has a well-defined positive diagonal

```math
\kappa_O
:=
\min_{Z\in O}\kappa_Z>0.
```

Moreover,

```math
\kappa_{O}\ge C_{\rm fund}(N).
```

Proof.

The allowed equalities preserve nontrivial representation content up to
conjugation, reflection, or sheet-preserving covariance. These operations
preserve the Casimir spectrum. Trivial-channel coordinates are removed before
forming shell 2, and positivity/reflection-positivity inequalities do not
identify nontrivial coordinates unless saturation is separately proved.
Therefore each retained orbit has a nonzero selected Casimir, bounded below
by \(C_{\rm fund}(N)\). `square`

### Definition 73.7: Shell-2 Matrix And Off-Diagonal Size

Let \(x_{61,2}\) be the vector of shell-2 orbit coordinates after the quotient
of Definition 73.5. Under the Casimir-row convention, write the retained
shell-2 linear system as

```math
M_{61,2}x_{61,2}
=
b_{61,2}(x_{\le1})
+T_{61}^{(>2)}
+\varepsilon_{61,2},
```

where all same-shell retained moment coordinates have been placed in the
linear matrix \(M_{61,2}\). Split

```math
M_{61,2}=D_{61,2}+O_{61,2},
```

with

```math
D_{61,2}:=\operatorname{diag}(\kappa_O)_{O\in\mathcal Z_{70}^{nr,min}/\mathfrak G_{61,2}^{min}}.
```

Define the finite off-diagonal row-sum bound

```math
\Omega_{61,2}
:=
\|O_{61,2}\|_{\infty\to\infty}.
```

For the primitive-coordinate subblock, before adding same-shell products,
\(\Omega_{61,2}=0\). For the full degree-\(D\) moment-lifted matrix,
\(\Omega_{61,2}\) is a finite computable number determined by the product-rule
cross terms and projection convention.

### Theorem 73.8: Shell-2 Right-Inverse Bound

If

```math
\Omega_{61,2}<\kappa_{2,\min}^{SEL2},
```

then \(M_{61,2}\) has a right inverse on the constrained shell-2 range with

```math
\|Q_{61,2}\|
\le
{1\over \kappa_{2,\min}^{SEL2}-\Omega_{61,2}}.
```

In particular, on the primitive-coordinate subblock,

```math
\|Q_{61,2}^{prim}\|
\le
{1\over \kappa_{2,\min}^{SEL2}}
\le
{1\over C_{\rm fund}(N)}
=
{2N\over N^2-1}.
```

Proof.

The diagonal matrix \(D_{61,2}\) is invertible with
\(\|D_{61,2}^{-1}\|\le1/\kappa_{2,\min}^{SEL2}\). If
\(\|D_{61,2}^{-1}O_{61,2}\|<1\), the Neumann series gives

```math
M_{61,2}^{-1}
=
(I+D_{61,2}^{-1}O_{61,2})^{-1}D_{61,2}^{-1}
```

on the constrained range, with the stated norm bound. In the primitive
subblock, the Casimir rows are diagonal after retractions are moved to lower
shells and non-retractions beyond shell 2 are assigned to \(T_{61}^{(>2)}\);
hence \(\Omega_{61,2}=0\). The final inequality is Lemma 73.6. `square`

If \(\Omega_{61,2}\ge\kappa_{2,\min}^{SEL2}\), this theorem does not prove
failure. It says the full degree-\(D\) matrix must be inverted directly rather
than by diagonal dominance.

### Definition 73.9: Same-Shell Nonlinear Remainder Convention

Use the moment-lifted convention of Paper 14 Definition 28.1: every retained
monomial of degree at most \(D\) containing a shell-2 primitive record is a
coordinate of \(x_{61,2}\). Under this convention, same-shell product-rule
terms are linear terms in \(M_{61,2}\), not nonlinear remainders.

The only terms not placed in \(M_{61,2}\) are:

1. degree \(>D\) products;
2. representation labels outside \(\Lambda_*\);
3. records first forced after shell 2;
4. projection, chart, or transport defects.

All four are assigned to \(T_{61}^{(>2)}+\varepsilon_{61,2}\).

### Corollary 73.10: Shell-2 Nonlinear Bound

Under the moment-lifted convention,

```math
r_{61,2}=0
```

for the retained shell-2 finite matrix. Therefore the shell-2 gap condition
reduces to the right-inverse existence and tail control:

```math
\|Q_{61,2}\|\,r_{61,2}=0<1.
```

If one uses a smaller coordinate convention that rewrites retained same-shell
products as functions of primitive coordinates, then the licensed fallback is

```math
r_{61,2}\le r_{61,2}^{raw}
```

with \(r_{61,2}^{raw}\) equal to the finite Lipschitz constant of that chosen
rewrite. The pass condition then becomes

```math
r_{61,2}^{raw}
<
\kappa_{2,\min}^{SEL2}-\Omega_{61,2}.
```

Proof.

In the moment-lifted convention, the Schwinger-Dyson and Casimir identities
are linear identities among expectations of the retained monomials. Products
created by differentiating a retained monomial are themselves retained moment
coordinates when they stay within degree and representation cutoff. The
terms outside the cutoff are not same-shell nonlinearities; they are exactly
tail or projection defects. Thus the same-shell nonlinear Lipschitz constant
for the retained finite matrix is zero. The fallback statement is Paper 14
Definition 28.4 applied to any smaller coordinate rewrite. `square`

### Definition 73.11: All-Depth Casimir-Moment Shell-Invertibility Source

For the all-depth tower, define

```math
\mathrm{P21\text{-}E14X13\text{-}CMSSI}
```

to mean:

1. every nontrivial primitive forced record at every shell has a declared
   Casimir self row;
2. the physical quotient at each shell deletes only trivial/lower-shell
   constants and symmetry duplicates, not nontrivial Casimir directions;
3. the moment-lifted convention is used at every finite retained degree;
4. the finite off-diagonal matrices obey

   ```math
   \Omega_{61,K}<\kappa_{K,\min}
   ```

   or else the exact finite matrix \(M_{61,K}\) is inverted with a certified
   bound \(q_K\);
5. the inverse amplification is summable against the forced tail:

   ```math
   \sum_{K\ge0} q_K\,Tail_K<\infty.
   ```

The shell-2 results above verify the \(K=2\) prototype of this source. They
do not by themselves prove the all-depth statement.

### Theorem 73.12: What Is Actually Closed By The Shell-2 Audit

On the active minimal fundamental, Casimir-row, moment-lifted branch:

1. \(\mathcal Z_{70}^{nr,min}\) is instantiated by Definition 73.1;
2. the shell-2 Casimir diagonals are computed by Definition 73.3 and bounded
   below by Lemma 73.4;
3. the physical quotient is fixed by Definition 73.5 and does not erase the
   Casimir gap by Lemma 73.6;
4. the primitive shell-2 right inverse satisfies

   ```math
   \|Q_{61,2}^{prim}\|\le {2N\over N^2-1};
   ```

5. the full degree-\(D\) right-inverse is bounded by Theorem 73.8 whenever
   \(\Omega_{61,2}<\kappa_{2,\min}^{SEL2}\), otherwise it is an exact finite
   matrix inversion task;
6. the retained same-shell nonlinear Lipschitz constant is zero under the
   moment-lifted convention.

Thus shell 2 does not introduce a new conceptual rank obstruction. The
remaining obstruction is the all-depth forced-tail source and, for the full
degree-\(D\) matrix, the finite off-diagonal dominance or exact inversion
audit.

Proof.

Items 1--3 are Definitions 73.1, 73.3, and 73.5 plus Lemmas 73.2, 73.4, and
73.6. Items 4--5 are Theorem 73.8. Item 6 is Corollary 73.10. The conclusion
is just the shell-invertibility logic of Paper 14 Definition 28.4 specialized
to the shell-2 Casimir-row matrix. `square`

### Definition 73.13: Forced-Tail Source Attempts

The all-depth forced-tail source for the common \(E_{14}/X_{13}\) bypass is
the following disjunction, always on the same pushed-forward `SEL2` law.

1. **KP source.**

   ```math
   \mathrm{P21\text{-}FTS\text{-}KP}
   :
   \mu_{KP}^{61}>g_c^{61}+\log C_{geom}^{61}.
   ```

2. **Collar-factorizing source.**

   ```math
   \mathrm{P21\text{-}FTS\text{-}COL}
   :
   \min(m_r^{61},M^{61}c_d^{61})
   >g_c^{61}+\log C_{geom}^{61}.
   ```

3. **Direct projection/connected/transport source.**

   ```math
   \mathrm{P21\text{-}FTS\text{-}DIR}
   :
   \operatorname{Tail}_{proj}(f)
   +\operatorname{Tail}_{conn}(f)
   +\operatorname{Tail}_{tr}(f)
   \le C_F^{61}e^{-m_F^{61}K}
   ```

   for every \(f\in\mathcal F_{61}^{(K)}\), with

   ```math
   m_F^{61}>g_c^{61}+\log C_{geom}^{61}.
   ```

These are exactly the non-area-law routes of Paper 14 Section 26, specialized
to the common battery.

### Theorem 73.14: Forced-Tail Decay Is Not Sourced By The Current Papers

The current Papers 10--14, 20, and 21 do not prove any of

```math
\mathrm{P21\text{-}FTS\text{-}KP},
\qquad
\mathrm{P21\text{-}FTS\text{-}COL},
\qquad
\mathrm{P21\text{-}FTS\text{-}DIR}
```

for the active common \(E_{14}/X_{13}\) forced tower.

More specifically:

1. the strong-coupling KP theorem in Paper 11 applies at sufficiently large
   heat time, while the active `SEL2` coefficient route is the AF/small-time
   branch; Paper 11 explicitly does not export the needed `SEL2`
   tree-rate/source gate;
2. the Paper-11 AF locality margin controls declared finite batteries and
   scale residuals, but it is not a forced-depth estimate
   \(a(f)\le C e^{-mK}\) for the all-depth shell tower;
3. Paper 12 controls Wilson-loop readout, smearing, perimeter, cusp, and
   admissible loop-continuity tails, but not the common \(E_{14}/X_{13}\)
   forced tower generated by repeated Schwinger-Dyson identities;
4. Paper 20 closes strict scalar coefficient, boundary/collar, and
   Bianchi/off-sheet root ledgers, but those are not the Paper-14 canonical
   forced-record tail norms for \(\mathcal F_{61}^{(K)}\);
5. the area-law forced-detour route of Paper 14 Corollary 26.8 remains
   forbidden in Paper 21.

Therefore the all-depth forced-tail source remains exactly

```math
\mathrm{P21\text{-}E14X13\text{-}FTS\text{-}SRC}
(C_F^{61},m_F^{61})
```

with

```math
m_F^{61}>g_c^{61}+\log C_{geom}^{61}.
```

Proof.

Paper 14 Definition 25.5 defines the canonical forced weight and Theorem
26.2/Corollary 26.4/Theorem 26.6 give the three non-area-law sufficient
routes. Honest Boundary 26.9 states that Paper 14 does not prove those routes
for actual four-dimensional Yang-Mills. Paper 11 Theorem 1A.2 and its export
contract state that Paper 11 does not supply the `SEL2` tree-rate/source gate;
its strong-coupling KP result does not continue unchanged to the AF
trajectory. Paper 12's import contract likewise says it supplies loop-readout
technology, not the `SEL2` tree-rate source or an area law. Paper 20's strict
coefficient source is a scalar root/collar audit, not a canonical
forced-record tail theorem for the countable \(E_{14}/X_{13}\) tower. Thus
none of the three admissible source attempts is currently proved. `square`

### Theorem 73.15: Executed Six-Task Verdict

The requested six-task pass has the following final status.

1. **Instantiate \(\mathcal Z_{70}^{nr}\):** done by Definition 73.1.
2. **Compute shell-2 Casimir diagonals:** done by Definition 73.3 and Lemma
   73.4, with uniform lower bound \(C_{\rm fund}(N)\).
3. **Classify physical quotients:** done by Definition 73.5.
4. **Bound \(Q_{61,2}\):** primitive bound closed by Theorem 73.8; full
   degree-\(D\) bound reduced to the finite number \(\Omega_{61,2}\), or to
   exact finite matrix inversion if diagonal dominance fails.
5. **Bound \(r_{61,2}\):** under the moment-lifted convention,
   \(r_{61,2}=0\) by Corollary 73.10.
6. **Source all-depth forced-tail decay:** not sourced by the current corpus;
   parked by Theorem 73.14 as
   `P21-E14X13-FTS-SRC`.

Consequently, the common \(E_{14}/X_{13}\) bypass is not closed yet, but its
linear-algebra obstruction has been substantially localized. The remaining
non-bookkeeping task is to prove one genuine same-record decay theorem for
the all-depth forced tower, or to accept that
\(E_{14}^{park}+X_{13}^{(26),SEL2}\) must stay carried in the Paper-21
worksheet.

Proof.

This is a summary of Theorems 73.8, 73.12, and 73.14. `square`

## 74. Forced-Depth Geometry, Bounded-Collar Cycles, And The Trace-Quotient Fork

Section 73 reduces the common \(E_{14}/X_{13}\) bypass to an all-depth
forced-tail source. This section tests the most tempting source: geometric
escape of forced records away from the original \(2\times2\) sheet, followed
by collar-factorizing clustering.

The verdict is decisive but not simply negative. Raw forced depth does **not**
force physical distance. There are non-retracting forced transitions that can
remain inside a bounded collar while increasing word length, representation
weight, or local trace complexity. Therefore ordinary collar-distance
clustering cannot prove `FTS` on the raw tower.

The only viable non-area-law rescue found here is a finite bounded-collar
trace quotient: bounded-collar cycles must be represented by a declared
finite local invariant trace algebra, after which only genuinely escaping
transitions count as forced depth. This is Barandes-aligned: it declares the
records actually demanded by the identities instead of hiding bounded local
history in an unobserved process.

### Definition 74.1: Forced Transition Automaton

For the common tower
\(\mathcal B_{61,j}^{[K]}\), define the forced transition automaton
\(\mathfrak A_{61}\) as follows.

A state is the local type of a primitive forced record, including:

```math
(\mathrm{supp},\mathrm{inc},\mathrm{word},\mathrm{chan},\mathrm{sheet\ type}),
```

where `supp` is the plaquette-collar support, `inc` is its incidence type
relative to the declared \(2\times2\) sheet, `word` is the reduced local
holonomy word up to the current finite trace quotient, `chan` is the
representation-channel data, and `sheet type` records whether the record is
planar, transverse, corner, rectangle-extension, local action-density, or a
product thereof.

An edge \(v\to w\) is present when one projected Schwinger-Dyson, loop, or
Casimir identity step applied to a primitive record of type \(v\) generates a
primitive record of type \(w\) with nonzero coefficient after deleting
retractions and lower-shell constants.

Every edge is labelled as:

1. `ret`: a retraction to a lower-shell record;
2. `esc`: a transition increasing the minimal collar distance from the
   \(2\times2\) sheet after removing the previously declared near factor;
3. `stag`: a non-retracting transition whose support remains in a bounded
   collar of the previous support;
4. `chan`: a transition whose support remains bounded but whose
   representation/trace complexity increases;
5. `branch`: a finite local branching choice.

Only `esc`, `stag`, and `chan` transitions can generate new unresolved forced
records. The `ret` transitions are lower-shell terms.

### Lemma 74.2: The Transition Alphabet Is Finite At Each Local Stencil

For fixed \(N\), local action range \(r_A\), finite local action stencil,
finite row \(j\), degree cutoff \(D\), and representation cutoff
\(\Lambda_*\), the transition alphabet of \(\mathfrak A_{61}\) is finite.
The number of outgoing primitive transition types is bounded by the local
branching constant of Paper 14 Theorem 23.7.

Proof.

Paper 14 Theorem 23.7 says that one identity step expands support by a
bounded plaquette-collar amount, increases length and representation weight
by bounded amounts, and has finitely many local stencil choices. The finite
row cutoffs retain only finitely many representation and monomial labels.
Thus only finitely many local transition labels can appear at each step.
`square`

### Definition 74.3: Raw Forced-Depth Escape Gate

The raw geometric escape gate is

```math
\mathrm{P21\text{-}FTS\text{-}RAWESC}(c_d)
```

for some \(c_d>0\). It asserts that every non-retracting primitive record
first appearing at forced depth \(K\) admits a collar-factorization

```math
f=f_{near}f_{far}+r_f
```

with \(f_{near}\in Alg_{K-1}\), and

```math
\operatorname{dist}_{col}
(\operatorname{supp}f_{far},\operatorname{supp}Alg_{K-1})
\ge c_d K,
```

up to uniformly tail-small \(r_f\). This is the geometric premise needed to
turn ordinary exponential clustering in physical/collar distance into the
forced-depth estimate

```math
a(f)\le C e^{-mK}.
```

### Theorem 74.4: Raw Forced-Depth Escape Fails

For a four-dimensional plaquette-containing `SU(N)` local action with a
nonzero adjacent plaquette coefficient, the raw gate
`P21-FTS-RAWESC(c_d)` fails for every \(c_d>0\).

More precisely, the forced transition automaton contains non-retracting
bounded-collar paths of arbitrary forced depth unless those paths are
explicitly quotiented into a declared bounded-collar trace algebra.

Proof.

Choose a non-retracting one-staple record from the active
planar/transverse branch and choose a local plaquette \(p\) sharing a link
with the current local detour but not cancelling the immediately previous
staple. Applying the Schwinger-Dyson/Casimir row to a selected link can insert
the same oriented local plaquette detour again, or insert another plaquette
inside the same bounded local collar. The resulting records have the form,
schematically,

```math
W_m=\operatorname{Tr}_\mu(A(\partial p)^mB)
```

or a finite product/local-action-density analogue, with \(m\) increased by
one under the transition. The support stays inside the fixed collar generated
by \(A\), \(B\), and \(p\), while the forced generation depth and local word
or channel complexity increase.

The transition is not a retraction because the inserted plaquette is not the
inverse of the immediately previous detour. Its coefficient is nonzero in at
least one generated channel by the same compact-group contraction mechanism
used in Lemma 69.4 and Lemma 73.4. Hence there are admissible non-retracting
transition paths with bounded physical collar distance and unbounded forced
depth.

Therefore no positive \(c_d\) can satisfy Definition 74.3 on the raw tower.
`square`

This theorem does not say that `FTS` is false. It says that `FTS` cannot be
proved by identifying forced depth with physical distance on the raw record
tower.

### Definition 74.5: Bounded-Collar Trace Quotient

Let \(Y\) be a finite bounded collar region containing \(q(Y)\) oriented link
variables. The bounded-collar trace algebra
\(\mathcal T_{N,Y}^{loc}\) is the finite invariant trace algebra generated by
the fundamental and antifundamental matrix traces of words in those
\(q(Y)\) link variables, modulo:

1. gauge conjugation at internal vertices;
2. determinant-one relations;
3. Cayley-Hamilton trace identities;
4. the finite Procesi/Razmyslov trace-generation bound for `SU(N)` invariant
   polynomial functions on a fixed finite tuple of matrices.

The bounded-trace quotient gate

```math
\mathrm{P21\text{-}FTS\text{-}BTQ}
```

asserts that every bounded-collar stagnant or channel-growth strongly
connected component of \(\mathfrak A_{61}\) is represented inside a declared
finite algebra \(\mathcal T_{N,Y}^{loc}\), with all required local trace
generators included in the moment-lifted battery.

The quotient is not allowed to identify records by intuition. It must exhibit
the finite local trace generators and the polynomial trace identities used to
rewrite the bounded-collar cycle records.

### Lemma 74.6: `BTQ` Is A Finite Operational Enlargement

For fixed \(N\) and fixed bounded collar radius, the local trace quotient of
Definition 74.5 is finite. Adding its generators to the declared scalar
battery is an operational record enlargement, not a hidden ontology or an
area-law input.

Proof.

The collar contains finitely many link variables. The gauge-invariant
polynomial trace algebra of a finite tuple of `SU(N)` matrices is finitely
generated by standard trace identities for fixed \(N\); the determinant-one
and Cayley-Hamilton relations remove unbounded powers of a fixed local word
as independent polynomial generators. Every Wilson-loop character record in a
bounded collar is a polynomial in matrix entries and their conjugates, hence
belongs to this finitely generated invariant algebra once the needed trace
generators are declared. All generators are finite scalar records of the same
whole-process law. `square`

### Theorem 74.7: The Bounded-Collar Fork

The bounded-collar part of the forced tower has exactly the following honest
fork.

1. If `P21-FTS-BTQ` is proved, stagnant/channel strongly connected components
   of \(\mathfrak A_{61}\) become finite same-shell or lower-shell algebra.
   They are no longer forced-tail depth.
2. If `P21-FTS-BTQ` is not proved or not declared, bounded-collar cycles
   remain in the forced tower, and collar-distance clustering cannot prove
   `FTS`.

Proof.

Under `BTQ`, every record generated by a bounded-collar stagnant cycle is
rewritten inside a finite declared local trace algebra. With the
moment-lifted convention, the resulting moments are coordinates of the finite
same-shell battery rather than off-shell tail records. Without `BTQ`, Theorem
74.4 supplies non-retracting bounded-collar paths of arbitrary forced depth.
Since their physical distance from the previous battery is bounded,
Definition 74.3 fails and no estimate based only on physical collar
separation can give \(e^{-mK}\). `square`

### Definition 74.8: Reduced Escape After `BTQ`

Assume `P21-FTS-BTQ`. Contract every bounded-collar stagnant or channel
strongly connected component of \(\mathfrak A_{61}\) to one finite local trace
state. The resulting reduced automaton is

```math
\overline{\mathfrak A}_{61}^{BTQ}.
```

Let \(\overline K(f)\) be the number of escaping transitions in the reduced
path generating \(f\). The reduced escape gate is

```math
\mathrm{P21\text{-}FTS\text{-}REDESC}(c_d)
```

and asserts that for every reduced primitive tail record \(f\),

```math
\operatorname{dist}_{col}
(\operatorname{supp}f_{far},\operatorname{supp}Alg_{<\overline K})
\ge c_d\,\overline K(f).
```

Define the reduced branching and coefficient-growth constants by

```math
N_{\overline K}\le N_0^{red}(C_{geom}^{red})^{\overline K},
\qquad
|c_f|\le C_c^{red}e^{g_c^{red}\overline K}.
```

If shell inverse norms obey

```math
q_{\overline K}\le C_q e^{g_q\overline K},
```

then inverse amplification is accounted for by \(g_q\).

### Theorem 74.9: Reduced Collar Source Pass Inequality

Assume:

1. `P21-FTS-BTQ`;
2. `P21-FTS-REDESC(c_d)`;
3. a same-record AF/collar clustering estimate

   ```math
   |\kappa(f_{far};G_1,\ldots,G_s)|
   \le C_{cl}e^{-M c_d\overline K};
   ```

4. a tail remainder estimate

   ```math
   \|r_f\|_{tail}\le C_re^{-m_r\overline K};
   ```

5. reduced branching, coefficient-growth, and inverse-growth constants as in
   Definition 74.8.

Set

```math
m_{red}:=\min(Mc_d,m_r).
```

Then the all-depth common forced-tail and inverse-amplified shell
summability pass if

```math
m_{red}>
g_c^{red}+\log C_{geom}^{red}+g_q.
```

If inverse amplification is uniformly bounded, \(g_q=0\).

Proof.

The reduced escape gate converts forced depth in the quotient automaton into
physical collar distance. The clustering and remainder estimates give

```math
a(f)\le C e^{-m_{red}\overline K}.
```

Multiplying by coefficient growth, branching, and inverse amplification gives
a shell contribution bounded by

```math
C\exp[-(m_{red}-g_c^{red}-\log C_{geom}^{red}-g_q)\overline K].
```

The displayed strict inequality makes the resulting geometric series
converge. This is Paper 14 Corollary 25.7 plus Definition 28.6, specialized
to the reduced automaton. `square`

### Theorem 74.10: Source Status After The Geometry Audit

The six requested tasks have the following source-level verdict.

1. **Forced-depth geometry audit.** Raw forced-depth physical escape is false
   by Theorem 74.4.
2. **Transition automaton.** The finite local transition automaton is defined
   in Definition 74.1 and is finite at each local stencil by Lemma 74.2.
3. **Bounded-collar cycles.** They exist on the raw tower and kill the naive
   collar-distance source unless `P21-FTS-BTQ` is proved.
4. **AF collar source.** After `BTQ`, the correct source is the reduced
   escape/clustering package of Definition 74.8 and Theorem 74.9.
5. **Inverse amplification.** The pass inequality must include \(g_q\):

   ```math
   m_{red}>g_c^{red}+\log C_{geom}^{red}+g_q.
   ```

6. **Common bypass.** The common \(E_{14}/X_{13}\) bypass can be reopened only
   under

   ```math
   \mathrm{P21\text{-}FTS\text{-}BTQ}
   +
   \mathrm{P21\text{-}FTS\text{-}REDESC}
   +
   \mathrm{P21\text{-}AF\text{-}COL\text{-}SRC}
   +
   \mathrm{P21\text{-}CMSSI}.
   ```

The current corpus proves none of this four-gate package. It does, however,
settle the obstruction: the naive physical-distance route is dead, and the
only non-circular route left by this audit is bounded-collar trace quotient
plus reduced forced-depth decay.

Proof.

Items 1--3 are Theorem 74.4 and Lemma 74.2. Item 4 is Theorem 74.9. Item 5
is the inverse-amplified shell summability part of Theorem 74.9, using Paper
14 Definition 28.6. Item 6 combines Theorem 62.8 with the refined source
requirements identified here and in Section 73. Papers 11--12 do not provide
the reduced forced-depth source, and Paper 20's strict scalar coefficient
ledger is not a canonical forced-tower tail theorem. The area-law route
remains forbidden. `square`

### Corollary 74.11: Next Executable Work

The next useful work is no longer to ask for generic "forced-tail decay."
It is the finite local algebra task:

1. choose the bounded collar radius \(R_{loc}\) for stagnant/channel
   components of \(\mathfrak A_{61}\);
2. instantiate the local trace generator list
   \(\mathcal T_{N,Y}^{loc}\) for that collar;
3. prove the bounded-collar rewrite identities for the stagnant cycles;
4. contract the quotient automaton
   \(\overline{\mathfrak A}_{61}^{BTQ}\);
5. compute \(C_{geom}^{red}\), \(g_c^{red}\), and \(g_q\);
6. only then test an AF collar source against

   ```math
   m_{red}>g_c^{red}+\log C_{geom}^{red}+g_q.
   ```

If the bounded trace quotient cannot be made explicit, the common
\(E_{14}/X_{13}\) bypass should remain parked and the worksheet must carry
\(E_{14}^{park}+X_{13}^{(26),SEL2}\).

## 75. Instantiating `BTQ`, Contracting The Reduced Automaton, And Computing The Reduced Constants

Section 74 left an executable finite-algebra task. This section carries it
out as far as the current source papers allow. The output is deliberately
finite and operational: every new coordinate is a declared scalar record of
the same pushed-forward `SEL2` law. Nothing here reconstructs a hidden
continuum gauge field, imports an area law, or changes the record law after
the fact.

The result is mixed but useful. The bounded-collar trace quotient can be
instantiated, and stagnant/channel cycles inside a fixed collar can be
rewritten exactly into a finite local trace algebra. The reduced automaton
and its constants are then finite-table objects. What is still not supplied by
Papers 10--14, 20, or the earlier parts of Paper 21 is the all-depth
same-record reduced escape source and the all-depth reduced inverse bound.

### Definition 75.1: The Active Bounded Collar \(Y_{61}^{BTQ}\)

Let \(Y_{61}^{seed}\) be the union of supports of the seed records in
\(\mathcal B_{61,j}^{(0)}\), including the active \(2\times2\) sheet, the
`ID/proj` Paper-14 scalar records, and the dynamic \(X_{13}\) records from
Definition 61.1.

Let \(r_A\) be the local action range in plaquette-collar distance, as in
Paper 14 Theorem 23.7. Define the bounded-collar radius

```math
R_{BTQ}^{61}:=2r_A+2.
```

The bounded collar is

```math
Y_{61}^{BTQ}:=\operatorname{Col}_{R_{BTQ}^{61}}(Y_{61}^{seed}).
```

This choice is intentionally conservative. A stagnant or channel transition
which is generated by one Schwinger-Dyson/Casimir step from a record already
inside the seed collar, and which does not escape in the sense of Definition
74.8, remains inside \(Y_{61}^{BTQ}\) after retractions and lower-shell
deletions. If the active stencil later proves a smaller invariant collar, the
same construction may be rerun with that smaller radius.

For an explicit hypercubic upper bound, enclose the \(2\times2\) sheet in the
box with vertex side lengths

```math
n_1=n_2=3+2R_{BTQ}^{61},
\qquad
n_3=n_4=1+2R_{BTQ}^{61}.
```

Let

```math
v_{BTQ}^{61}:=\prod_{\mu=1}^4 n_\mu,
\qquad
q_{BTQ}^{61}:=
\sum_{\mu=1}^4 (n_\mu-1)\prod_{\nu\ne\mu}n_\nu .
```

Here \(q_{BTQ}^{61}\) is the number of positively oriented link variables in
the enclosing box. The actual collar may have fewer links; all bounds below
remain valid with \(q(Y_{61}^{BTQ})\le q_{BTQ}^{61}\).

### Definition 75.2: Local Tree Gauge And Cycle Variables

Fix a rooted spanning tree \(\tau_Y\) of the connected finite graph underlying
\(Y=Y_{61}^{BTQ}\). For every oriented link \(e\notin\tau_Y\), let
\(H_e\in SU(N)\) be the based cycle holonomy obtained by following the tree
from the root to \(s(e)\), traversing \(e\), and returning to the root along
the tree from \(t(e)\).

Let

```math
m_Y:=|E_Y^+|-|V_Y|+1
```

be the first Betti number of the collar graph, where \(E_Y^+\) is the set of
positively oriented links. Enumerate the cycle variables as

```math
H_1,\ldots,H_{m_Y}.
```

The tree gauge is only a finite coordinate device. Scalar closed Wilson-loop
records are invariant under the original local gauge action and become
simultaneous-conjugation invariant functions of the finite tuple
\((H_1,\ldots,H_{m_Y})\). No charged endpoint or gauge-frame record is erased:
if such a record is present, it must be declared separately and is not
absorbed into this scalar quotient.

### Definition 75.3: The Instantiated Trace Quotient

Let \(\mathsf A_Y\) be the alphabet

```math
\mathsf A_Y:=\{H_1,H_1^{-1},\ldots,H_{m_Y},H_{m_Y}^{-1}\}.
```

Let \(\mathsf W_{\le N^2}(Y)\) be the set of reduced words in this alphabet of
length at most \(N^2\), modulo cyclic rotation and the paired-real convention
\(w\sim w^{-1}\) whenever the active scalar battery stores real central
records.

Define

```math
\mathcal G_{N,Y}^{BTQ}
:=
\left\{
\operatorname{Re}\operatorname{tr}_{\bf N}(w),
\operatorname{Im}\operatorname{tr}_{\bf N}(w)
:\, w\in\mathsf W_{\le N^2}(Y)
\right\},
```

with the imaginary generators deleted when the paired-real convention stores
only the real class coordinate. The bounded-collar trace quotient is the
finite algebra

```math
\mathcal T_{N,Y}^{loc}
:=
\mathbb R[\mathcal G_{N,Y}^{BTQ}]
/
\mathcal I_{N,Y}^{CH/PR},
```

where \(\mathcal I_{N,Y}^{CH/PR}\) is generated by determinant-one,
Cayley-Hamilton, cyclic trace, conjugation, and Procesi-Razmyslov trace
relations for simultaneous conjugation of a finite tuple of `SU(N)` matrices.

A crude generator-count bound is

```math
G_{BTQ}^{61}
\le
2\sum_{\ell=1}^{N^2}(2m_Y)^\ell
```

with the prefactor \(2\) replaced by \(1\) on a purely real paired-character
battery.

### Lemma 75.4: \(\mathcal T_{N,Y}^{loc}\) Represents All Bounded-Collar Scalar Records

Every scalar closed Wilson-loop or finite-product character record supported
inside \(Y\), with representation labels inside the active finite cutoff
\(\Lambda_*\) and product degree inside the active cutoff \(D\), is an element
of the finite algebra \(\mathcal T_{N,Y}^{loc}\).

Proof.

Tree gauge identifies the finite local gauge quotient for scalar closed
records with simultaneous conjugation of the finite tuple
\((H_1,\ldots,H_{m_Y})\). By the Procesi-Razmyslov finite generation theorem
for matrix invariants, the invariant polynomial algebra of this tuple is
generated by traces of words of length at most \(N^2\), modulo the trace
relations listed in Definition 75.3. A character in any fixed finite
irreducible representation is a universal polynomial in fundamental traces
of powers, by the Weyl character formula and Newton identities, with
determinant one imposed for `SU(N)`. Finite products up to degree \(D\) stay
inside the same polynomial algebra. Thus every retained bounded-collar scalar
record has a representative in \(\mathcal T_{N,Y}^{loc}\). `square`

### Definition 75.5: Rewrite Polynomials And Their Coefficient Norm

For each bounded-collar scalar primitive record \(F\) retained by the common
\(E_{14}/X_{13}\) tower, fix once and for all a normal-form polynomial

```math
\mathfrak p_F
\in
\mathbb R[\mathcal G_{N,Y}^{BTQ}]
```

representing \(F\) in \(\mathcal T_{N,Y}^{loc}\). Define the finite rewrite
norm

```math
B_{BTQ}^{61}
:=
\max_F \|\mathfrak p_F\|_{\ell^1},
```

where \(F\) ranges over the bounded-collar stagnant/channel primitive records
appearing in the active finite transition alphabet and over the finite exit
records obtained from them by one identity step.

This maximum is finite by Lemma 75.4 and Paper 14 Theorem 23.7. Its numerical
value is not supplied by the current corpus because the active action
coefficient table, representation cutoff, and chosen trace normal form have
not been tabulated.

### Theorem 75.6: Stagnant-Cycle Rewrite Identities

Every stagnant or channel-growth strongly connected component of
\(\mathfrak A_{61}\) supported in \(Y_{61}^{BTQ}\) rewrites exactly into the
declared finite algebra \(\mathcal T_{N,Y}^{loc}\). Consequently it contributes
no forced-tail depth after `BTQ`; it contributes only finite same-shell
coordinates and finite rewrite coefficients bounded by \(B_{BTQ}^{61}\).

Proof.

A stagnant/channel path stays inside \(Y_{61}^{BTQ}\) by definition of the
bounded component. Each primitive record along the path is a scalar closed
Wilson-loop, character, local action-density, or finite product thereof with
labels inside the active row cutoffs. Lemma 75.4 rewrites each such record as
a polynomial in the declared finite generator list. Iterating the path may
increase raw word length, as in \( \operatorname{Tr}(A(\partial p)^mB)\), but
it does not create a new scalar coordinate outside
\(\mathcal T_{N,Y}^{loc}\): long words are reduced by the finite trace
relations in \(\mathcal I_{N,Y}^{CH/PR}\). Therefore the whole strongly
connected component is represented by finitely many declared scalar records.

This is not a probabilistic decay estimate. It is an exact finite algebra
identity inside the same pushed-forward law. `square`

### Definition 75.7: Contracted `BTQ` Automaton

Let \(\mathfrak S_{bc}\) be the finite set of bounded-collar stagnant/channel
strongly connected components of \(\mathfrak A_{61}\) supported in
\(Y_{61}^{BTQ}\). Define the quotient map

```math
\pi_{BTQ}:V(\mathfrak A_{61})\to
V(\overline{\mathfrak A}_{61}^{BTQ})
```

by sending every \(S\in\mathfrak S_{bc}\) to one trace-state vertex
\([S]_{BTQ}\), deleting internal edges of \(S\), retaining retraction edges as
lower-shell edges, and retaining only external edges leaving \(S\) or entering
\(S\).

The reduced automaton is

```math
\overline{\mathfrak A}_{61}^{BTQ}
:=
\pi_{BTQ}(\mathfrak A_{61}).
```

The reduced forced depth \(\overline K\) counts only non-retracting edges of
\(\overline{\mathfrak A}_{61}^{BTQ}\) which are not internal bounded-collar
trace rewrites. Equivalently, it counts `esc` edges and any non-bounded
channel transition not covered by \(\mathcal T_{N,Y}^{loc}\).

### Lemma 75.8: The Contracted Automaton Is A Same-Record Finite Object

For fixed \(N\), \(r_A\), action stencil, representation cutoff, degree
cutoff, and collar \(Y_{61}^{BTQ}\), the quotient automaton
\(\overline{\mathfrak A}_{61}^{BTQ}\) has finite local transition alphabet and
is built from scalar records of the same `SEL2` pushed-forward law.

Proof.

Finiteness of the raw local transition alphabet is Lemma 74.2. The quotient
replaces each bounded-collar stagnant/channel component by a finite trace
state whose coordinates are the generators of \(\mathcal T_{N,Y}^{loc}\) and
their retained finite monomials. Lemma 75.4 and Theorem 75.6 show that these
coordinates are declared scalar records, not hidden variables. Contracting a
finite set of local component types and retaining their external finite
transition types preserves finiteness. `square`

### Definition 75.9: Reduced Branching And Coefficient Constants

For \(\bar v\in V(\overline{\mathfrak A}_{61}^{BTQ})\), let
\(\operatorname{Out}_{esc}(\bar v)\) be the set of reduced non-retracting
external edges that increase \(\overline K\). Define

```math
C_{geom}^{red}
:=
\max_{\bar v}
\#\operatorname{Out}_{esc}(\bar v).
```

Thus

```math
C_{geom}^{red}
\le
C_{geom}(4,r_A,A_{stencil}),
```

the one-step Paper-14 branching constant, and the inequality may be strict
because bounded stagnant/channel loops have been contracted.

Let \(a_e\) be the absolute projected identity coefficient of a reduced
escaping edge after inserting the `BTQ` rewrite polynomials for its bounded
source/target component. Define

```math
A_{esc}^{BTQ}
:=
\max_{e\in E_{esc}(\overline{\mathfrak A}_{61}^{BTQ})}
\max(1,|a_e|),
```

and set

```math
g_c^{red}:=\log A_{esc}^{BTQ},
\qquad
C_c^{red}:=C_{seed}^{61}B_{BTQ}^{61}.
```

Then any reduced primitive path of depth \(\overline K\) has coefficient
bounded by

```math
|c_f^{red}|
\le
C_c^{red}\exp(g_c^{red}\overline K).
```

This is the requested computation of \(C_{geom}^{red}\) and \(g_c^{red}\):
they are explicit finite maxima over the contracted transition table. The
current papers do not provide the numerical table, so no numerical value is
licensed.

### Theorem 75.10: Reduced Branching And Coefficient Bound

With Definitions 75.7 and 75.9,

```math
N_{\overline K}^{red}
\le
N_0^{red}(C_{geom}^{red})^{\overline K},
\qquad
|c_f^{red}|
\le
C_c^{red}e^{g_c^{red}\overline K}.
```

Proof.

At each reduced depth increment, a path chooses one external non-retracting
edge counted by \(\operatorname{Out}_{esc}\). Hence the number of reduced
primitive path types grows at most by \(C_{geom}^{red}\) per reduced step,
up to the finite initial factor \(N_0^{red}\). For coefficients, each reduced
escaping edge contributes at most \(A_{esc}^{BTQ}\), while bounded-collar
rewrites contribute only the finite normal-form factor absorbed into
\(C_c^{red}\). Multiplying over \(\overline K\) reduced steps gives the
displayed coefficient bound. `square`

### Definition 75.11: Reduced Inverse-Growth Constant \(g_q\)

For the retained shell matrix of the reduced automaton, write

```math
M_{61,\overline K}^{red}
=
D_{61,\overline K}^{red}
+O_{61,\overline K}^{red}.
```

Here \(D\) is the Casimir diagonal on retained nontrivial primitive-channel
coordinates and \(O\) contains same-shell off-diagonal couplings after the
`BTQ` rewrite. Define

```math
\kappa_{\min}^{red}
:=
\inf_{\overline K}
\min_{\alpha\in F_{\overline K}^{red}}
C_2(\mu_\alpha),
```

after deleting trivial/lower-shell coordinates. On the fundamental `SU(N)`
branch,

```math
\kappa_{\min}^{red}\ge C_{\rm fund}(N)
={N^2-1\over 2N}.
```

Let

```math
\Omega_{\overline K}^{red}
:=
\|O_{61,\overline K}^{red}\|_{\infty\to\infty}.
```

If there is a uniform diagonal-dominance margin

```math
\Omega_*^{red}:=\sup_{\overline K}\Omega_{\overline K}^{red}
<
\kappa_{\min}^{red},
```

then choose

```math
C_q^{red}:={1\over \kappa_{\min}^{red}-\Omega_*^{red}},
\qquad
g_q:=0.
```

Without that margin, the only honest all-depth definition is the carried
limsup

```math
g_q^{car}
:=
\limsup_{\overline K\to\infty}
{1\over\overline K}
\log^+\|Q_{61,\overline K}^{red}\|,
```

where \(Q_{61,\overline K}^{red}\) is a certified right inverse on the
constrained physical shell range.

### Theorem 75.12: What Is Actually Computed For \(g_q\)

The `BTQ` contraction computes \(g_q=0\) **if and only if** the reduced
all-depth Casimir diagonal-dominance source

```math
\mathrm{P21\text{-}RED\text{-}CMSSI}
:\quad
\sup_{\overline K}\Omega_{\overline K}^{red}
<
\kappa_{\min}^{red}
```

is proved, or an equivalent all-depth right-inverse certificate gives
uniformly bounded \(\|Q_{61,\overline K}^{red}\|\). Otherwise \(g_q\) must be
carried as \(g_q^{car}\).

Proof.

The Neumann-series/right-inverse estimate gives

```math
\|(D+O)^{-1}\|_{\infty\to\infty}
\le
{1\over \kappa_{\min}^{red}-\Omega_*^{red}}
```

under the displayed strict margin. This is the all-depth version of the
shell-2 estimate in Theorem 73.8 and the `SSI` requirement of Paper 14
Definition 28.6. If the margin is not proved, Paper 14 allows shell inverse
growth to be part of the summability budget; the correct exponent is exactly
the displayed limsup. `square`

### Theorem 75.13: `BTQ` Execution Verdict

The six requested operations have the following rigorous status.

1. **Instantiate \(\mathcal T_{N,Y}^{loc}\).** Done in Definitions 75.1--75.3.
   The explicit generator bound is

   ```math
   G_{BTQ}^{61}
   \le
   2\sum_{\ell=1}^{N^2}(2m_Y)^\ell,
   \qquad
   m_Y=|E_Y^+|-|V_Y|+1.
   ```

2. **Prove stagnant-cycle rewrites.** Done in Lemma 75.4 and Theorem 75.6,
   using finite invariant trace generation. Bounded-collar cycles are exact
   finite scalar records after `BTQ`, not forced-tail depth.
3. **Contract the quotient automaton.** Done in Definition 75.7 and Lemma
   75.8.
4. **Compute \(C_{geom}^{red}\).** Done as the finite maximum

   ```math
   C_{geom}^{red}
   =
   \max_{\bar v}\#\operatorname{Out}_{esc}(\bar v)
   \le C_{geom}(4,r_A,A_{stencil}).
   ```

5. **Compute \(g_c^{red}\).** Done as

   ```math
   g_c^{red}=\log A_{esc}^{BTQ},
   ```

   with \(A_{esc}^{BTQ}\) the finite maximum of absolute reduced escaping-edge
   coefficients after `BTQ` rewrite.
6. **Compute \(g_q\).** The shell-2 prototype supports the Casimir-row route,
   but the all-depth value is

   ```math
   g_q=0
   ```

   only under `P21-RED-CMSSI`; otherwise it is the carried limsup
   \(g_q^{car}\) of Definition 75.11.

Therefore the bounded-collar obstruction from Section 74 is removed as a
finite-algebra obstruction, but the common \(E_{14}/X_{13}\) bypass is still
not closed. The remaining source gate is now sharper:

```math
\mathrm{P21\text{-}FTS\text{-}REDESC}
+
\mathrm{P21\text{-}AF\text{-}COL\text{-}SRC}
+
\mathrm{P21\text{-}RED\text{-}CMSSI}
```

with the pass inequality

```math
m_{red}>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q.
```

If `P21-RED-CMSSI` holds, the last term is zero. If it does not, the branch
must carry \(g_q^{car}\) and test the stricter inequality with
\(g_q^{car}\).

Proof.

Items 1--3 are Definitions 75.1--75.7 and Theorem 75.6. Items 4--5 are
Definitions 75.9 and Theorem 75.10. Item 6 is Definition 75.11 and Theorem
75.12. The final inequality is Theorem 74.9 with the computed values of
\(C_{geom}^{red}\), \(g_c^{red}\), and \(g_q\). Papers 10--11 license the
finite same-record discipline and forbid treating this as a hidden continuum
gauge reconstruction; Paper 14 supplies the forced-tower and shell-inverse
criteria but not the remaining all-depth source. `square`

## 76. Finite-Generator Versus Finite-Battery: The `BTQ` Degree Leak

Section 75 instantiates the bounded-collar trace quotient. There is one more
honesty check before it can be used as a finite-battery `BLU` closure. A
finitely generated invariant trace algebra is not automatically a finite
scalar battery. The generators are finite, but arbitrary stagnant cycles can
produce polynomials of unbounded degree in those generators.

This distinction matters. Barandes-aligned record bookkeeping allows us to
declare the finite generator variables, but it does not allow us to silently
replace all moments of those variables by a finite list of scalar records.
Either the full local generator law is declared as a finite-dimensional
observable law, or high-degree generator moments must be controlled by a new
tail estimate.

### Lemma 76.1: Bounded-Collar Trace Rewriting Has Unbounded Polynomial Degree

The `BTQ` rewrite of bounded-collar stagnant cycles has no uniform polynomial
degree bound in general.

Proof.

Already for `SU(2)` and one cycle holonomy \(g\), the closed-loop records

```math
T_m(g):=\operatorname{tr}(g^m)
```

are supported in one fixed bounded collar. If

```math
x:=\operatorname{tr}(g),
```

then

```math
T_m(g)=2\,\mathsf T_m(x/2),
```

where \(\mathsf T_m\) is the Chebyshev polynomial of degree \(m\). Thus the
record is a polynomial in the single trace generator \(x\), but the polynomial
degree grows with \(m\). The same phenomenon persists for `SU(N)` by
Cayley-Hamilton recurrences: the word can be reduced to finitely many trace
generators, but the coefficients are polynomials in those generators with
degree growing along the stagnant cycle. `square`

### Definition 76.2: The `BTQ` Finite-Battery Closure Fork

The bounded-collar trace quotient supports a finite-battery bypass only under
one of the following extra gates.

1. **Full local generator law gate**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}FULLLAW}.
   ```

   The finite random vector

   ```math
   G_{BTQ}:=(G_1,\ldots,G_M),
   \qquad M:=G_{BTQ}^{61},
   ```

   of trace generators in Definition 75.3 is itself declared as a local
   operational record with its full pushed-forward law. Then every bounded
   stagnant-cycle scalar record is a measurable function of one declared
   finite-dimensional local record. This is finite-dimensional but not a
   finite scalar moment battery.

2. **Degree-tail gate**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}DEGTAIL}(D_j,\epsilon_j).
   ```

   The finite scalar battery retains all generator monomials of degree at
   most \(D_j\), with \(D_j\to\infty\), and the discarded high-degree part of
   every bounded-collar stagnant component has same-record tail

   ```math
   T_{BTQ,deg}(D_j)\le \epsilon_j,
   \qquad
   \epsilon_j\to0.
   ```

3. **Uniform degree bound gate**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}UDEG}(D_*).
   ```

   Every stagnant/channel component needed by the common \(E_{14}/X_{13}\)
   tower rewrites into generator polynomials of degree at most \(D_*\).

Lemma 76.1 shows that `UDEG` is false for the raw bounded-collar word-power
cycle unless the cycle is removed by an additional identity or selector.

### Theorem 76.3: Corrected Meaning Of The `BTQ` Contraction

The contraction in Section 75 is an exact finite-generator contraction. It is
a finite-battery contraction only under `P21-BTQ-FULLLAW`,
`P21-BTQ-DEGTAIL`, or a separately proved non-raw `P21-BTQ-UDEG`.

Proof.

Theorem 75.6 proves that bounded-collar stagnant records are functions of the
finite generator list. Lemma 76.1 proves that the degree of those functions is
not uniformly bounded on the raw stagnant cycle tower. A finite scalar battery
with fixed degree cutoff therefore cannot contain all such functions. The
three gates in Definition 76.2 are exactly the remaining ways to make the
contraction operational: declare the full finite-dimensional generator law,
send the degree cutoff to infinity with a controlled tail, or prove that the
active quotient has a true uniform degree bound after extra identities.
`square`

### Definition 76.4: Reduced Constants With Degree Accounting

Under `P21-BTQ-FULLLAW`, the reduced constants from Section 75 are unchanged:

```math
C_{geom}^{red}
=
\max_{\bar v}\#\operatorname{Out}_{esc}(\bar v),
\qquad
g_c^{red}=\log A_{esc}^{BTQ},
```

and \(g_q\) is decided by `P21-RED-CMSSI` as in Definition 75.11.

Under `P21-BTQ-DEGTAIL(D_j,\epsilon_j)`, define the degree-tail exponent

```math
m_{deg}^{BTQ}
:=
\liminf_{\overline K\to\infty}
{-1\over \overline K}
\log T_{BTQ,deg}(D_j(\overline K)).
```

The reduced forced-tail source must then use

```math
m_{red}^{eff}
:=
\min(m_{red},m_{deg}^{BTQ})
```

in place of \(m_{red}\).

### Theorem 76.5: Final `BTQ` Pass Inequality After The Degree Audit

The common \(E_{14}/X_{13}\) bypass can use the bounded-collar trace quotient
only if one of the `BTQ` finite-battery closure gates is supplied. The final
pass test is:

1. under `P21-BTQ-FULLLAW`,

   ```math
   m_{red}>
   \log A_{esc}^{BTQ}
   +\log C_{geom}^{red}
   +g_q;
   ```

2. under `P21-BTQ-DEGTAIL`,

   ```math
   m_{red}^{eff}>
   \log A_{esc}^{BTQ}
   +\log C_{geom}^{red}
   +g_q
   +g_{bat}^{BTQ};
   ```

3. under a genuine non-raw `P21-BTQ-UDEG`, the same inequality as in item 1
   applies with the finite degree bound included in \(B_{BTQ}^{61}\).

If none of these gates is proved, the Section-75 quotient is not enough for
finite-battery `BLU`. The common bypass remains parked and the worksheet must
continue to carry

```math
E_{14}^{park}+X_{13}^{(26),SEL2}.
```

Proof.

Theorem 74.9 gives the reduced forced-depth pass inequality once the bounded
collar has been eliminated from the tail tower. Section 75 eliminates it only
at finite-generator level. Definition 76.2 supplies the extra operational
gate needed to make that elimination legitimate for finite scalar batteries.
If the full generator law is declared, there is no scalar degree tail. If only
finite moments are declared, the degree tail is an additional discarded tail,
so the available decay exponent is the minimum of the reduced escape decay
and the degree-tail decay, and Section 80 shows that the growing scalar
moment battery contributes the additional surcharge \(g_{bat}^{BTQ}\). If no
gate is supplied, Lemma 76.1 gives explicit bounded-collar records whose
degree escapes every fixed finite battery.
`square`

### Corollary 76.6: What Is Settled For Good

The bounded-collar problem is now split into two precise facts.

1. The **raw physical-distance escape route is dead**: Section 74 proves that
   raw forced depth can grow inside a bounded collar.
2. The **finite-generator quotient is real but insufficient by itself**:
   Section 75 constructs it, while Lemma 76.1 proves that finite-generator
   rewriting does not automatically give finite-battery `BLU`.

Therefore the next executable decision is not another generic trace-quotient
argument. It is one of:

```math
\mathrm{P21\text{-}BTQ\text{-}FULLLAW},
\qquad
\mathrm{P21\text{-}BTQ\text{-}DEGTAIL},
\qquad
\mathrm{P21\text{-}BTQ\text{-}UDEG}
\text{ after a new selector/identity.}
```

Absent one of these, \(E_{14}^{park}+X_{13}^{(26),SEL2}\) remains carried.

## 77. Attacking `BTQ-DEGTAIL`: Why Moment Truncation Is Not Yet A Source

Section 76 isolates the finite-generator-to-finite-battery gap. This section
tests the most tempting way to close it: keep scalar moments of the finite
trace generators up to degree \(D_j\), prove a degree tail, and let
\(D_j\to\infty\).

The conclusion is sharp. The current corpus supports finite trace generators,
finite Peter-Weyl batteries, bounded Wilson-loop compactness, and local RG
tails for declared finite batteries. It does **not** support a uniform
high-degree moment tail for the bounded-collar trace-generator algebra on the
active `SEL2` law. Therefore `BTQ-DEGTAIL` is a real new source theorem, not a
consequence of Sections 75--76.

### Definition 77.1: Scalar Moment Truncation Of The `BTQ` Generator Law

Let

```math
G_{BTQ}=(G_1,\ldots,G_M),
\qquad M:=G_{BTQ}^{61},
```

be the finite trace-generator vector from Definition 75.3. Since each
generator is a trace of an `SU(N)` word, after normalization it is uniformly
bounded:

```math
|G_a|\le 1.
```

For \(D\ge0\), define the scalar moment battery

```math
\mathcal M_D(G_{BTQ})
:=
\{G^\alpha:\ |\alpha|\le D\}.
```

The scalar degree-tail gate is the assertion that there are \(D_j\to\infty\),
\(\epsilon_j\to0\), and a declared projection/truncation rule
\(\Pi_{\le D_j}^{BTQ}\), independent of the unknown expectation values of the
active law, such that every bounded-collar stagnant record \(F\) needed by the
common \(E_{14}/X_{13}\) tower has
\(\Pi_{\le D_j}^{BTQ}F\in\operatorname{span}\mathcal M_{D_j}(G_{BTQ})\) and

```math
\left|
\int (F-\Pi_{\le D_j}^{BTQ}F)\,d\nu_j^{SEL2}
\right|
\le \epsilon_j,
```

uniformly over the stagnant records discarded by the finite-battery
truncation. The projection rule may be algebraic, Peter-Weyl/Sobolev, or
orthogonal relative to a declared reference measure; it may not choose a
constant equal to the unknown target expectation.

### Lemma 77.2: Compactness Gives Subsequence Limits, Not A Degree Rate

Paper 10's finite Peter-Weyl/projective machinery and Paper 11's bounded
countable Wilson-loop compactness do not imply Definition 77.1 with a
quantitative \(\epsilon_j\).

Proof.

Paper 10 proves finite Peter-Weyl batteries and exact finite-battery
pushforward identities, but it treats cofinal continuum compatibility,
tightness, and uniqueness as additional hypotheses. Paper 11 gives diagonal
compactness for countable bounded Wilson-loop tests and finite-battery local
RG residual estimates when a local expansion tail is supplied. Neither
statement supplies a uniform approximation rate for all high-degree
polynomials in the local trace generators. Compactness gives subsequential
limits of fixed tested records; it does not say how fast the expectation of
records outside a growing degree cutoff tends to the finite-degree span.
`square`

### Lemma 77.3: Uniform Degree Tail Is False Without Extra Regularity

There is no purely compact-group, law-independent finite-generator estimate of
the form

```math
\sup_m
\inf_{\deg P\le D}
\|T_m-P\|_\infty
\to0
```

and hence no state-uniform expectation tail valid for all probability laws
\(\nu\) on the local generator space.

Proof.

Take the `SU(2)` one-cycle example from Lemma 76.1:

```math
T_m(g)=2\mathsf T_m(x/2),
\qquad x=\operatorname{tr}(g).
```

For every polynomial \(P\) of degree \(D<m\), consider the \(m+1\) alternating
extrema of \(\mathsf T_m\) on \([-1,1]\). If
\(\|\mathsf T_m-P\|_\infty<1/2\), then \(P\) must alternate sign between
successive extrema and therefore has at least \(m\) distinct zeros, impossible
for degree \(D<m\). Thus

```math
\inf_{\deg P\le D}\|\mathsf T_m-P\|_\infty\ge {1\over2}
\qquad(D<m).
```

Taking \(\nu\) to be a Dirac law at a point where the residual has absolute
value at least \(1/2\) shows that any law-independent projection rule has a
state for which the expectation error is at least \(1/2\). Thus finite
generator compactness alone cannot produce a uniform degree tail over all
possible local laws. `square`

### Definition 77.4: Actual Source Gates For `BTQ-DEGTAIL`

The degree-tail route is licensed only by one of the following same-record
regularity sources.

1. **Peter-Weyl/Sobolev local density source**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}PWREG}(s,R).
   ```

   The local `BTQ` generator law has a density whose Peter-Weyl coefficients
   satisfy

   ```math
   \sum_{\lambda}
   (1+C_2(\lambda))^s
   d_\lambda\,|\widehat K_{\lambda,j}|^2
   \le R^2
   ```

   cofinally on the same `SEL2` law.

2. **Heat-kernel smoothing source**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}HKSM}(t_*,R).
   ```

   The local generator law is a heat-kernel-smeared law with effective time
   \(t_*>0\) after all `SEL2` pushforwards and counterterms, giving

   ```math
   |\widehat K_{\lambda,j}|
   \le
   R e^{-t_*C_2(\lambda)/2}.
   ```

3. **Polynomial moment determinacy plus quantitative orthogonal tail**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}ORTH}(D_j,\epsilon_j).
   ```

   The orthogonal projection of every stagnant-cycle record to
   \(\operatorname{span}\mathcal M_{D_j}(G_{BTQ})\) has expectation error at
   most \(\epsilon_j\).

These are regularity/tail hypotheses about the local `BTQ` law. They are not
area-law, mass-gap, or confinement hypotheses, but they are also not supplied
by compactness alone.

### Theorem 77.5: Degree-Tail Pass Bound Under A Sobolev Source

Assume `P21-BTQ-PWREG(s,R)` and let \(d_{loc}\) be the dimension of the
compact local generator manifold after gauge quotient. If \(s>d_{loc}/2\),
then there is a constant \(C_{s,N,Y}\) such that the degree-tail error obeys

```math
T_{BTQ,deg}(D)
\le
C_{s,N,Y}R\,D^{-(s-d_{loc}/2)}.
```

Consequently a schedule \(D(\overline K)=\exp(\beta\overline K)\) gives

```math
m_{deg}^{BTQ}
\ge
\beta(s-d_{loc}/2).
```

Proof.

On a compact Lie-group quotient, Peter-Weyl/Sobolev regularity controls the
tail of the Fourier expansion by the standard spectral counting estimate.
The number of modes with Casimir at most \(L^2\) grows like \(L^{d_{loc}}\).
Cauchy-Schwarz then bounds the omitted high-Casimir tail by
\(D^{-(s-d_{loc}/2)}\), after translating the trace-polynomial degree cutoff
to a finite Peter-Weyl cutoff by the representation-product rules. Taking
\(D(\overline K)=e^{\beta\overline K}\) gives the displayed exponent. `square`

The cost is that the moment battery size grows like

```math
\#\mathcal M_{D(\overline K)}(G_{BTQ})
\le
\binom{M+D(\overline K)}{M},
```

so exponential \(D(\overline K)\) is not a harmless finite-battery operation:
it can feed into the shell-inverse and projection constants. Thus the
Sobolev route must be paired with `CMSSI` on the enlarged moment batteries.

### Theorem 77.6: Current Verdict For `BTQ-DEGTAIL`

The current Papers 10--12, 14, 20, and 21 do not prove
`P21-BTQ-DEGTAIL`.

Proof.

Paper 10 supplies finite Peter-Weyl batteries and exact finite-battery
pushforwards, but not a cofinal high-degree trace-generator tail. Paper 11
supplies local RG residual tails for declared finite batteries and conditional
AF polymer margins; it does not prove the local `BTQ` Sobolev or heat-kernel
regularity source in Definition 77.4 on the active `SEL2` law. Paper 12
controls renormalized Wilson-loop records on finite admissible batteries and
loop-continuity under explicit moduli, but not the full high-degree
bounded-collar trace-generator tail. Paper 14 says such a tail would imply
`FTS`, but does not prove it. Therefore `BTQ-DEGTAIL` remains an explicit new
source theorem. `square`

## 78. Reduced Escape: Linear Distance Fails, Polymer Size Is The Honest Replacement

Section 74 defined `REDESC` as a linear collar-distance source after `BTQ`.
Section 77 shows that bounded-collar degree cycles cannot be silently
discarded by finite scalar moments. This section tests the geometric part.

The verdict is again sharper than a simple no. Linear distance in the reduced
depth is too strong for a four-dimensional local forced tower. The replacement
should be a reduced polymer-size/KP source: forced depth should buy connected
polymer size, not necessarily linear distance from the original sheet.

### Definition 78.1: Reduced Support Polymer

After applying the `BTQ` quotient and a chosen finite-battery closure gate from
Definition 76.2, associate to each reduced primitive forced record \(f\) a
connected coarse plaquette polymer

```math
X_f^{red}
```

equal to the union of coarse plaquettes and local action stencils touched by
the non-`BTQ` escaping transitions in a reduced generating path. Let
\(|X_f^{red}|\) be its cardinality and \(\operatorname{diam}X_f^{red}\) its
collar graph diameter.

### Lemma 78.2: Linear Reduced Distance Is Not Forced By Locality

The gate `P21-FTS-REDESC(c_d)` is not a consequence of the finite local
transition rules.

Proof.

One reduced escaping transition changes support by only a bounded local
collar, by Paper 14 Theorem 23.7. A path may add plaquettes in a connected
cluster that fills a ball of radius \(R\) around the seed before moving
farther away. Such a path has reduced transition count comparable to the
volume of the ball, \(O(R^4)\), while the collar distance from the seed is
only \(O(R)\). Hence there is no local-combinatorial lower bound
\(\operatorname{dist}_{col}\ge c\,\overline K\). At best, locality alone gives
a sublinear distance lower bound after imposing additional self-avoidance or
growth restrictions, and even that requires an explicit path constraint.
`square`

This does not falsify forced-tail decay. It falsifies the attempt to obtain it
from linear physical distance alone.

### Definition 78.3: Reduced KP/Polymer-Size Source

Replace `REDESC` by the gate

```math
\mathrm{P21\text{-}FTS\text{-}REDKP}(\mu_{red},\alpha_{red}).
```

It asserts that the same `SEL2` pushed-forward law admits a connected-polymer
expansion for reduced forced records such that

```math
\sum_{\Gamma\ \mathrm{touching}\ X_f^{red}}
|z_\Gamma|\,
e^{\alpha_{red}|\Gamma|}
\le
C_{KP}^{red}
e^{-\mu_{red}|X_f^{red}|}.
```

The required geometric bridge is not distance but size:

```math
|X_f^{red}|
\ge
c_{size}\,\overline K(f)
```

after all bounded-collar cycles have been handled by `BTQ` and after all
finite-generator-to-finite-battery degree tails are accounted for.

### Lemma 78.4: Size Growth Is The Right Automaton Test

If the reduced automaton has no non-`BTQ` strongly connected component whose
external transitions preserve \(X_f^{red}\), then there is
\(c_{size}>0\) such that

```math
|X_f^{red}|\ge c_{size}\overline K(f).
```

Proof.

After `BTQ`, every bounded-collar stagnant/channel SCC is contracted. If no
remaining non-`BTQ` SCC can cycle without enlarging \(X_f^{red}\), then each
block of at most \(L_{rep}\) reduced transitions must add at least one new
plaquette/stencil cell to the connected support polymer, where \(L_{rep}\) is
the finite maximum length of a simple path in the quotient of the local
transition graph before support enlargement. Taking
\(c_{size}=1/L_{rep}\) gives the bound. `square`

If such a non-`BTQ` SCC exists, then either it must be added to the `BTQ`
finite-generator quotient, or it is a genuine new finite-generator leak.

### Theorem 78.5: Reduced KP Source Proves The Common Forced Tail

Assume:

1. one of the finite-battery closure gates from Definition 76.2;
2. `P21-FTS-REDKP(\mu_{red},\alpha_{red})`;
3. the size-growth condition of Lemma 78.4;
4. reduced branching and coefficient constants from Definition 75.9;
5. reduced inverse growth exponent \(g_q\) from Definition 75.11;
6. if the closure gate is `BTQ-DEGTAIL`, the degree-battery growth exponent
   \(g_{bat}^{BTQ}\) from Section 80; otherwise set \(g_{bat}^{BTQ}=0\).

Set

```math
m_{poly}^{red}:=\mu_{red}c_{size}.
```

If the closure gate is `BTQ-DEGTAIL`, set

```math
m_{eff}:=\min(m_{poly}^{red},m_{deg}^{BTQ});
```

otherwise set \(m_{eff}:=m_{poly}^{red}\). Then the common forced-tail plus
inverse-amplified shell summability passes if

```math
m_{eff}>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q
+g_{bat}^{BTQ}.
```

Proof.

The KP source gives a reduced forced-record weight bounded by
\(C e^{-\mu_{red}|X_f^{red}|}\). Lemma 78.4 converts this into
\(C e^{-m_{poly}^{red}\overline K}\). If a degree-tail route is used, the
discarded high-degree trace-generator tail supplies an additional error with
exponent \(m_{deg}^{BTQ}\), so the usable exponent is the minimum. Multiplying
by reduced branching, reduced coefficient growth, inverse amplification, and
the number of selected degree-battery scalar records gives the displayed
strict margin, exactly as in Paper 14 Theorem 26.2 and Definition 28.6, with
the battery-growth correction made explicit in Section 80. `square`

### Theorem 78.6: Source Status After The KP Pivot

The current corpus does not prove `P21-FTS-REDKP` on the active `SEL2`
common \(E_{14}/X_{13}\) tower. It does, however, identify it as the right
non-circular replacement for linear `REDESC`.

Proof.

Paper 11 contains KP/polymer mechanisms in strong-coupling heat-kernel
regimes and conditional AF local-expansion regimes. Paper 14 proves that KP
forced-polymer bounds imply `FTS`. But neither paper proves the reduced
common \(E_{14}/X_{13}\) polymer expansion and size-growth source on the
active matched `SEL2` law. Lemma 78.2 shows why ordinary linear distance is
too strong; Definition 78.3 is the source statement that matches the existing
Paper-11/Paper-14 technology without importing an area law. `square`

## 79. Weighted `CMSSI`: The Remaining Shell-Inverse Attack

The last part of the closure package is reduced shell invertibility. Raw row
sums may be too crude after the `BTQ` rewrite and polynomial degree
accounting. The right attack is a weighted norm.

### Definition 79.1: Reduced Complexity Weight

For a reduced shell coordinate \(v\), define

```math
\mathcal H(v)
:=
a_s |X_v^{red}|
+a_C C_2(\mu_v)
+a_D \deg_{BTQ}(v)
+a_R \operatorname{refl}(v),
```

with nonnegative parameters \(a_s,a_C,a_D,a_R\). Let

```math
w(v):=e^{\mathcal H(v)}.
```

For a reduced shell matrix \(M=D+O\), define the weighted off-diagonal norm

```math
\Omega_*^{red}(w)
:=
\sup_{\overline K}
\max_v
\sum_{u\ne v}
{|O_{vu}|\,w(u)\over w(v)}.
```

### Theorem 79.2: Weighted Diagonal Dominance Gives \(g_q=0\) Only For Zero-Spread Weights

If there is a weight \(w\) such that

```math
\Omega_*^{red}(w)<\kappa_{\min}^{red},
```

and the weight has zero exponential shell spread, then the reduced shell
right inverses are uniformly bounded in the unweighted norm and \(g_q=0\).
If the shell spread has exponential rate \(g_w>0\), then this argument gives
only \(g_q\le g_w\).

Proof.

In the weighted \(\ell^\infty_w\) norm,

```math
\|D^{-1}O\|_w
\le
{\Omega_*^{red}(w)\over \kappa_{\min}^{red}}
<1.
```

The Neumann series gives a uniformly bounded inverse on the constrained
physical shell range:

```math
\|Q_{\overline K}^{red}\|_w
\le
{1\over \kappa_{\min}^{red}-\Omega_*^{red}(w)}.
```

Converting from the weighted norm back to the unweighted norm costs the
oscillation of the weight on the shell.  Hence the unweighted inverse-growth
exponent is bounded by the exponential shell-spread rate \(g_w\), and is zero
when that rate is zero. `square`

### Corollary 79.3: Ordered Attack Menu Now

After the audits in Sections 77--79, the only rigorous attack sequence left is:

1. decide `BTQ-FULLLAW` versus `BTQ-DEGTAIL`; fixed finite scalar degree is
   not enough;
2. replace linear `REDESC` by `REDKP` plus the automaton size-growth test;
3. compute the reduced transition constants
   \(A_{esc}^{BTQ}\) and \(C_{geom}^{red}\) from the actual finite table;
4. search for a weighted `CMSSI` certificate
   \(\Omega_*^{red}(w)<\kappa_{\min}^{red}\);
5. compute the degree-battery growth surcharge \(g_{bat}^{BTQ}\) from
   Section 80, and test the corrected final source inequality

   ```math
   m_{eff}>
   \log A_{esc}^{BTQ}
   +\log C_{geom}^{red}
   +g_q
   +g_{bat}^{BTQ}.
   ```

If any one of items 1, 2, or 4 fails without a replacement norm or selector,
the common \(E_{14}/X_{13}\) bypass remains parked and the Paper-21 worksheet
must carry \(E_{14}^{park}+X_{13}^{(26),SEL2}\).

## 80. Battery-Growth Surcharge For The Degree-Truncated BTQ Battery

Section 79 still understated the cost of the `BTQ-DEGTAIL` route.  A
degree-truncated finite battery is not just one scalar observable: it is a
growing family of scalar records.  The Paper-14 forced-tail and SSI tests sum
over the available records in a shell, so record multiplicity is an entropy
term.  It must be charged on the same pushed-forward SEL2 law; otherwise the
finite-battery bypass silently spends a continuum amount of information while
pretending to use a fixed finite record.

This is the Barandes-aligned bookkeeping point: the hidden-variable record is
one actual record, not a sequence of after-the-fact observable choices.  If the
argument asks for more and more monomials of the BTQ generators, that growth is
part of the physical record prescription and must appear in the scalar
inequality.

### Definition 80.1: The BTQ Battery Count

Let

```math
G_{BTQ}=(G_1,\ldots,G_M)
```

be the finite generator list from Section 77.  For a degree schedule
\(D(\overline K)\), define

```math
\mathcal M_{\le D}^{BTQ}
:=
\{G^\alpha:\alpha\in{\mathbb N}^M,\ |\alpha|\le D\}.
```

The unreduced scalar battery size is

```math
B_{BTQ}(\overline K)
:=
\#\mathcal M_{\le D(\overline K)}^{BTQ}
=
{M+D(\overline K)\choose M}.
```

If the trace quotient supplies certified algebraic reductions, replace this by
the reduced count

```math
B_{BTQ}^{red}(\overline K)
:=
\#\Pi_{BTQ}^{red}\mathcal M_{\le D(\overline K)}^{BTQ}
\le
B_{BTQ}(\overline K).
```

Without a finite quotient-normal-form certificate, use the unreduced upper
bound.  Define the battery-growth exponent

```math
g_{bat}^{BTQ}
:=
\limsup_{\overline K\to\infty}
{1\over \overline K}
\log^+ B_{BTQ}^{red}(\overline K).
```

This is independent of the shell-inverse exponent \(g_q\).  The latter measures
how badly the already selected linear system is conditioned; \(g_{bat}^{BTQ}\)
measures how many scalar equations/records have been selected.

### Lemma 80.2: Schedule Values

For fixed \(M\):

1. if \(D(\overline K)=\overline K^p\), then \(g_{bat}^{BTQ}=0\);
2. if \(D(\overline K)=\exp(\beta\overline K)\), then

   ```math
   g_{bat}^{BTQ}=M\beta;
   ```

3. if \(D(\overline K)=\exp(o(\overline K))\), then
   \(g_{bat}^{BTQ}=0\).

Proof.

The count satisfies

```math
{D(\overline K)^M\over M!}
\le
{M+D(\overline K)\choose M}
\le
{(M+D(\overline K))^M\over M!}.
```

Taking \(\overline K^{-1}\log^+\) gives \(M\) times the exponential growth
rate of \(D(\overline K)\).  `square`

### Corollary 80.3: Sobolev Degree Tail Has A Hidden Entropy Cost

Assume the only available degree-tail source is the Sobolev bound from
Theorem 77.5:

```math
T_{BTQ,deg}(D)
\le
C_{s,N,Y}R\,D^{-a},
\qquad
a:=s-d_{loc}/2>0.
```

To make this tail exponentially small in the forced depth, one must choose an
exponential degree schedule \(D(\overline K)=e^{\beta\overline K}\).  Then

```math
T_{BTQ,deg}(D(\overline K))
\le
C_{s,N,Y}R\,e^{-a\beta\overline K},
```

but the scalar battery contributes

```math
g_{bat}^{BTQ}=M\beta.
```

Thus the net degree-tail margin is positive only after paying
\(M\beta\).  In particular, a Sobolev-only route cannot even make the
degree-truncation subproblem favorable unless

```math
a>M,
\qquad\text{i.e.}\qquad
s-d_{loc}/2>M,
```

before the automaton entropy, geometric multiplicity, and shell-inverse terms
are charged.

This is not a contradiction; it is the correct finite-battery accounting.  It
says that a merely algebraic regularity source must be extremely smooth to
offset the exponential number of monomials needed to extract an exponential
tail.

### Corollary 80.4: Heat-Kernel Smoothing Avoids The Battery Surcharge

If an actual same-record heat-kernel smoothing source gives

```math
T_{BTQ,deg}(D)
\le
C e^{-cD^r}
```

for some \(c,r>0\), then an exponential forced-depth tail
\(T_{BTQ,deg}(D(\overline K))\le Ce^{-m\overline K}\) is obtained by the
subexponential schedule

```math
D(\overline K)
\asymp
\left({m\over c}\overline K\right)^{1/r}.
```

Hence \(g_{bat}^{BTQ}=0\).  This is why the heat-kernel/Peter-Weyl regularity
source is structurally better than a bare Sobolev source for the BTQ bypass.
It preserves a finite-battery interpretation without exponentially many
scalar records.

### Theorem 80.5: Corrected BTQ Bypass Inequality

Let \(m_{eff}\) denote the actual forced-tail decay obtained from the reduced
escape source, the degree-tail source, and the finite algebra quotient.  The
common \(E_{14}/X_{13}\) bypass can pass only if

```math
m_{eff}>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q
+g_{bat}^{BTQ}.
```

If the inverse \(g_q\) was computed on a smaller battery than the one selected
by \(D(\overline K)\), this inequality is still incomplete: recompute \(g_q\)
on the enlarged battery or add the corresponding inverse-growth surcharge.
There is no valid route that both grows \(D(\overline K)\) and keeps using the
old fixed-battery inverse bound.

Proof.

For shell depth \(\overline K\), suppose a single selected scalar tail is
bounded by \(Ce^{-m_{eff}\overline K}\).  The reduced automaton supplies at
most \(A_{esc}^{BTQ\,\overline K}\) reduced escape strings and the local
geometry supplies the multiplicative exponential factor
\(C_{geom}^{red\,\overline K}\).  The shell inverse contributes
\(e^{(g_q+o(1))\overline K}\).  The selected BTQ scalar battery contributes
\(e^{(g_{bat}^{BTQ}+o(1))\overline K}\).  Therefore the total forced-tail sum
is bounded by

```math
C'
\exp\left(
-\left[
m_{eff}
-\log A_{esc}^{BTQ}
-\log C_{geom}^{red}
-g_q
-g_{bat}^{BTQ}
-o(1)
\right]\overline K
\right).
```

The Paper-14 forced-tail summability test requires a strictly positive
exponent.  `square`

### Status After The Surcharge

The BTQ bypass is now honest:

1. `BTQ-FULLLAW` still avoids finite degree growth, but it must be proved as a
   same-record law statement, not as an arbitrary infinite list of moments.
2. `BTQ-DEGTAIL` with only Sobolev regularity is viable only under the strong
   smoothness inequality \(s-d_{loc}/2>M\), and even then it still must beat
   the automaton, geometry, and \(g_q\) terms.
3. `BTQ-HKSM` or an equivalent Peter-Weyl exponential tail source is the
   cleanest route, because it can choose \(D(\overline K)\) subexponentially
   and hence \(g_{bat}^{BTQ}=0\).
4. Until one of these sources is actually proved on the SEL2 pushed-forward
   law, the worksheet must keep the common \(E_{14}/X_{13}\) bypass parked.

## 81. Quantitative Audit Of `BTQ-DEGTAIL`

We can now audit `BTQ-DEGTAIL` quantitatively.  The result is not a numerical
pass, because the current papers still do not tabulate the contracted BTQ
transition table, the exact generator quotient count, or a same-record
regularity exponent.  But the feasibility inequalities are now sharp enough
to falsify whole families of routes.

### Source Ledger 81.1

The audit uses only the following previously proved or explicitly parked
sources.

| Source | Imported fact | Consequence here |
|---|---|---|
| Paper 14 Definition 23.8 | forced towers require \(\sum_k N_kA_k<\infty\) | record multiplicity is an entropy term, not a free choice |
| Paper 14 Theorem 18.3 | enrichment either closes, is summable, or exposes an obstruction | a growing BTQ moment battery must be summably controlled |
| Paper 10 Definition 2A.1 | same-record projective towers require declared finite batteries and pushforward estimates | no undeclared infinite moment list may be used |
| Paper 10 Lemma 2A.3 | perfect finite blocking is exact only on a fixed finite battery | exact finite pushforward does not imply a cofinal BTQ degree tail |
| Paper 11 status item 25 | Paper 11 does not supply `P20-SEL2-TREE-RATE-GATE` | no tree-rate or area-law input may be imported |
| Paper 20 handoff | `P20-SEL2-TREE-RATE-GATE` remains parked | Paper 21 must close or falsify the scalar source directly |
| Sections 76--80 | BTQ is finite-generator, not finite-battery, unless a closure gate is proved | `BTQ-DEGTAIL` must pay \(g_{bat}^{BTQ}\) |

This source ledger is intentionally restrictive.  It prevents the audit from
using continuum Yang-Mills existence, an area law, or a mass gap as an
unstated premise.

### Definition 81.2: Quantitative Symbols

Set

```math
M:=G_{BTQ}^{61},
\qquad
G_{red}:=
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q,
```

and

```math
m_p:=m_{poly}^{red}=\mu_{red}c_{size}.
```

For a Sobolev/Peter-Weyl source, set

```math
a:=s-d_{loc}/2.
```

The active source table is therefore:

| Quantity | Current status |
|---|---|
| \(M\) | finite; crude upper bound from Definition 75.3, not numerically enumerated |
| \(d_{loc}\) | finite local quotient dimension; not numerically instantiated |
| \(a=s-d_{loc}/2\) | unsourced until `P21-BTQ-PWREG(s,R)` is proved |
| \(m_p=\mu_{red}c_{size}\) | unsourced until `P21-FTS-REDKP` and size-growth are proved |
| \(G_{red}\) | finite-table quantity; not numerically tabulated |
| \(g_{bat}^{BTQ}\) | now explicit from Section 80 once \(D(\overline K)\) is chosen |

For the collar in Definition 75.1, a safe geometric dimension bound is

```math
d_{loc}
\le
m_Y(N^2-1),
\qquad
m_Y=|E_Y^+|-|V_Y|+1.
```

The generic simultaneous-conjugation quotient may be smaller, but the current
corpus has not computed that reduction.  A pass proof may use a sharper
certified quotient dimension; a falsification audit may use this safe upper
bound only if it is enough to force failure.

### Proposition 81.3: Sobolev `BTQ-DEGTAIL` Feasibility

Assume `P21-BTQ-PWREG(s,R)` and use the exponential degree schedule

```math
D(\overline K)=e^{\beta\overline K}.
```

Then

```math
m_{deg}^{BTQ,cert}=a\beta,
\qquad
g_{bat}^{BTQ}=M\beta,
```

is the certified Sobolev exponent supplied by Theorem 77.5, and the corrected
certified pass inequality is

```math
\min(m_p,a\beta)>G_{red}+M\beta.
```

Consequently the Sobolev route can be certified by this source for some
\(\beta>0\) only if

```math
a>M
```

and, in that case, its best possible strict margin is

```math
S_{Sob}^{max}
=
m_p\left(1-{M\over a}\right)-G_{red}.
```

Thus the sharp feasibility test for the Sobolev bound as stated is

```math
a>M
\qquad\text{and}\qquad
m_p\left(1-{M\over a}\right)>G_{red}.
```

Equivalently,

```math
m_p>{a\over a-M}\,G_{red}.
```

Proof.

For \(D=e^{\beta\overline K}\), Theorem 77.5 gives
\(m_{deg}^{BTQ}\ge a\beta\), so the certified exponent is
\(m_{deg}^{BTQ,cert}=a\beta\), while Lemma 80.2 gives
\(g_{bat}^{BTQ}=M\beta\).  The corrected forced-tail inequality is therefore
\(\min(m_p,a\beta)>G_{red}+M\beta\).

If \(a\le M\), the left side grows no faster than the battery surcharge before
the intersection point and decreases relative to it after the intersection
point; with \(G_{red}\ge0\), no strict positive margin is possible.  If
\(a>M\), the margin function

```math
S_{Sob}(\beta):=\min(m_p,a\beta)-M\beta-G_{red}
```

increases on \(0<\beta<m_p/a\) and decreases on \(\beta>m_p/a\).  Its maximum
is attained at \(\beta_*=m_p/a\) and equals the displayed
\(S_{Sob}^{max}\).  `square`

### Corollary 81.4: Polynomial Degree Growth Cannot Beat Positive Entropy

If \(D(\overline K)=\overline K^p\), then \(g_{bat}^{BTQ}=0\), but the
Sobolev degree tail is only polynomial:

```math
T_{BTQ,deg}(D(\overline K))
\le
C\overline K^{-pa}.
```

Thus the exponential degree-tail exponent is \(m_{deg}^{BTQ}=0\).  This
cannot beat any positive \(G_{red}\).  A polynomial schedule is relevant only
in the degenerate case

```math
G_{red}=0
```

and then only if the polynomial summability exponent is large enough for the
underlying Paper-14 series.  That is not the active `SEL2` worksheet, where
reduced branching, coefficient growth, or inverse growth must be audited and
cannot be assumed zero.

### Proposition 81.5: Heat-Kernel Degree Tail Feasibility

Assume the stronger same-record source `P21-BTQ-HKSM(t_*,R)` gives

```math
T_{BTQ,deg}(D)\le C e^{-cD^r}
```

for some \(c,r>0\).  Choose

```math
D(\overline K)
\asymp
\left({\lambda\over c}\overline K\right)^{1/r}.
```

Then

```math
m_{deg}^{BTQ}\ge\lambda,
\qquad
g_{bat}^{BTQ}=0.
```

The heat-kernel degree route can therefore pass the degree/battery part
exactly when one can choose \(\lambda\) with

```math
\min(m_p,\lambda)>G_{red}.
```

Since \(\lambda\) is adjustable inside the tail estimate, the real obstruction
becomes

```math
m_p>G_{red},
```

plus the independent obligation to prove `P21-BTQ-HKSM(t_*,R)` on the same
`SEL2` pushed-forward law and to recompute \(g_q\) on the enlarged polynomial
degree batteries.

Proof.

The chosen \(D(\overline K)\) gives
\(T_{BTQ,deg}\le Ce^{-\lambda\overline K}\).  Its growth is polynomial in
\(\overline K\), hence subexponential, so Lemma 80.2 gives
\(g_{bat}^{BTQ}=0\).  The corrected source inequality is then
\(\min(m_p,\lambda)>G_{red}\).  `square`

### Definition 81.6: The Actual Worksheet To Fill

The quantitative audit should now be recorded by the following table, using
actual finite tables whenever they become available.

| Entry | Formula | Pass/fail use |
|---|---|---|
| Generator count | \(M=G_{BTQ}^{61}\) | controls the Sobolev surcharge \(M\beta\) |
| Local dimension | \(d_{loc}\) | controls \(a=s-d_{loc}/2\) |
| Sobolev exponent | \(a=s-d_{loc}/2\) | Sobolev route dead if \(a\le M\) |
| Reduced decay | \(m_p=\mu_{red}c_{size}\) | hard cap on usable tail rate |
| Reduced entropy | \(G_{red}=\log A_{esc}^{BTQ}+\log C_{geom}^{red}+g_q\) | must be beaten by the usable rate |
| Sobolev optimum | \(S_{Sob}^{max}=m_p(1-M/a)-G_{red}\) | pass iff positive |
| HK optimum | \(S_{HK}^{max}=m_p-G_{red}\) | pass iff positive, assuming `HKSM` |

The verdict rules are:

```math
\text{Sobolev pass}
\iff
a>M
\quad\text{and}\quad
S_{Sob}^{max}>0.
```

```math
\text{HK pass}
\iff
S_{HK}^{max}>0
\quad\text{and}\quad
\mathrm{P21\text{-}BTQ\text{-}HKSM}
\text{ is proved on the same record law.}
```

If neither condition is certified, `BTQ-DEGTAIL` remains parked and the
common \(E_{14}/X_{13}\) bypass cannot be spent.

### Theorem 81.7: Current Quantitative Verdict

With the current corpus, `BTQ-DEGTAIL` is quantitatively undecided, but its
Sobolev branch is highly constrained:

1. no numerical pass is licensed, because \(M,d_{loc},m_p,G_{red}\), and the
   source exponent \(s\) are not all instantiated from same-record finite
   tables;
2. the Sobolev branch is falsified immediately for any proposed source with
   \(s-d_{loc}/2\le M\);
3. even if \(s-d_{loc}/2>M\), the Sobolev branch still fails unless
   \(m_p(1-M/a)>G_{red}\);
4. the heat-kernel/Peter-Weyl branch is structurally preferable, because it
   can make \(g_{bat}^{BTQ}=0\), but Paper 10 supplies only fixed finite
   pushforward identities and Paper 11 explicitly does not supply the SEL2
   tree-rate source;
5. therefore the next executable source task is not to optimize \(\beta\)
   symbolically, but to prove or falsify one of:

   ```math
   \mathrm{P21\text{-}BTQ\text{-}HKSM}(t_*,R),
   \qquad
   \mathrm{P21\text{-}BTQ\text{-}PWREG}(s,R)
   \text{ with }s>d_{loc}/2+M,
   ```

   together with `P21-FTS-REDKP` and the enlarged-battery `CMSSI` bound.

Proof.

Items 1--3 are Proposition 81.3 and the missing finite-table entries in
Definition 81.6.  Item 4 follows from Proposition 81.5 together with the
source ledger: Paper 10 proves exact fixed finite pushforwards but leaves
cofinal compatibility and tightness as hypotheses, while Paper 11 states that
the SEL2 tree-rate source is not supplied.  Item 5 is the remaining list of
same-record source gates whose proof would make the worksheet numerical.
`square`

## 82. Pushing The BTQ Finite Census

This section instantiates the finite collar census as far as the declared
data permit.  The result is an explicit symbolic bound in \(N\) and the local
action range \(r_A\), plus a warning: even the conservative upper count for
the trace-generator battery is enormous.  This does not by itself falsify the
Sobolev branch, because falsification requires an actual or lower-bound
dimension for the active local law.  But it sharply identifies what a
Sobolev proof would have to overcome.

### Definition 82.1: Box Parameters

Recall Definition 75.1:

```math
R_{BTQ}^{61}:=2r_A+2.
```

The enclosing hyperrectangle has side lengths

```math
n_1=n_2=3+2R_{BTQ}^{61}=4r_A+7,
\qquad
n_3=n_4=1+2R_{BTQ}^{61}=4r_A+5.
```

For readability set

```math
A:=4r_A+7,
\qquad
B:=4r_A+5.
```

Then the enclosing vertex and positive-link counts are

```math
V_\Box=A^2B^2,
```

and

```math
E_\Box^+
=
2A(A-1)B^2
+2A^2B(B-1).
```

Equivalently,

```math
E_\Box^+
=
2AB\{(A-1)B+A(B-1)\}
=
2AB(2AB-A-B).
```

The first Betti number of the connected box graph is therefore

```math
m_\Box
:=
E_\Box^+-V_\Box+1
=
AB(3AB-2A-2B)+1.
```

For the actual active collar \(Y_{61}^{BTQ}\), regarded as a connected
subgraph of this box,

```math
q(Y_{61}^{BTQ})\le E_\Box^+,
\qquad
m_Y\le m_\Box.
```

The second inequality follows because the cycle space of a subgraph injects
into the cycle space of the ambient graph.

### Lemma 82.2: Generator Count Bound

Let \(\sigma_{rec}=2\) if the active scalar battery keeps both real and
imaginary trace coordinates, and \(\sigma_{rec}=1\) on the paired-real central
record convention.  Then

```math
M=G_{BTQ}^{61}
\le
\sigma_{rec}
\sum_{\ell=1}^{N^2}(2m_Y)^\ell
\le
\sigma_{rec}
\sum_{\ell=1}^{N^2}(2m_\Box)^\ell.
```

If \(m_\Box\ge1\), the closed-form upper bound is

```math
M
\le
\sigma_{rec}\,
{(2m_\Box)^{N^2+1}-2m_\Box\over 2m_\Box-1}.
```

Proof.

Definition 75.3 uses reduced words of length at most \(N^2\) in the alphabet

```math
\{H_1,H_1^{-1},\ldots,H_{m_Y},H_{m_Y}^{-1}\},
```

whose crude cardinality at length \(\ell\) is at most \((2m_Y)^\ell\).  The
factor \(\sigma_{rec}\) accounts for whether imaginary trace coordinates are
kept.  Cyclic rotation, inverse pairing, Cayley-Hamilton, determinant-one,
and Procesi-Razmyslov identities can only reduce this crude count.  `square`

### Lemma 82.3: Local Dimension Bounds

The safest quotient-dimension bound available without a support-stratum audit
is

```math
d_{loc}
\le
m_Y(N^2-1)
\le
m_\Box(N^2-1).
```

This is the dimension of the unreduced local cycle tuple
\(SU(N)^{m_Y}\).  It ignores simultaneous conjugation and is therefore safe
for pass certification: if

```math
s-{m_\Box(N^2-1)\over2}>M,
```

then certainly \(s-d_{loc}/2>M\).

A sharper quotient value is available only after classifying the physical
support stratum of the pushed-forward `SEL2` local law.  The expected
principal-stratum dimensions are:

```math
d_{char}(0,N)=0,
\qquad
d_{char}(1,N)=N-1,
```

and for \(m_Y\ge2\),

```math
d_{char}^{prin}(m_Y,N)=(m_Y-1)(N^2-1).
```

However, Paper 21 may use this sharper value only under an explicit
same-record support-stratum audit:

```math
\mathrm{P21\text{-}BTQ\text{-}PRINSTRAT}(Y,N).
```

Without that audit, use the safe unreduced dimension bound above.

### Corollary 82.4: Certified Sobolev Pass Threshold

Combining Lemma 82.2 and Lemma 82.3, a sufficient threshold for the Sobolev
branch to survive the first feasibility screen is

```math
s>
{m_\Box(N^2-1)\over2}
+
\sigma_{rec}
\sum_{\ell=1}^{N^2}(2m_\Box)^\ell.
```

This is only a sufficient threshold because it uses upper bounds for both
\(d_{loc}\) and \(M\).  It is deliberately conservative and is suitable for a
pass proof.  It is not a falsifier: failure of this conservative inequality
does not prove failure of the exact quotient, because the actual
\(d_{loc}\) and \(M\) may be smaller.

Under the principal-stratum audit and an exact/reduced generator-count census,
the corresponding sharp screen becomes

```math
s>{d_{char}^{prin}(m_Y,N)\over2}+M_{red}^{exact}.
```

### Example 82.5: Wilson-Plaquette Range Sanity Check

This example is **not** an active assumption.  It only calibrates the size of
the crude census if the local action range is the nearest plaquette range
\(r_A=1\).

Then

```math
R_{BTQ}^{61}=4,
\qquad
A=11,
\qquad
B=9,
```

so

```math
V_\Box=9801,
\qquad
E_\Box^+=35244,
\qquad
m_\Box=25444.
```

For \(SU(2)\), the crude paired-complex generator bound is

```math
M
\le
2\sum_{\ell=1}^{4}(50888)^\ell
=
13412201217575012880.
```

On the paired-real convention this number is divided by two:

```math
M_{real}
\le
6706100608787506440.
```

For \(SU(3)\), the same crude bound is already

```math
M
\le
2\sum_{\ell=1}^{9}(50888)^\ell
=
4576958484773586062861956033870277445143056.
```

These numbers are grotesquely loose because they ignore cyclic reduction,
inverse pairing, trace identities, Cayley-Hamilton reduction, active support
constraints, and the fact that only records generated by the actual transition
table are needed.  But they are useful: a Sobolev-only route that relies on
the unreduced word census is not credible.  It must either reduce the actual
finite table drastically, prove `BTQ-FULLLAW`, or switch to a heat-kernel
degree-tail source with \(g_{bat}^{BTQ}=0\).

### Theorem 82.6: Finite Census Verdict

The finite census has been pushed to the following rigorous boundary.

1. The active collar size is controlled symbolically by \(r_A\):

   ```math
   V_\Box=(4r_A+7)^2(4r_A+5)^2,
   ```

   ```math
   E_\Box^+
   =
   2(4r_A+7)(4r_A+5)
   \{2(4r_A+7)(4r_A+5)-(4r_A+7)-(4r_A+5)\},
   ```

   and

   ```math
   m_Y\le m_\Box
   =
   (4r_A+7)(4r_A+5)
   \{3(4r_A+7)(4r_A+5)-2(4r_A+7)-2(4r_A+5)\}+1.
   ```

2. The safe generator count is

   ```math
   M
   \le
   \sigma_{rec}
   \sum_{\ell=1}^{N^2}(2m_\Box)^\ell.
   ```

3. The safe dimension bound is

   ```math
   d_{loc}\le m_\Box(N^2-1).
   ```

4. These safe bounds are enough for pass certification but too crude for
   definitive failure.  A rigorous falsification of the Sobolev branch now
   requires one of:

   ```math
   \mathrm{P21\text{-}BTQ\text{-}EXACTCENSUS},
   \qquad
   \mathrm{P21\text{-}BTQ\text{-}PRINSTRAT},
   \qquad
   \mathrm{P21\text{-}BTQ\text{-}MLOWER},
   ```

   giving an exact/reduced \(M\), an actual local quotient dimension, or a
   lower bound strong enough to prove \(s-d_{loc}/2\le M\).

5. Until such a sharpened census is supplied, the honest next analytic route
   is `BTQ-HKSM`, because it can choose subexponential degree growth and
   avoid the enormous \(M\beta\) battery surcharge.

Proof.

Items 1--3 are Definitions 82.1 and Lemmas 82.2--82.3.  Item 4 is the logic of
Proposition 81.3: Sobolev survival depends on the exact comparison
\(s-d_{loc}/2>M\), and upper bounds alone cannot falsify that comparison.
Item 5 follows from Proposition 81.5 and the surcharge calculation in Section
80.  `square`

## 83. Active-Template Cayley-Hamilton Compression

Section 82 deliberately counted the whole ambient collar trace algebra.  That
count is safe but far too crude: the forced tower does not ask for every word
in the collar box.  It asks for the words actually generated by the active
stagnant/channel transitions.  This section replaces the ambient word census
by an active-template census.

The point is not to pretend that Cayley-Hamilton has solved the finite-battery
problem.  Section 76 is still correct: the polynomial degree of recurrence
coefficients can grow along the stagnant cycle.  The point is sharper: the
number of **active local coordinates** may collapse from the full collar word
bound to a finite recurrence module.  The remaining question is then whether
the law of that finite module is declared as a full finite-dimensional record,
or whether its growing moment degrees have a same-record tail.

### Definition 83.1: Active Stagnant Template List

Let \(\mathfrak T_{act}^{stag}\) be the finite list of bounded-collar
stagnant/channel templates actually generated by the active common
\(E_{14}/X_{13}\) transition table after:

1. deleting retractions and lower-shell constants;
2. imposing the active row representation cutoff \(\Lambda_*\);
3. imposing the active finite product degree from the row battery;
4. identifying templates only by declared symmetries: orientation reversal,
   paired-real character convention, reflection/covariance records already
   declared on the same battery, and exact trace identities.

A template \(T\in\mathfrak T_{act}^{stag}\) is called **CH-compressible** if,
after tree gauge on \(Y_{61}^{BTQ}\), every record in the generated family has
one of the forms

```math
F_T(\mathbf m)
=
\operatorname{Tr}_{\mu_T}
\left(
A_0 U_1^{m_1}A_1
\cdots
U_s^{m_s}A_s
\right),
\qquad
\mathbf m\in{\mathbb N}^s,
```

or a paired real/imaginary part of this scalar, with fixed finite words
\(A_i,U_i\) supported in \(Y_{61}^{BTQ}\), fixed nontrivial channel
\(\mu_T\in\Lambda_*\), and fixed slot number \(s=s(T)\).  Finite products of
such traces are recorded separately in the product-closure audit below.

Let \(\mathfrak T_{mix}^{stag}\) be the complementary list of active stagnant
templates whose language is not of this finite repeated-slot form, for
example arbitrary noncommuting interleavings of two independent cycle words.
The active-template compression closes only if

```math
\mathfrak T_{mix}^{stag}=\varnothing
```

or if the mixed templates are handled by a separate quotient/tail source.

### Lemma 83.2: Rootwise Cayley-Hamilton Recurrence

Fix a CH-compressible template \(T\) and a slot \(i\).  Put
\(d_T:=\dim \mu_T\).  In the representation \(\mu_T\),
Cayley-Hamilton gives

```math
\rho_{\mu_T}(U_i)^{d_T}
=
\sum_{r=0}^{d_T-1}
c_{i,r}^{(T)}\,\rho_{\mu_T}(U_i)^r,
```

where the coefficients \(c_{i,r}^{(T)}\) are polynomial class functions of
\(\rho_{\mu_T}(U_i)\), equivalently finite trace/character records supported
inside \(Y_{61}^{BTQ}\).

Consequently

```math
F_T(\mathbf m)
\in
\sum_{0\le r_1,\ldots,r_s<d_T}
\mathbb R[c_{i,r}^{(T)}]\,
F_T(r_1,\ldots,r_s).
```

Thus the active family for \(T\) is a module of rank at most

```math
R_T\le d_T^{s(T)}
```

over the coefficient ring generated by the slot Cayley-Hamilton coefficients.

Proof.

Apply the Cayley-Hamilton identity in representation \(\mu_T\) to each slot.
For \(m_i\ge d_T\), replace \(\rho_{\mu_T}(U_i)^{m_i}\) by a linear
combination of lower powers with coefficients
\(c_{i,r}^{(T)}\), and iterate until \(0\le m_i<d_T\).  Since the other
factors in the trace are fixed, the resulting expression is a linear
combination of the displayed finitely many seed traces over the coefficient
ring.  The coefficient functions are invariant scalar records of the same
bounded collar.  `square`

### Definition 83.3: Active Coordinate Count

For the CH-compressible active template list, define

```math
C_{coef}^{act}
:=
\#\{c_{i,r}^{(T)}:
T\in\mathfrak T_{act}^{stag},
1\le i\le s(T),
0\le r<d_T\},
```

after quotienting by declared identical coefficient records.  Define the
seed-trace rank count

```math
R_{seed}^{act}
:=
\sum_{T\in\mathfrak T_{act}^{stag}}
\sigma_T d_T^{s(T)},
```

where \(\sigma_T=2\) if both real and imaginary parts are retained and
\(\sigma_T=1\) on the paired-real convention.

The active finite-generator count is

```math
M_{act}^{CH}
:=
C_{coef}^{act}+R_{seed}^{act}.
```

This is the replacement candidate for the ambient \(M=G_{BTQ}^{61}\), but
only under the active-template census gate

```math
\mathrm{P21\text{-}BTQ\text{-}ACTCENSUS}.
```

That gate asserts:

1. \(\mathfrak T_{act}^{stag}\) is the complete active stagnant/channel list;
2. \(\mathfrak T_{mix}^{stag}=\varnothing\), or each mixed template is assigned
   to a separately declared source bucket;
3. the coefficient records and seed traces in \(M_{act}^{CH}\) are pushed
   forward on the same frozen `SEL2` law;
4. no undeclared charged endpoint, gauge-frame, or sector label is hidden in
   the compression.

This is an operational record declaration, not a microscopic field
reconstruction.

### Lemma 83.4: Product Closure Is The Remaining Degree Leak

Cayley-Hamilton compression does not by itself prove finite scalar-battery
closure.  Iterating the recurrence for large \(\mathbf m\) produces polynomial
coefficients in the finite coefficient records whose total degree can grow
with \(|\mathbf m|\).  Therefore the active compression has the following
honest fork.

1. **Full active law.**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}ACTFULLLAW}
   ```

   declares the full pushed-forward law of the finite vector consisting of
   all \(M_{act}^{CH}\) active coordinates.  Then the CH-compressible stagnant
   tower is a same-shell measurable function of one declared finite-dimensional
   record, and there is no degree-battery surcharge.

2. **Active degree tail.**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}ACTDEGTAIL}(D_j,\epsilon_j)
   ```

   keeps scalar monomials in the active coordinates up to degree \(D_j\) and
   proves a same-record tail for the discarded recurrence-coefficient
   polynomial part.  Section 80 applies with \(M\) replaced by
   \(M_{act}^{CH}\).

3. **Uniform active product degree.**

   ```math
   \mathrm{P21\text{-}BTQ\text{-}ACTUDEG}(D_*)
   ```

   proves that the active identities only need products of the compressed
   coordinates up to fixed degree \(D_*\).  Then the active battery is truly
   finite scalar, with no growing degree schedule.

If none of these gates is supplied, the active-template compression is only a
finite-generator compression and cannot be spent as finite-battery `BLU`.

Proof.

Lemma 83.2 expresses every repeated-slot record as a polynomial in the finite
active coordinate vector.  But the degree of that polynomial is not uniformly
bounded as the repetition vector grows; this is exactly the degree leak
identified in Lemma 76.1, now localized to the active recurrence coefficients.
A full finite-dimensional law controls every bounded measurable function of
the active vector.  A finite scalar moment battery controls only the declared
monomials, so it needs either a growing degree-tail estimate or a uniform
degree bound.  `square`

### Proposition 83.5: Re-running The Section-81 Screen With \(M_{act}^{CH}\)

Assume `P21-BTQ-ACTCENSUS` and the active degree-tail branch
`P21-BTQ-ACTDEGTAIL`.  Set

```math
a_{act}:=s-d_{act}/2,
```

where \(d_{act}\) is the dimension of the pushed-forward active coordinate
law.  The Sobolev feasibility screen becomes

```math
a_{act}>M_{act}^{CH}
```

and

```math
m_p\left(1-{M_{act}^{CH}\over a_{act}}\right)>G_{red}.
```

Equivalently,

```math
m_p>{a_{act}\over a_{act}-M_{act}^{CH}}\,G_{red}.
```

Under an active heat-kernel/Peter-Weyl degree-tail source, the battery
surcharge can again be zero:

```math
g_{bat}^{act}=0,
\qquad
\text{pass requires}\qquad
m_p>G_{red}.
```

Proof.

The Section-81 proof used only the number of selected scalar coordinates in
the degree battery.  Under `ACTCENSUS`, that number is
\(M_{act}^{CH}\) instead of the ambient \(G_{BTQ}^{61}\).  Repeating
Proposition 81.3 with \(M_{act}^{CH}\) gives the Sobolev formula.  Repeating
Proposition 81.5 gives the heat-kernel formula.  `square`

### Theorem 83.6: Active Compression Verdict

The active-template compression executes the five finite tasks promised after
Section 82.

1. **Active stagnant templates are isolated.**  They are the finite list
   \(\mathfrak T_{act}^{stag}\) generated by the actual transition table,
   not the whole ambient collar word set.
2. **Cayley-Hamilton recurrence is proved rootwise.**  Each repeated-slot
   template has rank at most \(d_T^{s(T)}\) over a finite coefficient ring.
3. **The active count is defined.**

   ```math
   M_{act}^{CH}=C_{coef}^{act}+R_{seed}^{act}.
   ```

4. **Product closure remains the decisive audit.**  The branch must choose
   `ACTFULLLAW`, `ACTDEGTAIL`, or `ACTUDEG`; otherwise it is only
   finite-generator bookkeeping.
5. **The Section-81 feasibility test is now sharper.**  Replace \(M\) by
   \(M_{act}^{CH}\) and \(d_{loc}\) by \(d_{act}\).  If

   ```math
   s-d_{act}/2\le M_{act}^{CH},
   ```

   the active Sobolev degree-tail route is falsified.  If the inequality is
   strict, the branch still must beat

   ```math
   m_p\left(1-{M_{act}^{CH}\over s-d_{act}/2}\right)>G_{red}.
   ```

This is the first nonridiculous Sobolev screen.  It is also Barandes-aligned:
the declared record is the actual finite active recurrence vector demanded by
the identities, not the whole ambient collar algebra and not an undeclared
history of microscopic local steps.

Proof.

Items 1--3 are Definitions 83.1 and 83.3 plus Lemma 83.2.  Item 4 is Lemma
83.4.  Item 5 is Proposition 83.5.  `square`

## 84. Active Stagnant Template Census And The Remaining Battery Leak

Section 83 replaced the enormous ambient trace-generator count by an active
Cayley-Hamilton recurrence count.  That is the right direction, but it is not
yet the end of the finite-generator-to-finite-battery problem.  This section
executes the active census against the actual template sources already proved
in Sections 69--76.

The result is deliberately sharp.  The active count can be reduced from the
whole bounded collar to a finite grammar of actual stagnant/channel
templates, but the raw active branch still contains at least one unbounded
repeated-slot family.  Therefore a fixed finite scalar moment battery is
still not licensed unless one proves a full local law, a genuine degree-tail
theorem, or an additional selector eliminating the repeated-slot family.

### Definition 84.1: Physical Active Quotient Of Stagnant Templates

Let \(\mathfrak A_{61}^{bc}\) be the bounded-collar stagnant/channel part of
the forced transition automaton from Definition 74.1, restricted to the
active collar \(Y_{61}^{BTQ}\) and with the trace identities of Section 75
declared.  This is the part of the automaton that Section 75 contracts into
finite trace states.  Its vertices are scalar records supported in
\(Y_{61}^{BTQ}\), with representation labels in the active cutoff
\(\Lambda_*\) and with the product cutoff used by the active row.

Define the physical quotient

```math
\Pi_{phys}^{act}:
\mathfrak A_{61}^{bc}\to
\mathfrak A_{61}^{bc,phys}
```

by imposing exactly the equivalences already declared in the preceding
audits:

1. lower-shell retractions are deleted;
2. hypercubic and reflection covariance are applied only to scalar closed
   records already stored on the same pushed-forward law;
3. central real-character pairing identifies \(w\) with \(w^{-1}\) only when
   the paired-real convention is the active battery convention;
4. conjugation, determinant-one, Cayley-Hamilton, and trace identities are
   imposed only inside \(\mathcal T_{N,Y}^{loc}\);
5. no Paper-14, \(X_{13}\), RP/Cov, corner, or entry residual is erased by
   this quotient.

Let \(\mathfrak T_{act}^{stag}\) be the finite template grammar obtained from
\(\mathfrak A_{61}^{bc,phys}\) by listing the finite connector paths and the
finite simple-cycle alphabet in each strongly connected component.  A
particular generated record is obtained by choosing multiplicities and an
interleaving word for these simple cycles.

The quotient is finite for fixed

```math
(N,r_A,\Lambda_*,D_{prod}^{act},Y_{61}^{BTQ}),
```

because the transition alphabet is finite by Lemma 74.2 and the bounded
collar trace quotient is finite at generator level by Lemma 75.4.

### Lemma 84.2: Exhaustive Automaton Normal Form

Every bounded-collar stagnant/channel scalar record generated by the active
common \(E_{14}/X_{13}\) tower is represented, after the quotient
\(\Pi_{phys}^{act}\), by one of the following five template classes.

| class | source | normal form | active status |
| --- | --- | --- | --- |
| \(T_{\rm pow}\) | Theorem 74.4 | \(\operatorname{Tr}_{\mu}(A(\partial p)^mB)\) | genuine one-slot repeated family |
| \(T_{\rm ord}\) | Sections 72--73 | \(\operatorname{Tr}_{\mu}(A_0U_1^{m_1}A_1\cdots U_s^{m_s}A_s)\) with fixed slot order | Cayley-Hamilton compressible |
| \(T_{\rm prod}\) | Paper-14 local action-density/product rows | \(\prod_{a=1}^d F_{T_a}(\mathbf m_a)\), \(d\le D_{prod}^{act}\) | compressible only after product-degree accounting |
| \(T_{\rm chan}\) | channel-growth edges inside \(\Lambda_*\) | one of the previous forms with \(\mu\in\Lambda_*\) | finite channel lift |
| \(T_{\rm mix}\) | arbitrary noncommuting cycle interleavings in a bounded SCC | \(\operatorname{Tr}_{\mu}(A W_{\omega_1}W_{\omega_2}\cdots W_{\omega_m}B)\) with unbounded word order | not repeated-slot compressible unless separately quotiented |

Proof.

In a finite directed strongly connected component, every path is a finite
connector, followed by simple cycles with multiplicities and interleavings,
followed by another finite connector.  If the interleaving order is fixed,
the path has the repeated-slot form of \(T_{\rm ord}\); the one-cycle case is
\(T_{\rm pow}\).  Paper 14's local action-density records add finite
products of such scalar rows, giving \(T_{\rm prod}\).  The representation
cutoff \(\Lambda_*\) makes channel lifts finite, giving \(T_{\rm chan}\).
If two or more noncommuting cycles can be interleaved in unbounded order and
the order is not fixed by the selected normal form, the record is exactly
\(T_{\rm mix}\).  These cases exhaust finite-automaton paths.  `square`

### Proposition 84.3: Cayley-Hamilton Data For The Compressible Classes

Let

```math
\mathfrak T_{CH}^{act}
\subset
\mathfrak T_{act}^{stag}
```

be the finite set of fixed-order compressible template schemes consisting of
\(T_{\rm pow}\), fixed-order \(T_{\rm ord}\), and their finite channel
lifts.  For \(T\in\mathfrak T_{CH}^{act}\), write

```math
F_T(\mathbf m)
=
\operatorname{Tr}_{\mu_T}
(A_0U_1^{m_1}A_1\cdots U_{s(T)}^{m_{s(T)}}A_{s(T)}),
```

with \(d_T=\dim\mu_T\).  Then

```math
R_T\le \sigma_T d_T^{s(T)},
\qquad
C_T\le s(T)d_T,
```

where \(R_T\) is the number of seed trace coordinates after
Cayley-Hamilton reduction, \(C_T\) is the number of recurrence-coefficient
coordinates, and \(\sigma_T\in\{1,2\}\) records whether the active scalar
battery stores one paired-real coordinate or separate real and imaginary
coordinates.

Consequently,

```math
R_{seed}^{act}
\le
\sum_{T\in\mathfrak T_{CH}^{act}}
\sigma_T d_T^{s(T)},
```

```math
C_{coef}^{act}
\le
\sum_{T\in\mathfrak T_{CH}^{act}}
s(T)d_T,
```

and

```math
M_{act}^{CH}
\le
\sum_{T\in\mathfrak T_{CH}^{act}}
\left(\sigma_Td_T^{s(T)}+s(T)d_T\right).
```

In the coarser but explicit form, if

```math
K_{CH}^{act}:=\#\mathfrak T_{CH}^{act},
\qquad
S_{act}:=\max_T s(T),
\qquad
d_{max}^{act}:=\max_{\mu\in\Lambda_*}\dim\mu,
\qquad
\sigma_{max}:=\max_T\sigma_T,
```

then

```math
M_{act}^{CH}
\le
K_{CH}^{act}
\left(
\sigma_{max}(d_{max}^{act})^{S_{act}}
+S_{act}d_{max}^{act}
\right).
```

Proof.

Lemma 83.2 applies independently to each repeated slot.  Each slot contributes
at most \(d_T\) recurrence coefficients and leaves exponents
\(0,\ldots,d_T-1\), so the reduced seed rank is at most \(d_T^{s(T)}\),
up to the real/complex scalar-storage factor \(\sigma_T\).  Summing over the
physically quotiented active template list gives the displayed bounds.
`square`

### Corollary 84.4: The Active Count Is Small Only If The Physical Table Is Small

The ambient bound of Section 82 is replaced by the active table parameters

```math
(K_{CH}^{act},S_{act},d_{max}^{act},\sigma_{max}).
```

This is a real improvement if the active transition table has few physical
stagnant templates and small slot number.  It is not a proof of feasibility
by itself, because \(K_{CH}^{act}\), \(S_{act}\), and \(d_{max}^{act}\) are
still source data of the actual active table.

For the minimal one-staple branch, Theorem 74.4 guarantees that
\(\mathfrak T_{CH}^{act}\) contains at least one \(T_{\rm pow}\)-type family
unless a later selector deletes every non-retracting adjacent-plaquette power
cycle.  Thus the active count is not empty, and the degree issue below is not
vacuous.

### Definition 84.5: Mixed-Template Residual

Define the mixed residual

```math
\mathfrak T_{mix}^{act}
:=
\mathfrak T_{act}^{stag}\setminus
\mathfrak T_{CH}^{act}
```

as the part of the finite template grammar not represented by the
fixed-order compressible schemes after finite product/channel lifts have been
assigned to their declared factors.  The active mixed-zero gate is

```math
\mathrm{P21\text{-}BTQ\text{-}ACTMIX0}
:
\mathfrak T_{mix}^{act}=\varnothing.
```

If `ACTMIX0` is not proved, the active Cayley-Hamilton count is incomplete.
The branch must either add a full finite trace law for the mixed SCC or carry
an additional finite-generator/degree-tail residual

```math
M_{mix}^{act}.
```

No previous section proves `ACTMIX0`; it is a finite table audit of the
contracted active SCCs.

### Lemma 84.6: Fixed-Degree `ACTUDEG` Fails On The Raw Power Family

Assume the active branch retains a \(T_{\rm pow}\)-family

```math
F_m(U)=\operatorname{Tr}_{\mu}(A U^mB)
```

with \(m\) unbounded, and assume only finitely many scalar polynomial moments
of the Cayley-Hamilton coordinates are declared.  Then

```math
\mathrm{P21\text{-}BTQ\text{-}ACTUDEG}(D_*)
```

is false for every fixed \(D_*\), unless an additional identity or selector
makes the family eventually periodic or bounded in \(m\).

Proof.

Already for `SU(2)`, Lemma 76.1 gives

```math
\operatorname{tr}(U^m)=2\mathsf T_m(\operatorname{tr}(U)/2),
```

whose polynomial degree is \(m\).  In the general irreducible channel,
Cayley-Hamilton gives a finite recurrence, but iterating the recurrence to
reach \(m\) produces polynomials in the recurrence coefficients of degree
growing with \(m\).  Therefore no fixed finite scalar moment degree can
contain all \(F_m\).  A finite vector of generators has been found, but a
fixed finite scalar moment battery has not.  `square`

This is not a defect in Cayley-Hamilton.  It is exactly the Barandes-aligned
distinction between declaring a finite operational law and declaring only a
finite list of scalar moments of that law.

### Proposition 84.7: Product Closure Audit

Let

```math
R_{seed}^{act}
=
\sum_{T\in\mathfrak T_{CH}^{act}}\sigma_Td_T^{s(T)}
```

be the active seed count from Proposition 84.3.  If the active local
identities require products of compressed seed coordinates only up to a fixed
degree \(D_{prod}^{act}\), then the number of product coordinates needed at
that fixed degree is bounded by

```math
B_{prod}^{act}
\le
\binom{R_{seed}^{act}+D_{prod}^{act}}{D_{prod}^{act}}.
```

However, this fixed product bound does **not** control the unbounded
recurrence-polynomial degree of Lemma 84.6.  Therefore a fixed product
cutoff is sufficient only under one of the following additional gates:

1. `ACTFULLLAW`: the full finite-dimensional active recurrence law is a
   declared record;
2. `ACTDEGTAIL`: the high-degree recurrence-polynomial part has a same-record
   tail;
3. `ACTPER`: the retained repeated-slot cycles are eventually periodic,
   nilpotent, idempotent, or otherwise finite-degree after the active
   selector;
4. `ACTNOPOW`: the active selector removes every unbounded repeated-slot
   power family.

Absent these gates, \(B_{prod}^{act}\) is only a finite count for the
declared low-degree products, not a closure of the whole stagnant tower.

Proof.

The binomial coefficient is the usual count of monomials of total degree at
most \(D_{prod}^{act}\) in \(R_{seed}^{act}\) variables.  Lemma 84.6 shows
that the stagnant power family requires arbitrarily high degree unless it is
controlled by a full law, a degree-tail estimate, or an additional finite
identity/selector.  `square`

### Theorem 84.8: Active Census Verdict

The five requested active-census tasks are now settled as far as the current
papers permit.

1. **Actual stagnant/channel generators.**  They are the five classes in
   Lemma 84.2, sourced from Sections 72--76 and Paper 14's forced-record
   taxonomy.
2. **CH-compressible versus mixed.**  Fixed-order repeated-slot templates are
   Cayley-Hamilton compressible.  Arbitrary noncommuting interleavings are
   not covered unless `ACTMIX0` or a full finite trace law is supplied.
3. **Template invariants.**  For every compressible template,

   ```math
   s=s(T),\qquad d_T=\dim\mu_T,\qquad
   R_T\le\sigma_Td_T^{s(T)},\qquad
   C_T\le s(T)d_T.
   ```

4. **Active count.**  The honest active generator count is bounded by

   ```math
   M_{act}^{CH}
   \le
   \sum_T(\sigma_Td_T^{s(T)}+s(T)d_T),
   ```

   or by the coarser

   ```math
   K_{CH}^{act}
   \left(
   \sigma_{max}(d_{max}^{act})^{S_{act}}
   +S_{act}d_{max}^{act}
   \right).
   ```

5. **Product closure and Section-81 rerun.**  The Section-81 Sobolev screen
   may use \(M_{act}^{CH}\) only after `ACTMIX0` and one of
   `ACTFULLLAW`, `ACTDEGTAIL`, `ACTPER`, or `ACTNOPOW`.  On the raw branch,
   Lemma 84.6 rules out a naive fixed-degree `ACTUDEG`.

Consequently, active compression has pushed the obstruction as far as finite
algebra alone can push it.  The next real source theorem must be one of:

```math
\mathrm{P21\text{-}BTQ\text{-}ACTFULLLAW},
\qquad
\mathrm{P21\text{-}BTQ\text{-}ACTDEGTAIL},
\qquad
\mathrm{P21\text{-}BTQ\text{-}ACTPER/ACTNOPOW}.
```

Without one of these, the common \(E_{14}/X_{13}\) finite-battery bypass is
still not closed, and the worksheet must continue to carry

```math
E_{14}^{park}+X_{13}^{(26),SEL2}
```

or a separately proved sharp replacement.

Proof.

Items 1--2 are Lemma 84.2 and Definition 84.5.  Items 3--4 are Proposition
84.3.  Item 5 is Proposition 84.7 plus Lemma 84.6.  The final alternatives
are exactly the operational closure gates of Lemma 83.4, sharpened by the
raw power-family obstruction from Theorem 74.4 and Lemma 76.1.  `square`

### Corollary 84.9: Next Source Target

The next useful work is not another ambient generator count.  It is to choose
one concrete closure route:

1. **Full-law route.**  Declare the finite active recurrence vector as a
   finite-dimensional scalar record law and prove same-record `BLU` for that
   law.  This is finite-dimensional but not a finite scalar moment battery.
2. **Heat-kernel/Peter-Weyl degree-tail route.**  Prove an active version of
   `BTQ-HKSM` or `BTQ-PWREG` strong enough to give `ACTDEGTAIL` with
   \(g_{bat}^{act}=0\) or a controlled surcharge.
3. **Selector route.**  Prove a no-power or periodic active selector that
   deletes the \(T_{\rm pow}\) family without importing an area law, mass gap,
   or confinement conclusion.

The first route is conceptually cleanest if the paper is allowed to use
finite-dimensional local laws as records.  The second is closest to the
finite scalar-battery discipline.  The third would be strongest, but it must
be proved as an exact same-record finite-table statement, not as a heuristic
claim that bounded-collar history is irrelevant.

## 85. Full-Law, Degree-Tail, Or Selector: First-Principles Fork

Section 84 leaves three possible escapes from the active bounded-collar
degree leak.  This section tests them from first principles and against the
source discipline of Papers 8, 10, 11, and 14.

The conclusion is strong:

1. a **full finite-dimensional local law** closes the bounded-collar
   finite-generator leak honestly, but it is a typed operational-law
   enlargement, not a finite scalar moment battery;
2. a **degree-tail theorem** would also close the leak, but the current
   corpus does not prove the required same-record heat-kernel/Peter-Weyl tail
   for the active bounded-collar quotient law;
3. a **selector deleting the unbounded power family** is generically false as
   an exact identity for a four-dimensional plaquette-containing `SU(N)`
   action.  It can only be used if its discarded terms are carried as a tail
   or if the dynamics/action is changed.

This is the sharpest Barandes-aligned branch point: either declare the actual
finite local law you need, or prove a same-record tail for the scalar moments.
Do not pretend a finite generator list is already a finite scalar battery.

### Definition 85.1: Active Bounded-Collar Full Law

Let \(Y=Y_{61}^{BTQ}\), choose the tree gauge of Definition 75.2, and let

```math
X_Y^{loc}
:=
SU(N)^{m_Y}/\!\!/SU(N)
```

be the compact simultaneous-conjugation quotient of the cycle variables
\((H_1,\ldots,H_{m_Y})\).  Since the group is compact, this quotient is a
compact Hausdorff operational state space for scalar bounded-collar records.

For each active `SEL2` row \(j\), define the pushed-forward local law

```math
\nu_{Y,j}^{act}
:=
(\pi_{Ad}\circ(H_1,\ldots,H_{m_Y}))_*\mu_j^{SEL2}
```

on \(X_Y^{loc}\), where \(\pi_{Ad}\) is the quotient map and
\(\mu_j^{SEL2}\) is the same whole-process pushed-forward law used throughout
the `SEL2` worksheet.

The full-law gate is

```math
\mathrm{P21\text{-}BTQ\text{-}ACTFULLLAW}
```

and means that the finite-dimensional probability law
\(\nu_{Y,j}^{act}\), not merely finitely many scalar moments of it, is a
declared record of the active branch.

This is not a continuum reconstruction claim.  It is a finite operational
record law on one bounded collar, exactly of the sort allowed by the
finite-battery/operational distinction in Paper 8 and by the same-record
pushforward discipline in Paper 10.

### Lemma 85.2: Full Law Represents Every Bounded-Collar Scalar Record

Every scalar closed Wilson-loop, character, local action-density, finite
product, and finite-channel bounded-collar record supported in \(Y\) is a
bounded continuous function on \(X_Y^{loc}\).  In particular, every record in
the active bounded-collar stagnant/channel tower has the form

```math
F=f_F(H_1,\ldots,H_{m_Y})
```

for some \(f_F\in C(X_Y^{loc})\).

Proof.

Tree gauge identifies scalar closed local records with simultaneous
conjugation-invariant functions of the finite tuple
\((H_1,\ldots,H_{m_Y})\).  Wilson-loop characters and action-density products
are polynomial functions of matrix entries and their conjugates, hence
continuous.  Gauge invariance makes them descend to the compact quotient.
The Procesi/Razmyslov and Cayley-Hamilton trace identities are useful finite
coordinate descriptions, but the statement does not depend on a chosen
finite generator list; the quotient law itself is the declared record.
`square`

### Theorem 85.3: `ACTFULLLAW` Closes The Bounded-Collar Battery Leak

Assume `P21-BTQ-ACTFULLLAW`.  Then every bounded-collar stagnant/channel
record in the common \(E_{14}/X_{13}\) tower is evaluated exactly as a
function of the single finite-dimensional local law
\(\nu_{Y,j}^{act}\).  Therefore the active bounded-collar quotient has:

```math
T_{act,deg}=0,
\qquad
g_{bat}^{act}=0,
```

and no `ACTMIX0`, `ACTUDEG`, or scalar moment degree-tail is needed for the
bounded-collar part.

What is closed is exactly the finite-generator-to-finite-record gap.  The
remaining common-bypass source obligations are the reduced escape/clustering
and reduced shell-inverse gates:

```math
\mathrm{P21\text{-}FTS\text{-}REDESC}
+
\mathrm{P21\text{-}AF\text{-}COL\text{-}SRC}
+
\mathrm{P21\text{-}RED\text{-}CMSSI}.
```

Proof.

By Lemma 85.2, every bounded-collar record is a bounded continuous observable
on \(X_Y^{loc}\).  Declaring \(\nu_{Y,j}^{act}\) as a record gives its
expectation directly:

```math
\mathbb E_{\mu_j^{SEL2}}F
=
\int_{X_Y^{loc}} f_F\,d\nu_{Y,j}^{act}.
```

There is no polynomial degree truncation and hence no discarded high-degree
tail.  Mixed noncommuting interleavings are also covered, because they are
ordinary continuous functions on the same compact quotient.  The only records
not addressed are records that leave the bounded collar or enter the
all-depth reduced forced tower; those are precisely the reduced
escape/clustering and inverse-amplification gates already isolated in
Sections 74--76.  `square`

### Corollary 85.4: Meaning Of The Full-Law Branch

The full-law branch is mathematically clean but changes the type of record
being used.

It is valid to write

```math
E_{14}^{park}+X_{13}^{(26),SEL2}
\quad\text{may be reopened through ACTFULLLAW}
```

only if the paper explicitly allows finite-dimensional local laws as
operational records.  It is not valid to present this as a proof that a fixed
finite scalar moment battery contains every stagnant-cycle record.

Thus the full-law branch is Barandes-aligned precisely because it refuses to
hide the extra information: the local law is declared, typed, and kept finite.

### Definition 85.5: Active Heat-Kernel/Peter-Weyl Degree-Tail Source

If the paper insists on finite scalar batteries rather than full local laws,
the strongest plausible route is an active same-record spectral tail.

Define

```math
\mathrm{P21\text{-}BTQ\text{-}ACTHKSM}(t_*,R,C)
```

to mean that the active bounded-collar quotient law \(\nu_{Y,j}^{act}\) is,
uniformly on the selected cofinal row, dominated in Peter-Weyl/Sobolev tail by
a heat-kernel smoothing time \(t_*>0\).  Concretely, if
\(\Pi_{\le L}^{PW}\) is the Peter-Weyl projection on \(X_Y^{loc}\), then for
every active bounded-collar stagnant observable \(f_F\),

```math
\left|
\int (f_F-\Pi_{\le L}^{PW}f_F)\,d\nu_{Y,j}^{act}
\right|
\le
C e^{-t_* L^2}
```

with constants uniform over the active bounded-collar tower after the
Cayley-Hamilton quotient and product normalization.

The exponent \(L^2\) is schematic: any explicit superlinear Casimir lower
bound sufficient to dominate the active recurrence degree is acceptable.

### Proposition 85.6: `ACTHKSM` Implies `ACTDEGTAIL`

Assume `P21-BTQ-ACTHKSM(t_*,R,C)`.  Then for every target reduced depth
\(\overline K\), choose a Peter-Weyl cutoff

```math
L(\overline K)
=
\left\lceil
\sqrt{\lambda\overline K/t_*}
\right\rceil .
```

The active degree-tail error satisfies

```math
T_{act,deg}(\overline K)
\le
C e^{-\lambda\overline K}.
```

The number of retained Peter-Weyl scalar coordinates grows subexponentially
in \(\overline K\), hence

```math
g_{bat}^{act}=0.
```

Therefore the degree part of the common bypass can pass with any
\(\lambda\) chosen below the available heat-kernel tail rate, subject only to
the independent reduced escape and inverse-growth inequalities.

Proof.

The displayed cutoff makes \(e^{-t_*L(\overline K)^2}\le e^{-\lambda
\overline K}\) up to an absorbed constant.  Weyl's law on the fixed compact
quotient gives polynomial growth of the number of Peter-Weyl modes below
Casimir cutoff \(L^2\).  Polynomial growth has zero exponential rate in
\(\overline K\), so the battery-growth surcharge is zero.  This is the active
version of the heat-kernel argument in Corollary 80.4 and Proposition 81.5.
`square`

### Theorem 85.7: Current Status Of The Degree-Tail Route

The current source papers do not prove

```math
\mathrm{P21\text{-}BTQ\text{-}ACTHKSM}(t_*,R,C)
```

for the active bounded-collar quotient law.

What is proved is weaker:

1. Paper 10 supplies finite Peter-Weyl batteries and exact finite-battery
   pushforward identities;
2. Paper 11 supplies heat-kernel and KP mechanisms on declared finite
   batteries in strong-coupling or local-RG settings;
3. Paper 20 and earlier Paper-21 sections prove several one-observable or
   finite-row regularity statements, including central plaquette regularity;
4. none of these proves a uniform positive smoothing time \(t_*>0\) for the
   whole active bounded-collar quotient law on the `SEL2` cofinal row.

Thus `ACTDEGTAIL` remains a genuine source theorem.  It is not a formal
consequence of compactness, Cayley-Hamilton, or rowwise finite
Peter-Weyl truncation.

Proof.

Finite Peter-Weyl compatibility gives exact statements for each declared
finite cutoff.  It does not give a uniform spectral tail for the full
bounded-collar quotient law.  Compactness gives subsequential weak limits but
no exponential coefficient decay.  The finite heat-kernel regularity already
proved for selected plaquette marginals does not control arbitrary
bounded-collar stagnant-cycle functions and products.  Therefore the uniform
tail in Definition 85.5 is additional source data.  `square`

### Lemma 85.8: Exact Periodic Selector Is Generically False

The periodic selector gate

```math
\mathrm{P21\text{-}BTQ\text{-}ACTPER}
```

is generically false for `SU(N)`.

Already on an `SU(2)` subgroup, let

```math
U_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta}).
```

Then

```math
\operatorname{tr}(U_\theta^m)=2\cos(m\theta).
```

For \(\theta/\pi\notin\mathbb Q\), this sequence is not eventually periodic
in \(m\).  Hence no exact finite periodic identity can identify all powers
\(\operatorname{tr}(U^m)\) with a bounded list of scalar records on all of
`SU(N)`.

Proof.

If \(2\cos(m\theta)\) were eventually periodic with period \(P\), then
\(\cos((m+P)\theta)=\cos(m\theta)\) for all large \(m\).  This forces
\(e^{iP\theta}=\pm1\), hence \(\theta/\pi\in\mathbb Q\), contradicting the
choice of \(\theta\).  Since this one-parameter subgroup lies in `SU(N)` for
every \(N\ge2\), a universal `SU(N)` selector cannot rely on periodic powers.
`square`

### Lemma 85.9: Exact No-Power Selector Is Not Available On The Plaquette Branch

Assume the active action has a nonzero adjacent plaquette coefficient and the
minimal one-staple branch of Theorem 74.4 is retained.  Then

```math
\mathrm{P21\text{-}BTQ\text{-}ACTNOPOW}
```

cannot be an exact zero selector.  Deleting the unbounded \(T_{\rm pow}\)
family deletes non-retracting records with nonzero identity coefficients.
Those records must either be represented by a declared full law, controlled by
a degree tail, or carried as an explicit residual.

Proof.

Theorem 74.4 constructs non-retracting bounded-collar paths of arbitrary
forced depth of the schematic form
\(\operatorname{Tr}_{\mu}(A(\partial p)^mB)\).  The construction uses a
nonzero adjacent plaquette coefficient and the same compact-group contraction
mechanism as the first-shell rank audit.  Therefore the generated terms are
not zero identities and not lower-shell retractions.  A selector that simply
removes them changes the Schwinger-Dyson/Casimir row unless the removed terms
are paid somewhere else.  `square`

### Theorem 85.10: Settled Fork

At the present source level, the three Section-84 closure routes have the
following rigorous status.

1. **Full-law route:** valid and clean as a finite-dimensional operational
   record enlargement.  It closes the bounded-collar degree leak by Theorem
   85.3, with

   ```math
   T_{act,deg}=0,\qquad g_{bat}^{act}=0.
   ```

   It must be advertised as a full-law record branch, not a finite scalar
   moment-battery theorem.

2. **Degree-tail route:** viable but unsourced.  `ACTHKSM` would imply
   `ACTDEGTAIL` with \(g_{bat}^{act}=0\) by Proposition 85.6, but Theorem
   85.7 says the current papers do not prove `ACTHKSM` for the active
   bounded-collar quotient law.

3. **Selector route:** generically unavailable as an exact closure.  `ACTPER`
   fails by Lemma 85.8, and `ACTNOPOW` fails on the active plaquette branch by
   Lemma 85.9 unless its deleted terms are carried or the branch/action is
   changed.

Therefore the honest next move is:

```math
\boxed{
\text{take } \mathrm{ACTFULLLAW}
\text{ as a typed finite-law branch,}
\quad\text{or prove } \mathrm{ACTHKSM}.
}
```

If the paper insists on scalar finite batteries and does not prove
`ACTHKSM`, then the common \(E_{14}/X_{13}\) bypass remains parked.

Proof.

The full-law route is Theorem 85.3.  The degree-tail implication is
Proposition 85.6 and its source status is Theorem 85.7.  The selector
obstructions are Lemmas 85.8 and 85.9.  These exhaust the closure routes of
Corollary 84.9.  `square`

### Corollary 85.11: Recommended Branch For Paper 21

The most honest and imaginative branch is the full-law branch:

```math
\mathrm{P21\text{-}BTQ\text{-}ACTFULLLAW}.
```

It is finite, operational, same-record, and non-circular.  It does not assume
an area law, a mass gap, a continuum Yang-Mills measure, or hidden local
subprocesses.  It simply declares the actual bounded-collar quotient law that
the identities are already using.

The price is conceptual but clean: Paper 21 must distinguish

```math
\text{finite scalar moment battery}
\quad\ne\quad
\text{finite-dimensional local law record}.
```

Once that distinction is stated, the finite-generator-to-finite-battery
obstruction is settled for bounded collars.  The remaining hard source is no
longer bounded-collar algebra; it is the reduced escaping tower:

```math
\mathrm{REDESC}
+
\mathrm{AF\text{-}COL\text{-}SRC}
+
\mathrm{RED\text{-}CMSSI}.
```

## 86. Activating The Full-Law Branch In The Non-Corner Worksheet

Section 85 decides the bounded-collar closure fork.  This section pushes the
decision back into the actual Paper-21 ledger.  The key point is narrow but
important:

```math
\mathrm{ACTFULLLAW}
```

removes the bounded-collar finite-battery leak, but it does not by itself
prove the common \(E_{14}/X_{13}\) bypass.  The escaping reduced tower must
still satisfy the non-area-law forced-tail and shell-invertibility estimates.

### Definition 86.1: Full-Law Common-Bypass Gate

On the strict Paper-12 diagonal branch of Theorem 66.5, define

```math
\mathrm{P21\text{-}E14X13\text{-}FULLLAW\text{-}BYPASS}
```

to be the conjunction of:

1. the active full-law branch

   ```math
   \mathrm{P21\text{-}BTQ\text{-}ACTFULLLAW};
   ```

2. reduced escape or reduced KP forced-tail source on the contracted
   automaton, giving a decay exponent \(m_{red}^{act}>0\);
3. the reduced coefficient and geometry constants of Section 75,

   ```math
   A_{esc}^{BTQ},\qquad C_{geom}^{red};
   ```

4. reduced shell inverse control with exponent \(g_q^{red}\), where
   \(g_q^{red}=0\) under `P21-RED-CMSSI`;
5. the strict inequality

   ```math
   m_{red}^{act}
   >
   \log A_{esc}^{BTQ}
   +\log C_{geom}^{red}
   +g_q^{red}.
   ```

There is no \(g_{bat}\) term in this gate, because Section 85 proves that the
full local law has no scalar degree truncation.

### Theorem 86.2: Full-Law Bypass Deletes The Parked \(E_{14}/X_{13}\) Pair

Assume `P21-E14X13-FULLLAW-BYPASS`.  Then the common parked pair

```math
E_{14}^{park}+X_{13}^{(26),SEL2}
```

may be replaced by zero in the strict non-corner worksheet.

Equivalently, on this branch,

```math
\mathcal G_{E14X13}^{SEL2}
\quad\text{is closed through the full-law bounded-collar route.}
```

Proof.

Sections 61--67 reduce the parked \(E_{14}/X_{13}\) pair to the common
finite-battery `BLU`/forced-tail source gate
\(\mathcal G_{E14X13}^{SEL2}\).  Sections 74--76 then split that gate into
bounded-collar closure, reduced forced-tail decay, and shell inverse control.
Theorem 85.3 supplies bounded-collar closure without a degree-tail surcharge
by declaring the full finite-dimensional local law.  The remaining hypotheses
of Definition 86.1 are exactly the reduced forced-tail summability and inverse
amplification inequality of Theorem 74.9 and Theorem 76.5, with
\(g_{bat}^{act}=0\).  Therefore the common forced tower is summable and the
Paper-14/\(X_{13}\) comparison defect vanishes on the selected same-record
branch.  `square`

### Corollary 86.3: Full-Law Non-Corner Envelope

On the strict Paper-12 diagonal branch and under
`P21-E14X13-FULLLAW-BYPASS`, the Section-67 non-corner envelope reduces from

```math
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}
```

to

```math
\mathcal R_{noncorn}^{86,SEL2}(s)
:=
U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

The corresponding surplus is

```math
\Phi_{86}^{SEL2}(s)
:=
S_{NC}(s)
-U_{11}^{RPCov,car,SEL2}(s)
-U_{13}^{RPF,bd}.
```

Thus the full-law branch converts the hard \(E_{14}/X_{13}\) obstruction into
the reduced-tower inequality of Definition 86.1.  It does not touch the
Paper-16 RP/covariance carry or the exact-entry residual-factorization carry.

### Theorem 86.4: Current Full-Law Status

The present text now proves the bounded-collar part of the full-law route, but
not the full common bypass.  Precisely:

1. `ACTFULLLAW` is an available typed branch by Definitions 85.1--85.3;
2. the scalar degree leak and \(g_{bat}^{act}\) are removed on that branch;
3. `P21-E14X13-FULLLAW-BYPASS` still requires actual same-record source data
   for \(m_{red}^{act}\), \(A_{esc}^{BTQ}\), \(C_{geom}^{red}\), and
   \(g_q^{red}\);
4. until the strict inequality in Definition 86.1 is proved, the worksheet
   may not silently delete \(E_{14}^{park}+X_{13}^{(26),SEL2}\).

Therefore the issue is now settled to a smaller obstruction:

```math
\boxed{
m_{red}^{act}
>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red}.
}
```

This is the next real theorem.  It is a reduced escaping-tower theorem, not a
bounded-collar finite-algebra theorem.

Proof.

Items 1--2 are Theorem 85.3.  Item 3 is Definition 86.1.  Item 4 is Theorem
86.2 read contrapositively: the parked pair is deleted only after the full
same-record bypass package is supplied.  `square`

### Corollary 86.5: Next Execution Target

The next work item is now sharply ordered.

1. Compute or bound the actual reduced escaping transition table:

   ```math
   A_{esc}^{BTQ},\qquad C_{geom}^{red}.
   ```

2. Prove reduced shell inverse control:

   ```math
   g_q^{red}=0
   ```

   by `P21-RED-CMSSI`, or carry an explicit \(g_q^{red}\).

3. Source reduced forced-tail decay \(m_{red}^{act}\) by a non-area-law
   mechanism: reduced KP, AF collar clustering after genuine escape, or a
   direct projection-tail theorem.

4. Test the single inequality

   ```math
   m_{red}^{act}
   >
   \log A_{esc}^{BTQ}
   +\log C_{geom}^{red}
   +g_q^{red}.
   ```

If it passes, \(E_{14}^{park}+X_{13}^{(26),SEL2}\) drops out of the
non-corner worksheet.  If it fails, the full-law branch has still done useful
work: it proves the failure is not bounded-collar algebra but reduced
escaping-tower entropy, coefficient growth, or inverse amplification.

## 87. Settling The Reduced Escaping Inequality

Section 86 leaves one displayed inequality:

```math
m_{red}^{act}
>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red}.
```

This section fixes its exact meaning.  The point is not to guess the sign of
the margin.  The point is to identify which pieces are finite table data,
which pieces are analytic same-record decay data, and when the parked
\(E_{14}/X_{13}\) pair may actually be deleted.

### Definition 87.1: Reduced Inequality Data

On the `ACTFULLLAW` branch of Definition 85.1, set

```math
G_{red}^{act}
:=
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red},
```

and

```math
\Delta_{red}^{act}
:=
m_{red}^{act}-G_{red}^{act}.
```

The reduced inequality is the gate

```math
\mathrm{P21\text{-}RED\text{-}INEQ}
\quad:\quad
\Delta_{red}^{act}>0.
```

Here:

1. \(A_{esc}^{BTQ}\) is the maximum absolute escaping-edge coefficient after
   inserting the bounded-collar trace quotient;
2. \(C_{geom}^{red}\) is the maximum reduced escaping branching number;
3. \(g_q^{red}\) is the reduced shell inverse growth exponent;
4. \(m_{red}^{act}\) is the actual same-record decay exponent for the reduced
   forced tower.

The first two are finite maxima over the contracted transition table.  The
third is a finite-shell inverse-growth problem.  The fourth is the only
analytic decay source.

### Definition 87.2: Certified Finite Envelopes

Let \(E_{esc}^{raw}\) be the finite list of raw local escaping transition
types before the `BTQ` contraction, and let \(a_e^{raw}\) be the absolute
identity-channel coefficient of \(e\).  Define

```math
A_{edge}^{raw}
:=
\max_{e\in E_{esc}^{raw}}\max(1,|a_e^{raw}|).
```

Let \(B_{BTQ}^{61}\) be the normal-form absolute-coefficient bound from
Theorem 75.6.  A safe finite coefficient envelope is

```math
A_{esc}^{env}
:=
\max\bigl(1,(B_{BTQ}^{61})^2A_{edge}^{raw}\bigr).
```

The square is deliberately conservative: one `BTQ` rewrite may be inserted on
the source side and one on the target side of a reduced escaping edge.  If the
actual normal form uses only one insertion, the square may be replaced by the
single factor \(B_{BTQ}^{61}\).

For the reduced branching constant set

```math
C_{geom}^{env}
:=
C_{geom}(4,r_A,A_{stencil}),
```

the Paper-14 one-step local branching envelope already used in Definition
75.9.  Finally set

```math
g_q^{env}:=
\begin{cases}
0, & \text{if } \mathrm{P21\text{-}RED\text{-}CMSSI}\text{ is proved},\\
g_q^{car}, & \text{otherwise.}
\end{cases}
```

These give the sufficient finite upper envelope

```math
G_{red}^{act}
\le
G_{red}^{env}
:=
\log A_{esc}^{env}
+\log C_{geom}^{env}
+g_q^{env}.
```

### Lemma 87.3: The Algebraic Side Is Finite But Not Numerically Closed

The current paper proves

```math
A_{esc}^{BTQ}<\infty,
\qquad
C_{geom}^{red}<\infty,
```

and it proves the displayed envelope

```math
G_{red}^{act}\le G_{red}^{env}.
```

It does not provide a sharp numerical value for \(A_{esc}^{BTQ}\) or
\(C_{geom}^{red}\).

Proof.

The finiteness of the quotient automaton is Lemma 75.8.  Definition 75.9
defines \(C_{geom}^{red}\) and \(A_{esc}^{BTQ}\) as maxima over that finite
transition table.  The branching envelope is the displayed Paper-14 local
branching bound.  For coefficients, each reduced escaping coefficient is a
finite linear combination of raw local coefficients after inserting at most
two bounded-collar normal forms; the absolute sum is bounded by
\((B_{BTQ}^{61})^2A_{edge}^{raw}\).  This proves the envelope.  The actual
transition table is not tabulated in the present corpus, so no sharper
number is licensed. `square`

### Definition 87.4: Actual Decay Source Fork

There are two honest ways to source \(m_{red}^{act}\).

1. **Reduced KP/size-growth source.**  Prove
   `P21-FTS-REDKP(\mu_red,\alpha_red)` on the same `SEL2` pushed-forward law
   and prove the size-growth test of Lemma 78.4 with constant
   \(c_{size}^{act}>0\).  Then define

   ```math
   m_{red}^{act}:=\mu_{red}^{act}c_{size}^{act}.
   ```

2. **Direct reduced projection-tail source.**  Prove directly that the
   inverse-amplified reduced forced tail satisfies

   ```math
   \sum_{\overline K\ge K}
   T_{\overline K}^{red,act}
   \le
   C e^{-m_{red}^{act}K}
   ```

   on the same finite-dimensional active law of Definition 85.1.

The strong-coupling Paper-11 `SC-KP` source is not an acceptable substitute on
the asymptotically-free `SEL2` branch, because Paper 11 Theorem SC.9 says that
the literal Haar-background character KP margin does not continue to the AF
trajectory.  A Wilson-loop area law or continuum confinement premise is also
forbidden here, because this source gate is upstream of the surface-area
conclusion.

### Lemma 87.5: The Current Corpus Does Not Source \(m_{red}^{act}\)

From Papers 10--14 and Paper 20 as currently written, one cannot infer

```math
m_{red}^{act}>0
```

for the common \(E_{14}/X_{13}\) reduced tower.

Proof.

Paper 10 supplies exact finite-battery/projective semantics only after a
battery is declared; it does not prove decay of an all-depth forced tower.
Paper 11 supplies conditional KP and AF locality mechanisms, and explicitly
states that it does not supply the Paper-20 `SEL2` tree-rate/source gate.
Paper 14 supplies finite-block entry and forced-tower criteria, but its
post-Paper-20 source boundary states that the later `SEL2` tree-rate source is
not exported there.  Paper 20 parks the relevant tree-rate and escape-mass
sources as same-record coefficient estimates.  Section 78 of the present
paper also shows that linear physical-distance escape is not forced by
locality, so \(m_{red}^{act}\) cannot be obtained from raw collar distance
alone.  Therefore a positive reduced decay exponent remains a new source
theorem: reduced KP plus size-growth, or an equivalent direct reduced
projection-tail theorem. `square`

### Theorem 87.6: Complete Pass/Fail/Carry Trichotomy

The inequality is settled by the following mutually exclusive outcomes.

1. **Certified pass.**  If either

   ```math
   m_{red}^{act}
   >
   G_{red}^{act}
   ```

   is computed from the actual reduced table, or the stronger sufficient
   inequality

   ```math
   m_{red}^{act}
   >
   G_{red}^{env}
   ```

   is proved, then `P21-RED-INEQ` holds and
   \(E_{14}^{park}+X_{13}^{(26),SEL2}\) may be deleted on the strict
   non-corner worksheet.

2. **Certified fail.**  If one has an upper bound \(m_{red}^{act}\le
   m_{red}^{up}\) and a lower bound \(G_{red}^{act}\ge G_{red}^{low}\) with

   ```math
   m_{red}^{up}\le G_{red}^{low},
   ```

   then `P21-RED-INEQ` fails.  In that case the full-law branch still removes
   the bounded-collar finite-algebra leak, but the common \(E_{14}/X_{13}\)
   bypass cannot be spent.

3. **Current carry.**  If neither a pass certificate nor a fail certificate is
   available, then the inequality is not decided by the current corpus and the
   worksheet must keep

   ```math
   E_{14}^{park}+X_{13}^{(26),SEL2}
   ```

   or an independently proved sharper carried replacement.

Proof.

The pass statement is Theorem 86.2 with Definition 87.1.  The envelope version
follows from Lemma 87.3.  The fail statement is elementary order comparison:
if every licensed decay exponent is at most \(m_{red}^{up}\) while the growth
side is at least \(G_{red}^{low}\), then the strict inequality cannot hold.
The carry statement is the contrapositive discipline already used in Paper 14
and Paper 20: an unproved source gate cannot be spent as a zero debit. `square`

### Corollary 87.7: Current Verdict For The Displayed Inequality

At the present source level, the displayed inequality is **not** proved and is
also **not** falsified.  It is settled to the exact source gate

```math
\mathrm{P21\text{-}RED\text{-}INEQ}
:
\quad
m_{red}^{act}
>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red}.
```

The bounded-collar part is no longer the obstruction on the `ACTFULLLAW`
branch.  The remaining obstruction is one of:

1. the actual reduced escaping table has too large
   \(A_{esc}^{BTQ}C_{geom}^{red}\);
2. `P21-RED-CMSSI` fails and \(g_q^{red}\) is positive;
3. the active same-record reduced tower has no positive decay exponent;
4. it has a positive exponent but not enough to beat the finite growth side.

Thus, until `P21-RED-INEQ` is certified, the strict non-corner envelope remains

```math
\mathcal R_{noncorn}^{87,SEL2}(s)
=
E_{14}^{park}
+X_{13}^{(26),SEL2}
+U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

Under a future certified pass it reduces to the Section-86 envelope

```math
\mathcal R_{noncorn}^{86,SEL2}(s)
=
U_{11}^{RPCov,car,SEL2}(s)
+U_{13}^{RPF,bd}.
```

### Corollary 87.8: The Six Concrete Tasks Are Now Fixed

To turn the carry verdict into a pass or fail, the next six executable tasks
are exactly:

1. tabulate the actual reduced escaping edge list
   \(E_{esc}(\overline{\mathfrak A}_{61}^{BTQ})\);
2. compute \(C_{geom}^{red}\) as the maximum escaping out-degree of that table;
3. compute \(A_{esc}^{BTQ}\) from the corresponding identity-channel
   coefficients after `BTQ` normal forms;
4. prove `P21-RED-CMSSI`, or compute a carried \(g_q^{red}\);
5. prove reduced KP plus size-growth, or a direct projection-tail theorem, to
   obtain \(m_{red}^{act}\);
6. compare \(\Delta_{red}^{act}=m_{red}^{act}-G_{red}^{act}\).

No continuum area law, mass gap, or unrecorded microscopic Markov kernel may be
used in any of these six tasks.  This is the Barandes-aligned version of the
gate: only whole pushed-forward laws on declared finite records are allowed to
enter the proof.

## 88. Executing The Six-Step Reduced Inequality Audit

Section 87 names the six tasks.  This section executes them as far as the
current finite data permit.  The result is a precise certificate format and a
sharp verdict: the finite side can be reduced to a finite table, but the
analytic decay side still requires a same-record reduced KP or direct
projection-tail theorem.

### Definition 88.1: Reduced Escaping Edge Certificate

A reduced escaping edge certificate is a finite object

```math
\mathsf C_{esc}^{red}
=
(\overline V,\overline E_{esc},s,t,\tau,a,\Delta_X,\mathcal O)
```

with the following entries.

1. \(\overline V\) is the finite vertex set of the contracted automaton
   \(\overline{\mathfrak A}_{61}^{BTQ}\) after the physical quotient of
   Definition 84.1 and the full-law bounded-collar convention of
   Definition 85.1.
2. \(\overline E_{esc}\) is the finite set of non-retracting external edges
   that increase reduced depth \(\overline K\).
3. \(s,t:\overline E_{esc}\to\overline V\) are source and target maps.
4. \(\tau(e)\) records the local transition type of \(e\): action-stencil
   insertion, Schwinger-Dyson/Casimir transfer, channel lift, support
   enlargement, or exact-entry comparison edge.  Only types already present
   in Papers 14, 20, and Sections 61--86 are allowed.
5. \(a(e)\) is the absolute identity-channel coefficient of the reduced edge
   after inserting the bounded-collar normal forms at its source and target.
6. \(\Delta_X(e)\in\mathbb N\) is the number of new coarse support cells added
   to \(X_f^{red}\) by the edge.
7. \(\mathcal O(e)\) is the same-shell off-diagonal shell-coupling
   contribution of the edge, used in the reduced shell inverse audit.

The certificate is valid only if every entry is evaluated on the same active
`SEL2` pushed-forward law.  It is invalid if it introduces an unrecorded
microscopic subprocess, an undeclared gauge frame, or a Wilson-loop area-law
premise.

### Lemma 88.2: Finite Generation Of The Certificate

For fixed

```math
(N,r_A,\Lambda_*,D_{prod}^{act},Y_{61}^{BTQ})
```

there is a finite algorithm that generates all candidate entries of
\(\mathsf C_{esc}^{red}\).

Proof.

The local transition alphabet is finite by Lemma 74.2.  The bounded-collar
trace quotient is finite at generator level by Lemma 75.4.  The active
physical quotient is finite by Definition 84.1, and `ACTFULLLAW` removes the
degree-tail expansion inside bounded-collar stagnant/channel components by
Theorem 85.3.  Therefore only external non-retracting edge types remain.
The active representation and product cutoffs make the channel and product
labels finite.  Deleting retractions/lower-shell constants and quotienting by
the declared symmetries is a finite operation.  This produces the finite
candidate certificate.  `square`

### Definition 88.3: Exact Reduced Constants From A Certificate

Given a valid certificate, define

```math
C_{geom}^{red}(\mathsf C_{esc}^{red})
:=
\max_{\bar v\in\overline V}
\#\{e\in\overline E_{esc}:s(e)=\bar v\},
```

and

```math
A_{esc}^{BTQ}(\mathsf C_{esc}^{red})
:=
\max_{e\in\overline E_{esc}}\max(1,a(e)).
```

These are the exact constants of Definition 75.9 when the certificate is the
actual reduced escaping table.

For pass certification without the full table, use the safe envelopes

```math
C_{geom}^{red}
\le
C_{geom}^{env}
:=
C_{geom}(4,r_A,A_{stencil}),
```

and

```math
A_{esc}^{BTQ}
\le
A_{esc}^{env}
:=
\max\bigl(1,(B_{BTQ}^{61})^2A_{edge}^{raw}\bigr).
```

If the certificate proves that only one bounded-collar normal form is inserted
per escaping edge, replace \((B_{BTQ}^{61})^2\) by \(B_{BTQ}^{61}\).  If it
proves edgewise normal-form norms \(B_s(e)\) and \(B_t(e)\), use the sharper

```math
A_{esc}^{BTQ}
\le
\max_{e\in\overline E_{esc}}
\max(1,B_s(e)B_t(e)a^{raw}(e)).
```

### Theorem 88.4: Steps 1--3 Are Finite-Table Complete

Tasks 1--3 of Corollary 87.8 are now reduced to a finite certificate:

```math
\overline E_{esc},
\qquad
C_{geom}^{red},
\qquad
A_{esc}^{BTQ}.
```

If \(\mathsf C_{esc}^{red}\) is supplied, these constants are computed exactly
by Definition 88.3.  Without the certificate, the present paper licenses only
the envelopes \(C_{geom}^{env}\) and \(A_{esc}^{env}\).

Proof.

Lemma 88.2 gives a finite candidate-generation procedure.  Definition 88.3 is
exactly the finite maximum defining \(C_{geom}^{red}\) and \(A_{esc}^{BTQ}\).
The envelope estimates are Lemma 87.3.  No analytic or continuum input enters
these three tasks.  `square`

### Definition 88.5: Weighted Reduced CMSSI Test

Let \(F_{\overline K}^{red}\) be the retained reduced shell at depth
\(\overline K\).  A weight is a real function

```math
w:F_{\overline K}^{red}\to\mathbb R
```

extended coherently over all depths by the same reduced template labels.
For a shell coupling \(\alpha\to\beta\), define the weighted off-diagonal
row sum

```math
\Omega_{\overline K}^{red}(w)
:=
\sup_{\alpha\in F_{\overline K}^{red}}
\sum_{\beta\ne\alpha}
|O_{\alpha\beta}^{red}|
\exp(w(\beta)-w(\alpha)).
```

The weighted CMSSI gate is

```math
\mathrm{P21\text{-}RED\text{-}CMSSI}(w)
:
\quad
\Omega_*^{red}(w)
:=
\sup_{\overline K}\Omega_{\overline K}^{red}(w)
<
\kappa_{\min}^{red}.
```

Equivalently, on the finite reduced transition grammar it is enough to prove
the edgewise row-sum inequality

```math
\sup_{\alpha}
\sum_{e:\alpha\to\beta(e)}
|\mathcal O(e)|
\exp(w(\beta(e))-w(\alpha))
<
\kappa_{\min}^{red},
```

uniformly over all depth labels generated by the same templates.

### Theorem 88.6: Step 4 Reduces To Weighted Diagonal Dominance

If `P21-RED-CMSSI(w)` holds for some coherent weight \(w\) whose shell
oscillation has zero exponential rate, then

```math
g_q^{red}=0.
```

If the same weighted dominance holds but the shell oscillation has exponential
rate \(g_w\), then the certified conclusion is \(g_q^{red}\le g_w\).

If no such weight or equivalent all-depth right-inverse certificate is proved,
then the only licensed value is the carried exponent

```math
g_q^{red}=g_q^{car}
:=
\limsup_{\overline K\to\infty}
{1\over\overline K}
\log^+\|Q_{61,\overline K}^{red}\|.
```

Proof.

Conjugating the shell matrix \(D+O\) by the diagonal weight \(e^w\) leaves the
Casimir diagonal \(D\) unchanged and replaces \(O\) by the weighted
off-diagonal matrix.  If the weighted row sum is strictly below
\(\kappa_{\min}^{red}\), the Neumann/Gershgorin estimate gives

```math
\|(D+O)^{-1}\|_{\infty,w\to\infty,w}
\le
{1\over \kappa_{\min}^{red}-\Omega_*^{red}(w)},
```

uniformly in \(\overline K\).  Hence inverse amplification has zero
exponential growth in the weighted norm.  Converting back to the unweighted
norm costs the shell oscillation of \(w\), giving \(g_q^{red}\le g_w\), and
giving \(g_q^{red}=0\) when \(g_w=0\).  Without the strict margin, Paper 14's
shell-inverse discipline requires carrying the limsup exponent.  `square`

### Definition 88.7: Support-Growth Automaton Test

For a valid reduced edge certificate, form the zero-growth subgraph

```math
\overline{\mathfrak A}_{0}^{red}
:=
(\overline V,\{e\in\overline E_{esc}:\Delta_X(e)=0\}).
```

The reduced size-growth gate is

```math
\mathrm{P21\text{-}RED\text{-}SIZE}(c_{size}^{act})
```

and means that every reduced escaping path of length \(\overline K\) satisfies

```math
|X_f^{red}|\ge c_{size}^{act}\overline K.
```

The finite automaton criterion is:

1. if \(\overline{\mathfrak A}_{0}^{red}\) has no directed cycle, then
   `P21-RED-SIZE` holds with

   ```math
   c_{size}^{act}
   =
   {1\over L_0+1},
   ```

   where \(L_0\) is the maximum length of a directed path in
   \(\overline{\mathfrak A}_{0}^{red}\);
2. if \(\overline{\mathfrak A}_{0}^{red}\) has a directed cycle, then
   size-growth fails unless that cycle is added to the `BTQ` quotient, killed
   by an exact selector, or assigned to a separate carried tail.

### Lemma 88.8: Step 5 Geometry Is Decided By The Zero-Growth SCCs

The support-growth part of Step 5 is completely finite: it is decided by the
directed cycles of \(\overline{\mathfrak A}_{0}^{red}\).

Proof.

If the zero-growth subgraph is acyclic, a reduced path can take at most
\(L_0\) consecutive zero-growth edges before an edge with \(\Delta_X(e)\ge1\)
must occur.  Thus every block of \(L_0+1\) reduced escaping edges adds at
least one new support cell, proving the displayed \(c_{size}^{act}\).  If a
zero-growth directed cycle exists, iterating it gives arbitrarily large
reduced depth with no support growth, contradicting any positive
\(c_{size}^{act}\) unless the cycle is removed from the reduced escaping
tower by a separate exact operation.  `square`

### Definition 88.9: Reduced Decay Rate Certificate

A reduced decay certificate is one of the following.

1. A same-record reduced KP source

   ```math
   \mathrm{P21\text{-}FTS\text{-}REDKP}(\mu_{red}^{act},\alpha_{red})
   ```

   plus `P21-RED-SIZE(c_size^act)`.  It sets

   ```math
   m_{red}^{act}:=\mu_{red}^{act}c_{size}^{act}.
   ```

2. A direct projection-tail source proving

   ```math
   \sum_{\overline K\ge K}
   T_{\overline K}^{red,act}
   \le
   C e^{-m_{red}^{act}K}.
   ```

The certificate is invalid if its proof uses a Wilson-loop area law, mass
gap, continuum Yang-Mills existence, or an unrecorded microscopic local
process.  Paper 11's AF-locality machinery may be used only if it is applied
to the same declared active reduced tower and supplies the displayed
same-record bound.

### Theorem 88.10: Step 5 Is The Sole Remaining Analytic Source

Given `ACTFULLLAW`, valid reduced table data, and the weighted CMSSI outcome,
the only remaining non-finite input in the reduced inequality is the reduced
decay certificate of Definition 88.9.

At the current source level:

```math
\mathrm{P21\text{-}FTS\text{-}REDKP}
```

is not proved for the active common \(E_{14}/X_{13}\) tower, and no direct
projection-tail theorem is supplied.  Therefore \(m_{red}^{act}\) is not
certified positive by the present corpus.

Proof.

The finite table constants are Theorem 88.4.  The inverse exponent is Theorem
88.6.  Support growth is finite by Lemma 88.8.  What remains is the analytic
decay of the actual same-record reduced forced records.  Paper 14 proves that
KP/clustering/area-law estimates imply `FTS`; it explicitly does not prove
those estimates for actual continuum Yang-Mills.  Paper 11 supplies
conditional SC and AF locality mechanisms, but Section 1A of Paper 11 and
Lemma 87.5 show that they do not by themselves supply the active `SEL2`
surface source.  Hence a reduced KP or direct projection-tail theorem remains
the sole live source.  `square`

### Definition 88.11: Certified Margin Test

Given certificates for the finite and inverse pieces, define

```math
G_{red}^{cert}
:=
\log A_{esc}^{cert}
+\log C_{geom}^{cert}
+g_q^{cert},
```

where each certified value is either the exact value from
\(\mathsf C_{esc}^{red}\) or its safe envelope.  If a reduced decay
certificate is available, define

```math
\Delta_{red}^{cert}
:=
m_{red}^{cert}-G_{red}^{cert}.
```

The strict reduced branch passes exactly when

```math
\Delta_{red}^{cert}>0.
```

If no reduced decay certificate is available, the certified margin is
undefined, not positive.

### Theorem 88.12: Six-Step Inequality Verdict

Executing the six tasks gives the following final status.

1. **Reduced edge list.**  Finite and exactly certifiable by
   \(\mathsf C_{esc}^{red}\), but not explicitly tabulated in the current
   paper.
2. **\(C_{geom}^{red}\).**  Exact once the table is supplied; otherwise safely
   bounded by \(C_{geom}^{env}\).
3. **\(A_{esc}^{BTQ}\).**  Exact once edge coefficients and normal-form norms
   are supplied; otherwise safely bounded by \(A_{esc}^{env}\).
4. **\(g_q^{red}\).**  Zero under weighted `RED-CMSSI`; otherwise carried as
   \(g_q^{car}\).
5. **\(m_{red}^{act}\).**  Requires same-record reduced KP plus support
   growth, or a direct projection-tail theorem.  The current corpus does not
   supply it.
6. **Comparison.**  Therefore the inequality

   ```math
   m_{red}^{act}
   >
   \log A_{esc}^{BTQ}
   +\log C_{geom}^{red}
   +g_q^{red}
   ```

   is not certified as true by the present papers.  It is also not falsified,
   because the actual reduced table and the actual reduced decay exponent are
   not yet known.

Thus the rigorous current verdict is:

```math
\boxed{
\mathrm{carry}\bigl(E_{14}^{park}+X_{13}^{(26),SEL2}\bigr)
\quad\text{until }
\mathsf C_{esc}^{red}
\text{ and a reduced decay certificate are supplied.}
}
```

The obstruction has nevertheless been pushed to its limit: bounded-collar
algebra is closed by `ACTFULLLAW`; finite escaping entropy and coefficients
are computable by \(\mathsf C_{esc}^{red}\); inverse amplification is a
weighted CMSSI test; the only genuinely analytic missing theorem is reduced
forced-tail decay on the same active record law.

Proof.

Items 1--3 are Theorem 88.4.  Item 4 is Theorem 88.6.  Item 5 is Theorem
88.10.  Item 6 is Definition 88.11 and Theorem 87.6.  The carry rule is
Corollary 87.7.  `square`

### Corollary 88.13: What Would Settle It Next

There are now only two productive next moves.

1. **Finite-table move.**  Supply \(\mathsf C_{esc}^{red}\), compute
   \(A_{esc}^{BTQ}\), \(C_{geom}^{red}\), test weighted CMSSI, and decide
   `RED-SIZE` by zero-growth SCCs.
2. **Analytic-source move.**  Prove the same-record reduced KP/projection-tail
   estimate that supplies \(m_{red}^{act}\).

Doing the finite-table move first is preferable: it tells the analytic source
exactly what exponent must be beaten and may reveal a zero-growth SCC that
must be quotiented before any KP estimate can possibly prove the inequality.

## 89. Instantiating The Reduced Escaping Edge Table

Section 88 gives the certificate format.  This section pushes Tasks 1--2 one
level further by instantiating the actual edge classes allowed by the previous
papers.  The outcome is a class-level reduced table and sharp formulas for
\(C_{geom}^{red}\) and \(A_{esc}^{BTQ}\).  A numerical value still requires
the finite transition table, but there is no longer any ambiguity about what
must be counted.

### Definition 89.1: Allowed Reduced Escaping Edge Classes

On the strict `ACTFULLLAW` branch, after deleting lower-shell retractions,
contracting bounded-collar stagnant/channel SCCs, and excluding debits already
assigned to \(U_{11}^{RPCov,car,SEL2}\) and \(U_{13}^{RPF,bd}\), the reduced
escaping edge set is the disjoint union

```math
\overline E_{esc}
=
\mathcal E_{SD}
\dot\cup
\mathcal E_{act}
\dot\cup
\mathcal E_{fus}
\dot\cup
\mathcal E_{cmp}.
```

The four classes are:

| class | source | meaning | not included |
| --- | --- | --- | --- |
| \(\mathcal E_{SD}\) | Paper-14 compact-group Schwinger-Dyson/Casimir identities | one projected SD/Casimir row creates a non-retracting forced record outside the contracted bounded-collar state | bounded-collar power cycles already absorbed by `BTQ` |
| \(\mathcal E_{act}\) | active local action-stencil/product rows | a local action-density or finite product insertion creates a new reduced forced record | global decoration debit \(D_{dec}^{SEL2}\) and already-paid KP decoration |
| \(\mathcal E_{fus}\) | finite channel/fusion closure inside \(\Lambda_*\) | representation-channel lift or finite Clebsch-Gordan/fusion expansion needed by the same reduced row | representation tails outside \(\Lambda_*\), which remain in the declared tail budget |
| \(\mathcal E_{cmp}\) | common \(E_{14}/X_{13}\) comparison tower | finite Paper-14/\(X_{13}\) comparison step not already covered by bounded-collar `ACTFULLLAW` | separate exact-entry residuals \(RPF\), `KPdec`, `WP`, and Paper-16 RP/Cov carries |

No fifth hidden class is allowed.  In particular, an edge that is really a
projective/covariance transport defect is charged to \(U_{11}^{RPCov}\), not
to \(\overline E_{esc}\); an edge that is an exact-entry residual-factorization
defect is charged to \(U_{13}^{RPF,bd}\); and an edge that stays inside the
bounded collar is a `BTQ` state transition, not reduced escape.

### Lemma 89.2: Exhaustion Of Reduced Escaping Edges

Every non-retracting reduced escaping edge in the common \(E_{14}/X_{13}\)
tower belongs to exactly one of the four classes in Definition 89.1.

Proof.

The raw forced transition sources are Paper-14 projected SD/loop identities,
local action-density/product insertions, finite representation-channel
bookkeeping, and the common Paper-14/\(X_{13}\) comparison records isolated in
Sections 61--67.  Sections 74--85 contract bounded-collar stagnant and channel
cycles into `BTQ`/`ACTFULLLAW` records.  Sections 30--36 and 67 keep RP/Cov,
RPF, entry `KPdec`, and whole-process mismatch in disjoint carried slots.
After those exclusions, an external non-retracting edge is either created by
the SD/Casimir row, by an action/product insertion, by a finite fusion/channel
lift, or by the common comparison tower.  The debit-exclusion conventions make
the classes disjoint.  `square`

### Definition 89.3: Class Counts And Coefficient Ceilings

For \(c\in\{SD,act,fus,cmp\}\), define the class out-degree

```math
C_c^{out}
:=
\max_{\bar v\in\overline V}
\#\{e\in\mathcal E_c:s(e)=\bar v\},
```

and the class coefficient ceiling

```math
A_c^{BTQ}
:=
\max_{e\in\mathcal E_c}\max(1,a(e)).
```

If a class is empty, set \(C_c^{out}=0\) and \(A_c^{BTQ}=1\).

For pass certification before the exact table is enumerated, introduce raw
class ceilings \(A_c^{raw}\) and normal-form insertion norms
\(B_{c,s},B_{c,t}\) such that

```math
a(e)\le B_{c,s}B_{c,t}a^{raw}(e)
\quad(e\in\mathcal E_c).
```

Then

```math
A_c^{BTQ}
\le
\max(1,B_{c,s}B_{c,t}A_c^{raw})
\le
\max(1,(B_{BTQ}^{61})^2A_c^{raw}).
```

The last inequality is the universal safe bound.  The edge certificate should
use the sharper class-specific \(B_{c,s},B_{c,t}\) whenever available.

### Theorem 89.4: Task 1 Edge List At Class Level

The reduced escaping edge list is now instantiated to the finite class table

```math
\boxed{
\overline E_{esc}
=
\mathcal E_{SD}
\dot\cup
\mathcal E_{act}
\dot\cup
\mathcal E_{fus}
\dot\cup
\mathcal E_{cmp}.
}
```

The exact Task-1 table is obtained by listing, for each class \(c\):

```math
\mathcal E_c
=
\{(\bar v,\bar v',\tau,a,\Delta_X,\mathcal O):
\tau\in c\}.
```

This is a finite enumeration in the data

```math
(N,r_A,\Lambda_*,D_{prod}^{act},Y_{61}^{BTQ})
```

and no continuum or area-law input is needed.

Proof.

Finiteness follows from Lemma 88.2.  The four-class exhaustion is Lemma
89.2.  The displayed tuple is exactly the certificate data of Definition
88.1 restricted to one class.  `square`

### Theorem 89.5: Task 2 Formula For \(C_{geom}^{red}\)

Given the class table, the exact reduced geometric branching constant is

```math
C_{geom}^{red}
=
\max_{\bar v\in\overline V}
\left(
\#\mathcal E_{SD}(\bar v)
+\#\mathcal E_{act}(\bar v)
+\#\mathcal E_{fus}(\bar v)
+\#\mathcal E_{cmp}(\bar v)
\right),
```

where \(\mathcal E_c(\bar v):=\{e\in\mathcal E_c:s(e)=\bar v\}\).

Consequently,

```math
C_{geom}^{red}
\le
C_{SD}^{out}
+C_{act}^{out}
+C_{fus}^{out}
+C_{cmp}^{out}
\le
C_{geom}^{env}.
```

The first inequality is sharp if the maximizing class out-degrees do not occur
at the same reduced vertex; it is exact if they do.

Proof.

By Definition 75.9 and Definition 88.3,
\(C_{geom}^{red}\) is the maximum number of escaping outgoing edges from a
reduced vertex.  The disjoint class decomposition in Theorem 89.4 splits that
outgoing set into the four displayed class subsets.  Taking the maximum gives
the exact formula.  Bounding each summand by its class maximum gives the first
inequality, and the ambient Paper-14 branching envelope gives the second.
`square`

### Theorem 89.6: Task 2 Formula For \(A_{esc}^{BTQ}\)

Given the class table, the exact reduced coefficient-growth base is

```math
A_{esc}^{BTQ}
=
\max\left(
1,
A_{SD}^{BTQ},
A_{act}^{BTQ},
A_{fus}^{BTQ},
A_{cmp}^{BTQ}
\right).
```

Before exact edge coefficients are tabulated, the certified class envelope is

```math
A_{esc}^{BTQ}
\le
\max\left(
1,
B_{SD,s}B_{SD,t}A_{SD}^{raw},
B_{act,s}B_{act,t}A_{act}^{raw},
B_{fus,s}B_{fus,t}A_{fus}^{raw},
B_{cmp,s}B_{cmp,t}A_{cmp}^{raw}
\right),
```

and the universal fallback is

```math
A_{esc}^{BTQ}
\le
\max\left(
1,
(B_{BTQ}^{61})^2
\max(A_{SD}^{raw},A_{act}^{raw},A_{fus}^{raw},A_{cmp}^{raw})
\right).
```

Proof.

By Definition 88.3, \(A_{esc}^{BTQ}\) is the maximum of \(\max(1,a(e))\) over
all reduced escaping edges.  The disjoint class decomposition lets us take the
maximum first inside each class, giving the exact class formula.  The
normal-form insertion estimate of Definition 89.3 gives the class envelope
and then the universal fallback.  `square`

### Corollary 89.7: Current Step-1/Step-2 Verdict

Tasks 1 and 2 are now complete up to the actual finite enumeration.

What is proved:

```math
\overline E_{esc}
=
\mathcal E_{SD}
\dot\cup
\mathcal E_{act}
\dot\cup
\mathcal E_{fus}
\dot\cup
\mathcal E_{cmp},
```

```math
C_{geom}^{red}
=
\max_{\bar v}
\sum_c\#\mathcal E_c(\bar v),
```

and

```math
A_{esc}^{BTQ}
=
\max(1,A_{SD}^{BTQ},A_{act}^{BTQ},A_{fus}^{BTQ},A_{cmp}^{BTQ}).
```

What is not yet supplied is the row-by-row finite list of class edges and
their numerical coefficient values.  Therefore Paper 21 may use the class
formulas and safe envelopes in the reduced inequality, but it may not claim a
numerical pass or failure until the concrete table
\(\mathsf C_{esc}^{red}\) is supplied.

## 90. Zero-Growth SCC Test For Reduced Size Growth

Section 89 instantiated the reduced escaping edge classes.  Before proving a
reduced KP bound, we must know whether reduced depth actually forces growth
of the reduced support polymer.  This is a finite graph question.

### Definition 90.1: Zero-Growth Subgraph

Given a reduced escaping edge certificate
\(\mathsf C_{esc}^{red}\), define the zero-growth edge set

```math
\overline E_{0}^{red}
:=
\{e\in\overline E_{esc}:\Delta_X(e)=0\}.
```

The zero-growth subgraph is

```math
\overline{\mathfrak A}_{0}^{red}
:=
(\overline V,\overline E_{0}^{red}).
```

For each class \(c\in\{SD,act,fus,cmp\}\), set

```math
\mathcal E_{c,0}
:=
\mathcal E_c\cap\overline E_{0}^{red}.
```

Thus

```math
\overline E_0^{red}
=
\mathcal E_{SD,0}
\dot\cup
\mathcal E_{act,0}
\dot\cup
\mathcal E_{fus,0}
\dot\cup
\mathcal E_{cmp,0}.
```

### Definition 90.2: Zero-Growth Cycle Classes

A directed cycle in \(\overline{\mathfrak A}_{0}^{red}\) is classified by the
set of edge classes it uses.

1. **BTQ-missed cycle.**  Every edge is a bounded-collar stagnant/channel edge
   that should have been internal to the `BTQ`/`ACTFULLLAW` state.
2. **Fusion-only cycle.**  The cycle uses only finite channel/fusion edges in
   \(\mathcal E_{fus,0}\).
3. **Comparison-only cycle.**  The cycle uses only common comparison edges in
   \(\mathcal E_{cmp,0}\).
4. **Action/SD zero-growth cycle.**  The cycle uses at least one edge from
   \(\mathcal E_{SD,0}\cup\mathcal E_{act,0}\).

The first three are bookkeeping obstructions: they must be quotiented,
assigned to same-shell inverse control, or moved back into the already
declared comparison battery.  The fourth is a genuine obstruction to reduced
size growth unless it is killed by a new exact identity or selector.

### Lemma 90.3: Acyclic Zero-Growth Graph Gives A Size Constant

If \(\overline{\mathfrak A}_{0}^{red}\) is acyclic, let \(L_0\) be the maximum
length of a directed path in it.  Then every reduced escaping path \(f\)
satisfies

```math
|X_f^{red}|
\ge
{1\over L_0+1}\,\overline K(f).
```

In particular,

```math
\mathrm{P21\text{-}RED\text{-}SIZE}(c_{size}^{act})
```

holds with

```math
c_{size}^{act}={1\over L_0+1}.
```

Since \(L_0\le|\overline V|-1\), the rough table-free lower bound is

```math
c_{size}^{act}\ge {1\over|\overline V|}.
```

Proof.

An acyclic finite directed graph has no directed path longer than \(L_0\).
Therefore a reduced escaping path can contain at most \(L_0\) consecutive
zero-growth edges.  Every block of \(L_0+1\) reduced escaping edges contains
at least one edge with \(\Delta_X(e)\ge1\), hence adds at least one support
cell to \(X_f^{red}\).  Summing over blocks gives the displayed bound, with
the finite remainder absorbed by weakening to the same constant.  The
inequality \(L_0\le|\overline V|-1\) is the standard longest-path bound for a
finite acyclic directed graph.  `square`

### Lemma 90.4: A Zero-Growth Cycle Falsifies Size Growth Until Repaired

If \(\overline{\mathfrak A}_{0}^{red}\) contains a directed cycle that remains
in the reduced escaping tower, then no positive \(c_{size}^{act}\) can satisfy

```math
|X_f^{red}|\ge c_{size}^{act}\overline K(f)
```

for all reduced paths.

Proof.

Iterating the zero-growth cycle \(n\) times gives reduced depth increasing
linearly in \(n\), while \(|X_f^{red}|\) remains unchanged along the cycle.
For any fixed \(c_{size}^{act}>0\), the inequality fails for sufficiently
large \(n\).  `square`

### Definition 90.5: Zero-Growth Repair Gate

The repair gate

```math
\mathrm{P21\text{-}RED\text{-}ZGREP}
```

holds when every directed cycle of \(\overline{\mathfrak A}_{0}^{red}\) is
assigned to one of the following repairs:

1. **BTQ completion:** the cycle is moved into the bounded-collar
   `ACTFULLLAW` state and removed from \(\overline E_{esc}\);
2. **same-shell inverse placement:** a fusion-only cycle is assigned to the
   reduced CMSSI/right-inverse ledger and not counted as reduced escape;
3. **comparison-battery placement:** a comparison-only cycle is assigned to
   the common \(E_{14}/X_{13}\) finite comparison battery and not counted as
   reduced escape;
4. **exact zero selector:** an action/SD zero-growth cycle is proved to have
   zero coefficient by a same-record identity;
5. **carried residual:** the cycle is removed from the pass branch and its
   full contribution is carried as a new explicit residual

   ```math
   U_{ZG}^{red}.
   ```

After applying the repairs, write
\(\overline{\mathfrak A}_{0,rep}^{red}\) for the remaining zero-growth
subgraph.

### Theorem 90.6: Zero-Growth SCC Test

The reduced size-growth gate has the following exact finite verdict.

1. If \(\overline{\mathfrak A}_{0}^{red}\) is acyclic, then

   ```math
   \mathrm{P21\text{-}RED\text{-}SIZE}\left({1\over L_0+1}\right)
   ```

   holds.

2. If \(\overline{\mathfrak A}_{0}^{red}\) has directed cycles and
   `P21-RED-ZGREP` repairs all of them so that
   \(\overline{\mathfrak A}_{0,rep}^{red}\) is acyclic, then the repaired
   pass branch has

   ```math
   \mathrm{P21\text{-}RED\text{-}SIZE}\left({1\over L_{0,rep}+1}\right),
   ```

   and the worksheet must add \(U_{ZG}^{red}\) for any carried residual cycle.

3. If a directed zero-growth action/SD cycle remains unrepaired, then
   `P21-RED-SIZE(c)` fails for every \(c>0\), and the reduced KP route cannot
   supply a positive linear forced-depth exponent.

Proof.

Item 1 is Lemma 90.3.  Item 2 applies Lemma 90.3 after the finite repair
operation and records the carried residual required by Definition 90.5.  Item
3 is Lemma 90.4, with the action/SD qualifier identifying the cycle as a
genuine reduced-escape obstruction rather than a bookkeeping edge that should
have been placed elsewhere.  `square`

### Corollary 90.7: Current Status Of Step 3

Step 3 is now reduced to a finite SCC computation on
\(\overline{\mathfrak A}_{0}^{red}\).

What is proved:

```math
\overline E_0^{red}
=
\mathcal E_{SD,0}
\dot\cup
\mathcal E_{act,0}
\dot\cup
\mathcal E_{fus,0}
\dot\cup
\mathcal E_{cmp,0},
```

and the pass/fail/repair criterion is Theorem 90.6.

What is not yet supplied is the actual finite edge certificate needed to
decide whether \(\overline{\mathfrak A}_{0}^{red}\) is acyclic.  Therefore
Paper 21 may not yet claim a positive \(c_{size}^{act}\), but it has reduced
the question to a finite directed-SCC audit with a precise repair rule.

## 91. Weighted CMSSI Audit For \(g_q^{red}\)

Sections 88--90 reduce the finite geometry side.  This section executes Step
4: decide whether inverse amplification contributes no exponent, or must be
carried as \(g_q^{red}\).  The key point is that a weighted diagonal-dominance
bound is useful only after paying the cost of converting the weighted norm
back to the ordinary finite-record norm.

### Definition 91.1: Reduced Shell Labels

Let \(F_{\overline K}^{red}\) be the reduced shell at depth \(\overline K\).
Each shell coordinate \(\alpha\in F_{\overline K}^{red}\) carries the finite
labels

```math
\alpha
=
(T_\alpha,\mu_\alpha,X_\alpha,h_\alpha,p_\alpha,\sigma_\alpha).
```

Here:

1. \(T_\alpha\) is the reduced template type;
2. \(\mu_\alpha\in\Lambda_*\) is the active representation/channel label;
3. \(X_\alpha=X_\alpha^{red}\) is the reduced support polymer;
4. \(h_\alpha\) is a finite channel/fusion-complexity index;
5. \(p_\alpha\) is the active product or comparison-battery degree label;
6. \(\sigma_\alpha\) stores the finite symmetry/paired-real convention.

The diagonal Casimir lower bound is

```math
\kappa_{\min}^{red}
:=
\inf_{\overline K}
\min_{\alpha\in F_{\overline K}^{red}}
C_2(\mu_\alpha),
```

after deleting trivial and lower-shell coordinates.  On the fundamental
`SU(N)` branch,

```math
\kappa_{\min}^{red}
\ge
C_{\rm fund}(N)
=
{N^2-1\over 2N}.
```

### Definition 91.2: Escape-Favoring Weight Family

For nonnegative parameters

```math
\mathbf a=(a_X,a_C,a_h,a_p)\in[0,\infty)^4,
```

define the real exponent weight

```math
w_{\mathbf a}(\alpha)
:=
-a_X|X_\alpha|
-a_C C_2(\mu_\alpha)
-a_h h_\alpha
-a_p p_\alpha.
```

For an edge \(e:\alpha\to\beta\), write

```math
\Delta_X(e)=|X_\beta|-|X_\alpha|,
\quad
\Delta_C(e)=C_2(\mu_\beta)-C_2(\mu_\alpha),
```

and similarly \(\Delta_h(e),\Delta_p(e)\).  Then

```math
e^{w_{\mathbf a}(\beta)-w_{\mathbf a}(\alpha)}
=
\exp\{-a_X\Delta_X(e)-a_C\Delta_C(e)
-a_h\Delta_h(e)-a_p\Delta_p(e)\}.
```

This sign convention rewards outward support growth and higher channel
complexity by making those edges smaller in the weighted row sum.  If an edge
decreases one of these labels, the exact finite table must pay the resulting
factor.

The shell oscillation of the weight is

```math
\operatorname{osc}_{\overline K}(w_{\mathbf a})
:=
\sup_{\alpha,\beta\in F_{\overline K}^{red}}
|w_{\mathbf a}(\alpha)-w_{\mathbf a}(\beta)|.
```

Its exponential spread rate is

```math
g_w(\mathbf a)
:=
\limsup_{\overline K\to\infty}
{1\over\overline K}
\operatorname{osc}_{\overline K}(w_{\mathbf a}).
```

If support size varies linearly across a shell, a nonzero \(a_X\) contributes
to \(g_w\).  If \(\Lambda_*\), \(h_\alpha\), and \(p_\alpha\) are uniformly
bounded on the active full-law branch, then \(a_C,a_h,a_p\) contribute no
exponential spread.

### Definition 91.3: Classwise Weighted Off-Diagonal Sums

For each class \(c\in\{SD,act,fus,cmp\}\), define

```math
\Omega_c(\mathbf a)
:=
\sup_{\alpha}
\sum_{\substack{e\in\mathcal E_c\\s(e)=\alpha}}
|\mathcal O(e)|
\exp\{-a_X\Delta_X(e)-a_C\Delta_C(e)
-a_h\Delta_h(e)-a_p\Delta_p(e)\}.
```

The total weighted off-diagonal row sum is

```math
\Omega_{tot}^{red}(\mathbf a)
:=
\Omega_{SD}(\mathbf a)
+\Omega_{act}(\mathbf a)
+\Omega_{fus}(\mathbf a)
+\Omega_{cmp}(\mathbf a).
```

Before the exact edge table is supplied, use class envelopes:

```math
\Omega_c(\mathbf a)
\le
C_c^{out}\,
O_c^{max}\,
\exp\Big(
\sup_{e\in\mathcal E_c}
[-a_X\Delta_X(e)-a_C\Delta_C(e)-a_h\Delta_h(e)-a_p\Delta_p(e)]
\Big),
```

where

```math
O_c^{max}:=\max_{e\in\mathcal E_c}|\mathcal O(e)|.
```

This is deliberately a row-sum bound, not a coefficient-growth bound.  The
\(A_{esc}^{BTQ}\) constants belong to the forced-tail coefficient side; the
\(\Omega_c\) constants belong to shell inversion.

### Theorem 91.4: Weighted CMSSI Pass Criterion

If there exists \(\mathbf a\in[0,\infty)^4\) such that

```math
\Omega_{tot}^{red}(\mathbf a)
<
\kappa_{\min}^{red},
```

then the reduced shell right inverses satisfy

```math
g_q^{red}
\le
g_w(\mathbf a).
```

In particular, if \(g_w(\mathbf a)=0\), then

```math
g_q^{red}=0.
```

Proof.

The weighted row-sum inequality is exactly `P21-RED-CMSSI(w_a)` from
Definition 88.5, decomposed by the four edge classes of Definition 89.1.
The weighted Neumann/Gershgorin estimate gives a uniform bound in the weighted
norm:

```math
\|Q_{\overline K}^{red}\|_{w_{\mathbf a}}
\le
{1\over \kappa_{\min}^{red}-\Omega_{tot}^{red}(\mathbf a)}.
```

For vectors on the finite shell, the ordinary and weighted \(\ell^\infty\)
norms differ by at most
\(\exp(\operatorname{osc}_{\overline K}(w_{\mathbf a}))\).  Therefore

```math
\|Q_{\overline K}^{red}\|_{\infty\to\infty}
\le
\exp(\operatorname{osc}_{\overline K}(w_{\mathbf a}))
{1\over \kappa_{\min}^{red}-\Omega_{tot}^{red}(\mathbf a)}.
```

Taking \(\overline K^{-1}\log^+\) and the limsup gives
\(g_q^{red}\le g_w(\mathbf a)\).  If the spread rate is zero, the inverse
growth exponent is zero.  `square`

### Corollary 91.5: Finite Optimization Form Of Step 4

Step 4 is the finite optimization problem

```math
g_{q,cert}^{red}
:=
\inf_{\mathbf a}
\left\{
g_w(\mathbf a):
\Omega_{tot}^{red}(\mathbf a)<\kappa_{\min}^{red}
\right\}.
```

If the feasible set is nonempty, then

```math
g_q^{red}\le g_{q,cert}^{red}.
```

If the feasible set contains a zero-spread weight, then \(g_q^{red}=0\).  If
the feasible set is empty and no other all-depth right-inverse certificate is
proved, the paper must carry

```math
g_q^{red}=g_q^{car}.
```

### Theorem 91.6: Executing The Requested Five CMSSI Steps

The five requested CMSSI tasks now have exact status.

1. **Reduced shell labels.**  Defined in Definition 91.1.
2. **Weight choice.**  The escape-favoring family
   \(w_{\mathbf a}\) is fixed in Definition 91.2.  It includes support size,
   Casimir, channel complexity, and product/comparison degree.
3. **Classwise off-diagonal bounds.**  The four pieces

   ```math
   \Omega_{SD},\quad\Omega_{act},\quad\Omega_{fus},\quad\Omega_{cmp}
   ```

   are defined in Definition 91.3, with finite class-envelope bounds.
4. **Casimir comparison.**  The pass condition is

   ```math
   \Omega_{SD}(\mathbf a)
   +\Omega_{act}(\mathbf a)
   +\Omega_{fus}(\mathbf a)
   +\Omega_{cmp}(\mathbf a)
   <
   \kappa_{\min}^{red}
   ```

   with

   ```math
   \kappa_{\min}^{red}\ge {N^2-1\over2N}
   ```

   on the fundamental branch.
5. **Conclusion.**  If a feasible zero-spread weight exists, set
   \(g_q^{red}=0\).  If only positive-spread weights are feasible, carry the
   certified value \(g_{q,cert}^{red}\).  If no feasible weight is known, keep
   \(g_q^{car}\).

At the current source level, the exact finite edge certificate is not yet
supplied, so Paper 21 cannot assert feasibility of the optimization problem.
It can, however, use this finite CMSSI audit as the required Step-4 test.

Proof.

Items 1--3 are Definitions 91.1--91.3.  Item 4 is Theorem 91.4 with the
Casimir lower bound of Definition 91.1.  Item 5 is Corollary 91.5.  The final
status follows because the quantities \(\mathcal O(e)\), class out-degrees,
and edge label increments are entries of the finite reduced certificate
\(\mathsf C_{esc}^{red}\), which has not yet been tabulated.  `square`

### Corollary 91.7: Updated Reduced Inequality

After the weighted CMSSI audit, the reduced inequality may be tested with

```math
g_q^{red}
=
\begin{cases}
0, & \text{if a zero-spread feasible weight is certified},\\
g_{q,cert}^{red}, & \text{if only positive-spread feasible weights are certified},\\
g_q^{car}, & \text{if no feasible weight/right inverse is certified}.
\end{cases}
```

Thus the next remaining source after the finite table and CMSSI tests is the
analytic reduced decay certificate for \(m_{red}^{act}\).

## 92. The Finite Reduced Escape Table

Sections 88--91 define the certificate format, the edge classes, the
zero-growth test, and the weighted inverse test.  This section writes the
finite table itself.  The table is finite and executable at the level licensed
by the preceding papers: it names the finite vertex coordinates, the finite
transition index sets, the coefficient slots, the support-growth increments,
and the row sums that feed \(C_{geom}^{red}\), \(A_{esc}^{BTQ}\), and
\(\Omega_{tot}^{red}\).

It still does not insert numerical action coefficients or Clebsch-Gordan
tables, because those are not tabulated in Papers 10--14 or Paper 20.  The
point is sharper: after this section, the only missing finite input is a
literal enumeration of the finite indices below.  There is no hidden fifth
edge class and no continuum premise in the table.

### Definition 92.1: Finite Vertex Coordinates

Let

```math
\mathfrak T_{red}^{act}
```

be the finite list of reduced active template types after the
`BTQ/ACTFULLLAW` contraction of Sections 75 and 85.  Let
\(\mathfrak L_{red}^{act}\) be the finite list of rooted local frontier
types: the reduced support shape seen in one action-range collar, modulo
translation, lattice symmetries allowed by the selector, paired-real
normalization, and the physical quotient of Definition 84.1.  The absolute
support polymer \(X_\alpha^{red}\) is not a vertex coordinate; only its local
frontier type is.

The finite reduced vertex set used by the table is

```math
\overline V_{92}
:=
\left\{
(T,\mu,\ell,h,p,\sigma):
T\in\mathfrak T_{red}^{act},\
\mu\in\Lambda_*,\
\ell\in\mathfrak L_{red}^{act},\
0\le h\le h_*^{act},\
0\le p\le p_*^{act},\
\sigma\in\Sigma_*^{act}
\right\}
/\!\sim_{phys}.
```

Here \(h\) is the finite channel/fusion-complexity label, \(p\) is the active
product/comparison degree label, and \(\sigma\) records orientation,
paired-real, center, and reflection conventions.  The quotient
\(\sim_{phys}\) deletes only trivial/lower-shell coordinates and declared
symmetries; it does not identify two records whose scalar readouts differ on
the same pushed-forward law.

The shell coordinate used in Section 91 is then

```math
\alpha=(\bar v,X_\alpha^{red}),
\qquad
\bar v\in\overline V_{92}.
```

This keeps the finite table finite while still letting support size grow.

### Definition 92.2: Finite Transition Index Sets

The reduced escape table is generated by four finite transition index sets.

1. **Schwinger-Dyson/Casimir indices.**  The finite set is denoted
   \(\Xi_{SD}\).  An element \(\xi\in\Xi_{SD}\) records a projected compact-group
   Schwinger-Dyson or Casimir row: local differentiated link, generator
   contraction, source template, target template, active representation
   channel, and the selected identity-channel projection.

2. **Action/product indices.**  The finite set is denoted
   \(\Xi_{act}\).  An element \(\xi\in\Xi_{act}\) records one active local
   action-stencil or finite product insertion: plaquette/stencil position
   relative to the frontier, action representation label, product slot, and
   target reduced template.

3. **Finite fusion/channel indices.**

   ```math
   \Xi_{fus}
   :=
   \{(\mu,\lambda,\mu',m):
   \mu,\lambda,\mu'\in\Lambda_*,
   1\le m\le N_{\mu,\lambda}^{\mu'}\}.
   ```

   Here \(N_{\mu,\lambda}^{\mu'}\) is the finite Clebsch-Gordan multiplicity
   inside the declared representation cutoff.  Terms outside
   \(\Lambda_*\) are not table edges; they belong to the representation-tail
   budget.

4. **Common comparison indices.**  The finite set is denoted
   \(\Xi_{cmp}\).  An element \(\xi\in\Xi_{cmp}\) records one finite
   comparison move in the common \(E_{14}/X_{13}\) battery: Paper-14 export
   seed, \(X_{13}\) dynamic seed, orientation/reflection choice, and
   comparison-battery slot.

Each \(\Xi_c\) is finite for fixed

```math
(N,r_A,\Lambda_*,D_{prod}^{act},Y_{61}^{BTQ}).
```

This is exactly the finite-generation content of Lemma 88.2, specialized to
the four classes of Definition 89.1.

### Definition 92.3: Row Maps

For each \(c\in\{SD,act,fus,cmp\}\), define a partial row map

```math
R_c:
\overline V_{92}\times\Xi_c
\dashrightarrow
\overline V_{92}\times\mathbb N
\times\mathbb Z\times\mathbb Z\times\mathbb Z
\times[0,\infty)\times[0,\infty).
```

If \(R_c(\bar v,\xi)\) is defined, write

```math
R_c(\bar v,\xi)
=
(\bar v',\Delta_X,\Delta_C,\Delta_h,\Delta_p,a,\mathcal O).
```

The entries mean:

1. \(\bar v'\) is the reduced target vertex after lower-shell retractions and
   physical quotients;
2. \(\Delta_X\) is the number of new reduced support cells added by the row;
3. \(\Delta_C,\Delta_h,\Delta_p\) are the Casimir, channel-complexity, and
   product/comparison increments used in Section 91;
4. \(a\) is the absolute identity-channel coefficient after inserting the
   `BTQ` normal forms required at the source and target;
5. \(\mathcal O\) is the absolute same-shell off-diagonal coupling used in
   the reduced shell inverse audit.

The map is undefined when the raw local row is a lower-shell retraction,
an internal bounded-collar `BTQ` transition, an already assigned
\(U_{11}^{RPCov}\) transport defect, an \(U_{13}^{RPF}\) exact-entry defect,
or a representation-tail term outside the active cutoff.

### Table 92.4: Reduced Escape Rows

The finite reduced table is the following row schema.

| row | finite index | source and target | coefficient slot | support increment | inverse slot | zero-growth disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `SD` | \(\xi\in\Xi_{SD}\) | \(\bar v\to\bar v'\) by \(R_{SD}\) | \(a_{SD}(\bar v,\xi)\le B_{SD,s}B_{SD,t}a_{SD}^{raw}(\bar v,\xi)\) | \(\Delta_X^{SD}(\bar v,\xi)\) | \(\mathcal O_{SD}(\bar v,\xi)\) | if \(\Delta_X=0\), it is an action/SD zero-growth row and must pass the Section-90 repair gate |
| `act` | \(\xi\in\Xi_{act}\) | \(\bar v\to\bar v'\) by \(R_{act}\) | \(a_{act}(\bar v,\xi)\le B_{act,s}B_{act,t}a_{act}^{raw}(\bar v,\xi)\) | \(\Delta_X^{act}(\bar v,\xi)\) | \(\mathcal O_{act}(\bar v,\xi)\) | if \(\Delta_X=0\), it is an action/SD zero-growth row and must pass the Section-90 repair gate |
| `fus` | \(\xi\in\Xi_{fus}\) | \(\bar v\to\bar v'\) by \(R_{fus}\) | \(a_{fus}(\bar v,\xi)\le B_{fus,s}B_{fus,t}N_{\mu,\lambda}^{\mu'}\) | \(\Delta_X^{fus}(\bar v,\xi)\) | \(\mathcal O_{fus}(\bar v,\xi)\) | zero-growth rows are same-shell channel bookkeeping unless they also change support; assign them to CMSSI or quotient them |
| `cmp` | \(\xi\in\Xi_{cmp}\) | \(\bar v\to\bar v'\) by \(R_{cmp}\) | \(a_{cmp}(\bar v,\xi)\le B_{cmp,s}B_{cmp,t}a_{cmp}^{raw}(\bar v,\xi)\) | \(\Delta_X^{cmp}(\bar v,\xi)\) | \(\mathcal O_{cmp}(\bar v,\xi)\) | zero-growth rows stay in the common comparison battery unless a non-retracting comparison escape is certified |

The actual edge sets are

```math
\mathcal E_c^{92}
:=
\{(\bar v,\bar v',c,\xi,a,\mathcal O,\Delta_X,\Delta_C,\Delta_h,\Delta_p):
R_c(\bar v,\xi)\ \text{is defined}\}.
```

Thus

```math
\overline E_{esc}^{92}
=
\mathcal E_{SD}^{92}
\dot\cup
\mathcal E_{act}^{92}
\dot\cup
\mathcal E_{fus}^{92}
\dot\cup
\mathcal E_{cmp}^{92}.
```

This is the finite table.  Filling it numerically means enumerating the
finite sets \(\overline V_{92}\) and \(\Xi_c\), applying the four row maps,
and deleting undefined rows by the exclusion rules above.

### Definition 92.5: The Zero-Growth Subtable

For each class \(c\), split

```math
\mathcal E_c^{+}
:=
\{e\in\mathcal E_c^{92}:\Delta_X(e)\ge1\},
\qquad
\mathcal E_c^{0}
:=
\{e\in\mathcal E_c^{92}:\Delta_X(e)=0\}.
```

The zero-growth subtable is

```math
\overline E_{0}^{92}
=
\mathcal E_{SD}^{0}
\dot\cup
\mathcal E_{act}^{0}
\dot\cup
\mathcal E_{fus}^{0}
\dot\cup
\mathcal E_{cmp}^{0}.
```

Rows in \(\mathcal E_{fus}^{0}\) are assigned first to reduced CMSSI;
rows in \(\mathcal E_{cmp}^{0}\) are assigned first to the finite comparison
battery.  Rows in
\(\mathcal E_{SD}^{0}\cup\mathcal E_{act}^{0}\) are the only dangerous
zero-growth rows.  They must be killed by an exact selector, moved into
`BTQ/ACTFULLLAW`, or carried as \(U_{ZG}^{red}\).  If any such row lies on a
directed zero-growth SCC after the repairs, the reduced size-growth source
fails by Lemma 90.4.

### Theorem 92.6: Exact Constants From The Table

For the table of Definition 92.4,

```math
C_{geom}^{red}
=
\max_{\bar v\in\overline V_{92}}
\sum_{c\in\{SD,act,fus,cmp\}}
\#\{e\in\mathcal E_c^{92}:s(e)=\bar v\}.
```

The coefficient base is

```math
A_{esc}^{BTQ}
=
\max\left(
1,\max_{e\in\overline E_{esc}^{92}}a(e)
\right).
```

Equivalently,

```math
A_{esc}^{BTQ}
=
\max(1,A_{SD}^{BTQ},A_{act}^{BTQ},A_{fus}^{BTQ},A_{cmp}^{BTQ}).
```

The weighted CMSSI row sum is

```math
\Omega_{tot}^{red}(\mathbf a)
=
\max_{\bar v}
\sum_{c}
\sum_{\substack{e\in\mathcal E_c^{92}\\s(e)=\bar v}}
\mathcal O(e)
\exp\{-a_X\Delta_X(e)-a_C\Delta_C(e)
-a_h\Delta_h(e)-a_p\Delta_p(e)\}.
```

Thus the same finite table computes all three finite quantities needed before
the analytic decay source:

```math
C_{geom}^{red},\qquad
A_{esc}^{BTQ},\qquad
g_q^{red}\ \text{through the CMSSI optimization}.
```

Proof.

The first two formulas are Definition 88.3 applied to the explicit edge set
\(\overline E_{esc}^{92}\).  The class maximum formula is Theorem 89.6.  The
weighted row-sum formula is Definition 91.3 without replacing the table by
class envelopes.  Since all entries are finite, these are finite maxima and
finite sums. `square`

### Corollary 92.7: What The Table Settles Now

The finite side is now table-complete in the following sense.

1. There are exactly four row classes:

   ```math
   SD,\quad act,\quad fus,\quad cmp.
   ```

2. Every retained reduced escape row is an entry of Table 92.4.
3. Every zero-growth row is visible in the subtable \(\overline E_0^{92}\).
4. \(C_{geom}^{red}\), \(A_{esc}^{BTQ}\), and the weighted CMSSI row sum are
   finite table functions.
5. No row may charge Paper-16 RP/Cov, exact-entry RPF, global decoration,
   representation-tail, or bounded-collar `BTQ` costs a second time.

What remains unresolved is not the shape of the table but its numerical
enumeration and the analytic source.  To finish the pass/fail decision one
must now:

```math
\text{enumerate }\overline V_{92}\text{ and the four }\Xi_c,
\quad
\text{run the SCC test on }\overline E_0^{92},
\quad
\text{run the CMSSI optimization},
\quad
\text{prove or falsify }m_{red}^{act}>G_{red}^{act}.
```

Until those finite and analytic checks are completed, the common
\(E_{14}/X_{13}\) pair remains parked exactly as in Corollary 87.7.

## 93. Analytic Decay For The Reduced Escaping Tower

Section 92 makes the finite table explicit.  This section performs the next
four analytic steps:

1. define the reduced forced-tail norm;
2. state the same-record analytic decay gate;
3. combine that gate with reduced size growth;
4. compare the resulting exponent with the finite table growth side.

The theorem is conditional in the right place.  It does not use a Wilson-loop
area law, a mass gap, an unconstructed continuum Yang-Mills measure, or an
unrecorded microscopic process.  It says exactly what analytic estimate must
be proved on the active pushed-forward `SEL2` law to spend the common
\(E_{14}/X_{13}\) carry.

### Definition 93.1: Reduced Paths And Forced Records

Let \(\mathcal P_{\overline K}^{red,act}\) be the set of directed paths

```math
f=(e_1,\ldots,e_{\overline K})
```

of length \(\overline K\) in the reduced table
\(\overline E_{esc}^{92}\), after all `BTQ/ACTFULLLAW` contractions and after
the zero-growth repairs selected in Definition 90.5.  For such a path set

```math
a(f):=\prod_{i=1}^{\overline K}a(e_i),
\qquad
X_f^{red}:=\bigcup_{i=1}^{\overline K}X_{e_i}^{new},
```

where \(X_{e_i}^{new}\) is the new reduced support added by \(e_i\).  Let
\(F_f^{red}\) denote the reduced forced scalar record generated by following
the path \(f\), with bounded-collar `BTQ` records already evaluated through
the active full local law.

Fix an admissible same-record tail seminorm

```math
\mathcal N_j^{red}(\,\cdot\,)
```

on the active reduced scalar records at row \(j\).  It must satisfy:

1. same-record evaluation:

   ```math
   \mathcal N_j^{red}(F)
   ```

   is computed under the same pushed-forward law \(\mu_j^{SEL2}\);

2. domination of the expectation/readout:

   ```math
   |\mathbb E_{\mu_j^{SEL2}}F|
   \le
   \mathcal N_j^{red}(F);
   ```

3. absolute homogeneity and finite subadditivity;
4. no hidden continuum or off-record input.

The reduced shell tail at exact depth \(\overline K\) is

```math
T_{\overline K}^{red,act}(j)
:=
\sum_{f\in\mathcal P_{\overline K}^{red,act}}
|a(f)|\,\mathcal N_j^{red}(F_f^{red})\,
\|Q_{61,\overline K}^{red}\|.
```

The tail from depth \(K\) onward is

```math
T_{\ge K}^{red,act}(j)
:=
\sum_{\overline K\ge K}T_{\overline K}^{red,act}(j).
```

This is the reduced common \(E_{14}/X_{13}\) forced tail.  It excludes costs
already assigned to \(U_{11}^{RPCov}\), \(U_{13}^{RPF}\), global decoration,
representation tails, and bounded-collar `BTQ` rewrites.

### Definition 93.2: Same-Record Reduced Decay Gate

The analytic source gate

```math
\mathrm{P21\text{-}RED\text{-}DECAY}
(\mu_{red}^{act},\alpha_{red},C_{red})
```

holds when there are constants
\(\mu_{red}^{act}>0\), \(\alpha_{red}\ge0\), and \(C_{red}<\infty\) such that
cofinally in \(j\), for every reduced path \(f\in
\mathcal P_{\overline K}^{red,act}\),

```math
\mathcal N_j^{red}(F_f^{red})
\le
C_{red}(1+\overline K)^{\alpha_{red}}
\exp(-\mu_{red}^{act}|X_f^{red}|).
```

Equivalently, this is the active same-record reduced KP/projection-tail
source.  It may be proved by a reduced KP expansion, a direct reduced
projection-tail theorem, or an AF collar estimate only after genuine reduced
escape has been verified.  It is not proved by merely naming a continuum
Yang-Mills limit, an area law, or a mass gap.

The primitive direct projection-tail alternative

```math
\mathrm{P21\text{-}RED\text{-}DPT}_{prim}(m_{red}^{act})
```

holds if, without factoring through support size, one proves cofinally for
every \(f\in\mathcal P_{\overline K}^{red,act}\)

```math
\mathcal N_j^{red}(F_f^{red})
\le
C(1+\overline K)^\alpha e^{-m_{red}^{act}\overline K}.
```

This alternative may replace the reduced KP route in the final margin test,
but the finite table growth still has to be paid.

The shell-level direct projection-tail alternative

```math
\mathrm{P21\text{-}RED\text{-}DPT}_{shell}(\delta)
```

holds if one proves the already coefficient-, branching-, and inverse-amplified
tail estimate

```math
T_{\ge K}^{red,act}(j)
\le
C e^{-\delta K}.
```

This stronger alternative already includes the finite table growth.  No
additional \(A_{esc}^{BTQ}\), \(C_{geom}^{red}\), or \(g_q^{red}\) term may
be charged again.

### Definition 93.3: Reduced Size-Growth Input

The finite size-growth input is

```math
\mathrm{P21\text{-}RED\text{-}SIZE}(c_{size}^{act})
:
\quad
|X_f^{red}|
\ge
c_{size}^{act}\overline K(f)
```

for every retained reduced path after the Section-90 repairs.  If the
zero-growth subgraph is acyclic, Section 90 gives

```math
c_{size}^{act}
=
{1\over L_0+1}.
```

If an unrepaired action/SD zero-growth SCC remains, then
\(c_{size}^{act}=0\) for the pass branch and the reduced KP route cannot give
a positive depth exponent.

### Theorem 93.4: Reduced KP Plus Size Growth Gives Analytic Decay

Assume:

1. the finite table \(\overline E_{esc}^{92}\) is the active reduced escape
   table;
2. `P21-RED-SIZE(c_size^act)` holds with \(c_{size}^{act}>0\);
3. `P21-RED-DECAY(mu_red^act,alpha_red,C_red)` holds;
4. the finite table constants and inverse exponent are
   \(A_{esc}^{BTQ}\), \(C_{geom}^{red}\), and \(g_q^{red}\).

Set

```math
m_{red}^{act}
:=
\mu_{red}^{act}c_{size}^{act},
\qquad
G_{red}^{act}
:=
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red}.
```

Then for cofinally large \(j\),

```math
T_{\overline K}^{red,act}(j)
\le
C'(1+\overline K)^{\alpha_{red}}
\exp\left[-(m_{red}^{act}-G_{red}^{act}-o(1))\overline K\right].
```

Consequently, if

```math
m_{red}^{act}>G_{red}^{act},
```

then the reduced forced tail is summable:

```math
T_{\ge K}^{red,act}(j)
\le
C''e^{-\delta K}
```

for some \(\delta>0\), cofinally in \(j\).

Proof.

For a path \(f\) of length \(\overline K\), the finite table gives

```math
|a(f)|\le (A_{esc}^{BTQ})^{\overline K}.
```

The number of such paths is bounded by

```math
\#\mathcal P_{\overline K}^{red,act}
\le
C_0(C_{geom}^{red})^{\overline K}.
```

The reduced shell inverse contributes at most

```math
\|Q_{61,\overline K}^{red}\|
\le
C_Q\exp((g_q^{red}+o(1))\overline K).
```

The analytic decay gate and size-growth input give

```math
\mathcal N_j^{red}(F_f^{red})
\le
C_{red}(1+\overline K)^{\alpha_{red}}
e^{-\mu_{red}^{act}|X_f^{red}|}
\le
C_{red}(1+\overline K)^{\alpha_{red}}
e^{-m_{red}^{act}\overline K}.
```

Multiplying the four estimates and summing over paths gives the displayed
shell bound.  If \(m_{red}^{act}>G_{red}^{act}\), choose
\(\delta<m_{red}^{act}-G_{red}^{act}\); the polynomial factor is absorbed by
slightly reducing \(\delta\), and the geometric tail converges. `square`

### Corollary 93.5: Direct Projection-Tail Route

If `P21-RED-DPT_prim(m_red^act)` is proved directly, then the same pass
condition is

```math
m_{red}^{act}
>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red},
```

because this primitive direct theorem supplies the analytic decay of one
reduced record before coefficient, branching, and inverse amplification.

If instead `P21-RED-DPT_shell(delta)` is proved with \(\delta>0\), then the
reduced forced tail is already summable and the common \(E_{14}/X_{13}\)
forced-tail part passes directly.  This prevents double counting: either
\(m_{red}^{act}\) is a primitive same-record decay rate for individual reduced
records and the table growth must be paid, or \(\delta\) is an already
inverse-amplified shell-tail rate and the finite growth has already been paid
inside its definition.

### Theorem 93.6: Four-Step Analytic Verdict

The four requested analytic steps now have exact status.

1. **Reduced forced-tail norm.**  Defined by
   \(T_{\overline K}^{red,act}(j)\) and \(T_{\ge K}^{red,act}(j)\) in
   Definition 93.1.
2. **Analytic decay gate.**  Defined as `P21-RED-DECAY` in Definition 93.2,
   with the primitive and shell direct alternatives
   `P21-RED-DPT_prim` and `P21-RED-DPT_shell`.
3. **Size-growth conversion.**  Theorem 93.4 proves

   ```math
   m_{red}^{act}=\mu_{red}^{act}c_{size}^{act}
   ```

   on the reduced KP route.
4. **Comparison.**  The common \(E_{14}/X_{13}\) carry may be spent only if

   ```math
   \mu_{red}^{act}c_{size}^{act}
   >
   \log A_{esc}^{BTQ}
   +\log C_{geom}^{red}
   +g_q^{red}.
   ```

   On the primitive direct projection-tail route, replace
   \(\mu_{red}^{act}c_{size}^{act}\) by the certified direct exponent
   \(m_{red}^{act}\).  On the shell direct route, a positive
   \(\delta\) already proves summability and no finite table growth is
   charged again.

At the current source level, Paper 21 has now written the analytic gate but
has not proved `P21-RED-DECAY`, `P21-RED-DPT_prim`, or
`P21-RED-DPT_shell` for the actual active `SEL2` law.  Therefore the result is
a rigorous reduction, not an unconditional continuum-Yang-Mills confinement
or mass-gap proof.

Proof.

Items 1--2 are Definitions 93.1--93.2.  Item 3 is Theorem 93.4.  Item 4 is
Theorem 93.4 and Corollary 93.5.  The final status follows from the source
audits in Papers 10--14 and Paper 20: none supplies this same-record reduced
decay theorem for the active common \(E_{14}/X_{13}\) tower. `square`

## 94. Source Audit For `P21-RED-DECAY`

Section 93 names the analytic decay gate.  This section audits what it would
take to prove it from first principles.  The goal is to avoid a common
mistake: declaring a KP norm and then silently assuming the norm contracts.
The contraction must be a same-record theorem on the active `SEL2`
pushed-forward law.

The outcome is precise.  The only rows that can plausibly source analytic
decay are support-growing `SD` and `act` rows.  Fusion and comparison rows may
be necessary finite bookkeeping, but they do not by themselves create
large-field or polymer-size suppression.  Therefore `P21-RED-DECAY` reduces
to a one-step reduced KP inequality plus a coverage test showing that every
large reduced support is actually reached through decay-eligible rows.

### Definition 94.1: Canonical Reduced Tail Seminorm

For a reduced forced record \(F_f^{red}\) first generated at reduced depth
\(\overline K(f)\), let
\(\mathcal A_{<f}^{red}\) be the unital algebra generated by all retained
reduced records of smaller depth, together with the bounded-collar
`ACTFULLLAW` records and lower-shell retractions already declared on the same
active row.

Define three same-record tail components.

1. **Projection tail**

   ```math
   \operatorname{Tail}_{proj,j}^{red}(F_f)
   :=
   \inf_{G\in\mathcal A_{<f}^{red},\,\|G\|_\infty\le\|F_f\|_\infty}
   \left|
   \mathbb E_{\mu_j^{SEL2}}(F_f-G)
   \right|.
   ```

2. **Connected tail**

   ```math
   \operatorname{Tail}_{conn,j}^{red}(F_f)
   :=
   \sup
   \left|
   \kappa_j(F_f;G_1,\ldots,G_r)
   \right|,
   ```

   where \(1\le r\le r_*^{red}\) and \(G_i\in\mathcal A_{<f}^{red}\) with
   \(\|G_i\|_\infty\le1\).  The cumulant \(\kappa_j\) is computed under
   \(\mu_j^{SEL2}\), not under an auxiliary continuum measure.

3. **Residual transport tail**

   ```math
   \operatorname{Tail}_{tr,j}^{red}(F_f)
   :=
   \operatorname{Lip}_{red}(F_f)\,
   \operatorname{Def}_{tr,j}^{red}(\overline K(f)),
   ```

   where \(\operatorname{Def}_{tr,j}^{red}\) is only the residual transport
   defect not already assigned to \(U_{11}^{RPCov}\), \(U_{13}^{RPF}\), or
   the whole-process `WP` ledger.

The canonical reduced tail seminorm is

```math
\mathcal N_{j,can}^{red}(F_f)
:=
\max\left\{
\operatorname{Tail}_{proj,j}^{red}(F_f),
\operatorname{Tail}_{conn,j}^{red}(F_f),
\operatorname{Tail}_{tr,j}^{red}(F_f)
\right\}.
```

This is the reduced analogue of Paper 14 Definitions 25.2--25.5, with the
law class collapsed to the single active same-record row \(\mu_j^{SEL2}\).

### Lemma 94.2: The Canonical Seminorm Is Admissible

\(\mathcal N_{j,can}^{red}\) is an admissible seminorm for Definition 93.1.
It dominates every unresolved projection, connected-cumulant, and residual
transport contribution of the reduced forced record \(F_f^{red}\).  It does
not dominate costs that were deliberately assigned elsewhere:

```math
U_{11}^{RPCov},\quad
U_{13}^{RPF},\quad
D_{dec}^{SEL2},\quad
\text{representation tails},\quad
\text{internal BTQ rewrites}.
```

Proof.

The three components are expectations, cumulants, or residual transport
defects computed under the same pushed-forward law.  The maximum is
homogeneous and finitely subadditive after the usual finite-dimensional
seminorm closure; if desired, replace it by its finite Minkowski functional
closure without changing the generated tail bounds.  Paper 14 Lemma 25.6
shows that these three components dominate the corresponding forced-record
tails in the BLU ledger.  The exclusions are exactly the ledger exclusions in
Definitions 92.3 and 93.1, so no previously assigned debit is charged again.
`square`

### Definition 94.3: Decay-Eligible And Neutral Rows

In the finite table of Section 92, define the decay-eligible edge set

```math
\mathcal E_{dec}^{92}
:=
\{e\in\mathcal E_{SD}^{92}\cup\mathcal E_{act}^{92}:\Delta_X(e)\ge1\}.
```

The neutral edge set is

```math
\mathcal E_{neu}^{92}
:=
\overline E_{esc}^{92}\setminus\mathcal E_{dec}^{92}.
```

Thus `fus` and `cmp` rows are neutral unless a separate same-record theorem
proves that the specific row carries analytic suppression.  A neutral row may
still be essential: it can change channels, comparison slots, or shell
coordinates, and it can contribute to \(A_{esc}^{BTQ}\), \(C_{geom}^{red}\),
or \(g_q^{red}\).  It just does not get to contribute to
\(\mu_{red}^{act}\) without a new source theorem.

### Definition 94.4: Decay Coverage

A valid reduced table has decay coverage

```math
\mathrm{P21\text{-}RED\text{-}COVER}(\chi_{dec},b_{dec})
```

if every retained path \(f=(e_1,\ldots,e_{\overline K})\) satisfies

```math
\sum_{i:e_i\in\mathcal E_{dec}^{92}}\Delta_X(e_i)
\ge
\chi_{dec}|X_f^{red}|-b_{dec},
```

with \(\chi_{dec}>0\) and \(b_{dec}<\infty\).

This is separate from size growth.  Size growth says reduced depth creates
support.  Decay coverage says that the created support was created through
rows that actually earn analytic decay.  If support can grow mainly through
neutral `fus/cmp` bookkeeping, then reduced KP does not follow from the
`SD/act` source.

### Definition 94.5: One-Step Reduced KP Source

The one-step reduced KP source

```math
\mathrm{P21\text{-}RED\text{-}1KP}
(\mu_0,\lambda_{sem},\alpha_0,C_0)
```

holds if, cofinally in \(j\), every reduced path \(f\) admits a pathwise
estimate

```math
\mathcal N_{j,can}^{red}(F_f^{red})
\le
C_0(1+\overline K(f))^{\alpha_0}
\exp\left(
-\mu_0
\sum_{e_i\in\mathcal E_{dec}^{92}}\Delta_X(e_i)
+\lambda_{sem}\overline K(f)
\right).
```

Here:

1. \(\mu_0>0\) is the analytic suppression per decay-eligible support cell;
2. \(\lambda_{sem}\ge0\) is the unavoidable same-record seminorm
   amplification per reduced row;
3. the estimate is invalid if it uses an area law, mass gap, continuum
   Yang-Mills measure, or an off-record stochastic kernel.

The ideal KP case has \(\lambda_{sem}=0\).  If
\(\lambda_{sem}>0\), that amplification is a real surcharge and must be paid
in the exponent.

### Theorem 94.6: One-Step KP Plus Coverage Implies The Section-93 Decay Gate

Assume:

1. `P21-RED-1KP(mu_0,lambda_sem,alpha_0,C_0)`;
2. `P21-RED-COVER(chi_dec,b_dec)`;
3. `P21-RED-SIZE(c_size^act)` with \(c_{size}^{act}>0\).

Then the primitive depth-decay exponent certified by the one-step KP source is

```math
m_{1KP}^{red}
:=
\mu_0\chi_{dec}c_{size}^{act}
-\lambda_{sem}.
```

If

```math
m_{1KP}^{red}>0,
```

then `P21-RED-DPT_prim(m_1KP^red)` holds.  Equivalently, the Section-93
support-decay gate holds with any support exponent

```math
0<\mu_{red}^{act}
<
\mu_0\chi_{dec}
-{\lambda_{sem}\over c_{size}^{act}}.
```

Proof.

By coverage,

```math
\sum_{e_i\in\mathcal E_{dec}^{92}}\Delta_X(e_i)
\ge
\chi_{dec}|X_f^{red}|-b_{dec}.
```

By size growth,

```math
|X_f^{red}|\ge c_{size}^{act}\overline K(f).
```

Insert both bounds into Definition 94.5.  The finite constant
\(e^{\mu_0b_{dec}}\) is absorbed into \(C_0\), and the exponent becomes at
most

```math
-(\mu_0\chi_{dec}c_{size}^{act}-\lambda_{sem})\overline K(f).
```

This is the primitive direct projection-tail estimate of Definition 93.2 with
exponent \(m_{1KP}^{red}\).  Dividing by the size-growth inequality gives the
equivalent support exponent whenever the displayed difference is positive.
`square`

### Corollary 94.7: Edge-Class Decay Verdict

For the current finite table, the analytic source audit is:

| row class | decay status | consequence |
| --- | --- | --- |
| `SD` with \(\Delta_X\ge1\) | decay-eligible | must satisfy the one-step KP estimate or be removed/carried |
| `act` with \(\Delta_X\ge1\) | decay-eligible | must satisfy the one-step KP estimate or be removed/carried |
| `fus` | neutral by default | paid through \(A_{esc}^{BTQ}\), CMSSI, or representation-tail budget |
| `cmp` | neutral by default | paid through comparison battery, \(A_{esc}^{BTQ}\), or carried residual |
| any row with \(\Delta_X=0\) | no depth decay | must pass the Section-90 zero-growth repair or enter \(g_q^{red}\)/a carry |

Thus the next nonformal proof obligation is exactly:

```math
\mathrm{P21\text{-}RED\text{-}1KP}
+
\mathrm{P21\text{-}RED\text{-}COVER}
+
\mathrm{P21\text{-}RED\text{-}SIZE}.
```

If their certified exponent

```math
m_{1KP}^{red}
=
\mu_0\chi_{dec}c_{size}^{act}-\lambda_{sem}
```

does not beat

```math
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red},
```

then the common \(E_{14}/X_{13}\) bypass still cannot be spent.

### Theorem 94.8: Current Status Of `P21-RED-DECAY`

At the current source level, Paper 21 has not proved

```math
\mathrm{P21\text{-}RED\text{-}1KP},
\qquad
\mathrm{P21\text{-}RED\text{-}COVER},
\qquad
\mathrm{P21\text{-}RED\text{-}SIZE}
```

for the actual enumerated table, because the table has not yet been
numerically enumerated and the same-record one-step KP estimate has not been
proved for the active `SEL2` law.  But the analytic obstruction is now
localized:

```math
\boxed{
\mu_0\chi_{dec}c_{size}^{act}
-\lambda_{sem}
>
\log A_{esc}^{BTQ}
+\log C_{geom}^{red}
+g_q^{red}.
}
```

This is the first-principles version of `P21-RED-DECAY`.  It is upstream of
confinement and cannot be discharged by assuming continuum Yang-Mills, a mass
gap, or an area law.

Proof.

Definitions 94.1--94.5 choose the canonical reduced norm, identify the
decay-eligible rows, and state the one-step same-record source.  Theorem 94.6
derives the usable primitive exponent.  Corollary 93.5 then supplies the
finite-table comparison.  The missing inputs are exactly the finite table SCC
and coverage data plus the one-step KP estimate on the active same-record
law. `square`

## 95. Four-Part Reduced Margin Audit

Sections 90--94 isolate the four inputs needed before the common
\(E_{14}/X_{13}\) bypass can be spent.  This section composes them into one
finite worksheet.  The worksheet is deliberately operational: every object is
a scalar record or a finite table entry on the active pushed-forward `SEL2`
law.  It does not appeal to an unconstructed continuum Yang-Mills measure, a
Wilson-loop area law, or a mass gap.

The four tasks are:

1. run the repaired zero-growth SCC test and extract \(c_{size}^{act}\);
2. run the decay-coverage test and extract \(\chi_{dec}\);
3. evaluate the finite growth side \(G_{fin}\);
4. compare the one-step KP exponent with \(G_{fin}\).

### Definition 95.1: Repaired Reduced Pass Graph

Start with the finite reduced table \(\overline E_{esc}^{92}\) of Section 92.
Choose a zero-growth repair assignment in the sense of Definition 90.5.  Let

```math
\overline E_{pass}^{95}
\subseteq
\overline E_{esc}^{92}
```

be the retained reduced pass edges after deleting:

1. edges moved into the bounded-collar `BTQ/ACTFULLLAW` state;
2. same-shell inverse edges assigned entirely to the CMSSI ledger;
3. comparison-battery edges assigned entirely to the common finite battery;
4. exact-zero rows killed by a same-record identity;
5. carried residual rows assigned to \(U_{ZG}^{red}\).

The repaired pass graph is

```math
\overline{\mathfrak A}_{pass}^{95}
:=
(\overline V_{92},\overline E_{pass}^{95}).
```

Its repaired zero-growth subgraph is

```math
\overline{\mathfrak A}_{0,rep}^{95}
:=
(\overline V_{92},
\overline E_{0,rep}^{95}),
\qquad
\overline E_{0,rep}^{95}
:=
\{e\in\overline E_{pass}^{95}:\Delta_X(e)=0\}.
```

Let \(L_{0,rep}^{95}\) be the maximum directed path length in
\(\overline{\mathfrak A}_{0,rep}^{95}\), with
\(L_{0,rep}^{95}=\infty\) if this graph has a directed cycle.  Define

```math
c_{size}^{95}
:=
\begin{cases}
(L_{0,rep}^{95}+1)^{-1},
& L_{0,rep}^{95}<\infty,\\[3pt]
0,
& L_{0,rep}^{95}=\infty.
\end{cases}
```

This is the exact finite version of \(c_{size}^{act}\) for the repaired pass
branch.

### Theorem 95.2: Step 1 SCC Verdict

The repaired pass branch satisfies

```math
\mathrm{P21\text{-}RED\text{-}SIZE}(c_{size}^{95})
```

if and only if \(L_{0,rep}^{95}<\infty\).  If
\(L_{0,rep}^{95}=\infty\), then no positive reduced size-growth constant is
available on the pass branch.

Proof.

This is Theorem 90.6 applied after the repair assignment of Definition 95.1.
If the repaired zero-growth graph is acyclic, every \(L_{0,rep}^{95}+1\)
retained edges contain at least one support-growing edge, giving
\((L_{0,rep}^{95}+1)^{-1}\).  If it has a directed cycle, iterating that cycle
increases reduced depth without increasing support, so no positive
\(c_{size}\) can hold. `square`

### Definition 95.3: Finite Decay-Coverage Ratio

For \(e\in\overline E_{pass}^{95}\), set

```math
u(e):=\Delta_X(e),
\qquad
d(e):=\Delta_X(e)\mathbf 1_{\{e\in\mathcal E_{dec}^{92}\}}.
```

Thus \(u\) measures created reduced support, while \(d\) measures the part of
that support created by decay-eligible `SD/act` rows.  For a directed path or
cycle \(\Gamma\), write

```math
u(\Gamma):=\sum_{e\in\Gamma}u(e),
\qquad
d(\Gamma):=\sum_{e\in\Gamma}d(e).
```

The finite cycle coverage ratio is

```math
\chi_{cyc}^{95}
:=
\min_{\substack{\Gamma\ {\rm simple\ directed\ cycle}\\u(\Gamma)>0}}
{d(\Gamma)\over u(\Gamma)}.
```

If there is no positive-support directed cycle, set
\(\chi_{cyc}^{95}=+\infty\); if there is a positive-support cycle with
\(d(\Gamma)=0\), then \(\chi_{cyc}^{95}=0\).

For a chosen \(0<\chi<\chi_{cyc}^{95}\), define the finite transient defect

```math
B_{cov}^{95}(\chi)
:=
\max_{\pi\ {\rm simple\ directed\ path}}
\bigl(\chi u(\pi)-d(\pi)\bigr)_+.
```

The maximum is finite because the graph is finite and \(\pi\) ranges over
simple paths.  Let \(X_*^{95}\) be the maximum seed/frontier support size
among vertices in \(\overline V_{92}\).  Set

```math
b_{dec}^{95}(\chi)
:=
B_{cov}^{95}(\chi)+\chi X_*^{95}.
```

### Lemma 95.4: Step 2 Is A Minimum Cycle-Ratio Test

If \(0<\chi<\chi_{cyc}^{95}\), then the repaired pass graph satisfies

```math
\mathrm{P21\text{-}RED\text{-}COVER}
(\chi,b_{dec}^{95}(\chi)).
```

If \(\chi_{cyc}^{95}=0\), no positive uniform decay-coverage constant is
available on the repaired pass graph.

Proof.

Decompose any finite directed path into simple directed cycles plus a simple
residual path by the usual cycle-erasure algorithm.  For every simple cycle
with \(u(\Gamma)>0\),
\(d(\Gamma)\ge\chi u(\Gamma)\), because \(\chi<\chi_{cyc}^{95}\).  Cycles
with \(u(\Gamma)=0\) also satisfy the inequality since \(d(\Gamma)\ge0\).
The only possible loss comes from the residual simple path, and it is bounded
by \(B_{cov}^{95}(\chi)\).  Hence

```math
d(f)\ge \chi u(f)-B_{cov}^{95}(\chi).
```

The reduced support of the generated record is bounded by the seed support
plus the accumulated support increments:

```math
|X_f^{red}|\le X_*^{95}+u(f).
```

Combining the two estimates gives

```math
d(f)\ge \chi |X_f^{red}|-b_{dec}^{95}(\chi),
```

which is the coverage gate.  If \(\chi_{cyc}^{95}=0\), there are simple cycles
with arbitrarily small \(d/u\), or a positive-support cycle with \(d=0\).
Iterating such cycles prevents any positive uniform coverage constant. `square`

### Definition 95.5: Step 3 Finite Growth Side

For the repaired pass graph define the exact finite constants

```math
C_{geom}^{95}
:=
\max_{\bar v\in\overline V_{92}}
\#\{e\in\overline E_{pass}^{95}:s(e)=\bar v\},
```

and

```math
A_{esc}^{95}
:=
\max_{e\in\overline E_{pass}^{95}}\max(1,a(e)).
```

If the exact table is not yet numerically enumerated, use the safe envelopes
from Sections 89 and 92:

```math
C_{geom}^{95}\le C_{geom}^{env},
\qquad
A_{esc}^{95}\le A_{esc}^{env}.
```

The inverse-growth input is

```math
g_q^{95}
:=
\begin{cases}
0, & \text{if a zero-spread `P21-RED-CMSSI` weight is certified},\\
g_{q,cert}^{red}, & \text{if only a positive-spread CMSSI weight is certified},\\
g_q^{car}, & \text{if no CMSSI/right-inverse certificate is supplied}.
\end{cases}
```

Finally define the finite-battery closure surcharge

```math
g_{bat}^{95}
:=
\begin{cases}
0,
& \text{on the `BTQ/ACTFULLLAW` or fixed finite-degree branch},\\
g_{bat}^{BTQ},
& \text{on the `BTQ-DEGTAIL` branch},\\
0,
& \text{under `BTQ-HKSM` with subexponential degree schedule}.
\end{cases}
```

The growth side to be beaten is

```math
G_{fin}^{95}
:=
\log A_{esc}^{95}
+\log C_{geom}^{95}
+g_q^{95}
+g_{bat}^{95}.
```

The term \(g_{bat}^{95}\) is included to keep the Section-80 correction
visible.  On the strict active full-law branch it vanishes; on a genuine
degree-tail branch it cannot be silently dropped.

### Definition 95.6: Step 4 One-Step KP Margin

Assume the same-record one-step KP source

```math
\mathrm{P21\text{-}RED\text{-}1KP}
(\mu_0,\lambda_{sem},\alpha_0,C_0)
```

has been proved for the active `SEL2` law.  For any
\(0<\chi<\chi_{cyc}^{95}\), define

```math
\Delta_{1KP}^{95}(\chi)
:=
\mu_0\chi c_{size}^{95}
-\lambda_{sem}
-G_{fin}^{95}.
```

When \(0<\chi_{cyc}^{95}<\infty\), the best finite-coverage margin is

```math
\Delta_{1KP,best}^{95}
:=
\sup_{0<\chi<\chi_{cyc}^{95}}
\Delta_{1KP}^{95}(\chi).
```

Equivalently,

```math
\Delta_{1KP,best}^{95}
=
\mu_0\chi_{cyc}^{95}c_{size}^{95}
-\lambda_{sem}
-G_{fin}^{95},
```

with the understanding that the supremum is approached by
\(\chi\uparrow\chi_{cyc}^{95}\), while the finite transient
\(b_{dec}^{95}(\chi)\) may grow as \(\chi\) approaches the boundary.  This
transient affects constants, not the exponential rate.

If \(\chi_{cyc}^{95}=+\infty\), do not define
\(\Delta_{1KP,best}^{95}\) by the supremum above.  The infinite cycle ratio
says that the repaired pass graph has no positive-support cycle.  Together
with \(L_{0,rep}^{95}<\infty\), this forces the entire repaired pass graph to
be acyclic, hence the reduced tower has a finite maximum depth
\(K_{max}^{95}\).  In that finite-depth case,

```math
T_{\ge K}^{red,act}(j)=0
\qquad
(K>K_{max}^{95}),
```

so the common finite forced-tail branch is summable without an asymptotic
one-step KP margin.

### Theorem 95.7: Four-Part Reduced Margin Verdict

The repaired reduced common \(E_{14}/X_{13}\) forced-tail branch passes if the
following finite/same-record conditions hold:

1. \(L_{0,rep}^{95}<\infty\), so \(c_{size}^{95}>0\);
2. \(\chi_{cyc}^{95}>0\), so positive decay coverage is available;
3. \(G_{fin}^{95}<\infty\), with \(g_q^{95}\) and \(g_{bat}^{95}\) certified
   on the chosen branch;
4. either the repaired pass graph has finite maximum depth, or the
   same-record one-step KP margin is positive:

   ```math
   \Delta_{1KP,best}^{95}>0.
   ```

In the finite-depth case, \(T_{\ge K}^{red,act}(j)=0\) for
\(K>K_{max}^{95}\).  In the positive-margin case, there exists \(\delta>0\)
such that, cofinally in \(j\),

```math
T_{\ge K}^{red,act}(j)\le C e^{-\delta K}.
```

Consequently the common reduced forced-tail part of the
\(E_{14}/X_{13}\) bypass is summable on the active pass branch.

The branch fails, rather than merely parks, if either:

```math
c_{size}^{95}=0,
\qquad\text{or}\qquad
\chi_{cyc}^{95}=0,
```

or if rigorous upper bounds on \(\mu_0\), \(c_{size}^{95}\), and
\(\chi_{cyc}^{95}\) together with lower bounds on
\(\lambda_{sem}+G_{fin}^{95}\) force
\(\Delta_{1KP,best}^{95}\le0\).

If the finite table, CMSSI/right-inverse certificate, BTQ closure branch, or
one-step KP source is not supplied, the branch is parked at the named missing
input and no bypass spending is allowed.

Proof.

Item 1 is Theorem 95.2.  Item 2 is Lemma 95.4.  Item 3 is Definition 95.5 and
the corrected BTQ accounting of Section 80.  If the repaired pass graph is
acyclic, there are no paths beyond its finite maximum length, so the tail is
eventually zero.  Otherwise item 4 gives

```math
\mu_0\chi c_{size}^{95}-\lambda_{sem}
>
\log A_{esc}^{95}+\log C_{geom}^{95}+g_q^{95}+g_{bat}^{95}
```

for some admissible \(\chi\).  Theorem 94.6 turns the left-hand side before
finite growth into a primitive same-record decay exponent.  Theorem 93.4 and
Corollary 93.5 then sum the reduced forced tail after paying coefficient
growth, path branching, shell inverse growth, and, when present, the BTQ
degree-battery surcharge.  The fail and park alternatives are the
contrapositives of the finite SCC/coverage tests and the source-status rules
from Sections 90--94. `square`

### Corollary 95.8: Current Source-Level Status

The requested four tasks are now executed as finite formulas:

```math
c_{size}^{95}
=
\begin{cases}
(L_{0,rep}^{95}+1)^{-1},&\overline{\mathfrak A}_{0,rep}^{95}
\text{ acyclic},\\
0,&\text{otherwise},
\end{cases}
```

```math
\chi_{dec}^{95}
\text{ is any }0<\chi<\chi_{cyc}^{95},
\qquad
\chi_{cyc}^{95}
=
\min_{\Gamma}
{d(\Gamma)\over u(\Gamma)},
```

```math
G_{fin}^{95}
=
\log A_{esc}^{95}
+\log C_{geom}^{95}
+g_q^{95}
+g_{bat}^{95},
```

and, on the all-depth branch with \(0<\chi_{cyc}^{95}<\infty\),

```math
\Delta_{1KP,best}^{95}
=
\mu_0\chi_{cyc}^{95}c_{size}^{95}
-\lambda_{sem}
-G_{fin}^{95}.
```

If \(\chi_{cyc}^{95}=+\infty\) and the repaired zero-growth graph is acyclic,
replace this last rate formula by the finite-depth conclusion
\(T_{\ge K}^{red,act}(j)=0\) for \(K>K_{max}^{95}\).

What is still not supplied by Papers 10--14, Paper 20, or the current finite
table is the numerical edge enumeration and the same-record proof of
`P21-RED-1KP` for the actual active `SEL2` law.  Thus Paper 21 has reduced
the problem to a sharp finite/analytic inequality, but it has not yet proved
the bypass or the downstream confinement conclusion.

The next real computation is therefore not another symbolic rearrangement. It
is one of the following source-producing moves:

1. enumerate \(\overline E_{pass}^{95}\) and compute
   \(L_{0,rep}^{95}\), \(\chi_{cyc}^{95}\), \(A_{esc}^{95}\), and
   \(C_{geom}^{95}\);
2. prove a zero-spread or quantified positive-spread CMSSI certificate for
   \(g_q^{95}\);
3. prove the same-record one-step KP estimate and its constants
   \((\mu_0,\lambda_{sem})\);
4. if the branch uses degree-tail rather than full-law BTQ, prove the selected
   \(g_{bat}^{95}\) bound on the same finite battery.

## 96. Executable Reduced Edge Certificate

Section 95 says what must be computed.  This section fixes the certificate
format that makes the computation honest.  The point is not to add another
symbolic layer, but to prevent a row from entering the reduced pass graph
unless its operational source, coefficient, support increment, inverse slot,
and repair status are all named on the same active scalar record law.

This is the Barandes-aligned finite-record move: the certificate is a finite
table of observable records and exact row transformations.  It is not a
continuum gauge field, not a Wilson-loop area-law assumption, and not a hidden
stochastic process.

### Definition 96.1: Reduced Edge Certificate Object

An executable reduced edge certificate is a finite tuple

```math
\mathsf C_{96}^{red}
:=
(\overline V_{96},\overline E_{96},
s,t,c,\xi,a,\Delta_X,\mathcal O,\mathsf r,\mathsf p,\mathsf b).
```

The entries have the following meanings.

1. \(\overline V_{96}\subseteq\overline V_{92}\) is the finite vertex set
   actually reached by the active reduced branch.
2. \(\overline E_{96}\) is the finite candidate row set.
3. \(s,t:\overline E_{96}\to\overline V_{96}\) are source and target maps.
4. \(c(e)\in\{SD,act,fus,cmp\}\) is the row class.
5. \(\xi(e)\in\Xi_{c(e)}\) is the finite row index of Definition 92.2.
6. \(a(e)\ge0\) is the absolute coefficient after all declared
   `BTQ/ACTFULLLAW` normal forms and finite comparison-battery normalizations.
7. \(\Delta_X(e)\in\mathbb N\) is the reduced support increment.
8. \(\mathcal O(e)\) is the off-diagonal shell-inverse row contribution used
   in the CMSSI audit.
9. \(\mathsf r(e)\) is the row disposition:

   ```math
   \mathsf r(e)\in
   \{\mathrm{pass},\mathrm{BTQ},\mathrm{CMSSI},
   \mathrm{cmpbat},\mathrm{zero},\mathrm{carry}\}.
   ```

10. \(\mathsf p(e)\) is a provenance label naming the same-record source
    theorem, finite identity, or finite row definition that produced the row.
11. \(\mathsf b(e)\) is the finite-battery closure label:

    ```math
    \mathsf b(e)\in
    \{\mathrm{fulllaw},\mathrm{fixeddeg},\mathrm{degtail},\mathrm{HKSM}\}.
    ```

The retained pass edge set is

```math
\overline E_{pass}^{96}
:=
\{e\in\overline E_{96}:\mathsf r(e)=\mathrm{pass}\}.
```

It is the concrete version of \(\overline E_{pass}^{95}\).

### Definition 96.2: Row Admissibility

A row \(e\in\overline E_{96}\) is admissible only if all of the following
checks pass.

1. **Row-map check.**  The target satisfies

   ```math
   t(e)=R_{c(e)}(s(e),\xi(e))
   ```

   using the row maps of Definition 92.3.

2. **Same-record check.**  The provenance \(\mathsf p(e)\) evaluates both the
   source and target records under the active pushed-forward scalar law
   \(\mu_j^{SEL2}\).  No row may invoke a continuum Yang-Mills measure, an area
   law, a mass gap, or an off-record Markov kernel.

3. **No double-charge check.**  If a cost has already been assigned to
   \(U_{11}^{RPCov}\), \(U_{13}^{RPF}\), \(D_{dec}^{SEL2}\), a representation
   tail, or an internal `BTQ` rewrite, then that cost cannot appear inside
   \(a(e)\), \(\Delta_X(e)\), or \(\mathcal O(e)\).

4. **Cutoff check.**  If a representation or product label lies outside the
   active finite cutoff, the term is not a pass edge.  It must enter the
   declared representation-tail or product-tail budget.

5. **Zero-row check.**  If \(\mathsf r(e)=\mathrm{zero}\), the certificate must
   name the exact same-record identity proving \(a(e)=0\).  A heuristic
   cancellation is not enough.

6. **Carry check.**  If \(\mathsf r(e)=\mathrm{carry}\), the row is removed
   from the pass graph and contributes to a named nonnegative residual
   \(U_{row}^{96}\).  Carried rows are not allowed to improve
   \(c_{size}^{95}\), \(\chi_{cyc}^{95}\), or \(G_{fin}^{95}\).

7. **Closure check.**  If \(\mathsf b(e)=\mathrm{degtail}\), the certificate
   must include the corresponding \(g_{bat}^{BTQ}\) source.  If no such source
   is supplied, the pass branch is parked at `BTQ-DEGTAIL`.

The certificate is admissible if every row is admissible and every row in
\(\overline E_{esc}^{92}\) is either represented in \(\overline E_{96}\) or
assigned to an explicit tail/carry ledger.

### Definition 96.3: Certificate Outputs

Given an admissible \(\mathsf C_{96}^{red}\), define:

```math
\overline{\mathfrak A}_{pass}^{96}
:=
(\overline V_{96},\overline E_{pass}^{96}).
```

The repaired zero-growth graph is

```math
\overline{\mathfrak A}_{0}^{96}
:=
(\overline V_{96},
\{e\in\overline E_{pass}^{96}:\Delta_X(e)=0\}).
```

Let \(L_0^{96}\) be the longest directed path length in
\(\overline{\mathfrak A}_{0}^{96}\), with \(L_0^{96}=\infty\) if this graph
has a directed cycle.  Set

```math
c_{size}^{96}
:=
\begin{cases}
(L_0^{96}+1)^{-1},&L_0^{96}<\infty,\\
0,&L_0^{96}=\infty.
\end{cases}
```

For \(e\in\overline E_{pass}^{96}\), set

```math
u(e):=\Delta_X(e),
\qquad
d(e):=\Delta_X(e)\mathbf 1_{\{c(e)\in\{SD,act\},\,\Delta_X(e)\ge1\}}.
```

The coverage ratio is

```math
\chi_{cyc}^{96}
:=
\min_{\substack{\Gamma\ {\rm simple\ directed\ cycle}\\u(\Gamma)>0}}
{d(\Gamma)\over u(\Gamma)},
```

with the same conventions as Definition 95.3.  The finite growth constants
are

```math
C_{geom}^{96}
:=
\max_{\bar v\in\overline V_{96}}
\#\{e\in\overline E_{pass}^{96}:s(e)=\bar v\},
```

```math
A_{esc}^{96}
:=
\max_{e\in\overline E_{pass}^{96}}\max(1,a(e)).
```

The CMSSI optimization is the finite problem

```math
g_{q,cert}^{96}
:=
\inf_{\mathbf a}
\left\{
g_w(\mathbf a):
\Omega_{tot}^{96}(\mathbf a)<\kappa_{\min}^{red}
\right\},
```

where \(\Omega_{tot}^{96}\) is Definition 91.3 evaluated on the certified
rows rather than on class envelopes.

Finally,

```math
g_{bat}^{96}
:=
\begin{cases}
0,&\mathsf b(e)\ne\mathrm{degtail}\text{ for all pass rows},\\
g_{bat}^{BTQ},&\text{some pass row uses }\mathrm{degtail}.
\end{cases}
```

and

```math
G_{fin}^{96}
:=
\log A_{esc}^{96}
+\log C_{geom}^{96}
+g_q^{96}
+g_{bat}^{96}.
```

Here \(g_q^{96}\) is \(0\), \(g_{q,cert}^{96}\), or \(g_q^{car}\) according
to the three cases of Definition 95.5.

### Algorithm 96.4: Finite Certificate Audit

The finite audit is the following deterministic computation.

1. **Validate rows.**  Check Definition 96.2 for every row.
2. **Build pass graph.**  Form \(\overline E_{pass}^{96}\) by deleting rows
   with dispositions `BTQ`, `CMSSI`, `cmpbat`, `zero`, and `carry`.
3. **Run SCC.**  Compute strongly connected components of
   \(\overline{\mathfrak A}_{0}^{96}\).  A nontrivial SCC sets
   \(c_{size}^{96}=0\) unless a new repair changes the certificate.
4. **Run coverage.**  Compute the minimum cycle ratio
   \(\chi_{cyc}^{96}\).  Equivalently, solve the finite ratio problem by
   checking the sign of cycle weights

   ```math
   d(e)-\chi u(e)
   ```

   and locating the critical \(\chi\).
5. **Compute finite growth.**  Compute \(A_{esc}^{96}\) and
   \(C_{geom}^{96}\) by finite maxima.
6. **Run CMSSI.**  Evaluate the finite weighted row sums and decide whether
   \(g_q^{96}=0\), \(g_q^{96}\le g_{q,cert}^{96}\), or \(g_q^{96}=g_q^{car}\).
7. **Check closure surcharge.**  Decide \(g_{bat}^{96}\) from the closure
   labels \(\mathsf b(e)\).
8. **Output margin.**  On the all-depth branch, output

   ```math
   \Delta_{1KP,best}^{96}
   :=
   \mu_0\chi_{cyc}^{96}c_{size}^{96}
   -\lambda_{sem}
   -G_{fin}^{96}.
   ```

   If the pass graph is acyclic, output the finite-depth conclusion instead.

### Theorem 96.5: Certificate Audit Is Equivalent To The Section-95 Inputs

An admissible certificate \(\mathsf C_{96}^{red}\) supplies all finite inputs
required by Theorem 95.7:

```math
c_{size}^{95}=c_{size}^{96},
\qquad
\chi_{cyc}^{95}=\chi_{cyc}^{96},
\qquad
A_{esc}^{95}=A_{esc}^{96},
\qquad
C_{geom}^{95}=C_{geom}^{96},
```

with \(g_q^{95}=g_q^{96}\) and \(g_{bat}^{95}=g_{bat}^{96}\) on the chosen
closure branch.  Therefore the common \(E_{14}/X_{13}\) reduced forced-tail
branch passes, parks, or fails exactly according to the output of Algorithm
96.4 together with the same-record one-step KP constants
\((\mu_0,\lambda_{sem})\).

Proof.

Definitions 96.1--96.3 instantiate the abstract pass graph, zero-growth
subgraph, coverage weights, coefficient maximum, branching maximum, inverse
ledger, and battery-growth surcharge of Section 95.  The row admissibility
checks ensure that no row changes the law, imports a continuum premise, or
double-charges a debit already assigned elsewhere.  The SCC computation is
Theorem 95.2, the minimum cycle-ratio computation is Lemma 95.4, and the
finite growth side is Definition 95.5.  Hence Algorithm 96.4 is exactly the
finite portion of Theorem 95.7. `square`

### Corollary 96.6: What Must Be Enumerated First

The certificate should be filled in the following order.

1. **`SD` rows first.**  They are the most likely decay-eligible rows and they
   control both \(d(e)\) and the Casimir/CMSSI ledger.
2. **`act` rows second.**  They are the other possible source of decay
   coverage and the main source of action-coefficient growth.
3. **`fus` rows third.**  They usually do not create decay, but they may
   enlarge \(C_{geom}\), \(A_{esc}\), and \(g_q\).
4. **`cmp` rows fourth.**  They determine whether the common
   \(E_{14}/X_{13}\) battery stays finite or reintroduces a comparison carry.
5. **Zero-growth rows last.**  After all four classes are listed, run the SCC
   repair test.  A zero-growth SCC found before the row list is complete is
   diagnostic but not final.

This ordering is not cosmetic.  It prevents the analytic estimate from being
proved against the wrong graph.  The graph comes first; the same-record KP
constant is meaningful only after the retained pass rows are fixed.

### Theorem 96.7: Current Status After The Certificate Contract

Paper 21 now has a finite certificate contract strong enough to make the next
calculation executable.  What remains open is not a new definition but the
actual finite enumeration:

```math
\mathsf C_{96}^{red}
\quad\text{with all admissibility checks passed.}
```

Until that table is supplied, the paper may use the Section-89 and Section-92
envelopes, but it may not claim numerical values for

```math
L_0^{96},\quad
\chi_{cyc}^{96},\quad
A_{esc}^{96},\quad
C_{geom}^{96},\quad
g_q^{96}.
```

Once the table is supplied, the remaining analytic theorem is sharply
targeted:

```math
\mu_0\chi_{cyc}^{96}c_{size}^{96}
-\lambda_{sem}
>
\log A_{esc}^{96}
+\log C_{geom}^{96}
+g_q^{96}
+g_{bat}^{96}.
```

This is the first point at which the same-record one-step KP proof should be
attempted.  Before the certificate exists, a claimed value of \(\mu_0\) has no
fixed pass graph to act on. `square`

## 97. Six-Step First Instantiation Of \(\mathsf C_{96}^{red}\)

Section 96 defines the certificate contract.  This section executes the next
six steps as far as the present papers allow.  The result is an instantiated
finite branch record and a row-census ledger.  It is not yet a numerical pass,
because Papers 10--14 and Paper 20 do not tabulate the actual `SD`, `act`,
`fus`, and `cmp` rows.  The gain is that the missing data are now exactly the
finite entries of \(\mathsf C_{96}^{red}\), not another hidden continuum
assumption.

### Definition 97.1: Frozen Branch Parameters

The first certificate instance is built at fixed data

```math
\mathfrak P_{97}
:=
\left(
N,\rho,\rho_{\rm fund},r_A,A_{stencil},
\Lambda_*,D_{prod}^{act},Y_{61}^{BTQ},
\mathfrak T_{red}^{act},\mathfrak L_{red}^{act},
h_*^{act},p_*^{act},\Sigma_*^{act},
\mathsf b_{97}
\right).
```

Here:

1. \(N\) fixes the group \(SU(N)\);
2. \(\rho\) is the tested nontrivial representation and
   \(\rho_{\rm fund}\) is the fundamental branch when used;
3. \(r_A\) and \(A_{stencil}\) fix the local action range and finite action
   stencil;
4. \(\Lambda_*\) is the active representation cutoff;
5. \(D_{prod}^{act}\) is the active product-degree cutoff;
6. \(Y_{61}^{BTQ}\) is the bounded collar of Definition 75.1;
7. \(\mathfrak T_{red}^{act}\), \(\mathfrak L_{red}^{act}\),
   \(h_*^{act}\), \(p_*^{act}\), and \(\Sigma_*^{act}\) are the finite vertex
   coordinates of Definition 92.1;
8. \(\mathsf b_{97}\in
   \{\mathrm{fulllaw},\mathrm{fixeddeg},\mathrm{degtail},\mathrm{HKSM}\}\)
   is the branch closure convention.

The first-pass vertex set is

```math
\overline V_{97}
:=
\overline V_{92}(\mathfrak P_{97}),
```

with the same physical quotient as Definition 92.1.  The first-pass
certificate is

```math
\mathsf C_{97}^{red}
:=
(\overline V_{97},\overline E_{97},
s,t,c,\xi,a,\Delta_X,\mathcal O,\mathsf r,\mathsf p,\mathsf b).
```

All row entries below are functions of \(\mathfrak P_{97}\).  No row may
change \(\mathfrak P_{97}\) after the census starts.

### Definition 97.2: Step 2 `SD` Row Census

The `SD` census is the finite set

```math
\overline E_{SD}^{97}
:=
\left\{
e_{SD}(\bar v,\xi):
\bar v\in\overline V_{97},\
\xi\in\Xi_{SD},\
R_{SD}(\bar v,\xi)\ \text{is defined}
\right\}.
```

For \(e=e_{SD}(\bar v,\xi)\), set

```math
s(e):=\bar v,
\qquad
t(e):=R_{SD}(\bar v,\xi),
\qquad
c(e):=SD,
\qquad
\xi(e):=\xi.
```

The absolute coefficient slot is

```math
a(e)
:=
B_{SD,s}(e)B_{SD,t}(e)
a_{SD}^{raw}(e),
```

where \(B_{SD,s}\) and \(B_{SD,t}\) are the declared source/target normal-form
costs after `BTQ/ACTFULLLAW` contraction.  If no normal-form insertion is
needed, the corresponding factor is \(1\).

The support increment is

```math
\Delta_X(e)
:=
|X_{t(e)}^{loc}\setminus X_{s(e)}^{loc}|,
```

computed in the reduced local frontier representative.  The decay indicator is

```math
d(e)=\Delta_X(e)\mathbf 1_{\{\Delta_X(e)\ge1\}}.
```

The inverse-row contribution is

```math
\mathcal O(e):=\mathcal O_{SD}(\bar v,\xi).
```

The disposition is assigned by the following strict rule:

```math
\mathsf r(e)
=
\begin{cases}
\mathrm{pass},&
\Delta_X(e)\ge1\text{ and all admissibility checks pass},\\
\mathrm{zero},&
a(e)=0\text{ by a named exact same-record SD identity},\\
\mathrm{BTQ},&
e\text{ is an internal bounded-collar stagnant row},\\
\mathrm{CMSSI},&
\Delta_X(e)=0\text{ and the row is assigned wholly to shell inversion},\\
\mathrm{carry},&
\text{otherwise}.
\end{cases}
```

The provenance label \(\mathsf p(e)\) must name the compact-group
Schwinger-Dyson/Casimir identity and the finite projected row used to produce
it.  The closure label is \(\mathsf b(e)=\mathsf b_{97}\).

The first-pass `SD` outputs are

```math
C_{SD}^{out,97}
:=
\max_{\bar v}
\#\{e\in\overline E_{SD}^{97}:s(e)=\bar v,\ \mathsf r(e)=\mathrm{pass}\},
```

```math
A_{SD}^{97}
:=
\max_{e\in\overline E_{SD}^{97},\,\mathsf r(e)=\mathrm{pass}}
\max(1,a(e)),
```

and

```math
\Omega_{SD}^{97}(\mathbf a)
:=
\sup_{\alpha}
\sum_{\substack{e\in\overline E_{SD}^{97}\\s(e)=\bar v_\alpha\\
\mathsf r(e)=\mathrm{pass}}}
|\mathcal O(e)|
\exp\{-a_X\Delta_X(e)-a_C\Delta_C(e)-a_h\Delta_h(e)-a_p\Delta_p(e)\}.
```

### Definition 97.3: Step 3 `act` Row Census

The `act` census is the finite set

```math
\overline E_{act}^{97}
:=
\left\{
e_{act}(\bar v,\xi):
\bar v\in\overline V_{97},\
\xi\in\Xi_{act},\
R_{act}(\bar v,\xi)\ \text{is defined}
\right\}.
```

For \(e=e_{act}(\bar v,\xi)\), set

```math
s(e):=\bar v,\quad
t(e):=R_{act}(\bar v,\xi),\quad
c(e):=act,\quad
\xi(e):=\xi.
```

The coefficient slot is

```math
a(e)
:=
B_{act,s}(e)B_{act,t}(e)
a_{act}^{raw}(e).
```

Here \(a_{act}^{raw}(e)\) is the finite local action/product coefficient
inside the cutoff \((A_{stencil},\Lambda_*,D_{prod}^{act})\).  If the row
requires a representation outside \(\Lambda_*\) or product degree above
\(D_{prod}^{act}\), it is not an `act` pass row and must enter the declared
tail budget.

The support increment, inverse-row contribution, provenance, and closure label
are

```math
\Delta_X(e):=|X_{t(e)}^{loc}\setminus X_{s(e)}^{loc}|,
\qquad
\mathcal O(e):=\mathcal O_{act}(\bar v,\xi),
```

```math
\mathsf p(e):=\mathrm{local\ action/product\ row\ on\ }\mu_j^{SEL2},
\qquad
\mathsf b(e):=\mathsf b_{97}.
```

The disposition is

```math
\mathsf r(e)
=
\begin{cases}
\mathrm{pass},&
\Delta_X(e)\ge1\text{ and all admissibility checks pass},\\
\mathrm{zero},&
a(e)=0\text{ by a named same-record action identity},\\
\mathrm{BTQ},&
e\text{ is an internal bounded-collar row},\\
\mathrm{CMSSI},&
\Delta_X(e)=0\text{ and the row is assigned wholly to shell inversion},\\
\mathrm{carry},&
\text{otherwise}.
\end{cases}
```

The first-pass `act` outputs are

```math
C_{act}^{out,97}
:=
\max_{\bar v}
\#\{e\in\overline E_{act}^{97}:s(e)=\bar v,\ \mathsf r(e)=\mathrm{pass}\},
```

```math
A_{act}^{97}
:=
\max_{e\in\overline E_{act}^{97},\,\mathsf r(e)=\mathrm{pass}}
\max(1,a(e)),
```

and the weighted row sum \(\Omega_{act}^{97}(\mathbf a)\) obtained from
Definition 91.3 with the certified `act` rows.

### Definition 97.4: Step 4 `fus` And `cmp` Row Census

The `fus` census is

```math
\overline E_{fus}^{97}
:=
\left\{
e_{fus}(\bar v,\mu,\lambda,\mu',m):
\bar v\in\overline V_{97},\
\mu,\lambda,\mu'\in\Lambda_*,\
1\le m\le N_{\mu,\lambda}^{\mu'},\
R_{fus}(\bar v,\mu,\lambda,\mu',m)\ \text{is defined}
\right\}.
```

For \(e\in\overline E_{fus}^{97}\),

```math
a(e)
:=
B_{fus,s}(e)B_{fus,t}(e)N_{\mu,\lambda}^{\mu'},
\qquad
\mathcal O(e):=\mathcal O_{fus}(e).
```

The `cmp` census is

```math
\overline E_{cmp}^{97}
:=
\left\{
e_{cmp}(\bar v,\xi):
\bar v\in\overline V_{97},\
\xi\in\Xi_{cmp},\
R_{cmp}(\bar v,\xi)\ \text{is defined}
\right\}.
```

For \(e\in\overline E_{cmp}^{97}\),

```math
a(e)
:=
B_{cmp,s}(e)B_{cmp,t}(e)a_{cmp}^{raw}(e),
\qquad
\mathcal O(e):=\mathcal O_{cmp}(e).
```

The default disposition for `fus` and `cmp` rows is:

```math
\mathsf r(e)
=
\begin{cases}
\mathrm{pass},&
\Delta_X(e)\ge1\text{ and the row is a genuine retained reduced escape},\\
\mathrm{CMSSI},&
\Delta_X(e)=0\text{ and the row is assigned to shell inversion},\\
\mathrm{cmpbat},&
c(e)=cmp\text{ and the row is wholly inside the common comparison battery},\\
\mathrm{zero},&
a(e)=0\text{ by a named exact finite identity},\\
\mathrm{carry},&
\text{otherwise}.
\end{cases}
```

These rows are neutral for analytic decay unless a separate same-record
theorem says otherwise.  Therefore their decay weight is

```math
d(e)=0
```

unless they are explicitly reclassified by a new source theorem.  They still
contribute to \(C_{geom}\), \(A_{esc}\), and \(g_q\).

Set

```math
C_{fus}^{out,97},\ C_{cmp}^{out,97},
\qquad
A_{fus}^{97},\ A_{cmp}^{97},
\qquad
\Omega_{fus}^{97}(\mathbf a),\ \Omega_{cmp}^{97}(\mathbf a)
```

by the same finite maxima and weighted row sums as in Definitions 97.2 and
97.3.

The empty-class convention is:

```math
C_c^{out,97}=0,\qquad A_c^{97}=1,\qquad
\Omega_c^{97}(\mathbf a)=0
```

whenever the retained pass rows of class \(c\) are empty.

### Definition 97.5: Step 5 Assembled First-Pass Certificate

The first-pass candidate edge set is the disjoint union

```math
\overline E_{97}
:=
\overline E_{SD}^{97}
\dot\cup
\overline E_{act}^{97}
\dot\cup
\overline E_{fus}^{97}
\dot\cup
\overline E_{cmp}^{97}.
```

The retained pass set is

```math
\overline E_{pass}^{97}
:=
\{e\in\overline E_{97}:\mathsf r(e)=\mathrm{pass}\}.
```

The first-pass constants are

```math
C_{geom}^{97}
:=
\max_{\bar v\in\overline V_{97}}
\#\{e\in\overline E_{pass}^{97}:s(e)=\bar v\},
```

```math
A_{esc}^{97}
:=
\max\left(
1,A_{SD}^{97},A_{act}^{97},A_{fus}^{97},A_{cmp}^{97}
\right),
```

and

```math
\Omega_{tot}^{97}(\mathbf a)
:=
\Omega_{SD}^{97}(\mathbf a)
+\Omega_{act}^{97}(\mathbf a)
+\Omega_{fus}^{97}(\mathbf a)
+\Omega_{cmp}^{97}(\mathbf a).
```

The finite inverse exponent is

```math
g_q^{97}
=
\begin{cases}
0,&\exists\mathbf a\text{ with }g_w(\mathbf a)=0
\text{ and }\Omega_{tot}^{97}(\mathbf a)<\kappa_{\min}^{red},\\
g_{q,cert}^{97},&\exists\mathbf a
\text{ with }\Omega_{tot}^{97}(\mathbf a)<\kappa_{\min}^{red}
\text{ but only positive spread},\\
g_q^{car},&\text{otherwise},
\end{cases}
```

where

```math
g_{q,cert}^{97}
:=
\inf_{\Omega_{tot}^{97}(\mathbf a)<\kappa_{\min}^{red}}
g_w(\mathbf a).
```

The closure surcharge is

```math
g_{bat}^{97}
:=
\begin{cases}
0,&\mathsf b_{97}\in\{\mathrm{fulllaw},\mathrm{fixeddeg},\mathrm{HKSM}\},\\
g_{bat}^{BTQ},&\mathsf b_{97}=\mathrm{degtail}.
\end{cases}
```

Thus

```math
G_{fin}^{97}
:=
\log A_{esc}^{97}
+\log C_{geom}^{97}
+g_q^{97}
+g_{bat}^{97}.
```

### Algorithm 97.6: Step 6 Audit And Margin Output

Run the following finite computation on \(\overline E_{pass}^{97}\).

0. **Check table supplied.**  If any required row class in
   \(\mathsf C_{97}^{red}\) has no finite constructor table, return
   `PARK-TABLE`.  If the constructors are supplied but the concrete finite
   index lists, raw coefficients, exact-zero identities, or disposition
   choices have not been literally expanded for the chosen
   \(\mathfrak P_{97}\), return `PARK-ENUM`.
1. Build the zero-growth graph

   ```math
   \overline{\mathfrak A}_{0}^{97}
   :=
   (\overline V_{97},
   \{e\in\overline E_{pass}^{97}:\Delta_X(e)=0\}).
   ```

2. If \(\overline{\mathfrak A}_{0}^{97}\) has a directed cycle, set
   \(c_{size}^{97}=0\) and return `FAIL-SIZE` unless the certificate is
   repaired.
3. Otherwise set

   ```math
   c_{size}^{97}:=(L_0^{97}+1)^{-1}.
   ```

4. Compute

   ```math
   \chi_{cyc}^{97}
   :=
   \min_{\substack{\Gamma\ {\rm simple\ directed\ cycle}\\u(\Gamma)>0}}
   {d(\Gamma)\over u(\Gamma)}.
   ```

   If \(\chi_{cyc}^{97}=0\), return `FAIL-COVER` unless the certificate is
   repaired.

5. If \(\chi_{cyc}^{97}=+\infty\) and the pass graph is acyclic, return the
   finite-depth conclusion

   ```math
   T_{\ge K}^{red,act}(j)=0\qquad(K>K_{max}^{97}).
   ```

6. On the all-depth branch, output

   ```math
   \Delta_{1KP,best}^{97}
   :=
   \mu_0\chi_{cyc}^{97}c_{size}^{97}
   -\lambda_{sem}
   -G_{fin}^{97}.
   ```

   If `P21-RED-1KP(mu_0,lambda_sem,alpha_0,C_0)` is not supplied, return
   `PARK-1KP`.  If it is supplied and \(\Delta_{1KP,best}^{97}>0\), return
   `PASS-REDTAIL`.  If rigorous bounds force
   \(\Delta_{1KP,best}^{97}\le0\), return `FAIL-MARGIN`.  Otherwise return
   `PARK-MARGIN`.

### Theorem 97.7: Six-Step Execution Verdict

The six requested steps are now executed at the level licensed by the present
source papers.

1. **Parameters frozen.**  Definition 97.1 fixes
   \(\mathfrak P_{97}\).  The certificate may not change \(N\), \(r_A\),
   \(\Lambda_*\), \(D_{prod}^{act}\), \(Y_{61}^{BTQ}\), or the closure branch
   mid-proof.
2. **`SD` rows enumerated schematically.**  Definition 97.2 gives the exact
   finite `SD` row set, coefficient slot, support increment, inverse row, and
   disposition rule.
3. **`act` rows enumerated schematically.**  Definition 97.3 gives the exact
   finite `act` row set and its cutoff/tail discipline.
4. **`fus/cmp` rows enumerated schematically.**  Definition 97.4 gives the
   finite channel and comparison rows and marks them decay-neutral unless a new
   same-record theorem reclassifies them.
5. **Certificate assembled.**  Definition 97.5 builds
   \(\overline E_{pass}^{97}\), \(A_{esc}^{97}\), \(C_{geom}^{97}\),
   \(g_q^{97}\), \(g_{bat}^{97}\), and \(G_{fin}^{97}\).
6. **Audit executed.**  Algorithm 97.6 returns one of:

   ```math
   \mathrm{PASS\text{-}REDTAIL},\quad
   \mathrm{PARK\text{-}TABLE},\quad
   \mathrm{PARK\text{-}ENUM},\quad
   \mathrm{FAIL\text{-}SIZE},\quad
   \mathrm{FAIL\text{-}COVER},\quad
   \mathrm{FAIL\text{-}MARGIN},\quad
   \mathrm{PARK\text{-}1KP},\quad
   \mathrm{PARK\text{-}MARGIN}.
   ```

Before Section 98, the honest output is `PARK-TABLE` until concrete finite
row constructors are supplied.  After the constructors are supplied but before
the literal finite index expansion is printed, the honest output is
`PARK-ENUM`.  After that enumeration, the next likely park is `PARK-1KP`
unless the same-record one-step KP constants \((\mu_0,\lambda_{sem})\) are
proved.  It is not legitimate to replace any missing input by a continuum
Yang-Mills measure, an area law, a mass gap, or an unrecorded local stochastic
process.

Proof.

Items 1--5 are Definitions 97.1--97.5.  Item 6 is Algorithm 97.6.  Finiteness
comes from the fixed branch record: \(\overline V_{97}\) is finite, each
\(\Xi_c\) is finite for fixed
\((N,r_A,\Lambda_*,D_{prod}^{act},Y_{61}^{BTQ})\), and every row is either
retained, repaired, zeroed, assigned to an already named finite battery, or
carried.  The same-record restriction follows from Definition 96.2 and from
the Paper-10/Paper-20 audits: exact finite-battery projectivity is available
only for declared finite records, while the tree-rate and reduced-tail source
remain same-record source theorems rather than downstream confinement
assumptions. `square`

### Corollary 97.8: What To Do After This Section

The next nonformal task is now a literal table fill, in this order:

```math
\overline E_{SD}^{97},
\qquad
\overline E_{act}^{97},
\qquad
\overline E_{fus}^{97},
\qquad
\overline E_{cmp}^{97}.
```

After those four tables are filled, Algorithm 97.6 computes the finite side
without further conceptual choices.  Only then should the proof of
`P21-RED-1KP` be attempted, because only then is the target inequality fixed:

```math
\mu_0\chi_{cyc}^{97}c_{size}^{97}
-\lambda_{sem}
>
\log A_{esc}^{97}
+\log C_{geom}^{97}
+g_q^{97}
+g_{bat}^{97}.
```

## 98. Filled Constructor Tables For The Four Row Classes

Corollary 97.8 asks for the finite tables in the order

```math
\overline E_{SD}^{97},\quad
\overline E_{act}^{97},\quad
\overline E_{fus}^{97},\quad
\overline E_{cmp}^{97}.
```

This section fills those tables at the strongest level currently licensed by
the source papers: finite row constructors with exact admissibility,
coefficient, support, inverse, and disposition columns.  It does not pretend
that Papers 10--14 or Paper 20 already contain a printed numerical list of
all vertices, raw local coefficients, Clebsch-Gordan multiplicities, or exact
zero identities for the chosen \(\mathfrak P_{97}\).  Thus this section
discharges `PARK-TABLE` and leaves the more concrete `PARK-ENUM` until the
finite index expansion is carried out.

### Table 98.1: Filled `SD` Constructor Table

For every \(\bar v\in\overline V_{97}\) and
\(\xi\in\Xi_{SD}\), form \(e=e_{SD}(\bar v,\xi)\) when
\(R_{SD}(\bar v,\xi)\) is defined.  Write

```math
R_{SD}(\bar v,\xi)
=
(\bar v',\Delta_X,\Delta_C,\Delta_h,\Delta_p,a_{raw},\mathcal O_{raw}).
```

The filled `SD` rows are:

| row family | condition | \(s(e)\to t(e)\) | \(a(e)\) | \(d(e)\) | \(\mathcal O(e)\) | disposition | provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SD-pass` | \(\Delta_X\ge1\), row admissible | \(\bar v\to\bar v'\) | \(B_{SD,s}B_{SD,t}a_{raw}\) | \(\Delta_X\) | \(\mathcal O_{raw}\) | `pass` | projected compact-group SD/Casimir row |
| `SD-CMSSI` | \(\Delta_X=0\), same-shell inverse row | \(\bar v\to\bar v'\) | \(B_{SD,s}B_{SD,t}a_{raw}\) | \(0\) | \(\mathcal O_{raw}\) | `CMSSI` | same-record shell inverse row |
| `SD-BTQ` | internal bounded-collar stagnant/channel row | internal to \(Y_{61}^{BTQ}\) | paid by `BTQ` normal form | \(0\) | not a reduced escape row | `BTQ` | bounded-collar contraction |
| `SD-zero` | exact same-record identity gives \(a_{raw}=0\) | \(\bar v\to\bar v'\) | \(0\) | \(0\) | \(0\) | `zero` | named SD/Casimir cancellation |
| `SD-carry` | row violates cutoff, source, or no-double-charge check | removed | carried | not used | not used | `carry` | named residual \(U_{SD,row}^{97}\) |

Thus

```math
\overline E_{SD,pass}^{98}
:=
\{e_{SD}(\bar v,\xi):\text{ row family is `SD-pass`}\}.
```

The `SD` contribution to the finite audit is

```math
C_{SD}^{out,98}
:=
\max_{\bar v}\#\{e\in\overline E_{SD,pass}^{98}:s(e)=\bar v\},
```

```math
A_{SD}^{98}
:=
\max_{e\in\overline E_{SD,pass}^{98}}\max(1,a(e)),
```

and

```math
\Omega_{SD}^{98}(\mathbf a)
:=
\sup_{\alpha}
\sum_{\substack{e\in\overline E_{SD,pass}^{98}\\s(e)=\bar v_\alpha}}
|\mathcal O(e)|
\exp\{-a_X\Delta_X(e)-a_C\Delta_C(e)-a_h\Delta_h(e)-a_p\Delta_p(e)\}.
```

If \(\overline E_{SD,pass}^{98}=\varnothing\), set
\(C_{SD}^{out,98}=0\), \(A_{SD}^{98}=1\), and
\(\Omega_{SD}^{98}=0\).

### Table 98.2: Filled `act` Constructor Table

For every \(\bar v\in\overline V_{97}\) and
\(\xi\in\Xi_{act}\), form \(e=e_{act}(\bar v,\xi)\) when
\(R_{act}(\bar v,\xi)\) is defined.  Write

```math
R_{act}(\bar v,\xi)
=
(\bar v',\Delta_X,\Delta_C,\Delta_h,\Delta_p,a_{raw},\mathcal O_{raw}).
```

The filled `act` rows are:

| row family | condition | \(s(e)\to t(e)\) | \(a(e)\) | \(d(e)\) | \(\mathcal O(e)\) | disposition | provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `act-pass` | \(\Delta_X\ge1\), row admissible | \(\bar v\to\bar v'\) | \(B_{act,s}B_{act,t}a_{raw}\) | \(\Delta_X\) | \(\mathcal O_{raw}\) | `pass` | local action/product row on \(\mu_j^{SEL2}\) |
| `act-CMSSI` | \(\Delta_X=0\), same-shell inverse row | \(\bar v\to\bar v'\) | \(B_{act,s}B_{act,t}a_{raw}\) | \(0\) | \(\mathcal O_{raw}\) | `CMSSI` | same-record shell inverse row |
| `act-BTQ` | internal bounded-collar row | internal to \(Y_{61}^{BTQ}\) | paid by `BTQ` normal form | \(0\) | not a reduced escape row | `BTQ` | bounded-collar contraction |
| `act-zero` | exact same-record action/product identity gives \(a_{raw}=0\) | \(\bar v\to\bar v'\) | \(0\) | \(0\) | \(0\) | `zero` | named action cancellation |
| `act-tail` | representation/product label outside \((\Lambda_*,D_{prod}^{act})\) | removed | tail budget | not used | not used | `carry` | declared representation/product tail |
| `act-carry` | source/no-double-charge check fails | removed | carried | not used | not used | `carry` | named residual \(U_{act,row}^{97}\) |

Thus

```math
\overline E_{act,pass}^{98}
:=
\{e_{act}(\bar v,\xi):\text{ row family is `act-pass`}\}.
```

The `act` contribution is

```math
C_{act}^{out,98}
:=
\max_{\bar v}\#\{e\in\overline E_{act,pass}^{98}:s(e)=\bar v\},
```

```math
A_{act}^{98}
:=
\max_{e\in\overline E_{act,pass}^{98}}\max(1,a(e)),
```

and \(\Omega_{act}^{98}(\mathbf a)\) is the corresponding finite weighted
row sum.  Empty-class values are \(0,1,0\) as above.

### Table 98.3: Filled `fus` Constructor Table

For every \(\bar v\in\overline V_{97}\) and
\((\mu,\lambda,\mu',m)\in\Xi_{fus}\), form
\(e=e_{fus}(\bar v,\mu,\lambda,\mu',m)\) when \(R_{fus}\) is defined.  Write

```math
R_{fus}(\bar v,\mu,\lambda,\mu',m)
=
(\bar v',\Delta_X,\Delta_C,\Delta_h,\Delta_p,a_{raw},\mathcal O_{raw}).
```

The filled `fus` rows are:

| row family | condition | \(s(e)\to t(e)\) | \(a(e)\) | \(d(e)\) | \(\mathcal O(e)\) | disposition | provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fus-pass` | \(\Delta_X\ge1\), genuine retained reduced escape | \(\bar v\to\bar v'\) | \(B_{fus,s}B_{fus,t}N_{\mu,\lambda}^{\mu'}\) | \(0\) | \(\mathcal O_{raw}\) | `pass` | finite Clebsch-Gordan/channel lift |
| `fus-CMSSI` | \(\Delta_X=0\), same-shell channel row | \(\bar v\to\bar v'\) | \(B_{fus,s}B_{fus,t}N_{\mu,\lambda}^{\mu'}\) | \(0\) | \(\mathcal O_{raw}\) | `CMSSI` | shell inverse/channel bookkeeping |
| `fus-zero` | multiplicity or projected coefficient is zero | \(\bar v\to\bar v'\) | \(0\) | \(0\) | \(0\) | `zero` | finite fusion identity |
| `fus-tail` | at least one representation label lies outside \(\Lambda_*\) | removed | tail budget | not used | not used | `carry` | representation-tail ledger |
| `fus-carry` | not same-record or no-double-charge check fails | removed | carried | not used | not used | `carry` | named residual \(U_{fus,row}^{97}\) |

The `fus` rows are decay-neutral in this branch:

```math
d(e)=0
\qquad(e\in\overline E_{fus}^{98}),
```

unless a later same-record theorem explicitly reclassifies a fusion row as
decay-eligible.  Their finite outputs are

```math
C_{fus}^{out,98},\qquad A_{fus}^{98},\qquad
\Omega_{fus}^{98}(\mathbf a)
```

by the same finite maxima and row sums over `fus-pass` rows.

### Table 98.4: Filled `cmp` Constructor Table

For every \(\bar v\in\overline V_{97}\) and
\(\xi\in\Xi_{cmp}\), form \(e=e_{cmp}(\bar v,\xi)\) when
\(R_{cmp}(\bar v,\xi)\) is defined.  Write

```math
R_{cmp}(\bar v,\xi)
=
(\bar v',\Delta_X,\Delta_C,\Delta_h,\Delta_p,a_{raw},\mathcal O_{raw}).
```

The filled `cmp` rows are:

| row family | condition | \(s(e)\to t(e)\) | \(a(e)\) | \(d(e)\) | \(\mathcal O(e)\) | disposition | provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `cmp-pass` | non-retracting comparison escape, \(\Delta_X\ge1\) | \(\bar v\to\bar v'\) | \(B_{cmp,s}B_{cmp,t}a_{raw}\) | \(0\) | \(\mathcal O_{raw}\) | `pass` | common \(E_{14}/X_{13}\) comparison move |
| `cmp-battery` | row wholly inside common finite comparison battery | battery internal | paid inside battery | \(0\) | battery internal | `cmpbat` | common finite battery |
| `cmp-CMSSI` | \(\Delta_X=0\), same-shell comparison row not internal to battery | \(\bar v\to\bar v'\) | \(B_{cmp,s}B_{cmp,t}a_{raw}\) | \(0\) | \(\mathcal O_{raw}\) | `CMSSI` | shell inverse/comparison row |
| `cmp-zero` | exact finite comparison identity gives \(a_{raw}=0\) | \(\bar v\to\bar v'\) | \(0\) | \(0\) | \(0\) | `zero` | exact comparison identity |
| `cmp-carry` | finite comparison audit not proved | removed | carried | not used | not used | `carry` | named residual \(U_{cmp,row}^{97}\) |

The `cmp` rows are also decay-neutral by default:

```math
d(e)=0
\qquad(e\in\overline E_{cmp}^{98}).
```

Their finite outputs are

```math
C_{cmp}^{out,98},\qquad A_{cmp}^{98},\qquad
\Omega_{cmp}^{98}(\mathbf a)
```

by finite maxima and row sums over `cmp-pass` rows.

### Definition 98.5: Assembled Filled Constructor Certificate

The filled constructor-level pass set is

```math
\overline E_{pass}^{98}
:=
\overline E_{SD,pass}^{98}
\dot\cup
\overline E_{act,pass}^{98}
\dot\cup
\overline E_{fus,pass}^{98}
\dot\cup
\overline E_{cmp,pass}^{98}.
```

The finite constants are now constructor-level table functions:

```math
C_{geom}^{98}
:=
\max_{\bar v\in\overline V_{97}}
\#\{e\in\overline E_{pass}^{98}:s(e)=\bar v\},
```

```math
A_{esc}^{98}
:=
\max(1,A_{SD}^{98},A_{act}^{98},A_{fus}^{98},A_{cmp}^{98}),
```

```math
\Omega_{tot}^{98}(\mathbf a)
:=
\Omega_{SD}^{98}(\mathbf a)
+\Omega_{act}^{98}(\mathbf a)
+\Omega_{fus}^{98}(\mathbf a)
+\Omega_{cmp}^{98}(\mathbf a).
```

The zero-growth and coverage graphs are computed from
\(\overline E_{pass}^{98}\) by Algorithm 97.6:

```math
c_{size}^{98},\qquad
\chi_{cyc}^{98}.
```

Finally,

```math
G_{fin}^{98}
:=
\log A_{esc}^{98}
+\log C_{geom}^{98}
+g_q^{98}
+g_{bat}^{98}.
```

### Theorem 98.6: Corollary 97.8 Is Filled At Constructor Level

Tables 98.1--98.4 fill the four finite row classes requested by Corollary
97.8.  They discharge `PARK-TABLE` in Algorithm 97.6 in the following precise
sense: every row class has a finite constructor, a coefficient slot, a support
increment, an inverse slot, a disposition rule, and a same-record provenance
requirement.

They do not discharge `PARK-ENUM`.  To discharge `PARK-ENUM`, one must still
expand the concrete finite sets

```math
\overline V_{97},\quad
\Xi_{SD},\quad
\Xi_{act},\quad
\Xi_{fus},\quad
\Xi_{cmp}
```

for the chosen \(\mathfrak P_{97}\), and insert the actual values of
\(a_{raw}\), \(\mathcal O_{raw}\), \(\Delta_X\), and the exact-zero/carry
decisions for each row.

Proof.

Each table is finite because \(\overline V_{97}\) and all \(\Xi_c\) are finite
at fixed \(\mathfrak P_{97}\).  Each table row either becomes a retained pass
edge, is assigned to `CMSSI`, `BTQ`, or `cmpbat`, is zero by a named finite
identity, or is carried in a named residual.  Therefore no fifth row class is
left unaccounted for, and no row is allowed to import a continuum measure,
area law, mass gap, or off-record process.  The remaining enumeration is
literal finite arithmetic and representation bookkeeping, not a new source
principle. `square`

### Corollary 98.7: Updated Execution Status

After Section 98, the current honest output of Algorithm 97.6 is:

```math
\mathrm{PARK\text{-}ENUM}.
```

The next task is to choose a concrete \(\mathfrak P_{97}\) small enough to
enumerate, expand the four finite constructor tables, and then compute

```math
c_{size}^{98},\quad
\chi_{cyc}^{98},\quad
A_{esc}^{98},\quad
C_{geom}^{98},\quad
g_q^{98},\quad
g_{bat}^{98}.
```

Only after that computation is complete should the same-record one-step KP
estimate be fitted to the actual margin

```math
\mu_0\chi_{cyc}^{98}c_{size}^{98}
-\lambda_{sem}
>
G_{fin}^{98}.
```

## 99. Stepwise Literal Enumeration Attempt And Status Lock

Section 98 discharges `PARK-TABLE`.  This section executes the next five
steps in the strict order required by Corollary 98.7:

1. choose a concrete \(\mathfrak P_{97}\);
2. expand the finite index sets;
3. insert row values and dispositions;
4. compute the finite constants;
5. fit the same-record one-step KP estimate.

The execution is deliberately conservative.  If a value is not printed by
Papers 10--14 or Paper 20 as a finite same-record datum, it is not guessed.
It is recorded as a named missing finite entry.  This is not a philosophical
pause; it is the only way to keep the reduced confinement route upstream of
any area-law, mass-gap, or continuum-Yang-Mills assumption.

### Source Audit 99.1: Current Status After Section 98

The current status is:

```math
\mathrm{PARK\text{-}ENUM}.
```

The following are already supplied.

| item | status after Section 98 |
| --- | --- |
| four row classes | closed: `SD`, `act`, `fus`, `cmp` |
| constructor tables | closed at finite-constructor level |
| same-record admissibility rule | closed by Definitions 96.2 and 97.1 |
| no-double-charge rule | closed by Definitions 96.2 and 98.1--98.4 |
| finite growth formula | closed as a table function |
| finite SCC/coverage algorithm | closed as Algorithm 97.6 |

The following are not yet supplied.

| missing finite datum | why it matters |
| --- | --- |
| literal \(\overline V_{97}\) list | without vertices, there is no pass graph |
| literal \(\Xi_{SD},\Xi_{act},\Xi_{cmp}\) lists | without indices, only constructors exist |
| row maps \(R_{SD},R_{act},R_{cmp}\) on the chosen branch | without targets and increments, SCC/coverage cannot run |
| raw row coefficients \(a_{raw}\) and inverse slots \(\mathcal O_{raw}\) | without these, \(A_{esc}\) and \(g_q\) cannot be computed |
| exact-zero and carry decisions row by row | without these, the retained pass set is not fixed |
| `P21-RED-1KP` constants | without these, the analytic exponent cannot be fitted |

Thus the current honest output remains `PARK-ENUM`, not `PARK-1KP`: the
one-step KP source should not be fitted before the finite pass graph exists.

### Definition 99.2: Minimal Literal Probe \(\mathfrak P_{99}^{min}\)

The first literal probe is the smallest nontrivial branch that can be tested
without changing the ontology:

```math
\mathfrak P_{99}^{min}
:=
\left(
N=2,\rho={1\over2},\rho_{\rm fund}={1\over2},
r_A=1,A_{stencil}=A_{plaq}^{Wilson},
\Lambda_*^{99},D_{prod}^{act}=2,
Y_{61}^{BTQ},\mathfrak T_{red}^{act},
\mathfrak L_{red}^{act},
h_*^{act},p_*^{act},\Sigma_*^{act},
\mathsf b_{99}=\mathrm{fulllaw}
\right),
```

with

```math
\Lambda_*^{99}:=\{0,{1\over2},1\}
```

in the usual \(SU(2)\) spin notation.

This is a probe, not a general `SU(N)` theorem.  Its purpose is to decide
whether the certificate machinery can be made literal on the smallest
nontrivial active channel.  If it passes, the same construction can be
enlarged.  If it fails because of a genuine SCC, coverage, or margin
obstruction, it falsifies this minimal probe only.

The `fulllaw` choice is intentional: it tests the cleanest branch identified
in Theorem 85.3 and Corollary 85.11, so no degree-tail battery surcharge is
introduced at the first enumeration attempt:

```math
g_{bat}^{99}=0.
```

### Theorem 99.3: Step 1 Is A Legal Same-Record Freeze

\(\mathfrak P_{99}^{min}\) is a legal instance of the finite certificate
framework.  It fixes the group, tested representation, representation cutoff,
local action range, product cutoff, bounded-collar convention, reduced vertex
coordinate families, and closure branch before any row is enumerated.

It does not prove confinement, does not choose a continuum Yang-Mills measure,
and does not import an area law or mass gap.

Proof.

All entries in \(\mathfrak P_{99}^{min}\) are finite branch data of the type
allowed in Definition 97.1.  The representation cutoff is finite, the product
cutoff is finite, and the closure branch is one of the four allowed values.
The branch still reads all rows under the active pushed-forward `SEL2` scalar
law and therefore satisfies the no-smuggling condition of Definition 96.2.
`square`

### Definition 99.4: Step 2 Finite Index Expansion

For the probe \(\mathfrak P_{99}^{min}\), the representation-fusion part is
literal.  The \(SU(2)\) tensor rule is

```math
j_1\otimes j_2
=
\bigoplus_{j=|j_1-j_2|}^{j_1+j_2}j,
```

with unit multiplicities.  Retaining only \(\Lambda_*^{99}=\{0,1/2,1\}\),
the retained fusion index set is:

| \(\mu\) | \(\lambda\) | retained \(\mu'\) | multiplicity |
| --- | --- | --- | --- |
| \(0\) | \(0\) | \(0\) | \(1\) |
| \(0\) | \(1/2\) | \(1/2\) | \(1\) |
| \(0\) | \(1\) | \(1\) | \(1\) |
| \(1/2\) | \(0\) | \(1/2\) | \(1\) |
| \(1/2\) | \(1/2\) | \(0,1\) | \(1,1\) |
| \(1/2\) | \(1\) | \(1/2\) | \(1\) |
| \(1\) | \(0\) | \(1\) | \(1\) |
| \(1\) | \(1/2\) | \(1/2\) | \(1\) |
| \(1\) | \(1\) | \(0,1\) | \(1,1\) |

Equivalently,

```math
|\Xi_{fus}^{99}|=11.
```

The omitted channels

```math
{1\over2}\otimes1\supset{3\over2},
\qquad
1\otimes{1\over2}\supset{3\over2},
\qquad
1\otimes1\supset2
```

are not retained pass rows at this cutoff.  They enter the representation-tail
ledger if the corresponding local row tries to use them.

The other three index sets are finite but not literally expanded by the
current corpus:

```math
\Xi_{SD}^{99},\qquad
\Xi_{act}^{99},\qquad
\Xi_{cmp}^{99}.
```

To discharge `PARK-ENUM`, the paper still needs the following finite lists.

```math
\mathrm{TRED\text{-}LIST}_{99}:=\mathfrak T_{red}^{act},
\qquad
\mathrm{LRED\text{-}LIST}_{99}:=\mathfrak L_{red}^{act},
```

```math
\mathrm{SD\text{-}IDX}_{99}:=\Xi_{SD}^{99},
\qquad
\mathrm{ACT\text{-}IDX}_{99}:=\Xi_{act}^{99},
\qquad
\mathrm{CMP\text{-}IDX}_{99}:=\Xi_{cmp}^{99}.
```

### Theorem 99.5: Step 2 Verdict

Step 2 is partially executed:

```math
\Xi_{fus}^{99}
\quad\text{is literally enumerated,}
```

but

```math
\overline V_{99},\quad
\Xi_{SD}^{99},\quad
\Xi_{act}^{99},\quad
\Xi_{cmp}^{99}
```

are not yet literal finite lists in the current source corpus.

Consequently Step 2 does not discharge `PARK-ENUM`.

Proof.

The fusion table follows from the \(SU(2)\) Clebsch-Gordan rule and the
declared cutoff \(\Lambda_*^{99}\).  The vertex set still depends on the
finite reduced template list and local frontier quotient, while the `SD`,
`act`, and `cmp` indices depend on the projected Schwinger-Dyson row list,
the active local action stencil/product list, and the common comparison
battery seed list.  Sections 92, 97, and 98 define these as finite
constructors but do not print their literal entries. `square`

### Definition 99.6: Step 3 Row-Value Package

For \(\mathfrak P_{99}^{min}\), define the literal row-value package

```math
\mathcal D_{99}^{row}
:=
\left(
\overline V_{99},
\Xi_{SD}^{99},\Xi_{act}^{99},\Xi_{cmp}^{99},
R_{SD}^{99},R_{act}^{99},R_{fus}^{99},R_{cmp}^{99},
a_{raw}^{99},\mathcal O_{raw}^{99},
\mathsf z^{99},\mathsf c^{99}
\right).
```

Here \(\mathsf z^{99}\) is the finite list of exact-zero identities, and
\(\mathsf c^{99}\) is the finite list of carry/tail assignments.

The known part of \(\mathcal D_{99}^{row}\) is:

```math
N_{\mu,\lambda}^{\mu'}=1
\qquad
((\mu,\lambda,\mu')\in\Xi_{fus}^{99}).
```

Thus the retained fusion coefficients satisfy

```math
a_{fus}^{99}(e)
=
B_{fus,s}(e)B_{fus,t}(e)
```

for every retained fusion row.  Under the strict full-law normal form with no
source/target insertion cost this becomes \(a_{fus}^{99}(e)=1\).

All other row values remain entries of \(\mathcal D_{99}^{row}\).

### Theorem 99.7: Step 3 Verdict

Step 3 cannot be completed from the current text.  The missing data are finite
and explicit, but they are not present:

```math
R_{SD}^{99},\ R_{act}^{99},\ R_{cmp}^{99},
\quad
\Delta_X,\Delta_C,\Delta_h,\Delta_p,
\quad
a_{raw},\mathcal O_{raw},
\quad
\mathsf z^{99},\mathsf c^{99}.
```

The known fusion multiplicities alone are insufficient to classify pass,
CMSSI, comparison-battery, zero, and carry rows, because the target vertex and
support increment still come from the row maps.

Therefore the current algorithmic output remains:

```math
\mathrm{PARK\text{-}ENUM}.
```

Proof.

Algorithm 97.6 requires a retained pass graph.  A retained pass graph requires
source and target vertices, support increments, row coefficients, inverse
slots, and dispositions.  The \(SU(2)\) fusion multiplicity table provides
only one coefficient subslot.  It does not provide \(R_c\), \(\Delta_X\), or
the zero/carry decisions.  Hence the finite graph is not yet defined. `square`

### Definition 99.8: Step 4 Conditional Finite Constants

If \(\mathcal D_{99}^{row}\) is supplied, define

```math
\overline E_{pass}^{99}
:=
\{e\in\overline E^{99}:\mathsf r(e)=\mathrm{pass}\}.
```

Then

```math
C_{geom}^{99}
:=
\max_{\bar v\in\overline V_{99}}
\#\{e\in\overline E_{pass}^{99}:s(e)=\bar v\},
```

```math
A_{esc}^{99}
:=
\max_{e\in\overline E_{pass}^{99}}\max(1,a(e)),
```

```math
c_{size}^{99}
:=
\begin{cases}
(L_0^{99}+1)^{-1},&
\overline{\mathfrak A}_0^{99}\text{ acyclic},\\
0,&\text{otherwise},
\end{cases}
```

and

```math
\chi_{cyc}^{99}
:=
\min_{\substack{\Gamma\ {\rm simple\ directed\ cycle}\\u(\Gamma)>0}}
{d(\Gamma)\over u(\Gamma)}.
```

For the `SU(2)` fusion subtable alone one has the safe constructor bound

```math
C_{fus}^{out,99}\le 11.
```

If the strict full-law normal form has \(B_{fus,s}=B_{fus,t}=1\), then

```math
A_{fus}^{99}=1
```

on retained fusion rows.  These two facts are not enough to compute
\(C_{geom}^{99}\), \(A_{esc}^{99}\), \(c_{size}^{99}\), or
\(\chi_{cyc}^{99}\), because `SD`, `act`, and `cmp` rows may add pass edges,
zero-growth rows, inverse slots, and carries.

### Theorem 99.9: Step 4 Verdict

The finite constants cannot yet be computed numerically or symbolically to a
closed inequality.  The only currently certified finite subtable fact is the
fusion bound

```math
|\Xi_{fus}^{99}|=11,
\qquad
C_{fus}^{out,99}\le11,
```

with unit retained Clebsch-Gordan multiplicities.

The global constants remain conditional table functions:

```math
c_{size}^{99},\quad
\chi_{cyc}^{99},\quad
A_{esc}^{99},\quad
C_{geom}^{99},\quad
g_q^{99},\quad
g_{bat}^{99}=0.
```

Thus the status is still `PARK-ENUM`, not `FAIL-SIZE`,
`FAIL-COVER`, `PARK-1KP`, or `FAIL-MARGIN`.

Proof.

`FAIL-SIZE` and `FAIL-COVER` require an actual graph.  `PARK-1KP` requires an
actual graph and finite constants but no one-step KP source.  `FAIL-MARGIN`
requires finite constants and rigorous upper/lower bounds forcing the margin
nonpositive.  None of those states is available before
\(\mathcal D_{99}^{row}\) is supplied.  `square`

### Definition 99.10: Step 5 Exact One-Step KP Target For The Probe

Once \(\mathcal D_{99}^{row}\) is supplied, the analytic source to prove is:

```math
\mathrm{P21\text{-}RED\text{-}1KP}_{99}
(\mu_0,\lambda_{sem},\alpha_0,C_0).
```

It is Definition 94.5 restricted to the retained decay-eligible rows of the
probe:

```math
\mathcal E_{dec}^{99}
:=
\{e\in\overline E_{pass}^{99}:
c(e)\in\{SD,act\},\ \Delta_X(e)\ge1\}.
```

The required pathwise estimate is

```math
\mathcal N_{j,can}^{red}(F_f^{red})
\le
C_0(1+\overline K(f))^{\alpha_0}
\exp\left(
-\mu_0
\sum_{e_i\in\mathcal E_{dec}^{99}}\Delta_X(e_i)
+\lambda_{sem}\overline K(f)
\right),
```

cofinally in \(j\), on the same pushed-forward `SEL2` scalar law.

If this source is proved, the probe passes the reduced-tail rate test exactly
when

```math
\mu_0\chi_{cyc}^{99}c_{size}^{99}
-\lambda_{sem}
>
\log A_{esc}^{99}
+\log C_{geom}^{99}
+g_q^{99}.
```

The \(g_{bat}\) term is absent only because \(\mathsf b_{99}=\mathrm{fulllaw}\).

### Theorem 99.11: Step 5 Verdict And Updated Status

Step 5 cannot yet be attempted as a proof of `P21-RED-1KP` for the probe,
because the set \(\mathcal E_{dec}^{99}\) is not defined until
\(\mathcal D_{99}^{row}\) is supplied.

The completed stepwise execution therefore has the following rigorous status:

| step | result |
| --- | --- |
| 1. choose \(\mathfrak P_{97}\) | done: \(\mathfrak P_{99}^{min}\) |
| 2. expand finite sets | partially done: \(\Xi_{fus}^{99}\) enumerated; vertex, `SD`, `act`, `cmp` lists missing |
| 3. fill row values | parked at \(\mathcal D_{99}^{row}\) |
| 4. compute constants | conditional; only \(C_{fus}^{out,99}\le11\), \(g_{bat}^{99}=0\) certified |
| 5. fit `P21-RED-1KP` | not yet legitimate; decay-eligible edge set not fixed |

Therefore the current status of Paper 21 is locked as

```math
\boxed{\mathrm{PARK\text{-}ENUM}.}
```

The next nonformal task is now uniquely specified:

```math
\text{print }\mathcal D_{99}^{row}
\text{ for }\mathfrak P_{99}^{min}.
```

Only after that finite package is printed may the paper run SCC/coverage,
compute \(A_{esc},C_{geom},g_q\), and attack the one-step KP source.

Proof.

The table follows from Theorems 99.3, 99.5, 99.7, and 99.9.  The final
sentence is Algorithm 97.6 applied to the current data: constructor tables
exist, so the status is not `PARK-TABLE`; literal finite row enumeration is
missing, so the status is `PARK-ENUM`. `square`

## 100. Maximal Same-Record Print Of \(\mathcal D_{99}^{row}\)

Section 99 identified the next task as printing
\(\mathcal D_{99}^{row}\) for \(\mathfrak P_{99}^{min}\).  This section
does that print at the strongest level licensed by the current corpus.  The
answer is deliberately split into two parts:

1. a literal subpackage that is actually printed;
2. a carried row-map obstruction for the parts not printed in Papers 10--14
   or Paper 20.

This is not a stylistic caution.  A row package is executable only if its
source and target vertices, support increments, raw coefficients, inverse
slots, and dispositions are all finite same-record data.  The compact-group
Schwinger-Dyson identity by itself is not yet such a table; it is the identity
source from which a table would have to be projected.

### Source Audit 100.1: What The Previous Papers Actually Supply

The relevant source status is:

| source | supplied fact | not supplied |
| --- | --- | --- |
| Paper 14, Theorem 10.2 | exact finite compact-group Schwinger-Dyson identity | reduced `SEL2` row map \(R_{SD}^{99}\) |
| Paper 14, Definition 12.1 | projected SD ledger as a finite-battery construction | literal \(\Xi_{SD}^{99}\), targets, increments, coefficients |
| Paper 20, `P20-SEL2-ACTROW` ledger | the active scalar row and finite ledgers are named | the Section-92 reduced table entries |
| Paper 10 | fixed finite-battery/projective semantics | all-depth reduced row enumeration |
| Paper 11 | conditional finite-battery RG mechanisms | the active `SEL2` tree-rate or reduced KP source |
| Paper 21, Section 98 | finite constructors for `SD`, `act`, `fus`, `cmp` | literal row maps except the representation multiplicity subslot |

Therefore a full numerical \(\mathcal D_{99}^{row}\) is not currently a
consequence of the corpus.  What can be printed is the following maximal
same-record package.

### Definition 100.2: The Printed Vertex Skeleton

For \(\mathfrak P_{99}^{min}\), the vertex skeleton is

```math
\overline V_{99}^{skel}
:=
\left\{
(T,\mu,\ell,h,p,\sigma):
T\in\mathfrak T_{red}^{act},\
\mu\in\{0,{1\over2},1\},\
\ell\in\mathfrak L_{red}^{act},\
0\le h\le h_*^{act},\
0\le p\le p_*^{act},\
\sigma\in\Sigma_*^{act}
\right\}/\!\sim_{phys}.
```

This is a finite same-record skeleton.  It is not yet the literal vertex list
\(\overline V_{99}\), because the current paper has not printed the finite
lists

```math
\mathfrak T_{red}^{act},\qquad
\mathfrak L_{red}^{act},\qquad
\Sigma_*^{act},
```

or the quotient representatives for \(\sim_{phys}\) at this probe.

### Definition 100.3: Literal Fusion Multiplicity Subpackage

The representation part is literal.  In `SU(2)` spin notation,

```math
\Xi_{fus}^{99,lit}
=
\{
(0,0,0,1),\
(0,{1\over2},{1\over2},1),\
(0,1,1,1),
```

```math
({1\over2},0,{1\over2},1),\
({1\over2},{1\over2},0,1),\
({1\over2},{1\over2},1,1),\
({1\over2},1,{1\over2},1),
```

```math
(1,0,1,1),\
(1,{1\over2},{1\over2},1),\
(1,1,0,1),\
(1,1,1,1)
\}.
```

For every \((\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit}\),

```math
N_{\mu,\lambda}^{\mu'}=1.
```

Hence the printed coefficient subslot is

```math
a_{fus}^{99,lit}(e)
=
B_{fus,s}(e)B_{fus,t}(e),
```

and on the strict full-law normal-form convention with no source or target
insertion cost,

```math
a_{fus}^{99,lit}(e)=1.
```

Define the literal fusion subpackage by

```math
\mathcal D_{99}^{fus,lit}
:=
\left(
\Xi_{fus}^{99,lit},
\{N_{\mu,\lambda}^{\mu'}=1\}_{(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit}},
a_{fus}^{99,lit}
\right).
```

The omitted representation products are exactly

```math
({1\over2},1,{3\over2}),\qquad
(1,{1\over2},{3\over2}),\qquad
(1,1,2),
```

and they belong to the representation-tail ledger, not to the retained pass
graph at cutoff \(\Lambda_*^{99}\).

### Definition 100.4: Unprinted Row-Map Subpackage

The remaining row-map data required by Definition 99.6 are the following
finite but unprinted objects:

```math
\mathcal U_{99}^{rowmap}
:=
\left(
\overline V_{99}^{lit},
\Xi_{SD}^{99,lit},\Xi_{act}^{99,lit},\Xi_{cmp}^{99,lit},
R_{SD}^{99},R_{act}^{99},R_{fus}^{99},R_{cmp}^{99},
a_{SD,raw}^{99},a_{act,raw}^{99},a_{cmp,raw}^{99},
\mathcal O_{SD}^{99},\mathcal O_{act}^{99},\mathcal O_{fus}^{99},
\mathcal O_{cmp}^{99},
\mathsf z_{SD/act/cmp}^{99},\mathsf c_{SD/act/cmp}^{99}
\right).
```

The current corpus supplies finite constructors for these entries but does not
print their literal values.  In particular:

1. \(R_{SD}^{99}\) would require the projected compact-group SD/Casimir rows
   after `BTQ/ACTFULLLAW` contraction.
2. \(R_{act}^{99}\) would require the local Wilson/heat-kernel action-stencil
   rows and product rows at \(D_{prod}^{act}=2\).
3. \(R_{cmp}^{99}\) would require the common \(E_{14}/X_{13}\) comparison
   seed table after the exact-entry residual assignments.
4. \(R_{fus}^{99}\) is not fixed by the Clebsch-Gordan multiplicities alone:
   the multiplicities give coefficients, but not the reduced target vertex,
   support increment, shell inverse slot, or disposition.

### Definition 100.5: The Only Fully Executable Current Completion

Because \(\mathcal U_{99}^{rowmap}\) is not printed, the only fully
executable row package licensed by the present corpus is the carried
completion

```math
\mathcal D_{99}^{row,car}
:=
\left(
\overline V_{99}^{skel},
\Xi_{fus}^{99,lit},
\mathcal U_{99}^{rowmap},
\mathsf z_{fus}^{99,lit},
\mathsf c_{99}^{car}
\right),
```

where

```math
\mathsf z_{fus}^{99,lit}
:=
\{N_{\mu,\lambda}^{\mu'}=1:
(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit}\}
```

and \(\mathsf c_{99}^{car}\) assigns every row whose target, increment,
inverse slot, or disposition depends on \(\mathcal U_{99}^{rowmap}\) to the
single named residual

```math
U_{rowmap}^{99}
:=
U_{SD,row}^{99}
+U_{act,row}^{99}
+U_{fus,rowmap}^{99}
+U_{cmp,row}^{99}.
```

Equivalently, the retained pass graph of this carried completion is empty:

```math
\overline E_{pass}^{99,car}=\varnothing.
```

This makes no illicit spending.  It also proves no reduced-tail pass.  If a
numeric convention is needed for the empty pass graph, set

```math
A_{esc}^{99,car}=1,\qquad C_{geom}^{99,car}=1,\qquad g_q^{99,car}=0,
```

but the real worksheet still carries \(U_{rowmap}^{99}\).  Thus the empty
graph does not delete \(E_{14}/X_{13}\); it merely records that the missing
row maps have not been converted into pass edges.

### Theorem 100.6: Full Literal \(\mathcal D_{99}^{row}\) Is Not Printed By The Current Corpus

The maximal current print of \(\mathcal D_{99}^{row}\) is exactly:

```math
\mathcal D_{99}^{row}
=
\mathcal D_{99}^{fus,lit}
\quad\text{plus the carried row-map obstruction}\quad
\mathcal U_{99}^{rowmap}.
```

The following facts are certified:

```math
|\Xi_{fus}^{99,lit}|=11,
\qquad
N_{\mu,\lambda}^{\mu'}=1
\quad((\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit}),
```

```math
g_{bat}^{99}=0
\quad\text{on the full-law branch}.
```

The following facts are not certified:

```math
\overline V_{99}^{lit},\quad
\Xi_{SD}^{99,lit},\quad
\Xi_{act}^{99,lit},\quad
\Xi_{cmp}^{99,lit},
```

```math
R_{SD}^{99},\quad R_{act}^{99},\quad R_{fus}^{99},\quad R_{cmp}^{99},
```

```math
\Delta_X,\quad a_{raw},\quad \mathcal O_{raw},
\quad\mathsf r(e)
```

row by row.

Consequently Algorithm 97.6 still cannot run SCC/coverage on a nonempty pass
graph, and `P21-RED-1KP` still has no edge set on which to be fitted.  The
precise current status is therefore the refined park

```math
\boxed{\mathrm{PARK\text{-}ROWMAP}\subset\mathrm{PARK\text{-}ENUM}.}
```

Proof.

The literal fusion list follows from the `SU(2)` Clebsch-Gordan rule and the
cutoff \(\Lambda_*^{99}=\{0,1/2,1\}\).  Paper 14 proves the compact-group
Schwinger-Dyson identity and defines a projected ledger, but it does not
print the reduced Section-92 `SD` row maps.  Paper 20 freezes the active
`SEL2` scalar row and several scalar coefficient ledgers, but it does not
print the finite reduced edge table \(\overline V_{99}\times\Xi_c\to
\overline V_{99}\).  Sections 92, 97, and 98 of this paper give finite
constructors, not literal row values.  Therefore the only executable current
completion is the carried completion of Definition 100.5.  Any nonempty pass
graph would require at least one currently unprinted target/increment row
value, so it would be an assumption rather than a printed datum. `square`

### Corollary 100.7: Next Required Literal Print

The next task is no longer the broad instruction "print
\(\mathcal D_{99}^{row}\)".  It is the narrower finite list

```math
\overline V_{99}^{lit},\quad
\Xi_{SD}^{99,lit},\quad
\Xi_{act}^{99,lit},\quad
\Xi_{cmp}^{99,lit},
```

followed by the row-map table

```math
R_c^{99}(\bar v,\xi)
=
(\bar v',\Delta_X,\Delta_C,\Delta_h,\Delta_p,a_{raw},\mathcal O_{raw}),
\qquad
c\in\{SD,act,fus,cmp\}.
```

Only after that literal row-map table is present can the paper decide whether
the pass graph is empty, acyclic, coverage-positive, or margin-failing.

## 101. Literal Vertex Representative Print Attempt

Corollary 100.7 asks first for

```math
\overline V_{99}^{lit}.
```

This section tries to print it.  The result is sharper than Section 100: the
current corpus does not yet print the vertex representatives themselves.  It
prints a canonical representative schema and identifies the exact finite lists
whose absence prevents a literal enumeration.

### Definition 101.1: Vertex Data Required For Literal Printing

For \(\mathfrak P_{99}^{min}\), a literal vertex representative is a chosen
canonical representative of an equivalence class

```math
[(T,\mu,\ell,h,p,\sigma)]_{\sim_{phys}}
```

with

```math
\mu\in\{0,{1\over2},1\}.
```

To print the finite list one must supply the four finite data:

```math
\mathfrak T_{99}^{lit}:=\mathfrak T_{red}^{act},
\qquad
\mathfrak L_{99}^{lit}:=\mathfrak L_{red}^{act},
```

```math
\Sigma_{99}^{lit}:=\Sigma_*^{act},
\qquad
\operatorname{Can}_{99}^{phys}:
\mathfrak T_{99}^{lit}\times\{0,{1\over2},1\}
\times\mathfrak L_{99}^{lit}
\times\{0,\ldots,h_*^{act}\}
\times\{0,\ldots,p_*^{act}\}
\times\Sigma_{99}^{lit}
\to
\overline V_{99}^{lit}.
```

Here \(\operatorname{Can}_{99}^{phys}\) must choose one representative after
lower-shell deletion, declared lattice/reflection symmetries, paired-real
normalization, centrality, and the active quotient of Definition 84.1.  It is
not allowed to identify two records whose scalar readouts differ on the same
pushed-forward `SEL2` law.

### Source Audit 101.2: Why The Five Template Classes Are Not A Vertex List

Definition 84.1 and Lemma 84.2 print a finite grammar for active
bounded-collar stagnant/channel templates:

```math
T_{\rm pow},\quad T_{\rm ord},\quad T_{\rm prod},\quad
T_{\rm chan},\quad T_{\rm mix}.
```

These are grammar classes, not the literal reduced vertex list.  A vertex of
Definition 92.1 also records:

1. the active reduced template representative \(T\);
2. the representation channel \(\mu\);
3. the rooted local frontier type \(\ell\);
4. the finite labels \(h,p,\sigma\);
5. the physical quotient representative.

Thus replacing \(\mathfrak T_{red}^{act}\) by the five class names above
would collapse physically distinct active records and would violate the
no-smuggling rule of Definition 96.2.

### Definition 101.3: The Maximal Canonical Representative Schema

The strongest vertex print currently licensed is the schema

```math
\overline V_{99}^{can}
:=
\operatorname{im}\operatorname{Can}_{99}^{phys}
```

where

```math
\operatorname{Can}_{99}^{phys}
(T,\mu,\ell,h,p,\sigma)
:=
\min_{\preceq_{99}}
\left[
(T,\mu,\ell,h,p,\sigma)
\right]_{\sim_{phys}}
```

for any fixed total order \(\preceq_{99}\) on the finite raw tuple set.
The order \(\preceq_{99}\) is purely a representative-selection device; it
does not add an equivalence and does not erase a scalar record.

Equivalently,

```math
\overline V_{99}^{can}
=
\left\{
\operatorname{Can}_{99}^{phys}(T,\mu,\ell,h,p,\sigma):
T\in\mathfrak T_{red}^{act},\
\mu\in\{0,{1\over2},1\},\
\ell\in\mathfrak L_{red}^{act},\
0\le h\le h_*^{act},\
0\le p\le p_*^{act},\
\sigma\in\Sigma_*^{act}
\right\}.
```

This is finite and executable once the three finite source lists and the
quotient representative map are supplied.  It is not a literal enumeration
until those lists are printed.

### Definition 101.4: Vertex-Print Obstruction

Define the vertex obstruction package

```math
\mathcal U_{99}^{vert}
:=
\left(
\mathfrak T_{red}^{act},
\mathfrak L_{red}^{act},
\Sigma_*^{act},
h_*^{act},
p_*^{act},
\operatorname{Can}_{99}^{phys}
\right).
```

The current source corpus proves that \(\mathcal U_{99}^{vert}\) is finite,
but it does not print its values.  Therefore

```math
\overline V_{99}^{lit}
```

is not presently available as a literal finite list.

### Theorem 101.5: Literal Vertex Representatives Are Not Yet Printed

The current corpus licenses the finite representative schema
\(\overline V_{99}^{can}\), but it does not print
\(\overline V_{99}^{lit}\).

The exact current obstruction is

```math
\boxed{\mathrm{PARK\text{-}VERT}}.
```

More explicitly:

```math
\overline V_{99}^{lit}
\text{ is printable from the corpus}
```

if and only if the finite package \(\mathcal U_{99}^{vert}\) is printed.

Proof.

Definition 92.1 defines vertices as tuples modulo \(\sim_{phys}\).  Definition
84.1 proves the active physical quotient is finite, and Sections 75 and 85
justify the `BTQ/ACTFULLLAW` contraction.  But no section prints the actual
lists \(\mathfrak T_{red}^{act}\), \(\mathfrak L_{red}^{act}\), or
\(\Sigma_*^{act}\), nor a canonical representative table for
\(\sim_{phys}\) on the probe.  Lemma 84.2 gives only a grammar of template
classes, not the individual representatives needed by Definition 92.1.  Hence
\(\overline V_{99}^{can}\) is the maximal same-record schema, while
\(\overline V_{99}^{lit}\) remains unprinted. `square`

### Corollary 101.6: The Next Finite Print Is Now Unambiguous

The next task is to print the finite package

```math
\mathcal U_{99}^{vert}
=
\left(
\mathfrak T_{red}^{act},
\mathfrak L_{red}^{act},
\Sigma_*^{act},
h_*^{act},
p_*^{act},
\operatorname{Can}_{99}^{phys}
\right).
```

Once that is printed, the literal vertex list is

```math
\overline V_{99}^{lit}
=
\overline V_{99}^{can},
```

and only then can the paper honestly print \(R_{fus}^{99}\),
\(R_{act}^{99}\), \(R_{SD}^{99}\), and \(R_{cmp}^{99}\) row by row.

## 102. Conservative Over-Refined Print Of \(\mathcal U_{99}^{vert}\)

Section 101 shows that the exact minimal quotient list is not printed by the
current corpus.  This section gives the next best rigorous object: a literal
finite **cover** of the vertex representatives.  It is deliberately
over-refined.  It may split physically equivalent vertices, which can only
increase later finite constants; it never identifies two scalar records whose
readouts differ on the same pushed-forward law.

Thus the cover is safe for an upper-bound/pass-graph audit.  A later exact
quotient table may sharpen it.

### Definition 102.1: Numerical Collar Data For \(\mathfrak P_{99}^{min}\)

For \(\mathfrak P_{99}^{min}\), \(N=2\) and \(r_A=1\).  Hence Definition
75.1 gives

```math
R_{BTQ}^{61}=2r_A+2=4.
```

Using the rectangular collar bound of Definition 75.1,

```math
n_1=n_2=3+2R_{BTQ}^{61}=11,
\qquad
n_3=n_4=1+2R_{BTQ}^{61}=9.
```

The enclosing vertex and positive-link counts are

```math
V_\Box=11^2\,9^2=9801,
```

and

```math
E_\Box^+
=
2\cdot11\cdot10\cdot9^2
+2\cdot11^2\cdot9\cdot8
=35244.
```

Thus the safe tree-gauge cycle count is

```math
m_\Box:=E_\Box^+-V_\Box+1=25444.
```

The actual collar may be smaller.  The over-refined print uses the safe box
value \(m_\Box\).

### Definition 102.2: The Literal Local Word Alphabet

Let

```math
\mathsf H_\Box
:=
\{H_1,H_1^{-1},\ldots,H_{m_\Box},H_{m_\Box}^{-1}\}.
```

For \(N=2\), Definition 75.3 requires reduced trace words of length at most
\(N^2=4\).  Define

```math
\mathsf W_{\le4}^{99}
:=
\{w=w_1\cdots w_\ell:
1\le\ell\le4,\ w_i\in\mathsf H_\Box,\ w
\text{ freely reduced}\}/\!\sim_{cyc,inv},
```

where \(\sim_{cyc,inv}\) is generated by cyclic rotation and the paired-real
identification \(w\sim w^{-1}\).  This is finite and literal.

### Definition 102.3: Over-Refined Active Template List

Define the over-refined active template list

```math
\mathfrak T_{99}^{+}
```

to consist of all tuples

```math
T=
(c,\tau,d,(\lambda_1,w_1),\ldots,(\lambda_d,w_d)),
```

with

```math
c\in\{SD,act,fus,cmp\},
\qquad
\tau\in\{T_{\rm pow},T_{\rm ord},T_{\rm prod},T_{\rm chan},T_{\rm mix},T_{\rm esc}\},
```

```math
0\le d\le D_{prod}^{act}=2,
\qquad
\lambda_i\in\{0,{1\over2},1\},
\qquad
w_i\in\mathsf W_{\le4}^{99}.
```

The extra label \(T_{\rm esc}\) records non-bounded-collar escaping local
rows.  It is not a new row class; it is only a template flag.  The row class
is still \(c\in\{SD,act,fus,cmp\}\).

This list is an over-cover of \(\mathfrak T_{red}^{act}\): every active
template retained by the Section-92 row constructors has a representative in
\(\mathfrak T_{99}^{+}\), but \(\mathfrak T_{99}^{+}\) may contain inactive
formal templates.

### Definition 102.4: Over-Refined Local Frontier List

Let

```math
\mathsf Q_{loc}^{99}:=\{-1,0,1\}^4
```

be the one-action-range coarse cell stencil rooted at \(0\).  Define

```math
\mathfrak L_{99}^{+}
:=
\{L\subseteq\mathsf Q_{loc}^{99}:0\in L,\ L\ne\varnothing\}/\!\sim_{B_4},
```

where \(B_4\) is the finite hypercubic signed-permutation group preserving
the root.  Choose the lexicographically least representative in each
\(B_4\)-orbit.  This is a finite rooted frontier list with

```math
|\mathfrak L_{99}^{+}|\le 2^{80}.
```

The bound is crude but literal.  It is enough for a finite certificate; a
future stencil-specific frontier list may be much smaller.

### Definition 102.5: Over-Refined Symmetry And Label Sets

Use the following finite label sets:

```math
\mathsf H_{99}^{+}
:=
\{\varnothing\}
\cup\Xi_{fus}^{99,lit}
\cup(\Xi_{fus}^{99,lit})^2,
```

so

```math
h_*^{99,+}:=|\mathsf H_{99}^{+}|-1=132.
```

For product/comparison degree, use the active cutoff

```math
p_*^{99,+}:=D_{prod}^{act}=2.
```

Finally define

```math
\Sigma_{99}^{+}
:=
\{\pm1\}_{or}\times\{\pm1\}_{ref}
\times\{\mathrm{paired},\mathrm{unpaired}\}
\times Z(SU(2)),
```

with \(Z(SU(2))=\{\pm I\}\).  Thus

```math
|\Sigma_{99}^{+}|=16.
```

These flags over-record orientation, reflection, paired-real convention, and
center sector.  Over-recording is safe: it may split vertices but cannot
identify distinct scalar records.

### Definition 102.6: The Printed Vertex Cover

Define the over-refined vertex universe

```math
\overline V_{99}^{+}
:=
\left\{
(T,\mu,L,h,p,\sigma):
T\in\mathfrak T_{99}^{+},\
\mu\in\{0,{1\over2},1\},\
L\in\mathfrak L_{99}^{+},\
h\in\mathsf H_{99}^{+},\
0\le p\le2,\
\sigma\in\Sigma_{99}^{+}
\right\}.
```

The conservative vertex representative map is the identity:

```math
\operatorname{Can}_{99}^{+,phys}
(T,\mu,L,h,p,\sigma)
:=
(T,\mu,L,h,p,\sigma).
```

Equivalently, this choice refuses all quotient identifications not already
built into \(\mathsf W_{\le4}^{99}\) and \(\mathfrak L_{99}^{+}\).  It is
therefore a refinement of the physical quotient, not a collapse.

### Theorem 102.7: \(\mathcal U_{99}^{vert}\) Has A Conservative Printed Cover

The package

```math
\mathcal U_{99}^{vert,+}
:=
\left(
\mathfrak T_{99}^{+},
\mathfrak L_{99}^{+},
\Sigma_{99}^{+},
h_*^{99,+}=132,
p_*^{99,+}=2,
\operatorname{Can}_{99}^{+,phys}
\right)
```

is a literal finite over-refined print of the vertex data for
\(\mathfrak P_{99}^{min}\).

It gives the working vertex cover

```math
\overline V_{99}^{lit,+}:=\overline V_{99}^{+}.
```

Every exact vertex of the unprinted minimal list \(\overline V_{99}^{lit}\)
has at least one representative in \(\overline V_{99}^{lit,+}\).  Therefore
the paper may use \(\overline V_{99}^{lit,+}\) for conservative finite
upper-bound audits.  It may not use it to claim sharp constants.

Proof.

Definitions 75.1--75.3 give a finite collar word alphabet.  For \(N=2\) the
trace-word length bound is \(4\), so \(\mathsf W_{\le4}^{99}\) is finite.
Lemma 84.2 gives the five active stagnant/channel grammar classes, and
Definition 89.1 gives the four reduced row classes.  Definition 102.3 forms
the finite product of these finite labels with the cutoff
\(\Lambda_*^{99}\) and \(D_{prod}^{act}=2\).  Definition 102.4 over-covers
all rooted one-action-range frontier shapes by all rooted subsets of
\(\{-1,0,1\}^4\) modulo the hypercubic root stabilizer.  Definition 102.5
over-records the finite channel/product/symmetry labels.

No step identifies two records beyond already declared finite symmetries.
Thus the construction is same-record safe and finite.  Since it includes all
row classes, all five active grammar flags, all retained representation
labels, all degree-\(\le2\) local products, and all rooted local frontier
shapes in the action-range stencil, it covers the minimal vertex list. `square`

### Corollary 102.8: Status After Printing The Vertex Cover

Using the conservative cover, the active finite-table status becomes

```math
\boxed{\mathrm{PARK\text{-}ROWMAP}^{+}}.
```

The superscript means: row maps are now to be printed on the over-refined
vertex cover \(\overline V_{99}^{lit,+}\).  Exact quotient sharpening remains
available later, but it is no longer a blocker for beginning the row-map
print.

The next row-map task is therefore:

```math
R_{fus}^{99,+}:
\overline V_{99}^{lit,+}\times\Xi_{fus}^{99,lit}
\dashrightarrow
\overline V_{99}^{lit,+}\times
\mathbb N\times\mathbb Z^3\times[0,\infty)^2.
```

## 103. Printing \(R_{fus}^{99,+}\) Row By Row

This section executes the first row-map print promised by Corollary 102.8.
The point is deliberately modest: it prints the retained `SU(2)` fusion rows
on the over-refined cover.  It does not infer the `SD`, `act`, or `cmp` rows.

### Definition 103.1: Fusion Coordinates On The Over-Refined Cover

Write a vertex of the printed cover as

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in\overline V_{99}^{lit,+},
```

where \(\alpha\in\Lambda_*^{99}=\{0,{1\over2},1\}\) is the active retained
representation/channel label.  Write a retained fusion index as

```math
\xi=(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit}.
```

The row is compatible with \(\bar v\) only when

```math
\alpha=\mu.
```

The finite channel-history label set from Definition 102.5 is used as a
two-step sliding record.  Define

```math
\ell(\varnothing)=0,\qquad
\ell(\eta)=1\quad(\eta\in\Xi_{fus}^{99,lit}),
\qquad
\ell((\eta_1,\eta_2))=2,
```

and

```math
\operatorname{Push}_{fus}^{99,+}(h,\xi)
:=
\begin{cases}
\xi,&h=\varnothing,\\
(h,\xi),&h\in\Xi_{fus}^{99,lit},\\
(\eta_2,\xi),&h=(\eta_1,\eta_2)\in(\Xi_{fus}^{99,lit})^2.
\end{cases}
```

The corresponding channel-complexity increment is

```math
\Delta_h^{fus}(h,\xi)
:=
\ell(\operatorname{Push}_{fus}^{99,+}(h,\xi))-\ell(h)
\in\{0,1\}.
```

This sliding update is not a scalar-record quotient.  The active scalar
record and the next fusion availability depend only on the current channel
\(\alpha\) and the retained index \(\xi\); the \(h\)-slot is a finite ledger
coordinate for row accounting.  Keeping the last two fusion indices
over-records enough information for the printed row certificate and never
identifies two different scalar observables.

For the Casimir bookkeeping coordinate, use the finite order index

```math
\iota_C(0)=0,\qquad
\iota_C({1\over2})=1,\qquad
\iota_C(1)=2.
```

Thus the `fus` Casimir-coordinate increment is

```math
\Delta_C^{fus}(\alpha,\mu')
:=
\iota_C(\mu')-\iota_C(\alpha).
```

This integer coordinate is only the finite row-weight coordinate.  The actual
`SU(2)` Casimir values remain \(C_2(j)=j(j+1)\) when a Casimir estimate is
needed.

### Definition 103.2: The Eleven Retained Fusion Rows

The retained row list is exactly the literal subpackage
\(\Xi_{fus}^{99,lit}\) from Definition 100.3.  Written as source channel,
inserted channel, and target channel, the rows are:

| row | compatible source \(\alpha\) | inserted \(\lambda\) | target \(\alpha'=\mu'\) | multiplicity |
| --- | --- | --- | --- | --- |
| \(F_1\) | \(0\) | \(0\) | \(0\) | \(1\) |
| \(F_2\) | \(0\) | \(1/2\) | \(1/2\) | \(1\) |
| \(F_3\) | \(0\) | \(1\) | \(1\) | \(1\) |
| \(F_4\) | \(1/2\) | \(0\) | \(1/2\) | \(1\) |
| \(F_5\) | \(1/2\) | \(1/2\) | \(0\) | \(1\) |
| \(F_6\) | \(1/2\) | \(1/2\) | \(1\) | \(1\) |
| \(F_7\) | \(1/2\) | \(1\) | \(1/2\) | \(1\) |
| \(F_8\) | \(1\) | \(0\) | \(1\) | \(1\) |
| \(F_9\) | \(1\) | \(1/2\) | \(1/2\) | \(1\) |
| \(F_{10}\) | \(1\) | \(1\) | \(0\) | \(1\) |
| \(F_{11}\) | \(1\) | \(1\) | \(1\) | \(1\) |

Equivalently, for every source vertex \(\bar v=(T,\alpha,L,h,p,\sigma)\),
the defined retained `fus` rows are precisely the rows in this table whose
first column equals \(\alpha\).

The omitted products

```math
{1\over2}\otimes1\supset{3\over2},
\qquad
1\otimes{1\over2}\supset{3\over2},
\qquad
1\otimes1\supset2
```

are not rows of \(R_{fus}^{99,+}\).  They remain in the representation-tail
ledger declared in Definition 100.3.

### Definition 103.3: The Printed Row Map \(R_{fus}^{99,+}\)

Let

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in\overline V_{99}^{lit,+},
\qquad
\xi=(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit}.
```

If \(\alpha\ne\mu\), the row is undefined:

```math
R_{fus}^{99,+}(\bar v,\xi)\ \text{is undefined}.
```

If \(\alpha=\mu\), define

```math
\bar v'
:=
\left(
T,\,
\mu',\,
L,\,
\operatorname{Push}_{fus}^{99,+}(h,\xi),\,
p,\,
\sigma
\right).
```

Then

```math
R_{fus}^{99,+}(\bar v,\xi)
:=
\left(
\bar v',
\Delta_X,
\Delta_C,
\Delta_h,
\Delta_p,
a,
\mathcal O
\right),
```

where

```math
\Delta_X:=0,
\qquad
\Delta_C:=\Delta_C^{fus}(\alpha,\mu'),
\qquad
\Delta_h:=\Delta_h^{fus}(h,\xi),
\qquad
\Delta_p:=0,
```

and, on the strict exact scalar-record convention,

```math
a:=1,
\qquad
\mathcal O:=0.
```

If a later branch reintroduces source or target normal-form insertion costs,
replace \(a=1\) by

```math
a=B_{fus,s}^{99,+}(\bar v,\xi)B_{fus,t}^{99,+}(\bar v,\xi),
```

but the strict branch printed here has
\(B_{fus,s}^{99,+}=B_{fus,t}^{99,+}=1\).  The multiplicity factor is always
one for the retained `SU(2)` rows in Definition 103.2.

### Table 103.4: Row-By-Row Output

For any fixed

```math
\bar v=(T,\alpha,L,h,p,\sigma),
```

the printed outputs are:

| row | condition on \(\alpha\) | target vertex \(\bar v'\) | \((\Delta_X,\Delta_C,\Delta_h,\Delta_p)\) | \((a,\mathcal O)\) | disposition |
| --- | --- | --- | --- | --- | --- |
| \(F_1=(0,0,0,1)\) | \(\alpha=0\) | \((T,0,L,\operatorname{Push}(h,F_1),p,\sigma)\) | \((0,0,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_2=(0,{1\over2},{1\over2},1)\) | \(\alpha=0\) | \((T,{1\over2},L,\operatorname{Push}(h,F_2),p,\sigma)\) | \((0,1,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_3=(0,1,1,1)\) | \(\alpha=0\) | \((T,1,L,\operatorname{Push}(h,F_3),p,\sigma)\) | \((0,2,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_4=({1\over2},0,{1\over2},1)\) | \(\alpha={1\over2}\) | \((T,{1\over2},L,\operatorname{Push}(h,F_4),p,\sigma)\) | \((0,0,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_5=({1\over2},{1\over2},0,1)\) | \(\alpha={1\over2}\) | \((T,0,L,\operatorname{Push}(h,F_5),p,\sigma)\) | \((0,-1,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_6=({1\over2},{1\over2},1,1)\) | \(\alpha={1\over2}\) | \((T,1,L,\operatorname{Push}(h,F_6),p,\sigma)\) | \((0,1,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_7=({1\over2},1,{1\over2},1)\) | \(\alpha={1\over2}\) | \((T,{1\over2},L,\operatorname{Push}(h,F_7),p,\sigma)\) | \((0,0,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_8=(1,0,1,1)\) | \(\alpha=1\) | \((T,1,L,\operatorname{Push}(h,F_8),p,\sigma)\) | \((0,0,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_9=(1,{1\over2},{1\over2},1)\) | \(\alpha=1\) | \((T,{1\over2},L,\operatorname{Push}(h,F_9),p,\sigma)\) | \((0,-1,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_{10}=(1,1,0,1)\) | \(\alpha=1\) | \((T,0,L,\operatorname{Push}(h,F_{10}),p,\sigma)\) | \((0,-2,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |
| \(F_{11}=(1,1,1,1)\) | \(\alpha=1\) | \((T,1,L,\operatorname{Push}(h,F_{11}),p,\sigma)\) | \((0,0,\Delta_h,0)\) | \((1,0)\) | `CMSSI` |

Here \(\operatorname{Push}\) abbreviates
\(\operatorname{Push}_{fus}^{99,+}\), and
\(\Delta_h=\Delta_h^{fus}(h,F_i)\).  Rows whose condition on \(\alpha\) fails
are undefined, not zero-coefficient rows; the corresponding tensor channel is
simply not available at that source vertex.

### Lemma 103.5: Same-Record Legality And No Double Charge

Every defined row of \(R_{fus}^{99,+}\) is a same-record finite
Clebsch-Gordan channel row.  It changes only the active retained
representation label and the finite channel-history ledger.  It does not
change the local frontier, product degree, orientation/reflection convention,
center sector, or support polymer.

Consequently,

```math
\Delta_X=0,\qquad
\Delta_p=0,
```

for every defined row.  The row is not a Paper-16 projective/covariance
transport row, not an \(RPF\) exact-entry row, not a `KPdec` decoration row,
and not a comparison-battery row.

Proof.

The table is exactly the retained `SU(2)` tensor-product table of Definition
100.3, with unit multiplicities.  Tensoring a retained representation channel
with a retained local channel and projecting onto a retained summand is a
finite algebraic operation inside the same scalar pushed-forward law.  It
does not move the support set \(L\), does not add a local action stencil, and
does not change any endpoint, decoration, comparison, projective, or
whole-process datum.  The only changed scalar coordinate is the retained
channel label \(\alpha\), and the only changed ledger coordinate is \(h\).
Thus none of the previously parked debits is charged again. `square`

### Corollary 103.6: Fusion Rows Are Printed And Repaired

The retained fusion row map is now printed:

```math
\boxed{
R_{fus}^{99,+}\ \text{is the row map of Definition 103.3 and Table 103.4}.
}
```

All defined retained fusion rows are zero-support rows:

```math
\mathcal E_{fus,pass}^{99,+}=\varnothing,
\qquad
\mathcal E_{fus,0}^{99,+}
=
\{(\bar v,R_{fus}^{99,+}(\bar v,\xi)):
\bar v\in\overline V_{99}^{lit,+},\
\xi\in\Xi_{fus}^{99,lit},\
\alpha(\bar v)=\mu(\xi)\}.
```

On the strict exact scalar-record branch, they are assigned to the
same-shell channel/`CMSSI` ledger.  Hence they contribute no reduced escaping
pass edge and no coefficient growth to \(A_{esc}^{BTQ}\):

```math
C_{fus,pass}^{99,+}=0,
\qquad
A_{fus,pass}^{99,+}=1.
```

If a later audit elects to keep these zero-growth channel rows inside the
directed graph instead of assigning them to `CMSSI`, then the printed table
still applies, but the zero-growth SCC test of Section 90 must be rerun with
the fusion-only cycles included.  No such rerun is needed on the strict branch.

The active status therefore sharpens from
\(\mathrm{PARK\text{-}ROWMAP}^{+}\) to

```math
\boxed{\mathrm{PARK\text{-}ROWMAP}^{+}_{SD,act,cmp}}.
```

The next unprinted maps are \(R_{SD}^{99,+}\), \(R_{act}^{99,+}\), and
\(R_{cmp}^{99,+}\).  Among these, \(R_{act}^{99,+}\) is the most important
because it decides whether support-growing rows actually earn reduced
analytic decay.

## 104. Printing The Structural Action Row Map \(R_{act}^{99,+}\)

This section prints the action/product row map on the same over-refined
vertex cover.  The print is intentionally split into two pieces:

1. the target, support, channel, and degree update, which are finite
   combinatorics and are printed here; and
2. the local-action coefficient and same-shell inverse entries, which are
   finite source data from the active local action ledger and remain parked
   unless supplied as an explicit table.

This split is necessary.  Papers 11--12 and Sections 97--100 of this paper
license a finite local action-stencil/product constructor, but they do not
print the numeric coefficient table for the active `SEL2` law.  Therefore the
paper may print \(R_{act}^{99,+}\) structurally, but it may not yet count
support-growing action rows as certified pass rows unless their finite
coefficient and admissibility entries are supplied.

### Definition 104.1: Over-Refined Action Atoms

Let

```math
\mathsf Q_{loc}^{99}=\{-1,0,1\}^4
```

be the rooted one-action-range stencil of Definition 102.4.  Define the
over-refined action-support list

```math
\mathsf S_{act}^{99,+}
:=
\{S\subseteq\mathsf Q_{loc}^{99}:S\ne\varnothing,\ S\cap L\ne\varnothing
\text{ for some }L\in\mathfrak L_{99}^{+}\}.
```

Equivalently, \(\mathsf S_{act}^{99,+}\) is the finite list of local action
supports that can touch at least one rooted frontier representative.  It is
an over-cover: a later stencil-specific audit may delete inactive supports.

An over-refined action atom is a tuple

```math
\zeta=(\kappa,S,w,\lambda,\upsilon)
```

with

```math
\kappa\in\{\mathrm{plaq},\mathrm{stencil},\mathrm{prod}\},
\qquad
S\in\mathsf S_{act}^{99,+},
\qquad
w\in\mathsf W_{\le4}^{99},
```

```math
\lambda\in\Lambda_*^{99}=\{0,{1\over2},1\},
\qquad
\upsilon\in\Sigma_{99}^{+}.
```

Write

```math
\lambda(\zeta):=\lambda,\qquad
w(\zeta):=w,\qquad
S(\zeta):=S.
```

The finite action-atom list is

```math
\mathsf A_{act}^{99,+}
:=
\{\zeta=(\kappa,S,w,\lambda,\upsilon)\text{ as above}\}.
```

For each atom, introduce two finite value slots:

```math
c_{act}^{99,+}(\zeta),
\qquad
a_{act,raw}^{99,+}(\zeta,\chi),
\qquad
\mathcal O_{act}^{99,+}(\zeta,\chi),
```

where \(c_{act}^{99,+}(\zeta)\) is the raw local-action/product coefficient
\(a_{act,raw}^{99,+}(\zeta,\chi)\) is the channel-projected raw row
coefficient after applying the retained compact-group/product projection,
and \(\mathcal O_{act}^{99,+}(\zeta,\chi)\) is the same-shell inverse
off-diagonal slot after the retained channel projection \(\chi\).  These are
not assigned numerical values by this section.  A missing entry is denoted
\(\star\) and forces the row into the carried action-value ledger.

### Definition 104.2: The Printed Action Index Set

The over-refined retained action index set is

```math
\Xi_{act}^{99,+}
:=
\left\{
(\zeta,\chi):
\zeta\in\mathsf A_{act}^{99,+},\
\chi=(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit},\
\lambda=\lambda(\zeta)
\right\}.
```

Thus an action row consists of a local action atom together with a retained
`SU(2)` channel projection.  The omitted channel projections

```math
{1\over2}\otimes1\supset{3\over2},
\qquad
1\otimes{1\over2}\supset{3\over2},
\qquad
1\otimes1\supset2
```

are not retained action rows.  They remain in the representation-tail ledger,
exactly as in Definition 100.3.

### Definition 104.3: Frontier And Template Updates

Let \(L\in\mathfrak L_{99}^{+}\) be represented by its chosen rooted subset of
\(\mathsf Q_{loc}^{99}\).  For an action atom \(\zeta\), define the raw
frontier union

```math
L^\sharp(L,\zeta):=L\cup S(\zeta),
```

and the support increment

```math
\Delta_X^{act}(L,\zeta):=|L^\sharp(L,\zeta)\setminus L|.
```

Let

```math
\operatorname{Can}_{L}^{99,+}(L^\sharp)
```

be the lexicographically least \(B_4\)-representative of \(L^\sharp\) in
\(\mathfrak L_{99}^{+}\).  Set

```math
L':=\operatorname{Can}_{L}^{99,+}(L^\sharp(L,\zeta)).
```

For templates, write

```math
T=(c,\tau,d,(\lambda_1,w_1),\ldots,(\lambda_d,w_d)).
```

If \(p=2\), the action/product update exceeds the active product cutoff and
is not a retained row.  If \(p\le1\), define the appended product list

```math
\operatorname{Append}_{\le2}
\bigl(
((\lambda_1,w_1),\ldots,(\lambda_d,w_d)),
(\lambda(\zeta),w(\zeta))
\bigr)
```

to be the last at most two entries after appending
\((\lambda(\zeta),w(\zeta))\).  Let its length be \(d'\le2\).  Define

```math
\tau_{act}^{99,+}(L,\zeta)
:=
\begin{cases}
T_{\rm esc},&\Delta_X^{act}(L,\zeta)\ge1,\\
T_{\rm prod},&\Delta_X^{act}(L,\zeta)=0.
\end{cases}
```

Then the target action template is

```math
\operatorname{ActTpl}_{99}^{+}(T,L,\zeta)
:=
\left(
act,\,
\tau_{act}^{99,+}(L,\zeta),\,
d',\,
\operatorname{Append}_{\le2}(\cdots)
\right)
\in\mathfrak T_{99}^{+}.
```

This is again an over-refined update.  It records a support-growing local
action/product row as \(T_{\rm esc}\) and a non-support-growing retained
local action/product row as \(T_{\rm prod}\).  More delicate distinctions
among plaquette, improved-stencil, and product rows remain in the atom
\(\zeta\) and its coefficient slot.

### Definition 104.4: The Structural Row Map \(R_{act}^{99,+}\)

Let

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in\overline V_{99}^{lit,+},
\qquad
\xi=(\zeta,\chi)\in\Xi_{act}^{99,+},
```

with

```math
\chi=(\mu,\lambda,\mu',1).
```

If \(\alpha\ne\mu\), the row is undefined:

```math
R_{act}^{99,+}(\bar v,\xi)\ \text{is undefined}.
```

If \(p=2\), the retained row map is undefined and the attempted row is sent to
the product-tail ledger.  This is the disposition `act-tail`, not a
zero-coefficient identity.

If \(\alpha=\mu\) and \(p\le1\), define

```math
T':=\operatorname{ActTpl}_{99}^{+}(T,L,\zeta),
\qquad
L':=\operatorname{Can}_{L}^{99,+}(L\cup S(\zeta)),
```

```math
h':=\operatorname{Push}_{fus}^{99,+}(h,\chi),
\qquad
p':=p+1,
\qquad
\sigma':=\sigma.
```

Set

```math
\bar v'
:=
(T',\mu',L',h',p',\sigma').
```

Then the structural action row map is

```math
R_{act}^{99,+}(\bar v,\xi)
:=
\left(
\bar v',
\Delta_X,
\Delta_C,
\Delta_h,
\Delta_p,
a,
\mathcal O
\right),
```

where

```math
\Delta_X:=\Delta_X^{act}(L,\zeta),
\qquad
\Delta_C:=\Delta_C^{fus}(\alpha,\mu'),
\qquad
\Delta_h:=\Delta_h^{fus}(h,\chi),
\qquad
\Delta_p:=1.
```

On the strict no-extra-normal-form convention, the coefficient and
off-diagonal slots are

```math
a:=a_{act,raw}^{99,+}(\zeta,\chi),
\qquad
\mathcal O:=\mathcal O_{act}^{99,+}(\zeta,\chi).
```

If a source or target `BTQ/ACTFULLLAW` normal form is explicitly inserted,
replace \(a\) by

```math
a
:=
B_{act,s}^{99,+}(\bar v,\xi)
B_{act,t}^{99,+}(\bar v,\xi)
a_{act,raw}^{99,+}(\zeta,\chi).
```

The strict structural print sets \(B_{act,s}^{99,+}=B_{act,t}^{99,+}=1\).

### Table 104.5: Row-By-Row Disposition Rule

For each source vertex \(\bar v=(T,\alpha,L,h,p,\sigma)\) and action index
\(\xi=(\zeta,(\mu,\lambda,\mu',1))\), assign exactly one of the following
rows:

| row family | condition | \(s(e)\to t(e)\) | \(a(e)\) | \(d(e)\) | \(\mathcal O(e)\) | disposition | ledger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `act-undef` | \(\alpha\ne\mu\) | no row | not used | not used | not used | undefined | no tensor channel at source |
| `act-tail` | \(\alpha=\mu,\ p=2\) | removed | product-tail budget | not used | not used | `carry` | \(U_{act,prod}^{99,+}\) |
| `act-zero` | \(\alpha=\mu,\ p\le1,\ a_{act,raw}^{99,+}(\zeta,\chi)=0\) by named same-record identity | \(\bar v\to\bar v'\) | \(0\) | \(0\) | \(0\) | `zero` | exact action cancellation |
| `act-BTQ` | \(\alpha=\mu,\ p\le1,\ \Delta_X=0\), and the row is internal to the declared `BTQ/ACTFULLLAW` state | internal | paid by `BTQ/ACTFULLLAW` | \(0\) | not a reduced row | `BTQ` | bounded-collar state |
| `act-CMSSI` | \(\alpha=\mu,\ p\le1,\ \Delta_X=0\), finite \(a,\mathcal O\), not internal `BTQ` | \(\bar v\to\bar v'\) | \(a\) | \(0\) | \(\mathcal O\) | `CMSSI` | same-shell inverse ledger |
| `act-pass` | \(\alpha=\mu,\ p\le1,\ \Delta_X\ge1\), finite \(a,\mathcal O\), all no-double-charge checks pass | \(\bar v\to\bar v'\) | \(a\) | \(\Delta_X\) | \(\mathcal O\) | `pass` | reduced escaping action row |
| `act-carry` | any remaining compatible retained row, including \(a=\star\), \(\mathcal O=\star\), or failed same-record/no-double-charge check | removed | carried | not used | not used | `carry` | \(U_{act,row}^{99,+}\) |

The row-depth contribution is

```math
d(e):=\Delta_X(e)\mathbf 1_{\{\mathsf r(e)=\mathrm{pass}\}}.
```

Thus action rows are decay-eligible only in the `act-pass` family.

### Lemma 104.6: Same-Record Legality And Debit Separation

Every defined structural row of \(R_{act}^{99,+}\) is evaluated on the same
active pushed-forward `SEL2` scalar law as the source vertex.  The row changes
only:

1. the finite action template \(T\);
2. the retained channel \(\alpha\to\mu'\);
3. the rooted local frontier \(L\to L'\);
4. the finite channel-history ledger \(h\to h'\);
5. the active product degree \(p\to p+1\).

It does not charge perimeter, cusp, readout, Paper-14 export,
projective/covariance transport, \(RPF\), `KPdec`, or whole-process mismatch
debits.

Proof.

The support update uses only \(L\cup S(\zeta)\) inside the fixed finite local
stencil \(\mathsf Q_{loc}^{99}\).  The channel update uses the retained
`SU(2)` Clebsch-Gordan subtable already printed in Definition 100.3 and
Section 103.  The product update stays inside \(D_{prod}^{act}=2\), or else
the row is removed to the product-tail ledger.  All values are read from the
same finite local action ledger \(a_{act,raw}^{99,+}\) and
\(\mathcal O_{act}^{99,+}\) under the active `SEL2` law.  The excluded debits
are exactly the exclusions in Definitions 89.1, 92.3, and 97.3, so no
previously parked debit is spent a second time. `square`

### Corollary 104.7: What The Action Print Closes And What It Does Not Close

The structural action row map is now printed:

```math
\boxed{
R_{act}^{99,+}\ \text{is the row map of Definition 104.4 with dispositions
from Table 104.5}.
}
```

The action pass edge set is the finite set

```math
\mathcal E_{act,pass}^{99,+}
:=
\{(\bar v,R_{act}^{99,+}(\bar v,\xi)):
\mathsf r(\bar v,\xi)=\mathrm{pass}\}.
```

Consequently the action contributions are the finite table functions

```math
C_{act,pass}^{99,+}
:=
\max_{\bar v\in\overline V_{99}^{lit,+}}
\#\{e\in\mathcal E_{act,pass}^{99,+}:s(e)=\bar v\},
```

```math
A_{act,pass}^{99,+}
:=
\max_{e\in\mathcal E_{act,pass}^{99,+}}\max(1,a(e)).
```

If \(\mathcal E_{act,pass}^{99,+}=\varnothing\), use the empty-class values

```math
C_{act,pass}^{99,+}=0,\qquad
A_{act,pass}^{99,+}=1.
```

However, the current corpus still has not supplied the finite value table

```math
\mathcal V_{act}^{99,+}
:=
\{c_{act}^{99,+}(\zeta),K_{act}^{99,+}(\zeta,\chi),
a_{act,raw}^{99,+}(\zeta,\chi),
\mathcal O_{act}^{99,+}(\zeta,\chi),
\mathsf z_{act}^{99,+},\mathsf c_{act}^{99,+}\}.
```

Therefore Section 104 closes the action target/increment map but does not yet
certify a numerical \(A_{act,pass}^{99,+}\), a numerical action CMSSI row
sum, or an action decay-coverage constant.  The active finite-table status is

```math
\boxed{
\mathrm{PARK\text{-}ROWMAP}^{+}_{SD,cmp}
\quad+\quad
\mathrm{PARK\text{-}ACTVAL}^{+}.
}
```

The next profitable finite-table task is to print \(R_{SD}^{99,+}\) or to
supply \(\mathcal V_{act}^{99,+}\).  If the goal is to decide the reduced
decay inequality quickly, \(\mathcal V_{act}^{99,+}\) is more important:
without it, the newly printed support-growing action rows cannot be counted
as certified pass rows.

## 105. The Finite Action-Value Ledger \(\mathcal V_{act}^{99,+}\)

Section 104 printed the structural action row map.  This section prints the
value ledger that must be supplied before any structural action row can be
counted as a certified pass row.  The result is a clean fork:

1. with no additional source table, all compatible nonzero action rows remain
   carried; and
2. with a finite same-record action source table, the action rows are
   evaluated by the formulas below.

No continuum Yang-Mills measure, area law, or off-record stochastic kernel is
used in either branch.

### Definition 105.1: The Action-Value Source Package

An action-value source package for the over-refined probe is a finite tuple

```math
\mathcal S_{act}^{99,+}
:=
\left(
c_{act}^{99,+},
K_{act}^{99,+},
P_{act}^{99,+},
\mathcal O_{act}^{99,+},
\mathsf z_{act}^{99,+},
\mathsf c_{act}^{99,+}
\right).
```

Here:

1. \(c_{act}^{99,+}(\zeta)\in\mathbb R\cup\{\star\}\) is the local
   action/product coefficient of the atom \(\zeta\);
2. \(K_{act}^{99,+}(\zeta,\chi)\in\mathbb R\cup\{\star\}\) is the total
   retained finite projection multiplier for the atom and channel;
3. \(P_{act}^{99,+}(\zeta,\chi)\in[0,\infty)\cup\{\star\}\) is the auxiliary
   product/stencil multiplier used when \(K_{act}^{99,+}\) is sourced through
   the compact-group derivative scalar below;
4. \(\mathcal O_{act}^{99,+}(\zeta,\chi)\in[0,\infty)\cup\{\star\}\) is the
   same-shell inverse off-diagonal slot;
5. \(\mathsf z_{act}^{99,+}\) is the finite list of named same-record exact
   zero identities;
6. \(\mathsf c_{act}^{99,+}\) is the finite list of carried assignments:
   product-tail, representation-tail, missing coefficient, missing inverse
   slot, no-double-charge failure, or non-`SEL2` source.

The symbol \(\star\) means "not supplied by the current source corpus."  It is
not a number and cannot be optimized over.  Any row needing a \(\star\)-entry
is removed from the pass graph and charged to the carried action-value
ledger.

### Definition 105.2: Retained `SU(2)` Channel Projection Scalars

For a retained `SU(2)` fusion channel

```math
\chi=(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit},
```

define the compact-group action-projection scalar

```math
\Gamma_{act}^{99}(\chi)
:=
{1\over2}
\left(
C_2(\mu')-C_2(\mu)-C_2(\lambda)
\right),
\qquad
C_2(j):=j(j+1).
```

For the eleven retained rows this gives:

| row | \((\mu,\lambda,\mu')\) | \(\Gamma_{act}^{99}\) |
| --- | --- | --- |
| \(F_1\) | \((0,0,0)\) | \(0\) |
| \(F_2\) | \((0,{1\over2},{1\over2})\) | \(0\) |
| \(F_3\) | \((0,1,1)\) | \(0\) |
| \(F_4\) | \(({1\over2},0,{1\over2})\) | \(0\) |
| \(F_5\) | \(({1\over2},{1\over2},0)\) | \(-{3\over4}\) |
| \(F_6\) | \(({1\over2},{1\over2},1)\) | \({1\over4}\) |
| \(F_7\) | \(({1\over2},1,{1\over2})\) | \(-1\) |
| \(F_8\) | \((1,0,1)\) | \(0\) |
| \(F_9\) | \((1,{1\over2},{1\over2})\) | \(-1\) |
| \(F_{10}\) | \((1,1,0)\) | \(-2\) |
| \(F_{11}\) | \((1,1,1)\) | \(-1\) |

Thus

```math
\Gamma_{max}^{99}:=
\max_{\chi\in\Xi_{fus}^{99,lit}}
|\Gamma_{act}^{99}(\chi)|
=2.
```

Rows \(F_1,F_2,F_3,F_4,F_8\) have zero compact-group derivative channel
scalar.  They can still appear as neutral bookkeeping/product rows if a
separate product source table says so, but they do not generate a
Schwinger-Dyson action-derivative coefficient through the displayed
contraction.

### Definition 105.3: Channel-Projected Raw Action Coefficient

For derivative action-stencil rows one may source the total projection
multiplier by the rule

```math
K_{act}^{99,+}(\zeta,\chi)
=
\Gamma_{act}^{99}(\chi)P_{act}^{99,+}(\zeta,\chi).
```

For a pure finite product row whose coefficient is not of derivative form,
the source package must instead supply \(K_{act}^{99,+}(\zeta,\chi)\)
directly.  If neither declaration is present, the row is carried.

With this convention, the raw coefficient is

```math
a_{act,raw}^{99,+}(\zeta,\chi)
:=
\begin{cases}
0,&(\zeta,\chi)\in\mathsf z_{act}^{99,+},\\
\left|
c_{act}^{99,+}(\zeta)
K_{act}^{99,+}(\zeta,\chi)
\right|,
&c_{act}^{99,+}(\zeta),K_{act}^{99,+}(\zeta,\chi)
\ne\star,\\
\star,&\text{otherwise}.
\end{cases}
```

The row coefficient used in \(R_{act}^{99,+}\) is then

```math
a(e)
=
B_{act,s}^{99,+}(e)B_{act,t}^{99,+}(e)
a_{act,raw}^{99,+}(\zeta,\chi),
```

with \(B_{act,s}^{99,+}=B_{act,t}^{99,+}=1\) on the strict exact structural
branch.

### Definition 105.4: Action-Value Envelopes

If \(\mathcal S_{act}^{99,+}\) supplies finite coefficient and inverse slots,
define

```math
C_{act,coef}^{99,+}
:=
\max_{\zeta\in\mathsf A_{act}^{99,+}}
|c_{act}^{99,+}(\zeta)|,
```

```math
P_{act,max}^{99,+}
:=
\max_{(\zeta,\chi)\in\Xi_{act}^{99,+}}
P_{act}^{99,+}(\zeta,\chi),
```

```math
K_{act,max}^{99,+}
:=
\max_{(\zeta,\chi)\in\Xi_{act}^{99,+}}
|K_{act}^{99,+}(\zeta,\chi)|,
```

```math
O_{act,max}^{99,+}
:=
\max_{(\zeta,\chi)\in\Xi_{act}^{99,+}}
\mathcal O_{act}^{99,+}(\zeta,\chi).
```

If any displayed maximum contains a \(\star\)-entry, the corresponding
envelope is not certified and the rows using that entry are carried.  When
the envelopes are certified, every strict action row satisfies

```math
a(e)
\le
C_{act,coef}^{99,+}\,
K_{act,max}^{99,+}.
```

On the derivative-sourced subbranch,

```math
K_{act,max}^{99,+}
\le
\Gamma_{max}^{99}P_{act,max}^{99,+}
=2P_{act,max}^{99,+}.
```

Consequently the certified action coefficient base obeys

```math
A_{act,pass}^{99,+}
\le
\max\left(
1,
C_{act,coef}^{99,+}K_{act,max}^{99,+}
\right)
```

on the strict branch, after deleting `BTQ`, `CMSSI`, `zero`, `tail`, and
carried rows.

### Definition 105.5: The Safe Carried Completion

The safe carried completion is the source package

```math
\mathcal S_{act,car}^{99,+}
```

that keeps the exact zero identities already explicitly named, but assigns
every compatible row with an unsupplied coefficient, unsupplied product
multiplier, unsupplied inverse slot, or failed no-double-charge check to

```math
U_{act,row}^{99,+}.
```

Under \(\mathcal S_{act,car}^{99,+}\), the certified action pass graph is
empty:

```math
\mathcal E_{act,pass}^{99,+,car}=\varnothing.
```

Use the empty-class values

```math
C_{act,pass}^{99,+,car}=0,
\qquad
A_{act,pass}^{99,+,car}=1,
\qquad
\Omega_{act}^{99,+,car}(\mathbf a)=0.
```

This does not assert that the physical action rows vanish.  It asserts only
that the current source corpus has not supplied the finite same-record values
needed to spend them on the pass branch.

### Theorem 105.6: Action-Value Source Gate

The action-value source gate

```math
\mathrm{P21\text{-}ACTVAL}^{99,+}
\left(
C_{act,coef}^{99,+},
K_{act,max}^{99,+},
O_{act,max}^{99,+}
\right)
```

holds if and only if all of the following finite data are supplied on the
active pushed-forward `SEL2` scalar law:

1. \(c_{act}^{99,+}(\zeta)\) for every action atom not explicitly deleted;
2. \(K_{act}^{99,+}(\zeta,\chi)\), or the derivative-source data
   \(\Gamma_{act}^{99}(\chi)P_{act}^{99,+}(\zeta,\chi)\), for every retained
   channel projection not explicitly deleted;
3. \(\mathcal O_{act}^{99,+}(\zeta,\chi)\) for every retained same-shell
   action row not assigned to `BTQ`, `zero`, `tail`, or `carry`;
4. the exact-zero list \(\mathsf z_{act}^{99,+}\);
5. the carried list \(\mathsf c_{act}^{99,+}\), with no overlap with
   already parked perimeter/cusp/readout/Paper-14/RP-Cov/RPF/KPdec/WP debits.

When this gate holds, Table 104.5 becomes an executable finite table.  It
computes:

```math
\mathcal E_{act,pass}^{99,+},
\qquad
C_{act,pass}^{99,+},
\qquad
A_{act,pass}^{99,+},
\qquad
\Omega_{act}^{99,+}(\mathbf a),
```

and it contributes to the decay-coverage audit through exactly the rows with

```math
\mathsf r(e)=\mathrm{pass},
\qquad
\Delta_X(e)\ge1.
```

If the gate does not hold, the only honest completion is the safe carried
completion of Definition 105.5.

Proof.

Definitions 104.4 and 104.5 already print the target, support, channel, and
degree updates.  The only remaining entries needed to classify a compatible
action row are the raw value, the inverse slot, and the zero/carry/no-double
charge labels.  Items 1--5 are exactly those finite entries.  Once supplied,
the row table is finite because \(\overline V_{99}^{lit,+}\) and
\(\Xi_{act}^{99,+}\) are finite.  If any required value is missing, treating
the row as pass would import an off-record assumption about the active local
action law, so the carried completion is forced. `square`

### Corollary 105.7: Current Verdict For Action Rows

The action-value ledger is now printed as a finite source gate, but the
current papers do not supply all entries of
\(\mathcal S_{act}^{99,+}\).  Therefore the status sharpens to

```math
\boxed{
\mathrm{PARK\text{-}ROWMAP}^{+}_{SD,cmp}
\quad+\quad
\mathrm{PARK\text{-}ACTSRC}^{+}.
}
```

What is closed:

```math
R_{act}^{99,+}\ \text{target/increment map},
\qquad
\Gamma_{act}^{99}(\chi)\ \text{for all retained }SU(2)\text{ channels},
```

and the safe envelopes conditional on a finite same-record local-action
source table.

What remains open is not a definitional issue.  It is the actual source
theorem/table:

```math
\mathcal S_{act}^{99,+}
\quad\text{on the active }SEL2\text{ scalar law}.
```

Until that table is supplied, support-growing action rows cannot be used to
prove `P21-RED-COVER`, `P21-RED-1KP`, or the final reduced inequality.

## 106. Printing The Structural Schwinger-Dyson Row Map \(R_{SD}^{99,+}\)

This section prints the compact-group Schwinger-Dyson/Casimir row map on the
same over-refined cover.  It uses only the exact finite compact-group identity
and the retained `SU(2)` channel table.  As with the action rows, the
structural target/increment map is finite and printed, while any row whose
projected coefficient or inverse slot is not supplied by the current source
corpus is carried.

### Definition 106.1: Over-Refined SD Atoms

Let \(\mathsf Q_{loc}^{99}=\{-1,0,1\}^4\).  An over-refined
Schwinger-Dyson/Casimir atom is a tuple

```math
\omega=(\theta,S,w,\lambda,\upsilon)
```

with

```math
\theta\in\{\mathrm{Cas},\mathrm{SDdiv},\mathrm{loop},\mathrm{retr}\},
\qquad
S\subseteq\mathsf Q_{loc}^{99},\quad S\ne\varnothing,
```

```math
w\in\mathsf W_{\le4}^{99},
\qquad
\lambda\in\Lambda_*^{99}=\{0,{1\over2},1\},
\qquad
\upsilon\in\Sigma_{99}^{+}.
```

The labels mean:

1. `Cas` is a compact-group Casimir self-row;
2. `SDdiv` is a projected compact-group divergence row;
3. `loop` is a projected finite loop-identity row generated by one SD step;
4. `retr` is a lower-shell retraction row, included so that it can be
   explicitly deleted rather than counted as reduced escape.

The finite over-refined SD atom list is

```math
\mathsf A_{SD}^{99,+}
:=
\{\omega=(\theta,S,w,\lambda,\upsilon)\text{ as above}\}.
```

As in Sections 102 and 104, this list may contain inactive formal atoms.
Inactive atoms are removed by the finite source ledger below.

### Definition 106.2: The Printed SD Index Set

The retained SD index set is

```math
\Xi_{SD}^{99,+}
:=
\left\{
(\omega,\chi):
\omega\in\mathsf A_{SD}^{99,+},\
\chi=(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit},\
\lambda=\lambda(\omega)
\right\}.
```

For a pure Casimir self-row, the intended channel is

```math
\chi_{Cas}(\mu):=(\mu,0,\mu,1),
```

which is present in \(\Xi_{fus}^{99,lit}\) for
\(\mu\in\{0,{1\over2},1\}\).  Non-Casimir rows use the same retained channel
projection convention as Sections 103--105.  Omitted representation channels
belong to the representation-tail ledger and are not rows of
\(R_{SD}^{99,+}\).

### Definition 106.3: SD Projection Scalars

For a retained channel \(\chi=(\mu,\lambda,\mu',1)\), reuse

```math
\Gamma_{SD}^{99}(\chi)
:=
{1\over2}\left(C_2(\mu')-C_2(\mu)-C_2(\lambda)\right),
\qquad
C_2(j)=j(j+1).
```

Thus the eleven values are exactly the values printed in Definition 105.2.
For Casimir self-rows define

```math
\Gamma_{Cas}^{99}(\mu):=C_2(\mu).
```

On the retained `SU(2)` cutoff,

```math
\Gamma_{Cas}^{99}(0)=0,\qquad
\Gamma_{Cas}^{99}({1\over2})={3\over4},\qquad
\Gamma_{Cas}^{99}(1)=2.
```

The universal retained SD scalar envelope is therefore

```math
\Gamma_{SD,max}^{99,+}
:=
\max\left(
\max_{\chi\in\Xi_{fus}^{99,lit}}|\Gamma_{SD}^{99}(\chi)|,
\max_{\mu\in\Lambda_*^{99}}\Gamma_{Cas}^{99}(\mu)
\right)
=2.
```

### Definition 106.4: The SD Source-Value Package

The finite SD source-value package is

```math
\mathcal S_{SD}^{99,+}
:=
\left(
K_{SD}^{99,+},
\mathcal O_{SD}^{99,+},
\mathsf z_{SD}^{99,+},
\mathsf c_{SD}^{99,+}
\right).
```

Here:

1. \(K_{SD}^{99,+}(\omega,\chi)\in\mathbb R\cup\{\star\}\) is the total
   projected compact-group SD/Casimir multiplier after finite projection to
   the retained scalar row;
2. \(\mathcal O_{SD}^{99,+}(\omega,\chi)\in[0,\infty)\cup\{\star\}\) is the
   same-shell inverse off-diagonal slot;
3. \(\mathsf z_{SD}^{99,+}\) is the finite list of exact same-record SD/Casimir
   zeros;
4. \(\mathsf c_{SD}^{99,+}\) is the finite list of carried assignments:
   representation-tail, lower-shell retraction, bounded-collar `BTQ`,
   missing projection coefficient, missing inverse slot, failed
   no-double-charge check, or non-`SEL2` source.

For a derivative-sourced SD row one may set

```math
K_{SD}^{99,+}(\omega,\chi)
=
\Gamma_{SD}^{99}(\chi)P_{SD}^{99,+}(\omega,\chi),
```

where \(P_{SD}^{99,+}\) is the finite projection multiplier.  For a Casimir
self-row one may set

```math
K_{SD}^{99,+}(\omega,\chi_{Cas}(\mu))
=
\Gamma_{Cas}^{99}(\mu)P_{Cas}^{99,+}(\omega).
```

If neither declaration is supplied, the row is carried.

### Definition 106.5: The Structural Row Map \(R_{SD}^{99,+}\)

Let

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in\overline V_{99}^{lit,+},
\qquad
\xi=(\omega,\chi)\in\Xi_{SD}^{99,+},
```

with \(\omega=(\theta,S,w,\lambda,\upsilon)\) and
\(\chi=(\mu,\lambda,\mu',1)\).

If \(\alpha\ne\mu\), the row is undefined.  If \(\theta=\mathrm{retr}\), the
row is not a reduced escaping row and is sent to the retraction/carry ledger.

For \(\alpha=\mu\) and \(\theta\ne\mathrm{retr}\), define

```math
L^\sharp(L,\omega):=L\cup S,
\qquad
\Delta_X^{SD}(L,\omega):=|L^\sharp(L,\omega)\setminus L|,
```

and

```math
L':=\operatorname{Can}_{L}^{99,+}(L^\sharp(L,\omega)).
```

Write \(T=(c,\tau,d,(\lambda_1,w_1),\ldots,(\lambda_d,w_d))\).  Define the SD
target template by

```math
\operatorname{SDTpl}_{99}^{+}(T,L,\omega)
:=
\left(
SD,\,
\tau_{SD}^{99,+}(L,\omega),\,
d,\,
(\lambda_1,w_1),\ldots,(\lambda_d,w_d)
\right),
```

where

```math
\tau_{SD}^{99,+}(L,\omega)
:=
\begin{cases}
T_{\rm esc},&\Delta_X^{SD}(L,\omega)\ge1,\\
T_{\rm chan},&\Delta_X^{SD}(L,\omega)=0.
\end{cases}
```

Set

```math
T':=\operatorname{SDTpl}_{99}^{+}(T,L,\omega),
\qquad
h':=\operatorname{Push}_{fus}^{99,+}(h,\chi),
\qquad
p':=p,
\qquad
\sigma':=\sigma.
```

The target vertex is

```math
\bar v':=(T',\mu',L',h',p',\sigma').
```

Then

```math
R_{SD}^{99,+}(\bar v,\xi)
:=
\left(
\bar v',
\Delta_X,
\Delta_C,
\Delta_h,
\Delta_p,
a,
\mathcal O
\right),
```

with

```math
\Delta_X:=\Delta_X^{SD}(L,\omega),
\qquad
\Delta_C:=\Delta_C^{fus}(\alpha,\mu'),
\qquad
\Delta_h:=\Delta_h^{fus}(h,\chi),
\qquad
\Delta_p:=0.
```

On the strict no-extra-normal-form convention,

```math
a:=|K_{SD}^{99,+}(\omega,\chi)|,
\qquad
\mathcal O:=\mathcal O_{SD}^{99,+}(\omega,\chi).
```

If source or target normal forms are inserted, replace \(a\) by

```math
a
:=
B_{SD,s}^{99,+}(\bar v,\xi)B_{SD,t}^{99,+}(\bar v,\xi)
|K_{SD}^{99,+}(\omega,\chi)|.
```

The strict structural print sets \(B_{SD,s}^{99,+}=B_{SD,t}^{99,+}=1\).

### Table 106.6: Row-By-Row SD Disposition Rule

For each source vertex \(\bar v=(T,\alpha,L,h,p,\sigma)\) and SD index
\(\xi=(\omega,(\mu,\lambda,\mu',1))\), assign exactly one of the following
rows:

| row family | condition | \(s(e)\to t(e)\) | \(a(e)\) | \(d(e)\) | \(\mathcal O(e)\) | disposition | ledger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SD-undef` | \(\alpha\ne\mu\) | no row | not used | not used | not used | undefined | no retained channel at source |
| `SD-retr` | \(\alpha=\mu,\theta=\mathrm{retr}\) | lower shell | retraction ledger | not used | not used | `carry` | lower-shell retraction |
| `SD-zero` | \(\alpha=\mu,\theta\ne\mathrm{retr}, K_{SD}^{99,+}(\omega,\chi)=0\) by named identity | \(\bar v\to\bar v'\) | \(0\) | \(0\) | \(0\) | `zero` | exact compact-group cancellation |
| `SD-BTQ` | \(\alpha=\mu,\theta\ne\mathrm{retr}, \Delta_X=0\), and the row is internal to `BTQ/ACTFULLLAW` | internal | paid by `BTQ/ACTFULLLAW` | \(0\) | not a reduced row | `BTQ` | bounded-collar state |
| `SD-CMSSI` | \(\alpha=\mu,\theta\ne\mathrm{retr}, \Delta_X=0\), finite \(a,\mathcal O\), not internal `BTQ` | \(\bar v\to\bar v'\) | \(a\) | \(0\) | \(\mathcal O\) | `CMSSI` | same-shell inverse ledger |
| `SD-pass` | \(\alpha=\mu,\theta\ne\mathrm{retr}, \Delta_X\ge1\), finite \(a,\mathcal O\), all admissibility checks pass | \(\bar v\to\bar v'\) | \(a\) | \(\Delta_X\) | \(\mathcal O\) | `pass` | reduced escaping SD/Casimir row |
| `SD-carry` | any remaining compatible row, including \(a=\star\), \(\mathcal O=\star\), tail, or no-double-charge failure | removed | carried | not used | not used | `carry` | \(U_{SD,row}^{99,+}\) |

The row-depth contribution is

```math
d(e):=\Delta_X(e)\mathbf 1_{\{\mathsf r(e)=\mathrm{pass}\}}.
```

Thus SD rows are decay-eligible only in the `SD-pass` family.

### Definition 106.7: SD Envelopes And Safe Carried Completion

If \(\mathcal S_{SD}^{99,+}\) supplies finite projection and inverse slots,
define

```math
K_{SD,max}^{99,+}
:=
\max_{(\omega,\chi)\in\Xi_{SD}^{99,+}}
|K_{SD}^{99,+}(\omega,\chi)|,
```

```math
O_{SD,max}^{99,+}
:=
\max_{(\omega,\chi)\in\Xi_{SD}^{99,+}}
\mathcal O_{SD}^{99,+}(\omega,\chi).
```

If the derivative/Casimir source multipliers are used, then

```math
K_{SD,max}^{99,+}
\le
\Gamma_{SD,max}^{99,+}
\max(P_{SD,max}^{99,+},P_{Cas,max}^{99,+})
=
2\max(P_{SD,max}^{99,+},P_{Cas,max}^{99,+}).
```

The certified SD coefficient base obeys

```math
A_{SD,pass}^{99,+}
\le
\max(1,K_{SD,max}^{99,+})
```

on the strict branch.

The safe carried completion \(\mathcal S_{SD,car}^{99,+}\) assigns every
compatible SD row with a missing projection coefficient, missing inverse
slot, tail, lower-shell retraction, or failed no-double-charge check to

```math
U_{SD,row}^{99,+}.
```

Under this safe completion,

```math
\mathcal E_{SD,pass}^{99,+,car}=\varnothing,
\qquad
C_{SD,pass}^{99,+,car}=0,
\qquad
A_{SD,pass}^{99,+,car}=1,
\qquad
\Omega_{SD}^{99,+,car}(\mathbf a)=0.
```

### Theorem 106.8: The SD Row Map Is Printed, But Its Source Values Are Parked

The structural compact-group Schwinger-Dyson/Casimir row map is now printed:

```math
\boxed{
R_{SD}^{99,+}\ \text{is the row map of Definition 106.5 with dispositions
from Table 106.6}.
}
```

The SD source gate

```math
\mathrm{P21\text{-}SDVAL}^{99,+}
(K_{SD,max}^{99,+},O_{SD,max}^{99,+})
```

holds exactly when the finite package
\(\mathcal S_{SD}^{99,+}\) is supplied on the active `SEL2` scalar law with
no overlap with already parked RP/Cov, RPF, `KPdec`, whole-process,
perimeter/cusp/readout, action-source, or comparison-battery debits.

If this gate holds, \(R_{SD}^{99,+}\) contributes the finite table functions

```math
\mathcal E_{SD,pass}^{99,+},
\qquad
C_{SD,pass}^{99,+},
\qquad
A_{SD,pass}^{99,+},
\qquad
\Omega_{SD}^{99,+}(\mathbf a),
```

and its pass rows contribute to decay coverage exactly when
\(\Delta_X\ge1\).  If the gate does not hold, the only honest completion is
the carried completion of Definition 106.7.

Proof.

Paper 14 supplies the exact compact-group Schwinger-Dyson identity before
finite projection.  Section 106 restricts it to the same retained `SU(2)`
channel table and over-refined finite vertex cover already used for
Sections 103--105.  Finiteness follows from the finite sets
\(\mathsf A_{SD}^{99,+}\), \(\Xi_{fus}^{99,lit}\), and
\(\overline V_{99}^{lit,+}\).  The structural target and increment data are
therefore printed.  What the current corpus does not print is the finite
projected source multiplier \(K_{SD}^{99,+}\), the inverse slot
\(\mathcal O_{SD}^{99,+}\), and the exact zero/carry tags for every retained
row.  Those are precisely the entries in \(\mathcal S_{SD}^{99,+}\).  Missing
entries cannot be interpreted as pass rows without importing an off-record
source theorem, so the carried completion is forced. `square`

### Corollary 106.9: Current Finite-Table Status

After Sections 103--106, the printed row-map situation is:

| row class | target/increment map | value/source status |
| --- | --- | --- |
| `fus` | printed | closed and assigned to `CMSSI` on strict branch |
| `act` | printed | parked at `PARK-ACTSRC+` |
| `SD` | printed | parked at `PARK-SDSRC+` |
| `cmp` | not yet printed | parked at `PARK-ROWMAP_cmp+` |

Thus the current status is

```math
\boxed{
\mathrm{PARK\text{-}ROWMAP}^{+}_{cmp}
\quad+\quad
\mathrm{PARK\text{-}ACTSRC}^{+}
\quad+\quad
\mathrm{PARK\text{-}SDSRC}^{+}.
}
```

The next finite-table move is to print \(R_{cmp}^{99,+}\).  After that, the
paper can assemble the carried finite graph and run the zero-growth SCC,
CMSSI, and envelope audits under the safe carried completions.

## 107. Printing The Structural Comparison Row Map \(R_{cmp}^{99,+}\)

This section prints the last structural row map on the over-refined cover.
The comparison rows represent only the common \(E_{14}/X_{13}\) finite-battery
comparison tower.  They do not contain action-source coefficients,
Schwinger-Dyson/Casimir source coefficients, fusion multiplicities,
Paper-16 RP/Cov transport, entry-level `RPF`, `KPdec`, or `WP` defects, or
any continuum Yang-Mills law.  Those costs stay in their already named
ledgers.

The print is therefore intentionally narrow: \(R_{cmp}^{99,+}\) supplies the
finite target and increment bookkeeping for comparison rows.  The actual
comparison coefficient, inverse slot, zero identity, and battery/carry
decision remain a finite source package.

### Definition 107.1: Over-Refined Comparison Atoms

Let \(\mathsf Q_{loc}^{99}=\{-1,0,1\}^4\).  An over-refined comparison atom is
a tuple

```math
\beta=(\theta,S,w,\delta_p,\upsilon,\mathfrak b)
```

with

```math
\theta\in
\{\mathrm{E14},\mathrm{X13cut},\mathrm{X13read},
\mathrm{diag},\mathrm{battery},\mathrm{retr}\},
```

```math
S\subseteq\mathsf Q_{loc}^{99},\qquad
w\in\mathsf W_{\le4}^{99}\cup\{\varnothing\},
```

```math
\delta_p\in\{0,1,2\},\qquad
\upsilon\in\Sigma_{99}^{+},\qquad
\mathfrak b\in
\{\mathrm{external},\mathrm{cmpbat},\mathrm{zero},\mathrm{carry}\}.
```

The labels mean:

1. `E14` is a common Paper-14 export-comparison row after all component
   debits already assigned elsewhere are excluded;
2. `X13cut` is the cutoff-to-exact comparison row of the \(X_{13}\) battery;
3. `X13read` is the exact-readout comparison row of the \(X_{13}\) battery;
4. `diag` is a finite diagonalization/common-row alignment step;
5. `battery` is an internal comparison-battery transition;
6. `retr` is a lower-shell or off-branch retraction, included only so it can
   be deleted or carried explicitly.

The finite atom list is

```math
\mathsf A_{cmp}^{99,+}
:=
\{\beta=(\theta,S,w,\delta_p,\upsilon,\mathfrak b)\text{ as above}\}.
```

As before, this is an over-cover.  Inactive formal atoms are removed by the
comparison source ledger.

### Definition 107.2: The Printed Comparison Index Set

The comparison index set is

```math
\Xi_{cmp}^{99,+}
:=
\mathsf A_{cmp}^{99,+}.
```

Comparison rows do not perform representation fusion.  They preserve the
retained representation coordinate:

```math
\alpha'=\alpha.
```

Any row that needs a nontrivial representation-channel change must factor
through \(R_{fus}^{99,+}\).  This convention prevents the common comparison
battery from double-counting fusion/channel bookkeeping.

### Definition 107.3: Comparison Source-Value Package

The finite comparison source-value package is

```math
\mathcal S_{cmp}^{99,+}
:=
\left(
a_{cmp,raw}^{99,+},
\mathcal O_{cmp}^{99,+},
\mathsf z_{cmp}^{99,+},
\mathsf b_{cmp}^{99,+},
\mathsf c_{cmp}^{99,+}
\right).
```

Here:

1. \(a_{cmp,raw}^{99,+}(\bar v,\beta)\in[0,\infty)\cup\{\star\}\) is the
   absolute raw finite comparison coefficient after the row is projected to
   the active `SEL2` scalar battery;
2. \(\mathcal O_{cmp}^{99,+}(\bar v,\beta)\in[0,\infty)\cup\{\star\}\) is the
   same-shell inverse off-diagonal slot;
3. \(\mathsf z_{cmp}^{99,+}\) is the finite list of exact same-record
   comparison identities with coefficient zero;
4. \(\mathsf b_{cmp}^{99,+}\) is the finite list of rows wholly internal to
   the common \(E_{14}/X_{13}\) comparison battery;
5. \(\mathsf c_{cmp}^{99,+}\) is the finite list of carried assignments:
   missing comparison coefficient, missing inverse slot, product-degree tail,
   lower-shell retraction, off-record comparison, or no-double-charge failure.

The symbol \(\star\) is not a number.  A row needing a \(\star\)-entry cannot
be used as a pass row.

### Definition 107.4: The Structural Row Map \(R_{cmp}^{99,+}\)

Let

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in\overline V_{99}^{lit,+},
\qquad
\beta=(\theta,S,w,\delta_p,\upsilon,\mathfrak b)\in\Xi_{cmp}^{99,+}.
```

If \(\theta=\mathrm{retr}\), the row is not a reduced escaping comparison row
and is sent to the retraction/carry ledger.

If

```math
p+\delta_p>p_*^{99,+}=2,
```

the row is outside the active product/comparison degree cutoff and is sent to
the comparison degree-tail/carry ledger.

Otherwise define

```math
L^\sharp(L,\beta):=L\cup S,
\qquad
\Delta_X^{cmp}(L,\beta):=|L^\sharp(L,\beta)\setminus L|,
```

and

```math
L':=\operatorname{Can}_{L}^{99,+}(L^\sharp(L,\beta)).
```

Write \(T=(c,\tau,d,(\lambda_1,w_1),\ldots,(\lambda_d,w_d))\).  Define the
comparison target template by

```math
\operatorname{CmpTpl}_{99}^{+}(T,L,\beta)
:=
\left(
cmp,\,
\tau_{cmp}^{99,+}(L,\beta),\,
d,\,
(\lambda_1,w_1),\ldots,(\lambda_d,w_d)
\right),
```

where

```math
\tau_{cmp}^{99,+}(L,\beta)
:=
\begin{cases}
T_{\rm mix},&\theta=\mathrm{battery}\text{ or }\mathfrak b=\mathrm{cmpbat},\\
T_{\rm esc},&\Delta_X^{cmp}(L,\beta)\ge1,\\
T_{\rm chan},&\Delta_X^{cmp}(L,\beta)=0.
\end{cases}
```

Set

```math
T':=\operatorname{CmpTpl}_{99}^{+}(T,L,\beta),
\qquad
\alpha':=\alpha,
\qquad
h':=h,
```

```math
p':=p+\delta_p,
\qquad
\sigma':=\upsilon.
```

The target vertex is

```math
\bar v':=(T',\alpha',L',h',p',\sigma').
```

Then

```math
R_{cmp}^{99,+}(\bar v,\beta)
:=
\left(
\bar v',
\Delta_X,
\Delta_C,
\Delta_h,
\Delta_p,
a,
\mathcal O
\right),
```

with

```math
\Delta_X:=\Delta_X^{cmp}(L,\beta),
\qquad
\Delta_C:=0,
\qquad
\Delta_h:=0,
\qquad
\Delta_p:=\delta_p.
```

On the strict no-extra-normal-form convention,

```math
a:=a_{cmp,raw}^{99,+}(\bar v,\beta),
\qquad
\mathcal O:=\mathcal O_{cmp}^{99,+}(\bar v,\beta).
```

If comparison source or target normal forms are inserted, replace \(a\) by

```math
a
:=
B_{cmp,s}^{99,+}(\bar v,\beta)B_{cmp,t}^{99,+}(\bar v,\beta)
a_{cmp,raw}^{99,+}(\bar v,\beta).
```

The strict structural print sets
\(B_{cmp,s}^{99,+}=B_{cmp,t}^{99,+}=1\).

### Table 107.5: Row-By-Row Comparison Disposition Rule

For each source vertex \(\bar v\) and comparison atom \(\beta\), assign
exactly one of the following rows:

| row family | condition | \(s(e)\to t(e)\) | \(a(e)\) | \(d(e)\) | \(\mathcal O(e)\) | disposition | ledger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `cmp-retr` | \(\theta=\mathrm{retr}\) | lower shell | retraction ledger | not used | not used | `carry` | lower-shell comparison retraction |
| `cmp-tail` | \(p+\delta_p>2\) | removed | degree-tail/carry | not used | not used | `carry` | comparison degree tail |
| `cmp-battery` | \(\theta=\mathrm{battery}\) or \(\mathfrak b=\mathrm{cmpbat}\) or \((\bar v,\beta)\in\mathsf b_{cmp}^{99,+}\) | battery internal | paid inside common battery | \(0\) | battery internal | `cmpbat` | common \(E_{14}/X_{13}\) finite battery |
| `cmp-zero` | \(\mathfrak b=\mathrm{zero}\), or \((\bar v,\beta)\in\mathsf z_{cmp}^{99,+}\), or \(a_{cmp,raw}^{99,+}(\bar v,\beta)=0\) by a named identity | \(\bar v\to\bar v'\) | \(0\) | \(0\) | \(0\) | `zero` | exact comparison identity |
| `cmp-CMSSI` | \(\Delta_X=0\), finite \(a,\mathcal O\), not internal battery | \(\bar v\to\bar v'\) | \(a\) | \(0\) | \(\mathcal O\) | `CMSSI` | same-shell comparison inverse row |
| `cmp-pass` | \(\Delta_X\ge1\), finite \(a,\mathcal O\), not internal battery, all admissibility checks pass | \(\bar v\to\bar v'\) | \(a\) | \(0\) | \(\mathcal O\) | `pass` | non-retracting comparison escape |
| `cmp-carry` | \(\mathfrak b=\mathrm{carry}\), or any remaining compatible row, including \(a=\star\), \(\mathcal O=\star\), off-record comparison, or no-double-charge failure | removed | carried | not used | not used | `carry` | \(U_{cmp,row}^{99,+}\) |

The comparison row-depth contribution is always

```math
d(e)=0.
```

Thus comparison rows may increase branching, coefficients, inverse sums, and
support size, but they do not by themselves supply analytic decay coverage.
Any later theorem that wants a comparison row to carry decay must reclassify
that row explicitly and prove the same-record source estimate.

### Definition 107.6: Comparison Envelopes And Safe Carried Completion

If \(\mathcal S_{cmp}^{99,+}\) supplies finite coefficient and inverse slots,
define

```math
A_{cmp,raw}^{99,+}
:=
\max_{\bar v,\beta}
\max(1,a_{cmp,raw}^{99,+}(\bar v,\beta)),
```

```math
O_{cmp,max}^{99,+}
:=
\max_{\bar v,\beta}
\mathcal O_{cmp}^{99,+}(\bar v,\beta).
```

On the strict branch,

```math
A_{cmp,pass}^{99,+}
\le
A_{cmp,raw}^{99,+}.
```

With comparison normal forms,

```math
A_{cmp,pass}^{99,+}
\le
\max(1,B_{cmp,s}^{99,+}B_{cmp,t}^{99,+}A_{cmp,raw}^{99,+}).
```

The safe carried completion \(\mathcal S_{cmp,car}^{99,+}\) assigns every
compatible comparison row with a missing coefficient, missing inverse slot,
off-record comparison, degree-tail, lower-shell retraction, or failed
no-double-charge check to \(U_{cmp,row}^{99,+}\), and assigns all declared
internal battery rows to `cmpbat`.

Under this completion,

```math
\mathcal E_{cmp,pass}^{99,+,car}=\varnothing,
\qquad
C_{cmp,pass}^{99,+,car}=0,
\qquad
A_{cmp,pass}^{99,+,car}=1,
\qquad
\Omega_{cmp}^{99,+,car}(\mathbf a)=0.
```

### Theorem 107.7: The Comparison Row Map Is Printed, But Its Source Values Are Parked

The structural common-comparison row map is now printed:

```math
\boxed{
R_{cmp}^{99,+}\ \text{is the row map of Definition 107.4 with dispositions
from Table 107.5}.
}
```

The comparison source gate

```math
\mathrm{P21\text{-}CMPVAL}^{99,+}
(A_{cmp,raw}^{99,+},O_{cmp,max}^{99,+})
```

holds exactly when the finite package \(\mathcal S_{cmp}^{99,+}\) is supplied
on the active `SEL2` scalar law, with no overlap with the already parked
Paper-14 component debit, \(X_{13}\) debit, RP/Cov, `RPF`, `KPdec`, `WP`,
perimeter/cusp/readout, action-source, SD-source, or fusion/channel ledgers.

If this gate holds, \(R_{cmp}^{99,+}\) contributes the finite table functions

```math
\mathcal E_{cmp,pass}^{99,+},
\qquad
C_{cmp,pass}^{99,+},
\qquad
A_{cmp,pass}^{99,+},
\qquad
\Omega_{cmp}^{99,+}(\mathbf a).
```

If the gate does not hold, the only honest completion is the carried
completion of Definition 107.6.

Proof.

Sections 61--67 isolate the common \(E_{14}/X_{13}\) finite-battery bypass and
comparison tower as a same-record finite process.  Sections 89--98 assign
that tower to the `cmp` class and forbid it from absorbing RP/Cov, entry
residual, action-source, SD-source, or fusion costs.  Definition 107.1 prints
a finite over-refined atom list for exactly that tower, and Definition 107.4
prints the induced source, target, support, channel, label, and degree
increments on the already printed vertex cover.  Thus the structural row map
is finite and explicit.

What remains absent from the current corpus is not the target map.  It is the
finite source package: the raw comparison coefficient, inverse slot,
exact-zero list, internal-battery list, and carry list for every retained
row.  Treating a missing comparison entry as a pass row would spend an
unproved comparison theorem.  Therefore the source gate or the carried
completion is forced. `square`

### Corollary 107.8: Current Finite-Table Status

After Sections 103--107, the printed row-map situation is:

| row class | target/increment map | value/source status |
| --- | --- | --- |
| `fus` | printed | closed and assigned to `CMSSI` on strict branch |
| `act` | printed | parked at `PARK-ACTSRC+` |
| `SD` | printed | parked at `PARK-SDSRC+` |
| `cmp` | printed | parked at `PARK-CMPSRC+` |

Thus the current status is

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}^{+}
\quad+\quad
\mathrm{PARK\text{-}SDSRC}^{+}
\quad+\quad
\mathrm{PARK\text{-}CMPSRC}^{+}.
}
```

The row-map obstruction has been discharged on the over-refined cover.
Section 108 below assembles the carried finite graph using the safe
completions of Sections 105--107 and runs the zero-growth SCC classification.
Any nonempty pass graph beyond fusion bookkeeping now requires an actual
same-record source table for `act`, `SD`, or `cmp`.

## 108. Carried Finite Table And Zero-Growth SCC Classification

This section builds the carried finite table promised by Corollary 107.8.  It
combines the four printed structural row maps

```math
R_{fus}^{99,+},\qquad
R_{act}^{99,+},\qquad
R_{SD}^{99,+},\qquad
R_{cmp}^{99,+}
```

with the strict carried source convention:

```math
\mathcal S_{act}^{99,+}=\mathcal S_{act,car}^{99,+}
\quad\text{unless } \mathrm{P21\text{-}ACTVAL}^{99,+}\text{ is supplied,}
```

```math
\mathcal S_{SD}^{99,+}=\mathcal S_{SD,car}^{99,+}
\quad\text{unless } \mathrm{P21\text{-}SDVAL}^{99,+}\text{ is supplied,}
```

and

```math
\mathcal S_{cmp}^{99,+}=\mathcal S_{cmp,car}^{99,+}
\quad\text{unless } \mathrm{P21\text{-}CMPVAL}^{99,+}\text{ is supplied.}
```

No source gate is silently assumed.  Thus a row with a missing coefficient,
missing inverse slot, missing zero identity, failed no-double-charge check, or
off-record provenance is removed from the pass graph and charged to the
appropriate carried ledger.

### Definition 108.1: The Carried Candidate Table

Let

```math
\overline V_{108}^{+}:=\overline V_{99}^{lit,+}.
```

The carried candidate table is

```math
\mathsf C_{108}^{car,+}
:=
\left(
\overline V_{108}^{+},
\overline E_{108}^{car,+},
s,t,c,\xi,a,\Delta_X,\Delta_C,\Delta_h,\Delta_p,
\mathcal O,\mathsf r,\mathsf p,\mathsf b
\right).
```

The candidate edge set is the disjoint union

```math
\overline E_{108}^{car,+}
:=
\overline E_{fus}^{108}
\dot\cup
\overline E_{act}^{108,car}
\dot\cup
\overline E_{SD}^{108,car}
\dot\cup
\overline E_{cmp}^{108,car}.
```

The four pieces are obtained by applying the printed row maps:

```math
\overline E_{fus}^{108}
:=
\left\{
(\bar v,\xi,R_{fus}^{99,+}(\bar v,\xi)):
\bar v\in\overline V_{108}^{+},\
\xi\in\Xi_{fus}^{99,lit},\
R_{fus}^{99,+}(\bar v,\xi)\text{ is defined}
\right\},
```

```math
\overline E_{act}^{108,car}
:=
\left\{
e_{act}^{car}(\bar v,\xi):
\bar v\in\overline V_{108}^{+},\
\xi\in\Xi_{act}^{99,+},\
R_{act}^{99,+}(\bar v,\xi)\text{ is defined or tail-compatible}
\right\},
```

```math
\overline E_{SD}^{108,car}
:=
\left\{
e_{SD}^{car}(\bar v,\xi):
\bar v\in\overline V_{108}^{+},\
\xi\in\Xi_{SD}^{99,+},\
R_{SD}^{99,+}(\bar v,\xi)\text{ is defined or retraction-compatible}
\right\},
```

and

```math
\overline E_{cmp}^{108,car}
:=
\left\{
e_{cmp}^{car}(\bar v,\beta):
\bar v\in\overline V_{108}^{+},\
\beta\in\Xi_{cmp}^{99,+},\
R_{cmp}^{99,+}(\bar v,\beta)\text{ is defined or tail/retraction-compatible}
\right\}.
```

For \(e_{c}^{car}(\bar v,\xi)\), the target is the printed target of
\(R_c^{99,+}(\bar v,\xi)\) when that row is defined.  If the attempted row is
only tail-compatible or retraction-compatible, it has no retained target and
is immediately assigned to `carry`.  Undefined representation-channel
mismatches are not rows.

### Definition 108.2: Carried Disposition Function

The carried disposition function \(\mathsf r_{108}^{car}\) is defined by the
following class rules.

| class | structural source | carried disposition | pass contribution | ledger |
| --- | --- | --- | --- | --- |
| `fus` | \(R_{fus}^{99,+}\) | `CMSSI` for every defined retained fusion row | none | same-shell channel ledger |
| `act` | \(R_{act}^{99,+}\) | `BTQ` if internal `BTQ/ACTFULLLAW`; `zero` only for already named exact zeros; otherwise `carry` under \(\mathcal S_{act,car}^{99,+}\) | none | \(U_{act,row}^{99,+}+U_{act,prod}^{99,+}\) |
| `SD` | \(R_{SD}^{99,+}\) | `BTQ` if internal `BTQ/ACTFULLLAW`; `zero` only for already named exact zeros; otherwise `carry` under \(\mathcal S_{SD,car}^{99,+}\) | none | \(U_{SD,row}^{99,+}\) |
| `cmp` | \(R_{cmp}^{99,+}\) | `cmpbat` for internal comparison-battery rows; `zero` for already named exact zeros; otherwise `carry` under \(\mathcal S_{cmp,car}^{99,+}\) | none | \(U_{cmp,row}^{99,+}\) |

Thus

```math
\mathsf r_{108}^{car}(e)\in
\{\mathrm{CMSSI},\mathrm{BTQ},\mathrm{cmpbat},\mathrm{zero},\mathrm{carry}\}
```

for every row in \(\overline E_{108}^{car,+}\).  In particular,

```math
\mathsf r_{108}^{car}(e)\ne\mathrm{pass}
\qquad(e\in\overline E_{108}^{car,+}).
```

The provenance labels are:

```math
\mathsf p(e)\in
\{R_{fus}^{99,+},R_{act}^{99,+},R_{SD}^{99,+},R_{cmp}^{99,+}\}
```

together with the safe carried source completion that determined the
disposition.  The closure label is the strict full-law label unless an
explicit degree-tail row is carried:

```math
\mathsf b(e)=\mathrm{fulllaw}
```

for retained rows, and the named tail/carry ledger for removed rows.

### Lemma 108.3: The Carried Table Is Admissible

The certificate \(\mathsf C_{108}^{car,+}\) satisfies the row-admissibility
checks of Definition 96.2.

Proof.

The row-map check holds by construction: every retained row is produced by one
of \(R_{fus}^{99,+}\), \(R_{act}^{99,+}\), \(R_{SD}^{99,+}\), or
\(R_{cmp}^{99,+}\).  The same-record check holds because Sections 103--107
print only finite rows on the active pushed-forward `SEL2` scalar law.  The
no-double-charge check is built into the row-map sections: fusion rows do not
charge transport or comparison debits; action rows exclude perimeter, cusp,
readout, Paper-14, RP/Cov, RPF, `KPdec`, and whole-process mismatch; SD rows
exclude action-source and comparison-battery costs; comparison rows exclude
fusion, action-source, SD-source, RP/Cov, RPF, `KPdec`, `WP`, and
perimeter/cusp/readout costs.  Cutoff failures are carried as product,
representation, or comparison-degree tails.  Zero rows require named exact
same-record identities.  Carried rows are removed from the pass graph and
placed in named nonnegative residuals.  Hence all checks are satisfied.
`square`

### Definition 108.4: The Retained Pass Graph Of The Carried Table

The retained pass edge set of the carried table is

```math
\overline E_{pass}^{108,car}
:=
\{e\in\overline E_{108}^{car,+}:
\mathsf r_{108}^{car}(e)=\mathrm{pass}\}.
```

By Definition 108.2,

```math
\boxed{
\overline E_{pass}^{108,car}=\varnothing.
}
```

The carried pass graph is therefore

```math
\overline{\mathfrak A}_{pass}^{108,car}
:=
(\overline V_{108}^{+},\varnothing).
```

The zero-growth pass subgraph is

```math
\overline{\mathfrak A}_{0}^{108,car}
:=
\left(
\overline V_{108}^{+},
\{e\in\overline E_{pass}^{108,car}:\Delta_X(e)=0\}
\right)
=
(\overline V_{108}^{+},\varnothing).
```

### Theorem 108.5: Zero-Growth SCC Classification On The Carried Strict Branch

On the carried strict branch, the zero-growth SCC test has the following
complete verdict.

1. **Pass-graph SCCs.**  There are no directed SCCs in the zero-growth pass
   subgraph:

   ```math
   \overline{\mathfrak A}_{0}^{108,car}
   =
   (\overline V_{108}^{+},\varnothing).
   ```

2. **Fusion cycles.**  Retained fusion cycles may exist in the candidate
   table, because \(R_{fus}^{99,+}\) contains zero-support channel rows.
   They are impossible as pass cycles on the carried strict branch, since
   every retained fusion row has disposition `CMSSI`.

3. **Bounded-collar cycles.**  Any row recognized as internal to
   `BTQ/ACTFULLLAW` is impossible as a reduced pass cycle, because its
   disposition is `BTQ` and it has already been contracted into the bounded
   collar state.

4. **Comparison-battery cycles.**  Internal common-comparison cycles may exist
   in the candidate table.  They are impossible as pass cycles on the carried
   strict branch, because their disposition is `cmpbat`.  Non-internal
   comparison rows without \(\mathrm{P21\text{-}CMPVAL}^{99,+}\) are carried.

5. **Action/SD zero-growth cycles.**  Potential action or SD zero-growth
   cycles are not certified pass cycles.  Under
   \(\mathcal S_{act,car}^{99,+}\) and \(\mathcal S_{SD,car}^{99,+}\), every
   compatible action/SD row lacking a supplied finite value package is
   carried, zeroed by a named identity, or placed in `BTQ`/`CMSSI`.  Therefore
   no action/SD zero-growth SCC remains in the pass graph.

Consequently the finite SCC test cannot return `FAIL-SIZE` on the carried
strict branch.  It returns the finite-depth empty-pass verdict:

```math
T_{\ge1}^{red,act,108,car}(j)=0
```

for the certified carried pass graph.

Proof.

Definition 108.4 gives an empty pass edge set.  A directed SCC with an edge
requires at least one edge, so the zero-growth pass subgraph has no nontrivial
SCC.  Items 2--5 classify the candidate cycles before pass-graph deletion:
fusion rows are repaired by `CMSSI`; bounded-collar rows are internal `BTQ`;
comparison-battery rows are internal `cmpbat`; and action/SD rows are not
pass rows unless their source packages are supplied.  Hence no candidate
cycle can survive as a zero-growth pass SCC under the carried strict
completion.  The finite-depth statement is Algorithm 97.6 applied to the
empty pass graph. `square`

### Corollary 108.6: What Remains After The Carried SCC Pass

The carried finite table settles only the strict carried branch.  It proves:

```math
\overline E_{pass}^{108,car}=\varnothing,
\qquad
\overline{\mathfrak A}_{0}^{108,car}
=(\overline V_{108}^{+},\varnothing),
```

so the following cycles are impossible as certified pass cycles:

```math
\text{fusion-only cycles},\quad
\text{BTQ bounded-collar cycles},\quad
\text{comparison-battery cycles},\quad
\text{action/SD zero-growth cycles}.
```

What remains open is not an SCC in the carried pass graph.  It is the source
problem of creating a nonempty pass graph:

```math
\mathrm{PARK\text{-}ACTSRC}^{+},\qquad
\mathrm{PARK\text{-}SDSRC}^{+},\qquad
\mathrm{PARK\text{-}CMPSRC}^{+}.
```

If any of these source gates is later supplied, the corresponding rows must
be reinserted into the pass graph and the zero-growth SCC test must be rerun.
The dangerous future cases are exactly:

1. a supplied action/SD zero-growth pass SCC not killed by `BTQ`, `CMSSI`, or
   an exact zero selector;
2. a supplied comparison escape row that is not internal to `cmpbat` and
   creates branching or inverse growth without analytic decay coverage;
3. a supplied source package that changes a carried row into pass while
   violating the no-double-charge exclusions.

Until one of the source packages is supplied, the certified carried graph has
no reduced all-depth tail to estimate.  This is not a proof of confinement and
not a failure of confinement; it is the honest empty-pass completion of the
current finite table.

## 109. First Action-Source Audit For `ACTSRC+`

Section 108 identifies `PARK-ACTSRC+` as one of the three remaining
finite-source obstructions.  This section checks the relevant earlier papers
before spending or zeroing any action rows.  The conclusion is deliberately
strict: Papers 16 and 20 provide a strong same-record envelope route, but not
the literal finite action-value table required by Section 105.

### Audit 109.1: Three Different Action Objects

There are three action-related objects in the corpus, and they must not be
conflated.

1. **The actual `SEL2` scalar row freeze.**  Paper 20 defines
   `P20-SEL2-ACTROW`.  It freezes the active finite row

   ```math
   \mathfrak R_j^{SEL2}
   =
   (i(j),H_j,L_j,S_j,B_j^{sheet},\mathscr S_j^{SEL2},
   \mathscr C_j^{SEL2},Y_j,Z_j,\nu_{conv,j}^{sheet},
   \lambda_j,\mathcal R_j,P_j,\psi_\rho)
   ```

   and gives the exact scalar target

   ```math
   \widetilde a_{\rho,j}^{SEL2}
   =
   \int
   \psi_\rho(P_j(Y,Z))\mathcal R_j(Y,Z)\,
   d\nu_{conv,j}^{sheet}(Y)d\lambda_j(Z).
   ```

   This is a coefficient/readout row freeze.  It does not enumerate the
   action atoms \(\zeta\), their channel multipliers, or the inverse
   off-diagonal slots of \(\mathcal S_{act}^{99,+}\).

2. **The heat-kernel actual trajectory.**  Paper 16's `HK-AYM` gives the
   finite heat-kernel lattice law

   ```math
   d\mu_i^{HK}
   =
   Z_i^{-1}
   \prod_p K_{t_i}(U_p)\prod_e d{\rm Haar}(U_e),
   \qquad
   K_t(U)=\sum_\lambda d_\lambda e^{-tC_2(\lambda)/2}\chi_\lambda(U).
   ```

   This is the finite same-record action law used by the primary regulator
   path.  It proves that the underlying finite action law exists and is
   compact-group heat-kernel based.  It is not yet the reduced Section-105
   row-value table.

3. **The small-field YM2 vertex ledger.**  Paper 16's `HK-SF-YM2` gives a
   finite local second-order vertex ledger on the same pushed-forward finite
   record law.  In the strict minimal branch its local envelope has the form

   ```math
   C_v^{YM2,min}
   =
   24C_4C_{cov}^2
   +18C_3^2C_{cov}^3
   +C_JC_{cov}
   +C_{rem}g_*^{\epsilon_v},
   ```

   while the full branch uses the finite constant \(C_v^{YM2}\).  This is a
   local vertex-envelope source.  It does not by itself print
   \(c_{act}^{99,+}(\zeta)\), \(K_{act}^{99,+}(\zeta,\chi)\), or
   \(\mathcal O_{act}^{99,+}(\zeta,\chi)\) row by row.

### Definition 109.2: Literal Action-Source Gate

The literal action-source gate

```math
\mathrm{P21\text{-}ACTSRC\text{-}LIT}^{99,+}
```

holds when the following finite same-record package is supplied on the active
`SEL2` scalar law:

```math
\mathcal S_{act}^{99,+}
=
\left(
c_{act}^{99,+},
K_{act}^{99,+},
P_{act}^{99,+},
\mathcal O_{act}^{99,+},
\mathsf z_{act}^{99,+},
\mathsf c_{act}^{99,+}
\right)
```

with the meanings of Definition 105.1.  Equivalently, it supplies:

1. an active atom retention/deletion map inside \(\mathsf A_{act}^{99,+}\);
2. the local coefficients \(c_{act}^{99,+}(\zeta)\);
3. the channel multipliers \(K_{act}^{99,+}(\zeta,\chi)\), or the derivative
   data \(P_{act}^{99,+}(\zeta,\chi)\) together with
   \(\Gamma_{act}^{99}(\chi)\);
4. the same-shell inverse slots
   \(\mathcal O_{act}^{99,+}(\zeta,\chi)\);
5. an exact same-record zero list; and
6. a carried list with no overlap with Paper-14, RP/Cov, RPF, `KPdec`, `WP`,
   perimeter/cusp/readout, or comparison-battery debits.

Only this literal gate turns \(R_{act}^{99,+}\) into executable pass rows.

### Lemma 109.3: `ACTROW` Does Not Imply `ACTSRC-LIT`

`P20-SEL2-ACTROW` does not imply
\(\mathrm{P21\text{-}ACTSRC\text{-}LIT}^{99,+}\).

Proof.

`P20-SEL2-ACTROW` fixes a finite scalar coefficient target and identifies the
finite pushed-forward row on which the coefficient is evaluated.  Its output
is the scalar integral
\(\widetilde a_{\rho,j}^{SEL2}\) and the heat-kernel comparison time
\(T_j^{SEL2,conv}\).  Section 105 needs a different object: a finite row
table indexed by action atoms and retained representation channels.  The
scalar target does not determine, row by row, which local action atoms are
retained, which product rows are derivative-sourced, which inverse
off-diagonal slots are finite, or which exact zero identities hold.  Therefore
the implication would add finite source data not contained in `ACTROW`.
`square`

### Definition 109.4: YM2 Envelope Action-Source Gate

The weaker YM2 envelope gate

```math
\mathrm{P21\text{-}ACTSRC\text{-}YM2ENV}^{99,+}
(\Pi_{act}^{99,+},C_{act}^{YM2},O_{act}^{YM2})
```

holds if the `HK-SF-YM2` local vertex ledger is pushed forward to the active
over-refined action atoms with finite projection norm
\(\Pi_{act}^{99,+}\), finite inverse-slot envelope \(O_{act}^{YM2}\), and

```math
C_{act}^{YM2}
\le
\Pi_{act}^{99,+} C_v^{YM2}
```

on the full branch, or

```math
C_{act}^{YM2,min}
\le
\Pi_{act}^{99,+} C_v^{YM2,min}
```

on the strict minimal branch.  The envelope asserts that every retained
action row sourced through the YM2 ledger satisfies

```math
\left|
c_{act}^{99,+}(\zeta)
K_{act}^{99,+}(\zeta,\chi)
\right|
\le
C_{act}^{YM2},
\qquad
\mathcal O_{act}^{99,+}(\zeta,\chi)
\le
O_{act}^{YM2},
```

after deleting exact zeros and rows assigned to `BTQ`, `CMSSI`, or a carried
tail.  The gate is weaker than `ACTSRC-LIT`: it bounds rows, but need not
name every row value individually.

### Lemma 109.5: What `HK-SF-YM2` Supplies

On the common pushed-forward finite record law, `HK-SF-YM2` supplies the
following source data for Section 105:

```math
\text{finite local label list}
\quad+\quad
p=1
\quad+\quad
C_v^{YM2}\ \text{or}\ C_v^{YM2,min}.
```

It supplies a valid route to
\(\mathrm{P21\text{-}ACTSRC\text{-}YM2ENV}^{99,+}\) once the finite
projection norm and inverse-slot envelope in Definition 109.4 are provided.
It does not supply
\(\mathrm{P21\text{-}ACTSRC\text{-}LIT}^{99,+}\) by itself.

Proof.

Paper 16 states `HK-SF-YM2` as a finite second-order vertex list with a
finite vertex constant and \(p=1\).  Paper 20 imports that ledger on the
active `SEL2` scalar record for the heat-kernel scalar comparison, including
the odd cancellation and time-tangent absorption clauses.  These facts give a
finite local envelope source.  To obtain the Section-105 literal table one
must still identify the active action atoms, push each local YM2 label to the
over-refined vertex cover, evaluate each retained channel multiplier, and
bound or compute each inverse off-diagonal slot.  Those are precisely the
missing projection and row-value data in Definition 109.4 and Definition
109.2. `square`

### Lemma 109.6: Derivative-Channel Zeroes Are Conditional Exact Zeroes

For derivative-sourced action rows only, the channel rows

```math
F_1,\ F_2,\ F_3,\ F_4,\ F_8
```

are exact zero rows, because Section 105 computes

```math
\Gamma_{act}^{99}(F_i)=0
\qquad
i\in\{1,2,3,4,8\}
```

and derivative-sourced rows obey

```math
K_{act}^{99,+}(\zeta,F_i)
=
\Gamma_{act}^{99}(F_i)P_{act}^{99,+}(\zeta,F_i).
```

They are not universal action zeroes.  A pure product row with an independent
finite product source can still contribute on the same representation
channel.

Proof.

This is the displayed contraction rule of Definition 105.3.  If the row is
declared derivative-sourced and no independent product source is present, the
multiplier is zero.  If a separate product source supplies
\(K_{act}^{99,+}\) directly, the derivative contraction is not the defining
multiplier, so \(\Gamma_{act}^{99}=0\) gives no zero identity. `square`

### Theorem 109.7: Current `ACTSRC+` Verdict

The current papers prove the following action-source facts:

```math
\mathrm{P20\text{-}SEL2\text{-}ACTROW},
\qquad
\mathrm{HK\text{-}AYM},
\qquad
\mathrm{HK\text{-}SF\text{-}YM2}
\ \text{as a finite local envelope route},
```

and Section 105 computes all retained compact-group projection scalars
\(\Gamma_{act}^{99}(\chi)\).  They do not prove
\(\mathrm{P21\text{-}ACTSRC\text{-}LIT}^{99,+}\).

Consequently the honest refined status is

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}^{+}
=
\mathrm{PARK\text{-}ACTSRC\text{-}PUSH}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ZC}^{99,+}.
}
```

Here:

```math
\mathrm{PARK\text{-}ACTSRC\text{-}PUSH}^{99,+}
```

is the missing finite pushforward from the `HK-SF-YM2` local labels to
\(\mathsf A_{act}^{99,+}\) and the projection norm \(\Pi_{act}^{99,+}\);

```math
\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL}^{99,+}
```

is the missing row-by-row coefficient/multiplier table or its certified YM2
envelope;

```math
\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{99,+}
```

is the missing same-shell inverse off-diagonal bound
\(\mathcal O_{act}^{99,+}\); and

```math
\mathrm{PARK\text{-}ACTSRC\text{-}ZC}^{99,+}
```

is the missing exact zero/carry classification, including the distinction
between derivative zeroes and independent product rows.

Until these four subgates are supplied, Section 108's carried completion is
still forced:

```math
\mathcal E_{act,pass}^{99,+,car}=\varnothing,
\qquad
A_{act,pass}^{99,+,car}=1,
\qquad
\Omega_{act}^{99,+,car}=0.
```

Proof.

The positive source facts are exactly Audit 109.1 and Lemma 109.5.  Lemma
109.3 rules out upgrading the scalar row freeze to a literal action table.
Lemma 109.6 supplies only conditional derivative-channel zeroes, not a
universal action zero list.  Definition 105.1 shows that executable action
rows need a pushforward, row values or a certified envelope, inverse slots,
and zero/carry/no-double-charge classification.  These four missing packages
are precisely the displayed refined parks.  Therefore no action row may be
reinserted into the pass graph yet. `square`

### Corollary 109.8: Action-Source Work Program

The action-source work program is the following.  Section 110 begins this
program by carrying out items 1--2 in an over-refined envelope form.

1. Print the finite pushforward

   ```math
   \pi_{YM2\to act}^{99,+}:
   I_v^{YM2}\times\overline V_{99}^{lit,+}
   \longrightarrow
   \mathsf A_{act}^{99,+}\cup\{\mathrm{tail},\mathrm{BTQ},\mathrm{zero}\}.
   ```

2. Compute or bound the projection norm \(\Pi_{act}^{99,+}\).

3. Decide which retained action rows are derivative-sourced and apply Lemma
   109.6 only to those rows.

4. Bound the same-shell inverse envelope \(O_{act}^{YM2}\).

5. Recompute \(A_{act,pass}^{99,+}\) and
   \(\Omega_{act}^{99,+}(\mathbf a)\), then rerun the zero-growth SCC test
   with action rows reinserted only where the literal or envelope source gate
   has actually passed.

This keeps the proof Barandes-aligned in the operational sense: all
quantities are same-record finite facts on the pushed-forward law, and no
continuum Yang-Mills measure, area law, or off-record stochastic kernel is
imported to close a finite row.

## 110. Over-Refined `YM2 -> act` Pushforward Carrier

Section 109 shows that `HK-SF-YM2` is an envelope source, not yet a literal
action row table.  This section pushes that envelope as far as the present
corpus permits.  It prints a finite carrier relation from the seven
Paper-16 `YM2` labels to the Section-104 action atoms and extracts a coarse
projection-norm bound.  The literal monomial selector remains open.

### Definition 110.1: Size Parameters For The Over-Refined Carrier

Let

```math
N_S^{99,+}:=|\mathsf S_{act}^{99,+}|,
\qquad
N_W^{99}:=|\mathsf W_{\le4}^{99}|,
\qquad
N_\Sigma^{99,+}:=|\Sigma_{99}^{+}|.
```

These are finite by Definitions 102.4 and 104.1.  Also set

```math
\Lambda_*^{99}=\{0,{1\over2},1\},
\qquad
I_v^{YM2}:=\{4,33,J2,gf2,cov2,rec2,norm2\}.
```

For a set of action kinds \(\mathcal K\subseteq\{\mathrm{plaq},
\mathrm{stencil},\mathrm{prod}\}\) and a representation set
\(\mathcal L\subseteq\Lambda_*^{99}\), define the finite action carrier

```math
\mathsf A_{act}^{99,+}(\mathcal K,\mathcal L)
:=
\{
(\kappa,S,w,\lambda,\upsilon)\in\mathsf A_{act}^{99,+}:
\kappa\in\mathcal K,\ \lambda\in\mathcal L
\}.
```

Its cardinality is bounded by

```math
\#\mathsf A_{act}^{99,+}(\mathcal K,\mathcal L)
\le
|\mathcal K|\,|\mathcal L|\,N_S^{99,+}N_W^{99}N_\Sigma^{99,+}.
```

This deliberately uses the over-refined support list.  It may count inactive
supports and physically equivalent representatives more than once, but it
never loses a possible same-record local action row.

### Definition 110.2: The YM2 Carrier Relation

Define the over-refined carrier relation

```math
\Pi_{YM2\to act}^{110,+}
\subset
I_v^{YM2}\times\overline V_{99}^{lit,+}
\times
\left(\mathsf A_{act}^{99,+}\cup
\{\mathrm{zero},\mathrm{carry}\}\right)
```

as follows.  For every vertex
\(\bar v\in\overline V_{99}^{lit,+}\):

1. The quartic local vertex label \(4\) is carried by the stencil carrier

   ```math
   \Pi_{YM2\to act}^{110,+}(4,\bar v)
   :=
   \mathsf A_{act}^{99,+}
   (\{\mathrm{stencil}\},\Lambda_*^{99}).
   ```

2. The cubic-cubic label \(33\) is carried by the product/stencil carrier

   ```math
   \Pi_{YM2\to act}^{110,+}(33,\bar v)
   :=
   \mathsf A_{act}^{99,+}
   (\{\mathrm{prod},\mathrm{stencil}\},\Lambda_*^{99}).
   ```

   The extra `stencil` option is intentional: Paper 16 records \(33\) as a
   connected local second-order ledger term after the covariance contraction,
   and the present paper has not printed a literal selector deciding whether
   each such contraction is stored as a product atom or as an effective local
   stencil atom.

3. The Jacobian quadratic label \(J2\) is carried by the neutral stencil
   carrier

   ```math
   \Pi_{YM2\to act}^{110,+}(J2,\bar v)
   :=
   \mathsf A_{act}^{99,+}
   (\{\mathrm{stencil}\},\{0\}).
   ```

   This is the same-record scalar Jacobian carrier.  If a later literal
   audit finds a non-neutral projected Jacobian channel, that row must be
   added explicitly and charged as an extension of this carrier, not silently
   imported here.

4. On the strict axial-tree, exact-covariance, connected/cumulant,
   minimal-record branch,

   ```math
   \Pi_{YM2\to act}^{110,+}(\ell,\bar v):=\{\mathrm{zero}\},
   \qquad
   \ell\in\{gf2,cov2,rec2,norm2\}.
   ```

   Outside that strict branch, these four labels are not pass rows.  They are
   assigned to `carry`:

   ```math
   \Pi_{YM2\to act}^{110,+}(\ell,\bar v):=\{\mathrm{carry}\},
   \qquad
   \ell\in\{gf2,cov2,rec2,norm2\}.
   ```

This is a carrier relation, not a literal row-value table.  To convert it to
a function, split each nonzero carrier set by an auxiliary finite index

```math
m\in\mathcal M_\ell^{110,+}(\bar v)
```

that names one element of the displayed carrier.  Then

```math
\pi_{YM2\to act}^{110,+}(\ell,\bar v,m)=\zeta_{\ell,\bar v,m}
```

for carrier atoms, and equals `zero` or `carry` in the corresponding strict
or nonstrict cases.

### Lemma 110.3: Same-Record Legality Of The Carrier

Every atom in \(\Pi_{YM2\to act}^{110,+}(\ell,\bar v)\) is an action atom of
Definition 104.1 on the same active pushed-forward `SEL2` scalar law as
\(\bar v\).  The carrier does not charge Paper-14 export, RP/Cov transport,
RPF, `KPdec`, `WP`, perimeter/cusp/readout, or comparison-battery debits.

Proof.

The carrier uses only \(\mathsf A_{act}^{99,+}\), which was defined from the
finite local stencil \(\mathsf Q_{loc}^{99}\), the retained word list
\(\mathsf W_{\le4}^{99}\), the retained representation list
\(\Lambda_*^{99}\), and the finite orientation/sector list \(\Sigma_{99}^+\).
These are all coordinates of the over-refined same-record finite row map.
No projective, covariance, Paper-14, whole-process, readout, or comparison
operation is performed by the carrier relation.  Optional labels are either
zero on the strict branch or carried outside it, so they are not spent twice.
`square`

### Definition 110.4: Coarse Projection Norm

On the strict optional-zero branch, define

```math
Q_{110}^{act,+}
:=
\max_{\bar v\in\overline V_{99}^{lit,+}}
\sum_{\ell\in\{4,33,J2\}}
\#\Pi_{YM2\to act}^{110,+}(\ell,\bar v).
```

By Definition 110.2,

```math
Q_{110}^{act,+}
\le
10\,N_S^{99,+}N_W^{99}N_\Sigma^{99,+}.
```

Indeed the quartic carrier contributes at most
\(3N_S^{99,+}N_W^{99}N_\Sigma^{99,+}\), the
cubic-cubic product/stencil carrier contributes at most
\(6N_S^{99,+}N_W^{99}N_\Sigma^{99,+}\), and the neutral Jacobian carrier
contributes at most \(N_S^{99,+}N_W^{99}N_\Sigma^{99,+}\).

The corresponding coarse projection norm is

```math
\Pi_{act}^{110,+}:=Q_{110}^{act,+}.
```

Outside the strict optional-zero branch, set

```math
Q_{110}^{act,+,nonstrict}:=Q_{110}^{act,+}
```

for pass-row purposes and carry the optional labels
\(gf2,cov2,rec2,norm2\) in their own ledgers.  They do not enlarge the pass
projection norm unless a later source theorem reclassifies one of them as a
same-record pass row.

### Corollary 110.5: Envelope Consequence For `ACTSRC+`

Assume `HK-SF-YM2` on the same pushed-forward finite law.  On the strict
optional-zero branch, Section 110 supplies the envelope pushforward gate

```math
\mathrm{P21\text{-}ACTSRC\text{-}PUSH\text{-}ENV}^{110,+}
```

with

```math
\Pi_{act}^{99,+}
\le
\Pi_{act}^{110,+}
\le
10\,N_S^{99,+}N_W^{99}N_\Sigma^{99,+}.
```

Consequently the YM2 envelope of Definition 109.4 may be taken in the coarse
form

```math
C_{act}^{YM2,min,110}
\le
\Pi_{act}^{110,+} C_v^{YM2,min}.
```

On the full nonminimal branch one may instead write

```math
C_{act}^{YM2,110}
\le
\Pi_{act}^{110,+} C_v^{YM2}
```

while carrying the optional labels until their same-record source theorem is
printed.

This is not yet a literal action-value source table:

```math
\mathrm{P21\text{-}ACTSRC\text{-}LIT}^{99,+}
\quad\text{does not follow.}
```

The remaining literal selector obstruction is

```math
\mathrm{PARK\text{-}ACTSRC\text{-}SEL}^{110,+},
```

the finite decision of which carrier atoms are actually produced by each
`HK-SF-YM2` local monomial on the active `SEL2` record.

Proof.

The carrier relation of Definition 110.2 contains every action atom licensed
by the three nonoptional `YM2` labels under the over-refined local stencil.
Definition 110.4 counts that carrier, giving the displayed projection norm.
The envelope estimate is Definition 109.4 with
\(\Pi_{act}^{99,+}\) replaced by the certified over-refined upper bound
\(\Pi_{act}^{110,+}\).  Since no row coefficient, derivative/product
classification, or same-shell inverse slot is evaluated here, the literal
source table is still not supplied. `square`

### Theorem 110.6: Updated `ACTSRC+` Status

After Section 110, the action-source obstruction has the following precise
shape.

Closed on the envelope branch:

```math
\mathrm{P21\text{-}ACTSRC\text{-}PUSH\text{-}ENV}^{110,+},
\qquad
\Pi_{act}^{99,+}
\le
10\,N_S^{99,+}N_W^{99}N_\Sigma^{99,+}.
```

Still open for executable action pass rows:

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}^{+}
=
\mathrm{PARK\text{-}ACTSRC\text{-}SEL}^{110,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ZC}^{99,+}.
}
```

Therefore Section 108's carried action completion remains forced for the
literal pass graph, but the envelope branch now has an explicit finite
projection surcharge.  The next action task is no longer "find a
pushforward"; it is to either:

1. print the literal selector
   \(\mathcal M_\ell^{110,+}(\bar v)\) and row values inside the carrier; or
2. accept the coarse bound
   \(\Pi_{act}^{110,+}C_v^{YM2,min}\) and test whether the reduced decay
   inequality can survive such a large over-refined surcharge.

Proof.

Corollary 110.5 proves the envelope pushforward and projection bound.
Definition 105.1 still requires row values, inverse slots, and zero/carry
classification before any action row becomes pass.  The carrier relation
also leaves open the literal selector deciding which over-refined atoms are
physically present.  These are exactly the four displayed residual source
gates. `square`

## 111. Coarse Action-Envelope Feasibility Test

Section 110 leaves a fork.  Either print the literal selector inside the
carrier, or accept the over-refined carrier as a coarse envelope and test the
reduced decay inequality with that surcharge.  This section performs the
second test.  The result is not a mathematical failure of the actual branch;
it is a failure of the coarse over-cover as a useful proof route unless a very
large reduced decay exponent is later supplied.

### Definition 111.1: Action Surcharge From The Coarse Carrier

Let

```math
B_{act}^{110}
:=
B_{act,s}^{99,+}B_{act,t}^{99,+}
```

be the source/target normal-form coefficient multiplier for action rows.  On
the strict exact structural convention \(B_{act}^{110}=1\).  Define the
coarse action coefficient base

```math
A_{act}^{110,env}
:=
\max\left(
1,\,
B_{act}^{110}\Pi_{act}^{110,+}C_v^{YM2,min}
\right)
```

on the strict minimal `HK-SF-YM2` branch.  The full nonminimal branch replaces
\(C_v^{YM2,min}\) by \(C_v^{YM2}\).

The corresponding logarithmic action surcharge is

```math
\delta_{act}^{110}
:=
\log A_{act}^{110,env}
=
\log^+\left(
B_{act}^{110}\Pi_{act}^{110,+}C_v^{YM2,min}
\right).
```

If the non-action rows have coefficient base \(A_{nonact}^{cert}\), then the
coarse-envelope coefficient side satisfies

```math
\log A_{esc}^{BTQ}
\le
\max\left(
\log A_{nonact}^{cert},
\delta_{act}^{110}
\right)
```

provided every action row admitted to the pass graph is sourced only through
the Section-110 YM2 envelope.  Thus the coarse sufficient reduced gate is

```math
m_{red}^{act}
>
\log C_{geom}^{cert}
+g_q^{cert}
+\max\left(
\log A_{nonact}^{cert},
\delta_{act}^{110}
\right).
```

This is a sufficient gate, not a necessary one, because
\(\Pi_{act}^{110,+}\) is an over-refined projection norm.

### Lemma 111.2: Literal Size Of The Coarse Projection Norm

For the \(\mathfrak P_{99}^{min}\) over-refined cover of Section 102,

```math
m_\Box=25444,
\qquad
|\mathsf H_\Box|=2m_\Box=50888.
```

The reduced-word list obeys the safe bound

```math
N_W^{99}
\le
\sum_{\ell=1}^{4}
50888(50887)^{\ell-1}
=
6705705274431562880.
```

Moreover

```math
N_S^{99,+}\le 2^{81}-1<2^{81},
\qquad
N_\Sigma^{99,+}=16.
```

Therefore Section 110 gives

```math
\Pi_{act}^{110,+}
\le
10\cdot 2^{81}\cdot 16
\cdot
6705705274431562880,
```

and hence

```math
\log \Pi_{act}^{110,+}
\le
104.57
```

in natural logarithms.

Proof.

Definition 102.1 gives \(m_\Box=25444\), so the oriented local word alphabet
has \(2m_\Box=50888\) letters.  A freely reduced word of length \(\ell\) has
at most \(50888(50887)^{\ell-1}\) representatives before the cyclic/inverse
quotient; quotienting can only reduce the count.  Summing \(\ell\le4\) gives
the displayed bound.  The local stencil \(\mathsf Q_{loc}^{99}\) has
\(3^4=81\) points, so the nonempty action-support list has at most
\(2^{81}-1\) members.  Definition 102.5 gives \(N_\Sigma^{99,+}=16\).
Substitution into Corollary 110.5 gives the projection bound; taking logs
gives \(104.5695\ldots\), rounded upward to \(104.57\). `square`

### Corollary 111.3: Best-Case Coarse Feasibility Target

Even in the artificially favorable case

```math
B_{act}^{110}=1,\qquad
A_{nonact}^{cert}=1,\qquad
C_{geom}^{cert}=1,\qquad
g_q^{cert}=0,
```

the coarse-envelope branch requires

```math
m_{red}^{act}
>
\log^+\left(\Pi_{act}^{110,+}C_v^{YM2,min}\right).
```

Using Lemma 111.2, a sufficient numerical target is

```math
m_{red}^{act}
>
\log^+ C_v^{YM2,min}+104.57.
```

With the actual non-action geometry, inverse, and normal-form factors
restored, the target becomes

```math
m_{red}^{act}
>
\log C_{geom}^{cert}
+g_q^{cert}
+\max\left(
\log A_{nonact}^{cert},
\log^+(B_{act}^{110}C_v^{YM2,min})+104.57
\right).
```

Thus the over-refined action envelope is only useful if the future reduced
decay source is strong enough to beat a coefficient surcharge of order
\(10^2\) in natural logarithmic units before the remaining finite growth
side is counted.

### Theorem 111.4: Coarse Envelope Is Not A Certified Survival Route

The current corpus does not certify that the reduced decay inequality can
survive the Section-110 coarse over-refined action surcharge.

More precisely:

1. the current papers do not source any positive numerical
   \(m_{red}^{act}\) for the active common \(E_{14}/X_{13}\) reduced tower;
2. the coarse action-envelope route requires at least the best-case threshold
   of Corollary 111.3;
3. no current source gives

   ```math
   m_{red}^{act}
   >
   \log^+ C_v^{YM2,min}+104.57;
   ```

4. therefore the coarse carrier cannot be spent as a certified pass route.

This is not a falsification of the actual `ACTSRC+` branch.  It is only a
falsification of the **blind over-cover spending strategy**:

```math
\text{spend all atoms in }
\Pi_{YM2\to act}^{110,+}
\text{ with no literal selector}.
```

Proof.

Items 1 and 3 are the current source verdict of Sections 87--88 and Section
109: no same-record reduced KP or direct reduced projection-tail theorem has
been supplied for \(m_{red}^{act}\).  Item 2 is Corollary 111.3.  Hence no
certified strict inequality can be formed.  Since
\(\Pi_{YM2\to act}^{110,+}\) is an over-cover, failure to certify with it
does not imply failure of the true smaller selector.  It only says that the
coarse envelope is too expensive to close the branch from the present
sources. `square`

### Corollary 111.5: Execution Verdict After The Coarse Test

After Sections 109--111, the action-source route is sharply ordered.

The following path is currently not productive:

```math
\mathrm{P21\text{-}ACTSRC\text{-}PUSH\text{-}ENV}^{110,+}
\quad\text{alone}
\quad\Longrightarrow\quad
\mathrm{P21\text{-}RED\text{-}INEQ}.
```

The next useful finite task is instead the literal selector:

```math
\mathrm{PARK\text{-}ACTSRC\text{-}SEL}^{110,+}
```

namely the row-by-row decision, inside
\(\Pi_{YM2\to act}^{110,+}\), of which atoms are actually produced by
\(4,33,J2\), which rows are derivative-sourced, which rows are pure product
rows, and which rows are exact zero or carried.

Only after that selector is printed should the paper recompute

```math
\Pi_{act}^{sharp},\qquad
A_{act,pass}^{sharp},\qquad
\Omega_{act}^{sharp}(\mathbf a),
```

and rerun the Section-108 SCC test with certified action rows reinserted.
The coarse projection norm remains useful as a safety bound, but not as the
intended pass mechanism.

## 112. Literal Selector Skeleton For The Nonoptional `YM2` Labels

Section 111 shows that the over-refined carrier is too large to be the main
proof route.  This section therefore attacks the literal selector.  The
current papers are strong enough to remove the wrong **kinds** of action
atoms and to define a sharply smaller monomial-selector package.  They are
not yet strong enough to print every monomial support, word, coefficient, and
inverse slot.

### Source Audit 112.1: What The Previous Papers Fix

Paper 16's `HK-SF-YM2` and Paper 20's active `SEL2` root audit fix the
nonoptional second-order labels as:

```math
\{4,33,J2\}.
```

Their meanings are:

| label | source meaning | strict action kind |
| --- | --- | --- |
| \(4\) | one quartic term from the BCH/Taylor expansion of the local YM action | local stencil |
| \(33\) | connected second cumulant of two cubic YM vertices, with the exponential centering already performed | connected effective local stencil |
| \(J2\) | quadratic Haar/log-chart/heat-parametrix Jacobian term | neutral scalar stencil |

The optional labels

```math
gf2,\quad cov2,\quad rec2,\quad norm2
```

are zero on the strict axial-tree, exact-covariance, connected/cumulant,
minimal-record branch, and carried outside that branch.  Thus they do not
enter the strict action pass selector.

### Definition 112.2: Monomial Selector Package

Define the monomial-selector package

```math
\mathcal U_{112}^{mon}
:=
\left(
\mathsf S_4^{112},\mathsf W_4^{112},\Sigma_4^{112},
\mathsf S_{33}^{112},\mathsf W_{33}^{112},\Sigma_{33}^{112},
\mathsf S_J^{112},\mathsf W_J^{112},\Sigma_J^{112}
\right).
```

Here:

```math
\mathsf S_\ell^{112}\subseteq\mathsf S_{act}^{99,+},
\qquad
\mathsf W_\ell^{112}\subseteq\mathsf W_{\le4}^{99},
\qquad
\Sigma_\ell^{112}\subseteq\Sigma_{99}^{+},
```

for \(\ell\in\{4,33,J\}\).  The intended meanings are:

1. \(\mathsf S_4^{112},\mathsf W_4^{112},\Sigma_4^{112}\) list the actual
   quartic local YM Taylor monomials in the active axial-tree chart.
2. \(\mathsf S_{33}^{112},\mathsf W_{33}^{112},\Sigma_{33}^{112}\) list the
   actual connected double-cubic cumulant monomials after the covariance
   contraction has been performed and centered.
3. \(\mathsf S_J^{112},\mathsf W_J^{112},\Sigma_J^{112}\) list the actual
   quadratic Haar/log-chart/heat-parametrix Jacobian monomials.

The current corpus proves these lists are finite: Paper 11 gives finite
block axial-tree charts and finite local Taylor/Jacobian derivative
constants; Paper 16 packages the surviving labels into the finite `YM2`
ledger; Paper 20 imports the same labels on the active `SEL2` scalar record.
The current corpus does **not** print the literal values of the lists above.

For cardinalities write

```math
n_4^{112}
:=
|\mathsf S_4^{112}|\,|\mathsf W_4^{112}|\,|\Sigma_4^{112}|,
```

```math
n_{33}^{112}
:=
|\mathsf S_{33}^{112}|\,|\mathsf W_{33}^{112}|\,|\Sigma_{33}^{112}|,
```

and

```math
n_J^{112}
:=
|\mathsf S_J^{112}|\,|\mathsf W_J^{112}|\,|\Sigma_J^{112}|.
```

### Definition 112.3: The Strict Kind-Level Selector

Assuming \(\mathcal U_{112}^{mon}\), define

```math
\mathfrak S_{YM2\to act}^{112}
=
\mathfrak S_4^{112}
\dot\cup
\mathfrak S_{33}^{112}
\dot\cup
\mathfrak S_J^{112}
```

as follows.

The quartic selector is

```math
\mathfrak S_4^{112}
:=
\left\{
(4,\zeta):
\zeta=(\mathrm{stencil},S,w,\lambda,\upsilon),\
S\in\mathsf S_4^{112},\
w\in\mathsf W_4^{112},\
\lambda\in\Lambda_*^{99},\
\upsilon\in\Sigma_4^{112}
\right\}.
```

The connected double-cubic selector is

```math
\mathfrak S_{33}^{112}
:=
\left\{
(33,\zeta):
\zeta=(\mathrm{stencil},S,w,\lambda,\upsilon),\
S\in\mathsf S_{33}^{112},\
w\in\mathsf W_{33}^{112},\
\lambda\in\Lambda_*^{99},\
\upsilon\in\Sigma_{33}^{112}
\right\}.
```

The Jacobian selector is

```math
\mathfrak S_J^{112}
:=
\left\{
(J2,\zeta):
\zeta=(\mathrm{stencil},S,w,0,\upsilon),\
S\in\mathsf S_J^{112},\
w\in\mathsf W_J^{112},\
\upsilon\in\Sigma_J^{112}
\right\}.
```

Thus \(4\) and \(33\) may project to any retained
\(\lambda\in\{0,{1\over2},1\}\), but \(J2\) is neutral in the strict scalar
Jacobian convention.

### Lemma 112.4: Kind Eliminations

On the strict axial-tree, exact-covariance, connected/cumulant,
minimal-record branch:

```math
4\not\to\mathrm{prod},\qquad
4\not\to\mathrm{plaq},
```

```math
33\not\to\mathrm{prod},\qquad
33\not\to\mathrm{plaq},
```

and

```math
J2\not\to\mathrm{prod},\qquad
J2\not\to\mathrm{plaq},\qquad
J2\not\to\lambda\ne0.
```

Proof.

Paper 20 identifies the nonabsorbed second-order root labels in the active
axial-tree chart.  The label \(4\) is one quartic Taylor/BCH local YM
insertion after the heat-kernel time tangent has been absorbed; in the
Section-104 action typing this is a local coordinate stencil, not a product
of two retained action atoms and not the raw plaquette time coordinate.  The
label \(33\) is the connected second cumulant of two cubic terms after
exponential centering and covariance contraction.  On the connected/cumulant
branch it is recorded as the resulting connected effective local stencil; if
one refuses that connected-cumulant realization, the row must be carried, not
spent as a pure product pass row.  The label \(J2\) is the quadratic
Haar/log-chart/heat-parametrix Jacobian term.  It is a scalar Jacobian
stencil, so it is neither a product nor a plaquette action row, and under the
strict scalar Jacobian convention it carries the neutral representation
label \(\lambda=0\). `square`

### Corollary 112.5: Sharp Selector Projection Norm

If the monomial selector package \(\mathcal U_{112}^{mon}\) is supplied, the
strict selector projection norm obeys

```math
\Pi_{act}^{112,sel}
\le
3n_4^{112}+3n_{33}^{112}+n_J^{112}.
```

Consequently the strict minimal YM2 envelope sharpens from Section 110's
over-refined bound to

```math
C_{act}^{YM2,min,112}
\le
\Pi_{act}^{112,sel}C_v^{YM2,min}.
```

Proof.

The quartic selector has one copy for each retained representation
\(\lambda\in\Lambda_*^{99}\), hence at most \(3n_4^{112}\) atoms.  The
connected double-cubic selector has the same representation count, hence at
most \(3n_{33}^{112}\) atoms.  The Jacobian selector is neutral, hence
contributes only \(n_J^{112}\) atoms.  Lemma 112.4 deletes all other kind
branches.  Definition 109.4 then gives the envelope bound. `square`

### Theorem 112.6: Selector Status After The Kind-Level Audit

Section 112 closes the kind-level selector and replaces the coarse
projection-norm target by the monomial-selector target

```math
\Pi_{act}^{112,sel}
\le
3n_4^{112}+3n_{33}^{112}+n_J^{112}.
```

However, it does not close `ACTSRC+`, because the literal monomial package
\(\mathcal U_{112}^{mon}\), the row values, and the inverse slots are still
unprinted.  The updated action-source obstruction is therefore

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}^{+}
=
\mathrm{PARK\text{-}ACTSRC\text{-}MON}^{112,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ZC}^{99,+}.
}
```

Here `MON` means the finite lists
\(\mathsf S_\ell^{112},\mathsf W_\ell^{112},\Sigma_\ell^{112}\) for
\(\ell\in\{4,33,J\}\).  The previous selector obstruction
\(\mathrm{PARK\text{-}ACTSRC\text{-}SEL}^{110,+}\) is reduced to this
monomial print.

Proof.

Source Audit 112.1 and Lemma 112.4 identify the allowed kinds and eliminate
the impossible branches.  Corollary 112.5 gives the sharp conditional
projection norm.  But Definition 112.2 explicitly records that the actual
finite monomial support, word, and sector lists are not printed in the
current corpus.  Definition 105.1 still requires row values and inverse
slots before action rows become pass rows.  Hence the displayed four-source
park is exact. `square`

### Corollary 112.7: Next Concrete Print

The next concrete finite print is no longer the whole action carrier.  It is
the much smaller monomial package

```math
\mathcal U_{112}^{mon}
=
\left(
\mathsf S_4^{112},\mathsf W_4^{112},\Sigma_4^{112},
\mathsf S_{33}^{112},\mathsf W_{33}^{112},\Sigma_{33}^{112},
\mathsf S_J^{112},\mathsf W_J^{112},\Sigma_J^{112}
\right).
```

Once that package is printed, Paper 21 can compute

```math
\Pi_{act}^{112,sel},
\qquad
A_{act}^{112,env},
\qquad
\delta_{act}^{112}
:=
\log^+\left(
B_{act}^{110}\Pi_{act}^{112,sel}C_v^{YM2,min}
\right),
```

and decide whether the action source is still too expensive or whether it is
worth attacking `ROWVAL`, `INV`, and `ZC` next.

## 113. Root Monomial Alphabet And Coupled Support Lists

Section 112 reduces the action selector to the actual monomials behind the
three nonoptional labels \(4,33,J2\).  This section prints the finite
root-coordinate alphabet and replaces the product-list count
\(|\mathsf S_\ell||\mathsf W_\ell||\Sigma_\ell|\) by a coupled monomial graph.
This is the correct finite object: a monomial chooses its support, word, and
sector simultaneously.

### Definition 113.1: Root Axial-Tree Coordinate Alphabet

Fix one active `SEL2` root template on the strict axial-tree branch.  Let
\(\mathsf E_{root}^{113}\) be the finite list of non-tree root link
coordinates in the root battery after the tree links have been set to the
identity, exactly as in the block axial-tree gauge of Paper 11 and the
`SEL2` root census of Paper 20.  Choose a fixed orthonormal basis
\((T_1,T_2,T_3)\) of \(\mathfrak{su}(2)\).  Define the root coordinate
alphabet

```math
\mathsf X_{root}^{113}
:=
\mathsf E_{root}^{113}\times\{1,2,3\},
```

and set

```math
n_A^{113}:=|\mathsf X_{root}^{113}|=3|\mathsf E_{root}^{113}|.
```

For \(x=(e,a)\in\mathsf X_{root}^{113}\), let
\(\operatorname{supp}_{root}(x)\subseteq\mathsf Q_{loc}^{99}\) be the rooted
local support touched by the tree-gauge reconstruction of the coordinate
\(e\), including the finite fundamental surface used in the axial-tree
chart.  This support map is finite because the root battery and the tree
paths are finite.

Let

```math
\operatorname{Sym}^d(\mathsf X_{root}^{113})
:=
\{\nu:\mathsf X_{root}^{113}\to\mathbb N:\sum_x\nu(x)=d\}
```

be the finite set of degree-\(d\) symmetric coordinate monomials.  Hence

```math
|\operatorname{Sym}^d(\mathsf X_{root}^{113})|
=
\binom{n_A^{113}+d-1}{d}.
```

### Definition 113.2: Derivative-Tensor Monomial Sets

Let \(S_{loc}^{YM}\) be the local heat-kernel/Yang-Mills action density in
the active root axial-tree coordinates after the quadratic Gaussian and
heat-time tangent have been extracted.  Let \(J_{root}\) be the corresponding
Haar/log-chart/heat-parametrix Jacobian density.

Define the quartic monomial set

```math
\mathfrak M_4^{113}
:=
\{\nu\in\operatorname{Sym}^4(\mathsf X_{root}^{113}):
D^\nu S_{loc}^{YM}(0)\ne0\}.
```

Define the cubic monomial set

```math
\mathfrak M_3^{113}
:=
\{\nu\in\operatorname{Sym}^3(\mathsf X_{root}^{113}):
D^\nu S_{loc}^{YM}(0)\ne0\}.
```

Define the Jacobian quadratic monomial set

```math
\mathfrak M_J^{113}
:=
\{\nu\in\operatorname{Sym}^2(\mathsf X_{root}^{113}):
D^\nu\log J_{root}(0)\ne0\}.
```

The current corpus proves these are finite but does not print their literal
members.  The safe cardinality bounds are

```math
|\mathfrak M_4^{113}|\le\binom{n_A^{113}+3}{4},
```

```math
|\mathfrak M_3^{113}|\le\binom{n_A^{113}+2}{3},
```

and

```math
|\mathfrak M_J^{113}|\le\binom{n_A^{113}+1}{2}.
```

### Definition 113.3: Connected Double-Cubic Pairing Set

Let

```math
\mathfrak W_6^{conn}
```

be the finite set of Wick pairing patterns on six labeled cubic legs that
are connected between the two cubic vertices.  Use the safe bound

```math
|\mathfrak W_6^{conn}|\le15,
```

the total number of pairings of six labeled legs.

The connected double-cubic monomial set is

```math
\mathfrak M_{33}^{113}
:=
\{(\nu_1,\nu_2,\pi):
\nu_1,\nu_2\in\mathfrak M_3^{113},\
\pi\in\mathfrak W_6^{conn},\
\pi\text{ is root-local for the declared covariance selector}\}.
```

If the root-local covariance selector is not supplied, the corresponding
entries are not pass rows; they remain in
\(\mathrm{PARK\text{-}ACTSRC\text{-}COVPAIR}^{113,+}\).  With the selector,

```math
|\mathfrak M_{33}^{113}|
\le
15|\mathfrak M_3^{113}|^2
\le
15\binom{n_A^{113}+2}{3}^{2}.
```

This is still conservative: for a fully cross-connected cubic-cubic
cumulant, the number of pairings is smaller than 15, but the bound is enough
for a same-record certificate.

### Definition 113.4: Coupled Support/Word/Sector Graphs

For a coordinate monomial \(\nu\), define its local support by

```math
S(\nu)
:=
\bigcup_{x:\nu(x)>0}\operatorname{supp}_{root}(x)
\subseteq\mathsf Q_{loc}^{99}.
```

Let \(w(\nu)\in\mathsf W_{\le4}^{99}\) be the finite trace/coordinate word
obtained by applying the tree-gauge reconstruction to the monomial and then
taking the paired-real cyclic representative used in Definition 102.2.  For
the connected double-cubic element \(m=(\nu_1,\nu_2,\pi)\), set

```math
S(m):=S(\nu_1)\cup S(\nu_2)\cup S_{\rm cov}(\pi),
```

where \(S_{\rm cov}(\pi)\) is the finite root-local covariance support
selected by \(\pi\), and let \(w(m)\) be the corresponding connected
paired-real trace word.

On the strict scalar branch, all three nonoptional labels use the single
sector

```math
\sigma_{scal}^{113}
\in\Sigma_{99}^{+}.
```

Orientation, reflection, and center signs are stored in the row coefficient;
they are not additional sector branches for the central scalar selector.

Define the coupled graphs

```math
\mathfrak G_4^{113}
:=
\{(S(\nu),w(\nu),\sigma_{scal}^{113}):
\nu\in\mathfrak M_4^{113}\},
```

```math
\mathfrak G_J^{113}
:=
\{(S(\nu),w(\nu),\sigma_{scal}^{113}):
\nu\in\mathfrak M_J^{113}\},
```

and

```math
\mathfrak G_{33}^{113}
:=
\{(S(m),w(m),\sigma_{scal}^{113}):
m\in\mathfrak M_{33}^{113}\}.
```

Set

```math
n_4^{113}:=|\mathfrak G_4^{113}|,
\qquad
n_{33}^{113}:=|\mathfrak G_{33}^{113}|,
\qquad
n_J^{113}:=|\mathfrak G_J^{113}|.
```

These coupled counts replace the product counts of Definition 112.2.

### Lemma 113.5: Coupled Monomial Counts

On the strict scalar root branch with root-local covariance selector,

```math
n_4^{113}
\le
\binom{n_A^{113}+3}{4},
```

```math
n_{33}^{113}
\le
15\binom{n_A^{113}+2}{3}^{2},
```

and

```math
n_J^{113}
\le
\binom{n_A^{113}+1}{2}.
```

Proof.

The maps \(\nu\mapsto(S(\nu),w(\nu),\sigma_{scal}^{113})\) and
\(m\mapsto(S(m),w(m),\sigma_{scal}^{113})\) may identify different monomials,
but they cannot create more graph elements than their domains.  The domain
cardinalities are the bounds in Definitions 113.2 and 113.3. `square`

### Corollary 113.6: Polynomial Action Selector Norm

With the coupled monomial package of Definition 113.4,

```math
\Pi_{act}^{113,mon}
\le
3n_4^{113}+3n_{33}^{113}+n_J^{113}.
```

Consequently

```math
\boxed{
\Pi_{act}^{113,mon}
\le
3\binom{n_A^{113}+3}{4}
+45\binom{n_A^{113}+2}{3}^{2}
+\binom{n_A^{113}+1}{2}.
}
```

Thus the selector surcharge is polynomial in the number of root coordinates,
not exponential in the over-refined word and support cover of Section 111.

### Theorem 113.7: Updated Monomial-Selector Status

Section 113 closes the root monomial alphabet and gives a computable
polynomial envelope for the strict action selector.  It reduces
\(\mathrm{PARK\text{-}ACTSRC\text{-}MON}^{112,+}\) to the following concrete
finite tables:

```math
\mathrm{PARK\text{-}ACTSRC\text{-}DTENS}^{113,+}
```

for the nonzero derivative tensors
\(\mathfrak M_4^{113},\mathfrak M_3^{113},\mathfrak M_J^{113}\);

```math
\mathrm{PARK\text{-}ACTSRC\text{-}COVPAIR}^{113,+}
```

for the root-local connected Wick/covariance pairings entering
\(\mathfrak M_{33}^{113}\); and

```math
\mathrm{PARK\text{-}ACTSRC\text{-}ROOTCOUNT}^{113,+}
```

for the literal number \(n_A^{113}\) on each active root template, if a
numerical surcharge is desired.

The full action-source obstruction is now

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}^{+}
=
\mathrm{PARK\text{-}ACTSRC\text{-}DTENS}^{113,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}COVPAIR}^{113,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ZC}^{99,+}.
}
```

If only an envelope is needed, `ROOTCOUNT` plus the polynomial bound in
Corollary 113.6 is enough to test the action surcharge.  If pass rows are to
be inserted literally, `DTENS`, `COVPAIR`, `ROWVAL`, `INV`, and `ZC` must all
be supplied on the same pushed-forward law.

Proof.

Definitions 113.1--113.4 construct the finite coordinate alphabet, derivative
monomial sets, connected double-cubic pairings, and coupled support/word
graphs from the same root axial-tree chart used in Papers 11, 16, and 20.
Lemma 113.5 and Corollary 113.6 give the polynomial selector envelope.  What
remains unprinted are exactly the nonzero derivative tensors, covariance
pairings, row values, inverse slots, and zero/carry classifications. `square`

### Corollary 113.8: Next Numerical Test

The next numerical action-source test is to compute or bound
\(n_A^{113}\) for the actual active root template and insert it into

```math
\Pi_{act}^{113,mon}
\le
3\binom{n_A^{113}+3}{4}
+45\binom{n_A^{113}+2}{3}^{2}
+\binom{n_A^{113}+1}{2}.
```

The corresponding strict minimal action surcharge is

```math
\delta_{act}^{113}
:=
\log^+\left(
B_{act}^{110}
\Pi_{act}^{113,mon}
C_v^{YM2,min}
\right).
```

If this polynomial surcharge is still too large, the proof must print the
actual derivative tensors and covariance pairings rather than use the
polynomial envelope.  If it is small enough to leave a possible margin, the
next step is to attack `ROWVAL` and `INV` for the surviving monomial rows.

## 114. Root-Coordinate Count And Polynomial Surcharge Test

Section 113 reduces the action-selector surcharge to a polynomial in
\(n_A^{113}\).  This section bounds \(n_A^{113}\) for the actual active root
template convention currently printed in the finite table: the Section-102
over-refined local stencil with strict axial-tree gauge and scalar records.

### Definition 114.1: Active Root Stencil Graph

Use the active root local stencil already fixed in Section 102:

```math
\mathsf Q_{loc}^{99}=\{-1,0,1\}^4.
```

Its vertex count is

```math
V_{loc}^{99}=|\mathsf Q_{loc}^{99}|=3^4=81.
```

Let \(E_{loc}^{99,+}\) be the set of positively oriented unit lattice links
contained in this \(3\times3\times3\times3\) stencil.  In each of four
directions there are \(3-1\) edges along that direction and \(3^3\) choices
of the transverse coordinates, hence

```math
|E_{loc}^{99,+}|
=
4(3-1)3^3
=216.
```

The strict axial-tree root convention chooses a spanning tree in the
connected root stencil and uses the corresponding tree links as gauge-fixing
coordinates.  The surviving root coordinates are the non-tree links, each
with three \(\mathfrak{su}(2)\) components.

### Lemma 114.2: Root Coordinate Bound

On the full connected Section-102 root stencil, the number of non-tree root
links satisfies

```math
|\mathsf E_{root}^{113}|
\le
|E_{loc}^{99,+}|-(V_{loc}^{99}-1)
=216-80
=136.
```

Consequently

```math
\boxed{
n_A^{113}\le3\cdot136=408.
}
```

If the active root battery is literally the full Section-102 positive-link
stencil, then this count is exact for any spanning axial tree.  If the active
root battery is a connected subtemplate, the same formula applied to that
subgraph gives a no-larger cycle-rank count under the full-stencil
convention.  If one refuses the connected axial-tree reduction and carries
all positive links as possible root coordinates, the unconditional
cover-based fallback is

```math
n_A^{113}\le3|E_{loc}^{99,+}|=648.
```

Proof.

A connected graph with \(V\) vertices and \(E\) positively oriented links has
a spanning tree with \(V-1\) tree links, so axial-tree gauge leaves at most
\(E-(V-1)\) non-tree link coordinates.  The full Section-102 stencil has
\(V=81\) and \(E=216\).  Multiplication by \(3\) accounts for the fixed
orthonormal basis of \(\mathfrak{su}(2)\).  The fallback bound simply keeps
all positive links before tree elimination. `square`

### Corollary 114.3: Polynomial Selector Surcharge

Inserting \(n_A^{113}\le408\) into Corollary 113.6 gives

```math
\Pi_{act}^{113,mon}
\le
3\binom{411}{4}
+45\binom{410}{3}^{2}
+\binom{409}{2}.
```

Thus

```math
\boxed{
\Pi_{act}^{113,mon}
\le
5{,}851{,}199{,}818{,}721{,}526
}
```

and

```math
\boxed{
\log\Pi_{act}^{113,mon}\le36.31.
}
```

Under the all-positive-link fallback \(n_A^{113}\le648\),

```math
\log\Pi_{act}^{113,mon}\le39.08.
```

Proof.

This is direct arithmetic in the polynomial envelope

```math
3\binom{n_A^{113}+3}{4}
+45\binom{n_A^{113}+2}{3}^{2}
+\binom{n_A^{113}+1}{2}.
```

For \(n_A^{113}=408\), the value is
\(5{,}851{,}199{,}818{,}721{,}526\), whose natural logarithm is less than
\(36.31\).  For \(n_A^{113}=648\), the natural logarithm is less than
\(39.08\). `square`

### Theorem 114.4: Surcharge Test Against The Reduced Inequality

On the connected strict root branch, the action-source selector part of the
carried surcharge obeys the safe sufficient bound

```math
\delta_{act}^{114}
\le
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31.
```

Under the fallback all-link cover, replace \(36.31\) by \(39.08\).

Therefore the reduced decay inequality can survive the polynomial
action-selector envelope only if the active reduced mass source eventually
beats the certified non-action geometry and the action surcharge, for
example by the sufficient same-record condition

```math
m_{red}^{act}
>
\log C_{geom}^{cert}
+g_q^{cert}
+\max\!\left\{
\log A_{nonact}^{cert},
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31
\right\}.
```

The current corpus still does not supply this positive numerical
\(m_{red}^{act}\) margin.  Section 114 therefore does not prove the reduced
decay inequality; it proves that the root-count part of the action surcharge
is polynomial and numerically far below the coarse Section-111 over-cover.
Compared with the Section-111 coarse bound
\(\log\Pi_{act}^{110,+}\le104.57\), the connected root polynomial envelope
saves at least

```math
104.57-36.31=68.26
```

natural-log units.  That is a real finite-combinatorial gain, but not yet a
same-record decay certificate.

Proof.

Since \(\Pi_{act}^{113,mon}\ge1\),

```math
\log^+\!\left(
B_{act}^{110}C_v^{YM2,min}\Pi_{act}^{113,mon}
\right)
\le
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)
+\log\Pi_{act}^{113,mon}.
```

Corollary 114.3 gives the strict and fallback values of the last term.  The
displayed reduced inequality is the corresponding same-record survival
condition after adding the already certified non-action geometry and
quantum-growth terms. `square`

### Corollary 114.5: Updated Action-Source Ledger

The root-count part of the monomial selector is now bounded:

```math
\mathrm{PARK\text{-}ACTSRC\text{-}ROOTCOUNT}^{113,+}
\longrightarrow
\mathrm{ROOTCOUNT\text{-}BD}^{114}
\quad
(n_A^{113}\le408).
```

The remaining action-source obstruction is

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}^{+}
=
\mathrm{PARK\text{-}ACTSRC\text{-}DTENS}^{113,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}COVPAIR}^{113,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{99,+}
+\mathrm{PARK\text{-}ACTSRC\text{-}ZC}^{99,+}.
}
```

The next derivative-table decision is now honest.  If an independent source
can plausibly give

```math
m_{red}^{act}
\gtrsim
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31
```

after non-action debits, then the full derivative tensor and covariance-pair
table should be printed.  If no such source can be found, the obstruction has
moved from combinatorics to analytic decay: no amount of further finite
selector bookkeeping will by itself close the strict branch.

## 115. Exact Analytic Margin After The Polynomial Action Surcharge

Section 114 makes the action-selector part finite and polynomial.  This
section freezes the exact primitive reduced-decay target that remains.  The
purpose is to decide, before printing the full derivative tensor table,
whether the table could plausibly close the branch or whether the real
obstruction has already moved to analytic decay.

### Definition 115.1: Current Coefficient-Growth Threshold

Work on the connected strict root branch of Section 114, with the same
minimal `HK-SF-YM2` pushed-forward law.  Define the current action coefficient
threshold

```math
G_{act}^{115}
:=
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31.
```

Define the non-action coefficient threshold

```math
G_{nonact}^{115}
:=
\log A_{nonact}^{cert}.
```

Define the finite table and inverse threshold

```math
G_{table}^{115}
:=
\log C_{geom}^{cert}+g_q^{cert}.
```

The current primitive reduced-decay target is

```math
\boxed{
\Theta_{red}^{115}
:=
G_{table}^{115}
+\max\{G_{nonact}^{115},G_{act}^{115}\}.
}
```

Equivalently,

```math
\boxed{
\Theta_{red}^{115}
=
\log C_{geom}^{cert}+g_q^{cert}
+\max\!\left\{
\log A_{nonact}^{cert},
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31
\right\}.
}
```

Under the all-positive-link fallback of Lemma 114.2, replace \(36.31\) by
\(39.08\).

### Lemma 115.2: Primitive Reduced-Decay Pass Criterion

If the primitive reduced decay route is used, then the strict branch passes
the current action-envelope test only if a same-record source supplies

```math
\boxed{
m_{red}^{act}>\Theta_{red}^{115}.
}
```

If the reduced KP route is used, this means

```math
\mu_{red}^{act}c_{size}^{act}>\Theta_{red}^{115}.
```

If the one-step KP/cycle-ratio route of Sections 94--96 is used, this means

```math
\mu_0\chi_{cyc}c_{size}^{act}
-\lambda_{sem}
>
\Theta_{red}^{115}.
```

If instead the shell-direct route
`P21-RED-DPT_shell(delta)` is proved with \(\delta>0\), then
\(\Theta_{red}^{115}\) is not charged again, because that theorem already
includes the coefficient, branching, and inverse amplification.

Proof.

Theorem 93.4 and Corollary 93.5 say that a primitive reduced decay exponent
must dominate the coefficient base, path branching, and inverse amplification.
Section 111 packages those terms as
\(\log C_{geom}^{cert}+g_q^{cert}+\max\{\log A_{nonact}^{cert},
\delta_{act}\}\).  Section 114 replaces the coarse action surcharge
\(\delta_{act}^{110}\) by the polynomial connected-root bound
\(\log^+(B_{act}^{110}C_v^{YM2,min})+36.31\).  Substitution gives
\(\Theta_{red}^{115}\).  The reduced KP and one-step KP forms are just the
definitions of \(m_{red}^{act}\) in Sections 93--96.  The shell-direct
exception is Corollary 93.5's no-double-charge rule. `square`

### Corollary 115.3: Best-Case Lower Target

Even under the artificially favorable strict conventions

```math
B_{act}^{110}=1,\qquad
A_{nonact}^{cert}=1,\qquad
C_{geom}^{cert}=1,\qquad
g_q^{cert}=0,
```

the connected-root polynomial branch still requires

```math
\boxed{
m_{red}^{act}>\log^+\!\left(C_v^{YM2,min}\right)+36.31.
}
```

Under the fallback all-link cover, the best-case target is

```math
m_{red}^{act}>\log^+\!\left(C_v^{YM2,min}\right)+39.08.
```

Thus the derivative tensor table is worth printing only if it is expected to
reduce the action coefficient threshold below \(G_{act}^{115}\), or if a
same-record analytic source can plausibly exceed this target.

Proof.

Set the four favorable constants to their displayed values in Definition
115.1.  Then \(G_{table}^{115}=0\), \(G_{nonact}^{115}=0\), and
\(G_{act}^{115}=\log^+C_v^{YM2,min}+36.31\). `square`

### Theorem 115.4: Current Margin Verdict

The current papers do not prove

```math
m_{red}^{act}>\Theta_{red}^{115}.
```

They also do not prove the shell-direct alternative
`P21-RED-DPT_shell(delta)` with \(\delta>0\).  Therefore the strict branch
remains parked at a source obstruction, not at a remaining combinatorial
root-count obstruction.

More precisely:

1. Paper 16 supplies the finite `HK-SF-YM2` local vertex envelope and the
   finite constant \(C_v^{YM2,min}\), but not a numerical value small enough
   to discharge Corollary 115.3.
2. Paper 20 supplies the active `SEL2` scalar row freeze and the same-record
   heat-kernel comparison scaffolding, but not the reduced common
   \(E_{14}/X_{13}\) primitive decay rate \(m_{red}^{act}\).
3. Sections 93--96 define valid same-record routes to \(m_{red}^{act}\), but
   the current finite certificate still lacks the row values, inverse slots,
   and one-step KP constants needed to evaluate them.
4. Section 114 proves that the root-count surcharge is only \(36.31\) log
   units on the connected strict branch; it does not create analytic decay.

Hence the next proof-producing move is not another coarse finite envelope.
It is one of:

```math
\mathrm{P21\text{-}RED\text{-}DPT}_{prim}(m_{red}^{act})
\quad\text{with }m_{red}^{act}>\Theta_{red}^{115},
```

```math
\mathrm{P21\text{-}RED\text{-}DPT}_{shell}(\delta)
\quad\text{with }\delta>0,
```

or a literal derivative/row-value/inverse table that lowers
\(G_{act}^{115}\) enough to make a known same-record analytic source viable.

Proof.

The negative source statements are the audits in Sections 93--96, 109, and
114, together with Paper 20's terminal status: the corpus has finite
same-record scaffolding but no theorem proving the required primitive reduced
tail decay.  The alternatives listed are exactly Lemma 115.2 and Corollary
93.5. `square`

### Corollary 115.5: Immediate Work Order

After Section 115, the next work should be ordered as follows.

1. Try to source \(m_{red}^{act}\) directly from a full-law or degree-tail
   theorem on the same finite `SEL2` scalar law.
2. If no such source exists, print enough of `DTENS` and `COVPAIR` to replace
   \(36.31\) by the actual derivative-table surcharge.
3. Then print `ROWVAL`, `INV`, and `ZC` only for the rows that survive the
   literal derivative/covariance selector.
4. Recompute \(\Theta_{red}\) with those literal values and rerun the
   reduced pass/SCC test.

This order is intentionally conservative: analytic decay is the scarce
resource, so finite tables should be printed only when they either reduce
\(\Theta_{red}^{115}\) or supply the same-record constants entering
\(m_{red}^{act}\).

## 116. Source Audit For \(m_{red}^{act}\)

Section 115 identifies the exact threshold.  This section audits possible
sources for the numerator \(m_{red}^{act}\).  The rule is strict:
\(m_{red}^{act}\) must be a same-record decay exponent for the active reduced
common \(E_{14}/X_{13}\) forced tower, after the bounded-collar
`BTQ/ACTFULLLAW` records have been handled and after all no-double-charge
exclusions have been imposed.

### Definition 116.1: What Counts As A Source

A valid source for \(m_{red}^{act}\) is one of the following.

1. **Primitive direct reduced tail.**

   ```math
   \mathrm{P21\text{-}RED\text{-}DPT}_{prim}(m_{red}^{act})
   ```

   on the active reduced forced records of Definition 93.2.

2. **Reduced KP plus finite growth.**

   ```math
   \mathrm{P21\text{-}RED\text{-}1KP}
   (\mu_0,\lambda_{sem},\alpha_0,C_0)
   +
   \mathrm{P21\text{-}RED\text{-}COVER}(\chi_{dec},b_{dec})
   +
   \mathrm{P21\text{-}RED\text{-}SIZE}(c_{size}^{act}),
   ```

   which gives

   ```math
   m_{red}^{act}
   =
   \mu_0\chi_{dec}c_{size}^{act}-\lambda_{sem}
   ```

   when the right-hand side is positive.

3. **Shell-direct theorem.**

   ```math
   \mathrm{P21\text{-}RED\text{-}DPT}_{shell}(\delta),
   \qquad \delta>0.
   ```

   This does not define a primitive \(m_{red}^{act}\); it bypasses the
   primitive margin because the finite coefficient, branching, and inverse
   growth have already been paid inside the shell estimate.

Everything else is auxiliary.  In particular, `BTQ-FULLLAW`,
`BTQ-DEGTAIL`, `RED-CMSSI`, projective compatibility, and loop
renormalization can lower or define the growth side, but they do not by
themselves create \(m_{red}^{act}\).

### Lemma 116.2: Projective And Loop-Readout Sources Do Not Produce \(m_{red}^{act}\)

Papers 10--12 do not supply \(m_{red}^{act}\).

Proof.

Paper 10 proves a finite-battery non-Abelian cutoff and projective transport
framework.  Its honest boundary explicitly leaves open continuum
Yang-Mills existence, an unconditional same-record whole-process tower,
projective tightness and uniqueness, mass gap, Wilson-loop area law, and
confinement.  These results are essential for record discipline, but they do
not estimate the reduced common \(E_{14}/X_{13}\) forced-tail seminorm of
Definition 93.1.

Paper 11 supplies local-RG and AF/KP mechanisms under stated finite-row
source hypotheses.  It does not automatically identify those mechanisms with
the active reduced common forced tower; Section 78 already records that the
linear collar-distance route fails and must be replaced by a reduced KP or
direct projection-tail theorem.

Paper 12 supplies renormalized loop-readout, smearing, perimeter/cusp, and
finite-loop-battery control.  Those estimates are readout/renormalization
ledgers, not a primitive same-record decay bound for the reduced
\(E_{14}/X_{13}\) forced records.  Using them as \(m_{red}^{act}\) would
import a Wilson-loop area-law or confinement conclusion upstream of the
surface proof. `square`

### Lemma 116.3: Paper 20 Coefficient Sources Do Not Produce \(m_{red}^{act}\)

Paper 20's `SEL2` coefficient, block-time, escape-mass, and tree-rate
sources do not by themselves supply \(m_{red}^{act}\).

Proof.

Paper 20 freezes the active scalar row and develops one-plaquette/block
coefficient estimates for the surface rate gate.  These estimates concern
objects such as \(a_{\rho,j}^{SEL2}\), \(T_j^{SEL2,conv}\), escape mass of a
plaquette marginal, and the Paper-13 surface coefficient rate.  The reduced
forced-tail object in Section 93 is different: it is an all-depth tower of
new reduced records generated by the common \(E_{14}/X_{13}\) bypass after
bounded-collar contraction.  A positive one-block coefficient rate or
nonidentity plaquette escape mass does not imply exponential decay of this
all-depth reduced forced-tail seminorm.  Therefore Paper 20 supplies
compatible scalar scaffolding and no-smuggling discipline, but not
\(\mathrm{P21\text{-}RED\text{-}DPT}_{prim}\),
\(\mathrm{P21\text{-}RED\text{-}1KP}\), or
\(\mathrm{P21\text{-}RED\text{-}DPT}_{shell}\). `square`

### Definition 116.4: Paper-16 Reduced-KP Transfer Package

The only existing source technology in the corpus that can plausibly become
\(m_{red}^{act}\) is the clean finite-template analytic worksheet of Paper
16.  Define

```math
\mathrm{P21\text{-}RED\text{-}KP16\text{-}XFER}
(\mu_0,\lambda_{sem})
```

to be the following same-record package.

1. **Row-local clean analytic data.**  For every decay-eligible reduced row
   \(e\in\mathcal E_{dec}\), the Paper-16 certificate
   `HK-AN-FINTPL-CLOSE(m_e)` holds on the same active pushed-forward
   `SEL2` law, with finite row data

   ```math
   \Delta_B,L_{ent},L_{KP},\lambda_D,R_{blk},
   C_v^{row},r_{res}^{clean},m_e.
   ```

2. **Uniform decay lower bound.**  The row-local exported residual margins
   \(\Delta_{res}(e)\) have a positive common lower bound:

   ```math
   \mu_0
   \le
   \inf_{e\in\mathcal E_{dec}}\Delta_{res}(e),
   \qquad
   \mu_0>0.
   ```

3. **Seminorm transfer.**  The canonical reduced seminorm
   \(\mathcal N_{j,can}^{red}\) of Definition 94.1 is dominated by the
   Paper-16 clean residual polymer norm on each transferred row, up to an
   exponential per-row amplification \(e^{\lambda_{sem}}\).  This domination
   is computed under the same active law and does not include costs already
   assigned to \(U_{11}^{RPCov}\), \(U_{13}^{RPF}\), representation tails,
   internal `BTQ` rewrites, or comparison batteries.

4. **Coverage and size.**  The finite table supplies
   `P21-RED-COVER(chi_dec,b_dec)` and
   `P21-RED-SIZE(c_size^act)` for the same retained pass graph.

This is a transfer package, not a new analytic theorem.  Its content is the
identification of Paper 16's clean residual-polymer source with the actual
reduced forced records used by Paper 21.

### Lemma 116.5: Paper-16 Transfer Would Source \(m_{red}^{act}\)

If

```math
\mathrm{P21\text{-}RED\text{-}KP16\text{-}XFER}
(\mu_0,\lambda_{sem})
```

holds, then the primitive reduced decay route supplies

```math
\boxed{
m_{red}^{act}
=
\mu_0\chi_{dec}c_{size}^{act}-\lambda_{sem}.
}
```

Consequently the strict branch passes the Section-115 primitive margin if

```math
\mu_0\chi_{dec}c_{size}^{act}-\lambda_{sem}
>
\Theta_{red}^{115}.
```

Proof.

Paper 16's `HK-AN-FINTPL-CLOSE` exports a row-local clean residual decay
margin \(\Delta_{res}(e)>0\) once its finite row constants are verified.  A
uniform lower bound gives the one-step suppression \(\mu_0\) on every
decay-eligible row.  The seminorm-transfer clause converts that row-local
bound into the one-step reduced KP estimate of Definition 94.5, with
\(\lambda_{sem}\) recording exactly the unavoidable norm-conversion
amplification.  Coverage and size growth then invoke Theorem 94.6, giving
the displayed \(m_{red}^{act}\).  Section 115 gives the final comparison
threshold. `square`

### Lemma 116.6: `BTQ` And Degree-Tail Sources Are Auxiliary

`BTQ-FULLLAW`, `BTQ-DEGTAIL`, `BTQ-HKSM`, and `RED-CMSSI` do not by
themselves source \(m_{red}^{act}\).

Proof.

`BTQ-FULLLAW` and its active variants convert bounded-collar stagnant
families into finite same-shell records.  They remove a false forced-depth
source; they do not create decay for escaping reduced records.  A degree-tail
source gives a separate exponent \(m_{deg}^{BTQ}\) and possibly a battery
growth surcharge \(g_{bat}^{BTQ}\).  In Section 78 the usable exponent on the
degree-tail branch is \(\min(m_{poly}^{red},m_{deg}^{BTQ})\), so
\(m_{deg}^{BTQ}\) cannot replace \(m_{poly}^{red}\).  `RED-CMSSI` controls
the shell inverse growth \(g_q^{red}\); it lowers the growth side but is not a
projection-tail decay theorem. `square`

### Theorem 116.7: Complete Source Audit For \(m_{red}^{act}\)

The possible sources now have the following status.

| candidate source | could source \(m_{red}^{act}\)? | current status |
| --- | --- | --- |
| Direct primitive projection-tail theorem | yes | not proved for the active `SEL2` reduced tower |
| Shell-direct tail theorem | bypasses primitive \(m_{red}^{act}\) | not proved |
| Paper-16 clean KP worksheet transferred by `KP16-XFER` | yes | plausible and Barandes-aligned, but transfer package not proved |
| Paper 10 projective/tower control | no, auxiliary | finite/projective scaffolding only |
| Paper 11 AF/KP local-RG machinery | only after same-tower instantiation | conditional mechanism; not the active reduced tower theorem by itself |
| Paper 12 loop readout/de-smearing | no, auxiliary | readout and renormalization only |
| Paper 20 coefficient/tree-rate/escape mass | no, different target | surface-rate scaffolding only |
| `BTQ-FULLLAW`/`BTQ-DEGTAIL`/`HKSM` | no, auxiliary | closes bounded-collar/degree leak; does not replace reduced KP |
| `RED-CMSSI` | no, auxiliary | controls \(g_q^{red}\), not decay |

Therefore the only currently credible noncircular route to a primitive
\(m_{red}^{act}\) is:

```math
\mathrm{P21\text{-}RED\text{-}KP16\text{-}XFER}
(\mu_0,\lambda_{sem})
+
\mathrm{P21\text{-}RED\text{-}COVER}
+
\mathrm{P21\text{-}RED\text{-}SIZE}.
```

The direct shell-tail route remains cleaner if it can be proved, but no
previous paper supplies it.

Proof.

Lemmas 116.2, 116.3, and 116.6 eliminate the auxiliary candidates as sources
of \(m_{red}^{act}\).  Definition 116.4 and Lemma 116.5 identify the exact
transfer package required to turn Paper 16's clean finite-template analytic
worksheet into the Section-94 one-step reduced KP source.  Definition 116.1
lists the direct primitive and shell-direct alternatives.  The table is just
this exhaustive classification. `square`

### Corollary 116.8: Next Execution Order

The next proof-producing pass should be:

1. classify the currently retained `SD` and `act` pass rows with
   \(\Delta_X\ge1\);
2. for each such row, test whether the Paper-16 clean finite-template row data
   exist on the same active pushed-forward law;
3. compute the row-local \(\Delta_{res}(e)\) and the lower bound
   \(\mu_0\);
4. prove or carry the seminorm-transfer amplification \(\lambda_{sem}\);
5. combine with the finite coverage and size constants to test

   ```math
   \mu_0\chi_{dec}c_{size}^{act}-\lambda_{sem}
   >
   \Theta_{red}^{115}.
   ```

If any of steps 1--4 cannot be made literal on the same finite law, the
honest state remains `PARK-m_red`.  Printing the derivative tensor table is
then useful only insofar as it lowers \(\Theta_{red}^{115}\) or supplies the
row data needed by `KP16-XFER`.

## 117. Decay-Eligible `SD` And `act` Rows

Section 116 says that the next honest task is to classify the retained
`SD` and `act` pass rows with \(\Delta_X\ge1\).  There are two different
objects here, and they must not be conflated:

1. the **structural candidate rows** printed by Sections 104 and 106; and
2. the **licensed pass rows** obtained only after the source tables
   `ACTSRC+` and `SDSRC+` supply finite coefficients, inverse slots, and
   zero/carry decisions.

The current corpus has the first object and not the second.

### Definition 117.1: Structural Action Decay Candidates

Let

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in \overline V_{99}^{lit,+},
\qquad
\xi=(\zeta,\chi)\in\Xi_{act}^{99,+},
```

where

```math
\zeta=(\kappa,S,w,\lambda,\upsilon),
\qquad
\chi=(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit}.
```

Define the structural action decay-candidate set by

```math
\mathcal E_{act,dec}^{117,str}
:=
\left\{
(\bar v,\xi):
\alpha=\mu,\quad
p\le1,\quad
\Delta_X^{act}(L,\zeta)\ge1
\right\}.
```

Equivalently,

```math
(\bar v,\xi)\in\mathcal E_{act,dec}^{117,str}
\quad\Longleftrightarrow\quad
\alpha=\mu,\ p\le1,\ S(\zeta)\not\subseteq L.
```

Rows with \(\alpha\ne\mu\) are undefined, rows with \(p=2\) are product-tail
rows, and rows with \(\Delta_X^{act}=0\) are action bookkeeping rows.  None
of these may be counted as reduced escaping decay rows.

### Definition 117.2: Structural SD Decay Candidates

Let

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in \overline V_{99}^{lit,+},
\qquad
\xi=(\omega,\chi)\in\Xi_{SD}^{99,+},
```

where

```math
\omega=(\theta,S,w,\lambda,\upsilon),
\qquad
\chi=(\mu,\lambda,\mu',1)\in\Xi_{fus}^{99,lit}.
```

Define the structural SD decay-candidate set by

```math
\mathcal E_{SD,dec}^{117,str}
:=
\left\{
(\bar v,\xi):
\alpha=\mu,\quad
\theta(\omega)\ne\mathrm{retr},\quad
\Delta_X^{SD}(L,\omega)\ge1
\right\}.
```

Equivalently,

```math
(\bar v,\xi)\in\mathcal E_{SD,dec}^{117,str}
\quad\Longleftrightarrow\quad
\alpha=\mu,\ \theta(\omega)\ne\mathrm{retr},\ S(\omega)\not\subseteq L.
```

Rows with \(\theta=\mathrm{retr}\) are lower-shell/retraction rows, and rows
with \(\Delta_X^{SD}=0\) are channel or same-support bookkeeping rows.  They
are not decay rows.

### Definition 117.3: Licensed Decay Rows

The licensed action decay rows are

```math
\mathcal E_{act,dec}^{117}
:=
\left\{
(\bar v,\xi)\in\mathcal E_{act,dec}^{117,str}:
\begin{array}{l}
a_{act}^{99,+}(\bar v,\xi)<\infty,\quad
\mathcal O_{act}^{99,+}(\bar v,\xi)<\infty,\\
\text{the row is not assigned to tail, `BTQ`, `CMSSI`, zero, or carry,}\\
\text{and all Section-104 no-double-charge checks pass}
\end{array}
\right\}.
```

The licensed SD decay rows are

```math
\mathcal E_{SD,dec}^{117}
:=
\left\{
(\bar v,\xi)\in\mathcal E_{SD,dec}^{117,str}:
\begin{array}{l}
K_{SD}^{99,+}(\bar v,\xi)<\infty,\quad
\mathcal O_{SD}^{99,+}(\bar v,\xi)<\infty,\\
\text{the row is not assigned to retraction, `BTQ`, `CMSSI`, zero, or carry,}\\
\text{and all Section-106 admissibility checks pass}
\end{array}
\right\}.
```

Finally set

```math
\mathcal E_{dec}^{117,str}
:=
\mathcal E_{act,dec}^{117,str}
\cup
\mathcal E_{SD,dec}^{117,str},
\qquad
\mathcal E_{dec}^{117}
:=
\mathcal E_{act,dec}^{117}
\cup
\mathcal E_{SD,dec}^{117}.
```

### Lemma 117.4: Current Carried Completion Has No Licensed Decay Rows

On the strict carried completion of Section 108,

```math
\boxed{
\mathcal E_{act,dec}^{117}=\varnothing,\qquad
\mathcal E_{SD,dec}^{117}=\varnothing,\qquad
\mathcal E_{dec}^{117}=\varnothing.
}
```

Proof.

Section 105 explicitly records

```math
\mathcal E_{act,pass}^{99,+,car}=\varnothing.
```

The reason is not a structural absence of action rows; it is the absence of
the finite action source table \(\mathcal S_{act}^{99,+}\).  Under the safe
completion, every action row that is not already a tail, zero, `BTQ`, or
`CMSSI` row is carried in \(\mathcal S_{act,car}^{99,+}\), not licensed as a
pass row.  Since every licensed action decay row must in particular be an
`act-pass` row, \(\mathcal E_{act,dec}^{117}=\varnothing\).

Section 106 similarly records

```math
\mathcal E_{SD,pass}^{99,+,car}=\varnothing.
```

The SD source ledger remains parked at `PARK-SDSRC+`; under the safe
completion every non-retraction/nonzero/non-`BTQ`/non-`CMSSI` SD row is
carried rather than licensed.  Hence
\(\mathcal E_{SD,dec}^{117}=\varnothing\).  The union statement follows.
`square`

### Lemma 117.5: Only Structural `act-pass` And `SD-pass` Rows Can Source \(\mu_0\)

Any row contributing to the Paper-16 transfer lower bound \(\mu_0\) must lie
in \(\mathcal E_{dec}^{117,str}\).  In particular, fusion rows, comparison
rows, `BTQ` rows, `CMSSI` rows, zero rows, carried rows, retraction rows,
product-tail rows, undefined rows, and rows with \(\Delta_X=0\) cannot be
used to lower bound \(\mu_0\).

Proof.

The exponent \(\mu_0\) in Definition 116.4 is a uniform lower bound on
row-local residual decay margins for rows that create a new reduced escaping
record.  Fusion rows in Section 103 have \(\Delta_X=0\) and are channel
bookkeeping.  Comparison rows in Section 107 are common-law transport and
battery comparison rows; they do not create the active reduced escaping
record.  `BTQ` and `CMSSI` rows are already assigned to bounded-collar and
channel/seminorm ledgers, respectively.  Zero and carried rows have no
positive certified row-local decay margin.  Retraction and product-tail rows
leave the escaping-row ledger by definition.  Finally, \(\Delta_X=0\) rows
do not increase reduced support and therefore cannot be the escaping-step
source measured by \(c_{size}^{act}\).  The only printed structural row
families left are exactly the `act-pass` and `SD-pass` candidates of
Definitions 117.1 and 117.2. `square`

### Theorem 117.6: Step-1 Classification Verdict

The classification requested in Corollary 116.8 is:

```math
\boxed{
\mathcal E_{dec}^{117,str}
=
\mathcal E_{act,dec}^{117,str}
\cup
\mathcal E_{SD,dec}^{117,str},
}
```

where

```math
\mathcal E_{act,dec}^{117,str}
\Longleftrightarrow
\alpha=\mu,\quad p\le1,\quad S(\zeta)\not\subseteq L,
```

and

```math
\mathcal E_{SD,dec}^{117,str}
\Longleftrightarrow
\alpha=\mu,\quad \theta(\omega)\ne\mathrm{retr},\quad S(\omega)\not\subseteq L.
```

The current licensed set is empty:

```math
\boxed{
\mathcal E_{dec}^{117}=\varnothing
\quad\text{on the Section-108 carried completion.}
}
```

Therefore the present corpus does not yet permit a numerical computation of
\(\mu_0\), \(\chi_{dec}\), or \(c_{size}^{act}\) from the pass graph.  Any
attempt to set

```math
m_{red}^{act}
=
\mu_0\chi_{dec}c_{size}^{act}-\lambda_{sem}
```

on the carried graph gives no positive source: the licensed pass graph is
empty.  This is not a falsification of the structural branch.  It is a
source-table obstruction: the candidate rows are known, but their row values
and admissibility decisions are not yet printed.

Proof.

Definitions 117.1 and 117.2 translate the two pass-row conditions printed in
Tables 104.5 and 106.6 into support-growth form.  Lemma 117.4 gives the
carried-branch licensed set.  Lemma 117.5 excludes every other row family
from the decay-source role. `square`

### Corollary 117.7: Next Execution Order

The next proof-producing task is not to compute \(\mu_0\) on the carried
graph.  The graph has no licensed decay rows.  The next task is to turn the
structural candidate rows into literal rows:

1. instantiate the finite lists of candidates in
   \(\mathcal E_{act,dec}^{117,str}\) and
   \(\mathcal E_{SD,dec}^{117,str}\) on the over-refined vertex cover;
2. supply `ACTSRC+` row values, inverse slots, derivative/product selectors,
   and zero/carry decisions for the action candidates;
3. supply `SDSRC+` coefficients, inverse slots, and zero/carry decisions for
   the SD candidates;
4. remove every row assigned to `BTQ`, `CMSSI`, tail, retraction, zero, or
   carry;
5. only then compute

   ```math
   \chi_{dec},\qquad
   c_{size}^{act},\qquad
   \mu_0,\qquad
   \lambda_{sem}.
   ```

If the literal source pass remains empty after these source tables are
printed, the primitive Paper-16 transfer route collapses and Paper 21 must
switch to a direct all-shell tail theorem or explicitly park
\(m_{red}^{act}\).

## 118. Finite Candidate Table For Structural Decay Rows

This section executes the first item of Corollary 117.7.  It prints the
finite row generator for

```math
\mathcal E_{act,dec}^{117,str},
\qquad
\mathcal E_{SD,dec}^{117,str}.
```

The output is intentionally a generator rather than a several-billion-line
table.  It is literal in the same sense as Sections 102--106: every symbol
ranges over an explicitly finite set already printed in the paper, and every
generated row is a concrete row on the over-refined vertex cover.

### Definition 118.1: Retained Fusion Rows By Source Channel

Let

```math
\mathcal F_\alpha^{99}
:=
\{F_i=(\alpha,\lambda_i,\mu_i',1)\in\Xi_{fus}^{99,lit}\}.
```

From Definition 103.2,

| source \(\alpha\) | retained rows \(\mathcal F_\alpha^{99}\) | count |
| --- | --- | --- |
| \(0\) | \(F_1=(0,0,0,1),\ F_2=(0,{1\over2},{1\over2},1),\ F_3=(0,1,1,1)\) | \(3\) |
| \(1/2\) | \(F_4=({1\over2},0,{1\over2},1),\ F_5=({1\over2},{1\over2},0,1),\ F_6=({1\over2},{1\over2},1,1),\ F_7=({1\over2},1,{1\over2},1)\) | \(4\) |
| \(1\) | \(F_8=(1,0,1,1),\ F_9=(1,{1\over2},{1\over2},1),\ F_{10}=(1,1,0,1),\ F_{11}=(1,1,1,1)\) | \(4\) |

Write

```math
N_{fus}(\alpha):=|\mathcal F_\alpha^{99}|,
\qquad
N_{fus}(0)=3,\quad
N_{fus}({1\over2})=4,\quad
N_{fus}(1)=4.
```

These are the only channel rows allowed in the structural decay printer.
Every action or SD candidate below chooses exactly one
\(F_i\in\mathcal F_\alpha^{99}\).

### Definition 118.2: Support-Growth Counters

For \(L\in\mathfrak L_{99}^{+}\), define

```math
B_{act}^{118}(L)
:=
\#\{S\in\mathsf S_{act}^{99,+}:S\not\subseteq L\}.
```

Since \(\mathsf S_{act}^{99,+}\) is an over-refined local support list inside
\(\mathsf Q_{loc}^{99}=\{-1,0,1\}^4\), one always has the safe bound

```math
B_{act}^{118}(L)\le 2^{81}-2^{|L|}.
```

If the maximal support over-cover is used, namely
\(\mathsf S_{act}^{99,+}=\mathcal P(\mathsf Q_{loc}^{99})\setminus\{\varnothing\}\),
then the bound is an equality.

For SD rows the printed atom list uses all nonempty local supports, so set

```math
B_{SD}^{118}(L)
:=
\#\{S\subseteq\mathsf Q_{loc}^{99}:S\ne\varnothing,\ S\not\subseteq L\}
=2^{81}-2^{|L|}.
```

The predicate \(S\not\subseteq L\) is exactly the support-growth predicate
\(\Delta_X\ge1\) from Definitions 104.3 and 106.5.

### Definition 118.3: The Literal Action Candidate Printer

Fix a source vertex

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in\overline V_{99}^{lit,+}.
```

If \(p=2\), no structural action decay candidate is printed from \(\bar v\).
Those attempted rows are product-tail rows.

If \(p\le1\), then for every tuple

```math
(F_i,\kappa,S,w,\upsilon)
\in
\mathcal F_\alpha^{99}
\times
\{\mathrm{plaq},\mathrm{stencil},\mathrm{prod}\}
\times
\{S\in\mathsf S_{act}^{99,+}:S\not\subseteq L\}
\times
\mathsf W_{\le4}^{99}
\times
\Sigma_{99}^{+},
```

write

```math
F_i=(\alpha,\lambda_i,\mu_i',1)
```

and form the action atom

```math
\zeta_i(\kappa,S,w,\upsilon)
:=
(\kappa,S,w,\lambda_i,\upsilon).
```

The corresponding structural action candidate is

```math
e_{act}^{118}
(\bar v;i,\kappa,S,w,\upsilon)
:=
\left(
\bar v,\,
\xi_i
\right),
\qquad
\xi_i:=
\left(\zeta_i(\kappa,S,w,\upsilon),F_i\right).
```

Its target and increments are those of Definition 104.4:

```math
R_{act}^{99,+}(\bar v,\xi_i)
=
(\bar v',\Delta_X,\Delta_C,\Delta_h,1,a,\mathcal O),
```

where

```math
\Delta_X=|S\setminus L|\ge1.
```

The row is structural only.  It becomes a licensed pass row exactly when the
source table supplies finite \(a_{act,raw}^{99,+}\),
\(\mathcal O_{act}^{99,+}\), and the Section-104 no-double-charge checks.

### Table 118.4: Action Candidate Counts Per Source Vertex

Let

```math
W_{99}:=|\mathsf W_{\le4}^{99}|.
```

For a fixed source vertex \(\bar v=(T,\alpha,L,h,p,\sigma)\), the number of
printed structural action decay candidates is

```math
N_{act,dec}^{118}(\bar v)
=
\mathbf 1_{\{p\le1\}}\,
48\,W_{99}\,B_{act}^{118}(L)\,N_{fus}(\alpha).
```

Equivalently,

| \(\alpha\) | \(p\le1\) count | \(p=2\) count |
| --- | --- | --- |
| \(0\) | \(144\,W_{99}B_{act}^{118}(L)\) | \(0\) |
| \(1/2\) | \(192\,W_{99}B_{act}^{118}(L)\) | \(0\) |
| \(1\) | \(192\,W_{99}B_{act}^{118}(L)\) | \(0\) |

The factor \(48=3\cdot16\) is the product of the three action kinds
\(\kappa\) and the sixteen symmetry/center flags \(\upsilon\).

### Definition 118.5: The Literal SD Candidate Printer

Fix again

```math
\bar v=(T,\alpha,L,h,p,\sigma)\in\overline V_{99}^{lit,+}.
```

For every tuple

```math
(F_i,\theta,S,w,\upsilon)
\in
\mathcal F_\alpha^{99}
\times
\{\mathrm{Cas},\mathrm{SDdiv},\mathrm{loop}\}
\times
\{S\subseteq\mathsf Q_{loc}^{99}:S\ne\varnothing,\ S\not\subseteq L\}
\times
\mathsf W_{\le4}^{99}
\times
\Sigma_{99}^{+},
```

write

```math
F_i=(\alpha,\lambda_i,\mu_i',1)
```

and form the SD atom

```math
\omega_i(\theta,S,w,\upsilon)
:=
(\theta,S,w,\lambda_i,\upsilon).
```

The corresponding structural SD candidate is

```math
e_{SD}^{118}
(\bar v;i,\theta,S,w,\upsilon)
:=
\left(
\bar v,\,
\xi_i
\right),
\qquad
\xi_i:=
\left(\omega_i(\theta,S,w,\upsilon),F_i\right).
```

Its target and increments are those of Definition 106.5:

```math
R_{SD}^{99,+}(\bar v,\xi_i)
=
(\bar v',\Delta_X,\Delta_C,\Delta_h,0,a,\mathcal O),
```

where

```math
\Delta_X=|S\setminus L|\ge1.
```

No `retr` rows appear in this printer.  They are lower-shell retraction rows,
not decay candidates.

### Table 118.6: SD Candidate Counts Per Source Vertex

For a fixed source vertex \(\bar v=(T,\alpha,L,h,p,\sigma)\), the number of
printed structural SD decay candidates is

```math
N_{SD,dec}^{118}(\bar v)
=
48\,W_{99}\,B_{SD}^{118}(L)\,N_{fus}(\alpha).
```

Equivalently,

| \(\alpha\) | count |
| --- | --- |
| \(0\) | \(144\,W_{99}B_{SD}^{118}(L)\) |
| \(1/2\) | \(192\,W_{99}B_{SD}^{118}(L)\) |
| \(1\) | \(192\,W_{99}B_{SD}^{118}(L)\) |

The same factor \(48=3\cdot16\) appears here because the three
non-retraction SD kinds replace the three action kinds.

### Theorem 118.7: The Structural Candidate Table Is Printed

The finite candidate table generated by Definitions 118.3 and 118.5 is
exactly the structural decay-candidate set of Section 117:

```math
\boxed{
\mathcal E_{act,dec}^{118,str}
=
\mathcal E_{act,dec}^{117,str},
\qquad
\mathcal E_{SD,dec}^{118,str}
=
\mathcal E_{SD,dec}^{117,str}.
}
```

Consequently,

```math
\boxed{
\mathcal E_{dec}^{118,str}
=
\mathcal E_{act,dec}^{118,str}
\cup
\mathcal E_{SD,dec}^{118,str}
}
```

is now a printed finite object on the over-refined cover.

Proof.

For action rows, Definition 104.2 requires a pair
\((\zeta,\chi)\) with \(\lambda(\zeta)=\lambda(\chi)\).  Definition 118.3
chooses a retained fusion row \(F_i=(\alpha,\lambda_i,\mu_i',1)\) and then
sets \(\lambda(\zeta)=\lambda_i\), so the retained action-index condition is
exactly satisfied.  The channel compatibility \(\alpha=\mu\) is built in by
choosing \(F_i\in\mathcal F_\alpha^{99}\).  The condition \(p\le1\) is
explicit, and \(S\not\subseteq L\) is equivalent to
\(\Delta_X^{act}\ge1\).  These are precisely the conditions in Definition
117.1.

For SD rows, Definition 106.2 has the same retained channel condition, and
Definition 118.5 again enforces it by choosing
\(F_i\in\mathcal F_\alpha^{99}\).  The row kind is restricted to
\(\{\mathrm{Cas},\mathrm{SDdiv},\mathrm{loop}\}\), which is exactly
\(\theta\ne\mathrm{retr}\), and \(S\not\subseteq L\) is equivalent to
\(\Delta_X^{SD}\ge1\).  These are precisely the conditions in Definition
117.2. `square`

### Corollary 118.8: What Remains Before \(\mu_0\) Can Be Computed

The structural candidate rows are now fixed.  The licensed pass rows are
still not fixed:

```math
\mathcal E_{dec}^{118}
=
\varnothing
\quad\text{under the Section-108 carried completion.}
```

The next finite-table tasks are therefore exactly:

1. fill \(a_{act,raw}^{99,+}\) and \(\mathcal O_{act}^{99,+}\) on the action
   candidates printed by Definition 118.3;
2. fill \(K_{SD}^{99,+}\) and \(\mathcal O_{SD}^{99,+}\) on the SD candidates
   printed by Definition 118.5;
3. print the exact zero/carry tags for both candidate families;
4. delete rows sent to `BTQ`, `CMSSI`, tail, retraction, zero, or carry;
5. only then compute the pass graph constants

   ```math
   \chi_{dec},\quad c_{size}^{act},\quad \mu_0,\quad \lambda_{sem}.
   ```

Thus Section 118 closes the enumeration part of step 1 and leaves the source
part, not the row grammar, as the active obstruction.

## 119. Row-By-Row `ACTSRC+` Source Functional

This section sources `ACTSRC+` row by row as far as the existing papers allow.
The conclusion is deliberately split:

1. the strict `YM2` coefficient-envelope source is finite and row-local; but
2. literal derivative-tensor membership, connected covariance-pair
   membership, exact signed row values, and same-shell inverse slots are not
   yet printed.

Thus this section reduces `PARK-ACTSRC+`; it does not license action pass
rows.

### Definition 119.1: Strict `YM2` Source Components

Use the strict axial-tree, exact-covariance, connected/cumulant,
minimal-record branch.  The nonoptional `YM2` source labels are

```math
4,\qquad 33,\qquad J2.
```

Paper 16 supplies their local absolute constants

```math
C_4^{loc}\le24C_4C_{cov}^{2},
\qquad
C_{33}^{loc}\le18C_3^2C_{cov}^{3},
\qquad
C_J^{loc}\le C_JC_{cov}.
```

The optional labels

```math
gf2,\quad cov2,\quad rec2,\quad norm2
```

are zero on this strict branch and carried outside it.  They are not
`ACTSRC+` pass rows.

Let the coupled monomial graphs of Section 113 be

```math
\mathfrak G_4^{113},
\qquad
\mathfrak G_{33}^{113},
\qquad
\mathfrak G_J^{113}.
```

For a tuple \(g=(S,w,\upsilon)\), introduce finite signed component
coefficients

```math
A_4^{119}(g,\chi),\qquad
A_{33}^{119}(g,\chi),\qquad
A_J^{119}(g,\chi),
```

where \(\chi\in\Xi_{fus}^{99,lit}\).  These coefficients are evaluated on
the same active pushed-forward `SEL2` law.  The current corpus supplies the
following finite envelopes:

```math
|A_4^{119}(g,\chi)|
\le
24C_4C_{cov}^{2},
```

```math
|A_{33}^{119}(g,\chi)|
\le
18C_3^2C_{cov}^{3},
```

and

```math
|A_J^{119}(g,\chi)|
\le
C_JC_{cov}.
```

The signed values themselves are not printed unless the derivative tensor and
covariance-pair tables are supplied.  These envelopes are exactly the
row-local version of Paper 16's `HK-SF-YM2` vertex ledger.

### Definition 119.2: Row-By-Row Strict Action Source

Let

```math
e=e_{act}^{118}(\bar v;i,\kappa,S,w,\upsilon)
```

be a structural action candidate from Definition 118.3, and write

```math
\chi=F_i=(\alpha,\lambda_i,\mu_i',1),
\qquad
g(e):=(S,w,\upsilon).
```

Define the strict same-record action source functional

```math
\mathcal A_{act}^{119}(e)
```

by the following row-by-row rule.

If \(\kappa\ne\mathrm{stencil}\), then

```math
\mathcal A_{act}^{119}(e):=0.
```

These are not produced by the strict nonoptional `YM2` source.  A future
independent plaquette or product source would be a new source branch and
must be carried separately; it is not silently imported here.

If \(\kappa=\mathrm{stencil}\), set

```math
\mathcal A_{act}^{119}(e)
:=
\mathbf 1_{\{g(e)\in\mathfrak G_4^{113}\}}
A_4^{119}(g(e),\chi)
```

```math
\quad+
\mathbf 1_{\{g(e)\in\mathfrak G_{33}^{113}\}}
A_{33}^{119}(g(e),\chi)
```

```math
\quad+
\mathbf 1_{\{g(e)\in\mathfrak G_J^{113}\}}
\mathbf 1_{\{\lambda_i=0\}}
A_J^{119}(g(e),\chi).
```

The Jacobian component is neutral: if \(g(e)\in\mathfrak G_J^{113}\) but
\(\lambda_i\ne0\), its `J2` contribution is zero.

The row's coefficient-envelope is

```math
C_{act,row}^{119}(e)
:=
\mathbf 1_{\{\kappa=\mathrm{stencil}\}}
\Bigl[
\mathbf 1_{\{g(e)\in\mathfrak G_4^{113}\}}24C_4C_{cov}^{2}
```

```math
\qquad+
\mathbf 1_{\{g(e)\in\mathfrak G_{33}^{113}\}}18C_3^2C_{cov}^{3}
\qquad+
\mathbf 1_{\{g(e)\in\mathfrak G_J^{113},\lambda_i=0\}}C_JC_{cov}
\Bigr].
```

Thus

```math
|\mathcal A_{act}^{119}(e)|
\le
C_{act,row}^{119}(e)
\le
C_v^{YM2,min}.
```

The strict raw action coefficient may be sourced by

```math
a_{act,raw}^{119}(e):=|\mathcal A_{act}^{119}(e)|
```

when the signed values are printed, or by the finite envelope

```math
a_{act,raw}^{119}(e)\le C_{act,row}^{119}(e)
```

when only Paper 16's local absolute constants are used.

### Definition 119.3: Exact Zero And Carry Tags From The Source Functional

The source functional gives the following row tags.

| tag | condition | status |
| --- | --- | --- |
| `act-zero-kind` | \(\kappa\ne\mathrm{stencil}\) on the strict nonoptional `YM2` branch | exact zero for this source branch |
| `act-zero-mon` | \(\kappa=\mathrm{stencil}\) and \(g(e)\notin\mathfrak G_4^{113}\cup\mathfrak G_{33}^{113}\cup\mathfrak G_J^{113}\) | exact zero after the monomial graphs are printed |
| `act-zero-Jchan` | \(g(e)\in\mathfrak G_J^{113}\) but \(\lambda_i\ne0\), with no \(4\) or \(33\) contribution | exact neutral-Jacobian zero |
| `act-rowval-env` | \(C_{act,row}^{119}(e)>0\) but signed values are not printed | finite coefficient envelope only |
| `act-rowval-lit` | \(\mathcal A_{act}^{119}(e)\) is printed as a signed finite number | literal coefficient value |
| `act-carry-inv` | \(\mathcal O_{act}^{99,+}(e)\) is not printed | carried, not pass |

Derivative-channel zeroes from Lemma 109.6 are available only for a component
declared derivative-sourced through

```math
K_{act}^{99,+}(\zeta,\chi)
=
\Gamma_{act}^{99}(\chi)P_{act}^{99,+}(\zeta,\chi).
```

For those derivative-sourced components, rows

```math
F_1,F_2,F_3,F_4,F_8
```

have zero component contribution.  This zero is not applied to a direct
scalar stencil component unless the source table explicitly declares that
the component is derivative-sourced.

### Lemma 119.4: Same-Record Legality

The functional \(\mathcal A_{act}^{119}\) is a same-record source functional
on the active `SEL2` law.  It does not use a continuum Yang-Mills measure,
a Wilson-loop area law, or any off-record stochastic process.

Proof.

Definitions 119.1 and 119.2 use only the finite local labels supplied by
Paper 16's `HK-SF-YM2`, the root-coordinate monomial graphs of Section 113,
the over-refined action candidates of Section 118, and the retained
`SU(2)` channel table of Section 103.  Paper 20's interior `YM2` audit
confirms that the three nonoptional labels \(4,33,J2\) are the correct
same-record second-order local labels after odd terms vanish and the
heat-time tangent is absorbed.  It also confirms that exact signed
three-term cancellation is not currently proved; hence this section uses
finite envelopes unless the signed derivative/covariance tables are printed.
Every operation is finite and lives on the same pushed-forward scalar record.
`square`

### Lemma 119.5: What Is Closed And What Is Still Parked

Section 119 closes the following source subgate:

```math
\boxed{
\mathrm{P21\text{-}ACTSRC\text{-}ROWENV}^{119,+}
}
```

meaning that every structural action candidate now has a same-record
row-by-row coefficient-envelope assignment:

```math
e
\longmapsto
C_{act,row}^{119}(e),
```

and every strict non-`YM2` kind is zero for this source branch.

It does not close:

```math
\mathrm{PARK\text{-}ACTSRC\text{-}DTENS}^{113,+},
\qquad
\mathrm{PARK\text{-}ACTSRC\text{-}COVPAIR}^{113,+},
```

```math
\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL\text{-}LIT}^{119,+},
\qquad
\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{99,+},
\qquad
\mathrm{PARK\text{-}ACTSRC\text{-}ZC\text{-}LIT}^{119,+}.
```

Here `ROWVAL-LIT` is the signed numerical table
\(\mathcal A_{act}^{119}(e)\), `INV` is the same-shell off-diagonal slot
\(\mathcal O_{act}^{99,+}(e)\), and `ZC-LIT` is the fully printed
zero/carry list after the monomial graphs are literal.

Proof.

Definition 119.2 gives a finite coefficient envelope for every candidate
row.  Definition 119.3 gives exact source-branch zeroes for impossible kinds
and for missing selected monomials once the graphs are printed.  But the
graphs \(\mathfrak G_4^{113},\mathfrak G_{33}^{113},\mathfrak G_J^{113}\)
still depend on the derivative-tensor and connected covariance-pair tables
unless they are used only through the polynomial envelope.  Moreover,
Definition 105.6 requires same-shell inverse slots before a row can be
classified as pass.  None of these data is supplied by the absolute
`HK-SF-YM2` constants. `square`

### Theorem 119.6: Row-By-Row `ACTSRC+` Verdict

The honest row-by-row `ACTSRC+` status after Section 119 is

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}^{+}
=
\mathrm{P21\text{-}ACTSRC\text{-}ROWENV}^{119,+}
\quad+
\mathrm{PARK\text{-}ACTSRC\text{-}DTENS}^{113,+}
\quad+
\mathrm{PARK\text{-}ACTSRC\text{-}COVPAIR}^{113,+}
\quad+
\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL\text{-}LIT}^{119,+}
\quad+
\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{99,+}
\quad+
\mathrm{PARK\text{-}ACTSRC\text{-}ZC\text{-}LIT}^{119,+}.
}
```

Under the Section-108 carried completion,

```math
\mathcal E_{act,pass}^{119,car}=\varnothing.
```

If the paper elects to use the envelope branch rather than literal row
values, the action coefficient base is bounded by

```math
A_{act}^{119,env}
\le
\max\left(1,\,
B_{act}^{110}
\Pi_{act}^{113,mon}C_v^{YM2,min}
\right),
```

where the polynomial selector surcharge \(\Pi_{act}^{113,mon}\) is the one
bounded in Corollary 114.3.  This is the same safe action surcharge used in
Section 115.  It is a coefficient-envelope route, not a pass-row source
until inverse slots and zero/carry tags are supplied.

Proof.

Lemma 119.5 proves the closed and parked subgates.  The empty carried pass
graph follows from Definition 105.5, because rows with unsupplied inverse
slots or literal values remain carried.  The envelope coefficient base is
Definition 109.4 with the Section-113 polynomial selector and the strict
minimal `YM2` vertex constant. `square`

### Corollary 119.7: Next Action-Source Steps

After row-by-row sourcing, the next action tasks are now sharply ordered.

1. Print the derivative tensor table
   \(\mathfrak M_4^{113},\mathfrak M_3^{113},\mathfrak M_J^{113}\) or keep
   the polynomial envelope.
2. Print the connected covariance-pair selector for
   \(\mathfrak G_{33}^{113}\), or keep the polynomial envelope.
3. Print the same-shell inverse/off-diagonal slot
   \(\mathcal O_{act}^{99,+}(e)\) for every candidate not already zero.
4. Only then promote rows from `act-rowval-env` or `act-rowval-lit` to
   `act-pass`, rerun the zero-growth SCC test, and compute
   \(A_{act,pass}^{99,+}\), \(\Omega_{act}^{99,+}\), and the contribution to
   \(\chi_{dec}\).

If any of these finite source tables remains unprinted, action rows stay
outside the licensed pass graph and \(m_{red}^{act}\) remains parked.

## 120. Row-By-Row `SDSRC+` Source Functional

This section sources `SDSRC+` row by row as far as the existing papers allow.
The compact-group source is stronger than the action source in one respect:
Paper 14 proves the exact finite Schwinger-Dyson identity before projection.
The remaining difficulty is the finite projected ledger: which projected rows
are retained, what their finite projection multipliers are, and what
same-shell inverse slots they require.

### Definition 120.1: Compact-Group SD Source Components

Use the finite compact-group identity of Paper 14, Theorem 10.2:

```math
\mathbb E_\eta[L_e^A F]
=
\mathbb E_\eta[F L_e^A S_\eta].
```

After projection to the Section-106 over-refined retained `SD` row list,
there are three non-retraction source kinds:

```math
\theta\in\{\mathrm{Cas},\mathrm{SDdiv},\mathrm{loop}\}.
```

The retained channel scalars are already printed in Definition 106.3:

```math
\Gamma_{SD}^{99}(\chi)
=
{1\over2}\left(C_2(\mu')-C_2(\mu)-C_2(\lambda)\right),
```

and

```math
\Gamma_{Cas}^{99}(0)=0,\qquad
\Gamma_{Cas}^{99}({1\over2})={3\over4},\qquad
\Gamma_{Cas}^{99}(1)=2.
```

The compact-group source supplies algebraic identities.  Projection to the
finite retained battery is encoded by finite row multipliers

```math
P_{Cas}^{120}(\omega,\chi),\qquad
P_{SDdiv}^{120}(\omega,\chi),\qquad
P_{loop}^{120}(\omega,\chi).
```

If a multiplier is not printed by the finite projected ledger, its row is
carried.  It is not inferred from the unprojected identity alone.

### Definition 120.2: Strict SD Source Functional

Let

```math
e=e_{SD}^{118}(\bar v;i,\theta,S,w,\upsilon)
```

be a structural SD candidate from Definition 118.5, and write

```math
\chi=F_i=(\alpha,\lambda_i,\mu_i',1),
\qquad
\omega=(\theta,S,w,\lambda_i,\upsilon).
```

Define the strict projected SD source functional

```math
\mathcal K_{SD}^{120}(e)
```

by the following row-by-row rule.

**Casimir self rows.**  A pure Casimir row acts on an already retained record;
it is a self/CMSSI row, not an escaping support-growth row.  Therefore, for
the structural decay candidates of Section 118, which all satisfy
\(S\not\subseteq L\),

```math
\mathcal K_{SD}^{120}(e):=0
\qquad
(\theta=\mathrm{Cas}).
```

If one instead evaluates same-support Casimir rows, the only sourced channel
is

```math
\chi=\chi_{Cas}(\alpha)=(\alpha,0,\alpha,1),
```

and the coefficient is

```math
\Gamma_{Cas}^{99}(\alpha)P_{Cas}^{120}(\omega,\chi_{Cas}(\alpha)).
```

Those rows belong to `CMSSI` or the same-shell inverse ledger, not to
\(\mathcal E_{SD,dec}^{118,str}\).

**Schwinger-Dyson divergence rows.**  For \(\theta=\mathrm{SDdiv}\), set

```math
\mathcal K_{SD}^{120}(e)
:=
\Gamma_{SD}^{99}(\chi)P_{SDdiv}^{120}(\omega,\chi)
```

when the projected multiplier is printed.  If it is not printed, the row is
carried.

**Loop rows.**  For \(\theta=\mathrm{loop}\), set

```math
\mathcal K_{SD}^{120}(e)
:=
\Gamma_{SD}^{99}(\chi)P_{loop}^{120}(\omega,\chi)
```

when the projected loop multiplier is printed.  If it is not printed, the
row is carried.

The row coefficient used by the strict structural row map is

```math
a_{SD}^{120}(e):=|\mathcal K_{SD}^{120}(e)|
```

when \(\mathcal K_{SD}^{120}(e)\) is printed.

### Definition 120.3: Projection Envelopes

Define the finite projection envelopes

```math
P_{SDdiv,max}^{120}
:=
\max_{\omega,\chi}
|P_{SDdiv}^{120}(\omega,\chi)|,
\qquad
P_{loop,max}^{120}
:=
\max_{\omega,\chi}
|P_{loop}^{120}(\omega,\chi)|,
```

where the maximum ranges only over printed retained projected rows.  If the
projected ledger is not printed, these constants are parked.

When the minimal unit-projection convention is explicitly supplied, namely:

1. each retained channel in \(\Xi_{fus}^{99,lit}\) has multiplicity one;
2. every projected derivative/loop sum uses at most the links appearing in
   the retained word \(w\);
3. \(w\in\mathsf W_{\le4}^{99}\);

one may take the safe bounds

```math
P_{SDdiv,max}^{120}\le4,
\qquad
P_{loop,max}^{120}\le4.
```

Under that convention every printed `SDdiv` or `loop` coefficient obeys

```math
|\mathcal K_{SD}^{120}(e)|
\le
2\max(P_{SDdiv,max}^{120},P_{loop,max}^{120})
\le8.
```

Without the minimal unit-projection convention, keep the symbolic finite
bound

```math
|\mathcal K_{SD}^{120}(e)|
\le
2\max(P_{SDdiv,max}^{120},P_{loop,max}^{120}).
```

### Definition 120.4: SD Zero And Carry Tags

The source functional gives the following row tags for structural SD
candidates.

| tag | condition | status |
| --- | --- | --- |
| `SD-zero-CasEsc` | \(\theta=\mathrm{Cas}\) and \(S\not\subseteq L\) | exact zero/inactive over-cover for decay candidates |
| `SD-zero-trivCas` | same-support Casimir row with \(\alpha=0\) | exact zero because \(C_2(0)=0\) |
| `SD-zero-derchan` | \(\theta\in\{\mathrm{SDdiv},\mathrm{loop}\}\), printed multiplier finite, and \(\Gamma_{SD}^{99}(\chi)=0\) | exact compact-group derivative zero |
| `SD-rowval-proj` | projected multiplier \(P_\theta^{120}\) printed and \(\Gamma_{SD}^{99}(\chi)\ne0\) | finite projected coefficient |
| `SD-carry-proj` | projected multiplier not printed | carried, not pass |
| `SD-carry-inv` | \(\mathcal O_{SD}^{99,+}(e)\) not printed | carried, not pass |

The derivative-channel zeroes are exactly the retained rows

```math
F_1,\ F_2,\ F_3,\ F_4,\ F_8,
```

because these are precisely the rows with \(\Gamma_{SD}^{99}(\chi)=0\).

### Lemma 120.5: Same-Record Legality And No Double Charge

The source functional \(\mathcal K_{SD}^{120}\) is a same-record finite
source functional on the active `SEL2` law.  It does not charge `ACTSRC+`,
RP/Cov transport, `RPF`, `KPdec`, `WP`, perimeter/cusp/readout, comparison
battery, or continuum Yang-Mills existence.

Proof.

The unprojected identity is Paper 14's finite compact-group integration by
parts on the cutoff law.  Section 106 already restricts that identity to the
same retained `SU(2)` channel table and the same over-refined finite vertex
cover as the rest of Paper 21.  The only extra data in Definition 120.2 are
the finite projected multipliers \(P_\theta^{120}\), which are part of the
projected SD ledger itself.  No action coefficient, projective transport
tail, exact-entry residual, whole-process mismatch, or readout correction is
used.  The support-growing Casimir over-cover rows are deleted precisely to
avoid charging a same-support Casimir self identity as an escaping record.
`square`

### Lemma 120.6: What `SDSRC+` Now Closes

Section 120 closes the compact-group scalar part of `SDSRC+`:

```math
\boxed{
\mathrm{P21\text{-}SDSRC\text{-}CGSCAL}^{120,+}
}
```

meaning that:

1. support-growing `Cas` candidates are inactive exact zeroes for the
   strict Casimir self-row source;
2. `SDdiv` and `loop` candidates have the row formula

   ```math
   K_{SD}^{120}(e)=\Gamma_{SD}^{99}(\chi)P_\theta^{120}(\omega,\chi);
   ```

3. derivative-channel zeroes are exactly the retained channels with
   \(\Gamma_{SD}^{99}(\chi)=0\);
4. finite coefficient envelopes follow once the projected multipliers are
   printed or bounded.

It does not close:

```math
\mathrm{PARK\text{-}SDSRC\text{-}PROJ}^{120,+},
\qquad
\mathrm{PARK\text{-}SDSRC\text{-}INV}^{99,+},
\qquad
\mathrm{PARK\text{-}SDSRC\text{-}ZC\text{-}LIT}^{120,+}.
```

`PROJ` is the literal projected multiplier table
\(P_{SDdiv}^{120},P_{loop}^{120}\), `INV` is the same-shell inverse slot
\(\mathcal O_{SD}^{99,+}\), and `ZC-LIT` is the fully printed zero/carry
list after projection.

Proof.

Definitions 120.2--120.4 give the row formula and zero/carry tags.  Lemma
120.5 proves same-record legality.  A pass row still needs a printed
projected coefficient, a printed inverse slot, and a no-double-charge
admissibility check, exactly as Table 106.6 and Theorem 106.8 require.
`square`

### Theorem 120.7: Row-By-Row `SDSRC+` Verdict

The honest row-by-row `SDSRC+` status after Section 120 is

```math
\boxed{
\mathrm{PARK\text{-}SDSRC}^{+}
=
\mathrm{P21\text{-}SDSRC\text{-}CGSCAL}^{120,+}
\quad+
\mathrm{PARK\text{-}SDSRC\text{-}PROJ}^{120,+}
\quad+
\mathrm{PARK\text{-}SDSRC\text{-}INV}^{99,+}
\quad+
\mathrm{PARK\text{-}SDSRC\text{-}ZC\text{-}LIT}^{120,+}.
}
```

Under the Section-108 carried completion,

```math
\mathcal E_{SD,pass}^{120,car}=\varnothing.
```

If the projected multiplier table and inverse slots are supplied, the SD
coefficient base obeys

```math
A_{SD,pass}^{120}
\le
\max\left(
1,\,
2\max(P_{SDdiv,max}^{120},P_{loop,max}^{120})
\right),
```

and under the minimal unit-projection convention,

```math
A_{SD,pass}^{120}\le8.
```

This bound applies only to rows surviving the zero/carry, `BTQ`, and `CMSSI`
filters.  It does not by itself insert pass rows while `PROJ` or `INV` is
unprinted.

Proof.

Lemma 120.6 gives the closed and parked subgates.  The carried pass statement
is Definition 106.7 applied after the source audit: every row with an
unprinted projected multiplier, unprinted inverse slot, or failed
admissibility check is carried.  The coefficient bound is Definition 120.3
combined with \(\Gamma_{SD,max}^{99,+}=2\). `square`

### Corollary 120.8: Next SD-Source Steps

The next `SDSRC+` tasks are:

1. print the finite projected multiplier table
   \(P_{SDdiv}^{120},P_{loop}^{120}\), or certify the minimal
   unit-projection bound \(P_{\theta,max}^{120}\le4\);
2. print the inverse/off-diagonal slots
   \(\mathcal O_{SD}^{99,+}(e)\) for the surviving nonzero `SDdiv` and
   `loop` rows;
3. delete rows assigned to exact zero, `BTQ`, `CMSSI`, retraction, or carry;
4. only then compute

   ```math
   \mathcal E_{SD,pass}^{99,+},
   \qquad
   A_{SD,pass}^{99,+},
   \qquad
   \Omega_{SD}^{99,+},
   \qquad
   \chi_{dec}^{SD}.
   ```

If `PROJ` and `INV` remain unprinted, the SD source has been algebraically
reduced but still contributes no licensed reduced decay rows.

## 121. Classification Of `SD` Candidates After Source Reduction

This section classifies the structural `SD` candidates into the five
operational buckets requested by the finite-table audit:

```math
\mathrm{SD\text{-}zero},\qquad
\mathrm{SD\text{-}CMSSI},\qquad
\mathrm{SD\text{-}BTQ},\qquad
\mathrm{SD\text{-}carry},\qquad
\mathrm{SD\text{-}pass}.
```

The classification is made under the Section-120 compact-group scalar source.
It distinguishes the **support-growing decay candidates** of Section 118
from same-support `SD` rows in the full Section-106 row map.

### Definition 121.1: Channel Split For SD Rows

Let

```math
\mathcal F_0^{SD,0}:=\{F_1,F_2,F_3\},
\qquad
\mathcal F_{1/2}^{SD,0}:=\{F_4\},
\qquad
\mathcal F_{1}^{SD,0}:=\{F_8\}
```

be the retained channels with

```math
\Gamma_{SD}^{99}(F_i)=0.
```

Let

```math
\mathcal F_0^{SD,+}:=\varnothing,
```

```math
\mathcal F_{1/2}^{SD,+}:=\{F_5,F_6,F_7\},
\qquad
\mathcal F_{1}^{SD,+}:=\{F_9,F_{10},F_{11}\}
```

be the retained channels with nonzero compact-group derivative scalar.
Write

```math
N_0^{SD}(\alpha):=|\mathcal F_\alpha^{SD,0}|,
\qquad
N_+^{SD}(\alpha):=|\mathcal F_\alpha^{SD,+}|.
```

Thus

```math
N_0^{SD}(0)=3,\quad N_+^{SD}(0)=0,
```

and

```math
N_0^{SD}({1\over2})=N_0^{SD}(1)=1,
\qquad
N_+^{SD}({1\over2})=N_+^{SD}(1)=3.
```

### Definition 121.2: Classifier On Support-Growing SD Candidates

Let

```math
e=e_{SD}^{118}(\bar v;i,\theta,S,w,\upsilon)
\in
\mathcal E_{SD,dec}^{118,str},
```

so \(S\not\subseteq L\) and \(\theta\in\{\mathrm{Cas},\mathrm{SDdiv},\mathrm{loop}\}\).
Write \(\chi=F_i\).

Assign \(e\) as follows.

1. **Zero.**  Put \(e\in\mathrm{SD\text{-}zero}\) if either:

   ```math
   \theta=\mathrm{Cas},
   ```

   because support-growing Casimir candidates are inactive over-cover rows
   for the strict Casimir self-row source; or

   ```math
   \theta\in\{\mathrm{SDdiv},\mathrm{loop}\},
   \qquad
   \chi\in\mathcal F_\alpha^{SD,0}.
   ```

   The second condition is the compact-group derivative-channel zero
   \(\Gamma_{SD}^{99}(\chi)=0\).  It uses only the finite scalar printed in
   Definition 106.3; no numerical projected multiplier is needed beyond the
   finite retained-projection declaration.

2. **CMSSI.**  Put no support-growing candidate into `SD-CMSSI`:

   ```math
   \mathrm{SD\text{-}CMSSI}\cap\mathcal E_{SD,dec}^{118,str}
   =
   \varnothing.
   ```

   CMSSI rows have \(\Delta_X=0\).  Section-118 decay candidates have
   \(\Delta_X=|S\setminus L|\ge1\).

3. **BTQ.**  Put no support-growing candidate into `SD-BTQ`:

   ```math
   \mathrm{SD\text{-}BTQ}\cap\mathcal E_{SD,dec}^{118,str}
   =
   \varnothing.
   ```

   `BTQ` rows are internal bounded-collar rows and have no reduced escaping
   support increment.

4. **Carry.**  If

   ```math
   \theta\in\{\mathrm{SDdiv},\mathrm{loop}\},
   \qquad
   \chi\in\mathcal F_\alpha^{SD,+},
   ```

   then put \(e\in\mathrm{SD\text{-}carry}\) unless both the projected
   multiplier and inverse slot are printed:

   ```math
   P_\theta^{120}(\omega,\chi)\ \text{printed and finite},
   \qquad
   \mathcal O_{SD}^{99,+}(e)\ \text{printed and finite}.
   ```

   Failed no-double-charge or same-record admissibility checks also send the
   row to `SD-carry`.

5. **Pass.**  Put \(e\in\mathrm{SD\text{-}pass}\) exactly when the live
   nonzero row satisfies

   ```math
   \theta\in\{\mathrm{SDdiv},\mathrm{loop}\},
   \qquad
   \chi\in\mathcal F_\alpha^{SD,+},
   ```

   ```math
   P_\theta^{120}(\omega,\chi)<\infty,
   \qquad
   \mathcal O_{SD}^{99,+}(e)<\infty,
   ```

   and all no-double-charge and same-record admissibility checks pass.

This is an exhaustive disjoint classification of
\(\mathcal E_{SD,dec}^{118,str}\).

### Table 121.3: Support-Growing SD Candidate Counts

Let

```math
W_{99}:=|\mathsf W_{\le4}^{99}|,
\qquad
B_{SD}^{118}(L)=2^{81}-2^{|L|}.
```

For a fixed source vertex \(\bar v=(T,\alpha,L,h,p,\sigma)\), the support
growing SD candidates have the following structural counts.

| source \(\alpha\) | `SD-zero-CasEsc` | `SD-zero-derchan` | live nonzero `SDdiv/loop` |
| --- | --- | --- | --- |
| \(0\) | \(48W_{99}B_{SD}^{118}(L)\) | \(96W_{99}B_{SD}^{118}(L)\) | \(0\) |
| \(1/2\) | \(64W_{99}B_{SD}^{118}(L)\) | \(32W_{99}B_{SD}^{118}(L)\) | \(96W_{99}B_{SD}^{118}(L)\) |
| \(1\) | \(64W_{99}B_{SD}^{118}(L)\) | \(32W_{99}B_{SD}^{118}(L)\) | \(96W_{99}B_{SD}^{118}(L)\) |

The first column is

```math
16W_{99}B_{SD}^{118}(L)N_{fus}(\alpha),
```

coming from \(\theta=\mathrm{Cas}\).  The second column is

```math
2\cdot16W_{99}B_{SD}^{118}(L)N_0^{SD}(\alpha),
```

coming from the two derivative families `SDdiv` and `loop` in zero
channels.  The third column is

```math
2\cdot16W_{99}B_{SD}^{118}(L)N_+^{SD}(\alpha),
```

coming from the two derivative families in nonzero channels.  The row sums
agree with Table 118.6.

### Definition 121.4: Classifier On Same-Support SD Rows

For completeness, the same classifier on the full Section-106 row map handles
rows with \(\Delta_X=0\) as follows.

1. `SD-BTQ`: rows internal to the declared `BTQ/ACTFULLLAW` state.
2. `SD-CMSSI`: nonzero same-support rows with finite projected coefficient
   and finite inverse slot, not internal to `BTQ`.
3. `SD-zero`: exact compact-group zeros, including trivial Casimir rows and
   derivative-channel zeroes.
4. `SD-carry`: retraction rows, unprinted projected multipliers, unprinted
   inverse slots, failed admissibility checks, representation tails, and
   any row outside the active same-record law.
5. `SD-pass`: empty for \(\Delta_X=0\), because pass rows must be reduced
   escaping rows.

Thus `SD-CMSSI` and `SD-BTQ` are real buckets for the full SD row map, but
they are empty on the Section-118 support-growing decay-candidate table.

### Theorem 121.5: Current Classification Verdict

On the current carried branch, the support-growing SD candidates classify as
follows.

```math
\mathrm{SD\text{-}CMSSI}
\cap
\mathcal E_{SD,dec}^{118,str}
=\varnothing,
\qquad
\mathrm{SD\text{-}BTQ}
\cap
\mathcal E_{SD,dec}^{118,str}
=\varnothing.
```

The certified zero set is

```math
\mathrm{SD\text{-}zero}^{121}
=
\{\theta=\mathrm{Cas}\}
\cup
\{\theta\in\{\mathrm{SDdiv},\mathrm{loop}\},
\ \chi\in\mathcal F_\alpha^{SD,0}\}.
```

The only live nonzero structural candidates are

```math
\mathrm{SD\text{-}live}^{121}
=
\{\theta\in\{\mathrm{SDdiv},\mathrm{loop}\},
\ \chi\in\mathcal F_\alpha^{SD,+}\}.
```

Since `SDSRC-PROJ` and `SDSRC-INV` are still unprinted, the current licensed
pass set is empty:

```math
\boxed{
\mathrm{SD\text{-}pass}^{121,car}=\varnothing.
}
```

All live nonzero structural candidates are therefore carried:

```math
\boxed{
\mathrm{SD\text{-}carry}^{121,car}
=
\mathrm{SD\text{-}live}^{121}.
}
```

Proof.

Definition 121.2 is a direct specialization of the row-source functional of
Definition 120.2 and the tags of Definition 120.4.  Support-growing
structural candidates have \(\Delta_X\ge1\), so they cannot be `CMSSI` or
`BTQ` rows.  The Casimir self-source is same-support, hence support-growing
Casimir rows are inactive over-cover rows.  The compact-group derivative
scalar \(\Gamma_{SD}^{99}\) vanishes exactly on
\(\mathcal F_\alpha^{SD,0}\), giving the derivative zeroes.  The remaining
`SDdiv/loop` rows are exactly \(\mathcal F_\alpha^{SD,+}\).  Table 106.6
requires finite projected coefficients and inverse slots before any such row
is pass; Section 120 leaves both `PROJ` and `INV` unprinted.  Therefore the
current pass set is empty and the live nonzero structural candidates are
carried. `square`

### Corollary 121.6: Consequence For The Reduced Decay Source

`SDSRC+` currently contributes no licensed reduced decay rows:

```math
\chi_{dec}^{SD}=0
\qquad
\text{on the Section-108/120 carried branch.}
```

If `PROJ` and `INV` are later printed, then only the live nonzero rows in
\(\mathrm{SD\text{-}live}^{121}\) can enter
\(\mathcal E_{SD,pass}^{99,+}\).  In particular:

1. no source-channel-\(\alpha=0\) support-growing SD row can become pass;
2. possible SD pass rows occur only for source channels
   \(\alpha=1/2\) and \(\alpha=1\);
3. their coefficient base is bounded by Theorem 120.7, and by \(8\) under
   the minimal unit-projection convention.

Thus the next SD-specific task is not another classification step.  It is to
print or bound the projected multiplier and inverse tables for the live rows:

```math
P_{SDdiv}^{120},\quad P_{loop}^{120},
\qquad
\mathcal O_{SD}^{99,+}.
```

## 122. Survival Audit For \(\Delta_X\ge1\) `SD` Rows

The question "do any \(\Delta_X\ge1\) `SD` rows survive?" has two different
honest meanings.  This section separates them.

1. **Structural survival.**  A row survives the finite source reductions if it
   is a support-growing Section-118 `SD` candidate and is not killed by the
   exact-zero, `CMSSI`, or `BTQ` classifiers.
2. **Licensed survival.**  A row survives as an actual reduced pass row if, in
   addition, its projected multiplier and same-shell inverse slot are printed
   and all admissibility checks pass.

The first notion asks whether there is still a finite algebraic object worth
printing.  The second asks whether that object can already be spent in the
decay inequality.

### Definition 122.1: Structural Survivor Set

For a fixed source vertex \(\bar v=(T,\alpha,L,h,p,\sigma)\), define

```math
\mathcal E_{SD,\Delta}^{122,str}(\bar v)
:=
\mathcal E_{SD,dec}^{118,str}(\bar v)
\setminus
\left(
\mathrm{SD\text{-}zero}^{121}
\cup
\mathrm{SD\text{-}CMSSI}
\cup
\mathrm{SD\text{-}BTQ}
\right).
```

Equivalently,

```math
\mathcal E_{SD,\Delta}^{122,str}(\bar v)
=
\left\{
e_{SD}^{118}(\bar v;i,\theta,S,w,\upsilon):
\theta\in\{\mathrm{SDdiv},\mathrm{loop}\},
\ \chi=F_i\in\mathcal F_\alpha^{SD,+},
\ S\not\subseteq L
\right\}.
```

Here

```math
\mathcal F_0^{SD,+}=\varnothing,
\qquad
\mathcal F_{1/2}^{SD,+}=\{F_5,F_6,F_7\},
\qquad
\mathcal F_1^{SD,+}=\{F_9,F_{10},F_{11}\}.
```

### Lemma 122.2: Exact Count Of Structural Survivors

Let

```math
W_{99}:=|\mathsf W_{\le4}^{99}|,
\qquad
B_{SD}^{118}(L):=2^{81}-2^{|L|}.
```

Then

```math
N_{SD,surv}^{122}(\bar v)
:=
|\mathcal E_{SD,\Delta}^{122,str}(\bar v)|
=
32\,W_{99}\,B_{SD}^{118}(L)\,N_+^{SD}(\alpha),
```

where

```math
N_+^{SD}(0)=0,
\qquad
N_+^{SD}(1/2)=3,
\qquad
N_+^{SD}(1)=3.
```

Thus

| source \(\alpha\) | structural \(\Delta_X\ge1\) `SD` survivors |
| --- | --- |
| \(0\) | \(0\) |
| \(1/2\) | \(96\,W_{99}B_{SD}^{118}(L)\) |
| \(1\) | \(96\,W_{99}B_{SD}^{118}(L)\) |

Proof.  Table 121.3 already gives the live nonzero `SDdiv/loop` count as

```math
2\cdot16\,W_{99}B_{SD}^{118}(L)N_+^{SD}(\alpha).
```

These and only these rows remain after removing the `Cas` zeroes and the
derivative-channel zeroes.  Since every Section-118 decay candidate has
\(\Delta_X=|S\setminus L|\ge1\), none can be `CMSSI` or `BTQ`.  Substituting
the three values of \(N_+^{SD}(\alpha)\) gives the table. `square`

### Corollary 122.3: When Structural Survivors Exist

Because

```math
B_{SD}^{118}(L)=2^{81}-2^{|L|},
```

the structural survivor set is nonempty exactly when

```math
\alpha\in\{1/2,1\},
\qquad
|L|<81,
\qquad
W_{99}>0.
```

The last condition is automatic for the declared finite word list
\(\mathsf W_{\le4}^{99}\).  If \(L=\mathsf Q_{loc}^{99}\), then
\(|L|=81\) and no local support-growing `SD` row exists; the local frontier is
already full inside the over-refined stencil.

### Definition 122.4: Licensed Survivor Set

Define the currently spendable support-growing `SD` rows by

```math
\mathcal E_{SD,\Delta}^{122,lic}(\bar v)
:=
\left\{
e\in\mathcal E_{SD,\Delta}^{122,str}(\bar v):
P_\theta^{120}(\omega,\chi)<\infty,\ 
\mathcal O_{SD}^{99,+}(e)<\infty,\ 
\mathrm{Adm}_{SD}^{122}(e)=1
\right\}.
```

Here \(\theta\in\{\mathrm{SDdiv},\mathrm{loop}\}\), and
\(\mathrm{Adm}_{SD}^{122}\) denotes the no-double-charge, same-record, and
active-law admissibility filters inherited from Sections 99, 106, and 120.

### Theorem 122.5: Structural Survival Yes, Licensed Survival No

On the current carried strict branch,

```math
\boxed{
\mathcal E_{SD,\Delta}^{122,str}(\bar v)\ne\varnothing
\quad
\text{for }\alpha\in\{1/2,1\},\ |L|<81.
}
```

However,

```math
\boxed{
\mathcal E_{SD,\Delta}^{122,lic}(\bar v)=\varnothing
\quad
\text{for every current source vertex }\bar v.
}
```

Proof.  The first statement is Corollary 122.3.  For the second, Section 120
leaves both required spendability tables unprinted:

```math
P_{SDdiv}^{120},\quad P_{loop}^{120},
\qquad
\mathcal O_{SD}^{99,+}.
```

The paper therefore has live structural rows but no licensed `SD-pass` rows.
This is exactly the carried-branch verdict of Theorem 121.5, now restricted
to \(\Delta_X\ge1\). `square`

### Corollary 122.6: Reduced Decay Contribution At This Stage

The `SD` block contributes no certified reduced decay mass at the present
stage:

```math
\chi_{dec}^{SD}=0
\qquad
\text{on the current carried branch.}
```

If the projected multiplier and inverse tables are later printed, then the
only rows that can change this verdict are precisely
\(\mathcal E_{SD,\Delta}^{122,str}\).  Hence the next finite task is narrow:
ignore \(\alpha=0\), ignore `Cas`, ignore derivative-channel zeroes, and print
or bound only the nonzero `SDdiv/loop` survivor rows for
\(\alpha=1/2,1\) with \(S\not\subseteq L\).

## 123. Projected-Multiplier Attack For The `SDSRC+` Survivors

Section 122 reduced the decay-eligible `SDSRC+` problem to the live rows

```math
\theta\in\{\mathrm{SDdiv},\mathrm{loop}\},
\qquad
\chi\in
\{F_5,F_6,F_7,F_9,F_{10},F_{11}\},
\qquad
S\not\subseteq L.
```

This section attacks the first of the two missing spendability inputs:

```math
P_{SDdiv}^{120}(\omega,\chi),
\qquad
P_{loop}^{120}(\omega,\chi).
```

The proof has to remain finite-record and whole-process.  The unprojected
Schwinger-Dyson identity from Paper 14 is exact, but Paper 14 explicitly
separates that identity from the finite-battery projection problem.  Therefore
there are only two honest branches:

1. print the literal projected multiplier table;
2. adopt an explicit minimal retained-word projection certificate and use its
   envelope.

There is no third branch in which the exact unprojected identity silently
licenses projected pass rows.

### Definition 123.1: Minimal Retained-Word Projection Certificate

For the support-growing survivor rows of Definition 122.1, define

```math
\mathrm{SDPROJ}^{min}_{123}
```

to be the following finite certificate.

1. Retained representation channels are exactly
   \(\Lambda_*^{99}=\{0,1/2,1\}\), with the unit `SU(2)` multiplicities of
   Definition 99.4.
2. The projected derivative or loop expression is expanded only on retained
   scalar trace words \(w\in\mathsf W_{\le4}^{99}\).
3. A single left-invariant derivative can hit at most the occurrences of the
   selected oriented link inside \(w\).
4. Off-word, off-cutoff, and nonretained representation terms are not
   projected into pass rows; they are carried in the already named
   representation/projection tail ledger.
5. No normal-form source or target insertion multiplier is charged inside
   `SDSRC+`; such factors, if used, must be named outside this certificate.

This is a finite projection convention, not a continuum Yang-Mills input.
It chooses what the retained projected ledger means on the already frozen
finite battery.

### Lemma 123.2: Projected-Multiplier Bound Under The Minimal Certificate

If \(\mathrm{SDPROJ}^{min}_{123}\) is supplied, then every support-growing
survivor row satisfies

```math
|P_{SDdiv}^{120}(\omega,\chi)|\le4,
\qquad
|P_{loop}^{120}(\omega,\chi)|\le4.
```

Proof.  The retained word has length at most four:
\(w\in\mathsf W_{\le4}^{99}\).  A one-link left derivative can create at most
one retained contribution per occurrence of the selected oriented link in
that word.  The `SU(2)` retained Clebsch-Gordan multiplicities in
\(\Lambda_*^{99}\) are all one.  Thus the absolute projected coefficient is
bounded by the number of relevant link occurrences in \(w\), which is at most
four.  Any term outside the retained word or representation cutoff is not
folded into the pass coefficient under Definition 123.1; it is carried.
`square`

### Definition 123.3: Live Channel Scalars

For the six live survivor channels, Definition 106.3 gives the exact scalar

```math
\Gamma_{SD}^{99}(\mu,\lambda,\mu')
={1\over2}\left(C_2(\mu')-C_2(\mu)-C_2(\lambda)\right),
\qquad
C_2(j)=j(j+1).
```

The values are:

| channel | \((\mu,\lambda,\mu')\) | \(\Gamma_{SD}^{99}\) | coefficient bound under \(\mathrm{SDPROJ}^{min}_{123}\) |
| --- | --- | --- | --- |
| \(F_5\) | \((1/2,1/2,0)\) | \(-3/4\) | \(\le3\) |
| \(F_6\) | \((1/2,1/2,1)\) | \(1/4\) | \(\le1\) |
| \(F_7\) | \((1/2,1,1/2)\) | \(-1\) | \(\le4\) |
| \(F_9\) | \((1,1/2,1/2)\) | \(-1\) | \(\le4\) |
| \(F_{10}\) | \((1,1,0)\) | \(-2\) | \(\le8\) |
| \(F_{11}\) | \((1,1,1)\) | \(-1\) | \(\le4\) |

The last column bounds both `SDdiv` and `loop` rows, because both use the
same compact-group channel scalar and the same retained-word projection
envelope.

### Theorem 123.4: Sharp Support-Growing `SDSRC` Coefficient Envelope

Under \(\mathrm{SDPROJ}^{min}_{123}\), every structural survivor

```math
e\in\mathcal E_{SD,\Delta}^{122,str}
```

has a finite projected coefficient satisfying

```math
|\mathcal K_{SD}^{120}(e)|
\le
4|\Gamma_{SD}^{99}(\chi)|
\le8.
```

Consequently,

```math
\boxed{
A_{SD,proj}^{123}\le8.
}
```

The bound \(8\) is attained only by the retained channel \(F_{10}\) at the
level of this envelope.

Proof.  For `SDdiv` and `loop` rows, Definition 120.2 gives

```math
\mathcal K_{SD}^{120}(e)
=
\Gamma_{SD}^{99}(\chi)P_\theta^{120}(\omega,\chi),
\qquad
\theta\in\{\mathrm{SDdiv},\mathrm{loop}\}.
```

Lemma 123.2 bounds \(|P_\theta^{120}|\) by \(4\), and Definition 123.3 prints
the live channel scalars.  Their largest absolute value is \(2\), on
\(F_{10}\).  Hence \(|\mathcal K_{SD}^{120}|\le8\). `square`

### Corollary 123.5: What This Does And Does Not Close

If \(\mathrm{SDPROJ}^{min}_{123}\) is accepted as the active projected-ledger
certificate, then the support-growing projected-multiplier obstruction is
closed at the envelope level:

```math
\mathrm{PARK\text{-}SDSRC\text{-}PROJ}^{120,+}
\quad\leadsto\quad
\mathrm{P21\text{-}SDSRC\text{-}PROJENV}^{123,+}(8)
```

for the decay-eligible survivor rows.

If the paper demands literal row values instead of the minimal envelope, then
the remaining requirement is the finite table

```math
P_{SDdiv}^{120}(\omega,F_i),\quad
P_{loop}^{120}(\omega,F_i),
\qquad
i\in\{5,6,7,9,10,11\},
```

restricted to \(S\not\subseteq L\).

In neither branch does Theorem 123.4 license pass rows by itself.  A pass row
still needs the same-shell inverse/off-diagonal slot
\(\mathcal O_{SD}^{99,+}(e)\) and the no-double-charge admissibility tag.

## 124. Same-Shell Inverse Attack For `SDSRC+`

After Section 123, the only potentially decisive `SDSRC+` obstruction for
decay-eligible rows is the inverse slot

```math
\mathcal O_{SD}^{99,+}(e),
\qquad
e\in\mathcal E_{SD,\Delta}^{122,str}.
```

This section checks whether the existing papers already supply it.

### Lemma 124.1: Paper 14 Does Not Print The Section-99 Inverse Slots

Paper 14 supplies exact finite compact-group Schwinger-Dyson identities and
defines projected ledgers, but it does not print the rowwise inverse table

```math
e\longmapsto\mathcal O_{SD}^{99,+}(e)
```

for the over-refined Section-99/106 row map.

Proof.  Paper 14 Theorem 10.2 is an integration-by-parts identity before
finite projection.  Paper 14 Definition 12.1 defines a projected ledger and
places off-battery terms into a projection defect.  Paper 14 Honest Boundary
10.6 and Honest Boundary 12.5 explicitly identify projection control,
compatibility, and determinacy as the remaining hard tasks.  None of these
statements prints a finite right inverse for the Section-99 same-shell
`SD` rows. `square`

### Lemma 124.2: Paper 16 Does Not Supply The `SD` Inverse Slot

Paper 16 supplies finite-template local gauge and heat-kernel/RG closure
technology, but it does not identify a rowwise inverse slot for the
projected compact-group `SDdiv/loop` survivor rows of Section 122.

Proof.  The Paper-16 inverse constructions are local template and transport
devices for the finite-record RG closure.  They are not the projected
Schwinger-Dyson same-shell inverse matrix of the Section-99 retained
`SD` row graph.  Using them here would require an additional same-record
transfer theorem identifying the Paper-16 inverse coordinates with
\(\mathcal O_{SD}^{99,+}\).  No such rowwise transfer table is printed in the
current corpus. `square`

### Lemma 124.3: Paper 20 Does Not Supply The `SD` Inverse Slot

Paper 20 supplies coefficient-normalization, surface-expansion, and
heat-kernel comparison audits for the actual `SEL2` branch.  It does not
print \(\mathcal O_{SD}^{99,+}\) for the Section-122 survivor rows.

Proof.  The Paper-20 objects are scalar coefficient and surface-entry
ledgers.  They do not define the Section-99 same-shell inverse matrix for
projected compact-group `SDdiv/loop` rows.  Importing such a matrix from
Paper 20 would double-charge or conflate the coefficient/surface audit with
the finite `SDSRC+` source-value gate. `square`

### Definition 124.4: The Exact Finite Inverse Certificate Needed

The missing finite object is:

```math
\mathrm{SDINV}_{124}
:=
\left\{
\mathcal O_{SD}^{99,+}(e):
e\in\mathcal E_{SD,\Delta}^{122,str}
\right\},
```

together with an admissibility tag

```math
\mathrm{Adm}_{SD}^{124}(e)\in\{0,1\}
```

confirming that the row is evaluated on the same pushed-forward scalar law,
does not duplicate an `ACTSRC`, `CMPSRC`, `BTQ`, `CMSSI`, RP/Cov, readout, or
projection-tail debit, and is not a retraction or representation-tail row.

If this table is printed and finite, define

```math
O_{SD,surv}^{124}
:=
\begin{cases}
\max_{e\in\mathcal E_{SD,\Delta}^{122,str}}
\mathcal O_{SD}^{99,+}(e),&
\mathcal E_{SD,\Delta}^{122,str}\ne\varnothing,\\
0,&
\mathcal E_{SD,\Delta}^{122,str}=\varnothing.
\end{cases}
```

### Theorem 124.5: Current Corpus Cannot License `SDSRC+` Pass Rows

From the current corpus alone,

```math
\boxed{
\mathrm{SDINV}_{124}\ \text{is not supplied}.
}
```

Therefore, even under the minimal projected-coefficient envelope of Theorem
123.4,

```math
\boxed{
\mathcal E_{SD,\Delta}^{122,lic}=\varnothing.
}
```

Proof.  Lemmas 124.1--124.3 exhaust the plausible source papers named in the
current dependency chain.  Sections 106, 120, 121, and 122 define the inverse
slot and classify its role, but they do not print its finite values.  Table
106.6 and Definition 122.4 require a finite inverse slot before a row can be
assigned `SD-pass`.  Hence every live structural survivor remains carried.
`square`

## 125. Final `SDSRC+` Verdict

The `SDSRC+` audit is now closed in the following precise sense: there is no
remaining informal bucket.  The support-growing `SD` source is either a
conditional finite certificate or a parked finite inverse/projection
obstruction.

### Theorem 125.1: Conditional `SDSRC+` Pass Gate

Let the source vertex satisfy \(\alpha\in\{1/2,1\}\) and \(|L|<81\).  Suppose
the following finite certificate is supplied on the active `SEL2` scalar law:

```math
\mathrm{SDPROJ}_{125}
\quad\text{and}\quad
\mathrm{SDINV}_{124},
```

where \(\mathrm{SDPROJ}_{125}\) is either the literal table
\(P_{SDdiv}^{120},P_{loop}^{120}\) on the Section-122 survivor set or the
minimal envelope certificate \(\mathrm{SDPROJ}^{min}_{123}\), and
\(\mathrm{SDINV}_{124}\) is Definition 124.4.

Then the licensed support-growing `SD` pass set is exactly

```math
\mathcal E_{SD,\Delta}^{125,pass}
=
\left\{
e\in\mathcal E_{SD,\Delta}^{122,str}:
\mathcal O_{SD}^{99,+}(e)<\infty,\ 
\mathrm{Adm}_{SD}^{124}(e)=1
\right\}.
```

Under \(\mathrm{SDPROJ}^{min}_{123}\), its coefficient base obeys

```math
\boxed{
A_{SD,pass}^{125}\le8.
}
```

Proof.  The structural survivor set is Theorem 122.5.  The coefficient bound
is Theorem 123.4.  The inverse and admissibility requirements are exactly
Definition 124.4 and Table 106.6.  No other `SD` structural row can enter:
`Cas` support-growing rows are zero, derivative-channel-zero rows have
\(\Gamma_{SD}^{99}=0\), and same-support rows have \(\Delta_X=0\) and are
not reduced escaping pass rows. `square`

### Theorem 125.2: Unconditional Present-Corpus Verdict

Without an additional finite inverse certificate, the present-corpus verdict
is

```math
\boxed{
\mathcal E_{SD,pass}^{125,current}=\varnothing,
\qquad
\chi_{dec}^{SD}=0.
}
```

The decay-eligible support-growing part of the parked `SDSRC+` term is now
sharpened to

```math
\boxed{
\mathrm{PARK\text{-}SDSRC}_{\Delta}^{+}
=
\mathrm{P21\text{-}SDSRC\text{-}CGSCAL}^{120,+}
+
\mathrm{P21\text{-}SDSRC\text{-}SURV}^{122,+}
+
\mathrm{P21\text{-}SDSRC\text{-}PROJENV}^{123,+}(8)
+
\mathrm{PARK\text{-}SDSRC\text{-}INV}^{124,+}
}
```

if the minimal retained-word projection certificate is adopted.  If the paper
does not adopt that certificate, replace
\(\mathrm{P21\text{-}SDSRC\text{-}PROJENV}^{123,+}(8)\) by
\(\mathrm{PARK\text{-}SDSRC\text{-}PROJ}^{120,+}\).

Proof.  The scalar source and zero/carry classification are closed by
Sections 120--122.  The projection envelope is closed conditionally by
Section 123.  The inverse slot is not supplied by the current corpus by
Theorem 124.5.  Therefore the current licensed pass set is empty and the SD
decay contribution remains zero. `square`

### Corollary 125.3: What To Do Next

`SDSRC+` should not be attacked again at the scalar-identity level.  That
part is done.  The next useful move is one of:

1. print \(\mathrm{SDINV}_{124}\) for the six live channels
   \(F_5,F_6,F_7,F_9,F_{10},F_{11}\) and support-growing
   `SDdiv/loop` atoms;
2. if literal values are required, print the projected multipliers
   \(P_{SDdiv}^{120},P_{loop}^{120}\) instead of using
   \(\mathrm{SDPROJ}^{min}_{123}\);
3. if neither finite table can be supplied, keep `SDSRC+` parked and move to
   `ACTSRC+` or to a direct reduced-tail theorem.

Thus the issue is settled: `SDSRC+` is not a source of hidden decay in the
current text, but it has a clean finite certificate route with coefficient
base at most \(8\) once the inverse slots are printed.

## 126. Final Envelope Attack For `ACTSRC+`

The `ACTSRC+` obstruction has two possible interpretations.  The first asks
for a literal signed action table; the second asks only for a certified finite
coefficient envelope sufficient to run the reduced pass graph once inverse
and admissibility data are supplied.  The previous sections already show that
the envelope route is the only route presently sourced by Papers 16 and 20.

This section records the envelope route as a closed finite certificate and
prevents it from being confused with literal row values.

### Definition 126.1: Decay-Eligible Action Survivor Rows

Let

```math
\mathcal E_{act,\Delta}^{126,str}
```

be the structural action candidates of Definition 118.3 satisfying

```math
\alpha=\mu,\qquad p\le1,\qquad \Delta_X^{act}(L,\zeta)\ge1.
```

On the strict nonoptional `YM2` branch, remove all rows with
\(\kappa\ne\mathrm{stencil}\), since Definition 119.2 gives them the exact
source-branch zero

```math
\mathcal A_{act}^{119}(e)=0.
```

The remaining structural action survivors are stencil rows whose
support/word/sector tuple may be generated by one of the three nonoptional
`YM2` labels

```math
4,\qquad 33,\qquad J2.
```

This is a structural survivor set only.  A row is not licensed as pass until
its coefficient envelope or literal value, inverse slot, and admissibility
tag have all been supplied.

### Definition 126.2: Strict Action Envelope Certificate

Define

```math
\mathrm{ACTENV}_{126}
```

to be the following finite same-record certificate.

1. The active branch is the strict axial-tree, exact-covariance,
   connected/cumulant, minimal-record branch of Paper 16 `HK-SF-YM2`.
2. The only nonoptional labels are \(4,33,J2\).
3. Optional labels \(gf2,cov2,rec2,norm2\) are zero on this strict branch and
   carried outside it.
4. Non-stencil action kinds are zero for this `YM2` source branch.
5. The coupled monomial selector is bounded by Corollary 113.6 and Section
   114:

   ```math
   \Pi_{act}^{113,mon}
   \le
   3\binom{n_A^{113}+3}{4}
   +45\binom{n_A^{113}+2}{3}^{2}
   +\binom{n_A^{113}+1}{2},
   ```

   with

   ```math
   n_A^{113}\le408,
   \qquad
   \log\Pi_{act}^{113,mon}\le36.31.
   ```

6. The local `YM2` vertex envelope is

   ```math
   C_v^{YM2,min}
   =
   24C_4C_{cov}^2
   +18C_3^2C_{cov}^3
   +C_JC_{cov}.
   ```

The fallback all-positive-link cover may be used instead, in which case
\(\log\Pi_{act}^{113,mon}\le39.08\).

### Lemma 126.3: What Papers 16 And 20 Actually Source

Papers 16 and 20 source \(\mathrm{ACTENV}_{126}\) but not a literal signed
action row-value table.

Proof.  Paper 16 Definition 9L.1H and Theorem 9L.1I supply `HK-SF-YM2`,
including the nonoptional labels \(4,33,J2\), optional-label handling, and
the constants \(C_v^{YM2}\) and \(C_v^{YM2,min}\).  Paper 20 imports these
same labels on the active `SEL2` scalar root record and verifies the strict
root template conventions for the scalar interior audit.  In particular,
Paper 20 closes the scalar `GENMATCH`/`HKSD-TPL` route for the interior
Bianchi/off-sheet coefficient source.

None of those statements prints the Section-105 table

```math
\mathcal A_{act}^{119}(e),
\qquad
\mathcal O_{act}^{99,+}(e),
\qquad
\mathsf z_{act}^{99,+},\mathsf c_{act}^{99,+}
```

for each structural action row.  The scalar root cancellation in Paper 20 is
a coefficient-source identity after grouping the finite root labels against a
particular scalar test.  It is not a rowwise reduced pass table for the
Section-104 action graph. `square`

### Theorem 126.4: Closed Action Coefficient Envelope

Under \(\mathrm{ACTENV}_{126}\), every decay-eligible structural action
survivor has the finite coefficient envelope

```math
a_{act,raw}^{126}(e)
\le
B_{act}^{110}\Pi_{act}^{113,mon}C_v^{YM2,min}.
```

Therefore the action envelope coefficient base obeys

```math
\boxed{
A_{act,env}^{126}
\le
\max\left(
1,\,
B_{act}^{110}\Pi_{act}^{113,mon}C_v^{YM2,min}
\right).
}
```

Equivalently, on the active \(n_A^{113}\le408\) branch,

```math
\log A_{act,env}^{126}
\le
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31.
```

Under the all-positive-link fallback, replace \(36.31\) by \(39.08\).

Proof.  Definition 119.2 gives the row-local `YM2` envelope
\(C_{act,row}^{119}(e)\le C_v^{YM2,min}\) after deleting source-branch zero
rows.  Corollary 113.6 and Section 114 bound the number of retained coupled
monomial selector entries by \(\Pi_{act}^{113,mon}\).  The normal-form
multiplier \(B_{act}^{110}\) is the already named action source/target
insertion envelope.  Multiplying these three finite same-record factors gives
the displayed bound. `square`

### Corollary 126.5: DTENS/COVPAIR Are Optional For The Envelope Branch

The literal derivative tensor and covariance-pair tables

```math
\mathfrak M_4^{113},\quad
\mathfrak M_3^{113},\quad
\mathfrak M_J^{113},\quad
\mathfrak M_{33}^{113}
```

are not needed to certify the envelope bound of Theorem 126.4.  They are
needed only if the proof demands literal signed row values, sharper
zero/carry decisions, or a smaller selector surcharge.

Thus the `ACTSRC+` work fork is now:

```math
\text{envelope route: } \mathrm{ACTENV}_{126}
\quad\text{already closed,}
```

```math
\text{literal route: } \mathrm{PARK\text{-}ACTSRC\text{-}DTENS/COVPAIR/ROWVAL}.
```

## 127. Literal `ACTSRC+` Row-Value Audit

The envelope branch is closed, but the user may still demand literal signed
action values.  This section checks whether previous papers already supply
them.

### Definition 127.1: Literal Action Row-Value Certificate

The literal row-value certificate is the finite table

```math
\mathrm{ACTROWVAL}^{lit}_{127}
:=
\left\{
\mathcal A_{act}^{119}(e):
e\in\mathcal E_{act,\Delta}^{126,str}
\right\},
```

together with the derivative tensor and covariance-pair tables needed to
evaluate it:

```math
\mathrm{ACTDTENS}_{127}
:=
(\mathfrak M_4^{113},\mathfrak M_3^{113},\mathfrak M_J^{113}),
```

```math
\mathrm{ACTCOVPAIR}_{127}
:=
\mathfrak M_{33}^{113}.
```

These are finite tables on the already frozen root axial-tree coordinate
alphabet.  They are not continuum limits, random fields, or gauge-coordinate
ontic states; they are record-level proof coordinates.

### Lemma 127.2: Paper 16 Supplies Constants, Not The Literal Tables

Paper 16 does not print \(\mathrm{ACTROWVAL}^{lit}_{127}\),
\(\mathrm{ACTDTENS}_{127}\), or \(\mathrm{ACTCOVPAIR}_{127}\).

Proof.  Paper 16 `HK-SF-YM2` gives a finite second-order vertex ledger and
absolute constants

```math
24C_4C_{cov}^2,\qquad
18C_3^2C_{cov}^3,\qquad
C_JC_{cov}.
```

It also states the strict optional-label reductions.  These are sufficient
for \(\mathrm{ACTENV}_{126}\).  They do not enumerate the nonzero root
derivative tensor entries, the connected covariance pairing list, or the
signed value of every Section-119 action row. `square`

### Lemma 127.3: Paper 20's Rootwise Scalar Cancellation Is Not The Literal Action Table

Paper 20's strict rootwise `GENMATCH`/`HKSD-TPL` proof does not print
\(\mathrm{ACTROWVAL}^{lit}_{127}\).

Proof.  Paper 20 evaluates the grouped scalar root coefficient obtained by
combining the \(4\), \(33\), and \(J2\) labels against the active scalar
coefficient test.  That proves a scalar cancellation/gap statement for the
interior Bianchi/off-sheet contribution.  The Section-119 action table is a
different object: it assigns a signed value to each retained action atom and
channel row before the reduced pass graph is built.  A grouped cancellation
against one scalar test cannot be inverted into a full rowwise action-value
table without an additional finite linear algebra certificate. `square`

### Theorem 127.4: Literal `ACTSRC+` Values Remain Parked

The current corpus does not supply

```math
\mathrm{ACTROWVAL}^{lit}_{127}.
```

The honest status of the literal branch is therefore

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC\text{-}LIT}^{127,+}
=
\mathrm{PARK\text{-}ACTSRC\text{-}DTENS}^{113,+}
+
\mathrm{PARK\text{-}ACTSRC\text{-}COVPAIR}^{113,+}
+
\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL\text{-}LIT}^{119,+}.
}
```

This does not invalidate the envelope branch of Theorem 126.4.  It only
means that any sharper signed cancellation or row deletion must be printed as
a new finite table.

Proof.  Lemmas 127.2 and 127.3 exhaust the two plausible sources: the Paper-16
local vertex ledger and the Paper-20 rootwise scalar audit.  Neither prints
the required rowwise table. `square`

## 128. Action Inverse And Admissibility Audit

Even the closed envelope branch cannot license pass rows without inverse and
admissibility data.  This is the exact analogue of the `SDINV` obstruction,
but for action rows.

### Definition 128.1: Action Inverse Certificate

The finite action inverse certificate is

```math
\mathrm{ACTINV}_{128}
:=
\left\{
\mathcal O_{act}^{99,+}(e):
e\in\mathcal E_{act,\Delta}^{126,str}
\right\},
```

together with an admissibility/zero-carry tag

```math
\mathrm{Adm}_{act}^{128}(e)\in\{0,1\}.
```

The tag equals one only if the row is evaluated under the same pushed-forward
`SEL2` scalar law, does not duplicate `SDSRC`, `CMPSRC`, `BTQ`, `CMSSI`,
RP/Cov, readout, projection-tail, product-tail, or representation-tail
debits, and is not an exact source-branch zero.

If this table is printed and finite, define

```math
O_{act,surv}^{128}
:=
\begin{cases}
\max_{e\in\mathcal E_{act,\Delta}^{126,str}}
\mathcal O_{act}^{99,+}(e),&
\mathcal E_{act,\Delta}^{126,str}\ne\varnothing,\\
0,&
\mathcal E_{act,\Delta}^{126,str}=\varnothing.
\end{cases}
```

### Lemma 128.2: Previous Papers Do Not Print `ACTINV`

Papers 16 and 20 do not print \(\mathrm{ACTINV}_{128}\).

Proof.  Paper 16 contains finite local right-inverse and covariance/template
technology for its RG and small-field ledgers, but it does not identify those
template inverses with the Section-104/105 same-shell inverse slot
\(\mathcal O_{act}^{99,+}\) row by row.  Paper 20 fixes scalar coefficient
rows and proves scalar root cancellations on the strict branch, but it does
not print the off-diagonal inverse table for the reduced action pass graph.
Using either source as `ACTINV` would require a new same-record transfer
theorem that is not currently in the corpus. `square`

### Lemma 128.3: Current Zero/Carry Tags Are Not Enough To License Rows

The current corpus supplies several exact action zero/carry rules:

1. non-stencil rows are zero for the strict nonoptional `YM2` source;
2. optional labels \(gf2,cov2,rec2,norm2\) are zero on the strict branch and
   carried outside it;
3. neutral Jacobian rows with \(\lambda\ne0\) are zero for the \(J2\)
   component;
4. derivative-channel scalar zeroes apply only to components explicitly
   declared derivative-sourced.

These rules delete rows, but they do not license the remaining rows as pass.

Proof.  Table 104.5 requires finite \(a\), finite \(\mathcal O\), and
admissibility before a compatible support-growing action row becomes
`act-pass`.  Zero/carry rules can only remove rows from consideration.  They
do not provide \(\mathcal O_{act}^{99,+}\) for the rows that remain. `square`

### Theorem 128.4: Current Corpus Cannot License `ACTSRC+` Pass Rows

From the current corpus alone,

```math
\boxed{
\mathrm{ACTINV}_{128}\ \text{is not supplied}.
}
```

Therefore, even under the closed envelope certificate
\(\mathrm{ACTENV}_{126}\),

```math
\boxed{
\mathcal E_{act,pass}^{128,current}=\varnothing.
}
```

Proof.  The envelope coefficient bound supplies only \(a(e)\).  Lemma 128.2
shows that the inverse slot is not printed, and Lemma 128.3 shows that the
available zero/carry tags cannot substitute for it.  Table 104.5 then forces
every remaining compatible support-growing action row to stay carried rather
than pass. `square`

## 129. Final `ACTSRC+` Verdict

The action source is now settled in the same sense as `SDSRC+`: the scalar
and envelope pieces are no longer vague, but the current corpus still lacks
the finite inverse/admissibility package needed to create pass rows.

### Theorem 129.1: Conditional `ACTSRC+` Pass Gate

Assume the strict branch and suppose the finite certificates

```math
\mathrm{ACTENV}_{126}
\quad\text{and}\quad
\mathrm{ACTINV}_{128}
```

are supplied on the active `SEL2` scalar law.  Then the licensed
support-growing action pass set is

```math
\mathcal E_{act,\Delta}^{129,pass}
=
\left\{
e\in\mathcal E_{act,\Delta}^{126,str}:
\mathcal O_{act}^{99,+}(e)<\infty,\ 
\mathrm{Adm}_{act}^{128}(e)=1
\right\}.
```

Its envelope coefficient base obeys

```math
\boxed{
A_{act,pass}^{129}
\le
\max\left(
1,\,
B_{act}^{110}\Pi_{act}^{113,mon}C_v^{YM2,min}
\right).
}
```

In particular, with \(n_A^{113}\le408\),

```math
\log A_{act,pass}^{129}
\le
\log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31.
```

If the literal certificates
\(\mathrm{ACTROWVAL}^{lit}_{127}\) and \(\mathrm{ACTINV}_{128}\) are supplied
instead, the same pass definition applies with the literal coefficients in
place of the envelope.

Proof.  The structural action row map is Table 104.5.  The envelope bound is
Theorem 126.4.  The inverse and admissibility requirements are Definition
128.1.  Rows already deleted as zero, `BTQ`, `CMSSI`, product-tail,
representation-tail, or carry are not in the displayed pass set. `square`

### Theorem 129.2: Unconditional Present-Corpus Verdict

On the current corpus,

```math
\boxed{
\mathcal E_{act,pass}^{129,current}=\varnothing,
\qquad
\chi_{dec}^{act}=0.
}
```

The decay-eligible support-growing part of the parked `ACTSRC+` term is now
sharpened to

```math
\boxed{
\mathrm{PARK\text{-}ACTSRC}_{\Delta}^{+}
=
\mathrm{P21\text{-}ACTSRC\text{-}ROWENV}^{119,+}
+
\mathrm{P21\text{-}ACTSRC\text{-}ROOTCOUNT}^{114,+}(n_A^{113}\le408)
+
\mathrm{P21\text{-}ACTSRC\text{-}ACTENV}^{126,+}
+
\mathrm{PARK\text{-}ACTSRC\text{-}INV}^{128,+}
+
\mathrm{PARK\text{-}ACTSRC\text{-}ADM/ZC}^{128,+}.
}
```

If literal signed values are demanded, add the parked literal branch

```math
\mathrm{PARK\text{-}ACTSRC\text{-}LIT}^{127,+}
=
\mathrm{PARK\text{-}ACTSRC\text{-}DTENS}^{113,+}
+
\mathrm{PARK\text{-}ACTSRC\text{-}COVPAIR}^{113,+}
+
\mathrm{PARK\text{-}ACTSRC\text{-}ROWVAL\text{-}LIT}^{119,+}.
```

Proof.  Sections 119, 114, and 126 close the finite coefficient-envelope
route.  Section 127 proves literal row values are not printed.  Section 128
proves the inverse/admissibility certificate is not supplied.  Therefore no
action row is licensed as pass, and no action reduced-decay contribution can
be computed on the present carried graph. `square`

### Corollary 129.3: What To Do Next

`ACTSRC+` should not be attacked again at the level of the Paper-16 scalar
`YM2` envelope; that part is done.  The next useful action-source move is
one of:

1. print \(\mathrm{ACTINV}_{128}\) and the admissibility/zero-carry tags for
   the envelope-surviving support-growing stencil rows;
2. print the literal derivative/covariance/value tables
   \(\mathrm{ACTROWVAL}^{lit}_{127}\) only if the envelope surcharge in
   Theorem 129.1 is too large;
3. if neither finite table can be supplied, stop spending source effort on
   `ACTSRC+` and move to a direct reduced-tail theorem or to the remaining
   comparison-source bucket.

Thus the `ACTSRC+` issue is settled for the current paper: the available
finite envelope is explicit, the literal row-value route is parked, and the
present obstruction to actual pass rows is the finite same-shell inverse and
admissibility package.

## 130. Final Review Export To Paper 22

Paper 21 stops here as a source-audit paper.  It has grown large because the
obstruction was not a single scalar constant: it was a finite same-record
source-table problem.  The final export must therefore be an import contract,
not another attempt to continue the proof inside this file.

### Theorem 130.1: Paper-21 Export Ledger

On the strict reduced `SEL2` scalar-record branch, Paper 21 exports the
following closed facts to Paper 22.

1. The structural finite row maps are printed on the over-refined vertex cover:

   ```math
   R_{fus}^{99,+},\qquad
   R_{act}^{99,+},\qquad
   R_{SD}^{99,+},\qquad
   R_{cmp}^{99,+}.
   ```

2. The carried finite table has an empty licensed pass graph on the current
   corpus:

   ```math
   \mathcal E_{pass}^{108,current}=\varnothing.
   ```

   Consequently the zero-growth SCC test is closed only vacuously.  It does
   not prove reduced decay and it does not falsify confinement.

3. The `SDSRC+` audit is closed as far as the present corpus permits:

   ```math
   \mathrm{PARK\text{-}SDSRC}_{\Delta}^{+}
   =
   \mathrm{P21\text{-}SDSRC\text{-}CGSCAL}^{120,+}
   +
   \mathrm{P21\text{-}SDSRC\text{-}SURV}^{122,+}
   +
   \mathrm{P21\text{-}SDSRC\text{-}PROJENV}^{123,+}(8)
   +
   \mathrm{PARK\text{-}SDSRC\text{-}INV}^{124,+}.
   ```

   Under the minimal retained-word projection convention, the live projected
   multiplier envelope is bounded by \(8\).  The current corpus still does not
   print the same-shell inverse slots needed to license `SD-pass` rows.

4. The `ACTSRC+` audit is closed at the finite-envelope level:

   ```math
   \mathrm{PARK\text{-}ACTSRC}_{\Delta}^{+}
   =
   \mathrm{P21\text{-}ACTSRC\text{-}ROWENV}^{119,+}
   +
   \mathrm{P21\text{-}ACTSRC\text{-}ROOTCOUNT}^{114,+}(n_A^{113}\le408)
   +
   \mathrm{P21\text{-}ACTSRC\text{-}ACTENV}^{126,+}
   +
   \mathrm{PARK\text{-}ACTSRC\text{-}INV}^{128,+}
   +
   \mathrm{PARK\text{-}ACTSRC\text{-}ADM/ZC}^{128,+}.
   ```

   In particular,

   ```math
   \log A_{act,pass}^{129}
   \le
   \log^+\!\left(B_{act}^{110}C_v^{YM2,min}\right)+36.31
   ```

   once `ACTINV` and admissibility/zero-carry tags are supplied.  Literal
   signed row values require the additional parked branch
   `DTENS/COVPAIR/ROWVAL-LIT`.

5. The comparison source remains the unsolved finite source bucket:

   ```math
   \mathrm{PARK\text{-}CMPSRC}^{+}.
   ```

   Paper 21 printed the structural comparison row map, but it did not print
   the comparison row values, inverse slots, or admissibility tags.

6. No step in Paper 21 imports a Wilson-loop area law, a mass gap, a
   continuum Yang-Mills measure, or an unrecorded local subprocess.  All
   exported data live on the same finite scalar pushed-forward record law.

Proof.  Items 1 and 2 are Sections 103--108.  Item 3 is Theorem 125.2.  Item
4 is Theorem 129.2.  Item 5 is Corollary 107.8 and Section 108.  Item 6 is the
Barandes-aligned boundary of Sections 0, 46--49, 93--99, and 108--129.
`square`

### Corollary 130.2: Paper-22 Continuation Problem

Paper 22 should not be a summary paper.  It should continue from the exact
current obstruction:

```math
\boxed{
\mathrm{PARK\text{-}CMPSRC}^{+}
\quad+\quad
\mathrm{PARK\text{-}COMMON\text{-}INV/ADM}^{+}
\quad+\quad
\mathrm{PARK\text{-}RED\text{-}TAIL}^{+}.
}
```

The immediate Paper-22 tasks are:

1. print the common same-shell inverse/admissibility ledger that can serve
   `ACTSRC+`, `SDSRC+`, and `CMPSRC+` without double charging;
2. close `CMPSRC+` row by row, or park it with the same precision now achieved
   for `ACTSRC+` and `SDSRC+`;
3. rebuild the licensed pass graph after those source packages are supplied;
4. run the zero-growth SCC and reduced coverage tests on the licensed graph,
   not on the carried graph;
5. if the finite pass graph remains empty or too expensive, prove a direct
   reduced-tail theorem upstream of confinement rather than spending further
   constants in the same finite-table route.

This is the correct handoff because the currently missing object is not the
Paper-20 scalar coefficient comparison.  That comparison is already reduced.
The missing object is the finite same-record source/pass graph needed to turn
the reduced source audit into an actual decay theorem.
