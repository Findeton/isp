"""R2 near-alternating + structured perturbation probe at n=5,6,7. The non-multiset-
functionality means we must probe ORIENTATIONS, not just multisets. Specifically attack
orientations near mu*'s deep basin and single/double-flip neighborhoods of alt."""
import itertools, numpy as np
from _r2_independent_hunt import char_matrix, altweight, seal_gap, closed_form, hadamard_sub

for n in [5,6,7]:
    N=1<<n; M=N-1
    C,_=char_matrix(n)
    cf=float(closed_form(n))
    alt=altweight(n).astype(int)
    g_alt=seal_gap(alt.astype(float),C)[0]
    Hsub=hadamard_sub(n)
    def minT(full): return int((Hsub*full[None,:]).sum(1).min())
    # 1-flip and 2-flip neighbors of alt
    best=np.inf; below=0; nch=0
    # all single flips
    for i in range(M):
        e=alt.copy(); e[i]*=-1
        g=seal_gap(e.astype(float),C)[0]; nch+=1
        best=min(best,g)
        if g<cf-1e-8: below+=1
    # random double flips
    rng=np.random.default_rng(31+n)
    for _ in range(3000):
        e=alt.copy()
        ij=rng.choice(M,size=2,replace=False); e[ij]*=-1
        g=seal_gap(e.astype(float),C)[0]; nch+=1
        best=min(best,g)
        if g<cf-1e-8: below+=1
    # random triple flips
    for _ in range(3000):
        e=alt.copy()
        ij=rng.choice(M,size=3,replace=False); e[ij]*=-1
        g=seal_gap(e.astype(float),C)[0]; nch+=1
        best=min(best,g)
        if g<cf-1e-8: below+=1
    print(f"n={n}: alt_gap={g_alt:.12f} closed={cf:.12f} ; near-alt neighborhood "
          f"({nch} perturbations: all 1-flips + random 2/3-flips): min={best:.12f} below_mu*={below}")
