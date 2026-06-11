# Paper 37 (v6) - SHARD: The Seam Theorem - Stationarity Forces the Dressed Base, and What the Mechanism Then Predicts

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

> **CORRECTION (2026-06-11, hostile review of the
> publishable batch).**  Three withdrawals, with reasons:
> (1) P-MIX (sin^2 th23 = 1/2) and P-CPV (J = 0) are WITHDRAWN as
> mechanism consequences - both rested on requiring an ORTHOGONAL
> neutral Dirac matrix, an unlisted measure-zero assumption that
> also smuggled CP conservation and silently fixed th12/th13 to
> excluded values; P-BB falls with them (it used measured angles
> as undisclosed inputs).  (2) The Sec. 3 seesaw realization
> (charges on the RH seal sector) is PARITY-BROKEN: Majorana
> bilinears carry even total charge, so no rule-allowed texture
> reaches the half-integer rungs (exhaustive receipt:
> code/v6_p38b_parity_obstruction.py), and the consistent-grading
> reading triggers the textbook FN cancellation.  The surviving
> realization (LH half-charges on the Weinberg operator) gives a
> discrete FOUR-MEMBER spectrum menu with TWO members live against
> today's data - the rung point 0.172747 and
> the cheaper texture 0.167880 (a first printing of this block
> said 0.169993 - transcription error vs the receipt; corrected;
> a first printing also said TWO-MEMBER, missing the two already
> data-dead members 0.160500 [~7 sigma] and 0.675516 [~300 sigma]
> - for an exhaustive-enumeration claim the full menu is the
> honest count, corrected in a subsequent review)
> - live members adjudicable at 7.3 sigma at JUNO-final, with
> minimality favoring the (currently worse, -3.0 sigma) cheap
> texture.  (3) "Oscillations require the seam" is withdrawn
> (grading-scope conflation).  The Seam Theorem (Lemmas A/B,
> Theorem C) and the selection rule are UNAFFECTED as mathematics.
> Full treatment: v6/publishable/paper-IX (rebuilt) and the
> registration STATUS UPDATE.

Subtitle:

```text
Paper 36 reduced the bridge problem to one question: can a record
be sealed in modulus and silent in phase?  This campaign answers
it CONSTRUCTIVELY, inside Paper II's own representation theorem,
and the forcing mechanism turns out to be nothing new at all -
it is STATIONARITY, the T omega = omega condition the RP form has
carried since the day it was proved.  The chain (receipts exact
to 1e-16): (L-A) a sealed binary seam - rank-one PSD letters with
weights p and 1-p - has intertwiner norm sqrt(p(1-p)) |<u,v>|,
bounded by sqrt(p(1-p)); (L-B) the seam transfer operator has
top eigenvalue 1 - p(1-p)(1 - |<u,v>|^2) at leading order: it
admits a stationary vector IFF the poles are ALIGNED; (T-C)
therefore any stationary state overlapping a sealed seam forces
saturation: the per-seam factor is eps(1-eps) EXACTLY - the
dressed base, derived; (R-D) the seam phase is rephasing gauge
(axiom-S silent) while its modulus is physical: the O35.1 object
exists.  The saturated seam moreover has COMMUTING letters: the
maximal "coherence" is achieved by the classical, definite record
- exactly what a record-first ontology should have predicted of
itself.  What remains identified rather than derived, named
precisely: (i) S-atomicity (sealed = rank-one); (ii) seam-block
decoupling at stationarity; (iii) the seam weight = the binding
marginality eps; (iv) O35.1b - rung index = seam-insertion count.
The campaign then pays the Feynman tax: the mechanism's UNTUNED
consequence set is extracted and registered before the deciding
experiments report - maximal atmospheric mixing (sin^2 th23 =
1/2: currently 3.1 sigma AGAINST us, registered with eyes open),
vanishing leptonic Dirac CP violation (J = 0, delta in {0, pi}:
currently 0.6 sigma compatible; DUNE/HK decide), the full dressed
spectrum with no free coefficient (S = 0.1727469: -0.05 sigma at
JUNO-now), and a discrete four-value m_bb menu (0.4-4.8 meV;
below next-generation sensitivity, labeled consistency).  Five
kill criteria are pre-committed.  The mechanism now runs real
risk on three independent observables: that is the point.
```

## 0. Pre-registration and provenance

The criteria and the consequence list were fixed before
computation and are printed verbatim at the top of the canonical
output.  Provenance note: the *factor* was a known target (Papers
35-36); the *forcing mechanism* (stationarity) was not — it
emerged from asking, inside the RP formalism, when a seam admits
a stationary state at all.  The consequence set (Phase 2) was
fixed in advance of checking any of it against current fits;
where the data now disfavors a registered item, the item is
registered anyway and the tension stated.

Receipts: `code/v6_p37_seam_theorem_campaign.py`, canonical
`/tmp/v6_p37_campaign.out`, bit-identical rerun verified.

## 1. The Seam Theorem

**Setting** (Paper II, Theorem 2.1): a stationary RP process is a
Hilbert space with PSD letters $A_0, A_1$, $T = A_0 + A_1 \preceq
\mathbf 1$, and a unit stationary vector $T\omega = \omega$.

**Identification S-atom (named).**  A *sealed binary seam* is a
letter pair of rank one: $A_0 = p\,uu^\dagger$, $A_1 =
(1-p)\,vv^\dagger$, unit $u, v$.  (A sealed distinction has no
internal multiplicity; this is the seam-level form of atomicity,
graded as an identification.)

**Lemma A (intertwiner norm; exact).**
$\lVert\sqrt{A_0}\sqrt{A_1}\rVert = \sqrt{p(1-p)}\,
|\langle u, v\rangle| \le \sqrt{p(1-p)}$, with equality iff the
poles are aligned.  *Receipt*: identity verified to $2.8\times
10^{-16}$ over 200 random complex seams, $d = 2..5$.

**Lemma B (stationarity gate; exact).**  On the seam span,
$\lambda_{\max}(A_0 + A_1) = \tfrac12\bigl[1 + \sqrt{1 -
4p(1-p)(1 - |c|^2)}\bigr]$ with $c = \langle u, v\rangle$; hence
$\lambda_{\max} = 1$ iff $|c| = 1$ (for $p \notin \{0,1\}$), and
for misaligned seams the gap obeys $1 - \lambda_{\max} \ge
p(1-p)(1 - |c|^2)$ — strictly positive.  *Receipt*: closed form
verified to $3.3\times 10^{-16}$; gap coefficient $= 1.000$.

**Theorem C (stationarity forces the dressed base).**  Let the
seam block act invariantly at stationarity (premise *seam-block
decoupling*, named: $T$ restricted to the seam span is $A_0 +
A_1$ there, with no compensating coupling to the rest).  If the
stationary state overlaps the seam, Lemma B forces $|c| = 1$;
Lemma A then gives the per-seam intertwiner norm
$\sqrt{p(1-p)}$ *exactly*.  With the seam weight identified as
the binding marginality ($p = \varepsilon$, carried over from
Paper 35's framing and still an identification), the per-seam
factor is $\varepsilon(1-\varepsilon) = \varepsilon_{\rm eff}$ —
**the dressed base, derived from stationarity**.  No new
principle enters: the forcing condition is the same $T\omega =
\omega$ that Paper II's representation theorem has always
carried.

**Remark (the classical punchline).**  At saturation the letters
*commute* ($\lVert[A_0, A_1]\rVert = 0$, receipted): the seam
that maximizes the "coherence" norm is the classical, definite
record.  The factor $\varepsilon(1-\varepsilon)$ is not a quantum
residue — it is the two-pole weight of a sealed classical coin,
which is exactly what a record-first ontology should have said in
the first place.

**Remark D (the O35.1 object).**  $u \mapsto e^{i\varphi}u$
changes no letter and no word weight: the seam phase is
rephasing gauge — axiom-S silent — while the modulus is physical.
"Sealed in modulus, silent in phase" exists, constructively, and
is precisely the structure field theory already uses (mass-term
phases under fermion rephasing).

## 2. The bridge ledger after Theorem C

```text
   DERIVED:    the per-seam factor eps(1-eps)
               (from: S-atomicity + decoupling + stationarity)
   IDENTIFIED: S-atomicity (sealed = rank-one)
               seam-block decoupling at stationarity
               seam weight = binding marginality (p = eps)
   OPEN:       O35.1b - rung index = seam-insertion count
               (half-rung = one amplitude factor sqrt(eps_eff))
```

The gap has contracted from "derive the factor" (Papers 34-35)
through "find the object" (Paper 36) to "derive the count" — each
step receipted, none skipped.

## 3. The untuned consequence set (registered; local only)

All claims below are registered in
`external/registered-prediction-lepton-mixing-cp.md` (a local,
dated document, posted nowhere) with version-flagged global-fit
inputs.

- **P-SPEC**: the full dressed spectrum, no free coefficient:
  $m = (1.542, 8.793, 50.134)$ meV, $S = 0.1727469$ ($-0.05
  \sigma$ at JUNO-now), $\Sigma m_\nu = 60.47$ meV.
- **P-MIX**: $\sin^2\theta_{23} = \tfrac12$ exactly (provenance:
  Paper 34's minimal texture, derived before this framing).
  Current global fit $\sim 0.572^{+0.018}_{-0.023}$: **$3.1
  \sigma$ against us today**, with known octant instability
  across releases — registered with eyes open, exactly as the
  spectrum point was.
- **P-CPV**: silent seam phases make the mass matrices
  real-equivalent: Jarlskog $J = 0$, $\delta_{CP} \in \{0,
  \pi\}$.  Current fit $\delta \approx 197^\circ \pm 27^\circ$:
  $0.6\sigma$ from $180^\circ$ — compatible.  DUNE/HK decide.
- **P-BB**: Majorana phases frozen at $0/\pi$ give a *discrete*
  four-value $m_{\beta\beta}$ menu: $\{0.44, 2.54, 2.67, 4.77\}$
  meV — below next-generation sensitivity; a consistency
  statement, labeled as such.

The portfolio is the point: one observable lands at $-0.05
\sigma$, one at $0.6\sigma$, one at $3.1\sigma$ *against*.  A
mechanism that only retrodicted would have no business carrying
the third item; this one carries it because the texture that
produces the factor also produces maximal mixing, and we do not
get to keep one and hide the other.

## 4. Kill criteria (pre-committed)

```text
  K1  the decoupling or atomicity premise fails on
      construction of the full rung ledger            -> withdrawn
  K2  sin^2(th23) = 1/2 excluded at 5 sigma           -> P-MIX dead;
      the minimal texture dies with it
  K3  CP conservation excluded at 5 sigma (DUNE/HK)   -> the silent-
      phase mechanism dead
  K4  S = 0.17275 excluded at 5 sigma (JUNO-final)    -> dressed base
      dead
  K5  O35.1b shown impossible                          -> bridge dead
```

K2-K4 are independent experiments; the mechanism can now die
three separate ways without recourse.  That is what "untuned"
buys.

## 5. The Einstein/Feynman scorecard, settled honestly

Einstein's demand was a forcing principle, not a fitted referent:
delivered — the forcing is stationarity, an axiom-level condition
the formalism already owned, and the impossibility direction
holds (a misaligned sealed seam *cannot* host a stationary
state; gap $\ge p(1-p)(1-|c|^2)$, exact).  Feynman's demand was
risk on observables the mechanism was not built for: delivered —
three registered claims, one currently against us at $3.1
\sigma$.  What each would still object to, recorded: Einstein —
the count (O35.1b) and the $p = \varepsilon$ identification are
still choices; the theory does not yet leave *no* choice.
Feynman — the global-fit inputs are version-sensitive and the
$m_{\beta\beta}$ menu is untestable this generation; only K2-K4
carry real risk, and the verdicts are years out.  Both
objections are correct, and they are the remaining work.

## Receipts

```text
code/v6_p37_seam_theorem_campaign.py   the whole campaign
/tmp/v6_p37_campaign.out               canonical (BIT-IDENTICAL)
Pre-registration printed first; L-A identity 2.8e-16 (200 random
complex seams); L-B closed form 3.3e-16, gap coefficient 1.000;
T-C demo (p = eps, |c| = 0.9: lam_max = 0.994116, no stationary
overlap); commuting-letters receipt 0.0; P-SPEC/P-MIX/P-CPV/P-BB
numbers; kill table.
```
