# Paper 47 (v6) - SHARD: The Tower Receipt - the Modular-Gap Tower Clause at Free Level: the Equivalence, the Exact Anchor, and the Detector

Preprint, not peer reviewed, version 2026-06-12.

Author: Felix Robles Elvira

Subtitle:

```text
A short receipt paper on the tower clause of the modular-gap
conjecture (C46), at free level.  THE FIRST FINDING IS AN
EQUIVALENCE, receipted up front: on a refinement tower (fixed
physical box L = 512 a_0 and mass m_phys = 0.4/a_0, spacing
halving; N = 512..4096, m_lat = 0.4..0.05) the gapped plateaus
are N-INDEPENDENT to machine precision (plateau 3.7e-15,
deficit-profile point 1.7e-15), so the free
tower IS the registration's mass-at-fixed-spacing stand-in -
the free tower clause REDUCES to the mass-scaling law, and the
conjecture's nontrivial tower content lives exactly at the
interacting/gauge wall (registered).  Within that scope, every
assertion of the clause is measured and anchored:
(1) THE EXACT ANCHOR: plateau eps_1 per level matches the
corner-transfer closed form eps_1 = pi K(k')/K(k), with
k + 1/k = 2 + m^2, to MACHINE PRECISION (rel 9e-16..9e-15,
zero free parameters); its small-m asymptote pi^2/ln(8/m)
identifies the corpus's recurring pi^2 as ONE COEFFICIENT -
the CTM pi^2, with the modulus-scale-8 reading receipted for
the gapped family (Bc = 8.265 ~ 8); gapless fits share the
coefficient with a geometry-dependent scale.  A blind
two-parameter fit on levels 0-2 is kept as an instrument demo
(out-of-sample level-3 prediction 0.13%, kill at 1%).
(2) THE UNIFORMITY CLAUSE: B* per level from a two-stage
detector (coarse bracket + INTEGER-grid refinement + log-log
interpolation; a declared refinement of the registration's
grid-step criterion, consistent where they overlap), at three
deficit targets with the interpolation systematic quantified
(max 1.8% coarse-vs-refined): B* DOUBLES per level - ratios
1.953/1.944/1.941 (3e-3) -> 1.957/1.952/1.950 (1e-3) ->
1.960/1.959/1.958 (3e-4), kill window [1.8, 2.2] - B* a_k
uniform in physical units at leading order, with the
detector's log-subleading drift SHRINKING monotonically under
tighter targets (a direction kill).  Honesty: at fixed target
the B* a_k drift grows mildly along the tower, and three
targets cannot FULLY distinguish detector prefactor from a
slow violation - the residual ambiguity is registered.
(3) THE GAPLESS TOWER: no positive plateau at any level -
across-level collapse (1.2758 -> 1.0051), per-level monotone
sweeps, and THE DECISIVE RECEIPT (monotonicity alone cannot
exclude a plateau): the per-level fit eps_1(B) = a/(ln B + b)
at N = 4096 with a = 9.936 ~ pi^2, rms 0.03% - eps_1 -> 0 as
B grows; no positive plateau is consistent with the receipted
form (fit-supported, registered as such).
NOT claimed: anything beyond free level; the wall; novelty of
the CTM form (cited and deployed); full detector-vs-violation
distinction at the receipted targets.
```

## 0. The tower, the object, and the equivalence

A refinement tower at fixed physical scales: $L_{\rm phys} =
512\,a_0$, $m_{\rm phys} = 0.4/a_0$; level $k$ has $a_k =
a_0/2^k$, $N_k = 512\cdot2^k$, $m_k = 0.4/2^k$, $k = 0..3$.
Gapless tower: same geometry, $m_{\rm phys} = 0$.  Screens:
single-cut end blocks; plateaus at the half-chain.  Instrument:
float64, valid at the low end of the modular spectrum
(receipted in the registration campaign; cited).

**The equivalence (K-EQUIV), stated up front.**  At free level
the gapped plateaus *and deficit profiles* are $N$-independent
to machine precision (receipted: plateau($m{=}0.2$) at $N =
512$ vs $1024$, rel diff $3.7\times10^{-15}$; deficit-profile
point ($m{=}0.2$, $B{=}16$) across the same $N$,
$1.7\times10^{-15}$ — the $B^*a_k$ bookkeeping rests on profile
independence, so both are receipted) — so the free tower is
*numerically the registration's mass-at-fixed-spacing
stand-in*: the free tower
clause reduces to the mass-scaling law.  What the tower
construction contributes is the physical-units bookkeeping
($B^*a_k$), one new level ($m = 0.05$), the exact anchor, and
the refined detector — and the equivalence itself, which
locates the conjecture's nontrivial tower content exactly at
the interacting/gauge wall (registered).

Receipts: `code/v6_p47_tower_receipt_campaign.py`, canonical
`/tmp/v6_p47_campaign.out`, bit-identical rerun verified;
ledger generated from computed flags.

## 1. The value clause — the exact anchor

```text
  level a_0:    m = 0.4:   3.283767
  level a_0/2:  m = 0.2:   2.673697
  level a_0/4:  m = 0.1:   2.251971
  level a_0/8:  m = 0.05:  1.944623
```

**The exact anchor (K-CTM, zero free parameters):** every
plateau matches the corner-transfer closed form

$$\varepsilon_1 = \pi\,\frac{K(k')}{K(k)}, \qquad k +
\tfrac1k = 2 + m^2$$

to machine precision (rel $9\times10^{-16}$–$9\times10^{-15}$).
Its small-$m$ asymptote is $\pi^2/\ln(8/m)$ — which identifies
the corpus's recurring $\pi^2$ (the registration's gapless fit
coefficient $a = 9.860$, this campaign's blind-fit $A = 9.945$
and gapless $a = 9.936$) as **one coefficient** — the CTM
$\pi^2$; the modulus-scale-8 reading is receipted for the
*gapped* family ($B_c = 8.265 \approx 8$), while the gapless
fits share the coefficient with a geometry-dependent scale
(stated).  The value-decay clause of the tower is the closed
form's logarithmic decay, now anchored rather than fitted.

The blind two-parameter fit $A/\ln(B_c/m)$ on levels 0–2 only
is kept as an instrument demo: $A = 9.945$, $B_c = 8.265$ (the
finite-$m$ shadow of exact 8), out-of-sample level-3 prediction
1.9471 vs measured 1.9446 — 0.13% (K-PRED at 1%: did not fire;
the closed form supersedes it as the anchor).

## 2. The uniformity clause — the B* ladder

Two-stage detector — coarse bracket on $\{2,3,4,6,\ldots,256\}$,
integer-grid refinement inside the bracket, log-log
interpolation — a **declared refinement** of the registration's
grid-step 0.1%-plateau criterion (consistent where they
overlap), at three deficit targets:

```text
  target 3e-3: B* = 5.12 / 10.00 / 19.44 / 37.73
               ratios 1.953 / 1.944 / 1.941
               B* a_k (a_0 units): 5.12 / 5.00 / 4.86 / 4.72
  target 1e-3: B* = 6.40 / 12.52 / 24.44 / 47.68
               ratios 1.957 / 1.952 / 1.950
               B* a_k: 6.40 / 6.26 / 6.11 / 5.96
  target 3e-4: B* = 7.82 / 15.32 / 30.02 / 58.78
               ratios 1.960 / 1.959 / 1.958
               B* a_k: 7.82 / 7.66 / 7.50 / 7.35
  interpolation systematic (coarse vs refined): max 1.8%
```

**$B^*$ doubles per level at leading order — $B^*a_k$ uniform
in physical units** (K-BSTAR, window [1.8, 2.2], all targets:
did not fire); and the detector's log-subleading drift
**shrinks monotonically as the target tightens** (K-BSTAR2:
did not fire) — every ratio at 3e-4 sits closer to 2 than at
3e-3.  Honesty, registered: at fixed target the $B^*a_k$ drift
grows mildly along the tower, and three targets cannot *fully*
distinguish the detector's prefactor from a slow violation of
the clause; the direction receipt and the shrinking magnitude
support the detector reading, and the residual ambiguity is
registered, not hidden.

## 3. The gapless tower

```text
  half-chain eps_1: 1.2758 -> 1.1707 -> 1.0816 -> 1.0051
    (strictly decreasing; K-0LEV: did not fire)
  per-level end-block sweeps: monotone decreasing through
    B = N/4 at every level (K-0SAT: did not fire)
  THE DECISIVE RECEIPT (N = 4096): eps_1(B) = a/(ln B + b),
    a = 9.936 (~pi^2), b = 2.69, rms 0.03% of mean
    -> eps_1(B) -> 0: no positive plateau is consistent with
    the receipted 1/ln B form (fit-supported; K-0FIT)
```

Monotonicity alone cannot exclude a plateau — the gapped sweep
is also monotone into its plateau — so the per-level $1/\ln B$
fit carries the receipt: at the deepest level the gap collapses
with $B$ itself, with the same $\pi^2$ coefficient (the CTM
object again).  Fixed-$N$ caps and complement-symmetry
flattening disclosed as in the registration.

## 4. Ledger

```text
  K-EQUIV  free-level tower = stand-in (4e-15)  -> did not fire
  K-CTM    exact closed-form anchor (<= 1e-5)   -> did not fire
           (measured rel 9e-16..9e-15)
  K-PRED   blind-fit out-of-sample (0.13%)      -> did not fire
  K-BSTAR  B* doubling, 3 targets, [1.8, 2.2]   -> did not fire
  K-BSTAR2 detector drift shrinks w/ target     -> did not fire
  K-0LEV   gapless across-level collapse        -> did not fire
  K-0SAT   gapless per-level monotone sweeps    -> did not fire
  K-0FIT   gapless per-level 1/ln B fit         -> did not fire
  REGISTERED: the interacting/gauge tower clause (the wall);
  the detector-vs-violation residual ambiguity; the per-level
  infinite-volume clause (exact for the gapped tower by
  K-EQUIV; fit-supported for the gapless tower by K-0FIT)
  (ledger generated from computed flags in the canonical)
```

## 5. Verdict

At free level the tower clause **reduces, by the receipted
equivalence, to the mass-scaling law** — locating the
conjecture's nontrivial tower content exactly at the
interacting/gauge wall.  Within that scope the clause is
measured and anchored end to end: plateau values match the
exact corner-transfer closed form to machine precision (zero
parameters; the corpus's recurring $\pi^2$ identified as the
CTM coefficient with modulus scale 8); $B^*$ doubles per level
with the detector's subleading drift quantified, shrinking
under tighter targets, and the residual ambiguity registered;
the gapless tower forms no positive plateau at any level,
receipted by the per-level $1/\ln B$ fit (fit-supported, as
the ledger registers).  NOT
claimed: anything beyond free level; the wall; novelty of the
CTM form (cited, and deployed); full detector-vs-violation
distinction at the receipted targets.

## Receipts

```text
code/v6_p47_tower_receipt_campaign.py   the campaign
/tmp/v6_p47_campaign.out                canonical (BIT-IDENTICAL,
                                        ledger from flags)
equivalence: plateau 3.7e-15, deficit-profile 1.7e-15;
plateaus 3.283767/2.673697/2.251971/
1.944623 vs closed form (rel 3.8e-15/6.3e-15/8.9e-16/8.7e-15);
asymptotes pi^2/ln(8/m) = 3.2946/2.6755/2.2523/1.9447; blind
fit A = 9.9452, Bc = 8.265, prediction 1.9471 vs 1.9446
(0.13%); B* ladders at 3 targets with ratios as tabulated;
interpolation systematic max 1.8%; gapless 1.2758/1.1707/
1.0816/1.0051; per-level fit a = 9.936, b = 2.69, rms 0.03%.
Literature: Baxter (corner transfer matrices); Peschel
(exact entanglement Hamiltonians; the eps_1 = pi K'/K class);
Calabrese-Lefevre; the modular-gap registration (P46) and its
instrument receipts; P39 (the tower object); P45 (the modular
instrument lineage).
```
