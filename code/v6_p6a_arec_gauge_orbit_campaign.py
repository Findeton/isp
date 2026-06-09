"""
v6_p6a: A_rec gauge-orbit campaign.
Tests whether the rescaling A_rec -> lambda*A_rec is detectable by ANY intrinsic
sealed-record readout, or whether it is a unit-gauge symmetry.
"""
import numpy as np, itertools, json

W_STAR  = 0.364784952089977          # primitive deletion work (paper 4 sec 5)
ETA_C   = 0.6093778634360061         # commitment root tanh(eta)=exp(-eta)
H_LEDGER= 0.4950532643315756         # coupled (x,y,xy) commitment fixed point
KAPPA_HAT = 2*np.pi                  # record-unit coupling (derived in p6c)

def build_model(A_rec):
    m = {}
    N = 8
    m['N'] = N
    m['capacity'] = np.ones(N)                       # 1 nat per atom (intrinsic)
    m['E'] = np.array([1,0,0,1,0,1,0,0], float)      # event support (intrinsic)
    # collar ring Laplacian (intrinsic)
    A = np.zeros((N,N))
    for i in range(N):
        A[i,(i+1)%N]=A[(i+1)%N,i]=1
    L = np.diag(A.sum(1)) - A
    m['L'] = L
    # deletion source (intrinsic)
    rho = W_STAR*(m['E']-m['E'].mean())
    m['rho'] = rho
    # record-unit response: L phi = kappa_hat * rho, sum phi = 0  (intrinsic)
    Laug = L + np.ones((N,N))/N
    phi = np.linalg.solve(Laug, KAPPA_HAT*rho)
    phi -= phi.mean()
    m['phi'] = phi
    # future stochastic law K_phi (intrinsic)
    K0 = A/A.sum(1, keepdims=True)
    K = K0*np.exp(-(phi[None,:]-phi[:,None])/2)
    K = K/K.sum(1, keepdims=True)
    m['K'] = K
    # whole-history law on (x,y) with stats (x,y,xy), commitment coefficients (intrinsic)
    states=[(x,y) for x in (-1,1) for y in (-1,1)]
    chi=np.array([[x,y,x*y] for (x,y) in states],float)
    h=np.array([H_LEDGER]*3)
    w=np.exp(chi@h)/4.0
    m['P_hist']=w/w.sum()
    # Born screen (intrinsic)
    a=np.array([1.0, np.exp(1j*np.pi/3)])/np.sqrt(2)
    m['born']=np.abs(a)**2/np.sum(np.abs(a)**2)
    m['interf']=np.abs(a.sum())**2/2
    # Z_perp normal boost holonomy labels (intrinsic)
    m['Z_perp']=np.array([+1,-1,+1,+1,-1,+1,-1,-1],float)
    # ---- continuum labels (the ONLY place A_rec enters) ----
    m['A_rec']=A_rec
    S1=list(range(0,4)); S2=list(range(4,8))
    m['A_op_S1']=A_rec*m['capacity'][S1].sum()
    m['A_op_S2']=A_rec*m['capacity'][S2].sum()
    m['A_op_tot']=A_rec*m['capacity'].sum()
    m['sigma_A']=m['capacity'].sum()/m['A_op_tot']          # = 1/A_rec
    m['kappa_cont']=KAPPA_HAT/m['sigma_A']                  # = 2pi*A_rec
    m['curv_density']=(L@phi)/ (A_rec*m['capacity'])        # curvature per continuum area
    return m

def intrinsic_battery(m):
    """Everything a sealed observer can read without an external ruler."""
    return {
        'P_hist': m['P_hist'],
        'born_weights': m['born'],
        'interference': np.array([m['interf']]),
        'K_phi_rows': m['K'].ravel(),
        'rho': m['rho'],
        'phi_record': m['phi'],
        'record_curvature': m['L']@m['phi'],
        'capacity_ratio_S1_S2': np.array([4.0/4.0]),
        'AREA_RATIO_S1_S2': np.array([m['A_op_S1']/m['A_op_S2']]),   # lambda cancels
        'AREA_RATIO_S1_tot': np.array([m['A_op_S1']/m['A_op_tot']]),
        'coupling_product_kappa_sigma': np.array([m['kappa_cont']*m['sigma_A']]),
        'eta_commit': np.array([ETA_C]),
        'W_star': np.array([W_STAR]),
        'Z_perp': m['Z_perp'],
    }

def kl_rows(K, K0):
    mask = K0 > 0
    return float(np.sum(K[mask]*np.log(K[mask]/K0[mask])))

def covariant_battery(m):
    return {
        'A_op_total (+1)': m['A_op_tot'],
        'sigma_A (-1)':    m['sigma_A'],
        'kappa_cont (+1)': m['kappa_cont'],
        'curv_density (-1)': float(np.abs(m['curv_density']).max()),
    }

base = build_model(A_rec=1.0)
N=base['N']
A=np.zeros((N,N))
for i in range(N): A[i,(i+1)%N]=A[(i+1)%N,i]=1
K0 = A/A.sum(1,keepdims=True)

print("=== p6a: A_rec gauge-orbit campaign ===\n")
results={}
for lam in (3.0, 0.25):
    other = build_model(A_rec=lam)
    bi, bo = intrinsic_battery(base), intrinsic_battery(other)
    bi['KL_work_K0_to_K']=np.array([kl_rows(base['K'],K0)])
    bo['KL_work_K0_to_K']=np.array([kl_rows(other['K'],K0)])
    gaps = {k: float(np.max(np.abs(bi[k]-bo[k]))) for k in bi}
    max_gap = max(gaps.values())
    print(f"lambda = {lam}: intrinsic readouts tested = {len(gaps)}, max |gap| = {max_gap:.3e}")
    results[f'intrinsic_max_gap_lambda_{lam}']=max_gap
    cb, co = covariant_battery(base), covariant_battery(other)
    for k in cb:
        w = +1 if '(+1)' in k else -1
        ratio = co[k]/cb[k]
        pred  = lam**w
        print(f"   covariant {k:<22s}: ratio={ratio:.6f}  predicted lambda^{w:+d}={pred:.6f}  gap={abs(ratio-pred):.2e}")
        results[f'cov_{k}_gap_lambda_{lam}']=abs(ratio-pred)
    print()

# --- isomorphism / dissolved Feynman split ---------------------------------
mA, mB = build_model(1.0), build_model(3.0)
record_keys = ['capacity','E','L','rho','phi','K','P_hist','born','Z_perp']
iso_gap = max(float(np.max(np.abs(np.asarray(mA[k])-np.asarray(mB[k])))) for k in record_keys)
print(f"isomorphism check: identity map on atoms, max gap over ALL record-level data = {iso_gap:.3e}")
print("=> the Paper-5 sigma_A counterfamily members are ISOMORPHIC as sealed record theories;")
print("   no intrinsic chi exists with chi(q0)!=chi(q1); the 'split' lives only in the unit label.\n")

# --- external-ruler attack --------------------------------------------------
METER2 = 0.737   # an external lab standard, NOT a record datum
attack_A = mA['A_op_tot']/METER2
attack_B = mB['A_op_tot']/METER2
print(f"external-ruler attack: A_op/meter^2 = {attack_A:.6f} vs {attack_B:.6f}  (detects lambda)")
print("=> the only observables that detect lambda import a non-record standard: FAILS-INTRINSICITY (as required)\n")

# --- finite invariant-ring (Buckingham-pi) ----------------------------------
# scaling weights of (A_rec, A1, A2, A3, sigma_A, kappa) = (1,1,1,1,-1,1)
import itertools as it
wts = {'A_rec':1,'A1':1,'A2':1,'A3':1,'sigma':-1,'kappa':1}
names=list(wts); inv=[]; noninv=[]
for exps in it.product(range(-2,3),repeat=len(names)):
    if all(e==0 for e in exps): continue
    w=sum(e*wts[n] for e,n in zip(exps,names))
    (inv if w==0 else noninv).append(exps)
print(f"invariant-ring scan over monomials with exponents in [-2,2]: invariant={len(inv)}, non-invariant={len(noninv)}")
sample=[dict(zip(names,e)) for e in inv[:4]]
print("sample invariants (all are ratio/product-of-weight-zero):")
for s in sample: print("  ", {k:v for k,v in s.items() if v!=0})
print("=> a monomial readout is lambda-invariant iff its total area-weight is zero: ratios and kappa*sigma only.")
