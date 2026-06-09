# Relativistic ISP V4 Paper 36: Hardening Summary And Compilation

Author: Felix Robles Elvira

Status: compilation and status-lock paper after Papers 32-35.  This paper
does not introduce a new physical mechanism.  It records exactly what the
GR, QFT, finite QCD, and repair hardening papers now prove inside the active
Barandes-aligned ISP corpus, and exactly which claims remain external bridge
claims.

## 0. Purpose

Searchable purpose tag:

`V4P36-HARDENING-COMPILATION-PURPOSE`.

Papers 32-35 did four different jobs:

$$
\boxed{
\begin{array}{c|l}
\hbox{paper} & \hbox{job}\\
\hline
P32 & \hbox{formal hardening of effective GR descent}\\
P33 & \hbox{formal hardening of relativistic QFT kinematics}\\
P34 & \hbox{formal hardening of finite QCD dynamics}\\
P35 & \hbox{repair of the load-bearing gates found in P32-P34}
\end{array}
}
$$

Paper 36 is the compilation layer.  Its purpose is to prevent the corpus from
blurring three different statuses:

$$
\boxed{
\begin{array}{c|l}
\hbox{status} & \hbox{meaning}\\
\hline
\mathrm{INTERNAL}_{ISP} &
\hbox{proved inside the active finite-record ontology}\\
\mathrm{BRIDGE} &
\hbox{comparison to standard external GR/QFT/QCD/YM formalisms}\\
\mathrm{FRONTIER} &
\hbox{next target if one wants a more minimal or external theorem}
\end{array}
}
$$

The rule of this paper is:

$$
\boxed{
\hbox{do not count a bridge as an internal theorem, and do not count an
active-corpus theorem as an unconditional theorem from bare stochastic
process theory.}
}
$$

### Continuum-floor status (external review, 2026-05)

The taxonomy above needs one more distinction that the corpus currently blurs:
an $\mathrm{INTERNAL}_{ISP}$ result can still be **conditional on an open
continuum step**.  The Yang-Mills continuum confinement/mass-gap result is in
exactly this position, and it splits cleanly:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{certificate} & \hbox{content} & \hbox{honest status}\\
\hline
\mathrm{RCP28} & \hbox{continuum source-Cauchy/determinacy (existence)} &
\mathrm{INTERNAL}_{ISP}\\
\mathrm{MID28} & \hbox{YM decoder separation/uniqueness} &
\mathrm{INTERNAL}_{ISP}\\
\mathrm{TSP28} & \hbox{positive continuum string tension / mass gap} &
\mathrm{INTERNAL}_{ISP}\hbox{ modulo }t_-\downarrow0\hbox{ floor survival (OPEN)}
\end{array}
}
$$

Two audit findings fix this status:

1. Non-circular.  The ISP suppositions are existence/reconstruction/whole-process
   conditions only; none assumes clustering, a correlation length, a mass scale,
   or a string tension.  So the mass gap is genuinely reduced to a positive
   string-tension floor, not assumed.

2. The floor is established only at fixed smearing.  In the standalone
   consolidation (paper 39, Section 11, row-token Bessel gap `TOK-BESSEL`) the
   floor is proved only at fixed heat-kernel collar time $t_->0$: the detector
   variance (Lemma 11.2a2) and the Casimir/height tail rates (Lemma 11.2a4) are
   positive only because $t_-$ is held away from $0$ and both degrade as
   $t_-\downarrow0$.  Uniform survival as $t_-\downarrow0$ — a positive continuum
   string tension — is the genuine infrared content and coincides with the open
   part of the Clay problem.

Therefore the honest corpus statement is: ISP closes continuum YM *existence and
uniqueness* (RCP28, MID28) and *reduces* the mass gap to a positive continuum
string-tension floor without assuming it, but the floor's $t_-\downarrow0$
survival (TSP28) is the single open step.  "YM proven within ISP" should be read
as "YM existence within ISP, plus a non-circular reduction of the gap to one
open continuum-floor inequality," not as an unconditional internal mass-gap
theorem.

## 1. Active Corpus Packet

Searchable import tag:

`V4P36-ACTIVE-CORPUS-PACKET`.

The post-P35 hardening corpus is:

$$
\boxed{
{\mathbb H}_{36}
=
(P24_{act},P25_{GR},P26_{QFT},P27_{QCD},P28_{YM},P29_{YMh},
P30_{cert},P31_{YMh2},P32_{GRH},P33_{QFH},P34_{QCH},P35_{rep}).
}
$$

The decisive active ontology imported from the GR and certificate papers is:

$$
\boxed{
\begin{array}{c|l}
\hbox{ingredient} & \hbox{role}\\
\hline
A^{*}R^{*}K^{*}E^{*} &
\hbox{finite actual normal form}\\
\mathrm{FAC} &
\hbox{same-actual covariance}\\
\mathrm{SLC} &
\hbox{stable local clock/frame/transport compatibility}\\
\mathrm{RSC} &
\hbox{source/probe/boundary/commutator dictionary completeness}\\
\mathrm{typed\ registry} &
\hbox{extension/anomaly channels must be printed before closure}\\
\mathrm{receipt\ functor} &
\hbox{finite effects must have finite row/source/probe receipts}\\
\mathrm{single\ response\ scale} &
\hbox{GR/source response and QCD row response use the same actual scale}
\end{array}
}
$$

The active-corpus clause is not decorative.  The theorems below are claims
inside this packet.  A critic may reject the packet, but then the criticism
is aimed at the ISP ontology itself, not at a hidden step in P32-P35.

## 2. P32 Compilation: Effective GR

Searchable GR tag:

`V4P36-P32-EFFECTIVE-GR-COMPILATION`.

Paper 32 proves:

$$
\boxed{
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS}
=
\mathrm{CLOSED}_{ISP}
}
$$

inside the active finite-record ontology, after Paper 35 repairs the
low-energy uniqueness hook:

$$
\boxed{
\mathrm{GR\text{-}LEU\text{-}001}
=
\mathrm{PASS}_{ISP}.
}
$$

The internal GR result uses:

$$
\boxed{
\begin{array}{ll}
\mathrm{GR1}:&\hbox{same-actual covariance from FAC}\\
\mathrm{GR2}:&\hbox{torsion-free active SLC branch}\\
\mathrm{GR3}:&\hbox{RSC source/stress dictionary completeness}\\
\mathrm{GR4}:&\hbox{Ward/Bianchi receipt discipline}\\
\mathrm{GR5}:&\hbox{low-energy rank-two divergence-free source-curvature
uniqueness}
\end{array}
}
$$

The cleaned status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\hbox{effective GR inside active ISP} &
\mathrm{CLOSED}_{ISP} &
\hbox{finite actual records have GR as the no-anomaly effective geometry}\\
\hbox{standard GR comparison} &
\mathrm{BRIDGE} &
\hbox{requires external readout gates GEXT1-GEXT8}\\
\hbox{bare stochastic derivation} &
\mathrm{FRONTIER} &
\hbox{would derive the active packet from minimal ISP alone}
\end{array}
}
$$

Thus P32 is strong as an internal ISP theorem, not as an unconditional
standalone derivation of all standard GR from no assumptions.

## 3. P33 Compilation: Relativistic QFT Kinematics

Searchable QFT tag:

`V4P36-P33-QFT-KINEMATICS-COMPILATION`.

Paper 33 proves:

$$
\boxed{
\mathrm{REL\text{-}QFT\text{-}KIN}
=
\mathrm{CLOSED}_{ISP}
}
$$

as finite source-response gluing over the active GR branch.

Paper 35 repaired the two delicate QFT points:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{hook} & \hbox{status} & \hbox{repair}\\
\hline
\mathrm{QFT\text{-}FSRG\text{-}GRAM\text{-}001} &
\mathrm{PASS}_{ISP} &
\hbox{reflection gluing is a positive Gram/kernel construction}\\
\mathrm{QFT\text{-}SPIN\text{-}CPT\text{-}BRIDGE\text{-}001} &
\mathrm{PASS}_{bridge} &
\hbox{standard spin-statistics/CPT are bridge claims, not hidden internal
claims}
\end{array}
}
$$

The cleaned status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\hbox{finite QFT kinematics} &
\mathrm{CLOSED}_{ISP} &
\hbox{source-response fields, locality collars, covariance, positivity}\\
\hbox{standard Hilbert/Wightman/AQFT comparison} &
\mathrm{BRIDGE} &
\hbox{requires QEXT1-QEXT10}\\
\hbox{standard spin-statistics and CPT} &
\mathrm{BRIDGE} &
\hbox{requires spectral/locality/orientation bridge hypotheses}
\end{array}
}
$$

The important correction is that Paper 33 no longer overclaims:

$$
\boxed{
\hbox{exchange/orientation holonomy inside ISP is not by itself the full
standard spin-statistics/CPT theorem.}
}
$$

It becomes the internal structure that the external bridge may identify with
standard QFT spin/CPT behavior.

## 4. P34 Compilation: Finite QCD Dynamics

Searchable QCD tag:

`V4P36-P34-FINITE-QCD-DYNAMICS-COMPILATION`.

Paper 34 proves:

$$
\boxed{
\mathrm{QCD\text{-}DYN}
=
\mathrm{CLOSED}_{finite\ ISP}
}
$$

after Paper 35 discharges:

$$
\boxed{
\mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001}
=
\mathrm{PASS}_{finite\ ISP}.
}
$$

The finite QCD proof chain is now:

$$
\boxed{
\begin{array}{c}
P26/P33\ \mathrm{QFT/YM\ kinematics}\\
\wedge\ P27\ \mathrm{zero\text{-}collapse\ and\ row\ budget}\\
\wedge\ P30\ \mathrm{finite\ receipt\ discipline}\\
\wedge\ P35\ \mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001}\\
\Longrightarrow
P34\ \mathrm{QCD\text{-}DYN}
=
\mathrm{PASS}_{finite\ ISP}.
\end{array}
}
$$

The repaired noncircularity statement is:

$$
\boxed{
\hbox{P34 does not import } \mathrm{QCD\text{-}DYN}=\mathrm{PASS}
\hbox{ from P27 as a premise.}
}
$$

Instead, P34 imports the finite certificate machinery, and P35 proves the
margin certificate.

The cleaned status is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{claim} & \hbox{status} & \hbox{meaning}\\
\hline
\hbox{finite QCD dynamics inside active ISP} &
\mathrm{CLOSED}_{finite\ ISP} &
\hbox{center/singlet/gap row margins pass}\\
\hbox{standard effective QCD comparison} &
\mathrm{BRIDGE} &
\hbox{requires CEXT1-CEXT10}\\
\hbox{continuum YM confinement/mass gap} &
\mathrm{separate\ YM\ descent} &
\hbox{handled by P28-P31, not by P34 alone}
\end{array}
}
$$

## 5. P35 Compilation: Repairs Discharged

Searchable repair tag:

`V4P36-P35-REPAIR-COMPILATION`.

Paper 35 discharges the five review rows:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{row} & \hbox{status} & \hbox{discharge}\\
\hline
\mathrm{RL1} & \mathrm{PASS}_{ISP} &
\mathrm{GR\text{-}LEU\text{-}001}\\
\mathrm{RL2} & \mathrm{PASS}_{ISP} &
\mathrm{QFT\text{-}FSRG\text{-}GRAM\text{-}001}\\
\mathrm{RL3} & \mathrm{PASS}_{bridge} &
\mathrm{QFT\text{-}SPIN\text{-}CPT\text{-}BRIDGE\text{-}001}\\
\mathrm{RL4} & \mathrm{PASS}_{finite\ ISP} &
\mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001}\\
\mathrm{RL5} & \mathrm{PASS} &
\mathrm{NO\text{-}CIRCULAR\text{-}IMPORT\text{-}AUDIT}
\end{array}
}
$$

The load-bearing QCD repair was:

$$
\boxed{
\mathrm{NO\text{-}FREE\text{-}BRANCHING\text{-}001}
=
\mathrm{PASS}_{ISP}.
}
$$

Paper 35 no longer assumes this packet freely.  It derives it through:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{theorem} & \hbox{proves} & \hbox{idea}\\
\hline
6.A & \mathrm{NFB1\text{-}5,NFB8,NFB9} &
\hbox{active branches are finite records with receipt discipline}\\
6.B & \mathrm{NFB6} &
\hbox{receipt faithfulness modulo Ward/vacuum/typed equivalence}\\
6.C & \mathrm{NFB7} &
\hbox{single response-scale lock from GR/source to QCD rows}\\
6.D & \mathrm{NFB1\text{-}9} &
\hbox{no-free-branching packet closes from the active corpus}\\
6.E & \chi_{\alpha}(d)\le(c_{\mathrm{act}}-\eta)d &
\hbox{token-coding entropy bound}
\end{array}
}
$$

Thus the deepest post-review QCD sentence is:

$$
\boxed{
R_{branch}=0
\hbox{ is derived from finite token injectivity plus active scale lock, not
selected after the confinement target.}
}
$$

## 6. Internal Closure Ledger

Searchable closure tag:

`V4P36-INTERNAL-CLOSURE-LEDGER`.

The post-P35 internal ledger is:

$$
\boxed{
\begin{array}{c|c|l}
\hbox{domain} & \hbox{internal status} & \hbox{scope}\\
\hline
\mathrm{effective\ GR} &
\mathrm{CLOSED}_{ISP} &
\hbox{active finite-record no-anomaly GR branch}\\
\mathrm{relativistic\ QFT\ kinematics} &
\mathrm{CLOSED}_{ISP} &
\hbox{finite source-response gluing over active GR}\\
\mathrm{finite\ QCD\ dynamics} &
\mathrm{CLOSED}_{finite\ ISP} &
\hbox{finite center/singlet/gap row dynamics}\\
\mathrm{continuum\ YM\ descent} &
\mathrm{CLOSED}_{ISP\ descent} &
\hbox{relative to P28-P31 certificate closure}\\
\mathrm{standard\ external\ equivalence} &
\mathrm{BRIDGE} &
\hbox{requires the external comparison gates}
\end{array}
}
$$

The phrase "closed" means:

$$
\boxed{
\hbox{closed inside the active ISP finite-record ontology.}
}
$$

It does not mean:

$$
\boxed{
\hbox{an unconditional theorem accepted in standard mathematical physics
without adopting the ISP ontology and bridge maps.}
}
$$

## 7. Bridge Ledger

Searchable bridge tag:

`V4P36-BRIDGE-LEDGER`.

The external bridges are:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{bridge} & \hbox{source paper} & \hbox{meaning}\\
\hline
\mathrm{GEXT1\text{-}GEXT8} & P32 &
\hbox{active ISP effective geometry to standard effective GR}\\
\mathrm{QEXT1\text{-}QEXT10} & P33 &
\hbox{active finite QFT kinematics to standard relativistic QFT frameworks}\\
\mathrm{CEXT1\text{-}CEXT10} & P34 &
\hbox{finite ISP QCD to standard effective QCD observables}\\
\mathrm{EXT1\text{-}EXT9} & P30 &
\hbox{ISP YM descent to standard continuum YM comparison}\\
\mathrm{spin/CPT\ bridge} & P33/P35 &
\hbox{standard spin-statistics/CPT identification}
\end{array}
}
$$

These bridges are not defects.  They are the honest comparison layer between
two languages:

$$
\boxed{
\hbox{finite actual ISP records}
\quad\leftrightarrow\quad
\hbox{standard continuum field-theoretic structures}.
}
$$

The internal theorem can be true even if an external bridge row is incomplete.
But a claim of standard equivalence requires the relevant bridge rows.

## 8. Falsifier Ledger

Searchable falsifier tag:

`V4P36-HARDENING-FALSIFIER-LEDGER`.

The hardening corpus is not protected from failure.  The main falsifiers are:

$$
\boxed{
\begin{array}{c|l|l}
\hbox{falsifier} & \hbox{would show} & \hbox{effect}\\
\hline
F_{GR} &
\hbox{persistent torsion/source cokernel not typed or represented} &
\hbox{P32 active GR closure fails or extends}\\
F_{QFT}^{pos} &
\hbox{finite reflection gluing is not positive after Gram repair} &
\hbox{P33 QFT positivity fails}\\
F_{QFT}^{bridge} &
\hbox{spin/CPT external hypotheses fail} &
\hbox{standard QFT bridge fails, internal ISP kinematics may remain}\\
F_{QCD}^{tok} &
\hbox{two distinct active branches share all receipts but are not equivalent} &
\hbox{NFB6 fails, QCD-DYN fails or typed branch prints}\\
F_{QCD}^{scale} &
\hbox{QCD row response scale differs from GR/source response scale} &
\hbox{NFB7 fails, active QCD margin fails or typed branch prints}\\
F_{circ} &
\hbox{P34 imports QCD-DYN pass as premise} &
\hbox{noncircularity fails}
\end{array}
}
$$

The most serious remaining internal attacks are:

$$
\boxed{
F_{QCD}^{tok}
\quad\hbox{and}\quad
F_{QCD}^{scale}.
}
$$

Paper 35 addresses them by deriving receipt faithfulness and single
response-scale lock from the active corpus.  A future critic must now attack
those derivations directly.

## 9. Consolidated Theorem

Searchable theorem tag:

`V4P36-CONSOLIDATED-HARDENING-THEOREM`.

### Theorem 9.1: P32-P35 Consolidated Hardening

Assume the active Barandes-aligned ISP corpus packet \({\mathbb H}_{36}\).
Then:

$$
\boxed{
\begin{array}{c|c}
\hbox{result} & \hbox{status}\\
\hline
\mathrm{GR\text{-}DYN\text{-}COFINAL\text{-}PASS} &
\mathrm{CLOSED}_{ISP}\\
\mathrm{REL\text{-}QFT\text{-}KIN} &
\mathrm{CLOSED}_{ISP}\\
\mathrm{QCD\text{-}DYN} &
\mathrm{CLOSED}_{finite\ ISP}\\
\mathrm{P32\text{-}P34\ hardening\ repair} &
\mathrm{PASS}_{P35}\\
\mathrm{internal/bridge\ separation} &
\mathrm{PASS}
\end{array}
}
$$

Proof.  P32 gives effective GR closure relative to
\(\mathrm{GR\text{-}LEU\text{-}001}\); P35 proves
\(\mathrm{GR\text{-}LEU\text{-}001}\).  P33 gives finite relativistic QFT
kinematics over the active GR branch; P35 repairs the reflection-gluing
positivity and moves standard spin/CPT to the bridge ledger.  P34 gives
finite QCD dynamics relative to \(\mathrm{QCD\text{-}MARGIN\text{-}CERT\text{-}001}\);
P35 proves the margin certificate by deriving no-free-branching from
actuality receipts, receipt faithfulness, and single response-scale lock.
P35 also proves the no-circular-import audit.  Therefore the P32-P34
hardening layer is consolidated inside the active ISP corpus. `square`

## 10. What Is Not Claimed

Searchable caution tag:

`V4P36-WHAT-IS-NOT-CLAIMED`.

The consolidated hardening theorem does not claim:

$$
\boxed{
\begin{array}{ll}
\mathrm{NC1}:&\hbox{standard GR/QFT/QCD has been replaced without bridge
work};\\
\mathrm{NC2}:&\hbox{the active ISP corpus is forced by bare stochastic
process theory alone};\\
\mathrm{NC3}:&\hbox{standard spin-statistics/CPT follows from exchange
holonomy without spectral/locality bridge hypotheses};\\
\mathrm{NC4}:&\hbox{finite QCD dynamics alone is the full continuum YM
Millennium theorem};\\
\mathrm{NC5}:&\hbox{experimental validation has been supplied by the
formal corpus itself}.
\end{array}
}
$$

The honest claim is:

$$
\boxed{
\hbox{the active ISP finite-record ontology now has a consolidated internal
GR/QFT/QCD hardening layer, with external equivalence claims separated into
bridge gates.}
}
$$

## 11. Next Frontier

Searchable frontier tag:

`V4P36-NEXT-FRONTIER`.

The next work is not another repair of P32-P35.  The repair layer is now
compiled.  The next frontier is:

$$
\boxed{
\begin{array}{c|l}
\hbox{frontier} & \hbox{question}\\
\hline
\mathrm{minimal\ ISP\ derivation} &
\hbox{can the active corpus packet be derived from minimal indivisible
stochastic premises?}\\
\mathrm{external\ equivalence} &
\hbox{can GEXT/QEXT/CEXT/EXT bridge rows be written in standard mathematical
physics language?}\\
\mathrm{experimental\ ledger} &
\hbox{which finite receipt predictions are distinct from standard GR/QFT/QCD?}\\
\mathrm{ontology\ stress\ tests} &
\hbox{black holes, cosmology, horizons, information, singularity replacement}
\end{array}
}
$$

If the next paper stays in hardening mode, it should address minimal ISP
derivation of the active packet.  If it moves to consequences, it should use
the P36 ledger as the stable base and clearly state which consequences are
internal ISP predictions and which are bridge-level comparisons.

## 12. Final Status

Searchable final tag:

`V4P36-FINAL-HARDENING-STATUS`.

The final compilation status is:

$$
\boxed{
\begin{array}{c|c}
\hbox{layer} & \hbox{post-P36 status}\\
\hline
P32 & \mathrm{compiled\ and\ closed}_{ISP}\\
P33 & \mathrm{compiled\ and\ closed}_{ISP}\hbox{ with spin/CPT bridge label}\\
P34 & \mathrm{compiled\ and\ closed}_{finite\ ISP}\\
P35 & \mathrm{repair\ gates\ discharged}\\
P36 & \mathrm{hardening\ summary\ compiled}
\end{array}
}
$$

Therefore:

$$
\boxed{
\mathrm{GR/QFT/QCD\ hardening\ layer}
=
\mathrm{CONSOLIDATED}_{active\ ISP}.
}
$$

The corpus may now either move outward to bridge/external-equivalence work or
move forward to consequence papers using the active ISP ontology as the
working physical base.
