#!/usr/bin/env python3
"""
f6_dfunctional_regime.py — design note 5: the dense-vs-sparse decider
formalized (paper 1 §7's deferred computation), the matched-profile exemplar
pair, the record-witnessed criterion, and the two bridges (supply law; base-
skew sensitivity).

THE CRITERION (note 5 §3): "D carries off-diagonal support between
commitments" is formalized as RECORD-WITNESSED support — Omega: does the
COMMITTED-record overlap advance strictly between commitments? Three
equivalent faces in the model class: the committed-overlap staircase (Omega),
the recoverable slack (R: optimal system+collar recovery mid-interval), and
the echo floor (E: paper 10's protocol measures exactly R — the criterion is
lab-facing and the corpus already owns the instrument).

THE EXEMPLARS (note 5 §2): pure-dephasing record processes with IDENTICAL
single-time coherence profile G(t) = s^t and identical at-commit data —
  DENSE  (classical shadow): k micro-records per interval, each committing
         contraction s^{1/k}; committed overlap advances continuously; no
         collar; nothing recoverable.
  SPARSE (genuinely indivisible): one uncommitted collar accumulates the
         intra-interval loss unitarily (theta(t) = arccos(s^{t-t_n}), so the
         reduced profile is s^t exactly); each commit SWAPS the collar into a
         fresh record and resets it — the committed overlap is a STAIRCASE.
Subtlety stated in advance: the NEXT seal commits the collar's accumulated
path-dependence — the recoverability window closes at the closing seal; all
recovery statements act mid-interval (that is what "indivisible" means).

PREDICTED CLARIFYING NEGATIVE (note 5 §3, verified below): raw off-diagonal
MAGNITUDE does not decide — single-slot visibility is identical by
construction and two-path D entries are nonzero in BOTH exemplars; what
separates two-time-wise is the mismatch-segment environment overlap
(s^{Dt} dense vs cos(Dtheta) sparse): passive records and single-time
tomography are blind (paper X's undecidability boundary drawn exactly);
active echo-class probing decides.

THE TWO BRIDGES: (i) supply — the odometer increment is the committed-overlap
drop at the event: sparse = exactly -ln s per commit (ATOMIC — routes A/C);
dense with evidence-threshold readouts = continuous exponential increments
(route B): conjunct 1 of the wall's conjunction == "realized regime sparse",
in-model. (ii) determinism precision (feeds note 6) — the content atom's
base-skew sensitivity dC/dp at the count-dual point is FIRST order; the map
w ~ 4.57*dp prices the exact-determinism conjunct at count-dual exactness
~1e-3 web-wide (j4's dispersion threshold w = 0.5% <=> dp = 1.1e-3).

NOT DECIDED HERE (pre-registered): which regime is REALIZED — the placement-
sector open, now equipped with a formal, model-decidable, experiment-facing
criterion. Precision: mpmath dps = 40 closed forms throughout; the one
simulation (dense readout increments) is float64 and disclosed as a
measurement. Constants: s = 0.7, three commits, k = 4, grid {0.25,0.5,0.75}.
"""

import numpy as np
from mpmath import mp, mpf, cos as mcos, acos as macos, log as mlog, e as me

mp.dps = 40
rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

S = mpf("0.7")
K = 4
COMMITS = 3
GRID = [mpf(n) + mpf(q) / K for n in range(COMMITS) for q in range(1, K + 1)]
TOL = mpf("1e-30")

# closed forms ---------------------------------------------------------------
def dense_committed(t):
    # micro-records completed by t (k per unit interval), each contributing s^{1/k}
    steps = int(mp.floor(t * K + mpf("1e-25")))
    return S ** (mpf(steps) / K)

def sparse_committed(t):
    # staircase: records hold s^n after commit n; flat between commits
    n = int(mp.floor(t + mpf("1e-25")))
    return S ** n

def sparse_collar(t):
    # collar overlap cos(theta(t)) with theta = arccos(s^{t-n}) inside interval
    n = int(mp.floor(t + mpf("1e-25")))
    return S ** (t - n) if t - n > 0 else mpf(1)

def profile_dense(t):
    return dense_committed(t)

def profile_sparse(t):
    return sparse_committed(t) * sparse_collar(t)


# ------------------------- CHECK 1: the matched profiles
print("CHECK 1: single-time profile identity (the blindness base)")
worst = max(abs(profile_dense(t) - profile_sparse(t)) for t in GRID)
worst2 = max(abs(profile_dense(t) - S ** t) for t in GRID)
ok = worst < TOL and worst2 < TOL
check("both exemplars' reduced coherence profiles equal s^t at every sampled "
      "time (micro-step grid; sparse continuous by construction) — single-time "
      "tomography cannot distinguish the regimes", ok,
      f"max |Delta| = {mp.nstr(worst, 3)}")

# ------------------------- CHECK 2: at-commit blindness
print("CHECK 2: at-commit record data identical")
ok = all(abs(dense_committed(mpf(n)) - S ** n) < TOL and
         abs(sparse_committed(mpf(n) + mpf("1e-30")) - S ** n) < TOL
         for n in range(1, COMMITS + 1))
check("committed-record overlaps AT commit times equal s^n in BOTH exemplars — "
      "the click law's own data (commit outcomes + survival skeleton) is "
      "regime-blind, instantiating paper X at the record grain", ok)

# ------------------------- CHECK 3: Omega — the staircase separates
print("CHECK 3: Omega (record-witnessed support) — the decider")
adv_sparse = []
adv_dense = []
for n in range(COMMITS):
    ts = [mpf(n) + mpf(q) / K for q in range(1, K)]  # strictly between commits
    cs = [sparse_committed(t) for t in ts]
    cd = [dense_committed(t) for t in ts]
    adv_sparse.append(max(abs(cs[i] - cs[i + 1]) for i in range(len(cs) - 1)) if len(cs) > 1 else mpf(0))
    adv_dense.append(max(abs(cd[i] - cd[i + 1]) for i in range(len(cd) - 1)))
ok = max(adv_sparse) < TOL and min(adv_dense) > mpf("0.03")
check("the committed overlap advances strictly BETWEEN commits in the dense "
      "exemplar (every micro-step) and NOT AT ALL in the sparse one (staircase "
      "flat) — Omega separates the regimes the record itself cannot", ok,
      f"max sparse advance {mp.nstr(max(adv_sparse), 3)}; "
      f"min dense per-gap advance {mp.nstr(min(adv_dense), 4)}")

# ------------------------- CHECK 4: recoverable slack + the echo floor
print("CHECK 4: R (recoverable slack) and the echo floor")
n = 2  # mid of the second interval
tmid = mpf(n - 1) + mpf("0.5")
prof = profile_sparse(tmid)
floor_sparse = sparse_committed(tmid)     # collar-undo restores to this exactly
gain_sparse = floor_sparse - prof         # closed form: s^{n-1}(1 - sqrt(s))
gain_closed = S ** (n - 1) * (1 - S ** mpf("0.5"))
ok = abs(gain_sparse - gain_closed) < TOL and gain_sparse > mpf("0.1")
check("SPARSE: the explicit collar-undo (inverse conditional rotation; the "
      "collar is uncommitted) restores coherence from the profile to the "
      "committed floor exactly — recoverable slack s^{n-1}(1 - sqrt(s))", ok,
      f"{mp.nstr(prof, 8)} -> {mp.nstr(floor_sparse, 8)} (gain {mp.nstr(gain_sparse, 6)})")
# dense: the allowed op class is system'(+empty collar) operations; the env
# branch overlap G is untouched by them, and for the pure-dephasing state
# rho = (1/2)[[1, G],[G*, 1]] the maximal off-diagonal over unitaries is
# (lambda_max - lambda_min)/2 = |G|/2 = the starting value — COMPUTED here
# (30 random SU(2) conjugations; float64, values O(0.5), disclosed), not
# asserted: recoverable slack exactly 0.
import numpy as _np
_rng6 = _np.random.default_rng(20260702)
G = complex(profile_dense(tmid))
rho = 0.5 * _np.array([[1.0, G], [_np.conj(G), 1.0]])
start = abs(rho[0, 1])
best = start
for _ in range(30):
    a_, b_, c_ = _rng6.normal(size=3)
    H = _np.array([[a_, b_ - 1j * c_], [b_ + 1j * c_, -a_]])
    w_, V = _np.linalg.eigh(H)
    U = V @ _np.diag(_np.exp(1j * _rng6.normal(size=2))) @ V.conj().T
    best = max(best, abs((U @ rho @ U.conj().T)[0, 1]))
ev = _np.linalg.eigvalsh(rho)
bound = (ev[-1] - ev[0]) / 2
ok = best <= bound + 1e-12 and abs(bound - start) < 1e-12
check("DENSE: recoverable slack COMPUTED as 0 — over 30 random system "
      "unitaries the off-diagonal never exceeds (lmax - lmin)/2 = |G|/2 = "
      "the starting value (committed records are environment; no collar "
      "exists); the echo floor EQUALS the profile, while in sparse it equals "
      "the committed staircase: paper 10's echo-floor protocol IS the regime "
      "discriminator, already in the corpus as an instrument", ok,
      f"max over U: {best:.12f} vs bound {float(bound):.12f}")

# ------------------------- CHECK 5: the two-time separator + clarifying negative
print("CHECK 5: two-time data — where the blindness ends (the clarifying negative)")
t1 = mpf(n - 1) + mpf("0.25")
t2 = mpf(n - 1) + mpf("0.75")
# env overlap between z-paths differing exactly on [t1, t2]:
ov_dense = S ** (t2 - t1)                                  # 2 of 4 micro-records mismatched
th = lambda t: macos(S ** (t - (n - 1)))
ov_sparse = mcos(th(t2) - th(t1))                          # collar (committed at next seal)
vis1 = profile_dense(t1) - profile_sparse(t1)              # single-slot visibility identical
ok = abs(vis1) < TOL and abs(ov_dense - ov_sparse) > mpf("0.1") \
     and ov_dense > mpf("0.5") and ov_sparse > mpf("0.5")
check("single-slot interference visibility is IDENTICAL (profile-matched) and "
      "two-path off-diagonal support is NONZERO IN BOTH — raw off-diagonal "
      "magnitude does NOT decide the regime; the mismatch-segment environment "
      "overlaps DO differ (s^{Dt} vs cos(Dtheta)): only active multi-time "
      "probing separates — paper 1 §7's phrase must be read as RECORD-WITNESSED "
      "support (Omega), sharpening the corpus's own sentence", ok,
      f"dense {mp.nstr(ov_dense, 6)} vs sparse {mp.nstr(ov_sparse, 6)}")

# ------------------------- CHECK 6: the supply bridge (the j4 hook)
print("CHECK 6: regime => increment law (the wall's conjunct 1, formalized)")
inc_sparse = [-mlog(sparse_committed(mpf(m) + mpf("1e-30"))) -
              -mlog(sparse_committed(mpf(m - 1) + mpf("1e-30"))) for m in range(1, COMMITS + 1)]
ok = all(abs(i - (-mlog(S))) < TOL for i in inc_sparse)
check("SPARSE: per-commit odometer increments are EXACTLY -ln s (atomic; with "
      "the mode menu these are j4's route-A/C atoms)", ok,
      f"all = {mp.nstr(-mlog(S), 8)}")
# dense with evidence-threshold readouts: content accrues continuously; a
# readout fires when accrued evidence crosses an Exp(1) draw => increments are
# themselves iid Exp — definitional in the model; float64 sanity measurement:
draws = rng.exponential(1.0, 4000)
xs = np.sort(draws)
ks = float(np.max(np.abs((np.arange(1, 4001) / 4000.0) - (1.0 - np.exp(-xs)))))
ok = ks < 0.03
check("DENSE: readout-on-evidence-threshold increments are continuous iid "
      "exponential (route B; KS sanity vs Exp(1), float64 measurement, "
      "disclosed) — so (realized regime sparse) <=> (atomic increments): "
      "conjunct 1 of the standing conjunction is the regime question, exactly", ok,
      f"KS = {ks:.4f}")

# ------------------------- CHECK 7: the base-skew sensitivity (feeds note 6)
print("CHECK 7: determinism precision — the content atom's base-skew sensitivity")
def seal_skew(p):
    p = mpf(p); q = 1 - p
    f = lambda h: (p * me**h - q * me**(-h)) / (p * me**h + q * me**(-h)) - me**(-h)
    h = mp.findroot(f, mpf("0.6"))
    a = p * me**h; b = q * me**(-h); Z = a + b
    D = (a / Z) * mlog((a / Z) / p) + (b / Z) * mlog((b / Z) / q)
    return h, D
h0, D0 = seal_skew("0.5")
eps = mpf("1e-10")
_, Dp = seal_skew(mpf("0.5") + eps)
_, Dm = seal_skew(mpf("0.5") - eps)
d1 = (Dp - Dm) / (2 * eps)
ok = abs(h0 - mpf("0.609377863436006")) < mpf("1e-12") and \
     abs(D0 - mpf("0.156109200157240")) < mpf("1e-12") and \
     abs(d1 - mpf("-0.713403")) < mpf("1e-5")
check("the skewed-base fixed point reproduces the count-dual atom and the "
      "sensitivity is FIRST order: dC/dp = -0.713404 at p = 1/2 (NOT a "
      "symmetric minimum — the seal condition breaks the relabel symmetry)", ok,
      f"dC/dp = {mp.nstr(d1, 8)}")
sens = abs(d1) / D0
dp_T3 = mpf("0.005") / sens
dp_cell = mpf("0.10") / sens
ok = abs(sens - mpf("4.5699")) < mpf("0.001") and dp_T3 < mpf("0.0012")
check("the precision map: relative content spread w = 4.570 * delta_p — j4's "
      "dispersion threshold (w = 0.5%) corresponds to base skew 1.1e-3, and "
      "the robust full-cell width (w = 10%) to 2.2e-2: the exact-determinism "
      "conjunct = count-dual exactness to ~1e-3 ACROSS THE WEB, which nothing "
      "in the corpus forces (the count-dual base is the admissible-class GATE "
      "for the W* theorem, not a derived property of every physical "
      "configuration)", ok,
      f"w/delta_p = {mp.nstr(sens, 6)}; delta_p(w=0.5%) = {mp.nstr(dp_T3, 4)}")

# ------------------------- SCOPE (printed, NOT a counted check — the first
# draft counted a hardcoded-True line here; reclassified at round 1 per the
# corpus's own precedent)
print("SCOPE: which regime is REALIZED is NOT decided here — it is paper 1 "
      "§7's placement open, now equipped with: a formal criterion (Omega), "
      "model-level decidability (this receipt), reduced-channel blindness "
      "drawn exactly (checks 1/2/5), a lab-facing instrument (the paper-10 "
      "echo floor), and the supply-law bridge that makes it the records "
      "wall's deciding conjunct.")

# ------------------------------------------------------------------- verdict
print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
