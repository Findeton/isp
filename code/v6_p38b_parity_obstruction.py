# Review follow-up receipt: the PARITY OBSTRUCTION in the
# FN-record realization, and the LH (Weinberg) four-member menu.
# Canonical: /tmp/v6_p38b_parity.out  (bit-identical required)
import numpy as np, itertools
eps = 0.031768636446582
e = eps*(1-eps); s = np.sqrt(e)

print("== 1. Majorana (RH-charge) realization: even-power obstruction ==")
# seal charges x = (0, 1/2, 1); seam shifts 1/2 unit; Majorana bilinear
# (i,j) needs n = 2(x_i + x_j) insertions -> magnitude s^n.
x = np.array([0.0, 0.5, 1.0])
mags = {}
for i in range(3):
    for j in range(i, 3):
        n = 2*(x[i]+x[j])
        mags[(i, j)] = s**round(n) if abs(n-round(n)) < 1e-12 else None
print("  diagonal insertions n_ii = 4 x_i are EVEN -> diagonal magnitudes")
print("  are integer powers of s^2 = eps_eff: the diagonal-dominated")
print("  spectrum is (eps^2, eps, 1)-spaced, NEVER (eps, sqrt(eps), 1).")
allowed = [(i, j) for (i, j), m in mags.items() if m is not None]
target = np.array([e, np.sqrt(e), 1.0])
best = 1e9
for choice in itertools.product([0, 1, -1], repeat=len(allowed)):
    M = np.zeros((3, 3))
    for c, (i, j) in zip(choice, allowed):
        M[i, j] = M[j, i] = c*mags[(i, j)]
    if abs(np.linalg.det(M)) < 1e-30:
        continue
    w = np.sort(np.abs(np.linalg.eigvalsh(np.linalg.inv(M))))
    best = min(best, max(abs(w/w[2] - target)))
print(f"  exhaustive unit-coefficient scan ({3**len(allowed)} textures):")
print(f"  best max-deviation from the rungs = {best:.4f} -> the rung")
print(f"  spectrum is UNREACHABLE in the Majorana realization.")
print(f"  (P38 Sec. 3's M_R = diag(1, e^-1/2, e^-1) had M_22 ~ s^1: an")
print(f"  ODD power on a Majorana diagonal - forbidden by the rule it")
print(f"  claimed to follow.  The A3 receipt verified a hand-built M.)")

print("\n== 2. The repair: LH half-charges on the Weinberg operator ==")
# q_L = (1, 1/2, 0); m_ij ~ lam^(q_i+q_j), lam = s, integer insertions only
q = np.array([1.0, 0.5, 0.0])
lam = s
allowedW = {}
for i in range(3):
    for j in range(i, 3):
        n = q[i]+q[j]
        allowedW[(i, j)] = lam**round(n) if abs(n-round(n)) < 1e-12 else None
print("  allowed entries:", {f"m{i+1}{j+1}": (f"lam^{round(q[i]+q[j])}"
      if v is not None else "FORBIDDEN") for (i, j), v in allowedW.items()})
menu = {}
allowW = [(i, j) for (i, j), m in allowedW.items() if m is not None]
for choice in itertools.product([0, 1, -1], repeat=len(allowW)):
    M = np.zeros((3, 3))
    nz = ins = 0
    for c, (i, j) in zip(choice, allowW):
        M[i, j] = M[j, i] = c*allowedW[(i, j)]
        if c:
            nz += 1
            ins += round(q[i]+q[j])
    w = np.sort(np.abs(np.linalg.eigvalsh(M)))
    if w[2] < 1e-30 or w[1] < 1e-12:
        continue        # need 3 nonzero masses (NO hierarchical)
    r = tuple(np.round(w/w[2], 8))
    key = r
    if key not in menu or (nz, ins) < menu[key][:2]:
        menu[key] = (nz, ins, r)
print(f"  full-rank unit-coefficient outcomes: {len(menu)}")
for key, (nz, ins, r) in sorted(menu.items(), key=lambda kv: kv[1][1]):
    m1, m2, m3 = r
    if m1 >= 1:
        print(f"    ratios ({m1:.6f}, {m2:.6f}, 1)  entries {nz}"
              f" insertions {ins}  S undefined (degenerate)")
        continue
    S = np.sqrt((m2**2 - m1**2)/(1 - m1**2))
    print(f"    ratios ({m1:.6f}, {m2:.6f}, 1)  entries {nz} insertions"
          f" {ins}  S = {S:.6f}  ({(S-0.17283)/0.00167:+.2f} s JUNO-now)")
print("  -> FULL-RANK NONDEGENERATE members (m1 > 0, all distinct):")
print("     exactly FOUR - S = 0.172747 (rung point, -0.05 s),")
print("     0.167880 (cheap texture, -3.0 s), 0.160500 (-7.4 s, dead),")
print("     0.675516 (~300 s, dead); rank-deficient outcomes (m1 = 0)")
print("     are listed above for completeness and excluded by the")
print("     full-rank requirement.  The two live members differ by")
print("     7.3 sigma at JUNO-final: adjudicable.  MINIMALITY (fewest")
print("     insertions) favors the CHEAP TEXTURE - currently the")
print("     worse-fitting live member.  (An earlier printing of this")
print("     block said TWO-MEMBER and -1.7 sigma: the first missed")
print("     the two data-dead members, the second was the 0.169993")
print("     closed-form transcription error - both corrected.)")

# ---------- 3. integer-charge scan (referee scope) -----------------
# For INTEGER RH charges the parity statement covers diagonals only
# (even powers of lam); off-diagonal-dominant textures can carry odd
# powers, so the full obstruction there is by exhaustive scan.
print("\n== 3. integer RH charges: exhaustive scan, Dirac-consistent ==")
lam = s
target3 = np.array([e, np.sqrt(e), 1.0])
best = (1e9, None)
hit = 0
for q in itertools.product(range(0, 4), repeat=3):
    # Dirac consistency: integer charges -> columns rule-allowed
    # (nonzero); Majorana entry (i,j) needs q_i+q_j insertions
    entries = [(i, j, lam**(q[i]+q[j])) for i in range(3)
               for j in range(i, 3)]
    for choice in itertools.product([0, 1, -1], repeat=6):
        M = np.zeros((3, 3))
        for c, (i, j, m) in zip(choice, entries):
            M[i, j] = M[j, i] = c*m
        if abs(np.linalg.det(M)) < 1e-30:
            continue
        w = np.sort(np.abs(np.linalg.eigvalsh(np.linalg.inv(M))))
        r = w/w[2]
        dev = max(abs(r - target3/target3[2]))
        if dev < best[0]:
            best = (dev, (q, choice, tuple(np.round(r, 5))))
        if dev < 1e-9:
            hit += 1
print(f"  exact rung hits over q in {{0..3}}^3 x unit +-: {hit}")
print(f"  best max-ratio deviation: {best[0]:.4f}  at q = {best[1][0]},"
      f" ratios {best[1][2]}")
print("  METRIC, pinned: max over the two independent ratio deviations")
print("  |m1/m3 - eps_eff| and |m2/m3 - sqrt(eps_eff)|, computed on the")
print("  SEESAW-INVERTED (light) spectrum: the charges sit on M_R and")
print("  the rung target is for the light masses, m_i ~ 1/mu_i with")
print("  mu_i the eigenvalue magnitudes of the scanned texture")
print("  (equivalently: |mu1/mu3 - eps_eff| and |mu1/mu2 - sqrt(e)|).")
print("  WITNESS (so the figure is checkable from one matrix):")
print("  q = (3,2,3), coefficient pattern {11:+1, 12:+1, 13:+1, 22:-1,")
print("  23:+1, 33:0} on magnitudes lam^(q_i+q_j); component deviations")
print("  (0.0144, 0.0092).  Applying the metric to the heavy spectrum")
print("  UNINVERTED gives (0.0144, 0.0770) on this same witness; an")
print("  earlier printing attributed that 0.077 to 'a less complete")
print("  scan variant' - it is the witness's own uninverted second")
print("  component; inversion convention now pinned (caught in review).")
print("  -> integer charges never reach the rungs (scan receipt);")
print("     half-odd charges reach them on the Majorana side (e.g.")
print("     q = (1, 1/2, 0): diag(lam^2, lam, 1) is rule-allowed) but")
print("     die via the Dirac column: charge 1/2 balances no integer")
print("     seam count -> exact zero -> light-mass rank collapse.")
print("     THE OBSTRUCTION IS THE CONJUNCTION, stated as such.")

# ---------- 4. integer charges on the WEINBERG operator (review) -----
# Closes the remaining branch: could INTEGER doublet charges on the
# Weinberg operator (direct light masses - NO seesaw inversion) reach
# the rungs?  Same texture family, DIRECT-spectrum metric.
print("\n== 4. integer doublet charges, Weinberg operator (direct) ==")
best = (1e9, None)
hit = 0
total = 0
for q in itertools.product(range(0, 4), repeat=3):
    entries = [(i, j, lam**(q[i]+q[j])) for i in range(3)
               for j in range(i, 3)]
    for choice in itertools.product([0, 1, -1], repeat=6):
        M = np.zeros((3, 3))
        for c, (i, j, m) in zip(choice, entries):
            M[i, j] = M[j, i] = c*m
        w = np.sort(np.abs(np.linalg.eigvalsh(M)))
        if w[0] < 1e-12 or w[1]-w[0] < 1e-12 or w[2]-w[1] < 1e-12:
            continue            # full rank + nondegenerate, as in Sec. 2
        total += 1
        dev = max(abs(w[0]/w[2] - e), abs(w[1]/w[2] - np.sqrt(e)))
        if dev < best[0]:
            best = (dev, (q, choice, (w[0]/w[2], w[1]/w[2])))
        if dev < 1e-9:
            hit += 1
q4, c4, r4 = best[1]
print(f"  full-rank nondegenerate textures: {total}")
print(f"  exact rung hits: {hit}")
print(f"  best max-ratio deviation (DIRECT metric): {best[0]:.4f}")
print(f"  witness: q = {q4}, coefficients {c4},")
print(f"  ratios ({r4[0]:.4f}, {r4[1]:.4f}, 1)")
print("  -> integer doublet charges never reach the rungs either; and")
print("     the rung DIAGONAL diag(lam^2, lam, 1) forces 2q1 = 2,")
print("     2q2 = 1, q3 = 0 (common shift fixed by q3 = 0; a shift")
print("     rescales the spectrum, not the ratios): q_L = (1, 1/2, 0)")
print("     is the UNIQUE normalized assignment realizing it.  The")
print("     surviving realization is SELECTED, not chosen.")
