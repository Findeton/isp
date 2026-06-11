# Relativistic ISP V5 Paper 14: Does Indivisibility Evade Bell Nonlocality?

Preprint, not peer reviewed, version 2026-05-30.

Author: Felix Robles Elvira

Date: 2026-05-31

Status: foundations analysis paper. This paper investigates a single sharp
question — whether the non-Markovianity (indivisibility) of ISP lets it *evade*
Bell nonlocality — and reaches a deliberately honest, two-sided answer. It does
not claim ISP defeats Bell's theorem. The conclusion is: non-Markovianity is
**not** a Bell loophole; it is the *mechanism* by which a single-history,
configuration-realist, no-collapse ontology pays one specific Bell price
(violation of Outcome Independence). ISP therefore lands at **exactly orthodox
quantum mechanics' locality status** — no-signalling, parameter-independent,
outcome-dependence — re-described as "nonlocality in time." That is a genuine
and attractive interpretive package, but it is a *relocation* of the nonlocal
content, not an *evasion* of it.

Searchable paper tag:

`V5P14-NON-MARKOVIANITY-AND-BELL-NONLOCALITY`.

## Abstract

ISP is often summarized as "local in space, with the non-Markovianity acting as
a kind of non-locality in time." This paper asks whether that slogan amounts to
evading Bell nonlocality. We separate three meanings of "evade," set out Bell's
theorem as a clean assumption taxonomy (single outcomes; measurement
independence; local causality = parameter independence ∧ outcome independence),
and locate ISP within it using the recent derivation of the Tsirelson bound from
causally local indivisible processes (Barandes–Hasan–Kagan, arXiv:2512.18105).
The result is unambiguous: a single-history theory that reproduces the CHSH
violation must give up one Bell assumption, and ISP gives up **outcome
independence** while keeping parameter independence, measurement independence,
and single definite outcomes. Hence ISP violates Bell's local causality — it is
Bell-nonlocal in the technical sense — and does so at the *same* address as
textbook quantum mechanics ("passion at a distance," Shimony). Non-Markovianity
does no work in *escaping* Bell; it does decisive work in letting a
configuration-realist, collapse-free, single-world model occupy that address at
all. We contrast this with the Brassard–Raymond-Robichaud "parallel lives"
escape (arXiv:1710.01380), which is local-realistic but *multivalued*, and which
ISP is not.

## Plain-Language Picture: How ISP Records Account For Nonlocality

`V5P14-PLAIN-LANGUAGE-PICTURE`.

Before the formal taxonomy, here is the picture in ordinary language. The precise
status is fixed in §5 and §10; this section is the on-ramp, not the proof.

**What is real in ISP.** Two things: *records* — definite outcomes that actually
get registered — and a *law* that says which joint patterns of records are
allowed and how probable they are (the whole-process record law). There are no
superpositions in the ontology, only registered facts and the law constraining
them.

**An entangled pair is one process, not two things.** Preparing an entangled pair
is not making two particles that each carry their own private instructions. It is
creating *one indivisible process* with *two readout windows*, one near each
party. Each window yields a definite local record; the single law ties the two
windows' records together.

**The correlation is a law that will not factor.** Each window, on its own, looks
random — so nothing one party does shows up in the other's local statistics (this
is no-signalling, §3). But the joint law linking the two windows does *not* split
into "window A's private law" times "window B's private law." That refusal to
factor is the entanglement (cf. V5 Paper 5), and it is the entire account of the
Bell correlations: the outcomes are correlated beyond any "two separate local
instruction sets" story *because there were never two separate stories* — there
is one process and one joint law.

**Why this is not the pre-set "gloves" story Bell refuted.** A natural worry: if
the law is fixed at preparation, isn't this just hidden instructions decided at
the source — the local-hidden-variable picture Bell's theorem kills? No. What is
fixed at preparation is the *law*, not the *answers*. The answers are not written
on either particle in advance; they become definite only when each window is
read, and they become definite *jointly*, under one law that cannot be factored
into two local laws. Because there are no two separate pre-set local facts, there
is nothing for the local-hidden-variable refutation to grip. ISP slips that
refutation by declining to be two separate things — which is exactly the content
of *indivisibility* (§2), and exactly why §5 locates ISP's Bell price in outcome
independence rather than in pre-set local values.

**Why nothing travels.** The single process and its joint law are anchored at the
preparation event, which lies in the *common past* of both readouts. So at
measurement time nothing races across the gap; the joint pattern was already a
feature of the one process from its shared origin. ISP packages this as memory:
the strangeness sits in the process carrying its joint origin forward in *time*,
not in an influence reaching across *space*.

**The honest caveat (developed in §7 and §10).** This picture genuinely dissolves
the "how do they coordinate across the gap?" puzzle — there is nothing to
coordinate, because it is one process read in two places — and it makes the
no-signalling, no-spooky-influence side feel natural. What it does *not* do is
make the correlation local in Bell's technical sense. "A single joint law that
will not factor into two local laws" is *precisely* the failure of outcome
independence that Bell calls nonlocal (§5). So ISP **relocates** the nonlocality —
from action across space to one indivisible process with memory — and grounds it
honestly in the common past; it does not **remove** it. ISP ends up exactly as
Bell-nonlocal as quantum mechanics (§9), with a different, and arguably more
comfortable, story about why.

## 0. Purpose And The Three Meanings Of "Evade"

`V5P14-PURPOSE-AND-DISAMBIGUATION`.

The phrase "ISP evades Bell nonlocality" is ambiguous across three very
different claims:

$$
\textbf{(E1)} \quad \text{ISP satisfies Bell's local-causality condition (no Bell nonlocality at all).}
$$

$$
\textbf{(E2)} \quad \text{ISP avoids superluminal causal influence and signalling.}
$$

$$
\textbf{(E3)} \quad \text{ISP removes the troubling content of nonlocality by relocating it from space to time.}
$$

The whole paper turns on keeping these apart. The honest verdicts, proved or
argued below, are:

- **(E1): false.** ISP cannot satisfy Bell local causality and still reproduce
  the Tsirelson violation. It is Bell-nonlocal.
- **(E2): true.** ISP is no-signalling and parameter-independent; there is no
  superluminal causal influence in its dynamics.
- **(E3): interpretive, not a theorem.** The "nonlocality in time" reading is
  coherent and attractive, but it re-narrates an outcome-dependence that remains
  a fact about spacelike-separated data. It does not make that content vanish.

So "does non-Markovianity evade Bell nonlocality?" splits into a clean *no*
(E1), a clean *yes* (E2), and a *matter of interpretation* (E3). Conflating them
is the only way to get a one-word answer, and any one-word answer is wrong.

## 1. Bell's Theorem As An Assumption Taxonomy

`V5P14-BELL-ASSUMPTION-TAXONOMY`.

Let two spacelike-separated parties choose settings $x,y$ and obtain outcomes
$a,b$. Let $\lambda$ be a complete description of the common past (a "hidden
variable," which may be as large as the entire shared history). Bell's theorem
(Bell 1964, 1976; CHSH 1969) derives the inequality

$$
S_{\mathrm{CHSH}} \le 2
$$

from the conjunction of three assumptions:

$$
\textbf{(SO)} \quad \text{single outcomes: each measurement yields one definite } a,b.
$$

$$
\textbf{(MI)} \quad \text{measurement independence: } \rho(\lambda \mid x,y) = \rho(\lambda).
$$

$$
\textbf{(LC)} \quad \text{local causality: } p(a,b \mid x,y,\lambda) = p(a\mid x,\lambda)\, p(b\mid y,\lambda).
$$

Following Jarrett (1984) and Shimony, local causality factorizes into two
logically independent conditions:

$$
\textbf{(PI)} \quad p(a\mid x,y,\lambda) = p(a\mid x,\lambda) \quad \text{(parameter independence)},
$$

$$
\textbf{(OI)} \quad p(a\mid b,x,y,\lambda) = p(a\mid x,y,\lambda) \quad \text{(outcome independence)},
$$

with

$$
\textbf{(LC)} \iff \textbf{(PI)} \wedge \textbf{(OI)}.
$$

Quantum mechanics yields $S_{\mathrm{CHSH}} = 2\sqrt2$ (Tsirelson 1980), so any
theory reproducing it must drop at least one of **SO, MI, LC**. The exits are
the well-known interpretive families:

| exit | give up | example |
| --- | --- | --- |
| nonlocal causation | **PI** | de Broglie–Bohm |
| outcome nonlocality | **OI** | textbook QM / collapse |
| superdeterminism / retrocausality | **MI** | $t$-symmetric models |
| many outcomes | **SO** | Everett; parallel lives |

The single most important structural fact for this paper: **no Bell assumption
is "Markovianity."** Bell's $\lambda$ may be the entire common history; the
theorem never assumes the dynamics divide through intermediate times. This is
the lever everything below rests on.

## 2. ISP In One Page

`V5P14-ISP-STRUCTURE`.

ISP (Barandes, *The Stochastic-Quantum Correspondence*, arXiv:2302.10778) models
a quantum system as an **indivisible stochastic process** on a configuration
space:

- configurations are **beables** — definite values at every time, not
  superpositions;
- the dynamics is given by transition matrices from an initial **division
  event**, and is **non-Markovian**: it does not factor as
  $\Gamma(t\leftarrow t_0)=\Gamma(t\leftarrow t')\,\Gamma(t'\leftarrow t_0)$
  except at division events;
- consequently the process assigns **no probabilities to trajectories** between
  division events — there is no joint law over intermediate configurations;
- the Hilbert space, wavefunction, and unitary group are a derived,
  instrumental re-encoding of this process (the stochastic–quantum dictionary).

The slogan attached to it is: *local in space, with indivisibility as a
"non-locality in time."* The task is to make that precise and test it against
§1.

## 3. Barandes's "Causal Locality" Is Parameter Independence, Not Local Causality

`V5P14-CAUSAL-LOCALITY-IS-PI`.

Barandes–Hasan–Kagan (*The CHSH Game, Tsirelson's Bound, and Causal Locality*,
arXiv:2512.18105) give ISP a formal locality condition. For spacelike-separated
systems $Q,R$ with initial configurations $q_0,r_0$ at the division time $t_0$:

$$
\textbf{(CL}_{\mathrm{ISP}}\textbf{)} \quad p(q_t \mid q_0, r_0) = p(q_t \mid q_0).
$$

In words: the distant system's initial configuration (and local operations) do
not change the local configuration statistics. They prove that **causally local
indivisible (unistochastic) processes saturate, but do not exceed, the Tsirelson
bound** $2\sqrt2$.

The decisive observation for the present question is what $\mathrm{CL}_{\mathrm{ISP}}$
*is*, in Bell's vocabulary:

$$
\boxed{\;\mathrm{CL}_{\mathrm{ISP}} \;\text{is a } \textbf{parameter-independence} \text{ / no-remote-influence condition, } \textbf{not} \text{ Bell's local causality.}\;}
$$

It controls how a *setting/state on one side* affects the *configuration
distribution on the other*. It says nothing forbidding the two outcomes from
being correlated given the common preparation. That residual correlation is
precisely **outcome dependence**. So $\mathrm{CL}_{\mathrm{ISP}}$ is strictly
weaker than $\textbf{LC}=\textbf{PI}\wedge\textbf{OI}$: it is (essentially)
$\textbf{PI}$ alone. Calling it "causal locality" is legitimate — it is the
no-superluminal-causation part of locality — but it must not be read as Bell
locality. This single equivocation is what makes the slogan sound like (E1) when
the mathematics only delivers (E2).

## 4. Non-Markovianity Is Not A Bell Loophole

`V5P14-NONMARKOV-NOT-A-LOOPHOLE`.

**Proposition 14.1 (no exemption from the theorem).** *Let a theory assign
definite configurations at all times (as ISP does) and reproduce
$S_{\mathrm{CHSH}}>2$. Then it violates at least one of $\textbf{SO},
\textbf{MI}, \textbf{LC}$. Non-Markovianity does not exempt it.*

*Argument.* Bell's derivation requires only that there exist a common-past
variable $\lambda$ relative to which the assumptions are stated. In a theory
with definite configurations at all times, take $\lambda$ to be the **entire
configuration history in the common past**. This object exists by hypothesis (it
is the trajectory of beables), regardless of whether the dynamics is Markovian.
With this $\lambda$, the CHSH derivation proceeds verbatim. Hence
$S_{\mathrm{CHSH}}>2$ forces the failure of $\textbf{SO}$, $\textbf{MI}$, or
$\textbf{LC}$. $\quad\blacksquare$

The only way for non-Markovianity to matter is if ISP **denies that the
configuration history is an admissible $\lambda$** — i.e. denies joint reality to
the trajectory (which is exactly the indivisibility postulate: no trajectory
probabilities). But that move does not *evade* Bell; it *chooses an exit*: it
denies the existence of a complete common-cause variable that screens off the
correlation, which is a failure of $\textbf{LC}$ (the correlation has no local
common-cause factorization), not a fourth way out. Either reading lands inside
the taxonomy of §1.

## 5. Which Exit ISP Takes: Outcome Independence

`V5P14-ISP-VIOLATES-OI`.

We now combine §3 (what ISP keeps) with §4 (it must drop something).

From Barandes–Hasan–Kagan and the stochastic–quantum dictionary, ISP **keeps**:

- $\textbf{SO}$: configurations are definite single outcomes;
- $\textbf{MI}$: settings are chosen independently of the preparation
  ("statistical independence");
- $\textbf{PI}$: $\mathrm{CL}_{\mathrm{ISP}}$, no remote influence.

It reproduces $S_{\mathrm{CHSH}}=2\sqrt2>2$.

**Proposition 14.2 (ISP is Bell-nonlocal via outcome dependence).** *Under
$\textbf{SO}\wedge\textbf{MI}\wedge\textbf{PI}$, the CHSH bound $S\le 2$ would
follow if $\textbf{OI}$ also held (since $\textbf{LC}=\textbf{PI}\wedge\textbf{OI}$
and §1). Because ISP achieves $S=2\sqrt2$, it must violate $\textbf{OI}$.
Equivalently, the common preparation does not screen off the spacelike outcome
correlation. Therefore ISP violates Bell's local causality: it is Bell-nonlocal.*

$$
\boxed{\;\textbf{SO}\;\checkmark\quad \textbf{MI}\;\checkmark\quad \textbf{PI}\;\checkmark\quad \textbf{OI}\;\times \;\Longrightarrow\; \textbf{LC}\;\times\;}
$$

This is **the same exit textbook quantum mechanics takes**: orthodox QM is
no-signalling, parameter-independent, and outcome-dependent — Shimony's "passion
at a distance." ISP does not improve on QM's Bell-locality status; it *matches*
it. So with respect to (E1): ISP is exactly as Bell-nonlocal as quantum
mechanics, no more and no less.

## 6. The Genuine Role Of Non-Markovianity

`V5P14-WHAT-INDIVISIBILITY-BUYS`.

If non-Markovianity does not escape Bell, what does it do? Something real, and
worth stating precisely.

Bell's theorem says: a theory with $\textbf{SO}\wedge\textbf{MI}\wedge\textbf{PI}$
cannot reproduce QM. To occupy the **OI-violating, PI-respecting, single-world,
no-signalling** address, the standard ontologies pay heavy tolls:

- collapse theories add a stochastic, Lorentz-tension-laden dynamical reduction;
- de Broglie–Bohm gives up $\textbf{PI}$ (an explicit nonlocal guiding equation);
- Everett gives up $\textbf{SO}$ (branching).

**ISP's contribution is to reach that same address with none of these tolls**: a
single-history, configuration-realist, collapse-free, single-world stochastic
process. Indivisibility is the *mechanism that makes this possible*. Because
there is no division event between preparation and measurement, there is **no
intermediate complete state through which the outcomes are required to
factorize** — which is exactly the room needed to violate $\textbf{OI}$ without
violating $\textbf{PI}$ and without collapse or branching. The interference terms
of the indivisible dynamics (the absence of intermediate marginals) are what
carry the outcome correlation.

So the honest statement of what non-Markovianity buys:

$$
\boxed{
\begin{array}{c}
\text{Non-Markovianity does not evade Bell. It is the mechanism by which a}\\[2pt]
\text{single-history, PI-respecting, no-collapse, single-world ontology}\\[2pt]
\text{realizes the outcome-independence exit that Bell leaves open.}
\end{array}}
$$

That is a substantive ontological achievement. It is not a locality miracle.

## 7. "Nonlocality In Time" Versus "Nonlocality In Space": Fair Assessment

`V5P14-TIME-VS-SPACE`.

The attractive ISP reading is: the correlation is not spooky action *across
space*; it is the system's *memory* — a non-locality *in time*. We assess this
honestly, both sides.

**What is genuinely true.** There is no superluminal causal influence (PI holds),
no signalling, and the dynamics references the past rather than a distant
present. A practitioner who dislikes "spatial action at a distance" gets a model
with none of it. This is real and is exactly (E2).

**What is interpretive, not a theorem.** The quantity that violates a Bell
inequality is a correlation between outcomes at **spacelike separation**. That
violation — the failure of $\textbf{OI}$ — is a frame-independent fact about the
joint data. Narrating the *dynamics* as temporal (the law uses the past) does
not convert the *correlation* into a temporal one; the correlated events remain
spacelike. "Nonlocality in time" is therefore a statement about the form of the
dynamical law, not a redescription that removes the spacelike outcome
dependence. It is a legitimate and appealing gloss, but the following are *not*
equivalent:

$$
\underbrace{\text{the law is non-Markovian (uses the past)}}_{\text{dynamics}}
\quad\not\equiv\quad
\underbrace{\text{the Bell correlation is temporal rather than spatial}}_{\text{the correlation}}.
$$

Hence (E3) is a coherent interpretation, defensible and arguably attractive, but
it is not a theorem and it does not dissolve the outcome dependence. The nonlocal
*content* is conserved; only its *narration* changes.

## 8. Two Distinct No-Signalling Realist Escapes: ISP Versus Parallel Lives

`V5P14-ISP-VS-PARALLEL-LIVES`.

Raymond-Robichaud (arXiv:1710.01380; with Brassard, "parallel lives") proves a
sharp complementary result: **every no-signalling theory with invertible
dynamics admits a local-realistic model** — but the construction is
**multivalued** (each local system carries a set of "lives"), evading Bell by
giving up $\textbf{SO}$.

This is the clean foil for ISP. There are (at least) two ways for a
no-signalling realist theory to live with Bell:

| route | keeps | gives up | character |
| --- | --- | --- | --- |
| **Parallel lives** (Brassard–R-R) | PI, OI, MI | **SO** (multivalued) | local-realistic, many local "lives" |
| **ISP** | PI, MI, **SO** | **OI** | single-history, outcome-dependent, non-Markovian |

ISP is **single-valued** (one configuration history), so it is *not*
local-realistic in the parallel-lives sense — it cannot be, by that very table.
The two frameworks are genuinely different corners of the no-signalling realist
landscape: parallel lives buys locality at the cost of multivaluedness; ISP buys
single-history realism at the cost of outcome dependence. Neither evades Bell;
each pays a different one of Bell's prices. This confirms §5 from the outside:
the price ISP pays is $\textbf{OI}$, not $\textbf{SO}$.

## 9. Locality-Status Table

`V5P14-LOCALITY-STATUS-TABLE`.

$$
\begin{array}{l|ccccc}
\text{theory} & \textbf{SO} & \textbf{PI} & \textbf{OI} & \textbf{MI} & \text{no-signal} \\
\hline
\text{Bell-local (classical)} & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
\text{textbook QM} & \checkmark & \checkmark & \times & \checkmark & \checkmark \\
\textbf{ISP} & \checkmark & \checkmark & \times & \checkmark & \checkmark \\
\text{de Broglie–Bohm} & \checkmark & \times & \checkmark & \checkmark & \checkmark \\
\text{Everett / parallel lives} & \times & \checkmark & \checkmark & \checkmark & \checkmark \\
\text{superdeterminism} & \checkmark & \checkmark & \checkmark & \times & \checkmark
\end{array}
$$

The **ISP row equals the textbook-QM row.** ISP's distinctiveness is *not* in this
table — it is one column to the side, in the *ontology*: ISP realizes the QM
locality profile with a single-history, configuration-realist, collapse-free,
non-Markovian process rather than with a wavefunction plus collapse. That is the
correct, deflationary statement of the locality result.

## 10. Verdict

`V5P14-VERDICT`.

**Theorem-level summary (collecting §§3–8).**

$$
\boxed{
\begin{array}{ll}
\text{(E1) does ISP satisfy Bell local causality?} & \textbf{No.}\ \text{It violates OI; it is Bell-nonlocal.}\\[3pt]
\text{(E2) does ISP avoid superluminal causation / signalling?} & \textbf{Yes.}\ \text{PI and no-signalling hold.}\\[3pt]
\text{(E3) does it remove the nonlocal content?} & \textbf{No; it relocates the narration only.}\\[3pt]
\text{role of non-Markovianity} & \text{mechanism for the OI exit, not an escape.}\\[3pt]
\text{ISP's Bell-locality status} & \text{identical to textbook QM.}
\end{array}}
$$

So: **non-Markovianity does not evade Bell nonlocality.** It does something more
modest and more interesting — it lets a single-world, single-history,
collapse-free, configuration-realist ontology sit at exactly quantum mechanics'
locality address (no-signalling, parameter-independent, outcome-dependent), and
it offers the "nonlocality in time" narration as an interpretive comfort. The
Bell-nonlocal content (outcome dependence across spacelike separation) is
faithfully reproduced, not removed.

## 11. Falsifiers And What Would Change The Verdict

`V5P14-FALSIFIERS`.

This verdict is falsifiable as an analysis; it would change if any of the
following were established.

1. **A genuine $\textbf{LC}$ proof.** Exhibit, for ISP, a complete common-past
   variable $\lambda$ (it may be the whole configuration history) through which
   the spacelike outcomes *do* factorize, while still reproducing $2\sqrt2$. This
   is impossible by §1 unless one of SO/MI fails — so any such claim must
   secretly drop SO or MI. Auditing a claimed (E1) proof reduces to finding which.
2. **An empirical handle on "time vs space."** If the temporal reading (E3) made
   a prediction differing from textbook QM, it would be more than narration. The
   stochastic–quantum correspondence is an *equivalence* with QM, so no such
   prediction exists at present; (E3) stays interpretive.
3. **An MI-located reading.** If ISP's division events were shown to correlate
   with future settings (violating $\textbf{MI}$ rather than $\textbf{OI}$), the
   verdict would move from "QM's address" to a retrocausal corner. The
   Barandes–Hasan–Kagan construction explicitly keeps MI, so this is not the
   current reading, but it is the one alternative worth watching.

## 12. Relation To The Corpus

`V5P14-RELATION-TO-CORPUS`.

This paper is the foundations companion to V5 Paper 5 (*entanglement as
indivisible record nonfactorization*): entanglement there is the
nonfactorization of one indivisible process; Bell nonlocality here is the
**outcome dependence** that this nonfactorization produces, located precisely in
the Bell taxonomy. The two are consistent: a single nonfactorizing process gives
outcome-dependent, no-signalling, parameter-independent statistics — the QM
profile.

It also instances a recurring, honest theme of the program. Just as the
center-gluing route to Yang–Mills confinement turned out to be a **faithful
reformulation** of the standard disorder variables that adds no new analytic
mechanism (the O1 verdict), ISP here is a **faithful reformulation** of quantum
mechanics' exact Bell-locality status that adds no new *locality* mechanism. In
both cases ISP's genuine value is ontological and reconstructive — a
probability-first, configuration-realist account of *what is going on* — not a
defeat of the hard external content (confinement there, Bell nonlocality here).
ISP reproduces the structure honestly; it does not get the structure for free.

## 13. Conclusion

`V5P14-CONCLUSION`.

Non-Markovianity is not a loophole in Bell's theorem, because Bell's theorem
never assumed Markovianity: its hidden variable may be the whole history, which
ISP supplies. Forced by Tsirelson to give up one assumption, ISP gives up
**outcome independence** — keeping single outcomes, measurement independence, and
parameter independence — and thereby occupies textbook quantum mechanics' exact
locality status: no-signalling and free of superluminal causation, but
Bell-nonlocal. The "nonlocality in time" reading is a coherent and appealing
narration of the *dynamics*, not a dissolution of the spacelike *correlation*.

The right one-line answer to "does ISP's non-Markovianity evade Bell
nonlocality?" is therefore:

$$
\boxed{
\begin{array}{c}
\text{It evades superluminal causation (which QM already does), not Bell's theorem.}\\[2pt]
\text{It relocates the narrative of the nonlocality from space to time;}\\[2pt]
\text{it does not remove the nonlocal content. ISP is exactly as Bell-nonlocal as QM.}
\end{array}}
$$

## References (verified)

- J. S. Bell, *On the Einstein–Podolsky–Rosen paradox*, Physics 1, 195 (1964);
  *The theory of local beables* (1976).
- J. Clauser, M. Horne, A. Shimony, R. Holt, PRL 23, 880 (1969) (CHSH).
- B. S. Tsirelson, Lett. Math. Phys. 4, 93 (1980) (the $2\sqrt2$ bound).
- J. Jarrett, *On the physical significance of the locality conditions in the
  Bell arguments*, Noûs 18, 569 (1984); A. Shimony (PI ∧ OI decomposition).
- J. A. Barandes, *The Stochastic-Quantum Correspondence*, arXiv:2302.10778.
- J. A. Barandes, M. Hasan, D. Kagan, *The CHSH Game, Tsirelson's Bound, and
  Causal Locality*, arXiv:2512.18105.
- P. Raymond-Robichaud, *The equivalence of local-realistic and no-signalling
  theories*, arXiv:1710.01380 (Brassard–Raymond-Robichaud "parallel lives").
