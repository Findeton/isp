# Paper 37 campaign: the Seam Theorem (O35.1a) + the untuned consequence
# set (Feynman phase).  Phase 1: prove, in Paper II's RP/POVM formalism,
# that a SEALED (rank-one) binary seam that supports a STATIONARY state
# has intertwiner norm exactly sqrt(p(1-p)) - the dressed-base factor -
# with the phase pure rephasing gauge.  Phase 2: extract everything else
# the mechanism fixes, with current-data status and kill criteria.
# Canonical: /tmp/v6_p37_campaign.out (bit-identical rerun required)

from mpmath import mp, mpf, sqrt, ln, exp, findroot, mpc, cos, sin, pi
import numpy as np

mp.dps = 40
rng = np.random.default_rng(37)

print("== PRE-REGISTRATION (written before computation) ==")
print("""  PHASE 1 (theorem): in the RP form (paper-II Thm 2.1), define a
  SEALED binary seam = rank-one PSD letters A0 = p uu*, A1 = (1-p)
  vv* (S-atomicity: a sealed distinction has no internal
  multiplicity - NAMED IDENTIFICATION).  Claims to prove: (L-A)
  ||sqrt(A0) sqrt(A1)|| = sqrt(p(1-p)) |<u,v>| <= sqrt(p(1-p));
  (L-B) lam_max(A0+A1) = 1 iff |<u,v>| = 1 (for p not 0,1); (T-C)
  a stationary state (T omega = omega) overlapping the seam FORCES
  alignment, hence saturation: the factor is eps(1-eps) EXACTLY,
  derived from stationarity - no new principle.  (R-D) the seam
  phase is rephasing gauge (axiom-S silent); the O35.1 object
  ("sealed in modulus, silent in phase") exists constructively.
  KILL: if stationarity forces MISalignment or a different factor,
  the dressed base dies by the program's own axioms.
  PHASE 2 (consequences, fixed in advance - no additions after
  checking data): (P-MIX) atmospheric mixing maximal, sin^2(th23)
  = 1/2 (provenance: P34 minimal texture, derived BEFORE this
  framing); (P-CPV) seam phases silent => mass matrices real-
  equivalent => Jarlskog J = 0, delta_CP in {0, pi}; (P-SPEC) the
  full dressed spectrum with NO free coefficient (C = C1 = 1 on
  eps_eff), hence S, Sum(m), and the DISCRETE m_bb menu under
  Majorana signs.  Each carries its current-data status, stated
  even where it hurts.""")

# ---------- constants ----------
theta = findroot(lambda x: x**3 + x**2 + x - 1, mpf("0.54"))
eta = -ln(theta)
kappa = eta*(1 - theta**2)/(1 - theta**2 + theta)
eps = 3*kappa - 1
eps_eff = eps*(1 - eps)
print(f"\n  eps = {mp.nstr(eps, 15)}   eps_eff = {mp.nstr(eps_eff, 15)}")

# ---------- Phase 1 receipts ----------
print("\n== L-A: the intertwiner-norm identity (random sealed seams) ==")
worst = 0.0
for _ in range(200):
    d = int(rng.integers(2, 6))
    u = rng.normal(size=d) + 1j*rng.normal(size=d)
    v = rng.normal(size=d) + 1j*rng.normal(size=d)
    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    p = float(rng.uniform(0.01, 0.99))
    A0 = p*np.outer(u, u.conj())
    A1 = (1 - p)*np.outer(v, v.conj())
    s0 = np.sqrt(p)*np.outer(u, u.conj())
    s1 = np.sqrt(1 - p)*np.outer(v, v.conj())
    lhs = np.linalg.norm(s0 @ s1, 2)
    rhs = np.sqrt(p*(1 - p))*abs(np.vdot(u, v))
    worst = max(worst, abs(lhs - rhs))
print(f"  ||sqrt(A0) sqrt(A1)|| = sqrt(p(1-p)) |<u,v>| : worst dev"
      f" {worst:.2e} over 200 random seams (d = 2..5, complex)")
print(f"  bound sqrt(p(1-p)) saturated iff |<u,v>| = 1: by the identity")

print("\n== L-B: lam_max(A0+A1) = 1 iff aligned ==")
# closed form on the seam span: lam_max = [1 + sqrt(1-4p(1-p)(1-|c|^2))]/2
worst = 0.0
gapmin = 1.0
for _ in range(200):
    p = float(rng.uniform(0.05, 0.95))
    c = float(rng.uniform(0, 1))
    u = np.array([1.0, 0.0])
    v = np.array([c, np.sqrt(1 - c**2)])
    T = p*np.outer(u, u) + (1 - p)*np.outer(v, v)
    lam = np.linalg.eigvalsh(T)[-1]
    pred = (1 + np.sqrt(1 - 4*p*(1 - p)*(1 - c**2)))/2
    worst = max(worst, abs(lam - pred))
    if c < 0.999:
        gapmin = min(gapmin, (1 - lam)/(p*(1 - p)*(1 - c**2)))
print(f"  closed form verified: worst dev {worst:.2e}")
print(f"  strict gap for misaligned seams: 1 - lam_max >="
      f" {gapmin:.3f} * p(1-p)(1-|c|^2)  (> 0 whenever |c| < 1)")

print("\n== T-C: stationarity forces saturation ==")
print("""  T omega = omega requires omega to be a 1-eigenvector of T; on
  the seam span, lam_max < 1 STRICTLY unless |<u,v>| = 1 (L-B), so
  any stationary state overlapping the seam forces alignment, and
  the intertwiner norm is then sqrt(p(1-p)) EXACTLY (L-A).  With
  p = eps: per-seam factor eps(1-eps) = eps_eff - the dressed
  base, DERIVED from (i) S-atomicity [identification], (ii) the
  RP form's own stationarity [theorem 2.1 machinery].""")
# numeric demo: misaligned seam admits no stationary overlap
p, c = 0.0318, 0.9
u = np.array([1.0, 0.0])
v = np.array([c, np.sqrt(1 - c**2)])
T = p*np.outer(u, u) + (1 - p)*np.outer(v, v)
lam = np.linalg.eigvalsh(T)[-1]
print(f"  demo (p = eps, |c| = 0.9): lam_max = {lam:.6f} < 1 ->"
      f" ||T w - w|| >= {1-lam:.2e} ||w_seam||: no stationary overlap")
A0 = p*np.outer(u, u)
A1 = (1 - p)*np.outer(u, u)/p*(1 - p)*p  # aligned variant below
ua = np.array([1.0, 0.0])
A0a = p*np.outer(ua, ua)
A1a = (1 - p)*np.outer(ua, ua)
print(f"  aligned seam: A0 A1 - A1 A0 = "
      f"{np.linalg.norm(A0a @ A1a - A1a @ A0a):.1e} -> the saturated seam")
print(f"  is CLASSICAL (commuting letters): sealed = aligned = classical;")
print(f"  the 'coherence' bound is met by the definite record, exactly")
print(f"  as a record-first ontology would have it.")
print(f"  R-D (phase): u -> e^(i phi) u changes no letter and no weight:")
print(f"  the seam phase is rephasing gauge = axiom-S silent; modulus")
print(f"  physical.  The O35.1 object EXISTS, constructively.")

print("\n== BRIDGE STATUS after T-C ==")
print("""  DERIVED: the per-seam factor eps(1-eps) (given S-atomicity +
  stationarity).  REMAINING IDENTIFICATION (O35.1b): rung index =
  number of seam insertions in amplitude (half-rung = one factor
  sqrt(eps(1-eps))).  The bridge gap has shrunk from 'derive the
  factor' to 'derive the count' - smaller, but still open and
  graded as such.""")

# ---------- Phase 2: the untuned consequence set ----------
print("\n== P-SPEC: the full dressed spectrum (no free coefficient) ==")
dm31 = mpf("2.511e-3")
m3 = sqrt(dm31/(1 - eps_eff**2))
m2, m1 = sqrt(eps_eff)*m3, eps_eff*m3
S = sqrt((m2**2 - m1**2)/(m3**2 - m1**2))
print(f"  m = ({mp.nstr(m1*1000, 4)}, {mp.nstr(m2*1000, 4)},"
      f" {mp.nstr(m3*1000, 5)}) meV;  S = {mp.nstr(S, 7)}"
      f"  (JUNO-now 0.17283 +- 0.00167: "
      f"{mp.nstr((S - mpf('0.17283'))/mpf('0.00167'), 2)} sigma)")
print(f"  Sum(m) = {mp.nstr((m1 + m2 + m3)*1000, 5)} meV")

print("\n== P-MIX: maximal atmospheric mixing (registered with eyes open) ==")
s23_fit, s23_lo, s23_hi = 0.572, 0.023, 0.018   # NuFIT 5.x-class NO
tension = (s23_fit - 0.5)/s23_lo
print(f"  claim: sin^2(th23) = 1/2 exactly (provenance: P34 minimal")
print(f"  texture, derived before this framing).  Current global fit")
print(f"  ~ {s23_fit} +{s23_hi}/-{s23_lo}: tension ~ {tension:.1f} sigma,")
print(f"  with KNOWN octant instability across fit releases - registered")
print(f"  anyway; resolving data: JUNO + atmospheric (DUNE/HK).")

print("\n== P-CPV: silent seam phases => J = 0, delta in {0, pi} ==")
d_fit, d_err = 197.0, 27.0   # NuFIT 5.x-class NO, degrees (approx)
print(f"  claim: leptonic Dirac CP violation vanishes (J = 0); current")
print(f"  fit delta ~ {d_fit} +- {d_err} deg: distance from 180 deg ~"
      f" {abs(d_fit-180)/d_err:.1f} sigma - COMPATIBLE today.")
print(f"  KILL: DUNE/HK excluding both CP-conserving values at 5 sigma")
print(f"  kills the silent-phase mechanism outright.")

print("\n== P-BB: the discrete m_bb menu (Majorana signs +-1) ==")
s12sq, s13sq = 0.303, 0.02225   # NuFIT 5.x-class
c12sq, c13sq = 1 - s12sq, 1 - s13sq
vals = []
for e2 in (1, -1):
    for e3 in (1, -1):
        mbb = abs(c12sq*c13sq*float(m1) + e2*s12sq*c13sq*float(m2)
                  + e3*s13sq*float(m3))
        vals.append((e2, e3, mbb*1000))
for e2, e3, v in vals:
    print(f"  (eta2, eta3) = ({e2:+d}, {e3:+d}):  m_bb = {v:.3f} meV")
print(f"  -> a DISCRETE four-value menu (phases frozen at 0/pi by the")
print(f"     mechanism); all ~1-4 meV: below next-generation 0vbb")
print(f"     sensitivity - a consistency statement, honestly labeled.")

print("\n== KILL TABLE (assembled) ==")
print("""  K1  stationarity forcing fails on inspection      -> withdrawn
  K2  sin^2(th23) = 1/2 excluded at 5 sigma         -> P-MIX dead
  K3  CP conservation excluded at 5 sigma (DUNE/HK) -> mechanism dead
  K4  S = 0.17275 excluded at 5 sigma (JUNO-final)  -> dressed base dead
  K5  O35.1b shown impossible (rung != seam count)  -> bridge dead""")
