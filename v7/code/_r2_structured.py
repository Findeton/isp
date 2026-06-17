"""R2 structured-family hunt: the families most likely to produce low-KL_1d multisets.
Bent/quadratic Boolean orientations, affine-subspace indicators, Reed-Muller low-degree,
and 'second-deepest' multi-level multisets. n=5,6,7. Anything below mu* is CRITICAL."""
import itertools, numpy as np
from _r2_independent_hunt import char_matrix, altweight, seal_gap, closed_form, hadamard_sub

def probe(n, gen_orients, label):
    N=1<<n; M=N-1
    C,_=char_matrix(n); cf=float(closed_form(n))
    best=np.inf; below=0; cnt=0
    for eps in gen_orients:
        eps=np.asarray(eps,float)
        if eps.shape[0]!=M: continue
        g=seal_gap(eps,C)[0]; cnt+=1
        best=min(best,g)
        if g<cf-1e-8: below+=1
    print(f"  n={n} [{label}]: {cnt} orientations, min_gap={best:.10f}, closed_mu*={cf:.10f}, below_mu*={below}")
    return below

for n in [5,6,7]:
    N=1<<n; M=N-1
    states=list(itertools.product((-1,1),repeat=n))
    masks=list(range(1,1<<n))
    # orientation from a Boolean function f: {0,1}^n -> {0,1}; eps_a = (-1)^{f-derived}.
    # Build eps from sign patterns of low-degree GF(2) polynomials (Reed-Muller).
    # A degree-d RM codeword c(x) = sum of monomials; eps_a = (-1)^{c on mask a}? We instead
    # use: eps_a = sign assigned by parity of a random subset structure. Concretely sample many
    # structured sign vectors: (1) eps_a = (-1)^{<a,v>} affine; (2) eps_a=(-1)^{|a&w|} for fixed w;
    # (3) products thereof; (4) eps_a = (-1)^{[|a| in S]} weight-set patterns (generalizes alt).
    fams=[]
    rng=np.random.default_rng(100+n)
    # (1) affine: eps_a = (-1)^{popcount(a & v) } for all v
    aff=[]
    for v in range(N):
        aff.append([(-1)**(bin(m & v).count('1')) for m in masks])
    fams.append(("affine-linear", aff))
    # (2) weight-set patterns: eps_a = +1 if |a| in S else -1, over many subsets S of {1..n}
    wsets=[]
    for _ in range(2000):
        S=set(int(x) for x in np.nonzero(rng.integers(0,2,n+1))[0])
        wsets.append([1 if bin(m).count('1') in S else -1 for m in masks])
    # include the exact alternating (|a| parity)
    wsets.append([(-1)**(bin(m).count('1')-1) for m in masks])
    fams.append(("weight-set patterns", wsets))
    # (3) quadratic-bent-like: eps_a = (-1)^{Q(a)} for random symmetric GF(2) quadratics Q(a)=sum_{i<j}q_ij a_i a_j
    quad=[]
    for _ in range(2000):
        Q=rng.integers(0,2,(n,n)); Q=np.triu(Q,1)
        row=[]
        for m in masks:
            abits=[(m>>i)&1 for i in range(n)]
            val=0
            for i in range(n):
                for j in range(i+1,n):
                    val ^= (Q[i,j]&abits[i]&abits[j])
            row.append((-1)**val)
        quad.append(row)
    fams.append(("quadratic-bent", quad))
    tot_below=0
    for lbl,orients in fams:
        tot_below += probe(n, orients, lbl)
    if tot_below>0:
        print(f"  *** n={n}: {tot_below} STRUCTURED orientations BELOW mu* -- CRITICAL ***")
