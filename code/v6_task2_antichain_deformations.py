"""
v6 Task 2 (HKT leg, PARTIAL): can antichain deformations on the division-event causal set carry the
hypersurface-deformation (Dirac-Schwinger) algebra?

A 'spatial slice' is a maximal antichain; equivalently the boundary of a down-set (order ideal) D.
A local 'normal deformation' (a tick of time) advances the slice by absorbing one event: the available
moves from D are the MINIMAL elements of its complement (events whose entire strict past lies in D).

The defining locality signature of the Dirac-Schwinger algebra is:
   * deformations at SPACELIKE-separated points COMMUTE (the ultralocal {H_perp(x),H_perp(y)} structure);
   * timelike-related deformations are SEQUENCED by causality.
We test exactly this on sprinkled causal sets.

HONEST SCOPE: this establishes the *commutation skeleton* only. The part that makes the algebra GR --
the metric STRUCTURE FUNCTION in {H_perp,H_perp}=g^{ij}H_j (HKT) -- is NOT obtained here; it needs the
local metric extracted from causal data (which the §4A dimension recovery shows is in principle present).
"""
import numpy as np
import itertools
rng = np.random.default_rng(5)

def run(N, theta, seed):
    r = np.random.default_rng(seed)
    uv = r.random((N, 2))                       # lightcone coords (u,v); A<B iff uA<uB and vA<vB
    pred = [set() for _ in range(N)]            # strict predecessors
    for i in range(N):
        ui, vi = uv[i]
        for j in range(N):
            if j != i and uv[j,0] < ui and uv[j,1] < vi:
                pred[i].add(j)
    comparable = lambda i, j: (uv[i,0]<uv[j,0] and uv[i,1]<uv[j,1]) or (uv[j,0]<uv[i,0] and uv[j,1]<uv[i,1])

    D = set(i for i in range(N) if uv[i,0]+uv[i,1] < theta)     # {u+v<theta} is a valid down-set
    is_avail = lambda e, Dset: (e not in Dset) and pred[e] <= Dset
    avail = [e for e in range(N) if is_avail(e, D)]

    # (1) available moves pairwise incomparable (spacelike) -> they form an antichain
    incomp = all(not comparable(a, b) for a, b in itertools.combinations(avail, 2))

    # (2) commutativity of available (spacelike) moves
    commute = True
    for e1, e2 in itertools.combinations(avail, 2):
        D1, D2 = D | {e1}, D | {e2}
        if not (is_avail(e2, D1) and is_avail(e1, D2) and (D1 | {e2}) == (D2 | {e1})):
            commute = False; break

    # (3) sequencing: a future event of an available move is NOT itself available (blocked by causality)
    seq_ok, seq_count = True, 0
    for e2 in range(N):
        if e2 in D:
            continue
        for e1 in pred[e2]:
            if e1 in avail:                      # e1 available and e1 < e2
                seq_count += 1
                if is_avail(e2, D):              # e2 must be blocked until e1 is absorbed
                    seq_ok = False
    return len(avail), incomp, commute, seq_ok, seq_count

print("="*78)
print("Task 2 (PARTIAL): antichain deformations vs the hypersurface-deformation locality skeleton")
print("="*78)
print(f"{'N':>4} {'theta':>6} | {'#moves':>6} | spacelike? | commute? | causally-sequenced? (pairs)")
all_ok = True
for N, theta, seed in [(80,0.7,1),(120,0.9,2),(120,1.0,3),(160,0.8,4),(200,1.1,5)]:
    nav, incomp, commute, seq_ok, seqc = run(N, theta, seed)
    ok = incomp and commute and seq_ok
    all_ok &= ok
    print(f"{N:>4} {theta:>6.2f} | {nav:>6} | {str(incomp):>9} | {str(commute):>7} | {str(seq_ok):>5} ({seqc} pairs)")

print()
print("="*78)
print("VERDICT (Task 2, partial)")
print("="*78)
print(f"- Across all trials: available deformations are mutually SPACELIKE and COMMUTE; timelike-related")
print(f"  deformations are SEQUENCED by the causal order.  all_checks_pass = {all_ok}")
print("- This is exactly the LOCALITY SKELETON of the Dirac-Schwinger algebra: normal deformations at")
print("  spacelike-separated points commute (the ultralocal {H_perp(x),H_perp(y)} structure), and")
print("  causal order supplies the time-ordering. The antichain-deformation moves realize it natively.")
print("- OPEN (honest): the part that makes the algebra GENERAL RELATIVITY -- the metric STRUCTURE")
print("  FUNCTION g^{ij} in {H_perp,H_perp}=g^{ij}H_j (HKT uniqueness) -- is NOT obtained here. It")
print("  requires the local metric read off from causal data (the §4A dimension recovery shows that")
print("  data is present). That quantitative step is the remaining work on the dynamics leg.")
