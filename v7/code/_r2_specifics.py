"""Verify specific numeric claims in the paper text."""
import numpy as np
from _r2_independent_hunt import char_matrix, altweight, seal_gap, closed_form, hadamard_sub

# n=6: paper claims next-best gap at minT=-61 is ~0.7165, far above mu*=0.0157
n=6; N=1<<n; M=N-1
C,_=char_matrix(n); cf=float(closed_form(n))
Hsub=hadamard_sub(n)
singleton_cols=[(1<<i)-1 for i in range(n)]
free_cols=[c for c in range(M) if c not in singleton_cols]
base=Hsub[:,singleton_cols].sum(axis=1); HF=Hsub[:,free_cols]; F=len(free_cols)
rng=np.random.default_rng(2)
# greedy-deepen to collect orientations at minT in [-63..-55]
band={}
for _ in range(800):
    fs=rng.integers(0,2,F)*2-1
    full=np.ones(M,dtype=np.int32); full[free_cols]=fs
    cur=(Hsub*full[None,:]).sum(1).min()
    while True:
        best_mt=cur; bi=-1
        for ii,c in enumerate(free_cols):
            full[c]*=-1; mt=(Hsub*full[None,:]).sum(1).min(); full[c]*=-1
            if mt<best_mt: best_mt=mt; bi=ii
        if bi<0: break
        full[free_cols[bi]]*=-1; cur=best_mt
        mt=int(cur)
        if mt<=-55: band.setdefault(mt,{})[full.tobytes()]=full.copy()
# evaluate min gap per depth level
print("n=6 min gap by minT level (greedy-deepen band):")
for mt in sorted(band):
    gaps=[seal_gap(f.astype(float),C)[0] for f in band[mt].values()]
    print(f"  minT={mt}: count={len(gaps)} min_gap={min(gaps):.6f}")
print(f"  closed mu*={cf:.6f}")

# n=5: smallest non-mu* gap claim 0.2436
n=5; N=1<<n; M=N-1
C5,_=char_matrix(n); cf5=float(closed_form(n))
Hsub5=hadamard_sub(n)
sc5=[(1<<i)-1 for i in range(n)]; fc5=[c for c in range(M) if c not in sc5]
base5=Hsub5[:,sc5].sum(axis=1); HF5=Hsub5[:,fc5]; F5=len(fc5)
# enumerate deep band minT<=-25 (paper's threshold), find smallest gap strictly above mu*
bitw=np.arange(F5,dtype=np.uint64); CHUNK=1<<22; total=1<<F5
gaps_nonmu=[]
for start in range(0,total,CHUNK):
    end=min(start+CHUNK,total)
    idx=np.arange(start,end,dtype=np.uint64)
    bits=((idx[:,None]>>bitw[None,:])&1).astype(np.int32); sg=bits*2-1
    T=base5[None,:]+sg@HF5.T; mins=T.min(axis=1)
    sel=np.where(mins<=-25)[0]
    for j in sel:
        full=np.ones(M,dtype=np.int32); full[fc5]=sg[j]
        g=seal_gap(full.astype(float),C5)[0]
        if g>cf5+1e-7: gaps_nonmu.append(g)
print(f"\nn=5 smallest non-mu* gap in deep band (minT<=-25) = {min(gaps_nonmu):.6f} (paper claims ~0.2436)")
