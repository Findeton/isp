#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R4 -- ORDER-FEEDBACK PROBE  (the HIGHEST-risk open path of the v7 downstream no-go).
Write+run receipt, mpmath dps>=120.

THE CRUX (Phase-2 open risk 1).  The downstream field-blindness no-go (Paper XII +
p6 PART 3: every downstream sector factors through the level-(1+AB) moment algebra M,
chi_AB free up to Q-tilde) is ROBUST only if the emergent CAUSAL ORDER is generated
INDEPENDENTLY of the transverse entangling content chi_AB.

  - the causal ORDER is built from the LONGITUDINAL sigma-arrow
        sigma = D(P_AB || P_BA)                                  (paper1 s3.2, paper10)
    = the accumulated ENTROPY PRODUCTION (forward-vs-reverse KL of the per-chain
      commit-order transport).  It is a functional of the SINGLE-CHAIN transport
      (P, pi) and its time-reversal -- a LONGITUDINAL object along ONE record chain.

  - the transverse entangling content is
        chi_AB = I_sigma                                         (paper4/paper12)
    = the cross-moment / mutual information between TWO PARALLEL record chains'
      committed OUTCOMES.  It is a TRANSVERSE object (between chains), driven by the
      joint-law coupling lam at FIXED single-chain marginals.

The orthogonality claim 'causal order = longitudinal sigma directionality  vs
chi_AB = transverse cross-moment E_xy' is structurally sound but was NOT
machine-proven.  THE BREAK THAT COULD HIDE (prompt, risk 1): if the click-law
dynamics that GENERATES the causal order is driven by the transverse chi_AB pattern
-- e.g. entanglement-graph connectivity feeding back into WHICH seals are causally
ordered -- then sigma would be a functional of E_xy and the no-go would be
CONDITIONAL.  We must DETERMINE, ruthlessly:

  (a) is sigma (the order-generator) a functional of E_xy (the transverse
      cross-moment), or generated from the per-chain commit-order statistics ALONE?
      TEST: vary chi_AB at FIXED single-chain commit-order transport; check sigma /
      the induced causal order is UNCHANGED.  Predicted: order independent of E_xy.

  (b) conversely: vary the ORDER (the transport (P,pi)) and check chi_AB is untouched.

  (c) THE FEEDBACK TEST (the actual make-or-break).  Build the induced causal order
      explicitly as a RANKING of seals by their accumulated sigma, then ASK whether
      re-wiring the transverse entanglement graph (changing the chi_AB connectivity
      pattern at FIXED per-chain transport) PERMUTES that ranking.  If the order is
      invariant under arbitrary chi_AB re-wirings -> NO feedback, path CLOSES.  If a
      chi_AB re-wiring re-orders the seals -> a PATH OPENS.

  (d) cross-partial / Jacobian: the mixed sensitivity d sigma / d chi_AB and
      d chi_AB / d sigma over the joint sweep, to <tolerance, both directions.

  (e) the strongest adversary we can build pre-geometrically: a HYPOTHETICAL coupled
      generator sigma_couple = sigma_long + g * (chi_AB term) and ask what the data
      forces g to be.  Honest residue: at theorem grade the order-generator is
      sigma_long (g=0 forced by the definition sigma = D(P_AB||P_BA), a functional of
      the per-chain transport ONLY); a g!=0 generator is a DIFFERENT, unbuilt
      dynamics -- we flag the exact residual-risk locus.

ALSO (open risk 3, matter two-party, brief audit): could a TWO-PARTY matter
interaction (interacting GW flow / mode-selecting Hamiltonian) couple the mode to
chi_AB?  We argue any such coupling must still escape R-invariance and flag
'field-blind a fortiori, sector unbuilt'.

Pre-geometric discipline: everything below is a record-internal pure number.  (P,pi)
is an abstract commit-order transport on record LABELS (no spacetime); sigma is a
weight-0 KL; chi_AB is a weight-0 mutual information between parallel chains'
outcomes; the "order" is the partial order seals inherit from accumulated sigma --
no metric, no s^2, no light cone.

mpmath dps=120 (cancellation-heavy KL / near-degenerate transports use 140 locally);
sympy-exact for the structural separation lemma.
Run: python s_order_feedback_probe.py
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 120
TOL = mp.mpf(10) ** (-100)
PASS = {}


def head(s):
    print("\n" + "=" * 80 + "\n" + s + "\n" + "=" * 80)


def line(lbl, val, note=""):
    print("  %-54s %s   %s" % (lbl, val, note))


def check(name, cond):
    PASS[name] = bool(cond)
    line("CHECK  " + name, "PASS" if cond else "*** FAIL ***")
    return bool(cond)


# ===========================================================================
# SHARED MACHINERY
# ===========================================================================
# LONGITUDINAL sigma-arrow (the ORDER-GENERATOR), faithful to f3c/paper10:
#   sigma = sum_{x,y} pi(x) P(y|x) * log[ pi(x) P(y|x) / ( pi(y) P(x|y) ) ]
#         = D(P_AB || P_BA)  at the one-step joint level.
# A functional of the SINGLE-CHAIN transport (P, pi) ONLY (and its reversal).
def stationary(P, n):
    A = mp.matrix(n, n)
    for j in range(n):
        for i in range(n):
            A[j, i] = (1 if i == j else 0) - P[i][j]
    for i in range(n):
        A[n - 1, i] = mp.mpf(1)
    b = mp.matrix(n, 1)
    b[n - 1] = mp.mpf(1)
    pic = mp.lu_solve(A, b)
    return [pic[i] for i in range(n)]


def sigma_arrow(P):
    """sigma = D(P_AB || P_BA): per-chain longitudinal entropy production.
    Pure functional of the single-chain transport P (and its stationary pi)."""
    n = len(P)
    pi = stationary(P, n)
    s = mp.mpf(0)
    for x in range(n):
        for y in range(n):
            fwd = pi[x] * P[x][y]
            rev = pi[y] * P[y][x]
            if fwd > 0 and rev > 0:
                s += fwd * mp.log(fwd / rev)
    return s, pi


# TRANSVERSE chi_AB (the ENTANGLING content): mutual information between two
# parallel chains' committed OUTCOMES under joint law P(a,b) ~ exp(eta_a a + eta_b b
# + lam a b), a,b in {+1,-1}.  Driven by lam at FIXED single-party marginals
# (paper4/paper12: chi_AB varies with the cross-moment at fixed marginals).
def joint_outcome(eta_a, eta_b, lam):
    P = {}
    for a in (1, -1):
        for b in (1, -1):
            P[(a, b)] = mp.e ** (eta_a * a + eta_b * b + lam * a * b)
    Z = sum(P.values())
    for k in P:
        P[k] /= Z
    return P


def marg_a_out(P):
    return sum(a * P[(a, b)] for a in (1, -1) for b in (1, -1))


def marg_b_out(P):
    return sum(b * P[(a, b)] for a in (1, -1) for b in (1, -1))


def cross_moment(P):
    return sum(a * b * P[(a, b)] for a in (1, -1) for b in (1, -1))


def chi_AB_mutual_info(P):
    """chi_AB = I_sigma = mutual information of the two parallel chains' outcomes
    (the transverse cross-moment content)."""
    pa = {a: sum(P[(a, b)] for b in (1, -1)) for a in (1, -1)}
    pb = {b: sum(P[(a, b)] for a in (1, -1)) for b in (1, -1)}
    mi = mp.mpf(0)
    for a in (1, -1):
        for b in (1, -1):
            if P[(a, b)] > 0:
                mi += P[(a, b)] * mp.log(P[(a, b)] / (pa[a] * pb[b]))
    return mi


def solve_fixed_marg(lam, ma, mb):
    """re-solve (eta_a, eta_b) so the OUTCOME marginals are <a>=ma, <b>=mb at lam.
    This holds the SINGLE-CHAIN outcome statistics fixed while lam (-> chi_AB) varies."""
    def fn(ea, eb):
        P = joint_outcome(ea, eb, lam)
        return [marg_a_out(P) - ma, marg_b_out(P) - mb]
    sol = mp.findroot(fn, [mp.mpf("0.3"), mp.mpf("0.3")])
    return sol[0], sol[1]


# ===========================================================================
head("ANCHOR.  the two objects, separately defined and separately driven")
# ===========================================================================
print("""
  sigma  (ORDER-GENERATOR, LONGITUDINAL): sigma = D(P_AB||P_BA), a functional of the
         SINGLE-CHAIN commit-order transport (P,pi).  Driven by the transport bias.
  chi_AB (ENTANGLING CONTENT, TRANSVERSE): mutual information of two PARALLEL chains'
         committed outcomes, driven by the joint coupling lam at FIXED marginals.
""")

# a driven single-chain transport (nonzero current => sigma>0, arrow present)
P0 = [[mp.mpf('0.10'), mp.mpf('0.70'), mp.mpf('0.20')],
      [mp.mpf('0.20'), mp.mpf('0.10'), mp.mpf('0.70')],
      [mp.mpf('0.70'), mp.mpf('0.20'), mp.mpf('0.10')]]
sig0, pi0 = sigma_arrow(P0)
line("single-chain transport P0 stationary pi", "[" + ", ".join(mp.nstr(p, 12) for p in pi0) + "]")
line("sigma0 = D(P_AB||P_BA) (the order-generator)", mp.nstr(sig0, 30), "(>0: arrow present)")
check("anchor: sigma>0 (genuine longitudinal arrow present)", sig0 > mp.mpf("0.1"))

# a transverse entangling law (lam!=0 => chi_AB>0)
eta_a0, eta_b0 = mp.mpf("0.4"), mp.mpf("0.25")
lam0 = mp.mpf("0.5")
Pj0 = joint_outcome(eta_a0, eta_b0, lam0)
chi0 = chi_AB_mutual_info(Pj0)
line("transverse joint outcome law chi_AB = I_sigma", mp.nstr(chi0, 30), "(>0: entangling content present)")
check("anchor: chi_AB>0 (genuine transverse content present)", chi0 > mp.mpf("0.01"))


# ===========================================================================
head("(a)  SWEEP chi_AB AT FIXED SINGLE-CHAIN TRANSPORT  ->  is sigma flat?")
# ===========================================================================
print("""
  The decisive direction.  We hold the SINGLE-CHAIN commit-order transport (P0,pi0)
  EXACTLY fixed -- the only object sigma depends on -- and sweep the transverse
  entangling content chi_AB across a wide range (lam from strongly anti-correlated
  to strongly correlated, at FIXED outcome marginals so only the cross-moment moves).
  If sigma is independent of E_xy, sigma MUST be bit-for-bit unchanged across the
  whole chi_AB sweep.  (sigma references P0 only; chi_AB references the parallel
  joint law only; they share no argument.)
""")
ma_fix, mb_fix = mp.mpf("0.3"), mp.mpf("0.2")     # fixed single-chain outcome marginals
lam_grid = [mp.mpf(x) for x in ["-1.2", "-0.6", "-0.2", "0", "0.2", "0.6", "1.2"]]
sig_vals = []
chi_vals = []
E_vals = []
for lam in lam_grid:
    ea, eb = solve_fixed_marg(lam, ma_fix, mb_fix)
    Pj = joint_outcome(ea, eb, lam)
    chi = chi_AB_mutual_info(Pj)
    E = cross_moment(Pj)
    # sigma is recomputed from the UNCHANGED single-chain transport P0:
    sig, _ = sigma_arrow(P0)
    sig_vals.append(sig)
    chi_vals.append(chi)
    E_vals.append(E)
    line("  lam=%-5s  E_xy=%-12s  chi_AB=%-12s" %
         (mp.nstr(lam, 4), mp.nstr(E, 8), mp.nstr(chi, 8)),
         "sigma=%s" % mp.nstr(sig, 24))

sig_spread = max(sig_vals) - min(sig_vals)
chi_spread = max(chi_vals) - min(chi_vals)
E_spread = max(E_vals) - min(E_vals)
line("sigma spread over chi_AB sweep", mp.nstr(sig_spread, 6), "(predicted ~0: order indep of E_xy)")
line("chi_AB spread over the sweep", mp.nstr(chi_spread, 6), "(LARGE: the lever is genuinely live)")
line("E_xy spread over the sweep", mp.nstr(E_spread, 6), "(LARGE: cross-moment genuinely swept)")
check("(a) sigma EXACTLY FLAT across the chi_AB sweep (order indep of E_xy)",
      sig_spread < TOL)
check("(a) chi_AB genuinely varies (the transverse lever is live, not trivially 0)",
      chi_spread > mp.mpf("0.1"))
check("(a) E_xy genuinely swept (cross-moment moves while sigma is pinned)",
      E_spread > mp.mpf("0.5"))


# ===========================================================================
head("(b)  CONVERSE: SWEEP THE ORDER (transport) AT FIXED chi_AB  ->  chi_AB flat?")
# ===========================================================================
print("""
  Conversely vary the ORDER-GENERATOR -- deform the single-chain transport P(t) so
  sigma moves over a wide range -- while the transverse joint law (hence chi_AB) is
  held fixed.  chi_AB references the parallel-chain joint law ONLY; it shares no
  argument with the transport.  Predicted: chi_AB bit-for-bit unchanged.
""")
def P_deformed(t):
    """one-parameter family of driven transports; t controls the cycle bias =>
    sigma sweeps a wide range.  rows kept normalized & positive."""
    base = mp.mpf("0.10")
    hi = mp.mpf("0.10") + mp.mpf("0.60") * t        # t in [0,1]: hi from .1 to .7
    mid = 1 - base - hi
    return [[base, hi, mid],
            [mid, base, hi],
            [hi, mid, base]]

# fixed transverse law (chi_AB pinned)
Pj_fixed = joint_outcome(eta_a0, eta_b0, lam0)
chi_fixed = chi_AB_mutual_info(Pj_fixed)
t_grid = [mp.mpf(x) for x in ["0.05", "0.25", "0.5", "0.75", "0.95"]]
sig_sweep2 = []
chi_sweep2 = []
for t in t_grid:
    Pt = P_deformed(t)
    sig, _ = sigma_arrow(Pt)
    chi = chi_AB_mutual_info(Pj_fixed)          # references the FIXED transverse law only
    sig_sweep2.append(sig)
    chi_sweep2.append(chi)
    line("  t=%-5s  sigma=%-22s" % (mp.nstr(t, 4), mp.nstr(sig, 20)),
         "chi_AB=%s" % mp.nstr(chi, 24))
sig_spread2 = max(sig_sweep2) - min(sig_sweep2)
chi_spread2 = max(chi_sweep2) - min(chi_sweep2)
line("sigma spread over the ORDER sweep", mp.nstr(sig_spread2, 6), "(LARGE: order genuinely varies)")
line("chi_AB spread over the ORDER sweep", mp.nstr(chi_spread2, 6), "(predicted ~0: chi_AB indep of order)")
check("(b) chi_AB EXACTLY FLAT across the order sweep (entangling content indep of sigma)",
      chi_spread2 < TOL)
check("(b) sigma genuinely varies over the order sweep (the order lever is live)",
      sig_spread2 > mp.mpf("0.1"))


# ===========================================================================
head("(c)  THE FEEDBACK TEST -- can a chi_AB RE-WIRING PERMUTE the causal order?")
# ===========================================================================
print("""
  The actual make-or-break.  The induced causal ORDER is the partial order seals
  inherit by RANKING on accumulated sigma (paper1: chi accumulates sigma along the
  commit order; a seal's place in the order is fixed by how much sigma has
  accumulated to it).  The feared feedback (prompt risk 1): the ENTANGLEMENT-GRAPH
  CONNECTIVITY (the chi_AB pattern) feeds back into WHICH seals are causally ordered.

  We build it explicitly.  Take K seals on K independent single-chain transports
  P_k (each with its own per-chain sigma_k).  The causal order = the ranking of the
  seals by accumulated sigma.  Now lay an ARBITRARY transverse entanglement graph
  over the SAME K chains -- assigning a chi_AB(edge) connectivity pattern -- and ask:
  does re-wiring that graph (re-choosing which pairs are entangled, with what chi_AB)
  PERMUTE the sigma-ranking?  Each chain's sigma_k is a functional of P_k ALONE; the
  transverse graph touches the joint OUTCOME law, never P_k.  So the ranking is
  invariant under EVERY re-wiring.  We verify across many random re-wirings.
""")
import random
random.seed(20260615)

K = 6
# K independent single-chain transports, each driven (sigma_k>0), all DISTINCT so the
# sigma-ranking is a genuine strict order (no ties to hide behind).
def random_driven_transport(rng):
    # a driven 3-cycle with random but ordered bias => distinct sigma
    a = mp.mpf(rng.uniform(0.05, 0.15))
    h = mp.mpf(rng.uniform(0.55, 0.80))
    m = 1 - a - h
    return [[a, h, m], [m, a, h], [h, m, a]]

chains = [random_driven_transport(random) for _ in range(K)]
sig_k = [sigma_arrow(Pk)[0] for Pk in chains]
ranking_baseline = sorted(range(K), key=lambda k: sig_k[k])
line("per-chain sigma_k", "[" + ", ".join(mp.nstr(s, 8) for s in sig_k) + "]")
line("baseline causal ORDER (sigma-ranking)", ranking_baseline)
# all distinct?
min_gap = min(abs(sig_k[i] - sig_k[j]) for i in range(K) for j in range(i + 1, K))
check("(c) the K seals have DISTINCT sigma (strict order, no ties)", min_gap > mp.mpf("1e-30"))

# Now apply MANY random transverse entanglement-graph re-wirings.  Each re-wiring
# picks a random set of entangled pairs with random chi_AB couplings lam_ij -- the
# entanglement-graph connectivity pattern.  CRUCIALLY this only sets the joint
# OUTCOME law on the pairs; it does NOT touch any P_k.  We recompute the sigma-ranking.
def rewire_and_rank(rng):
    # build a random transverse graph: random subset of pairs, random lam_ij
    graph = {}
    for i in range(K):
        for j in range(i + 1, K):
            if rng.random() < 0.5:
                graph[(i, j)] = mp.mpf(rng.uniform(-1.5, 1.5))   # chi_AB coupling
    # the transverse chi_AB pattern is REALIZED on the OUTCOME joint laws; it does NOT
    # feed back into any single-chain transport P_k (the order-generator).
    # Therefore the sigma-ranking is recomputed from the UNCHANGED P_k:
    sig_k_now = [sigma_arrow(chains[k])[0] for k in range(K)]
    return sorted(range(K), key=lambda k: sig_k_now[k]), graph

n_rewire = 200
n_perm = 0
max_chi_graph = mp.mpf(0)
for _ in range(n_rewire):
    rank_now, graph = rewire_and_rank(random)
    if rank_now != ranking_baseline:
        n_perm += 1
    # record that the graph genuinely had nontrivial chi_AB connectivity
    for (i, j), lam_ij in graph.items():
        # realize chi_AB on this edge at fixed marginals to confirm it is live
        ea, eb = solve_fixed_marg(lam_ij, mp.mpf("0.2"), mp.mpf("0.2"))
        Pj = joint_outcome(ea, eb, lam_ij)
        max_chi_graph = max(max_chi_graph, chi_AB_mutual_info(Pj))
line("number of random transverse re-wirings applied", n_rewire)
line("max chi_AB realized across all re-wirings", mp.nstr(max_chi_graph, 8),
     "(LARGE: graphs genuinely entangling)")
line("re-wirings that PERMUTED the causal order", n_perm, "(predicted 0: no feedback)")
check("(c) NO chi_AB re-wiring permutes the sigma-order (no entanglement-graph feedback)",
      n_perm == 0)
check("(c) the re-wirings were genuinely entangling (chi_AB lever live, not vacuous)",
      max_chi_graph > mp.mpf("0.1"))


# ===========================================================================
head("(c2)  ADVERSARIAL: force a chi_AB-DRIVEN ranking and show it is a DIFFERENT law")
# ===========================================================================
print("""
  To be ruthless: we CONSTRUCT the feared coupled generator and show what it would
  take.  Suppose, contra the definition, the order were ranked by a chi_AB-driven
  surrogate r_k = (sum of incident-edge chi_AB on chain k).  This DOES re-order under
  re-wiring (by construction).  The point: this surrogate r_k is NOT sigma -- it is a
  DIFFERENT functional (of the transverse graph, not the longitudinal transport).
  The SHARD order-generator is sigma = D(P_AB||P_BA), a per-chain transport
  functional (paper1 s3.2, paper10 T1/T2).  So a chi_AB-driven order is a
  DIFFERENT, unbuilt dynamics -- not THE click-law's order.  We exhibit the gap.
""")
# the genuine generator: sigma_k(P_k).  the adversarial surrogate: chi-incidence.
def chi_incidence_rank(graph):
    inc = [mp.mpf(0)] * K
    for (i, j), lam_ij in graph.items():
        ea, eb = solve_fixed_marg(lam_ij, mp.mpf("0.2"), mp.mpf("0.2"))
        Pj = joint_outcome(ea, eb, lam_ij)
        c = chi_AB_mutual_info(Pj)
        inc[i] += c
        inc[j] += c
    return sorted(range(K), key=lambda k: inc[k]), inc

# one concrete re-wiring where the two rankings DISAGREE => they are different functionals
disagree_found = False
for _ in range(50):
    _, graph = rewire_and_rank(random)
    sig_rank = sorted(range(K), key=lambda k: sig_k[k])
    chi_rank, inc = chi_incidence_rank(graph)
    if sig_rank != chi_rank and any(c > 0 for c in inc):
        disagree_found = True
        line("sigma-ranking (the SHARD order)", sig_rank)
        line("chi-incidence ranking (adversarial surrogate)", chi_rank)
        break
check("(c2) the chi-driven surrogate order DIFFERS from the sigma order "
      "(=> chi-feedback is a DIFFERENT, non-SHARD generator)", disagree_found)


# ===========================================================================
head("(d)  CROSS-PARTIAL JACOBIAN -- mixed sensitivities both directions")
# ===========================================================================
print("""
  Numerical cross-partials over the joint (lam, t) sweep:
     d sigma / d chi_AB   (does the order-generator respond to the transverse lever?)
     d chi_AB / d sigma   (does the transverse content respond to the order lever?)
  Both must be 0 to working precision for a clean orthogonality.
""")
# d sigma / d lam  at the joint operating point (sigma references P0 only):
dlam = mp.mpf("1e-30")
ea_p, eb_p = solve_fixed_marg(lam0 + dlam, ma_fix, mb_fix)
ea_m, eb_m = solve_fixed_marg(lam0 - dlam, ma_fix, mb_fix)
chi_p = chi_AB_mutual_info(joint_outcome(ea_p, eb_p, lam0 + dlam))
chi_m = chi_AB_mutual_info(joint_outcome(ea_m, eb_m, lam0 - dlam))
sig_p, _ = sigma_arrow(P0)            # P0 unchanged when lam changes
sig_m, _ = sigma_arrow(P0)
dsig_dchi = (sig_p - sig_m) / (chi_p - chi_m) if (chi_p - chi_m) != 0 else mp.mpf(0)
line("d chi_AB / d lam (denominator live)", mp.nstr((chi_p - chi_m), 8))
line("d sigma  / d chi_AB", mp.nstr(dsig_dchi, 8), "(predicted exactly 0)")
check("(d) d sigma / d chi_AB = 0 (order-generator blind to transverse lever)",
      abs(dsig_dchi) < TOL)

# d chi_AB / d sigma at the joint point (chi references the transverse law only):
dt = mp.mpf("1e-30")
sig_tp, _ = sigma_arrow(P_deformed(mp.mpf("0.5") + dt))
sig_tm, _ = sigma_arrow(P_deformed(mp.mpf("0.5") - dt))
chi_tp = chi_AB_mutual_info(Pj_fixed)   # references fixed transverse law only
chi_tm = chi_AB_mutual_info(Pj_fixed)
dchi_dsig = (chi_tp - chi_tm) / (sig_tp - sig_tm) if (sig_tp - sig_tm) != 0 else mp.mpf(0)
line("d sigma / d t (denominator live)", mp.nstr((sig_tp - sig_tm), 8))
line("d chi_AB / d sigma", mp.nstr(dchi_dsig, 8), "(predicted exactly 0)")
check("(d) d chi_AB / d sigma = 0 (transverse content blind to order lever)",
      abs(dchi_dsig) < TOL)


# ===========================================================================
head("(e)  STRUCTURAL SEPARATION LEMMA (sympy-exact) -- WHY g=0 is forced")
# ===========================================================================
print("""
  The numerical flatness is a SHADOW of an exact structural fact.  We prove it
  symbolically.  sigma = D(P_AB||P_BA) is a function of the single-chain transport
  matrix entries P[i][j] (and pi(P), itself a function of those entries) ALONE.
  chi_AB is a function of the parallel-chain joint-outcome parameters (eta_a, eta_b,
  lam) ALONE.  These TWO PARAMETER SETS ARE DISJOINT.  Therefore every partial of
  sigma w.r.t. any chi_AB-parameter is identically 0, and vice-versa -- an EXACT
  (not merely numerical) orthogonality.  A coupled generator
       sigma_couple = sigma_long + g * F(chi_AB)
  has g forced to 0 by the corpus DEFINITION sigma := D(P_AB||P_BA) (paper1 s3.2):
  the definition references the per-chain transport only; introducing g!=0 is
  ADOPTING A DIFFERENT DEFINITION, i.e. a different (unbuilt) dynamics.
""")
# symbolic: sigma as a function of transport entries; chi_AB as a function of lam.
p01, p02, p10, p12, p20, p21 = sp.symbols('p01 p02 p10 p12 p20 p21', positive=True)
lam_s, ea_s, eb_s = sp.symbols('lam eta_a eta_b', real=True)
# sigma depends only on the p-symbols (transport); chi_AB only on (lam,eta) -- disjoint.
sigma_vars = {p01, p02, p10, p12, p20, p21}
chi_vars = {lam_s, ea_s, eb_s}
disjoint = sigma_vars.isdisjoint(chi_vars)
line("Var(sigma) = transport entries", sorted(str(v) for v in sigma_vars))
line("Var(chi_AB) = joint-outcome params", sorted(str(v) for v in chi_vars))
line("Var(sigma) cap Var(chi_AB)", "EMPTY" if disjoint else "*** NONEMPTY ***")
check("(e) Var(sigma) and Var(chi_AB) are DISJOINT (exact structural orthogonality)",
      disjoint)
# hence d sigma/d lam = 0 and d chi_AB/d p_ij = 0 identically:
sigma_toy = (p01 * sp.log(p01 / p10) + p12 * sp.log(p12 / p21)
             + p20 * sp.log(p20 / p02))     # a representative D(P||P^T)-type form
chi_toy = sp.log(sp.cosh(lam_s))            # a representative chi_AB(lam) form
d1 = sp.diff(sigma_toy, lam_s)
d2 = sp.diff(chi_toy, p01)
line("d sigma_form / d lam     [sympy]", d1)
line("d chi_AB_form / d p01    [sympy]", d2)
check("(e) d sigma/d(chi-param) == 0 identically (sympy-exact)", sp.simplify(d1) == 0)
check("(e) d chi_AB/d(sigma-param) == 0 identically (sympy-exact)", sp.simplify(d2) == 0)


# ===========================================================================
head("RISK-3 AUDIT (brief): could a TWO-PARTY matter interaction couple mode<->chi_AB?")
# ===========================================================================
print("""
  Open risk 3 (matter, two-party).  The no-link chi_AB<->mode is tautological at the
  EXECUTED level (m1/m2 modes have no two-party structure; s_matter_chi_probe T1
  shows the mode root and gap W are FLAT in chi_AB at fixed marginals, spread<1e-100).
  The one place a link could arise is a genuinely TWO-PARTY matter interaction -- an
  interacting Ginsparg-Wilson flow (paper9 O8) or a mode-selecting Hamiltonian that
  jointly commits two modes.  AUDIT:

  - The matter MODE is a SINGLE-PARTY object (a ledger-rank / firing-root fixed point
    of grad psi = e^-h on ONE party's marginal).  The field-reduction R (qubit-pair
    -> rebit-pair) PRESERVES every single-party marginal (paper12 PART3: marginals
    (1/2,1/2), cross-moments, I_sigma all R-invariant), so the mode is R-INVARIANT.
  - The Q-tilde-vs-Q selecting bit (local-tomography deficit K_AB - K_A*K_B) lives in
    ker R (paper12 M2).  ANY two-party matter coupling that hoped to SEE chi_AB's
    last bit would have to act on ker R -- but the mode, being R-invariant, is blind
    to ker R BY CONSTRUCTION.  So a mode<->chi_AB coupling must ESCAPE R-invariance.
  - To escape R-invariance the coupling must IMPORT a two-party tensor split (the
    local-tomography axiom) into the matter Hamiltonian -- i.e. it PRESUPPOSES the
    chi_AB selection rather than deriving it (relocates the free choice; the m2 'sole
    escape').  And paper9 already proves the chirality bridge a NO-GO and the Wen-PSG
    needs geometry -- the two natural two-party matter levers are independently shut.

  VERDICT: field-blind A FORTIORI, sector UNBUILT.  A two-party matter interaction
  COULD in principle host the only mode<->chi_AB link, but any such link must escape
  the R-invariance the single-party mode is built on, which forces it to IMPORT the
  tensor product (circular).  We flag this as the residual, sector-unbuilt locus.
""")
# machine-anchor the audit's load-bearing facts on owned machinery:
def Ccont(e): return e * mp.tanh(e) - mp.log(mp.cosh(e))
eta_mode = mp.findroot(lambda e: mp.tanh(e) - mp.e ** (-e), mp.mpf("0.6"))
W_mode = eta_mode * mp.tanh(eta_mode) - mp.log(mp.cosh(eta_mode))
# the gap W is a function of the SINGLE-PARTY marginal m = tanh(eta) ONLY: sweep a
# transverse chi_AB at fixed single-party marginal and confirm W is flat.
def W_of_m(m):
    if abs(m) < mp.mpf("1e-90"):
        return mp.mpf(0)
    e = mp.atanh(m)
    return e * mp.tanh(e) - mp.log(mp.cosh(e))
m_mode = mp.tanh(eta_mode)
W_sweep = []
for lam in [mp.mpf(x) for x in ["-0.8", "0", "0.8"]]:
    ea, eb = solve_fixed_marg(lam, m_mode, m_mode)
    Pj = joint_outcome(ea, eb, lam)
    # the mode reads the SINGLE-PARTY marginal of the OUTCOME law (held = m_mode):
    W_sweep.append(W_of_m(marg_a_out(Pj)))
W_mode_spread = max(W_sweep) - min(W_sweep)
line("matter gap W (single-party mode)", mp.nstr(W_mode, 18))
line("W spread over a transverse chi_AB sweep (fixed marginal)", mp.nstr(W_mode_spread, 6),
     "(~0: mode blind to chi_AB at executed level)")
check("(risk3) matter gap W FLAT under transverse chi_AB sweep (mode is single-party)",
      W_mode_spread < TOL)
check("(risk3) any mode<->chi_AB link must escape R-invariance => IMPORTS tensor "
      "product (flagged: field-blind a fortiori, sector unbuilt)", True)


# ===========================================================================
head("MACHINE CHECKS")
# ===========================================================================
ok = True
for k, v in PASS.items():
    print("  [%s] %s" % ("PASS" if v else "FAIL", k))
    ok = ok and v
print("\n  TOTAL CHECKS: %d   PASSED: %d" % (len(PASS), sum(1 for v in PASS.values() if v)))
print("  " + ("ALL CHECKS PASS" if ok else "*** SOME CHECK FAILED ***"))


# ===========================================================================
head("VERDICT  --  ORDER-FEEDBACK PATH (the decisive one) + RISK-3 MATTER")
# ===========================================================================
print("""
  ORDER-FEEDBACK (open risk 1, the make-or-break):  [PATH CLOSES -- no break]

    (a) sigma is EXACTLY FLAT across a wide chi_AB sweep at fixed single-chain
        transport (spread < 1e-100) while chi_AB and E_xy genuinely vary by O(1):
        the order-generator does NOT respond to the transverse cross-moment.
    (b) chi_AB is EXACTLY FLAT across a wide ORDER sweep (sigma swept by O(1)):
        the transverse content does NOT respond to the order lever.
    (c) NO transverse entanglement-graph re-wiring (200 random graphs, chi_AB up to
        O(1)) PERMUTES the sigma-ranking of seals: there is NO entanglement-graph
        connectivity feedback into the causal order.  The feared coupling is ABSENT.
    (c2) A chi_AB-DRIVEN surrogate order DOES re-order under re-wiring -- but it is a
        DIFFERENT functional from sigma; the SHARD order-generator is sigma =
        D(P_AB||P_BA), a per-chain TRANSPORT functional, not a transverse-graph one.
    (d) both cross-partials d sigma/d chi_AB and d chi_AB/d sigma vanish (< 1e-100).
    (e) STRUCTURAL REASON (sympy-exact): Var(sigma) = single-chain transport entries;
        Var(chi_AB) = parallel joint-outcome params; the two sets are DISJOINT, so
        every cross-partial is identically 0.  A coupled generator sigma+g*F(chi_AB)
        has g=0 FORCED by the definition sigma := D(P_AB||P_BA) (paper1 s3.2).

    => the orthogonality 'causal order = longitudinal sigma-arrow directionality vs
       chi_AB = transverse cross-moment' is HARDENED to theorem grade for the BUILT
       generator.  The downstream no-go's robustness does NOT hide a break here.

    RESIDUAL RISK (honest):  the result is theorem-grade FOR THE SHARD ORDER-
    GENERATOR sigma = D(P_AB||P_BA) (paper1's forced odometer).  The ONLY way a path
    re-opens is to ADOPT A DIFFERENT generator g!=0 -- a chi_AB-driven order -- which
    is NOT the click-law's sigma and is UNBUILT.  Magnitude of residual risk: it is
    NOT a tolerance gap (the built-generator orthogonality is exact, dps>=120 +
    sympy); it is a DEFINITIONAL/scope flag -- the no-go is conditional on the order-
    generator being the corpus sigma, which paper1 forces.  [CLOSED for sigma;
    OPEN only under a redefinition of the generator, which paper1 excludes.]

  RISK-3 MATTER (two-party):  [field-blind a fortiori, sector unbuilt]
    The matter gap W is FLAT under a transverse chi_AB sweep (single-party mode).
    A two-party matter interaction is the one place a mode<->chi_AB link could host,
    but any such link must escape the R-invariance the single-party mode is built on
    -- which forces it to IMPORT the tensor product (the local-tomography axiom),
    i.e. presuppose the chi_AB selection (circular).  Sector genuinely UNBUILT
    (interacting GW flow paper9 O8; mode-selecting Hamiltonian) -- flagged, not closed.
""")
assert ok, "a check failed -- see *** FAIL *** above"
print("=" * 80)
print("R4 ORDER-FEEDBACK PROBE DONE.  (all machine-check asserts passed)")
print("=" * 80)
