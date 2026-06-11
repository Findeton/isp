# Paper 38 (v6) - SHARD: The Count and the Weight - Closing O35.1b, and What p = eps Refuses to Be

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

> **CORRECTION (2026-06-11, hostile review).**  Section
> 1's "knot resolved" and Section 3's A3 realization are
> CORRECTED: (a) the A3 seesaw (RH-sector charges, neutral
> orthogonal Dirac Y) verified a HAND-BUILT M_R whose diag entries
> violate the selection rule's own parity (Majorana bilinears
> carry even total charge: odd powers of sqrt(eps_eff) cannot
> appear on the diagonal); the exhaustive rule-allowed scan never
> reaches the rungs (code/v6_p38b_parity_obstruction.py); (b) the
> orthogonality of Y was an unlisted measure-zero assumption -
> "exact rungs for ANY neutral Y" is false for generic
> (non-orthogonal) neutral Y; (c) the consistent-grading reading
> triggers the textbook FN cancellation of RH charges (Altarelli-
> Feruglio).  O35.1b's status REVERTS: the selection-rule theorem
> stands; its rung application survives only in the LH-half-charge
> Weinberg realization with its menu (paper-IX,
> rebuilt; live members 0.172747 and 0.167880 - a first printing
> said 0.169993, transcription error vs the receipt, corrected).  The "superselection requires the seam for mixing"
> corollary is withdrawn (scope conflation).

Subtitle:

```text
The last two gaps in the bridge, attacked under pre-registered
criteria.  PHASE A (the count, O35.1b): in a record algebra
carrying a graded family charge with all sealed generators
neutral except ONE charged seam, the SELECTION RULE is a theorem
- transition amplitudes between sectors vanish exactly unless
the word's seam count balances the charge difference (receipt:
0 violations in 27,000 matrix elements), and the leading
balanced amplitude saturates ||S||^(units) exactly
(0.175384 = sqrt(eps_eff); 0.030759 = eps_eff).  Remove the
seam and the sectors disconnect EXACTLY: family charge is
superselected unless the seam exists, so neutrino oscillations
REQUIRE the breaking seam - the mechanism predicts its own
necessity.  The superselection-versus-mixing knot resolves
itself: putting the charges on the SEALED RIGHT-HANDED sector
(exactly the structure Paper 34's minimal texture already had)
makes the seesaw a conjugation - the light spectrum lands on the
eps_eff rungs EXACTLY for ANY neutral orthogonal Dirac sector
(receipt: ratios match eps_eff and sqrt(eps_eff) to 10 digits),
while large PMNS mixing lives entirely in the neutral sector,
untouched by the grading.  The mechanism class is
FROGGATT-NIELSEN (1979), credited; the record version's novelty
is the DERIVED suppression (the Seam Theorem), the
superselection pedigree (the silent-phase argument pattern of
univalence), and the registered consequence set (Paper 37).
PHASE B (p = eps): the pre-registered referent scan - ten exact
candidates for "the commit weight of the marginal triangle"
tested at 25 digits - returns exactly ONE match, and it is the
definitional combination itself.  p = eps is therefore NOT
derived; it survives as the sharpened one-line premise "the
seam weight is the normalized first-order binding deficit of
the marginal triangle," and per the pre-registration this is
the sharpened-premise outcome, recorded as such, not spun.  The
assembled bridge now reads: three theorems, four named premises,
one minimality selection - the cleanest the ladder has ever
been, and every remaining premise has a kill criterion.
```

## 0. Pre-registration and what this campaign was allowed to claim

Criteria fixed before computation (printed verbatim at the top of
the canonical output): Phase A succeeds only as a theorem with
receipts; Phase B's three admissible outcomes — derivation,
sharpened premise, or across-the-board exclusion *counted against
the mechanism* — were declared in advance, with no candidate
added after seeing its value.  Receipts:
`code/v6_p38_count_campaign.py`, canonical
`/tmp/v6_p38_campaign.out`, bit-identical rerun verified.

## 1. Phase A: the count is a theorem

**Theorem (selection rule).**  Let a record algebra carry a
graded charge $Q$ with eigenvalue $x \in \tfrac12\mathbb Z$ per
sector, all sealed generators $Q$-neutral except one seam $S$
shifting $Q$ by one unit.  Then for any word $W$ in the
generators, $\langle x'|W|x\rangle = 0$ unless the seam count of
$W$ (insertions minus adjoints) equals the charge difference;
and since neutral letters are contractions, the leading balanced
amplitude is $\lVert S\rVert^{\,\text{units}}$.  With $\lVert
S\rVert = \sqrt{\varepsilon(1-\varepsilon)}$ from the Seam
Theorem (Paper 37), a rung step of half a unit costs exactly one
amplitude factor $\sqrt{\varepsilon_{\rm eff}}$ — **the count,
O35.1b, closed as a theorem given the grading premises.**

*Proof*: decompose any word into $Q$-homogeneous components;
matrix elements between sectors pick out the component of charge
$x' - x$, which contains exactly the balanced seam count; the
norm bound is submultiplicativity.  *Receipts*: 0 violations in
27,000 randomly generated matrix elements (exact zeros); maximal
one-unit amplitude $0.175384 = \sqrt{\varepsilon_{\rm eff}}$ and
two-unit amplitude $0.030759 = \varepsilon_{\rm eff}$, saturated.

**The self-consistency bonus.**  Remove the seam and the sectors
disconnect *exactly* (receipt: maximal inter-sector amplitude
$0.0$ over 5,000 seamless words): family charge is superselected
unless the seam exists.  Since neutrino oscillations are
observed, **the mechanism predicts its own breaking seam must
exist** — the same object that carries the masses is the one
that permits the mixing.  A mechanism whose two jobs are done by
one object is the right kind of economical.

**The knot, resolved by a structure we already had.**  Exact
superselection of family charge would forbid oscillations — the
campaign's named danger.  The resolution: put the charges on the
*sealed right-handed sector only* (the Majorana seals at rungs
$0, \tfrac12, 1$), leaving the Dirac sector neutral.  Then the
seesaw is a conjugation, and the receipt shows the light
spectrum lands on the $\varepsilon_{\rm eff}$ rungs **exactly,
for any orthogonal neutral Dirac matrix** (ratios match
$\varepsilon_{\rm eff}$ and $\sqrt{\varepsilon_{\rm eff}}$ to
ten digits), while the PMNS mixing lives entirely in the neutral
sector — large mixing and superselected grading coexist.  This
is *precisely* the texture Paper 34's minimality selected before
any of this framing existed: the campaigns converged on one
structure from two independent directions, which is worth more
than either alone.  Honest grading: $\theta_{23} = 45^\circ$
remains minimality-*selected* (P34), not charge-*forced*.

**Credit, prominently.**  The mechanism class is
Froggatt–Nielsen (1979): masses suppressed by powers of a
symmetry-breaking insertion, one per unit of flavor charge.  The
record version adds what FN models never had: a *derived*
suppression factor (the Seam Theorem's
$\sqrt{\varepsilon(1-\varepsilon)}$, from stationarity), a
superselection pedigree for the charge (the silent-phase
argument pattern of univalence), and a registered consequence
set with pre-committed kills (Paper 37).

## 2. Phase B: what p = eps refuses to be

Ten exact candidates for "the commit weight of the marginal
triangle," computed from the triangle's own fixed point and
tested against $\varepsilon$ at 25 digits: codeword expectations
(fixed-point and free), commit-probability excess, amplitude and
occupation shifts, boundary deficits, the exact defect, and
control combinations.  Result: **one exact match — the
definitional combination $(3 - 1/\kappa)\kappa = 3\kappa - 1$
itself** (diff $6\times 10^{-42}$); everything else misses by
$0.007$–$0.4$.  No independent fixed-point referent equals
$\varepsilon$.

Per the pre-registration, this is the *sharpened-premise*
outcome: $p = \varepsilon$ stands as the named one-line
identification — **the seam weight is the normalized first-order
binding deficit of the marginal triangle** — not as a derived
quantity, and not (per the third admissible outcome) as an
exclusion, since the definitional reading is itself a coherent
referent.  The honest sentence: the theory says exactly once,
and without independent corroboration, that the marginality *is*
the weight.  That is where the ladder's empirical content
enters, and the grading now says so in one line instead of a
diffuse bridge.

## 3. The assembled bridge

```text
  THEOREM   selection rule: count = charge difference (Sec. 1)
  THEOREM   per-seam factor sqrt(eps(1-eps)) at stationarity (P37)
  THEOREM   light spectrum = eps_eff rungs for any neutral
            orthogonal Dirac sector (Sec. 1, exact receipt)
  PREMISE   family grading with silent inter-sector phases
            (univalence pattern -> superselection)
  PREMISE   seam uniqueness (one charged sealed object)
  PREMISE   S-atomicity; seam-block decoupling (P37)
  PREMISE   p = eps (sharpened, Sec. 2)
  SELECTED  theta23 = 45 deg (P34 minimality)
  CREDIT    Froggatt-Nielsen 1979 (mechanism class)
```

Three theorems, four premises, one selection.  Every premise now
carries a kill: K6 (the silent-phase argument fails for the
family grading — superselection pedigree lost), K7 (a second
charged sealed object exists — uniqueness dead), joining
K1–K5 of Paper 37.  The experimental exposure is unchanged and
unhedged: $S = 0.17275$ at JUNO-final, $\sin^2\theta_{23} =
\tfrac12$ against a current $3.1\sigma$ headwind, $\delta_{CP}
\in \{0, \pi\}$ at DUNE/HK.

## 4. Verdict

O35.1b is closed as a theorem *given the grading premises* — the
bridge's remaining freedom is now four named one-line premises,
each killable, instead of an unconstructed identification.  The
$p = \varepsilon$ gap did what the pre-registration anticipated:
it sharpened and refused to close, and that refusal is recorded
as the precise location where the program's one number meets the
world on trust.  The mechanism now has a name a phenomenologist
would recognize (Froggatt–Nielsen with derived suppression and
superselection pedigree), three independent ways to die in data,
and two ways to die on paper.  That is the most exposed — and
therefore the most scientific — position this ladder has ever
occupied.

## Receipts

```text
code/v6_p38_count_campaign.py   the whole campaign
/tmp/v6_p38_campaign.out        canonical (BIT-IDENTICAL rerun)
A1 selection rule: 0/27,000 violations; amplitudes saturate
   0.175384 / 0.030759 = sqrt(eps_eff) / eps_eff exactly;
A2 seamless superselection exact (0.0 over 5,000 words);
A3 FN-record seesaw: rung ratios match eps_eff, sqrt(eps_eff)
   to 10 digits for random orthogonal neutral Y;
B1 referent scan: 1/10 match, definitional only (6e-42).
```
