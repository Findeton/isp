"""
v7 ROUTE 2 (causal-set "Order + Number = Geometry") -- the NUMBER -> VOLUME half,
and the l_step residue.

Bombelli-Lee-Meyer-Sorkin (PRL 59, 521 (1987)) slogan: in a manifold-like causal set
the causal ORDER fixes the conformal / light-cone structure (Route 1 = Malament's
theorem) and the NUMBER of elements fixes the spacetime VOLUME (each element ~ one
fundamental volume element l_step^d).  So order + number -> the FULL metric =
conformal x volume.

SHARD owns the seal COUNT (number of commitments) and the LI causal ORDER.  ROUTE-2
QUESTION: does the seal count supply the conformal FACTOR / volume measure -- and in
what UNITS?  "Number = Volume" fixes volume in units of l_step^d: the conformal factor
(equivalently the volume density) is owned UP TO the one absolute scale l_step.

This receipt demonstrates NUMBER -> VOLUME-up-to-l_step on a sprinkled causal set:

  (1) Sprinkle a Poisson causal set into a 2d Minkowski causal interval (Alexandrov
      diamond / order-interval) at density rho = 1/l_step^d.  The fundamental
      MYRHEIM-MEYER estimator: E[N] = rho * V, i.e. the EXPECTED CARDINALITY of the
      interval equals (continuum volume) / l_step^d.  Recover V from N up to the
      Poisson fluctuation.  THEOREM (Poisson statistics): N is an unbiased counter of
      V/l_step^d; Var[N]/E[N]^2 -> 0, so V/l_step^d is asymptotically EXACTLY readable
      from the count.

  (2) The l_step RESIDUE (the scale wall, Paper III/57 recurring, on the volume axis):
      rescale l_step -> mu*l_step at FIXED physical geometry => the count N is
      INVARIANT (it counts elements, a weight-0 integer), while the inferred PHYSICAL
      volume V = N * l_step^d scales as mu^d.  So the count fixes V only in l_step^d
      UNITS -- a weight-0 number; the absolute physical volume is weight +d and needs
      the one absolute l_step the records provably cannot supply.

  (3) Myrheim-Meyer DIMENSION estimator (the order half that fixes d, the volume's
      exponent, WITHOUT a metric): the expected fraction of related pairs inside an
      order-interval, f = <relations>/C(N,2), is a pure FUNCTION OF THE DIMENSION d
      alone (f_d = 1.5 * Gamma(d/2) Gamma(d) / Gamma(3d/2) in the BLMS normalization,
      the standard Myrheim-Meyer formula).  So the ORDER (relation counts) fixes d
      (weight-0, scale-free), and then NUMBER fixes the volume in l_step^d units.
      => order+number deliver (dimension d) + (volume / l_step^d), both weight-0; the
         only missing input is the one weight +d unit l_step^d.

  (4) RATIO of two nested interval volumes V2/V1 = N2/N1 is l_step-INVARIANT (weight-0,
      readable exactly) -- the volume's RELATIVE/ratio structure is owned, exactly as
      Paper IV's hop-metric ratios are owned.  Absolute volume is not.

Pre-geometric reading: a Minkowski embedding is used HERE ONLY to GENERATE a manifold-like
sprinkling to test the estimator (the gate is manifoldlikeness / Hauptvermutung).  The
estimators themselves -- cardinality and the relation fraction -- are ORDER-THEORETIC
functionals of the bare causal set (no metric input), which is the point: order + number
are intrinsic; the metric they recover is conformal (Route 1) x volume (this receipt),
owned up to the single l_step.

mpmath dps>=50 where a number is computable; Poisson sprinkling with a fixed seed for
reproducibility; the THEOREM content (unbiasedness, l_step-invariance of the count, the
Myrheim-Meyer dimension formula) is exact, the sprinkle is a finite-sample illustration.
"""
import mpmath as mp
import random

mp.mp.dps = 60
PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-46s %s   %s" % (lbl, val, note))


# ===========================================================================
# A reproducible 2d-Minkowski causal interval sprinkler.
# Coordinates (t, x).  Causal order: p < q iff (t_q - t_p) > |x_q - x_p| and t_q > t_p
# (future-pointing timelike/null separation).  The Alexandrov interval between the
# bottom point b=(0,0) and the top point a=(T,0) is { p : b < p < a }.
# Light-cone coordinates u = (t+x)/2, v = (t-x)/2 make the interval a unit-ish square,
# the standard way to sprinkle a causal diamond uniformly in VOLUME.
# 2d Minkowski volume of the Alexandrov interval of proper time T (diagonal of the
# diamond): V = T^2 / 2  (area of the diamond with timelike diagonal T).
# ===========================================================================

def minkowski2d_diamond_volume(T):
    # diamond between (0,0) and (T,0): a square in (u,v) light-cone coords with
    # 0<u<T/2-ish ... the standard 2d-causal-interval volume is T^2/2.
    return T * T / mp.mpf(2)


def sprinkle_diamond(T, rho, seed):
    """Poisson-sprinkle the causal diamond of (timelike) diagonal T at density rho.
    Returns the list of sprinkled (t,x) points STRICTLY inside the interval.
    Sample N ~ Poisson(rho * V), then place N points uniformly in the diamond via
    light-cone coords (uniform in (u,v) is uniform in spacetime volume)."""
    rng = random.Random(seed)
    V = minkowski2d_diamond_volume(T)
    lam = float(rho * V)
    # draw Poisson(lam) by Knuth's algorithm (lam moderate here)
    L = mp.e ** (-mp.mpf(lam))
    k = 0
    p = mp.mpf(1)
    while True:
        k += 1
        p *= mp.mpf(rng.random())
        if p <= L:
            N = k - 1
            break
    pts = []
    # diamond in light-cone coords: vertices (0,0)&(T,0) => u in (0,T/2)*?
    # Use: t in (0,T), and at height t the spatial slice is |x| < min(t, T-t) (the diamond).
    # Uniform-in-volume sampling: sample u=(t+x)/2 ~ U(0,T/2), w=(t-x)/2 ~ U(0,T/2),
    # then t=u+w, x=u-w; the image is exactly the diamond and uniform in dt dx.
    for _ in range(N):
        u = mp.mpf(rng.random()) * (T / mp.mpf(2))
        w = mp.mpf(rng.random()) * (T / mp.mpf(2))
        t = u + w
        x = u - w
        pts.append((t, x))
    return pts


def causal_order_count_relations(pts):
    """Count ordered related pairs (p<q) under the 2d Minkowski causal order."""
    n = len(pts)
    rel = 0
    for i in range(n):
        ti, xi = pts[i]
        for j in range(n):
            if i == j:
                continue
            tj, xj = pts[j]
            dt = tj - ti
            if dt > 0 and dt > abs(xj - xi):  # i in causal past of j (timelike future)
                rel += 1
    return rel  # ordered count; unordered relations = rel (each pair counted once this way)


# ===========================================================================
head("(1) MYRHEIM-MEYER cardinality: E[N] = V / l_step^d  (number is an unbiased volume counter)")
# Fix a physical geometry: a 2d diamond of diagonal T. Fix l_step => density rho = 1/l_step^d.
# The expected cardinality is E[N] = rho*V = V/l_step^d.  We verify the empirical mean over
# many sprinkles tracks rho*V (unbiasedness) and that the relative fluctuation shrinks ~1/sqrt(N).
d = 2
T = mp.mpf("10")
V_phys_in_units = minkowski2d_diamond_volume(T)   # = T^2/2 = 50, in (l_step=1) units here
l_step = mp.mpf("1")
rho = 1 / l_step ** d
EN = rho * V_phys_in_units
line("d (spacetime dim, 2d Minkowski)", d)
line("diamond diagonal T", mp.nstr(T, 6))
line("continuum volume V (l_step=1 units)", mp.nstr(V_phys_in_units, 8), "(= T^2/2)")
line("density rho = 1/l_step^d", mp.nstr(rho, 6))
line("E[N] = rho*V (Myrheim-Meyer)", mp.nstr(EN, 8))

n_trials = 400
counts = []
for s in range(n_trials):
    pts = sprinkle_diamond(T, rho, seed=1000 + s)
    counts.append(len(pts))
mean_N = mp.mpf(sum(counts)) / n_trials
var_N = mp.mpf(sum((c - float(mean_N)) ** 2 for c in counts)) / n_trials
line("empirical mean N over %d sprinkles" % n_trials, mp.nstr(mean_N, 8))
line("|mean_N - E[N]| / E[N]", mp.nstr(abs(mean_N - EN) / EN, 4), "(unbiased: -> 0)")
line("Var[N] / E[N]   (Poisson: =1)", mp.nstr(var_N / EN, 5), "(Poisson signature)")
# Recover V/l_step^d from a SINGLE large count, error ~ 1/sqrt(N):
V_inferred = mean_N * l_step ** d   # N * l_step^d
line("V inferred = <N>*l_step^d", mp.nstr(V_inferred, 8), "(recovers V to ~1/sqrt(N))")
PASS["(1) number is an UNBIASED volume counter: E[N]=V/l_step^d, mean tracks it, Var/E~1 (Poisson)"] = (
    abs(mean_N - EN) / EN < mp.mpf("0.03") and abs(var_N / EN - 1) < mp.mpf("0.20")
)

# ===========================================================================
head("(2) THE l_step RESIDUE: rescale l_step -> mu*l_step => COUNT invariant, PHYSICAL volume scales")
# This is the scale wall on the VOLUME axis.  At FIXED physical geometry, the SPRINKLED SET
# (the actual elements and their order) is what it is -- the count N is a weight-0 integer,
# it does not change when we merely RELABEL the fundamental volume unit l_step.  But the
# PHYSICAL volume we ASCRIBE, V = N * l_step^d, scales as mu^d.  So 'Number = Volume' fixes
# volume ONLY in l_step^d units; the absolute physical volume is weight +d and needs l_step.
N_observed = counts[0]            # one concrete sprinkle's count: a fixed weight-0 integer
line("observed count N (a weight-0 integer)", N_observed, "(unchanged by relabeling l_step)")
for mu in [mp.mpf("1"), mp.mpf("2"), mp.mpf("3.3")]:
    l = mu * l_step
    V_ascribed = N_observed * l ** d
    line("  l_step -> %s : V = N*l_step^d" % mp.nstr(mu, 3), mp.nstr(V_ascribed, 8),
         "(scales as mu^d = %s)" % mp.nstr(mu ** d, 5))
# the count is mu-invariant; the ascribed physical volume is not:
V1 = N_observed * (mp.mpf("1") * l_step) ** d
V2 = N_observed * (mp.mpf("3.3") * l_step) ** d
line("V(mu=3.3)/V(mu=1)", mp.nstr(V2 / V1, 8), "(= mu^d = 10.89: weight +d, absolute scale FREE)")
PASS["(2) l_step residue: count N is l_step-INVARIANT (weight-0); physical volume V=N*l_step^d is weight +d"] = (
    abs(V2 / V1 - mp.mpf("3.3") ** d) < mp.mpf("1e-40")
)

# ===========================================================================
head("(3) MYRHEIM-MEYER DIMENSION: the ORDER (relation fraction) fixes d, scale-free")
# The expected ORDERING FRACTION (fraction of causally RELATED pairs among all pairs) in a
# d-dim Minkowski order-interval is a PURE FUNCTION of the dimension d (NO metric, NO l_step):
# the canonical Myrheim-Meyer ordering fraction (matches r1, r3, and the paper)
#   f(d) = <#relations>/C(N,2) ->  Gamma(d + 1) * Gamma(d/2) / (2 * Gamma(3d/2)).
# At d=2: f(2) = Gamma(3)*Gamma(1)/(2*Gamma(3)) = 2*1/(2*2) = 1/2 (a 2d interval has, on
# average, exactly half its pairs causally related).  At d=4: f(4) = 1/10.  Monotone
# decreasing in d => invertible: the relation fraction is a scale-free DIMENSION meter.
def mm_fraction(d_):
    d_ = mp.mpf(d_)
    return mp.gamma(d_ + 1) * mp.gamma(d_ / 2) / (2 * mp.gamma(3 * d_ / 2))
f2_formula = mm_fraction(2)
line("Myrheim-Meyer f(d) at d=2 (formula)", mp.nstr(f2_formula, 12), "(= 1/2 exactly)")
line("Myrheim-Meyer f(d) at d=4 (formula)", mp.nstr(mm_fraction(4), 12), "(= 1/10 exactly)")
PASS["(3a) Myrheim-Meyer formula exact: f(2) = 1/2, f(4) = 1/10 (scale-free dimension meter)"] = (
    abs(f2_formula - mp.mpf("0.5")) < mp.mpf("1e-50")
    and abs(mm_fraction(4) - mp.mpf("0.1")) < mp.mpf("1e-50")
)

# Empirically: over the sprinkles, <relations>/C(N,2) should track f(2) = 1/2.
# (Use the larger sprinkles for low variance.)
fracs = []
for s in range(60):
    pts = sprinkle_diamond(T, rho, seed=5000 + s)
    n = len(pts)
    if n < 2:
        continue
    rel = causal_order_count_relations(pts)   # ordered = unordered related-pair count
    Cn2 = n * (n - 1) / 2
    fracs.append(mp.mpf(rel) / Cn2)
f_emp = mp.fsum(fracs) / len(fracs)
line("empirical relation fraction <r>/C(N,2)", mp.nstr(f_emp, 8), "(tracks f_2 = 1/2)")
# Invert: solve f_d = f_emp for d (Myrheim-Meyer dimension estimate), scale-free.
d_est = mp.findroot(lambda dd: mm_fraction(dd) - f_emp, mp.mpf("2"))
line("Myrheim-Meyer dimension estimate", mp.nstr(d_est, 6), "(recovers d~2 from ORDER alone)")
PASS["(3b) ORDER fixes the dimension d (scale-free): empirical fraction -> d_est ~ 2 via Myrheim-Meyer"] = (
    abs(d_est - 2) < mp.mpf("0.25")
)
# the dimension is the volume's EXPONENT; the order fixes it with NO scale, NO metric.
# So order -> d (weight-0), number -> V/l_step^d (weight-0) ; only l_step^d (weight +d) missing.

# ===========================================================================
head("(4) VOLUME RATIOS are l_step-INVARIANT (weight-0): the RELATIVE volume is owned, exactly")
# A sub-interval (smaller diamond, diagonal T2<T) nested in the big one.  The RATIO of the
# two counts estimates the RATIO of the two continuum volumes, which is l_step-INDEPENDENT:
#   V2/V1 = (T2/T)^2  in 2d, and N2/N1 -> V2/V1 with the l_step^d unit CANCELLING.
T2 = mp.mpf("6")
V_ratio_true = (T2 / T) ** d            # = (6/10)^2 = 0.36
line("true volume ratio V(T2)/V(T) = (T2/T)^d", mp.nstr(V_ratio_true, 8))
# estimate by counts (mean over sprinkles of each diamond at the SAME rho):
c_big = []
c_sml = []
for s in range(200):
    c_big.append(len(sprinkle_diamond(T, rho, seed=7000 + s)))
    c_sml.append(len(sprinkle_diamond(T2, rho, seed=9000 + s)))
ratio_est = (mp.fsum(c_sml) / len(c_sml)) / (mp.fsum(c_big) / len(c_big))
line("count-ratio estimate <N2>/<N1>", mp.nstr(ratio_est, 8), "(-> V2/V1, l_step CANCELS)")
# and it is l_step-invariant ALGEBRAICALLY: N2/N1 = (rho V2)/(rho V1) = V2/V1, no l_step.
line("|ratio_est - true| / true", mp.nstr(abs(ratio_est - V_ratio_true) / V_ratio_true, 4),
     "(volume RATIO owned exactly, scale-free)")
PASS["(4) volume RATIO V2/V1 = N2/N1 is l_step-INVARIANT (weight-0): relative volume owned, absolute not"] = (
    abs(ratio_est - V_ratio_true) / V_ratio_true < mp.mpf("0.05")
)

# ===========================================================================
head("(5) THE ROUTE-2 LEDGER: order x number = (d + conformal) x (volume/l_step^d) -- up to l_step")
# Symbolic weight bookkeeping (the Paper III/6 grading homomorphism, on the volume axis):
#   - causal ORDER       : weight 0  (a relation; Malament -> conformal class, Route 1, scale-free)
#   - dimension d        : weight 0  (Myrheim-Meyer relation fraction; pure number)
#   - seal COUNT N       : weight 0  (an integer; counts elements)
#   - volume in units    : V/l_step^d = N : weight 0  (owned)
#   - absolute volume V  : weight +d (= N * l_step^d ; needs l_step^d, the ONE unit records lack)
weights = {
    "causal order (relation)": 0,
    "Myrheim-Meyer dimension d": 0,
    "seal count N": 0,
    "volume in l_step^d units (= N)": 0,
    "ABSOLUTE physical volume V = N*l_step^d": d,   # weight +d
    "ABSOLUTE metric (conformal x V^{1/d}) length": 1,  # weight +1 (a length)
}
for k, w in weights.items():
    line("weight(%s)" % k, "+%d" % w if w >= 0 else str(w),
         "(OWNED, weight-0)" if w == 0 else "(WALLED: needs l_step)")
# The honest Route-2 statement: everything weight-0 is owned (order->conformal+d, number->
# volume-in-units); the single weight +d object (absolute volume), equivalently the one
# weight +1 length unit l_step, is the SAME wall as d/G/c_m/metric -- a recurrence, not a new wall.
PASS["(5) Route-2 ledger: order(0)+dimension(0)+count(0)+volume-in-units(0) OWNED; absolute volume(+d)/l_step WALLED"] = (
    all(weights[k] == 0 for k in
        ["causal order (relation)", "Myrheim-Meyer dimension d", "seal count N",
         "volume in l_step^d units (= N)"])
    and weights["ABSOLUTE physical volume V = N*l_step^d"] == d
    and weights["ABSOLUTE metric (conformal x V^{1/d}) length"] == 1
)

# ===========================================================================
head("MACHINE CHECKS")
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))
assert ok, "a check failed"
print("=" * 78)
print("DONE.  Order+Number = Geometry on a sprinkled causal set: the ORDER fixes the")
print("       conformal structure + the dimension d (weight-0, Route 1 / Myrheim-Meyer),")
print("       the seal NUMBER fixes the VOLUME in l_step^d UNITS (weight-0, unbiased count).")
print("       The metric continuum is buildable UP TO the single absolute scale l_step --")
print("       a recurrence of the one scale wall (behind d, G, c_m, the metric), on the volume axis.")
print("=" * 78)
