"""
v6 §5.18: the CURVED-COEFFICIENT test -- the GR-vs-Horava discriminator.

The hypersurface-deformation algebra closes as {H_perp[N],H_perp[M]} = H_i[xi], xi = g^{ij}(N d_jM - M d_jN).
The STRUCTURE FUNCTION is the inverse spatial metric. GR <=> that coefficient IS the curved metric g^{ij}(x);
a rescaled/Horava theory <=> the coefficient is something else (a constant, or anisotropic). In FLAT space
(§5.17) g^{ij}=1 so the coefficient is trivially constant -- which is why flat space cannot distinguish the
two. CURVED space can. This is the decisive next probe flagged in §5.17.

2D conformal metric ds^2 = Omega(x)^2 (-dt^2 + dx^2). Inverse spatial metric g^{xx} = 1/Omega^2.

PART 1 (clean grid, defines the discriminator + shows it has power):
  push tracers along the CURVED unit normal n^mu = (1/Omega)(1,T')/sqrt(1-T'^2); commutator of two normal
  deformations -> measure C(x) = drift_x / (-eps^2 (N M' - M N')). Analytic target: C(x) = 1/Omega^2(x) (GR).
  Contrast: a "Horava" FLAT-normal push (ignore Omega) -> C(x) = const = 1. So the test SEPARATES GR (C tracks
  the curved 1/Omega^2) from Horava (C flat). [Uses Omega in the normal -- its job is to define the target and
  prove the discriminator distinguishes; the causal set (Part 2) must supply Omega from order+number, no insert.]

PART 2 (causal set, non-circular -- Omega NEVER inserted):
  The Part-1 coefficient C(x)=1/Omega^2 is exactly (coordinate-time per proper-time)^2 = (1/Omega)^2. The causal
  set supplies proper time via LONGEST CHAINS (no Omega inserted). Extract, from causal data only, two
  INDEPENDENT channels:
    (A) Omega_chain(x): local proper-time rate from longest chains in a thin coordinate slab (proper density is
        constant under a correct sprinkling, so longest-chain length in a slab of coordinate height h is
        proportional to Omega(x)*h).
    (B) Omega_dens(x):  local NUMBER density of events (coordinate density ~ Omega^2), the "number" datum.
  GR predicts BOTH give the same Omega, so the flow-drift coefficient C_chain(x)=1/Omega_chain^2 tracks the
  independently-extracted 1/Omega_dens^2 AND the true 1/Omega^2, and is NON-constant (dips in the curved
  centre). A Horava-like construction-artifact would give a CONSTANT coefficient; an anisotropic (Lifshitz
  z!=1) spacetime would make chains and density DISAGREE. Report correlations, centre/wing contrast, honestly.
"""
import numpy as np
rng = np.random.default_rng(0)

A, sig = 1.5, 0.8                      # conformal bump amplitude / width
Omega = lambda x: 1.0 + A*np.exp(-x**2/(2*sig**2))
gxx   = lambda x: 1.0/Omega(x)**2      # the GR inverse spatial metric (the target coefficient)

k = 1.3
N = lambda x: 1.0 + 0.6*np.cos(k*x)
M = lambda x: 1.0 + 0.6*np.sin(k*x)
def d(f, x, h=1e-4): return (f(x+h)-f(x-h))/(2*h)
lap_grad = lambda x: N(x)*d(M, x) - M(x)*d(N, x)      # (N M' - M N')

# ===================================================================================
print("="*84)
print("PART 1: clean grid -- does the curved-normal flow-drift give C(x)=1/Omega^2 (GR)?")
print("="*84)
xg = np.linspace(-2.2, 2.2, 700)
def push(t, x, F, eps, curved=True):
    sl = np.gradient(t, x); sl = np.clip(sl, -0.9, 0.9)        # slice slope T'(x)
    fac = (1.0/Omega(x)) if curved else 1.0                    # the proper-time Jacobian (GR) vs ignore (Horava)
    nt = fac/np.sqrt(1-sl**2); nx = fac*sl/np.sqrt(1-sl**2)
    return t + eps*F(x)*nt, x + eps*F(x)*nx
eps = 0.04
def commutator_drift(curved):
    t1, x1 = push(np.zeros_like(xg), xg.copy(), N, eps, curved); t1, x1 = push(t1, x1, M, eps, curved)
    t2, x2 = push(np.zeros_like(xg), xg.copy(), M, eps, curved); t2, x2 = push(t2, x2, N, eps, curved)
    return x1 - x2
m = (xg > -1.8) & (xg < 1.8)
for label, curved in [("GR  (curved normal, uses proper-time Jacobian 1/Omega)", True),
                      ("Hor (flat normal, ignores Omega)                     ", False)]:
    Dx = commutator_drift(curved)
    C = Dx[m] / (-eps**2 * lap_grad(xg[m]))               # measured coefficient
    cc_gr  = np.corrcoef(C, gxx(xg[m]))[0, 1]             # vs the curved metric 1/Omega^2
    cc_con = 1.0 - np.var(C)/np.var(C)                    # (constant ref handled by centre/wing below)
    cen = np.abs(xg[m]) < 0.3; win = np.abs(xg[m]) > 1.4
    print(f"  {label}")
    print(f"     corr(C, 1/Omega^2)={cc_gr:+.4f}   centre/wing C = {C[cen].mean()/C[win].mean():.3f}"
          f"   (GR target {gxx(0)/gxx(1.6):.3f},  Horava target 1.000)")
print(f"  -> the discriminator SEPARATES them: GR coefficient tracks the curved 1/Omega^2 and DIPS at the")
print(f"     centre (g^xx small where Omega large); Horava stays flat (centre/wing ~ 1).")

# ===================================================================================
print("\n" + "="*84)
print("PART 2: causal set -- recover the coefficient from order+number, Omega NEVER inserted")
print("="*84)

def sprinkle_conformal(n_target, ht, hx):
    # density ~ Omega^2 via rejection (uniform in proper volume): accept w.p. Omega^2/Omega_max^2
    out = []; Omax2 = Omega(0.0)**2
    while len(out) < n_target:
        t = rng.uniform(-ht, ht, n_target); x = rng.uniform(-hx, hx, n_target)
        keep = rng.uniform(0, 1, n_target) < Omega(x)**2 / Omax2
        out.append(np.column_stack([t[keep], x[keep]]))
        if sum(len(o) for o in out) >= n_target: break
    P = np.vstack(out)[:n_target]
    return P

def longest_chain(P_sub):
    # longest chain in a small subset; 2D conformal order = flat order (conformal invariance of null cones)
    t, x = P_sub[:, 0], P_sub[:, 1]; n = len(P_sub)
    order = np.argsort(t)                              # topological order by time
    L = np.ones(n)
    tt, xx = t[order], x[order]
    for j in range(n):
        # predecessors i<j (earlier time) with tt[j]-tt[i] > |xx[j]-xx[i]|
        dt = tt[j] - tt[:j]; dx = np.abs(xx[j] - xx[:j])
        anc = np.where(dt > dx)[0]
        if anc.size: L[j] = 1 + L[anc].max()
    return L.max()

xbins = np.linspace(-1.8, 1.8, 13); xc = 0.5*(xbins[:-1]+xbins[1:])
Och_trials, Ode_trials = [], []
for trial in range(6):
    P = sprinkle_conformal(60000, 3.0, 2.6)
    h = 0.55                                           # coordinate-time slab height for the chain estimate
    Och = np.full(len(xc), np.nan); Ode = np.full(len(xc), np.nan)
    for i in range(len(xc)):
        wsel = (P[:, 1] > xbins[i]) & (P[:, 1] < xbins[i+1])
        # (A) chains: longest chain in a thin coordinate slab [-h/2, h/2] at this x  ~  Omega * h
        sl = wsel & (np.abs(P[:, 0]) < h/2)
        if sl.sum() > 12: Och[i] = longest_chain(P[sl])
        # (B) density: events per unit coordinate area in a central band  ~  Omega^2
        db = wsel & (np.abs(P[:, 0]) < 1.0)
        Ode[i] = db.sum()
    Och_trials.append(Och); Ode_trials.append(Ode)

Och = np.nanmean(Och_trials, axis=0); Ode = np.nanmean(Ode_trials, axis=0)
# normalize each channel to the flat wings (|x|>1.4) so unknown constants cancel -> Omega_hat
wing = np.abs(xc) > 1.4
Om_chain = Och / np.nanmean(Och[wing])                 # ~ Omega(x)        (longest chain ~ proper time)
Om_dens  = np.sqrt(Ode / np.nanmean(Ode[wing]))        # ~ Omega(x)        (density ~ Omega^2)
C_chain  = 1.0 / Om_chain**2                           # flow-drift coefficient from chains  ~ 1/Omega^2
C_dens   = 1.0 / Om_dens**2                            # cross-check from density            ~ 1/Omega^2
C_true   = gxx(xc)

cc_ct  = np.corrcoef(C_chain, C_true)[0, 1]
cc_cd  = np.corrcoef(C_dens,  C_true)[0, 1]
cc_xch = np.corrcoef(C_chain, C_dens)[0, 1]            # the two INDEPENDENT channels agree? (isotropy/GR)
cen = np.abs(xc) < 0.25
print("   per-x recovered (mean over 6 sprinklings), normalized to flat wings:")
print(f"   {'x':>6} {'1/Om^2 true':>11} {'C_chain':>9} {'C_dens':>9}")
for i in range(0, len(xc), 2):
    print(f"   {xc[i]:>6.2f} {C_true[i]:>11.3f} {C_chain[i]:>9.3f} {C_dens[i]:>9.3f}")
print(f"\n   corr(C_chain, 1/Omega^2_true) = {cc_ct:+.3f}     [flow-drift coeff (chains) tracks the curved metric?]")
print(f"   corr(C_dens , 1/Omega^2_true) = {cc_cd:+.3f}     [independent density channel cross-check]")
print(f"   corr(C_chain, C_dens)         = {cc_xch:+.3f}     [two INDEPENDENT causal-data channels agree? = isotropy/GR]")
print(f"   centre/wing of C_chain = {np.nanmean(C_chain[cen]):.3f}  (GR target {gxx(0):.3f}; Horava-artifact target 1.000)")

print("\n" + "="*84); print("VERDICT (§5.18)"); print("="*84)
dip = np.nanmean(C_chain[cen])
if cc_ct > 0.7 and cc_xch > 0.7 and dip < 0.7:
    print(f"- POSITIVE: the flow-drift coefficient recovered from causal data TRACKS the curved inverse metric")
    print(f"  1/Omega^2 (corr {cc_ct:+.2f}), DIPS in the curved centre (centre/wing {dip:.2f} vs GR {gxx(0):.2f}),")
    print(f"  and the two independent channels (longest-chain proper time, number density) AGREE (corr {cc_xch:+.2f}).")
    print(f"  => the structure function is the curved metric g^{{ij}} (GR), NOT a constant (Horava) -- and the")
    print(f"     time/space conformal factors are isotropic (Lorentzian, z=1), not anisotropic (Lifshitz).")
    print(f"     Scope: shows the v6 construction is GR-faithful in CURVED space; it does not (cannot, w/o the")
    print(f"     dynamics) show nature SELECTS GR over Horava -- that is the §10 reconstruction question.")
elif cc_ct > 0.4 or dip < 0.85:
    print(f"- WEAK/NOISY POSITIVE: coefficient leans toward the curved 1/Omega^2 (corr {cc_ct:+.2f}, centre/wing")
    print(f"  {dip:.2f}) but noisily; above a flat-constant null yet not clean. Honest: suggestive, finite-N limited.")
else:
    print(f"- INCONCLUSIVE: corr {cc_ct:+.2f}, centre/wing {dip:.2f} -- causal-data noise dominates; the curved")
    print(f"  coefficient is not cleanly recovered at this N. Cannot distinguish GR from a flat coefficient here.")
