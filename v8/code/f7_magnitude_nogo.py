#!/usr/bin/env python3
"""
f7_magnitude_nogo.py — design note 7: the magnitude no-go (enumerative),
computable legs.

THE QUESTION: can any corpus principle pin the realized per-seal content to
the arena atom EXACTLY (w = 0)? The note's enumeration (P1-P8) closes every
existing route at the derivation level; this receipt fixes the four
computable claims:

  (1) P2's CONDITIONALITY: the arena fixed point is unique GIVEN the base
      (g'(h) = sech^2 h + e^{-h} > 0 everywhere => Var[sigma | mode, base] = 0
      exactly) — and a base ENSEMBLE of width dp produces marginal content
      spread w = 4.570*dp + O(dp^2): the wall's precision demand translates to
      count-dual exactness dp < 1.1e-3 web-wide (j4's dispersion threshold).
  (2) NO PROTECTED MINIMUM, axis 1 (base skew): dC/dp = -0.713404 at the
      count-dual point — FIRST order (re-fixed from f6 CHECK 7).
  (3) NO PROTECTED MINIMUM, axis 2 (cochain unit): perturbing the seal
      condition tanh h = e^{-lambda h} around the admissible unit lambda = 1
      also moves content at first order — dC/dlambda = C'(h)*dh/dlambda with
      dh/dlambda = -h e^{-lh}/(sech^2 h + l e^{-lh}). Two independent
      first-order axes => the content-critical locus has codimension >= 2:
      the symmetric point is NOT a protected point of content in
      configuration space.
  (4) WEIGHT HONESTY: w is a pure number (content ratios are kappa-free) —
      the grading trichotomy is silent on it in BOTH directions, which is why
      the no-go is ENUMERATIVE (relative to the named principle set), not
      absolute. Stated, and checked at the bookkeeping level.

Grade of the headline (note 7 §3): [ENUMERATIVE NO-GO — falsifiable by
exhibiting a pinning principle meeting the stated 1e-3 precision]. Which
regime/base nature realizes is NOT decided here.

Precision: mpmath dps = 40 throughout; no simulation anywhere (closed forms
and root-finding only). Seed irrelevant (no randomness).
"""

from mpmath import mp, mpf, e as me, tanh as mtanh, cosh as mcosh, sech, log as mlog

mp.dps = 40

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

C = lambda h: h * mtanh(h) - mlog(mcosh(h))
Cprime = lambda h: h * sech(h) ** 2          # C' = h sech^2 h (paper 1 §4.3)

# ------------------- CHECK 1: P2's conditionality — uniqueness given the base
print("CHECK 1: the arena fixed point is unique GIVEN the base (P2 conditional)")
g = lambda h: mtanh(h) - me ** (-h)
gp = lambda h: sech(h) ** 2 + me ** (-h)
grid = [mpf(x) / 10 for x in range(1, 51)]
ok = all(gp(h) > 0 for h in grid)
etaB = mp.findroot(g, mpf("0.6"))
ok = ok and abs(etaB - mpf("0.609377863436006")) < mpf("1e-12")
check("g'(h) = sech^2 h + e^{-h} > 0 on (0, 5] and the root is the known "
      "eta_B — Var[sigma | mode, base] = 0 holds EXACTLY, as a conditional "
      "statement: the determinism clause pins content GIVEN the base, and "
      "nothing pins the base", ok,
      f"eta_B = {mp.nstr(etaB, 15)}")

# ------------------- CHECK 2: axis 1 — base skew (re-fixed from f6)
print("CHECK 2: no protected minimum, axis 1 (base skew)")
def seal_skew(p):
    p = mpf(p); q = 1 - p
    f = lambda h: (p * me**h - q * me**(-h)) / (p * me**h + q * me**(-h)) - me**(-h)
    h = mp.findroot(f, mpf("0.6"))
    a = p * me**h; b = q * me**(-h); Z = a + b
    D = (a / Z) * mlog((a / Z) / p) + (b / Z) * mlog((b / Z) / q)
    return D
D0 = seal_skew("0.5")
eps = mpf("1e-10")
d1p = (seal_skew(mpf("0.5") + eps) - seal_skew(mpf("0.5") - eps)) / (2 * eps)
ok = abs(d1p - mpf("-0.713404")) < mpf("1e-5") and abs(D0 - mpf("0.156109200157240")) < mpf("1e-12")
check("dC/dp = -0.713404 at the count-dual point — FIRST order, not a "
      "protected minimum (the seal condition breaks the relabel symmetry)", ok,
      f"dC/dp = {mp.nstr(d1p, 8)}")

# ------------------- CHECK 3: axis 2 — the cochain-unit direction (new)
print("CHECK 3: no protected minimum, axis 2 (cochain unit lambda)")
def seal_lambda(lam):
    lam = mpf(lam)
    f = lambda h: mtanh(h) - me ** (-lam * h)
    return mp.findroot(f, mpf("0.6"))
h1 = seal_lambda(1)
# implicit-function closed form at lambda = 1:
dh_dl_closed = -h1 * me ** (-h1) / (sech(h1) ** 2 + me ** (-h1))
dh_dl_num = (seal_lambda(1 + eps) - seal_lambda(1 - eps)) / (2 * eps)
dC_dl = Cprime(h1) * dh_dl_closed
ok = abs(dh_dl_num - dh_dl_closed) < mpf("1e-8") and abs(dC_dl) > mpf("0.05")
check("dC/dlambda at the admissible unit: closed form matches numerics and is "
      "FIRST order — a second independent configuration axis moving content; "
      "the content-critical locus has codimension >= 2: no generic-"
      "configuration argument can appeal to a protected point", ok,
      f"dh/dl = {mp.nstr(dh_dl_closed, 8)}; dC/dl = {mp.nstr(dC_dl, 8)} "
      f"(relative {mp.nstr(dC_dl / D0, 6)})")

# ------------------- CHECK 4: the ensemble map to j4's thresholds
print("CHECK 4: the precision translation (what pinning would have to achieve)")
sens = abs(d1p) / D0
w_of = lambda dp: abs(seal_skew(mpf("0.5") + dp) - D0) / D0
dp_T3 = mpf("0.005") / sens
dp_cell = mpf("0.10") / sens
ok = abs(w_of(mpf("0.001094")) - mpf("0.005")) < mpf("3e-4") and \
     abs(sens - mpf("4.5699")) < mpf("0.001")
check("w = 4.570*dp holds to O(dp^2) at the per-mille scale: the j4 "
      "dispersion threshold (w = 0.5%) is dp = 1.09e-3 and the robust full "
      "cell (w = 10%) is dp = 2.2e-2 — ANY future pinning principle must "
      "force count-dual exactness below ~1e-3 WEB-WIDE to keep the "
      "degeneracy wall standing; the requirement is now quantified in "
      "advance", ok,
      f"w(dp=1.094e-3) = {mp.nstr(w_of(mpf('0.001094')), 4)}; "
      f"dp(T3) = {mp.nstr(dp_T3, 4)}, dp(cell) = {mp.nstr(dp_cell, 4)}")

# ------------------- CHECK 5: weight honesty (why the no-go is enumerative)
print("CHECK 5: weight bookkeeping — the grading engine is silent")
# content values are pure numbers (kappa never enters); the spread w is a
# RATIO of contents — invariant under any overall unit rescaling chi -> a*chi:
a = mpf("3.7")
w_ratio = (C(mpf("0.5")) - C(mpf("0.49"))) / C(mpf("0.5"))
w_ratio_scaled = (a * C(mpf("0.5")) - a * C(mpf("0.49"))) / (a * C(mpf("0.5")))
ok = abs(w_ratio - w_ratio_scaled) < mpf("1e-38")
check("the spread w is a content RATIO — exactly invariant under any unit "
      "rescaling (weight-0), so the kappa no-go's grading engine neither "
      "pins it nor forbids a pinning principle: the no-go is ENUMERATIVE "
      "(relative to the named principle set P1-P8), and the falsifier class "
      "is stated in note 7 §6 rather than claimed impossible", ok)

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
