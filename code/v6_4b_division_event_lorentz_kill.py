"""
v6 §4B KILL-TEST: do ISP's division events Poisson-sprinkle (Lorentz-invariant), or carry a preferred frame?

§4B reduced the whole geometry-side feasibility to ONE condition: the division events must be a Poisson
sprinkle w.r.t. the Lorentz-invariant 4-volume (Bombelli-Henson-Sorkin: that is the unique Lorentz-invariant
discrete point process). The honest subtlety: a UNIFORM-rate Poisson process is ALREADY Lorentz-invariant
(Lebesgue measure is boost-invariant), so a crude "is the marginal Poisson" check would wrongly pass naive
GRW. The genuine kill-criterion (BHS) is whether a PREFERRED FRAME can be RECONSTRUCTED from the events.

PART 1 -- frame-reconstruction estimator (BHS operationalized). Scan trial boosts beta; for each, bin events
by the trial-frame time t' and compute the Fano factor (Var/Mean of slab counts) of the t'-marginal. Poisson
=> Fano ~ 1 in EVERY frame (flat in beta, no preferred frame). A frame-imprinted process (temporally
synchronized / clocked) => Fano peaks at its rest frame (smears under boost) => preferred frame RECOVERED.
  Processes: (i) Poisson 4-volume [PASS expected]; (ii) synchronized shells (flashes on near-constant-t
  slices = a global clock) [KILL]; (iii) regular-clocked-per-cell (lattice in time) [KILL].

PART 2 -- the rate rule along a worldline (= the §5.7 scalar-rate condition as a Lorentz statement). Between
two FIXED spacetime events A,B on an accelerated worldline, the expected number of division events is
frame-invariant IFF the rate is per PROPER time (scalar). A per-COORDINATE-time rate names a frame and gives
a frame-dependent count. This is exactly which ISP rule survives.

VERDICT ties §4B and §5 together: the division events survive IFF Poisson-per-proper-4-volume = scalar rate;
the naive global-time ISP default is killed; whether the full interacting reconstruction delivers the scalar
rate is the one shared open residue (§10).
"""
import numpy as np
rng = np.random.default_rng(1)

def boost(t, x, beta):
    g = 1/np.sqrt(1-beta**2); return g*(t - beta*x), g*(x - beta*t)

T0, L0, Nev, Delta = 16.0, 16.0, 15000, 1.0
half, w = 4.5, 0.4                                          # analysis half-window & t'-slab width
def fano_tmarginal(t, x, beta):
    tp, xp = boost(t, x, beta)
    m = (np.abs(tp) < half) & (np.abs(xp) < half)          # central window fully inside the box for all beta
    tp = tp[m]
    if len(tp) < 100: return np.nan
    bins = np.arange(-half, half+w, w); c, _ = np.histogram(tp, bins=bins)
    return c.var()/c.mean() if c.mean() > 0 else np.nan

def make(kind):                                            # one realization of a candidate process
    if kind == "pois":   return (rng.uniform(-T0, T0, Nev), rng.uniform(-L0, L0, Nev))
    if kind == "shell":  return (rng.integers(-15, 16, Nev)*Delta + rng.normal(0, 0.05, Nev),
                                 rng.uniform(-L0, L0, Nev))
    if kind == "clock":  return (rng.integers(-15, 16, Nev)*Delta + rng.normal(0, 0.05, Nev),
                                 rng.integers(-15, 16, Nev)*Delta + rng.normal(0, 0.05, Nev))

betas = np.linspace(0.0, 0.7, 15)
nreal = 10
print("="*88)
print("PART 1: can a preferred frame be reconstructed?  Fano(t'-marginal) vs trial boost beta")
print(f"        (mean over {nreal} realizations; Poisson Fano ~ 1 in every frame = no preferred frame, BHS)")
print("="*88)
print(f"   {'process':<26} {'Fano(b=0)':>10} {'Fano(b=0.7)':>12} {'beta*':>7} {'signal S':>9}  verdict")
def analyze(name, kind, null=None):
    F = np.nanmean([[fano_tmarginal(*make(kind), b) for b in betas] for _ in range(nreal)], axis=0)
    bstar = betas[np.nanargmax(F)]; S = np.nanmax(F) - np.nanmedian(F)   # excess peak above the flat baseline
    if null is None:
        verdict = f"NULL (Poisson) S0={S:.2f}"
    else:
        verdict = "PASS (no preferred frame)" if S < 4*null else f"KILL (preferred frame @ beta~{bstar:.2f})"
    print(f"   {name:<26} {F[0]:>10.2f} {F[-1]:>12.2f} {bstar:>7.2f} {S:>9.2f}  {verdict}")
    return S
S_pois  = analyze("(i) Poisson 4-volume",     "pois")
S_shell = analyze("(ii) synchronized shells", "shell", null=S_pois)
S_clock = analyze("(iii) regular-clocked",    "clock", null=S_pois)
print(f"   [signal S = peak Fano - baseline Fano; Poisson null S0={S_pois:.2f} (finite-N noise); KILL if S >> S0]")

# ---------- PART 2: rate rule along an accelerated worldline ----------
print("\n" + "="*86)
print("PART 2: rate rule on an accelerated worldline -- scalar (proper-time) vs coordinate-time")
print("="*86)
a = 0.5                                                     # proper acceleration; worldline x=cosh(a tau)/a, t=sinh(a tau)/a
tauA, tauB = -2.0, 2.0
lam = 3.0
# expected counts between the SAME two spacetime events A,B, computed in two frames
def worldline(tau): return np.sinh(a*tau)/a, np.cosh(a*tau)/a   # (t, x)
tA, xA = worldline(tauA); tB, xB = worldline(tauB)
# scalar (proper-time) rule: N = lam * (tauB - tauA), manifestly frame-independent
N_scalar = lam*(tauB - tauA)
# coordinate-time rule: N = lam * (t_B^frame - t_A^frame); compute in rest frame and a boosted frame
for beta in [0.0, 0.5]:
    tAf, _ = boost(tA, xA, beta); tBf, _ = boost(tB, xB, beta)
    N_coord = lam*(tBf - tAf)
    tag = "rest frame" if beta == 0 else f"boosted beta={beta}"
    print(f"   {tag:<18}:  scalar(proper-time) N = {N_scalar:6.3f}   |   coordinate-time N = {N_coord:6.3f}")
print("   => scalar rule: SAME count in every frame (Lorentz-invariant). coordinate rule: frame-dependent (KILL).")

print("\n" + "="*86); print("VERDICT (§4B kill-test)"); print("="*86)
print(f"- The frame-reconstruction estimator PASSES Poisson (signal S={S_pois:.2f}, the finite-N null, no preferred")
print(f"  frame) and KILLS the clocked/synchronized processes (S={S_shell:.1f}, {S_clock:.1f} >> null -- rest frame recovered).")
print("- Part 2: only a per-PROPER-TIME (scalar) rate gives a frame-invariant division-event count along a")
print("  worldline; a per-coordinate-time rate is frame-dependent.")
print("- CONCLUSION: ISP's division events survive §4B IFF they are Poisson-per-proper-4-volume = the SCALAR")
print("  rate of §5.7-5.8. The naive global-time ISP default (synchronized/clocked) is KILLED. So §4B and the")
print("  rate leg (§5) are the SAME condition; whether the full INTERACTING reconstruction delivers the scalar")
print("  rate is the one shared open residue (§10) -- not closed here, but the kill-criterion is now operational.")
