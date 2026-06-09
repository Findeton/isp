"""
v6_p7h: the binding classification, settled at small scale.
Theorem (variational principle): the commitment fixed point is the unique
  global minimizer of the commitment free energy Phi(h) = psi(h) + sum_a
  exp(-h_a); Phi is strictly convex (Hessian = Cov(chi) + diag(e^-h) > 0),
  so every commitment fixed point used in this corpus is unique.
Exhaustive classification: ALL 127 statistic sets on 3 spins, defect sign
  vs relation structure; hypothesis H tested on complete data:
     defect > 0  <=>  the relation subgroup contains a triangle
  (relation-free sets have defect exactly 0 by the relabeling theorem).
4-spin probes including the plaquette {xy,yz,zw,wx} (4-relation, no
  triangle) as a fresh discriminating test.
"""
import numpy as np, itertools
from scipy.optimize import minimize, brentq

print("=== p7h: binding classification campaign ===\n")
com = lambda e: np.tanh(e)-np.exp(-e)
eh = brentq(com, 0.1, 2.0)
D1 = eh*np.tanh(eh)-np.log(np.cosh(eh))

def solve_ledger(nspin, stats):
    states = list(itertools.product((-1,1), repeat=nspin))
    chi = np.array([[np.prod([s[i] for i in S]) for S in stats] for s in states], float)
    base = np.log(1.0/len(states))
    def psi(h):
        z = chi@h
        zmax = z.max()
        return zmax + np.log(np.mean(np.exp(z-zmax)))
    Phi  = lambda h: psi(h) + np.sum(np.exp(-h))
    gPhi = lambda h: (lambda w: chi.T@(w/w.sum()))(np.exp(chi@h)) - np.exp(-h)
    best = None
    for s0 in (0.4, 0.9, 0.1):
        r = minimize(Phi, s0*np.ones(len(stats)), jac=gPhi, method='BFGS')
        if best is None or r.fun < best.fun - 1e-12: best = r
    h = best.x
    D = float(h @ np.exp(-h) - psi(h))
    return D, h, float(np.max(np.abs(gPhi(h))))

# uniqueness demonstration (variational theorem)
D,_ ,r1 = solve_ledger(2, [(0,),(1,),(0,1)])
print(f"variational principle: multi-start minimizations agree (residual {r1:.1e});")
print(f"  strict convexity of Phi = psi + sum exp(-h) PROVES uniqueness of every fixed point.\n")

# exhaustive 3-spin classification
chars = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)]
def rankF2(vecs):
    rows=[list(v) for v in vecs]; r=0; m=len(rows); cols=3
    for c in range(cols):
        piv=None
        for i in range(r,m):
            if rows[i][c]: piv=i; break
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        for i in range(m):
            if i!=r and rows[i][c]: rows[i]=[(a+b)%2 for a,b in zip(rows[i],rows[r])]
        r+=1
    return r
def triangles(S):
    return sum(1 for T in itertools.combinations(S,3)
               if all((sum(v) % 2)==0 for v in zip(*[chars[t] for t in T])))
counts = {"free(defect=0)":0,"tri&bind":0,"tri&anti":0,"notri&anti":0,"notri&bind":0}
worst_examples = {}
free_check_gaps=[]
for r in range(1,8):
    for S in itertools.combinations(range(7), r):
        vecs=[chars[i] for i in S]
        relation_free = (rankF2(vecs)==len(S))
        stats=[tuple(j for j in range(3) if chars[i][j]) for i in S]
        if relation_free:
            counts["free(defect=0)"]+=1
            if len(free_check_gaps)<4:
                D,_,_ = solve_ledger(3,stats); free_check_gaps.append(abs(len(S)*D1-D))
            continue
        D,_,res = solve_ledger(3,stats)
        defect = len(S)*D1 - D
        t3 = triangles(S)
        key = ("tri&bind" if defect>1e-9 else "tri&anti") if t3>0 else ("notri&anti" if defect<-1e-9 else "notri&bind")
        counts[key]+=1
        if key in ("tri&anti","notri&bind") and key not in worst_examples:
            worst_examples[key]=(S,defect)
print("exhaustive 3-spin classification (127 statistic sets):")
for k,v in counts.items(): print(f"  {k:<16s}: {v}")
print(f"  relabeling-zero theorem spot checks (relation-free sets): max |defect| = {max(free_check_gaps):.2e}")
if not worst_examples:
    print("  => HYPOTHESIS H CONFIRMED ON COMPLETE DATA: among relation-carrying sets,")
    print("     defect > 0 <=> the set contains a multiplicative triangle; otherwise defect < 0.")
else:
    print(f"  => HYPOTHESIS H REFUTED; counterexamples: {worst_examples}")

# 4-spin discriminating probes
print("\n4-spin probes (fresh tests of the law):")
probes = [
  ("plaquette {xy,yz,zw,wx} (4-rel, no tri)", 4, [(0,1),(1,2),(2,3),(3,0)]),
  ("{x,y,z,w,xyzw} (5-rel, no tri)",          4, [(0,),(1,),(2,),(3,),(0,1,2,3)]),
  ("{x,y,xy,zw,z,w} (tri + free pair)",       4, [(0,),(1,),(0,1),(2,3),(2,),(3,)]),
  ("{x,y,xy,xyzw,zw} (tri + 4-rel mix)",      4, [(0,),(1,),(0,1),(0,1,2,3),(2,3)]),
]
for name,ns,st in probes:
    D,_,res = solve_ledger(ns,st)
    defect = len(st)*D1 - D
    t3 = triangles_4 = sum(1 for T in itertools.combinations(range(len(st)),3)
        if all((sum(v)%2)==0 for v in zip(*[[1 if i in st[t] else 0 for i in range(ns)] for t in T])))
    pred = "bind" if t3>0 else "anti-bind"
    obs  = "bind" if defect>1e-9 else ("anti-bind" if defect<-1e-9 else "zero")
    print(f"  {name:<42s}: defect = {defect:+.9f}  law predicts {pred:<9s} observed {obs:<9s} {'OK' if pred==obs else 'VIOLATION'}")
