"""
Paper 1 v6, the DECISIVE calculation (layer 1): is the division-event point process Lorentz-invariant?

Reduction (the real content): a record/flash point process is Lorentz-invariant IFF its intensity is a
Lorentz SCALAR -- a rate per invariant proper-time / 4-volume -- not a rate "per slice" (per coordinate
time in a preferred frame). Non-relativistic ISP defines division events as special TIMES in a frame
(a per-slice notion), so the naive relativistic lift is frame-dependent; the covariant fix (= Tumulka's
relativistic-GRW flash recipe) is a proper-time rate.

We make this quantitative with the one frame-invariant diagnostic available: FLASHES PER UNIT PROPER TIME
of a worldline. If the generating rule is Lorentz-invariant, all frames agree on it; if it is per-slice,
different frames' rules give different physical flash sets.

Worldline moving at v in frame S; second frame S' boosted by beta. We compare, for each rule,
flashes-per-proper-time generated in S vs generated natively in S' (same physics, different frame).
"""
import numpy as np
rng = np.random.default_rng(3)

def boost_1d(t, x, beta):
    g = 1/np.sqrt(1-beta**2)
    return g*(t - beta*x), g*(x - beta*t)

def vel_add(v, beta):           # worldline velocity (v in S) as seen in S' (S' moves at beta in S)
    return (v - beta)/(1 - v*beta)

v, beta, lam = 0.5, 0.6, 1.0
g_v  = 1/np.sqrt(1-v**2)
vp   = vel_add(v, beta)
g_vp = 1/np.sqrt(1-vp**2)
N = 400_000

print("="*76)
print("DECISIVE TEST: is the division-event (flash) rate Lorentz-invariant?")
print("="*76)
print(f"worldline v={v} in S (gamma={g_v:.4f});  boost beta={beta} -> v'={vp:+.4f} in S' (gamma={g_vp:.4f})")
print(f"flash rate parameter lam={lam}\n")

# ---- SCALAR rule: Poisson interarrivals in PROPER TIME (the covariant / rGRW recipe) ----
tau = np.cumsum(rng.exponential(1/lam, N))           # proper-time stamps
t_S = g_v*tau; x_S = v*g_v*tau                        # worldline coords in S
tpr, xpr = boost_1d(t_S, x_S, beta)                  # boost the SAME physical flashes to S'
dtau_Sp = np.sqrt(np.maximum(np.diff(tpr)**2 - np.diff(xpr)**2, 0))   # proper time from S' coords
ppt_scalar_S  = N/tau[-1]
ppt_scalar_Sp = (N-1)/np.sum(dtau_Sp)
print("SCALAR (proper-time) rule:")
print(f"   flashes / proper-time  in S            = {ppt_scalar_S:.4f}")
print(f"   flashes / proper-time  boosted into S' = {ppt_scalar_Sp:.4f}")
print(f"   -> frame ratio = {ppt_scalar_S/ppt_scalar_Sp:.4f}   (1.000 = Lorentz-invariant)\n")

# ---- PER-SLICE rule: Poisson interarrivals in COORDINATE TIME of the generating frame ----
def per_slice(vel):
    t = np.cumsum(rng.exponential(1/lam, N))         # rate lam per coordinate time
    g = 1/np.sqrt(1-vel**2)
    return N/(t[-1]/g)                               # flashes / proper time = lam*gamma
ppt_ps_S  = per_slice(v)                              # rule applied in S
ppt_ps_Sp = per_slice(vp)                             # SAME rule applied natively in S'
print("PER-SLICE (coordinate-time) rule:")
print(f"   flashes / proper-time, rule applied in S  = {ppt_ps_S:.4f}   (= lam*gamma_v  = {lam*g_v:.4f})")
print(f"   flashes / proper-time, rule applied in S' = {ppt_ps_Sp:.4f}   (= lam*gamma_v' = {lam*g_vp:.4f})")
print(f"   -> frame ratio = {ppt_ps_S/ppt_ps_Sp:.4f}   (!= 1 => FRAME-DEPENDENT: breaks Lorentz)\n")

print("="*76)
print("VERDICT")
print("="*76)
print("- SCALAR (proper-time) rate  : frame ratio ~ 1.00  -> the SAME physical flash set in all frames")
print("                               => Lorentz-invariant point process; valid causal-set substrate.")
print(f"- PER-SLICE (coord-time) rate : frame ratio ~ {ppt_ps_S/ppt_ps_Sp:.2f}  -> different frames give different")
print("                               flash sets => preferred frame; breaks Lorentz.")
print("- ISP's non-relativistic division events are per-slice (special times in a frame). So the test")
print("  the relativistic-ISP construction must pass is EXACTLY: does it promote the division rate to a")
print("  Lorentz scalar (per proper 4-volume)? rGRW shows this is achievable for free systems; the")
print("  interacting derivation is the open step (= the same residue as the QFT reconstruction).")
print("- Note: the scalar rule = Poisson-in-4-volume, so the dimension-recovery of the §4A probe")
print("  (d=2->2.01, 3->2.95, 4->4.04) applies directly: scalar-rate division events ARE a valid geometry.")
