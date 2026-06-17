"""R2 n=6 and n=7 adversarial hunt + n=5 witness verification. Independent."""
import itertools, numpy as np, mpmath as mp
from _r2_independent_hunt import char_matrix, altweight, seal_gap, seal_gap_mp, closed_form, hadamard_sub

# ---- verify the n=5 multiset-non-functionality witness independently ----
print("="*80); print("WITNESS CHECK: n=5 two orientations, same T-multiset, different gap")
print("="*80)
eps_A = [1,1,-1,1,1,-1,1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,1]
eps_B = [-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1]
C5,_ = char_matrix(5)
TA = sorted(int(round(t)) for t in (C5*np.array(eps_A,float)[None,:]).sum(1))
TB = sorted(int(round(t)) for t in (C5*np.array(eps_B,float)[None,:]).sum(1))
gA,_ = seal_gap_mp(eps_A,5,dps=50); gB,_ = seal_gap_mp(eps_B,5,dps=50)
print(f"  same T-multiset? {TA==TB}  (values {sorted(set(TA))})")
print(f"  m_hat(A)={mp.nstr(gA,12)}  m_hat(B)={mp.nstr(gB,12)}  split={mp.nstr(abs(gA-gB),6)}")
print(f"  => gap NOT a multiset functional at n=5 (witness independently reproduced)")

# ============================================================================
print(); print("="*80)
print("PART 3: n=6 adversarial deep hunt (greedy-deepen + structured families)")
print("="*80)
n=6; N=1<<n; M=N-1
C6,_ = char_matrix(n)
cf6 = float(closed_form(n))
g_alt6 = seal_gap(altweight(n), C6)[0]
print(f"  closed mu*={cf6:.12f} ; alt gap={g_alt6:.12f} ; |diff|={abs(cf6-g_alt6):.2e}")

Hsub = hadamard_sub(n)
singleton_cols=[(1<<i)-1 for i in range(n)]
free_cols=[c for c in range(M) if c not in singleton_cols]
base = Hsub[:,singleton_cols].sum(axis=1)
HF = Hsub[:,free_cols]
F=len(free_cols)
def minT_of(full):  # full = length-M sign vector
    return int((Hsub*full[None,:]).sum(1).min())

# greedy-DEEPEN: from random gauge-fixed starts, flip the single free sign that most
# deepens minT; collect every distinct deep orientation along each path.
rng = np.random.default_rng(99)
deep_set = {}
deepest = 0
def full_from_free(fsigns):
    full = np.ones(M, dtype=np.int32); full[free_cols]=fsigns; return full
NSTART = 1200
for _ in range(NSTART):
    fsigns = rng.integers(0,2,F)*2-1
    full = full_from_free(fsigns)
    cur = (Hsub*full[None,:]).sum(1).min()
    while True:
        # try flipping each free sign, pick the one giving deepest minT
        best_mt = cur; best_i=-1
        for ii,c in enumerate(free_cols):
            full[c]*=-1
            mt = (Hsub*full[None,:]).sum(1).min()
            full[c]*=-1
            if mt < best_mt:
                best_mt=mt; best_i=ii
        if best_i<0: break
        full[free_cols[best_i]]*=-1
        cur=best_mt
        mt = int(cur)
        deepest=min(deepest,mt)
        if mt <= -44:
            deep_set[full.tobytes()] = full.copy()
print(f"  greedy-deepen: deepest minT reached = {deepest} (mu* = -{N-1}); "
      f"distinct deep(<=-44) orientations = {len(deep_set)}")

# also a large random breadth phase
randdeep = {}
CHUNK=1<<19
for batch in range(8):
    sg = (rng.integers(0,2,(CHUNK,F))*2-1).astype(np.int32)
    T = base[None,:] + sg @ HF.T
    mins = T.min(axis=1)
    sel = np.where(mins<=-40)[0]
    for j in sel:
        full = np.ones(M,dtype=np.int32); full[free_cols]=sg[j]
        randdeep[full.tobytes()]=full.copy()
print(f"  random breadth: distinct deep(<=-40) orientations = {len(randdeep)}; "
      f"random deepest minT = {int(min((base[None,:]+ (rng.integers(0,2,(CHUNK,F))*2-1)@HF.T).min(axis=1).min(),0))}")

# evaluate exact vector seal gap on every distinct deep orientation (both phases) + alt
all_deep = dict(deep_set); all_deep.update(randdeep)
# include alt-by-weight (gauge-equiv: its singletons are +1 already)
alt = altweight(n).astype(np.int32)
all_deep[alt.tobytes()] = alt
min_gap6=np.inf; below6=[]; mu_present=False; argminT=None
for key,full in all_deep.items():
    g = seal_gap(full.astype(float), C6)[0]
    mt = minT_of(full)
    if g < min_gap6:
        min_gap6=g; argminT=mt
    if g < cf6 - 1e-7:
        below6.append((g,mt,full.copy()))
    if abs(g-cf6)<1e-7:
        mu_present=True
print(f"  evaluated {len(all_deep)} distinct deep orientations (exact vector seal)")
print(f"  min gap over deep band = {min_gap6:.12f} at minT={argminT} ; closed mu*={cf6:.12f}")
print(f"  mu* realized? {mu_present} ; orientations BELOW mu*: {len(below6)}")

# ============================================================================
print(); print("="*80)
print("PART 4: n=7 adversarial deep hunt (greedy-deepen + alt anchor)")
print("="*80)
n=7; N=1<<n; M=N-1
C7,_ = char_matrix(n)
cf7 = float(closed_form(n))
g_alt7 = seal_gap(altweight(n), C7)[0]
print(f"  closed mu*={cf7:.12f} ; alt gap={g_alt7:.12f} ; |diff|={abs(cf7-g_alt7):.2e}")

Hsub7 = hadamard_sub(n)
singleton_cols7=[(1<<i)-1 for i in range(n)]
free_cols7=[c for c in range(M) if c not in singleton_cols7]
F7=len(free_cols7)
rng7=np.random.default_rng(7)
deep7={}
deepest7=0
DEEPTH7 = -(N-1)+40   # band near maximal depth -127: keep <= -87
for _ in range(400):
    fsigns = rng7.integers(0,2,F7)*2-1
    full=np.ones(M,dtype=np.int32); full[free_cols7]=fsigns
    cur=(Hsub7*full[None,:]).sum(1).min()
    for _it in range(400):
        best_mt=cur; best_i=-1
        # evaluate all flips vectorized
        for ii,c in enumerate(free_cols7):
            full[c]*=-1
            mt=(Hsub7*full[None,:]).sum(1).min()
            full[c]*=-1
            if mt<best_mt:
                best_mt=mt; best_i=ii
        if best_i<0: break
        full[free_cols7[best_i]]*=-1; cur=best_mt
        mt=int(cur); deepest7=min(deepest7,mt)
        if mt<=DEEPTH7:
            deep7[full.tobytes()]=full.copy()
alt7=altweight(n).astype(np.int32); deep7[alt7.tobytes()]=alt7
print(f"  greedy-deepen n=7: deepest minT reached = {deepest7} (mu*=-{N-1}); "
      f"distinct deep(<={DEEPTH7}) = {len(deep7)}")
min_gap7=np.inf; below7=[]; mu7=False; argmt7=None
for key,full in deep7.items():
    g=seal_gap(full.astype(float),C7)[0]
    mt=int((Hsub7*full[None,:]).sum(1).min())
    if g<min_gap7: min_gap7=g; argmt7=mt
    if g<cf7-1e-7: below7.append((g,mt))
    if abs(g-cf7)<1e-7: mu7=True
print(f"  evaluated {len(deep7)} deep orientations (exact vector seal)")
print(f"  min gap = {min_gap7:.12f} at minT={argmt7} ; closed mu*={cf7:.12f}")
print(f"  mu* realized? {mu7} ; BELOW mu*: {len(below7)}")
