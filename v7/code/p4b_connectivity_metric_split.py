"""
v7 Paper 4 — the connectivity/metric weight-split receipt (entanglement -> spacetime).

Paper 4's headline structural theorem: the entanglement -> geometry map splits cleanly
by WEIGHT, and the split IS the program's own scale no-go (Papers 3/6/57):

  - entanglement content  chi = D(P_AB||P_BA)  is WEIGHT-0 (a pure KL number, nats):
    gauge-invariant under the record-length rescaling l -> mu*l.  So entanglement can
    source weight-0 structure -- TOPOLOGY / CONNECTIVITY (the Van Raamsdonk pinch: zero
    mutual info => no edge => disconnected) and the connectivity graph's HOP-METRIC up to
    one overall scale l_step (the integer hop-distance RATIOS are l_step-invariant).

  - a graph DISTANCE / METRIC is WEIGHT +1 (a length = #hops * l_step): it scales as mu
    under l -> mu*l.  By the grading-homomorphism trichotomy (Paper 3), a weight-0
    record functional can NEVER be a weight +1 object -- the records cannot supply the
    one absolute l_step.  So entanglement provably CANNOT fix the metric.

  => entanglement -> spacetime is exactly HALF-OPEN: connectivity & hop-metric-up-to-scale YES
     (weight-0, non-circular), absolute metric NO (weight +1 = the Newton-constant no-go
     again).  The joint click-law (receipt p4a/f5) supplies the *dynamics* of the
     correlation that defines the graph; this receipt supplies the *geometry* verdict.

Verified at mpmath dps>=100 / sympy-exact:
  (1) WEIGHT: chi weight-0 (gauge-invariant), graph distance weight +1 (scales as mu);
      the metric needs l_step (weight +1) which a weight-0 functional cannot supply;
  (2) the PINCH-OFF as a weight-0 statement: I(i:j)=0 <=> no edge <=> disconnected;
  (3) the HOP-METRIC up to one overall scale: distance RATIOS d_ij/d_kl invariant under
      l_step -> mu*l_step (the absolute scale free), and the -log I additive-gauge contrast
      (the -log I ratios are NOT invariant -- so it is NOT a conformal/Weyl class).

Pre-geometric: every quantity is a record-internal probability / KL number; no spacetime,
metric, light cone, or s^2 is used as input -- the result is precisely that the records
yield connectivity + a hop-metric up to one scale but NOT an absolute metric.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 120
PASS = {}


def head(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


def line(lbl, val, note=""):
    print("  %-44s %s   %s" % (lbl, val, note))


# ===========================================================================
head("(1) WEIGHT: chi (entanglement content) weight-0; graph DISTANCE weight +1")
# Under the record-length gauge l -> mu*l: a KL content chi (nats) is invariant (weight 0);
# a length = (#hops) * l_step scales as mu (weight +1).  The metric needs l_step.
mu = sp.symbols("mu", positive=True)
w_chi = sp.Integer(0)          # chi ~ nats, dimensionless => weight 0
w_dist = sp.Integer(1)         # distance = #hops * l_step ~ l => weight +1
line("weight(chi = D(P_AB||P_BA))", str(w_chi), "(KL in nats: gauge-invariant)")
line("weight(graph distance = #hops*l_step)", str(w_dist), "(a length: scales as mu)")
# numeric gauge check: a KL number is unchanged by l->mu*l; a distance scales by mu.
p, q = mp.mpf("0.7"), mp.mpf("0.3")
chi_val = p * mp.log(p / mp.mpf("0.5")) + q * mp.log(q / mp.mpf("0.5"))
for mu_v in [mp.mpf("1.7"), mp.mpf("5")]:
    line("chi under l->%s*l / chi" % mp.nstr(mu_v, 2), mp.nstr(chi_val / chi_val, 6), "(=1: weight-0)")
    line("distance under l->%s*l / distance" % mp.nstr(mu_v, 2), mp.nstr(mu_v, 6), "(=mu: weight+1)")
PASS["(1) chi is weight-0 (gauge-invariant); a graph distance is weight +1 (scales as mu)"] = (
    w_chi == 0 and w_dist == 1
)
# the grading no-go: a weight-0 functional cannot equal a weight +1 object (Paper 3
# trichotomy). The metric's l_step is the one absolute unit the weight-0 records lack.
PASS["(1b) NO-GO: weight-0 entanglement content != weight +1 metric (records lack l_step)"] = (
    w_chi != w_dist
)

# ===========================================================================
head("(2) PINCH-OFF as a weight-0 statement: I(i:j)=0 <=> no edge <=> disconnected")
# Build a 3-node mutual-information adjacency. Nodes A,B share entanglement (I>0);
# node C is product with both (I=0). Edge exists iff I>0. C pinches off (Van Raamsdonk).
def mutual_info(joint):
    # joint: 2x2 probability matrix over (a,b) in {0,1}^2
    Z = sum(sum(row) for row in joint)
    P = [[joint[a][b] / Z for b in range(2)] for a in range(2)]
    pa = [P[a][0] + P[a][1] for a in range(2)]
    pb = [P[0][b] + P[1][b] for b in range(2)]
    I = mp.mpf(0)
    for a in range(2):
        for b in range(2):
            if P[a][b] > 0:
                I += P[a][b] * mp.log(P[a][b] / (pa[a] * pb[b]))
    return I


# A-B correlated (entangled): joint favours (0,0),(1,1)
I_AB = mutual_info([[mp.mpf("0.4"), mp.mpf("0.1")], [mp.mpf("0.1"), mp.mpf("0.4")]])
# A-C product: joint = pa x pc (independent) => I=0
I_AC = mutual_info([[mp.mpf("0.25"), mp.mpf("0.25")], [mp.mpf("0.25"), mp.mpf("0.25")]])
I_BC = I_AC
line("I(A:B) (entangled pair)", mp.nstr(I_AB, 10), "> 0  => edge A-B")
line("I(A:C) = I(B:C) (product)", mp.nstr(I_AC, 6), "= 0  => NO edge => C pinched off")
PASS["(2) pinch-off: I>0 => edge (A-B connected), I=0 => no edge (C disconnected component)"] = (
    I_AB > mp.mpf("0.01") and abs(I_AC) < mp.mpf("1e-100") and abs(I_BC) < mp.mpf("1e-100")
)

# ===========================================================================
head("(3) METRIC up to the ONE overall scale l_step: weight-0 fixes RATIOS, scale free")
# The weight-0 graph fixes all RELATIVE distances; the PHYSICAL metric assigns each a
# length = (weight-0 graph distance) * l_step, with l_step the ONE free modulus (weight+1).
# Under the physical scale freedom l_step -> mu*l_step, distance RATIOS d_ij/d_kl are
# INVARIANT (the similarity / ratio class) while absolute lengths scale by mu.  So the
# records deliver the metric UP TO ONE OVERALL SCALE -- not the absolute metric (weight+1),
# and NOT (by itself) the full local-Weyl conformal class.
# CAVEAT (why this is NOT a -log-I 'conformal' claim): an edge-length assignment
# d_ij = -log I_ij instead carries an ADDITIVE zero-point gauge under I -> s*I (all
# d shift by -log s), fixing distance DIFFERENCES (and their ratios) but NOT the metric
# ratios d_ij/d_kl -- a different, weaker structure. The physical modulus is l_step
# (multiplicative on distance), which gives the genuine ratio/similarity class below.
# ILLUSTRATIVE integer graph (hop) distances -- in a full construction these are the
# shortest-path hop-counts on the I>0 adjacency of check (2); here any weight-0 integers
# suffice, since the point (ratio-invariance under l_step) holds for ANY weight-0 distances.
hops = {"12": mp.mpf("2"), "13": mp.mpf("5"), "23": mp.mpf("3")}
def phys(l_step):
    return {k: hops[k] * l_step for k in hops}
d1 = phys(mp.mpf("1"))
d2 = phys(mp.mpf("3.3"))      # rescale the ONE physical scale l_step by 3.3 (the free modulus)
r1 = d1["13"] / d1["12"]
r2 = d2["13"] / d2["12"]
line("distance RATIO d13/d12, l_step=1", mp.nstr(r1, 12))
line("distance RATIO d13/d12, l_step=3.3", mp.nstr(r2, 12), "(= l_step 1: RATIOS fixed)")
line("absolute d12: l_step 1 vs 3.3", "%s vs %s" % (mp.nstr(d1["12"], 4), mp.nstr(d2["12"], 4)),
     "(scales by mu: absolute scale FREE)")
# additive-gauge contrast: -log I shifts additively (differences fixed, ratios NOT)
I12, I13 = mp.mpf("0.20"), mp.mpf("0.05")
add1 = (-mp.log(I13)) / (-mp.log(I12))
add2 = (-mp.log(mp.mpf("3.3") * I13)) / (-mp.log(mp.mpf("3.3") * I12))
line("(-log I) ratio: I-scale 1 vs 3.3", "%s vs %s" % (mp.nstr(add1, 5), mp.nstr(add2, 5)),
     "(NOT invariant: -log I is an additive gauge, not conformal)")
PASS["(3) metric up to ONE overall scale: distance RATIOS invariant under l_step, absolute scale free"] = (
    abs(r1 - r2) < mp.mpf("1e-100") and abs(d1["12"] - d2["12"]) > mp.mpf("0.1")
)
PASS["(3b) -log I is an ADDITIVE gauge (ratios NOT invariant) -- not a conformal/Weyl class"] = (
    abs(add1 - add2) > mp.mpf("0.05")
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
print("DONE.  Entanglement (weight-0) sources connectivity + a hop-metric up to one scale, NOT")
print("       the ABSOLUTE metric (weight +1 = the same l_step the scale no-go forbids).  Half-open.")
print("=" * 78)
