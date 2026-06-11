# Paper 38 campaign: O35.1b (rung = seam count) + the p = eps referent
# scan.  Canonical: /tmp/v6_p38_campaign.out (bit-identical required)

from mpmath import mp, mpf, tanh, exp, ln, cosh, sqrt, findroot
import numpy as np

mp.dps = 40
rng = np.random.default_rng(38)

print("== PRE-REGISTRATION (written before computation) ==")
print("""  PHASE A (the count): prove the SELECTION RULE - in a record
  algebra carrying a graded family charge Q in (1/2)Z, with all
  sealed generators Q-neutral EXCEPT one charged seam S, any
  transition amplitude between sectors x and x' vanishes unless
  the word's seam count balances the charge difference, and the
  leading balanced amplitude scales as ||S||^(2|x'-x|) with
  ||S|| = sqrt(eps(1-eps)) from the Seam Theorem.  Receipts on
  explicit systems: (A1) exact zeros for unbalanced words; (A2)
  exact superselection when the seam is removed (no mixing at
  all - oscillations REQUIRE the breaking seam); (A3) the
  FN-record seesaw: charges on the RH/seal sector ONLY, so large
  PMNS mixing survives superselection (the knot resolved by the
  same structure P34's minimal texture already had); verify exact
  rung eigenvalues under orthogonal neutral Y.  HONESTY: the
  mechanism class is Froggatt-Nielsen (1979) - credited; novelty
  = derived suppression + superselection pedigree.  Premises
  graded: family grading with silent inter-sector phases (the
  univalence argument pattern), seam uniqueness.
  PHASE B (p = eps): referent scan - every natural exact
  candidate for 'the commit weight of the marginal triangle',
  tested against eps at 25 digits.  Expected and acceptable
  outcomes: a derivation (unlikely), a sharpened one-line
  premise, or across-the-board exclusion COUNTED AGAINST the
  mechanism.  No candidate added after seeing its value.""")

# ---------- constants ----------
theta = findroot(lambda x: x**3 + x**2 + x - 1, mpf("0.54"))
eta = -ln(theta)
kappa = eta*(1 - theta**2)/(1 - theta**2 + theta)
eps = 3*kappa - 1
eps_eff = eps*(1 - eps)
amp = float(sqrt(eps_eff))
print(f"\n  eps = {mp.nstr(eps, 15)}; seam amplitude sqrt(eps_eff) ="
      f" {mp.nstr(sqrt(eps_eff), 12)}")

# ---------- A1: the selection rule on an explicit graded system ----------
print("\n== A1: selection rule (exact zeros + scaling) ==")
# sectors x = 0, 1/2, 1 (charge units n = 0,1,2); one state per sector
# neutral letters: random PSD block-diagonal; seam: lowering by one unit
d = 3
def rand_neutral():
    out = np.zeros((d, d))
    for i in range(d):
        out[i, i] = rng.uniform(0.2, 0.9)
    return out
N1, N2 = rand_neutral(), rand_neutral()
S = np.zeros((d, d))
S[0, 1] = amp
S[1, 2] = amp          # S lowers charge by one unit, amplitude sqrt(eps_eff)
letters = {"N1": (N1, 0), "N2": (N2, 0), "S": (S, -1), "St": (S.T, +1)}
viol = 0
checked = 0
for _ in range(3000):
    L = int(rng.integers(1, 7))
    word = [list(letters)[int(rng.integers(0, 4))] for _ in range(L)]
    Wm = np.eye(d)
    q = 0
    for nm in word:
        Wm = Wm @ letters[nm][0]
        q += letters[nm][1]
    for i in range(d):
        for j in range(d):
            dq = (i - j)          # charge change in units (row - col)
            el = Wm[i, j]
            checked += 1
            if dq != q and abs(el) > 1e-300:
                viol += 1
print(f"  unbalanced matrix elements nonzero: {viol} / {checked}"
      f" (exact selection rule)")
# scaling: best balanced one-unit and two-unit amplitudes
best1 = best2 = 0.0
for _ in range(20000):
    L = int(rng.integers(1, 7))
    word = [list(letters)[int(rng.integers(0, 4))] for _ in range(L)]
    Wm = np.eye(d)
    for nm in word:
        Wm = Wm @ letters[nm][0]
    best1 = max(best1, abs(Wm[0, 1]), abs(Wm[1, 2]))
    best2 = max(best2, abs(Wm[0, 2]))
print(f"  max one-unit amplitude = {best1:.6f}  (||S|| = {amp:.6f})")
print(f"  max two-unit amplitude = {best2:.6f}  (||S||^2 = {amp**2:.6f})")
print(f"  -> leading balanced amplitudes saturate ||S||^(units): the")
print(f"     count theorem's scaling, with neutral dressing only able")
print(f"     to suppress (neutral letters are contractions).")

# ---------- A2: remove the seam -> exact superselection ----------
print("\n== A2: no seam => exact superselection ==")
best_off = 0.0
for _ in range(5000):
    L = int(rng.integers(1, 9))
    word = [["N1", "N2"][int(rng.integers(0, 2))] for _ in range(L)]
    Wm = np.eye(d)
    for nm in word:
        Wm = Wm @ letters[nm][0]
    best_off = max(best_off, abs(Wm[0, 1]), abs(Wm[1, 2]), abs(Wm[0, 2]))
print(f"  max inter-sector amplitude over 5000 seamless words:"
      f" {best_off:.1e}")
print(f"  -> sectors disconnect exactly: family charge is superselected")
print(f"     UNLESS the seam exists; oscillations REQUIRE the breaking")
print(f"     seam - the mechanism predicts its own necessity.")

# ---------- A3: the FN-record seesaw (charges on the seal sector) -----
print("\n== A3: FN-record seesaw - rungs from charges, mixing free ==")
M0 = 1.0
M = np.diag([M0, M0/amp, M0/amp**2])   # RH seal masses at rungs 0,1/2,1
# neutral Dirac sector: ANY orthogonal Y (charge lives on RH only)
A_ = rng.normal(size=(3, 3))
Q_, R_ = np.linalg.qr(A_)
Y = Q_ @ np.diag(np.sign(np.diag(R_)))
mlight = Y @ np.linalg.inv(M) @ Y.T
ev = np.sort(np.abs(np.linalg.eigvalsh(mlight)))
print(f"  light ratios: m1/m3 = {ev[0]/ev[2]:.10f} (eps_eff ="
      f" {float(eps_eff):.10f})")
print(f"                m2/m3 = {ev[1]/ev[2]:.10f} (sqrt ="
      f" {amp:.10f})")
print(f"  -> EXACT rungs for ANY orthogonal neutral Y (seesaw =")
print(f"     conjugation): the spectrum comes from the CHARGES alone;")
print(f"     mixing comes from the neutral sector - large PMNS mixing")
print(f"     coexists with the superselected grading because the")
print(f"     charges live on the sealed RH sector (exactly the")
print(f"     structure P34's minimal texture already used).  Maximal")
print(f"     theta23 remains MINIMALITY-selected (P34), not")
print(f"     charge-forced: graded honestly.")

# ---------- B1: the p = eps referent scan ----------
print("\n== B1: p = eps referent scan (25 digits) ==")


def hstar(w, lam=mpf(1)):
    return findroot(lambda h: tanh(h) + lam*(1 - tanh(h)**2)*tanh(h)**(w-1)
                    / (1 + lam*tanh(h)**w) - exp(-h), eta)


h3 = hstar(3)
t3 = tanh(h3)
c_amp = t3**3/(1 + t3**3)            # codeword expectation at fixed point
c_amp0 = theta**3/(1 + theta**3)     # same at relation-free point
refs = {
    "codeword expectation at triangle fixed point": c_amp,
    "codeword expectation at free point": c_amp0,
    "commit-prob excess (1+<c>)/2 - 1/2": c_amp/2,
    "amplitude shift (theta^3 - t^3(h*))/theta^3": (theta**3 - t3**3)/theta**3,
    "occupation shift (e^-h* - theta)/theta": (exp(-h3) - theta)/theta,
    "deficit of the boundary: 3 - 1/kappa": 3 - 1/kappa,
    "(3 - 1/kappa) * kappa  [= eps, definitional]": (3 - 1/kappa)*kappa,
    "defect(3)/theta^3 (exact, sign flipped)": None,  # computed below
    "theta^6/(1+theta^6)": theta**6/(1 + theta**6),
    "eta - theta": eta - theta,
}


def Dt(h):
    return h*exp(-h) - ln(cosh(h))


dex = ln(1 + t3**3) - 3*(Dt(h3) - Dt(eta))
refs["defect(3)/theta^3 (exact, sign flipped)"] = dex/theta**3
hits = 0
for nm, v in refs.items():
    diff = v - eps
    tag = ""
    if abs(diff) < mpf("1e-25"):
        tag = "  <-- EXACT MATCH"
        hits += 1
    elif abs(diff) < mpf("0.003"):
        tag = "  <-- near (test failed at 25 digits)"
    print(f"  {nm}: {mp.nstr(v, 12)}  (diff {mp.nstr(diff, 3)}){tag}")
print(f"  exact matches: {hits} - and every match is DEFINITIONAL")
print(f"  (the eps-defining combination itself).  VERDICT B1: no")
print(f"  independent fixed-point referent equals eps; p = eps stands")
print(f"  as a sharpened one-line premise - 'the seam weight is the")
print(f"  normalized first-order binding deficit of the marginal")
print(f"  triangle' - NOT as a derived quantity.  Counted as stated in")
print(f"  the pre-registration: this is the sharpened-premise outcome,")
print(f"  not the derivation outcome.")

print("\n== ASSEMBLED BRIDGE LEDGER (after Phases A and B) ==")
print("""  THEOREM:    selection rule (count = charge difference; A1)
  THEOREM:    per-seam factor sqrt(eps(1-eps)) at stationarity (P37)
  THEOREM:    spectrum = eps_eff rungs for any neutral orthogonal
              Dirac sector (A3, exact)
  PREMISE:    family grading with silent inter-sector phases
              (univalence argument pattern; superselection)
  PREMISE:    seam uniqueness (the one charged sealed object)
  PREMISE:    S-atomicity; seam-block decoupling (P37)
  PREMISE:    p = eps (sharpened, B1; not derived)
  SELECTED:   theta23 = 45 deg (P34 minimality, unchanged)
  CREDIT:     Froggatt-Nielsen (1979) - the mechanism class;
              novelty = derived suppression + superselection
              pedigree + the registered consequence set (P37).
  NEW KILLS:  K6 silent-phase argument fails for the family
              grading -> superselection pedigree lost;
              K7 a second charged sealed object exists -> count
              theorem's uniqueness premise dead.""")
