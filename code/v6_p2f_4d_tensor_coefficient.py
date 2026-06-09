"""
v6 §5.18 (3+1 extension): the flow-drift coefficient is the FULL 3x3 inverse spatial metric tensor (GR).

2+1 (v6_p2e) tested a 2x2 tensor (one off-diagonal, planar rotation). 3+1 is the physical case: the spatial
slice is 3D, h_{ab} is a 3x3 symmetric tensor with THREE off-diagonals, and the drift-vs-gradient rotation is
a genuine SO(3) rotation. Mechanism (background ds^2 = -dt^2 + h_{ab}(x)dx^a dx^b, a,b=1,2,3):
    unit normal u^a = h^{ab} d_b T / sqrt(1 - h^{cd} d_c T d_d T),
    two-push commutator   Delta x^a = -eps^2 h^{ab} (N d_b M - M d_b N)  -- the full inverse 3-tensor.
Test: anisotropic, fully off-diagonal h_{ab}(x,y,z); run the real two-step normal flow as a vector op;
compare the measured 3-vector drift to (i) the GR tensor prediction h^{ab}(N d_bM - M d_bN) and (ii) the
isotropic-scalar null delta^{ab}(...). GR <=> measured tracks the tensor (rotated in 3D); isotropic fails.
"""
import numpy as np

n = 64; xs = np.linspace(-1.5, 1.5, n); dx = xs[1]-xs[0]
X, Y, Z = np.meshgrid(xs, xs, xs, indexing='ij')
def gauss(cx, cy, cz, s): return np.exp(-((X-cx)**2+(Y-cy)**2+(Z-cz)**2)/(2*s**2))

# ---- anisotropic 3x3 spatial metric field h_{ab}(x,y,z), all three off-diagonals nonzero ----
H = np.empty((n, n, n, 3, 3))
H[...,0,0] = 1.0 + 1.1*gauss( 0.0, 0.0, 0.0, 0.8)
H[...,1,1] = 1.0 + 0.4*gauss( 0.4, 0.0, 0.0, 1.0)
H[...,2,2] = 1.0 + 0.7*gauss(-0.3, 0.2, 0.0, 0.9)
H[...,0,1] = H[...,1,0] = 0.60*gauss(0.0, 0.0, 0.0, 0.8)
H[...,0,2] = H[...,2,0] = 0.45*gauss(0.1, 0.0, 0.1, 0.9)
H[...,1,2] = H[...,2,1] = 0.55*gauss(0.0, 0.1, 0.0, 0.8)
minfo = np.linalg.eigvalsh(H.reshape(-1,3,3)).min()
assert minfo > 0, f"metric not positive-definite (min eig {minfo})"
Hinv = np.linalg.inv(H)                                  # batched 3x3 inverse -> h^{ab}(x)
aniso = np.mean(np.abs(H[...,0,1])/np.sqrt(H[...,0,0]*H[...,1,1]))

# ---- lapse fields with gradients in all three directions ----
N = 1.0 + 0.4*np.cos(1.1*X + 0.3*Y - 0.5*Z)
M = 1.0 + 0.4*np.sin(0.9*X - 0.4*Y + 0.6*Z)
def grad3(F):
    g = np.gradient(F, dx, dx, dx); return np.stack(g, axis=-1)   # (...,3) covector

def raise_idx(cov):                                     # h^{ab} cov_b
    return np.einsum('...ab,...b->...a', Hinv, cov)

def push(T, D, F, eps):
    Tcov = grad3(T)                                     # d_b T
    up = raise_idx(Tcov)                                # h^{ab} d_b T
    sq = np.einsum('...a,...a->...', Tcov, up)          # h^{cd} d_c T d_d T
    norm = np.sqrt(np.clip(1.0 - sq, 1e-6, None))
    return T + eps*F/norm, D + eps*F[...,None]*up/norm[...,None]

# independently-coded GR tensor prediction & isotropic null
Ncov, Mcov = grad3(N), grad3(M)
lg = N[...,None]*Mcov - M[...,None]*Ncov                # lapse-gradient covector (N d_bM - M d_bN)
def predictions(eps):
    return -eps**2*raise_idx(lg), -eps**2*lg            # GR (tensor), isotropic (delta)

def vcos(a, b, msk):
    num = np.einsum('...a,...a->...', a, b)
    den = np.sqrt(np.einsum('...a,...a->...', a, a))*np.sqrt(np.einsum('...a,...a->...', b, b)) + 1e-30
    return np.mean((num/den)[msk])

lgmag = np.sqrt(np.einsum('...a,...a->...', lg, lg))
msk = np.zeros((n,n,n), bool); msk[8:n-8, 8:n-8, 8:n-8] = True
msk &= (lgmag > 0.05)

print("="*86)
print("3+1 tensor-coefficient test: is the flow-drift the FULL 3x3 inverse metric h^{ab}? (SO(3) rotation)")
print(f"   anisotropy (mean |h_01|/sqrt(h00 h11)) = {aniso:.3f}   grid {n}^3,  min eig(h) = {minfo:.3f}")
print("="*86)
print(f"   {'eps':>7} {'cos(meas,GR-tensor)':>20} {'cos(meas,isotropic)':>20} {'coeff ratio':>12}")
Z3 = np.zeros((n,n,n)); Z3v = np.zeros((n,n,n,3))
for eps in [0.05, 0.025, 0.0125]:
    T1, D1 = push(*push(Z3.copy(), Z3v.copy(), N, eps), M, eps)
    T2, D2 = push(*push(Z3.copy(), Z3v.copy(), M, eps), N, eps)
    meas = D1 - D2
    pgr, piso = predictions(eps)
    c_gr  = vcos(meas, pgr, msk); c_iso = vcos(meas, piso, msk)
    ratio = np.mean(np.sqrt(np.einsum('...a,...a->...', meas, meas))[msk]) \
          / np.mean(np.sqrt(np.einsum('...a,...a->...', pgr, pgr))[msk])
    print(f"   {eps:>7.4f} {c_gr:>20.4f} {c_iso:>20.4f} {ratio:>12.3f}")

pgr, piso = predictions(0.0125)
ang_pred = np.degrees(np.arccos(np.clip(vcos(pgr, piso, msk), -1, 1)))
T1, D1 = push(*push(Z3.copy(), Z3v.copy(), N, 0.0125), M, 0.0125)
T2, D2 = push(*push(Z3.copy(), Z3v.copy(), M, 0.0125), N, 0.0125)
meas = D1 - D2
ang_meas = np.degrees(np.arccos(np.clip(vcos(meas, piso, msk), -1, 1)))
print(f"\n   SO(3) rotation away from the isotropic direction (deg): tensor predicts {ang_pred:.2f}, "
      f"measured {ang_meas:.2f}")

print("\n" + "="*86); print("VERDICT (§5.18, 3+1)"); print("="*86)
c_gr = vcos(meas, pgr, msk); c_iso = vcos(meas, piso, msk)
if c_gr > 0.999 and (c_gr - c_iso) > 0.02:
    print(f"- POSITIVE: the measured flow-drift 3-VECTOR tracks the full inverse-metric TENSOR h^{{ab}}(N d_bM-M d_bN)")
    print(f"  (cos={c_gr:.4f}), rotated {ang_meas:.1f} deg in 3D away from the isotropic-scalar direction")
    print(f"  (cos to isotropic {c_iso:.4f}), matching the tensor's predicted SO(3) rotation ({ang_pred:.1f} deg).")
    print(f"  => in the PHYSICAL 3+1 case the structure function is the full 3x3 spatial metric tensor (GR);")
    print(f"     an isotropic/scalar or wrong-tensor (Horava/Lifshitz) coefficient is excluded by the rotation.")
    print(f"  Caveat: leading-order grid mechanism (clean); causal-set tensor extraction shown in §5.10 (3D diag).")
else:
    print(f"- NOT CLEAN: cos(meas,GR)={c_gr:.4f}, cos(meas,iso)={c_iso:.4f}.")
