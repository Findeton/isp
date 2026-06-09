"""
SCRATCH (not paper 2): hunt for the invariant law that makes the four branch-A roles ONE fact.

roles: T_record (likelihood contrast), T_source (stress-energy deletion), T_causal (causal incidence),
T_antichain (spatial density). Branch A needs the role-Gram J = Cov(T_i,T_j|click) to be FIXED by the event
law, i.e. the source row must not be free. §5.25/§5.27 obstruction: an independent source amplitude moves
d_source = (Ju)_source and hence beta = (4 gamma d_source/5)^(1/6).

Candidate law (after the guessing chain): the ONE FACT is the event's relative entropy / modular energy
w_e (record surprisal). The first law (Jacobson/entanglement-equilibrium) forces
    T_source(e) = T_e * w_e         (Clausius: energy = temperature * entropy),
    T_causal(e) = a_C * w_e         (causal info per relation, geometric ratio),
    T_antichain(e) = a_A * w_e       (entropy density, geometric ratio = 1/volume),
with T_e the GEOMETRIC (Unruh/modular) temperature -- not a free matter parameter. Then all four roles are
COLLINEAR in w_e: the role-Gram is rank-1, d_source = T_e * d_record is fixed, beta is determined.

Test: reproduce the obstruction (free source amplitude moves beta), then show the modular law removes it.
"""
import numpy as np
rng = np.random.default_rng(0)

N = 4000
w = rng.lognormal(mean=0.0, sigma=0.6, size=N)        # per-event relative entropy (record surprisal), >0
a_C, a_A = 0.8, 0.6                                    # geometric ratios (causal info, antichain density)
T_geom = 0.5                                           # GEOMETRIC modular/Unruh temperature (energy per nat)
noise = lambda s: rng.normal(0, s, N)                 # small intrinsic spread, same actual event

# role statistics over events (the columns whose covariance is the role-Gram J)
rec  = w + noise(0.02)
caus = a_C*w + noise(0.02)
anti = a_A*w + noise(0.02)

gamma = 7/48.0
u = np.array([0.5, 0.5, 0.5, 0.5])                    # common deletion direction
def beta_from(J):
    d = J @ u
    d_source = d[1]
    return (4*gamma*max(d_source, 0)/5)**(1/6), d_source

def gram(source_col):
    M = np.vstack([rec, source_col, caus, anti])      # rows = roles
    return np.cov(M)

print("="*84)
print("Branch-A unification test: does the modular/first-law source kill the free-amplitude obstruction?")
print("="*84)

# ---- (B) FREE source amplitude: reproduce the §5.25/§5.27 obstruction ----
print("\n(B) free source amplitude a_src (independent of the record) -> beta should MOVE:")
print(f"   {'a_src':>7} {'d_source':>10} {'beta':>10} {'Gram rank(>1e-3)':>18}")
betas_free = []
for a_src in [0.2, 0.5, 0.8, 1.1, 1.4]:
    v = rng.lognormal(0.0, 0.6, N)                    # INDEPENDENT source response (free amplitude)
    src = a_src * v + noise(0.02)
    J = gram(src)
    b, ds = beta_from(J)
    rk = int(np.sum(np.linalg.svd(J, compute_uv=False) > 1e-3*np.trace(J)))
    betas_free.append(b)
    print(f"   {a_src:>7.2f} {ds:>10.4f} {b:>10.4f} {rk:>18}")
print(f"   beta span (free) = {max(betas_free)-min(betas_free):.4f}   <- free parameter (branch B)")

# ---- (A) MODULAR law: source = T_geom * w (Clausius, geometric temperature) ----
print("\n(A) modular/first-law source  T_source = T_geom * w  (T_geom geometric, NOT free):")
print(f"   {'(ignored a_src)':>15} {'d_source':>10} {'beta':>10} {'Gram rank(>1e-3)':>18}")
betas_mod = []
for a_src in [0.2, 0.5, 0.8, 1.1, 1.4]:               # vary what WAS free; the law ignores it
    src = T_geom * w + noise(0.02)                    # forced by the first law; a_src plays no role
    J = gram(src)
    b, ds = beta_from(J)
    rk = int(np.sum(np.linalg.svd(J, compute_uv=False) > 1e-3*np.trace(J)))
    betas_mod.append(b)
    print(f"   {a_src:>15.2f} {ds:>10.4f} {b:>10.4f} {rk:>18}")
print(f"   beta span (modular) = {max(betas_mod)-min(betas_mod):.6f}   <- FIXED by geometry (branch A)")

# ---- collinearity signature: under the modular law the four roles are one direction ----
J_mod = gram(T_geom*w + noise(0.02))
sv = np.linalg.svd(J_mod, compute_uv=False)
print(f"\n   role-Gram singular values (modular): {np.array2string(sv, precision=4)}")
print(f"   ratio sv[1]/sv[0] = {sv[1]/sv[0]:.4f}  (->0 means rank-1: all four roles are ONE fact)")

print("\n" + "="*84); print("READING"); print("="*84)
print("- Free source amplitude => Gram rank>1, d_source tracks the free amplitude, beta moves (branch B).")
print("- Modular/first-law source T_source=T_geom*w => Gram collapses toward rank-1 (four roles collinear in")
print("  the entropy w), d_source = T_geom*d_record is FIXED, beta is determined and ignores the would-be free")
print("  amplitude. The closing input is that T_geom (and the antichain volume) are GEOMETRIC, not matter-free.")
print("- Physically: the one fact is the event's relative entropy / modular energy; the first law")
print("  delta Q = T delta S (Jacobson / entanglement equilibrium) makes record=source=causal=antichain one")
print("  quantity, with temperature and discreteness-volume as the (geometric) unit bridges.")
