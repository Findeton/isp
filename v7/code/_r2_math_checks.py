"""Independent verification of the all-n math claims (A,B,D,E,F)."""
import itertools, numpy as np, sympy as sp, mpmath as mp
mp.mp.dps=140

# ---- (A) two-value identity: sum_{a!=0} (-1)^{|a|-1} prod_{i in a} s_i = -(prod_i(1-s_i)-1) ----
print("(A) two-value identity, sympy-exact:")
ok=True
for n in range(2,8):
    s=sp.symbols(f"s0:{n}")
    lhs=sum((-1)**(bin(m).count('1')-1)*sp.prod([s[i] for i in range(n) if (m>>i)&1]) for m in range(1,1<<n))
    rhs=-(sp.prod([1-s[i] for i in range(n)])-1)
    ok = ok and sp.expand(lhs-rhs)==0
print(f"  identity holds n=2..7: {ok}")
# two-value collapse: on all-minus T=-(2^n-1), else +1
tv=True
for n in range(2,8):
    for bits in itertools.product((-1,1),repeat=n):
        pr=1
        for b in bits: pr*=(1-b)
        T=-(pr-1)
        exp=-((1<<n)-1) if all(b==-1 for b in bits) else 1
        tv = tv and T==exp
print(f"  collapse {{-(2^n-1),+1}} n=2..7: {tv}")

# ---- (B) moment invariants for ARBITRARY signs ----
print("(B) moment invariants sum_s T=0, sum_s T^2=2^n(2^n-1), arbitrary signs:")
mok=True
for n in range(2,7):
    eps=sp.symbols(f"e1:{1<<n}")
    states=list(itertools.product((-1,1),repeat=n))
    masks=list(range(1,1<<n))
    def chi(m,st): 
        p=1
        for i in range(n):
            if (m>>i)&1: p*=st[i]
        return p
    Tsum=sp.expand(sum(sum(eps[k]*chi(masks[k],st) for k in range(len(masks))) for st in states))
    Tsq=sp.expand(sum(sum(eps[k]*chi(masks[k],st) for k in range(len(masks)))**2 for st in states))
    for e in eps: Tsq=Tsq.subs(e**2,1)
    Tsq=sp.expand(Tsq)
    mok = mok and Tsum==0 and Tsq==(1<<n)*((1<<n)-1)
print(f"  invariants hold (sympy, arbitrary signs) n=2..6: {mok}")

# ---- (D) data-processing: m_hat >= KL_1d on T-marginal for ALL n. Independent random n=5 test ----
print("(D) data-processing m_hat >= KL_1d(T-marginal), independent random n=5:")
from _r2_independent_hunt import char_matrix, seal_gap
from collections import defaultdict
C5,_=char_matrix(5); N5=32
rng=np.random.default_rng(555)
min_exc=1e9; max_abs=0
for _ in range(5000):
    eps=rng.integers(0,2,31)*2-1
    g,p,Tf=seal_gap(eps.astype(float),C5)
    Plev=defaultdict(float); cnt=defaultdict(int)
    for si in range(N5):
        Plev[round(Tf[si])]+=p[si]; cnt[round(Tf[si])]+=1
    kl=sum(Plev[t]*np.log(Plev[t]/(cnt[t]/N5)) for t in Plev)
    min_exc=min(min_exc,g-kl); max_abs=max(max_abs,abs(g-kl))
print(f"  min(m_hat - KL_1d) = {min_exc:.3e} (>=0 => DPI holds); max|m_hat-KL_1d|={max_abs:.3e} (equality fails at n=5)")

# ---- (E) closed-form anchors vs corpus ----
print("(E) closed-form anchors (dps=140) vs corpus:")
def exact_min(n):
    N=1<<n; M=N-1
    def fp(h):
        w0=mp.e**(-h*M); eh=mp.e**h; Z=w0+M*eh
        return (w0*(-1)+eh)/Z - mp.e**(-h)
    h=mp.findroot(fp,mp.log(mp.mpf(M)))
    w0=mp.e**(-h*M); eh=mp.e**h; Z=w0+M*eh
    return h*(M*mp.e**(-h))-mp.log(Z/N)
for n,corpus in [(2,"0.266653365180"),(3,"0.133530982072"),(4,"0.064538521138"),(5,"0.031748698315")]:
    v=exact_min(n)
    print(f"  n={n}: {mp.nstr(v,15)}  corpus {corpus}  match={abs(v-mp.mpf(corpus))<mp.mpf('1e-11')}")
# prefactor -> 1
print(f"  m_min(40)*2^40 = {mp.nstr(exact_min(40)*2**40,12)} (->1)")

# ---- (F) two-point family: a*b=N-1 and minimizer extreme. Independent check ----
print("(F) two-point family minimizer over divisors:")
def scalar_gap_2pt(a_,b_,k_,N,M):
    a_,b_,k_=mp.mpf(a_),mp.mpf(b_),mp.mpf(k_)
    def seal(h):
        za=h*(-a_); zb=h*b_; mx=max(za,zb)
        wa=mp.e**(za-mx); wb=mp.e**(zb-mx); Z=k_*wa+(N-k_)*wb
        return (k_*wa*(-a_)+(N-k_)*wb*b_)/Z - M*mp.e**(-h)
    lo,hi=mp.mpf("1e-12"),mp.mpf("120"); flo=seal(lo)
    for _ in range(300):
        mid=(lo+hi)/2; fm=seal(mid)
        if flo*fm<=0: hi=mid
        else: lo=mid; flo=fm
    h=(lo+hi)/2
    za=h*(-a_); zb=h*b_; mx=max(za,zb)
    wa=mp.e**(za-mx); wb=mp.e**(zb-mx); Z=k_*wa+(N-k_)*wb
    Pa=wa/Z; Pb=wb/Z
    return k_*Pa*mp.log(Pa*N)+(N-k_)*Pb*mp.log(Pb*N)
allok=True
for n in range(2,13):
    N=2**n; M=N-1; cands=[]
    for av in range(1,N):
        if (N-1)%av==0:
            bv=(N-1)//av
            if (N*bv)%(av+bv)==0:
                kv=(N*bv)//(av+bv)
                if 1<=kv<=N-1:
                    cands.append((av,bv,kv,scalar_gap_2pt(av,bv,kv,N,M)))
    by_g=sorted(cands,key=lambda x:x[3])
    by_a=sorted(cands)
    is_min=by_g[0][:3]==(N-1,1,1)
    dec=all(by_a[i][3]>by_a[i+1][3] for i in range(len(by_a)-1))
    allok = allok and is_min and dec
    if n<=6 or not (is_min and dec):
        print(f"  n={n}: #cands={len(cands)} argmin={by_g[0][:3]} is_mu*={is_min} dec_in_a={dec}")
print(f"  two-point: mu* is minimizer & gap decreasing in a, n=2..12: {allok}")
