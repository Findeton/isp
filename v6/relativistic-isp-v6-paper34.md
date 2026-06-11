# Paper 34 (v6) - SHARD: The Coefficient - Computing the Neutrino-Step Dressing Instead of Leaving It Free

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

Subtitle:

```text
The publishable-campaign referees proved a hard fact about the
corpus' one quantitative confrontation with nature: with the O(1)
coefficient C free, the half-integer exponent lattice covers the
entire exponent axis (the 68% texture spread [0.22, 1.26] spans
0.506 in exponent units >= the rung spacing 0.5) - ZERO
discriminating power.  The registration was rebuilt to the
undressed spectrum point (C = 1), which current data expects JUNO
to kill at ~5.6 sigma.  This paper runs the only honest rescue
attempt: MAKE C COMPUTABLE.  The result is not a rescue.  If the
ladder lives on the seam entries (Dirac Yukawa and Majorana
matrices) with unit coefficients, then C becomes a computable
function of the discrete texture, and the campaign computes the
attainable menu: 50 distinct values in the 2x2 sector, a sampled
joint (C, C1) cloud in 3x3.  THE PROGRAM'S OWN MINIMALITY
PRINCIPLE SELECTS C = 1 EXACTLY - the democratic Yukawa with
hierarchical Majorana spectrum reproduces the registered bare
point at maximal mixing, with both minimality readings agreeing.
So the expected JUNO exclusion would kill not a number but a
conjunction: ladder seams + unit coefficients + minimality.
Non-minimal survivors exist (13 per 2M sampled 3x3 textures, all
at >= 13 seams) and are named in advance as the post-hoc
flexibility a skeptic should discount.  Two structural findings
sharpen the test: the m1 coefficient is DEGENERATE with C in the
observable (C1 ~ 1.5 alone reconciles the bare rung with today's
data - one observable, two coefficients), and the charged-sector
dressings are NOT attainable in the unit-seam class (gaps >= 1.6%
against essentially exact masses), so the sector criterion
("D-shield": pre-EWSB seesaw shielded, EWSB seams dressed)
remains a named hypothesis counted against the program.  Verdict:
C is computable per texture; the program computes its own
registered point; the honest new content is a sharper falsifier
and a precisely mapped degeneracy, not a saved prediction.
```

## 0. The problem, and what would count as solving it

Paper 29's coefficient no-go and the publishable-campaign reviews
(v6/publishable/paper-VII, two independent referees) establish:

1. The registered content must be a *point*, not a lattice with a
   free O(1) coefficient: with $C$ free in $m_2/m_3 =
   C\varepsilon^{1/2}$, exponent and coefficient are exactly
   degenerate ($x = 1/2 + \ln C/\ln\varepsilon$), and the
   program's own 68% spread covers the axis.
2. The registered point $m_1 : m_2 : m_3 = \varepsilon :
   \sqrt\varepsilon : 1$ gives $S_\nu = \sqrt{\varepsilon/(1+
   \varepsilon)} = 0.17556$ vs the measured $0.1718 \pm 0.0026$:
   $1.4\sigma$ today, expected $\approx 5.6\sigma$ at JUNO if
   central values hold.

"Computing the coefficient" means: a procedure, fixed before
looking at the answer, that takes program structure as input and
returns $C$ (and ideally the $m_1$ coefficient $C_1$) with no
continuous freedom.  What the data needs, computed once and used
throughout (receipts: `code/v6_p34_coefficient_campaign.py`,
canonical `/tmp/v6_p34_campaign.out`, bit-identical rerun):

```text
   C_needed = 0.97924 +- 0.01433 (today) +- 0.00370 (JUNO-class)
   bare point C = 1: +1.45 sigma today, +5.62 sigma at JUNO
```

## 1. Lemma N1 (no universal dressing): C != 1 requires structure

If every mass dresses by a common factor ($m_i = D\,
\varepsilon^{x_i}$), ratios are bare: $C \equiv 1$ exactly
(receipted at machine zero for random $D$).  A rung-dependent
smooth dressing $D(x) = e^{gx}$ shifts the step by $e^{g/2}$ —
*one free parameter again*: fitting $g$ to the neutrino step is
exactly the move this paper exists to forbid.  Consequence: a
computed $C \neq 1$ can only come from (i) matrix structure (the
physical masses are eigenvalues of ladder-valued matrices, not
bare ladder entries), or (ii) a derived $g$ from the binding
chain (Section 6 — open).  This organizes the campaign: the
matrix route is executable now.

## 2. Route A: the ladder-seesaw class, exhaustively at 2x2

**The class (premises named).**  P25's ledger gives the neutrino
both Dirac and Majorana channels — the seesaw is the program's
own structure.  Premise A1 (*unit seams*): the ladder lives on
the seam entries — Dirac Yukawa $Y_{ij} = s_{ij}\,
\varepsilon^{n_{ij}}$ and Majorana $M_{ij} = s_{ij}\,
\varepsilon^{m_{ij}}$ with $s = \pm 1$, exponents on the
half-integer ladder $\{0, \tfrac12, 1, \tfrac32, 2\}$ or absent —
so the light masses $m_\nu = Y M^{-1} Y^{\mathsf T}$ carry
*computable* O(1) coefficients from matrix structure alone.
Premise A2: the 2-3 sector dominates the step (the $m_1$ sector
enters at $\varepsilon^2$; quantified in Section 4).  Premise A3
(*observational*): the 2-3 mixing is large (35-55 degrees).

**Exhaustive enumeration** (2x2 sector: $4 + 3$ exponents, signs;
all $\sim 10^6$ configurations):

```text
   textures landing on the sqrt(eps) rung (C in [0.5, 2]): 161,644
   ... with large 2-3 mixing:                                8,504
   distinct attainable C values (1e-4 grid):                    50
```

**Result A (minimality selects the bare point).**  Under BOTH
minimality readings (fewest seams; cheapest total exponent), the
minimal large-mixing textures all give

```text
   C = 1.0000 exactly, theta_23 = 45 deg:
   Y = (democratic, all entries +-1),  M = diag(1, eps^{1/2})
```

— the democratic Dirac matrix against a hierarchical Majorana
spectrum, i.e. *the registered undressed point, now with a
texture-level pedigree*: ladder seams + unit coefficients +
minimality + large mixing $\Rightarrow$ $C = 1$ and maximal
atmospheric mixing.  The campaign therefore does **not** rescue
the prediction; it deepens what the expected JUNO exclusion would
kill.  We state this as the paper's principal finding precisely
because it runs against our interest.

**Result B (the attainable menu and its honesty numbers).**  The
50 attainable values cover, within $\pm 2\sigma$(today) of any
value, 56% of the $C \in [0.5, 2]$ axis — so *today* the menu has
little discriminating power, and a match today is weak evidence
(look-elsewhere, counted).  At JUNO precision the coverage drops
to 25%.  Near the needed value:

```text
   attainable C within 3 sigma(today) of C_needed = 0.97924:
     0.9919  (+0.88 s today, +3.42 s JUNO)   7 seams, cost 1.5
     0.9997  (+1.43 s today, +5.53 s JUNO)   7 seams, cost 2.0
     1.0000  (+1.45 s today, +5.62 s JUNO)   6 seams, cost 0.5
   attainable values within 2 sigma(JUNO) of C_needed: NONE
   closed-form anchors (not all attainable in the class):
     sqrt(1-eps)  = 0.98397 (+0.33 s today, +1.28 s JUNO)
                    nearest attainable 0.008 away - NOT attainable
     sqrt(1-2eps) = 0.96768 (-0.81 s today, -3.13 s JUNO)
```

So within the 2x2 class: if JUNO confirms today's central values,
*no attainable coefficient survives* — subject to the $m_1$
degeneracy of Section 4, which is why Section 4 exists.

## 3. Route B: the charged sector refuses the same mechanism

Any texture mechanism gains credibility only if it also speaks to
the charged steps, which are measured essentially exactly.
Required dressings against the nearest rungs:

```text
   m_e/m_mu:   x = 1.546; vs rung 1.5:  C_req = 0.8529
               nearest attainable 0.8393  (off by 1.6%)
   m_mu/m_tau: x = 0.818; vs rung 0.5:  C_req = 0.3335 (off 102%)
                          vs rung 1.0:  C_req = 1.8699 (off 1.7%)
```

Percent-level gaps against $< 10^{-4}$ measurements: **the
unit-seam class does not reproduce the charged sector.**  The
sector criterion this forces — charged masses pass through EWSB
seams and acquire dressing the program has not computed, while
the seesaw step is sealed pre-EWSB and stays at unit seams
("D-shield") — is a *named hypothesis, not a derivation*, and
until the EWSB dressing is computed the charged sector neither
confirms nor calibrates the mechanism.  Counted against the
program, exactly as the publishable-campaign referee demanded a
stated criterion for which ratios are dressed.

## 4. The m1 degeneracy: one observable, two coefficients

The observable is $S^2 = (C^2\varepsilon - C_1^2\varepsilon^2)/
(1 - C_1^2\varepsilon^2)$ with $m_1 = C_1\,\varepsilon\, m_3$.
The $\varepsilon^2$ suppression of $C_1$ is offset by the
smallness of the errors:

```text
   C1 = 0.0:  S(C=1) = 0.17833   (+4.13 sigma_JUNO from C1=1)
   C1 = 1.0:  S(C=1) = 0.17556   (the registered point)
   C1 = 1.5:  S(C=1) = 0.17202   (-5.27 sigma_JUNO; 0.09 sigma
                                   from TODAY'S central value)
   C1 = 2.0:  S(C=1) = 0.16694
```

**$C_1 \approx 1.5$ alone reconciles the bare 2-3 rung with
today's data.**  The tension attributed to $C$ is equally
attributable to a heavier-than-rung $m_1$ — and no oscillation
measurement separates them ($S$ is one number; cosmological
$\Sigma m_\nu$ shifts by only $\sim 2.5$ meV between these
scenarios, below near-term sensitivity).  Two consequences,
stated honestly: (i) the Section 2 class exclusion at JUNO is
*conditional on pinning $C_1$* — with $C_1$ free in $[0, 2]$ the
inferred-$C$ band smears by $\pm 0.0475$ and 3 attainable values
re-enter; (ii) any claimed kill or survival at JUNO is a
statement about the *joint* $(C, C_1)$ texture, which is why the
3x3 campaign of Section 5 is the decisive receipt.

## 5. The 3x3 joint campaign (sampled; exhaustion named as next)

Full 3x3 exhaustion is $6^{15} \times$ signs — infeasible; we
sample 2,000,000 seeded textures (attainability results are
LOWER bounds) under the full constraint set: normal-ordered
spectrum on the rung, $\theta_{23} \in [35, 55]^\circ$,
$\theta_{12} \in [25, 40]^\circ$, $|U_{e3}| < 0.3$ (premise,
named: charged-lepton rotation approximately diagonal, so the
PMNS matrix is the neutrino diagonalizer).

```text
   PMNS-compatible NO textures on the rung:        1,120 / 2M
   consistent with S today (2 sigma):                 47
   would SURVIVE a confirmed-central JUNO:            13
   cheapest JUNO survivor: C = 0.9973, C1 = 1.3053,
     S_pred = 0.17309 (+0.50 sigma today),
     theta23 = 50, theta12 = 39, |Ue3| = 0.07,
     13 seams, cost 11.0
   bare-rung + heavy-m1 degeneracy realized (C ~ 1,
     C1 in [1.3, 1.7]): 8 textures, cheapest at 12 seams
   (minimal textures: 6 seams, cost 0.5, C = 1, C1 sector bare)
```

**Result C (the shape of the verdict).**  JUNO-surviving ladder
textures *exist* — but every sampled survivor sits at $\ge 13$
seams against the minimal 6.  A confirmed-central JUNO therefore
executes the **minimality principle**, not the ladder: the
program could only retreat to a non-minimal texture by giving an
independent, pre-stated reason for it, and we name this *in
advance* as exactly the post-hoc flexibility a skeptic should
discount (and that Route B already shows the program cannot
currently supply: it has no computed dressing anywhere).

## 6. The analytic route: deriving g from the binding chain

The one route that could produce a *derived* non-unit coefficient
without texture freedom: compute the subleading term of the
binding analysis ($\varepsilon = 3\kappa_b - 1$ from the
relation-code energetics) and ask whether rungs dress
rung-dependently, $D(x) = e^{gx}$ with $g$ *computed*.  Lemma N1
shows exactly what this must deliver: $C = e^{g/2}$, so matching
today's central value needs $g = 2\ln C_{\mathrm{needed}} =
-0.042$.  Status: **not executed** — the corpus' binding
analysis (P8/P10 [P]) determines the marginal point; its
second-order structure has not been computed, and we do not
pretend otherwise.  Named open problem O34.1, with the target
value $g = -0.042 \pm 0.029$ (today) recorded so that any future
derivation is checkable against a number fixed now.

## 7. Scope and limitations, collected

(i) The 2x2 enumeration is exhaustive at exponents $\le 2$;
larger exponents only add cost, so minimality results are stable
against the bound, but the attainable-menu statements carry it.
(ii) The 3x3 results are sampled lower bounds; the exhaustive 3x3
(or a branch-and-bound on cost) is the named next receipt.
(iii) Real matrices with sign freedom only — Majorana phases
beyond $\pm 1$ are not scanned; they widen the menu and can only
weaken exclusions, never the minimality result.  (iv) The
PMNS-from-neutrino-sector premise (diagonal charged rotation) is
named; relaxing it reshuffles the mixing filters.  (v) The
mixing windows are the observed ranges; results were not tuned
against them (the minimality result is window-independent: the
democratic texture gives exactly 45 degrees).

## 8. Verdict, ledger updates, and falsifiers

**Verdict.**  The coefficient is computable per texture — the
unfalsifiability the referees identified is repaired in
principle.  But computing it does not move the prediction: the
program's own minimality selects the registered bare point
$C = 1$ (now with a texture derivation and a maximal-mixing
corollary), the data still expects that point to die at JUNO,
and the survivors are non-minimal.  The honest gains are
structural: a discrete falsifiable menu instead of a free
parameter, a mapped $(C, C_1)$ degeneracy, a charged-sector
no-go for the same mechanism, and a numerically pinned target
for the one analytic route that could still derive a non-unit
coefficient.

**Ledger updates** (P25/P29 rows, restated here):

- **P-eps-nu (registration)**: UNCHANGED — the undressed spectrum
  point stands as registered in v6/publishable/paper-VII, now
  with the texture pedigree of Section 2 (minimality
  $\Rightarrow$ C = 1, theta23 = 45 deg).  Expected outcome at
  current centrals remains death at ~5.6 sigma; what dies is the
  conjunction [ladder seams + unit coefficients + minimality].
- **NEW P-TEX (the sharpened falsifier)**: if JUNO confirms
  today's central values, the minimal unit-seam ladder-seesaw
  class is excluded; any continuation via a non-minimal texture
  requires an independent pre-stated selection principle, absent
  which the lattice mechanism for neutrino masses should be
  regarded as refuted in its predictive form.
- **NEW O34.1 (the analytic target)**: a future binding-chain
  derivation of rung dressing must produce
  $g = -0.042 \pm 0.029$ (today's value, recorded in advance);
  producing instead $g \approx 0$ confirms the bare point against
  the data.  *[Superseded by Paper 35's O35.1 after JUNO's first
  data: the target is now $g = \ln(1-\varepsilon) =
  -0.0322842083$ (pinned), the single-relation route is closed by
  theorem (P35 Secs. 4-5), and the surviving route is the
  relation-to-rung bridge.]*

## 9. Status update: JUNO's first data (dated 2026-06-11)

After this campaign was designed, we checked the experimental
record: **JUNO has already published its first measurement**
(59.1 days; arXiv:2511.14593; Nature 654, 343 (2026)):
$\Delta m^2_{21} = (7.50 \pm 0.12)\times 10^{-5}\,\mathrm{eV}^2$
(NO), already $1.6\times$ more precise than all prior data
combined.  Recomputed against it (receipts, Section F):

```text
   S = 0.17283 +- 0.00167          (was 0.17179 +- 0.00260)
   registered point 0.17556: +1.64 sigma   (was +1.45)
   needed dm21 = 7.739e-5: +1.99 sigma from JUNO's measurement
   C_needed = 0.98494 +- 0.00918   (was 0.97924 +- 0.01433)
     bare C = 1 (minimal texture):      +1.64 sigma
     nearest attainable 2x2 (0.9919):   +0.76 sigma
     sqrt(1-eps) anchor (NOT attainable in class): -0.11 sigma
   C1 reconciling bare rung with the new central: 1.403
```

Reading, stated carefully: the central value **moved toward the
registered point** (the survival branch's required drift has
partially materialized — about a third of the needed shift), while
the error shrank, leaving the tension nearly unchanged.  The
data is converging numerically toward the unattainable
$\sqrt{1-\varepsilon}$ anchor — which this campaign showed the
unit-seam 2x2 class cannot produce — while the nearest attainable
texture value ($0.9919$) remains compatible at $+0.76\sigma$.
Nothing in this update changes the verdict structure: the minimal
texture (bare point) sits at the pre-committed watch level, and
the next factor-of-3 in JUNO precision decides.  This section is a
dated addendum; the Section 0-8 numbers are the campaign snapshot
and are preserved as written.

## Receipts

```text
code/v6_p34_coefficient_campaign.py   the whole campaign
/tmp/v6_p34_campaign.out              canonical output
                                      (BIT-IDENTICAL rerun verified)
Sections: TARGET (C_needed both precisions); N1; A (exhaustive
2x2: 161,644 / 8,504 / 50; minimality -> C = 1; menu coverage
56% / 25%; near-needed list; anchors); B (charged gaps 1.6% /
102% / 1.7%); C (JUNO separability 4.3-8.7 sigma between
anchors); D (m1 smearing +-0.0475, 3 values re-enter); E (3x3
sampled: 1,120 / 47 / 13; cheapest survivor; degeneracy
realized at 12 seams).
```
