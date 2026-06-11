# Sealed-seam suppression in Froggatt–Nielsen-type models: two theorems, an obstruction by conjunction, and a discrete neutrino test

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-11
(substantially rebuilt after hostile review; the withdrawn claims
of the earlier draft are listed in Section 7 and stay withdrawn).

## Abstract

Froggatt–Nielsen (FN) mechanisms generate fermion mass hierarchies
as powers of a small parameter $\lambda$, one insertion per unit of
flavor charge, with $\lambda$ fitted.  We study an FN-type setting
in which the suppression is *pinned by a theorem*: for sealed
two-outcome records — rank-one POVM-type letter pairs with weights
$p$ and $1-p$ in a stationary representation — (i) the transition
norm is $\sqrt{p(1-p)}\,|\langle u,v\rangle| \le \sqrt{p(1-p)}$,
and (ii) a misaligned sealed pair cannot support a stationary
state (top transfer eigenvalue $\tfrac12[1+\sqrt{1-4p(1-p)
(1-|c|^2)}] < 1$ strictly), so stationarity forces saturation:
$\lVert S\rVert = \sqrt{p(1-p)}$ exactly, with the seam phase pure
rephasing gauge.  An exact selection rule follows in any algebra
graded by a family charge whose only charged sealed generator is
the seam: amplitudes vanish unless the seam count balances the
charge difference (receipts: $0/27{,}000$ violations; bounds
saturated to ten digits).  The paper's central *negative* result
is an **obstruction by conjunction**, found when the hostile
review of an earlier draft demolished its seesaw realization and
we completed the demolition: for *integer* right-handed charges,
Majorana diagonals carry even powers of $\lambda$ and an
exhaustive Dirac-consistent scan over rule-allowed textures
(charges in $\{0..3\}^3$, unit $\pm$ coefficients) never reaches
the half-integer-rung spectrum (zero exact hits; best deviation
$0.014$; receipted); for *half-odd* right-handed charges the
Majorana side can reach the rungs exactly, but the corresponding
Dirac column carries half-integer charge, balances no integer seam
count, and vanishes identically — rank collapse; and the textbook
cancellation in any case removes RH charges from the
light masses when the Dirac sector is charged consistently.  The
surviving realization places half-unit charges on the lepton
doublets (Weinberg-operator dressing), where the same selection
rule yields a **discrete menu** for the light spectrum
at unit coefficients (four full-rank members; two already excluded
by data): the rung point $S = \sqrt{\varepsilon_{\rm
eff}/(1+\varepsilon_{\rm eff})} = 0.172747$ (three insertions) and
the cheaper texture $S = 0.167880$ (two insertions), with
$\varepsilon_{\rm eff} = \varepsilon(1-\varepsilon)$ and
$\varepsilon = 0.031768636446582$ a constant whose self-contained
pedigree is the mathematical companion [C0].  Against JUNO's first
data ($S = 0.17283 \pm 0.00167$, our combination of JUNO's
$\Delta m^2_{21}$ with the global-fit $\Delta m^2_{31}$) the
data-live members sit at $-0.05\sigma$ and $-3.0\sigma$; they are
separated
by $7.3\sigma$ at JUNO-final precision, so the menu is
adjudicable this decade, and the minimality principle the program
uses elsewhere favors — on current data — the *worse* member,
which we state rather than hide.  What this paper does **not**
deliver, withdrawn from an earlier draft and listed with reasons:
mixing-angle and CP predictions (they rested on an unlisted
measure-zero orthogonality assumption), the claim that the
mechanism's flavor symmetry uniquely "predicts its own mediator,"
and any charged-fermion statement.  One quantitative input is
irreducible and stated in one line: the seam weight is the
companion theory's first-order marginality, $p = \varepsilon$ — a
referent scan shows it underivable from the obvious fixed-point
quantities, and it carries the aggravating fact that the
first-order law it comes from has its sign overturned at second
order at the defining weight.  The look-elsewhere cost of the
dressed value is counted (six of twelve natural one-factor forms
fit today's central value; three are mutually inseparable even at
JUNO-final), and the claim chronology relative to JUNO's first
release is disclosed in full.

## 1. The Seam Theorem

Work in the representation every reflection-positive stationary
process admits (companion [C2], Thm 2.1): Hilbert space, PSD
letters, $T = \sum_x A_x \preceq \mathbf 1$, stationary unit
vector $T\omega = \omega$.

**Definition (S-atom premise, named).**  A *sealed two-outcome
seam* is a letter pair of rank one: $A_0 = p\,uu^\dagger$,
$A_1 = (1-p)\,vv^\dagger$, unit $u, v$.

**Lemma 1 (norm).**  $\sqrt{A_0}\sqrt{A_1} = \sqrt{p(1-p)}\,
\langle u,v\rangle\,uv^\dagger$, so $\lVert\sqrt{A_0}\sqrt{A_1}
\rVert = \sqrt{p(1-p)}\,|\langle u,v\rangle| \le \sqrt{p(1-p)}$,
with equality iff the poles align.

**Lemma 2 (stationarity gate).**  On the seam span, with
$c = \langle u,v\rangle$ and $d = 4p(1-p)(1-|c|^2)$:
$\lambda_{\max}(A_0+A_1) = \tfrac12[1 + \sqrt{1-d}\,]$, equal to
$1$ iff $|c| = 1$; the exact gap is $\tfrac12[1 - \sqrt{1-d}\,]
\ge p(1-p)(1-|c|^2)/2$, strictly positive for misaligned poles.
(An earlier draft's abstract quoted the lower bound as the exact
gap; corrected.)

**Theorem 1 (stationarity forces saturation).**  If the seam block
acts invariantly at stationarity (premise: decoupling) and the
stationary state overlaps it, then alignment is forced and the
transition norm is exactly $\sqrt{p(1-p)}$.  At alignment the
letters commute: the extremal seam is classical, and the factor is
the two-pole weight of a definite record.  The seam phase
($u \mapsto e^{i\varphi}u$) changes no observable — the rephasing
structure mass terms have always had.

*Receipts*: norm identity to $2.8\times 10^{-16}$ (200 random
complex seams, $d = 2..5$); eigenvalue closed form to
$3.3\times 10^{-16}$.

## 2. The selection rule

**Theorem 2.**  In an algebra carrying a graded charge $Q$ with
every sealed generator $Q$-neutral except one seam $S$ shifting
$Q$ by one unit, $\langle x'|W|x\rangle = 0$ for every word whose
seam count fails to balance $x' - x$ (grade decomposition), and —
since neutral letters are contractions — balanced amplitudes obey
$|\langle x'|W|x\rangle| \le \lVert S\rVert^{|x'-x|}$
(submultiplicativity; an inequality, with saturation a property of
the specific model, exhibited in the receipts).

*Receipts*: $0$ violations in $27{,}000$ matrix elements; maximal
one- and two-unit amplitudes $0.175384$ and $0.030759$, saturating
$\sqrt{\varepsilon_{\rm eff}}$ and $\varepsilon_{\rm eff}$ to ten
digits in the explicit model.

**Scope correction (withdrawn corollary).**  An earlier draft
claimed "oscillations require the seam — the mechanism predicts
its own mediator."  That conflated two gradings: if the Dirac
sector is charged consistently, the claim's premise breaks the
spectrum (Section 3); if the Dirac sector is outside the graded
algebra, sectors connect without the seam and the corollary is
vacuous.  Withdrawn.  What survives is the unglamorous statement:
*within the graded (sealed) sector*, charge steps cost seam
insertions.

## 3. The obstruction by conjunction (central result)

The natural realization — FN charges on the right-handed seals,
$M_R$ hierarchical, Dirac sector neutral — **fails twice over**,
and we record both failures as the paper's main content:

**(a) The textbook cancellation.**  If the Dirac couplings are
charged consistently with the grading, the FN suppressions cancel
identically in the seesaw, $m_\nu = v^2\,Y M_R^{-1}Y^{\mathsf T}$
— the well-known result that FN charges on singlet neutrinos drop
out of the light masses (see e.g. [2]); and half-integer RH
charges make the Dirac column amplitudes exactly zero under a
unit-shifting seam, collapsing the rank.  An earlier draft evaded
this by declaring the Dirac sector "neutral" while keeping the
selection rule — an inconsistency the review exposed.

**(b) Parity, scoped, plus the scan.**  Majorana bilinears
$\nu^c_i\nu^c_j$ carry total charge $x_i + x_j$.  For **integer**
charges the diagonals carry even powers of $\lambda$ — a parity
statement that by itself constrains only diagonal-dominant
textures (off-diagonal-dominant blocks can carry odd-power
eigenvalue magnitudes), so the integer-charge obstruction is
completed by *exhaustive enumeration*: over charge vectors in
$\{0..3\}^3$ with unit $\pm$ coefficients on every rule-allowed
entry, **zero** textures reach the rung spectrum.  The closest
approach — metric pinned as the max over the two independent
ratio deviations $|m_1/m_3 - \varepsilon_{\rm eff}|$ and
$|m_2/m_3 - \sqrt{\varepsilon_{\rm eff}}|$, **computed on the
seesaw-inverted (light) spectrum**: the charges sit on $M_R$ and
the rung target is for the light masses, so $m_i \propto
1/\mu_i$ with $\mu_i$ the eigenvalue magnitudes of the scanned
texture (equivalently, the two components are $|\mu_1/\mu_3 -
\varepsilon_{\rm eff}|$ and $|\mu_1/\mu_2 -
\sqrt{\varepsilon_{\rm eff}}|$) — is $0.014$, with the
**witness published** so the figure is checkable from one matrix:
$q = (3,2,3)$, coefficient pattern $\{11{:}{+}1, 12{:}{+}1,
13{:}{+}1, 22{:}{-}1, 23{:}{+}1, 33{:}0\}$ on magnitudes
$\lambda^{q_i+q_j}$, component deviations $(0.0144, 0.0092)$.
(Applying the metric to the heavy spectrum *uninverted* gives
$(0.0144, 0.0770)$ on this same witness; an earlier draft
attributed that $0.077$ to "a less complete scan variant" — it
is in fact the witness's own uninverted second component, and
the inversion convention was unstated — the same class of
convention bug a previous revision fixed for the charge box,
caught in review and now pinned.)  The zero-exact-hits statement is
robust under the pinned convention: a full independent rerun of
the $\{0..3\}^3 \times \{0,\pm1\}^6$ scan confirms zero exact
hits, best deviation $0.0144$.  Scope honesty: the charge
box $\{0..3\}^3$ is a choice; entries beyond it carry magnitudes
$\le \lambda^7 \approx 5\times 10^{-6}$ and push textures
further from the target, but "exhaustive" means
exhaustive-within-the-box.  For **half-odd** charges, parity
does *not* obstruct the Majorana side — $q = (1, \tfrac12, 0)$
makes $M_R = \mathrm{diag}(\lambda^2, \lambda, 1)$ rule-allowed
and exactly on the rungs — but clause (a) kills the realization:
the $q = \tfrac12$ Dirac column carries half-integer charge,
balances no integer seam count, and is exactly zero, collapsing
the light-mass rank.  **The obstruction is the conjunction of (a)
and (b)-plus-scan**, and we state it as such; an earlier draft
presented (b) as a standalone parity theorem (false for half the
charge lattice) and left the scan's spectrum-inversion convention
unstated (the source of the misattributed $0.077$ above) — both
corrected here, with the scan scope and conventions now pinned.

**The surviving realization.**  Half-unit charges on the lepton
*doublets*, $q_L = (1, \tfrac12, 0)$, acting on the Weinberg
operator $(L_iH)(L_jH)$ with entry charges $q_i + q_j$ and
magnitudes $\lambda^{q_i+q_j}$ at integer insertions
($\lambda = \sqrt{\varepsilon_{\rm eff}}$): allowed entries are
$(11), (22), (33), (13)$; $(12)$ and $(23)$ are parity-forbidden.
This realization is *selected, not chosen*, by two facts: (i)
**integer** doublet charges on the Weinberg operator are excluded
by the same exhaustive enumeration run on the *direct* spectrum
(no seesaw inversion here) — zero exact hits over the full
$\{0..3\}^3 \times \{0,\pm1\}^6$ box, $30{,}624$ full-rank
nondegenerate textures, best deviation $0.0770$, witness in the
receipts; and (ii) $q_L = (1, \tfrac12, 0)$ is the *unique*
normalized assignment realizing the rung diagonal:
$\mathrm{diag}(\lambda^{2q_1}, \lambda^{2q_2}, \lambda^{2q_3}) =
\mathrm{diag}(\lambda^2, \lambda, 1)$ forces $2q_1 = 2$,
$2q_2 = 1$, with the common shift fixed by $q_3 = 0$ (a shift
rescales the spectrum, not its ratios).
Convention, pinned: entries are $0$ or $\pm 1$ times the allowed
magnitude; full rank and a nondegenerate ordering
($m_1 < m_2 < m_3$, all nonzero) required.  The exhaustive menu
then has exactly **four** members (a previous revision said three,
missing the quasi-degenerate fourth — caught in review; for a
paper whose method is exhaustive enumeration, we print the
complete list):

```text
  texture            insertions  spectrum ratios       S
  diag(l^2, l, 1)        3       (e_eff, sqrt(e_eff), 1) 0.172747
  m13 + m22 + m33        2       (0.0290, 0.1703, 1)     0.167880
  all four, sgn(m11
   m33) = -1             4       (0.0581, 0.1704, 1)     0.160500
  m11 + m22 + m13,
   m33 = 0               4       (0.839, 0.916, 1)       0.675516
  (the third and fourth are already excluded by data - at 7.4
   and ~300 sigma respectively - and are listed as falsified
   members, not hidden; an earlier draft printed 0.169993 for
   the second member, a wrong closed-form shortcut - the correct
   value follows from the printed ratios themselves: S^2 =
   m1/(1+2m1), m1 = (sqrt(1+4*e_eff)-1)/2, receipted)
```

## 4. The two-point test

Against JUNO's first data — $S = 0.17283 \pm 0.00167$, **our
combination** of JUNO's $\Delta m^2_{21} = (7.50\pm 0.12)\times
10^{-5}$ [3] with the global-fit $\Delta m^2_{31} = (2.511 \pm
0.027)\times 10^{-3}$ [6], not a JUNO-only number:

```text
  member               S          now        notes
  rung point           0.172747   -0.05 s    (reference)
  cheap texture        0.167880   -3.0  s    7.3 s from the rung
                                             point at JUNO-final
  third member         0.160500   -7.4  s    already excluded;
  fourth member        0.675516   excluded   listed, not hidden
  (undressed point     0.175472   +1.6  s    the registered claim of
   for comparison                            the companion note [VII])
```

The two data-live members are separated by $7.3\sigma$ at
JUNO-final precision ($\sigma_S^{\rm final} \approx 0.00067$:
the projected sub-percent splittings, $\sigma_{21} \approx 0.6\%$
and $\sigma_{31} \approx 0.5\%$ [5], propagated as half the
quadrature sum of the relative errors times $S$): the menu is
adjudicable this decade.
Pre-assigned outcome bands at JUNO-final, all branches covered:
data within $2\sigma$ of $0.172747$ — rung point survives, cheap
texture dead; within $2\sigma$ of $0.167880$ — the reverse, and
minimality scores a sharp win; **within $2\sigma_{\rm final}$ of $0.175472$ — both menu
members die while [VII]'s undressed point survives**; anywhere
else — the whole construction is dead and we say so.  Stated
against interest: the program's own minimality principle (fewest
insertions), applied as elsewhere in the corpus, favors the
**cheap texture** — currently the *worst-fitting live member at
$-3.0\sigma$*.  If JUNO-final confirms today's central value,
minimality-as-selector fails here and we will say so.

What the menu does *not* include: mixing angles and CP phases.
The allowed Weinberg textures are too sparse to generate the
observed mixing from the neutrino sector alone (the $(12), (23)$
entries are parity-forbidden), so the PMNS matrix must come
dominantly from the charged-lepton sector — the earlier draft's
$\theta_{23}$ and $\delta_{CP}$ "predictions" are **withdrawn**
(Section 7).  One genuine charged-sector *constraint* the
realization does impose, stated since review caught us denying
it: $q_{L_2} = \tfrac12$ makes the muon Yukawa row
$\bar L_2 e_R H$ carry half-integer charge, which vanishes unless
the right-handed charged-lepton charges compensate modulo 1 —
half-odd $e_{R_2}$ is an **additional named assumption** (a
massless muon is not negotiable).  So the mechanism says nothing
about charged *masses* but does constrain charged *charges*; the
abstract's withdrawal item is scoped accordingly.

## 5. The one-line input, with its aggravating fact

The mechanism's single quantitative input: the seam weight is the
companion theory's first-order marginality, $p = \varepsilon =
3\kappa - 1$, with $\kappa$ in closed form ([C0]; no
Standard-Model input anywhere in the chain).  A pre-registered
referent scan (ten exact fixed-point candidates, 25 digits) found
no independent quantity equal to $\varepsilon$: the identification
is not derived, and we state the aggravating fact a referee
located: $\varepsilon$ is the coefficient of a *first-order* law
whose sign prediction fails at the defining weight $w = 3$
(first-order $-0.0051$ vs exact $+0.0084$; [C0] itself warns
against extrapolating its truncations).  The input is therefore:
*the seam weight is a specific coefficient of an expansion that is
not trustworthy at the weight that motivates it.*  We keep the
input because the resulting point sits at $-0.05\sigma$ and the
falsification machinery is cheap; we decline to dress it up.

## 6. Chronology, trials, and look-elsewhere

Disclosed in full.  (i) The *value* $\varepsilon_{\rm eff} =
\varepsilon(1-\varepsilon)$ was noticed **after** JUNO's first
release; the program's registered claim is the *undressed* point
($0.175472$ at exact $\varepsilon$; see [VII] and its precision
correction), which that data disfavors at $1.6\sigma$.  (ii) The
look-elsewhere cost was counted before this mechanism existed.
The twelve forms, enumerated (base $\varepsilon\cdot f$):
$f \in \{1-\varepsilon$, $1/(1+\varepsilon)$, $e^{-\varepsilon}$,
$(1-\varepsilon)^2$, $1-2\varepsilon$, $1-\varepsilon/2$,
$1/(1+2\varepsilon)$, $1-\varepsilon^2$, $\cos\varepsilon$,
$1-\kappa\varepsilon$, $1-\theta\varepsilon$,
$1-\eta\varepsilon\}$: six fit the current central
value within $1\sigma$; three (including $\varepsilon_{\rm eff} =
\varepsilon(1-\varepsilon)$) are mutually
inseparable at $0.2\sigma$ even at JUNO-final — so the data can
confirm or kill the one-factor *class*, never select
$\varepsilon(1-\varepsilon)$ within it, and a theorem pinning any
cluster member would have looked equally prophetic.  The Seam
Theorem's evidential weight is therefore *zero until its premises
are tested elsewhere*; its value is that it converts a free
parameter into a falsifiable conjunction.  (iii) No claim in this
paper is "registered" in any externally verifiable sense until the
program's named deposit exists; the internal registration
documents carry their own dating and say the same.

## 7. Withdrawn claims (kept visible)

1. "$\sin^2\theta_{23} = 1/2$ exactly" — rested on requiring an
   *orthogonal* neutral Dirac matrix, a measure-zero assumption
   with no symmetry behind it, which also smuggled CP conservation
   (real orthogonal) and silently fixed $\theta_{12}, \theta_{13}$
   to excluded values.  Withdrawn as a mechanism prediction; what
   remains is a texture observation in the program's corpus
   (its registration document carries the same withdrawal).
2. "$J = 0$, $\delta_{CP} \in \{0, \pi\}$" — the phase-gauge
   argument covers the seam (Majorana) sector only; the Dirac and
   charged-lepton phases are untouched.  Withdrawn.
3. "Oscillations require the seam" — grading-scope conflation
   (Section 2).  Withdrawn.
4. The discrete $m_{\beta\beta}$ menu — computed with undisclosed
   measured mixing angles as inputs; meaningless once (1) is
   withdrawn.  Withdrawn.
5. "Exact rungs for any neutral Dirac sector" — exactness was an
   artifact of the orthogonality fiat; the honest exact statement
   is the Weinberg-realization menu of Section 3.
6. All charged-fermion *mass* statements — the earlier draft
   quantified charged-sector "gaps" with an unreproducible metric;
   no such number survives.  (Not withdrawn: the charge-mod-1
   compensation *constraint* of Section 4, which the realization
   genuinely imposes and which carries its own named assumption.)

## 8. Relation to Froggatt–Nielsen models

The mechanism class is FN [1].  Prior art on *derived* suppression
exists and is engaged per our standing commitment: in anomalous-
$U(1)$ (Green–Schwarz) FN models the parameter is computed from
the Fayet–Iliopoulos term, $\lambda \approx 0.17$–$0.22$
(Binétruy–Ramond; Dudas–Pokorski–Savoy; Ibáñez–Ross [4]) — a range
that, we note with appropriate discomfort, contains
$\sqrt{\varepsilon_{\rm eff}} = 0.175$.  What is different here:
the suppression is pinned by a stationarity theorem in a record
formalism rather than by an anomaly coefficient, the charge's
selection rule is exact rather than order-of-magnitude, and the
realization question (this paper's obstruction and menu) is
answered by exhaustive enumeration at unit coefficients.  What is
*not* different: like every FN model, the O(1)-coefficient
freedom is the mechanism's soft underbelly, and our unit-
coefficient discipline is a named choice, not a derivation.

## Reproducibility

Fixed-seed scripts regenerate every number (the seam lemmas, the
selection-rule receipts, the parity-obstruction scan, the Weinberg
menu, the prediction table); bit-identical reruns; code and
canonical outputs accompany the submission.

## References

[1] C. D. Froggatt, H. B. Nielsen, *Nucl. Phys. B* **147** (1979)
277.

[2] G. Altarelli, F. Feruglio, Models of neutrino masses and
mixings, *New J. Phys.* **6** (2004) 106 — including the
cancellation of singlet-neutrino FN charges in the seesaw.

[3] JUNO collaboration, arXiv:2511.14593; *Nature* **654** (2026)
343 — first measurement, $\Delta m^2_{21} = (7.50 \pm 0.12)\times
10^{-5}\,\mathrm{eV}^2$.

[4] P. Binétruy, P. Ramond, *Phys. Lett. B* **350** (1995) 49;
E. Dudas, S. Pokorski, C. A. Savoy, *Phys. Lett. B* **356** (1995)
45; L. E. Ibáñez, G. G. Ross, *Phys. Lett. B* **332** (1994) 100 —
anomalous-$U(1)$ FN with FI-derived $\lambda$.

[5] JUNO collaboration, JUNO physics and detector, *Prog. Part.
Nucl. Phys.* **123** (2022) 103927 — projected sub-percent
splitting precisions (an earlier draft cited the DUNE TDR and
Hyper-Kamiokande design report here; those experiments do not
measure $\Delta m^2_{21}$ at sub-percent — misattribution,
corrected).

[6] I. Esteban et al., NuFIT — global-fit $\Delta m^2_{31}$ input;
version sensitivity applies to the hybrid $S$ above.

**Companions:** [C0] the fixed-point theory (the constant's
pedigree); [C2] the representation theorem; [VII] the registered
undressed point and its correction record (the two claims are
mutually exclusive and cross-declared).
