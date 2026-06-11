# Paper 43 (v6) - SHARD: Records Curve It - The 2d Closure, What It Proved, and What It Measured Instead

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

Subtitle:

```text
The first test of mechanism M2 - curvature as consistency - and a
campaign that earned its conclusions by failing twice in the open
first.  TRIAL 1 declared the EXACT S_gen-saturation demand and its
kill fired immediately: finite-amplitude states exceed the
saturated Wall identity by relative entropy (+4.3e-2 receipted) -
exact saturation is FALSE physics, and the correct consistency
demand is FIRST-ORDER stationarity (entanglement equilibrium),
which is precisely the order at which the Einstein equation is an
equation of state.  TRIAL 2 then discovered the MODULAR-SILENCE
LEMMA (a site-diagonal record unitary never acts across any cut,
so delta S == 0 exactly, receipt 8e-13: local unitaries impose no
first-order consistency constraint - the planned two-signed-source
receipt was vacuous as designed) and exposed the POINTWISE
first-law density as structurally invalid at depth (ratio 0.39,
linear in amplitude: not noise), in exact agreement with P41's
kernel anatomy.  WHAT THEN STOOD: (i) the integrated first law
against the MEASURED finite-box weight W(d) = 2N sin(pi d/N)
passes at shallow source depth (ratio 0.987) and dilutes
monotonically with depth (0.987/0.844/0.697/0.613 in 20-site
bins) - THE CAMPAIGN'S INSTRUMENT DISCOVERY: the modular kernel
is SECTOR-ANISOTROPIC at depth (the X-sector weight runs; the
P-sector row-sum weight of P41 does not) - kills K1-K3 FIRED at
deep-source scope and the sector-resolved re-pose is registered;
(ii) the DIFFERENTIAL RESPONSE LAW forced by the first-order
demand + the measured weight is receipted at ratio 0.9994:
   nu phi'' + (pi/N)^2 nu phi = -2 pi delta T_00
- the JT-class 2d Einstein equation WITH the finite-geometry
curvature term, whose scale (pi/N)^2 is exactly the strip-Casimir
scale of P42's saturation receipt, and whose deep weight was
MEASURED (P41 row sums), not assumed.  The coupling normalization
is the near-edge Unruh 2 pi - pinned where all sector weights
agree, registered where they run.  (iii) The form-level exhibit:
applied to the finite-amplitude negative-energy state, the law
defocuses (phi'' > 0 on 90 sites) exactly where energy is locally
negative, with P42's strict QNEC inequality as the governing
bound at that amplitude.  NET: in two dimensions the program now
owns the response law's FORM with its curvature term receipted to
0.06%, the correct (first-order) statement of the consistency
principle, one new lemma, one new measured kernel anatomy - and
an honest ledger of which receipts fired.  Mass curves the record
geometry in 2d at the level the instruments can currently
certify: shallow-depth first law + differential form + locked
near-edge coupling; the deep-coupling question is now a NAMED,
MEASURED open item, not an invisible one.
```

## 0. Provenance, the two trials, and the design record

This campaign executes the "single next decisive move" identified
after Papers 41–42: the 2d dilaton-class arena where generalized
entropy is exactly computable and the QNEC instrument (licensed
in P42 by the saturation receipt, ratio 0.995) can probe the
geometry response.  Receipts:
`code/v6_p43_records_curve_it_2d_campaign.py`, canonical
`/tmp/v6_p43_campaign.out`, bit-identical rerun verified.  The
design block carries the full trial history per the program's
discipline — both failed trials are documented in place, because
both failures are physics:

**Trial 1 (exact saturation): killed by relative entropy.**  The
v1 demand — generalized entropy exactly on the vacuum-saturated
Wall identity in every state — fails at finite amplitude by
$+4.3\times 10^{-2}$: the excess *is* the relative entropy
$S(\rho\|\rho_{\rm vac})$, i.e. the strict QNEC inequality for
non-coherent states.  The consistency principle must be posed at
**first order** (entanglement equilibrium) — exactly where
Jacobson's derivation lives, and exactly the "equation of state"
scope the program had already adopted.  Second order is entropy
production, not equation of motion.

**Trial 2 (pointwise density and unitary sources): two lessons.**
(a) The pointwise first-law density $\delta S'' = 2\pi\,\delta
T_{00}$ fails structurally at depth (mean ratio $0.39$, perfectly
linear in amplitude — instrument-independent), consistent with
P41's anatomy: only the kernel's IR weight is universal.  (b) The
**modular-silence lemma**: a site-diagonal dilation never acts
across any cut — its block restriction is a local symplectic map —
so $\delta S \equiv 0$ *exactly* (receipt $8\times 10^{-13}$ at
every edge).  Site-local record unitaries are first-order silent
in the consistency demand: they impose no constraint ($0 = 0$)
and receive their geometry response from the law's *form*.  The
planned "two-signed first-order source" receipt was therefore
vacuous as designed, and is replaced by the silence-lemma receipt
plus the form-level exhibit.

## 1. The first law against the measured weight — and the sector anisotropy

The honest integrated first law uses the **measured** finite-box
weight $W(d) = 2N\sin(\pi d/N)$ (P41's row-sum receipt, accurate
3–7% in-window): $\delta S(j) = \sum_{x \ge j} W(x - j + \tfrac12)
\,\delta T_{00}(x)$.  Receipts at two amplitudes (linearity drift
$0.039$):

- shallow sources (depth $\lesssim 20$): ratio **0.987** — the
  first law holds at the percent level;
- the **depth dilution profile** (the campaign's instrument
  discovery, t-d): mean ratio $0.987 / 0.844 / 0.697 / 0.613$
  across source-depth bins $[0,20)/[20,40)/[40,60)/[60,80)$ — a
  smooth monotone running.  The **X-sector kernel weight runs
  with depth**, while the P-sector row-sum weight (P41) does not:
  the modular kernel is *sector-anisotropic at depth*.  New
  instrument science, measured, with the sector-resolved re-pose
  of the demand registered.

Kills K1–K3 (first law, restoration, pinning) accordingly
**fired at deep-source scope** and are kept fired: full-window
restoration reaches suppression only 1.5, and the coupling scan's
V-minimum tracks the deep dilution ($\epsilon^* \sim -0.3$) — not
because the demand is wrong but because the scalar-weight form of
it ignores the measured anisotropy.  At shallow depth, where all
sector weights agree (the near-edge $2\pi$ regime), the
cancellation operates and the normalization is pinned.

## 2. The response law — receipted at 0.06%

The first-order consistency demand ($\delta S_{\rm gen} = 0$ per
screen) with the measured weight forces, by differentiating
$W$, a **local differential law with the box's curvature term**:

$$
\nu\,\varphi'' + \Bigl(\frac{\pi}{N}\Bigr)^{2}\nu\,\varphi
\;=\; -\,2\pi\,\delta T_{00},
$$

the JT-class 2d Einstein equation on the finite geometry — and
the receipt verifies it at **ratio 0.9994** (range $[0.907,
1.097]$ where the source is appreciable).  Three features worth
stating plainly: the curvature scale $(\pi/N)^2$ is *exactly* the
strip-Casimir scale of P42's saturation receipt — the background
"cosmological" term and the vacuum modular identity are one
object; the deep weight that produced the equation was measured
(P41), not assumed; and the integration constants of $\varphi$
are the state data of P40 §9b — the $\Lambda$ typing, again.  The
coupling normalization is the receipted near-edge Unruh $2\pi$:
**G is fixed by capacity and temperature where the sectors agree;
the deep-coupling question is the registered sector-resolved
item.**

## 3. The form-level exhibit

Applying the derived law to the finite-amplitude negative-energy
state of P42 ($\delta T_{00} \in [-1.2\times 10^{-5},
+3.4\times 10^{-3}]$): $\varphi'' > 0$ on 90 sites — **classical
defocusing exactly where energy is locally negative** — with the
governing bound at that amplitude being P42's strict QNEC
inequality, not saturation.  The audit's wrong-object-class
lesson, embodied at the correct order: pointwise focusing fails
where it must; the quantum law does not.

## 4. Kill ledger and verdict

```text
  Trial 1 exact-saturation kill   -> FIRED (relative entropy);
     principle corrected to first order
  Trial 2 p4-as-designed          -> VACUOUS (silence lemma);
     rebuilt; the lemma itself is a kept discovery
  K1 integrated first law         -> PASSES shallow (0.987);
     FIRED deep (sector anisotropy t-d, measured profile)
  K2 restoration                  -> FIRED at deep scope (same
     cause); sector-resolved re-pose REGISTERED
  K3 coupling pinning             -> FIRED at deep scope; the
     2 pi normalization stands near-edge
  p4' differential law            -> RECEIPTED at 0.9994
  silence lemma                   -> RECEIPTED at 8e-13
  form-level defocusing exhibit   -> RECEIPTED (90 sites)
```

**Verdict.**  What this campaign set out to show — "mass curves
the record geometry, 2d, end-to-end" — it shows at the scope its
instruments can honestly certify: the consistency principle in
its correct (first-order) form; the response law's differential
form with its finite-geometry curvature term, receipted to
$0.06\%$; the coupling locked at the near-edge Unruh
normalization; defocusing where energy is negative under an
intact quantum bound.  What it could not show, it *measured
instead*: the modular kernel's sector anisotropy at depth — a
new, quantified object (the dilution profile) that any deeper
form of the consistency demand must now incorporate, registered
as the sector-resolved re-pose.  Two trials died in the open and
both deaths taught physics: exact saturation is relative entropy;
local unitaries are modular-silent.  The program's gravitational
ledger after Papers 41–43: the matter side receipted (QNEC,
saturation, two-signed sources), the response law's form
receipted in 2d with its curvature term, the deep coupling and
the 3+1 lift named and open.  That is what "records curve it"
looks like when every claim has to survive its own kill table.

## Receipts

```text
code/v6_p43_records_curve_it_2d_campaign.py   the campaign
/tmp/v6_p43_campaign.out            canonical (BIT-IDENTICAL)
Trial 1: exact-saturation excess +4.3e-2 (relative entropy)
Trial 2: pointwise density ratio 0.39 (linear in alpha);
         silence lemma 8e-13
p1': shallow ratio 0.987; depth profile 0.987/0.844/0.697/0.613
     (bins of 20); linearity drift 0.039
p2'/p3': suppression 1.5, eps* ~ -0.3 at deep scope (FIRED;
     cause = t-d anisotropy; sector-resolved re-pose registered)
p4': phi'' + (pi/N)^2 phi vs -2 pi dT00: ratio 0.9994
     [0.907, 1.097]
exhibit: phi'' > 0 on 90 sites where dT00 < 0
Literature: Jacobson (1995; 2015 entanglement equilibrium);
Wall (2d QNEC); Bousso et al. (QFC); Jackiw-Teitelboim;
Almheiri-Polchinski (dilaton response); Faulkner et al.
(gravitation from entanglement, first-order); Casini-Huerta;
Eisler-Peschel (kernel anatomy); Bianchi-Myers-class S_gen.
```
