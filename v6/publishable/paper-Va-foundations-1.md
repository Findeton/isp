# Quantum theory from sealed records I: Born composition, Lorentz signature, and the arrow of time

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-14.

## Abstract

We present the foundational layer of a research program that
reconstructs
quantum-mechanical, relativistic, and thermodynamic structure from a
single ontology: a ledger of *sealed records*, governed by three
axioms — **R** (laws are laws of whole sealed histories), **S** (no
distinction without a record), and **C** (couplings are fixed by
self-consistency under refinement).  The program builds on the
stochastic–quantum correspondence of Barandes' indivisible processes,
replacing configuration trajectories by committed records as the
primitive.  Main results at stated scope, each with a
machine-verified receipt in this submission or a tagged
companion/corpus pointer ([C]/[P]): (i) the **Born layer** — record weights compose through
square roots, and the tame-class reconstruction is *argued to* recover
the Weyl algebra and to land in the Schrödinger representation via the
Stone–von Neumann import, from record towers (at tame scope: the
tame-class definition with its growth constants and the boundary
classification are corpus-bound [P]), with ladder
operators, selection rules, and
exact continuum targets approached at machine precision; (ii)
**Lorentz signature** — the commitment structure of records *is argued
to select* a Lorentzian $(1,d)$ split with derived orientation classes (a
structural argument from the commit-order asymmetry, its proof
obligation corpus-bound [P]; the
spatial dimension $d = 3$ is *selected*, by a minimality principle
graded as input in the text, not derived), and the operational
identification lapse $=$ local clock rate is verified to
$3.7\times 10^{-8}$ in curved record geometries (a model-internal
consistency receipt), with first $3{+}1$-dimensional cosmological
checks (qualitative; no cosmological number is claimed in this
batch); (iii) the **arrow of
time** — reflection positivity is a *theorem* for eventless sectors
with finite primitive Markov presentations, the entropy-production
functional is the path-measure relative entropy
$\sigma = D(P_{AB}\Vert P_{BA})$ (the classical identity of
stochastic thermodynamics, here in record-pair form), and the
presentation hypothesis is
*sharp*: an explicit reversible, valid, finite-rank process (the
"record clock") fails reflection positivity, separating record laws
from general reversible processes; (iv) **thermality** — horizon
temperature $T = \kappa/2\pi$ is recovered in exact lattice
constructions, presented in full in the companion [C-VIII] and
cited here only as a consistency credential.  We state precisely what is axiom,
what is theorem, what is named identification, and what is imported
mathematics — the full dependency audit is part of the paper — and
we delimit the program's frontier: the tame class, the regularity
stratum of the emergent continuum, and continuous sector families.

## 1. Introduction

**The starting point.**  Barandes' stochastic–quantum theorem [1]
shows that unitary quantum dynamics on a finite-dimensional Hilbert
space corresponds exactly to *indivisible* stochastic processes —
processes specified by transition data over whole time intervals
rather than composable infinitesimal steps.  This reopens a question
usually closed by fiat: which classical-looking ontology, if any,
stands behind quantum theory's formal apparatus?

This program proposes an answer with a different primitive: not
trajectories, not measurement outcomes, but **records** — definite,
sealed entries in a ledger.  Three axioms govern them:

- **Axiom R (records).**  Physical law assigns weights to whole
  sealed histories of the ledger; "state at a time" is derived
  bookkeeping.
- **Axiom S (silent-seam exclusion).**  Any datum that no sealed
  record registers — a silent label, phase, or holonomy — is not
  part of the physics; constructions requiring one are excluded or
  must be quotiented to gauge.
- **Axiom C (refinement self-consistency).**  Records may be
  refined into finer records; the law's couplings are fixed points
  of the requirement that refined ledgers obey the same law.

R and S are principle-type axioms in Einstein's sense — they forbid
rather than construct; C is of a different kind, a fixed-point
*selection* condition, and we do not claim the principle-theory
mantle for it.  The program's results are *forcing arguments* — some proved as
theorems, others structural arguments resting on named inputs or
corpus-bound proof obligations, as the Section 7 audit records:
structures usually postulated (Hilbert space, signature, reflection
positivity, fermions, gauge groups) appear as the survivors of the
exclusions, *under the inputs and scope premises each layer names*.  This first paper presents the kinematic,
relativistic, and thermodynamic layer; a companion (Part II) treats
statistics and gauge structure; further papers treat the
matter-content selection and its falsifiable consequences.

**Mathematical home, stated first.**  So that nothing rests on
undefined vocabulary, the program's primitives have concrete
mathematical referents.  Two citation registers are used, and we
keep them honestly separate: [C0]–[C4], [C-VIII], [VII], and [IX]
are companion papers *submitted together with this one* ([C0] the
binding-theory companion; [C1]–[C4] necklace
invariants, reflection positivity and realization, the moment
test, the graded Weyl law; [C-VIII] horizons; [VII] the neutrino
registration note; [IX] the mechanism
paper), and **[P]** marks results whose full
treatment lives in the program corpus — a longer, internally dated
paper series available as supplementary material but *not* part of
this submission.  Every claim below whose proof is corpus-bound is
tagged [P], never [C]; the [C] pointers are checkable companions and
the [P] pointers are stated dependencies, not verified ones.  The
referents: a **ledger** is a
stationary stochastic process of committed symbols ("records") with
its word-probability functional; **reflection structure** means
bond- *and site-*reflection positivity of that functional (for
the reconstruction tradition see [3, 7]), *jointly* equivalent
([C2], Thm. 2.1) to a representation by positive-semidefinite
letter operators — site-RP is exactly what makes the letters
positive operators, and the two hypotheses are not interchangeable
(bond-RP alone does not give the operator form) — the operator
form in which all of this paper's transfer-matrix statements
live; **seams** are the invariant
tensors coupling letter fibers; record **towers** are inductive
families of such processes with stated growth conditions (the "tame
class," defined where used).  Sections below give, for each result,
the precise mathematical statement at this level, the receipt, and
the pointer to the companion proof; this paper's own role is the
physical layer — which structures are *forced* and which are
chosen.

**Method.**  Every quantitative claim carries a machine-checked
numerical receipt: a deterministic, fixed-seed script whose reruns
are bit-identical and whose output is quoted directly.  (We do not
claim proof-assistant formalization; "receipt" means a reproducible
computation, and theorems are proved as theorems in the text or
companions.)  Every load-bearing assumption is named and typed:
*axiom*, *theorem*, *identification* (a bridge chosen, not proved),
or *import* (classical mathematics).  The audit appears in Section
7 — including the honest count: three axioms, a handful of named
identifications, four scope premises, and three named structural
inputs (the power-sum weight form; screen-transport linearity and
transitivity; the spatial $d = 3$ minimality selection).

## 2. The Born layer at tame scope

**What is and is not claimed.**  We do not offer a Gleason-style or
decision-theoretic derivation of the Born rule, and we position this
section explicitly against that literature [8–11]: probabilities
here are *primitive* (record weights), as in Barandes'
correspondence [1], and the derived content is structural — that the
weight calculus of sealed histories organizes itself into the
Hilbert-space formalism, with amplitudes as square roots of weights
and the operator algebra emerging from record towers.  The
quantum-reconstruction programs [10, 11] derive the formalism from
operational axioms about laboratories; this program derives it from
an ontology with no observers in it.  Where they meet — the
uniqueness of the quadratic weight calculus — we rely on the
correspondence theorems, not on novelty claims.

**What the "quadratic" imports, exactly.**  Although we do not
*derive* the Born exponent, we can say precisely which single
structural assumption it is.  Let a record screen carry a finite
complex weight vector $a = (a_1, \dots, a_n)$ and let the event weight
be componentwise, $W_p(a) = \sum_i |a_i|^p$; require it invariant
under the admissible screen transports.  This separates into two layers.  *Layer 1 (tautological).*  Once the
screen norm is *declared* to be $\ell_q$, the readable exponent is
pinned to $p = q$ with no further content: an equal-split transport
$(1,0,\dots,0) \mapsto n^{-1/q}(1,\dots,1)$ sends the unit input
($W_p = 1$) to $W_p = n^{1-p/q}$, and a single screen size $n \ge 2$
already forces $n^{1-p/q} = 1$, i.e. $p = q$.  This holds for *every*
$q$ and says nothing about *which* $q$ — the readable exponent is
*identically* the norm one declares.  *Layer 2 (the substantive
step).*  All the content is in *which* transports are admissible: the
equal-split map preserves the $\ell_q$ norm of its one input–output
pair, but for $q \neq 2$ it does **not** extend to a linear $\ell_q$
isometry of the screen at all, so its very admissibility as a transport
is already a $q = 2$ statement.  And there is a classical reason the
admissible (linear, transitive) transports are the $q = 2$ (unitary)
family:
by the **Banach–Lamperti theorem** [17], for $q \neq 2$ the surjective
linear isometries of complex $\ell^n_q$ are the generalized
permutations (coordinate permutations dressed with phases), which do
**not** act transitively on the screen sphere — none carries
$(1,0,\dots,0)$ to the uniform superposition $n^{-1/q}(1,\dots,1)$ —
whereas $q = 2$ is the unique exponent whose isometry group $U(n)$ acts
**transitively**.  So the content of "the weight calculus is quadratic"
reduces to three structural inputs: **(0)** the screen weight is a
componentwise power-sum $W_p(a) = \sum_i |a_i|^p$ (additive over
components, phase-blind per component, a single global exponent — itself
an assumed form, not derived from R/S/C), and the admissible
record-screen transports **(a)** are **linear** maps preserving the
screen norm — so the Banach–Lamperti classification applies — and
**(b)** act **transitively** on the screen sphere: any normalized
configuration is reachable from any other (any-to-any reachability,
strictly stronger than mere reversibility/invertibility of a
transport).  Under (a) and (b), Banach–Lamperti forces $q = 2$ —
hence Born's square-root composition — by a named classical theorem.
(In finite dimension every injective linear isometry is automatically
onto, so the surjectivity hypothesis of Banach–Lamperti is free; the
equal-split argument is taken at screen size $n \ge 2$, the $n = 1$
sphere being degenerate.)  Linearity is
load-bearing, not cosmetic: drop it and *every* $\ell_q$ sphere becomes
a homogeneous space under (nonlinear) transitive transports — an
explicit $q = 3$ transport carries $(1,0,0)$ to the uniform vector while
staying on the sphere — so transitivity alone would not single out
$q = 2$.  This is the precise, minimal form of the import that the
correspondence theorems otherwise carry wholesale.

**Statement.**  For record ledgers in the tame class — sketched
here since it is load-bearing: inductive towers of finite record
processes whose generator matrix elements grow at most
polynomially in the tower level, whose limiting quadratic forms
are closable, and whose boundary behavior is limit-point in the
Weyl sense (no boundary data needed); the full definition with the
growth constants is corpus-bound [P], as is the boundary
classification with its receipts [P] — the
weight calculus reconstructs: (i) Born
composition — amplitudes attach to seams as square roots of record
weights, with relative seam data supplying interference (the
silent/physical criterion for such data is stated in Part II,
Section 2, where it carries superselection weight); (ii) the
Weyl/CCR algebra over the reconstructed configuration observables,
landing in the Schrödinger representation by Stone–von Neumann
(named import); (iii) unbounded position/momentum with ladder
structure and selection rules.

**Receipts.**  Gaussian record towers reconstruct continuum spectra
from finite data with errors falling from $7\times 10^{-2}$ to
$4.5\times 10^{-11}$ along the tower; dilation towers are exact and
projectively coherent; the boundary of the tame class is *itself
classified* — non-tame towers are exactly those missing boundary
records, realizing the classical Weyl limit-point/limit-circle
alternative [16] on record towers, with the threshold case
appearing at an explicit $1/\log n$ merging rate.

**Scope.**  The reconstruction half of the program's "L3" problem is
closed *conditionally on the [P] tame-class definition* (whose growth
constants are corpus-bound); beyond-tame self-adjointness is
classified, not derived.  (The frontier taxonomy of Section 7 tracks this.)

## 3. Lorentz signature and the operational metric

**Statement, with its honest scope.**  The commitment structure of
records — the seal order is unrefinable while relational directions
are not — *is argued to select* a *Lorentzian split*: exactly one timelike
direction, with orientation classes that follow from the same
commit-order argument (on the same [P] footing, not independently
proved).  This
is a structural argument from the commit-order asymmetry (the seal
order contributes the one unrefinable direction, the relational
directions the rest), not a theorem proved in this batch; the proof
obligation — that an unrefinable seal order forces exactly one timelike
direction in the reconstructed operational metric — is named here and
is corpus-bound [P], on the same footing as the open Lorentzian-port
obligation of §4.
What it does **not** force, from the axioms alone, is the number of
spatial dimensions.  The honest status of $d = 3$, stated once and
relied on everywhere: Part II proves that exchange holonomy
trivializes for $d \ge 3$ and that $d = 2$ is the anyonic
exception; *nothing in this batch excludes $d \ge 4$*.  The
selection is therefore a **minimality principle** — $d = 3$ is the
first dimension with trivial exchange holonomy — named here as an
input, exactly parallel to the fiber-minimality input of Part III,
and not silently absorbed; the audit table types it accordingly.  We note the instructive
contrast with causal set theory [12], where dimension is likewise
emergent-or-measured rather than axiomatic.  The emergent metric is
operational: the lapse function *is* the local clock rate of record
formation.

**Receipts.**  The lapse-equals-clock-rate identification is
internally consistent in curved record
geometries to ratio error
$3.7\times 10^{-8}$; $1{+}1$-dimensional
Friedmann–Robertson–Walker redshift to $2.1\times 10^{-4}$; a first
genuinely $3{+}1$ curved instance ($32^3$ spatial lattice) whose
agreement is at this stage qualitative (phase-quadrature structure
reproduced; the quantified receipt is corpus-bound [P] and we quote
no number for it here).  The Euclidean–Lorentzian bridge is
*operational rather than axiomatic*: the Osterwalder–Schrader
rotation is implemented as a theorem-backed construction (record
kernels reconstruct generators to $3.6\times 10^{-11}$; Lorentzian
leapfrog dynamics matches OS propagators at the exact discretization
order).

**The continuum caveat, stated up front.**  What emerges is a
*synthetic* geometry whose smooth Lorentzian manifolds form a
regularity stratum.  The program's continuum theorems are
class-uniform convergence results (a Mosco-convergence theorem with
audited constants and a sharp rate [P]) plus a *detector
characterization* of the smooth stratum (the graded local Weyl law
with constructive converse of [C4] — proved there in one dimension
with an executed two-dimensional port; the Lorentzian port is a
named sequel, so the detector characterization of an emergent
$3{+}1$ Lorentzian geometry is a stated target, not a possessed
theorem); homogenized record microstructure is *classified* as its
own stratum, not mistaken for smoothness.

## 4. The arrow of time: reflection positivity as a theorem

**Statement.**  For eventless sectors (no committed events in the
relevant window) admitting a finite primitive Markov presentation,
reflection positivity *holds as a theorem* — the ledger cannot hide
a thermodynamic arrow.  Quantitatively, the entropy-production rate
is exactly the order-evidence divergence:

$$
\sigma \;=\; \mathbb E[A_D] \;=\; D\bigl(P_{AB}\,\Vert\,P_{BA}\bigr),
$$

the Kullback–Leibler divergence between forward and reversed pair
statistics — "the arrow is the evidence."  This identity is
*classical stochastic thermodynamics*, not a discovery of this
program: entropy production as the relative entropy of forward
versus time-reversed path measures goes back to Schnakenberg and is
developed by Gaspard, Kawai–Parrondo–Van den Broeck, and
Roldán–Parrondo [15]; we import it (the audit row types it as a
classical import) and
add only the record-pair form and the corollary that matters here —
a **no-silent-arrow theorem**: eventless dynamics forces detailed
balance, so a thermodynamic arrow cannot hide in a sector with no
committed events.

**Sharpness.**  The presentation hypothesis cannot be dropped: there
exists an explicit three-dimensional process — the **record clock**
— that is reversible, fully valid (all word probabilities
nonnegative, certified analytically to all orders), of Hankel rank
exactly three, whose diagonal oscillates irrationally on its decay
circle.  By Perron–Frobenius obstruction theory it admits *no*
finite positive realization, and it *fails* reflection positivity:
the reflected Gram on the 15-word family — the $1 + 2 + 4 + 8 = 15$
words of length $\le 3$ over a binary alphabet — has minimum
eigenvalue $-1.06\times 10^{-2}$ (verified in companion [C2], Prop. 3.2;
the eigenvalue and the Perron–Frobenius non-realizability are not
reproduced in this paper).  Sealed
ledgers are thus a strict subclass of valid reversible processes,
and the separating witness is precisely a clock — an object that
keeps time without recording it.  The structural question this
opens (does reflection positivity plus finite rank *force*
realizability?) is developed in a dedicated companion paper, where
the obstruction is confined to combinatorially chiral patterns and
reduced to two sharp finite-dimensional conjectures.

## 5. Thermality: the consistency credential

The horizon sector — temperature $T = \kappa/2\pi$ obtained two
ways (Euclidean cone regularity, with its record-language reading
as a no-boundary-record condition graded in [C-VIII] as a named
identification, not a derived consequence of axiom S;
Bisognano–Wichmann modular data on the record lattice),
endpoint classification of lapse profiles, scattering, and capacity
— is presented in full, with its receipts and with the classical
literature it reproduces explicitly credited (Gibbons–Hawking,
Calabrese–Cardy, Weyl endpoint theory), in the companion paper
[C-VIII].  We do not duplicate it here; its role for this paper is
one sentence: the record framework reproduces the standard thermal
structure of horizons in exact lattice constructions, which is a
consistency credential every candidate framework must earn and
nothing more.

## 6. The number: one fixed-point constant

Axiom C is not decorative: it has a computable fixed point.  Two
registers, kept honestly separate: the *mathematics* of the fixed
point — the equation, the constants $\theta, \eta, \kappa_b,
\varepsilon$, their closed forms and exact algebraic relations —
is fully self-contained in the submitted companion [C0].  The
*identification* of that fixed point with axiom C's refinement
construction (the derivation sketched next) remains corpus-bound
[P]: [C0] derives the same equation from its own
exponential-consistency condition, and the claim that axiom C's
diamond construction produces that condition is a [P] dependency,
graded as such in the audit.  The
derivation, in outline: refine one record
into a binary tree of sub-records and demand that the committed
correlation across the refinement diamond reproduce the unrefined
correlation — projective consistency under binary refinement.  For
the minimal ($2\times 2$) committed diamond this closes into the
single equation

$$
\theta^3 + \theta^2 + \theta = 1,
$$

whose unique real root $\theta = 0.543689\ldots$ also satisfies
$\tanh\eta = e^{-\eta}$ under $\theta = e^{-\eta}$ and the
block-spin identity $\tanh(\eta/2) = \theta^2$ — one constant,
three structural faces, with the equivalences verified
symbolically and numerically.  A binding analysis on the
relation-code energetics of records (the constant $\kappa_b$ —
written with the subscript in this paper only to keep $\kappa$
free for the surface gravity of result (iv); it is exactly
[C0]'s $\kappa$ — is
the single-relation first-order marginality coefficient: the
coefficient in [C0]'s law $\theta^w(1 - w\kappa_b)$, an
*anti-binding* first order whose $w = 3$ sign is overturned at
second order, per [C0] — with closed form $\kappa_b =
\eta(1-\theta^2)/(1-\theta^2+\theta)$; full self-contained
definition, computation, and exact algebraic relations in the
submitted companion [C0]) yields the program's
small parameter
$\varepsilon = 3\kappa_b - 1 = 0.0317686364466$ (carried to
$\ge 10$ significant digits, the precision relevant at
next-generation experimental sensitivity).  Two things are claimed and
no more: the constant's pedigree contains no Standard-Model input —
checkable *within this batch* via [C0] —
and its provenance predates by many program papers
its registered confrontations with data (the accompanying note's
undressed spectrum-point registration and the mechanism paper [IX]'s
dressed menu; both with
stated falsifiers and named resolving experiments).  Whether that
confrontation survives is an experimental question; this section's
content is the derivation chain and its timestamp.

## 7. The audit: what is assumed, what is proved

The program maintains a complete dependency audit.  Abbreviated:

```text
result                          pedigree
Born layer at tame scope        theorem (R,S,C) + Barandes
                                correspondence import [1,2]
                                (uniqueness of the quadratic
                                calculus is inherited, not derived
                                here) + Stone-von Neumann import
                                + tame premise [P]
                                + power-sum weight ansatz INPUT
                                (componentwise additivity, per-
                                component phase-blindness, single
                                exponent; not derived from R,S,C)
Lorentzian split, orientation   structural argument [P] for the (1,d) split;
                                spatial d = 3 INPUT (minimality
                                principle, Sec. 3; d >= 4 not
                                excluded anywhere in this batch)
RP for eventless sectors        theorem + Markov-presentation
                                premise (SHARP: the clock [C2])
sigma = KL identity             classical import [15] (stochastic
                                thermodynamics); program adds the
                                record-pair form + no-silent-arrow
thermality T = kappa/2pi        receipts at stated scope [C-VIII],
                                reproducing Gibbons-Hawking/BW
                                structure (credited there)
lapse = clock rate              identification (operational,
                                model-internal check 3.7e-8)
continuum smooth stratum        class-uniform theorems [P] +
                                detector characterization [C4]
                                (1d + 2d port; Lorentzian open)
the constant theta, epsilon     equation + constants + closed
                                forms: companion [C0] (in-batch,
                                checkable); the axiom-C diamond
                                reading of that equation: [P];
                                + two identifications in the
                                binding chain [P]
```

The four scope premises promised in Section 1, counted here so
the numbers reconcile: the tame-class premise [P]; the
Markov-presentation premise (sharp, witness in [C2]); the
finite/atomic sector premise; and the smooth-stratum regularity
premise [P].  The three named structural inputs, likewise counted: the
power-sum weight form (§2 input (0)); screen-transport linearity and
transitivity (§2 inputs (a),(b)); and the spatial $d = 3$ minimality
selection (§3).
Named identifications and imports are enumerated exhaustively in
the program's audit paper; nothing is silently load-bearing.  The
frontier (tame class, continuous sector families) is likewise
structured: results are typed as rank-free, engine-uniform,
finite-receipted, or genuinely frontier-bound.

## 8. Relation to prior work

The stochastic–quantum correspondence is Barandes' [1, 2]; this
program is an ontology *proposal within* that correspondence —
records replace trajectories, and the axioms do forcing work the
correspondence alone does not attempt.  Among competing discrete or
stochastic ontologies: 't Hooft's cellular-automaton interpretation
[13] posits deterministic substrate dynamics where we posit sealed
stochastic records; Nelson's stochastic mechanics [14] derives the
Schrödinger equation from diffusion but inherits its known
locality difficulties; causal set theory [12] shares the discrete,
order-theoretic spirit and the lesson that dimension must be earned
rather than assumed.  Reflection positivity as the encoding of the
arrow connects to the Osterwalder–Schrader tradition [3]; the
sharpness witness (the clock) places the program's realization
question inside the classical positive-realization literature
(Dharmadhikari, Heller, Benvenuti–Farina — engaged in detail in
[C2], where the witness and its certificates are constructed).
Modular thermality belongs to Bisognano–Wichmann [4] and
algebraic QFT [5]; the synthetic-geometry stance to metric-measure
Lorentzian frameworks [6].  What we believe is new: the *direction*
of derivation (positivity and the Lorentzian split as outputs of a
record principle), the sharpness witnesses, and the audit
discipline.

## 9. Limitations and the program's frontier

Stated plainly: (i) all results hold at *stated scope* — tame
class, finite/atomic sector structure, with the frontier taxonomy
published; (ii) the continuum is reached as a regularity stratum,
not assumed — and the multidimensional rigidity theorem is open;
(iii) interacting dynamics (coupling flows, mass generation) is the
program's open dynamics layer; (iv) the identifications — few and
named — are bridges, not theorems.  On falsifiability we keep two
notions separate: a *failing
receipt* shows that the construction does not realize an
identification — an internal refutation — while *empirical*
falsification requires data.  The batch's empirical exposure is
carried by two documents: the registered **undressed spectrum
point** of the accompanying note [VII], and the
mechanism paper [IX], which registers the dressed **four-member
menu** (two members live against today's data, two
excluded and listed as falsified) with its own
pre-committed kill criteria.  Both are named here so this paper's audit and the
batch's actual empirical surface agree.

## Reproducibility

Every numerical claim regenerates from fixed-seed scripts with
bit-identical reruns; the receipts repository accompanies the
program.  This paper's role is the precise statement of axioms,
theorems, and scope; companion papers carry the full proofs and
extended receipts for each layer.

## References

[1] J. A. Barandes, The stochastic-quantum correspondence,
arXiv:2302.10778; New foundations for quantum theory (preprint
series).

[2] J. A. Barandes, Quantum systems as indivisible stochastic
processes (preprint).

[3] K. Osterwalder, R. Schrader, Axioms for Euclidean Green's
functions, *Commun. Math. Phys.* **31** (1973) 83–112.

[4] J. J. Bisognano, E. H. Wichmann, On the duality condition for a
Hermitian scalar field, *J. Math. Phys.* **16** (1975) 985.

[5] R. Haag, *Local Quantum Physics*, Springer (1996).

[6] F. Cavalletti, A. Mondino, Optimal transport in Lorentzian
synthetic spaces, *Invent. Math.* (2020+) — the synthetic frame.

[7] A. Klein, L. J. Landau, *J. Funct. Anal.* **44** (1981) 121 —
OS reconstruction for symmetric local semigroups.

[8] A. M. Gleason, Measures on the closed subspaces of a Hilbert
space, *J. Math. Mech.* **6** (1957) 885–893.

[9] D. Deutsch, Quantum theory of probability and decisions,
*Proc. R. Soc. Lond. A* **455** (1999) 3129; D. Wallace, *The
Emergent Multiverse*, OUP (2012) — decision-theoretic Born
derivations.

[10] L. Hardy, Quantum theory from five reasonable axioms,
arXiv:quant-ph/0101012.

[11] G. Chiribella, G. M. D'Ariano, P. Perinotti, Informational
derivation of quantum theory, *Phys. Rev. A* **84** (2011) 012311.

[12] L. Bombelli, J. Lee, D. Meyer, R. D. Sorkin, Space-time as a
causal set, *Phys. Rev. Lett.* **59** (1987) 521; S. Surya, The
causal set approach to quantum gravity, *Living Rev. Relativ.*
**22** (2019) 5.

[13] G. 't Hooft, *The Cellular Automaton Interpretation of Quantum
Mechanics*, Springer (2016).

[14] E. Nelson, Derivation of the Schrödinger equation from
Newtonian mechanics, *Phys. Rev.* **150** (1966) 1079; *Quantum
Fluctuations*, Princeton UP (1985).

[15] J. Schnakenberg, Network theory of microscopic and macroscopic
behavior of master equation systems, *Rev. Mod. Phys.* **48**
(1976) 571; P. Gaspard, Time-reversed dynamical entropy and
irreversibility, *J. Stat. Phys.* **117** (2004) 599; R. Kawai,
J. M. R. Parrondo, C. Van den Broeck, Dissipation: the
phase-space perspective, *Phys. Rev. Lett.* **98** (2007) 080602;
É. Roldán, J. M. R. Parrondo, Estimating dissipation from single
stationary trajectories, *Phys. Rev. Lett.* **105** (2010) 150607
— entropy production as path-measure relative entropy.

[16] M. Reed, B. Simon, *Methods of Modern Mathematical Physics
II*, Academic Press (1975) — the Weyl limit-point/limit-circle
alternative.

[17] J. Lamperti, On the isometries of certain function-spaces,
*Pacific J. Math.* **8** (1958) 459–466 (after S. Banach, *Théorie
des opérations linéaires*, 1932) — for $1 < q < \infty$, $q \neq 2$ the
surjective linear isometries of complex $\ell^n_q$ are the generalized
(phase-)permutations; the finite-dimensional endpoint cases
$\ell^n_1, \ell^n_\infty$ have the same (generalized-permutation)
isometry group by the separate classical classification (Banach 1932),
not by Lamperti's $L^p$ theorem; only $q = 2$ yields the transitive
group $U(n)$.

**Companion papers** [C1]–[C4]: the mathematical companions
submitted with this batch — [C1] the necklace-invariant
paper; [C2] the reflection-positivity /
realization paper (the clock witness); [C3] the moment-signature
test; [C4] the graded local Weyl law.
