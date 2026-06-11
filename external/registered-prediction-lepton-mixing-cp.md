# Registered predictions: lepton mixing, CP violation, and the dressed spectrum

*Registration date: 2026-06-11.  Local document — registered for
internal discipline only; not posted or submitted anywhere.
Provenance: corpus Paper 37 (the Seam Theorem campaign); claim
forms fixed in the campaign's pre-registration BEFORE any was
checked against current fits.*

> **STATUS UPDATE / WITHDRAWALS (2026-06-11, hostile
> review).**  P-MIX and P-CPV are WITHDRAWN as mechanism-derived
> claims: review exposed that both rested on an unlisted
> orthogonality assumption on the neutral Dirac sector
> (measure-zero, no symmetry; it also smuggled CP conservation and
> fixed th12/th13 to excluded values).  P-BB is withdrawn with
> them (it used measured mixing angles as undisclosed inputs).
> P-SPEC is REVISED to the menu of the surviving (LH-half-charge
> Weinberg) realization: live members S in {0.172747 [rung point,
> -0.05 sigma vs JUNO-now], 0.167880 [cheap texture, -3.0 sigma]}
> (the full menu has FOUR members - the other two, 0.160500 [~7
> sigma] and 0.675516 [~300 sigma], are already data-dead and are
> listed in paper-IX as falsified members, not hidden; a first
> printing of this block said 0.169993 for the
> cheap texture - transcription error vs the receipt, corrected);
> live members separated by 7.3 sigma at JUNO-final; minimality
> favors the second.  Outcome bands incl. the both-members-die
> branch are pre-assigned in paper-IX Sec. 4.  K2/K3 lapse with the withdrawals;
> K4 splits into K4a (rung point) / K4b (cheap texture); K1/K5-K7
> stand.  The parity obstruction and the menu receipts:
> code/v6_p38b_parity_obstruction.py; full treatment paper-IX
> (rebuilt).  Withdrawal, per the pre-registration's own rule, is
> recorded here rather than by deletion.

## Provenance chain (honesty first)

The mechanism: sealed binary seams (rank-one letter pairs) that
support a stationary state are forced to alignment (Paper 37,
Lemmas A/B, Theorem C), giving per-seam factor eps(1-eps) with
phase pure rephasing gauge.  The factor's VALUE was a known
target (post-diction, Papers 35-36, look-elsewhere counted
there); the FORCING (stationarity) and the consequence set below
were not tuned to data.  Named identifications still open:
S-atomicity; seam-block decoupling; seam weight = eps; rung =
seam count (O35.1b).  Exact constants: eps =
0.0317686364465818 (P8 closed form; 10+ digit rule per Paper 35).

## The registered claims

**P-SPEC (the dressed spectrum; no free coefficient).**
m1 : m2 : m3 = eps_eff : sqrt(eps_eff) : 1 with eps_eff =
eps(1-eps) = 0.0307593901849:

    S_nu = 0.1727469
    m = (1.542, 8.793, 50.134) meV   (dm31 = 2.511e-3 input)
    Sum(m_nu) = 60.47 meV

Status at registration: JUNO-first-data S = 0.17283 +- 0.00167
-> -0.05 sigma.  NOTE: this REPLACES nothing — the program's
registered point remains the undressed spectrum (see
registered-prediction-neutrino-step.md); P-SPEC is registered as
the MECHANISM'S claim, conditional on the Paper 37 premises, and
the two are distinguished exactly so the experiment can kill
either separately.

**P-MIX (maximal atmospheric mixing).**

    sin^2(theta_23) = 1/2 exactly

Provenance: Paper 34's minimal texture (derived before the seam
framing existed).  Status at registration: global fits ~ 0.572
+0.018/-0.023 (NO; version-unstable octant): ~3.1 sigma AGAINST.
Registered with eyes open.  Resolving data: JUNO + atmospheric
(DUNE/HK).  Pre-commitment: 5-sigma exclusion of maximality kills
P-MIX and the minimal texture with it; we will report it as
failed, not as "tension."

**P-CPV (no leptonic Dirac CP violation).**

    Jarlskog J = 0;  delta_CP in {0, pi}

From silent seam phases (mass matrices real-equivalent).  Status
at registration: delta ~ 197 +- 27 deg (NO) -> 0.6 sigma from
180 deg: compatible.  Resolving data: DUNE / Hyper-K.
Pre-commitment: 5-sigma exclusion of BOTH CP-conserving values
kills the silent-phase mechanism outright.

**P-BB (discrete Majorana menu; consistency only).**
Phases frozen at 0/pi give exactly four values under the dressed
spectrum (inputs sin^2 th12 = 0.303, sin^2 th13 = 0.02225):

    m_bb in {0.44, 2.54, 2.67, 4.77} meV

All below next-generation 0vbb sensitivity: registered as a
consistency statement with NO claimed discriminating power this
generation.

## Premises and voiding

- Normal ordering (voided by established IO, as in the
  neutrino-step registration).
- Global-fit inputs are NuFIT 5.x-class central values; version
  sensitivity flagged; each test is defined against the resolving
  experiment's own measurement, not against any fit.
- The mechanism premises (S-atomicity, decoupling, p = eps,
  O35.1b) are named in Paper 37; K1 withdrawal applies if any
  fails on construction.

## Kill table (verbatim from Paper 37)

    K1  premise failure on the full rung ledger     -> withdrawn
    K2  sin^2(th23) = 1/2 excluded at 5 sigma       -> P-MIX dead
    K3  CP conservation excluded at 5 sigma         -> mechanism dead
    K4  S = 0.17275 excluded at 5 sigma (JUNO)      -> dressed base dead
    K5  O35.1b shown impossible                     -> bridge dead

Third-party timestamping (Zenodo deposit of this file + Paper 37
+ receipts) remains the named next step and has NOT been done;
until then this registration has no evidential standing beyond
this repository's own dating.
