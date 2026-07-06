#!/usr/bin/env python3
"""
ml3a_least_bias.py — v9 round 11: THE LEAST-BIAS COUPLING CALCULATION
(note-ml3 SSml3a; gates G1-G3 pinned there, 2026-07-05, round 7).

The object: the two-party joint law (CHSH scenario: settings x, y in
{0,1}, outcomes a, b in {+1,-1}) selected by MAXIMUM ENTROPY under the
DERIVED constraints only:
  (i)  marginals <A_x> = <B_y> = 0 (paper 1's symmetric seal law);
  (ii) the amplitude budget sum_xy E_xy^2 = c^2 (the equality-budget
       FORM of the pinned amplitude constraint; c is a SCANNED free
       parameter, not calibrated — see DEVIATIONS below; the
       connectivity floor is c > 0);
  (iii) the fence: the solution must lie in the quantum set — ASSERTED
       via the exact Tsirelson-Landau-Masanes criterion for the
       zero-marginal 2x2x2 correlator body (quantum iff
       |asin E_00 + asin E_01 + asin E_10 - asin E_11| <= pi for ALL
       FOUR single-minus placements; at equal |E| the worst case is
       4*asin e for every odd-parity pattern and 2*asin e for every
       even one — the receipt's reduction, verified over all 16
       patterns), never imposed/projected. Note: the pinned G2 said
       "inside Q-tilde"; for THIS set the projections of Q, Q-tilde
       (NPA 1+AB), and NPA-1 coincide (Tsirelson), so the executed
       fence IS the pinned one.

REGISTRATION DEVIATIONS (round-11 review, disclosed): note-ml3 pinned
FOUR constraints; the "manifoldlikeness obligation" (a global web
constraint) has no behavior-level expression at the 2x2x2 abstraction
and was NOT implemented — the one-bit result is a theorem about the
IMPLEMENTED set (marginals + budget + fence); adding constraints can
only shrink the degenerate set, so one bit is an UPPER BOUND on the
freedom. The pinned "amplitude band" enters only as the equality-budget
FORM: c is a scanned free parameter — the ml1/ml2 measured band never
enters; nothing here is calibrated. The structure (equal spread, the
parity bit, the Tsirelson crossing) is budget-independent — that is the
derivation's content; the quantum match is CONDITIONAL on c = sqrt(2).

THE DERIVATION (verified below at dps = 80):
  With zero marginals each cell is P(ab|xy) = (1 + ab E_xy)/4 and the
  behavior entropy is sum_xy H(E_xy), H even in E, strictly decreasing
  in |E|, strictly concave in E^2. Maximizing under (ii) forces
  |E_xy| = c/2 for all four cells (equal spread; KKT verified
  numerically with asymmetric perturbations). Entropy is SIGN-BLIND
  exactly, so the sign pattern s in {+-1}^4 is degenerate; the local
  sign gauge (a_x, b_y flips) acts s_xy -> a_x b_y s_xy with invariant
  s_00 s_01 s_10 s_11 = +-1 — TWO orbits: the CHSH parity bit.
  RESULT: least-bias fixes the coupling's SHAPE (equal magnitudes, the
  exact magnitude-budget map) and provably cannot fix ONE discrete bit
  (the parity). On the ODD branch the fence binds exactly at the
  Tsirelson budget: 4 asin(c/2) <= pi <=> c <= sqrt(2), equality AT the
  quantum point E = 1/sqrt(2) (4 asin(1/sqrt 2) = pi, an identity).
  The EVEN branch is fence-interior for every c <= 2.

PINNED GATES, quoted from note-ml3 (round 7): G1 "well-posed
(existence + uniqueness up to the disclosed symmetry) or the degeneracy
dimension is computed exactly"; G2 "satisfies the fence (inside Q-tilde)
without being put there by hand (assert, don't project)"; G3 "at CHSH
marginals ... compared against the quantum value with the verdict
branch stated in advance (match <= 1% / miss / underdetermined)".
EXECUTED OUTCOMES (within the pinned branches): G1 = unique up to gauge
x ONE discrete bit, degeneracy exact; G2 = held via exact TLM — the
equal-magnitude maxent solution's odd branch saturates the boundary at
c = sqrt(2) and that SOLUTION is excluded above (odd-parity quantum
behaviors as such persist to budget c^2 = 2.25 on unequal-magnitude
families — the exclusion is of the maxent point, not the parity class);
the even branch is interior for c < 2 (boundary, deterministic-local,
at c = 2 exactly). G3 = the pinned third branch, UNDERDETERMINED, with
the conditional-exact characterization (the <= 1% match branch is NOT
claimed — it would need an independently calibrated c).
Precision: mpmath dps = 80 throughout (the standing rule binds: paper
2's capacity-blindness makes the landscape near-flat in the entangling
direction). No rng. Exit 1 by design if any pinned check refuses.
"""
import mpmath as mp

mp.mp.dps = 80
PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def cell_entropy(E):
    """Entropy of P(ab) = (1 + ab E)/4, zero marginals."""
    tot = mp.mpf(0)
    for s in (1, -1):
        p = (1 + s * E) / 4
        if p > 0:
            tot -= 2 * p * mp.log(p)      # two cells share each value
    return tot

def total_entropy(Es):
    return sum(cell_entropy(E) for E in Es)

print("[ml3a least-bias coupling, dps = 80]")

# ---- D1: H is even and strictly decreasing in |E| (sign-blindness, exact)
grid = [mp.mpf(k) / 40 for k in range(0, 40)]
even_ok = all(abs(cell_entropy(E) - cell_entropy(-E)) < mp.mpf(10) ** -75
              for E in grid)
dec_ok = all(cell_entropy(grid[i]) > cell_entropy(grid[i + 1])
             for i in range(len(grid) - 1))
check("D1: the cell entropy is EVEN in E to 1e-75 (sign-blind at every "
      "order — the degeneracy is exact, not perturbative) and strictly "
      "decreasing in |E|", even_ok and dec_ok)

# ---- D2/G1: equal-spread optimality (KKT + strict concavity in E^2)
c = mp.mpf(1) / 2                          # a generic sub-Tsirelson budget
e0 = c / 2
H_eq = total_entropy([e0] * 4)
worse = 0
for k in range(1, 25):
    d = mp.mpf(k) / 1000
    # asymmetric perturbations preserving the budget sum E^2 = c^2
    a = mp.sqrt(e0 ** 2 + d ** 2)
    b = mp.sqrt(e0 ** 2 - d ** 2)
    H_pert = cell_entropy(a) + cell_entropy(b) + 2 * cell_entropy(e0)
    if H_pert < H_eq: worse += 1
conc = all((cell_entropy(mp.sqrt((grid[i] ** 2 + grid[i + 2] ** 2) / 2))
            > (cell_entropy(grid[i]) + cell_entropy(grid[i + 2])) / 2)
           for i in range(1, len(grid) - 2))
check("G1 (well-posedness): the equal-spread solution |E_xy| = c/2 is the "
      "unique entropy maximizer under the budget — H(sqrt(u)) strictly "
      "concave in u (Schur-concavity carries the general claim; the 24 "
      "perturbations are spot checks, round-11 review NIT-12) — unique "
      "up to the sign gauge x ONE discrete bit",
      worse == 24 and conc, f"{worse}/24 perturbations worse")

# ---- D3/G1: the gauge orbits — the degeneracy is exactly one binary datum
pats = [tuple(1 - 2 * ((m >> i) & 1) for i in range(4)) for m in range(16)]
def orbit_parity(s): return s[0] * s[1] * s[2] * s[3]
def orbit_of(s0):
    seen = {s0}; stack = [s0]
    while stack:
        cur = stack.pop()
        for ax0 in (1, -1):
            for ax1 in (1, -1):
                for by0 in (1, -1):
                    for by1 in (1, -1):
                        img = (ax0*by0*cur[0], ax0*by1*cur[1],
                               ax1*by0*cur[2], ax1*by1*cur[3])
                        if img not in seen:
                            seen.add(img); stack.append(img)
    return frozenset(seen)
orbs = {orbit_of(s) for s in pats}
par_ok = all(len({orbit_parity(x) for x in o}) == 1 for o in orbs)
check("G1 (the degeneracy, exact — proper orbit decomposition, round-11 "
      "review MINOR-3): the local sign gauge partitions the 16 patterns "
      "into EXACTLY TWO transitive orbits of 8, parity constant per orbit "
      "and distinct — the un-fixable datum is ONE BIT",
      len(orbs) == 2 and all(len(o) == 8 for o in orbs) and par_ok
      and {orbit_parity(next(iter(o))) for o in orbs} == {1, -1})

# ---- G2: the fence via the exact TLM criterion, asserted per branch
def tlm_odd(e):
    """Max over odd-parity placements of |sum asin| for equal |E| = e."""
    return 4 * mp.asin(e)
def tlm_even(e):
    return 2 * mp.asin(e)
cs = [mp.mpf(k) / 20 for k in range(1, 40)]   # budgets c in (0, 2)
ok_below = all(tlm_odd(cc / 2) <= mp.pi + mp.mpf(10) ** -75
               for cc in cs if cc < mp.sqrt(2))
ok_above = all(tlm_odd(cc / 2) > mp.pi for cc in cs if cc > mp.sqrt(2))
ok_even = all(tlm_even(cc / 2) <= mp.pi for cc in cs if cc <= 2)
sat = abs(4 * mp.asin(1 / mp.sqrt(2)) - mp.pi)
check("G2 (the fence, asserted via exact TLM): both branches quantum for "
      "c < sqrt(2); the ODD branch saturates the boundary exactly at the "
      "Tsirelson budget (4*asin(1/sqrt 2) = pi to 1e-79) and is EXCLUDED "
      "above it; the EVEN branch stays interior to c = 2",
      ok_below and ok_above and ok_even and sat < mp.mpf(10) ** -79,
      f"saturation residual = {mp.nstr(sat, 3)}")

# ---- G3: the quantum-point comparison at the Tsirelson budget
cT = mp.sqrt(2)
eT = cT / 2
q = 1 / mp.sqrt(2)
match = abs(eT - q)
S_odd = 4 * eT                                  # CHSH value on the odd branch
check("G3 (the quantum point): at the Tsirelson budget the odd branch's "
      "correlators equal the quantum behavior's 1/sqrt(2) to all computed "
      "digits, and its CHSH value is 2*sqrt(2) exactly — CONDITIONAL-EXACT "
      "match; the branch verdict is UNDERDETERMINED-AT-ONE-BIT (the parity "
      "is entropy-blind at every order, D1)",
      match < mp.mpf(10) ** -79 and abs(S_odd - 2 * mp.sqrt(2)) < mp.mpf(10) ** -79,
      f"|e - 1/sqrt2| = {mp.nstr(match, 3)}")

print()
print(f"PRE-REGISTERED GATE LEDGER (note-ml3): "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — G1 unique up "
      f"to gauge x ONE BIT (degeneracy exact); G2 fence asserted (the "
      f"maxent odd branch Tsirelson-clipped); G3 = UNDERDETERMINED-AT-"
      f"ONE-BIT, conditional-exact match (c = sqrt(2) scanned, not "
      f"calibrated)")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
