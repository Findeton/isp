"""
v6 §5.18 (2+1 extension): is the flow-drift coefficient the full inverse spatial TENSOR g^{ij} (GR), or only
its trace/scalar part? 2D (§5.18) is degenerate -- the spatial slice is 1D so g^{xx} is a SCALAR; it cannot
test anisotropy / off-diagonal (rotation), which is exactly where a Horava/Lifshitz structure function
differs. Here we test 2+1, where the slice is 2D and h^{ab} is a genuine 2x2 tensor.

Analytic mechanism (background ds^2 = -dt^2 + h_{ab}(x)dx^a dx^b, slice t=T(x^a)):
  future unit normal  u^a = h^{ab} d_b T / sqrt(1 - h^{cd} d_c T d_d T)
  two normal pushes (proper-time eps*lapse), commutator of the tangential drift:
     Delta x^a = -eps^2 h^{ab} (N d_b M - M d_b N).
  => coefficient = the FULL inverse spatial tensor h^{ab}. When h^{ab} is anisotropic/off-diagonal the drift
  VECTOR is rotated away from the lapse-gradient covector -- the genuinely 2+1 content 2D cannot see.

Test: position-dependent anisotropic metric with OFF-DIAGONAL terms. Implement the two-step normal flow as a
real vector operation (NOT by writing the formula), then compare the measured drift vector to (i) the GR
tensor prediction h^{ab}(N d_bM - M d_bN) and (ii) an ISOTROPIC-scalar null delta^{ab}(...). GR <=> measured
tracks the tensor (rotated); the isotropic null fails (unrotated) wherever h is anisotropic.
"""
import numpy as np
rng = np.random.default_rng(0)

# ---- grid ----
n = 221; xs = np.linspace(-2.0, 2.0, n); dx = xs[1]-xs[0]
X, Y = np.meshgrid(xs, xs, indexing='ij')

# ---- anisotropic, position-dependent spatial metric h_{ab}(x,y) with OFF-DIAGONAL ----
hxx = 1.0 + 1.4*np.exp(-(X**2+Y**2)/(2*0.9**2))
hyy = 1.0 + 0.2*np.exp(-(((X-0.5)**2+Y**2))/(2*1.1**2))
hxy = 0.85*np.exp(-(X**2+Y**2)/(2*0.8**2))          # strong off-diagonal => large rotation; positivity checked
det = hxx*hyy - hxy**2
assert (det > 0).all() and (hxx > 0).all(), "metric not positive-definite"
# inverse 2x2 tensor field h^{ab}
ixx =  hyy/det; iyy =  hxx/det; ixy = -hxy/det
aniso = np.mean(np.abs(hxy)/np.sqrt(hxx*hyy))       # how off-diagonal it is (0 = isotropic-diagonal)

# ---- lapse fields with gradients in both directions ----
N = 1.0 + 0.4*np.cos(1.1*X + 0.3*Y)
M = 1.0 + 0.4*np.sin(0.9*X - 0.4*Y)
def grad(F):
    Fx, Fy = np.gradient(F, dx, dx); return Fx, Fy

def push(T, DXf, DYf, F, eps):
    Tx, Ty = grad(T)
    gx = ixx*Tx + ixy*Ty                            # raise index: h^{ab} d_b T
    gy = ixy*Tx + iyy*Ty
    norm = np.sqrt(np.clip(1.0 - (Tx*gx + Ty*gy), 1e-6, None))
    return (T + eps*F/norm, DXf + eps*F*gx/norm, DYf + eps*F*gy/norm)

print("="*84)
print("2+1 tensor-coefficient test: does the flow-drift carry the full inverse metric h^{ab}?")
print(f"   anisotropy of h (mean |h_xy|/sqrt(h_xx h_yy)) = {aniso:.3f}   (0 => no rotation to detect)")
print("="*84)

# independently-coded GR tensor prediction and isotropic-scalar null
Nx, Ny = grad(N); Mx, My = grad(M)
lgx = N*Mx - M*Nx; lgy = N*My - M*Ny                # lapse-gradient covector (N d_b M - M d_b N)
def predictions(eps):
    px = -eps**2*(ixx*lgx + ixy*lgy); py = -eps**2*(ixy*lgx + iyy*lgy)   # GR: h^{ab} (...)
    ix = -eps**2*lgx;                 iy = -eps**2*lgy                    # isotropic null: delta^{ab}(...)
    return (px, py), (ix, iy)

def vcos(ax, ay, bx, by, msk):                       # mean vector cosine over masked region
    num = ax*bx + ay*by; den = np.sqrt(ax**2+ay**2)*np.sqrt(bx**2+by**2) + 1e-30
    return np.mean((num/den)[msk])

mid = slice(20, n-20)
msk = np.zeros((n, n), bool); msk[mid, mid] = True
msk &= (np.abs(lgx) + np.abs(lgy) > 0.05)            # where there is a gradient to rotate

print(f"\n   {'eps':>6} {'cos(meas,GR-tensor)':>20} {'cos(meas,isotropic)':>20} {'coeff ratio':>12}")
for eps in [0.06, 0.03, 0.015]:
    # measured: actual two-step normal flow (vector op), both orders
    T,DX,DY = push(*push(np.zeros((n,n)), np.zeros((n,n)), np.zeros((n,n)), N, eps), M, eps)
    T2,DX2,DY2 = push(*push(np.zeros((n,n)), np.zeros((n,n)), np.zeros((n,n)), M, eps), N, eps)
    mx, my = DX-DX2, DY-DY2                          # commutator drift vector (measured)
    (px,py),(ix,iy) = predictions(eps)
    c_gr  = vcos(mx, my, px, py, msk)
    c_iso = vcos(mx, my, ix, iy, msk)
    ratio = np.mean(np.sqrt(mx**2+my**2)[msk]) / np.mean(np.sqrt(px**2+py**2)[msk])
    print(f"   {eps:>6.3f} {c_gr:>20.4f} {c_iso:>20.4f} {ratio:>12.3f}")

# rotation angle the anisotropy induces (GR-tensor vs isotropic), and whether measured matches GR's rotation
(px,py),(ix,iy) = predictions(0.03)
ang_pred = np.degrees(np.arccos(np.clip(vcos(px,py,ix,iy,msk), -1, 1)))   # GR vs isotropic angle
T,DX,DY = push(*push(np.zeros((n,n)),np.zeros((n,n)),np.zeros((n,n)),N,0.03),M,0.03)
T2,DX2,DY2 = push(*push(np.zeros((n,n)),np.zeros((n,n)),np.zeros((n,n)),M,0.03),N,0.03)
mx,my = DX-DX2, DY-DY2
ang_meas = np.degrees(np.arccos(np.clip(vcos(mx,my,ix,iy,msk), -1, 1)))   # measured vs isotropic angle
print(f"\n   rotation away from the isotropic direction (deg): GR-tensor predicts {ang_pred:.2f}, "
      f"measured {ang_meas:.2f}")

print("\n" + "="*84); print("VERDICT (§5.18, 2+1)"); print("="*84)
# recompute cleanest at smallest eps
eps=0.015
T,DX,DY=push(*push(np.zeros((n,n)),np.zeros((n,n)),np.zeros((n,n)),N,eps),M,eps)
T2,DX2,DY2=push(*push(np.zeros((n,n)),np.zeros((n,n)),np.zeros((n,n)),M,eps),N,eps)
mx,my=DX-DX2,DY-DY2; (px,py),(ix,iy)=predictions(eps)
c_gr=vcos(mx,my,px,py,msk); c_iso=vcos(mx,my,ix,iy,msk)
if c_gr > 0.999 and (c_gr - c_iso) > 0.02:
    print(f"- POSITIVE: the measured flow-drift VECTOR tracks the full inverse-metric TENSOR h^{{ab}}(N d_bM-M d_bN)")
    print(f"  (cos={c_gr:.4f}) and is measurably ROTATED ({ang_meas:.1f} deg) away from the isotropic-scalar")
    print(f"  direction (cos to isotropic only {c_iso:.4f}), exactly as the tensor predicts ({ang_pred:.1f} deg).")
    print(f"  => in 2+1 the structure function is the full spatial metric TENSOR (GR), not merely its scalar part;")
    print(f"     an isotropic/scalar (or wrong-tensor Horava) coefficient is excluded by the rotation.")
    print(f"  Caveat: leading-order grid mechanism (clean), like §5.18 Part 1; the causal-set extraction of the")
    print(f"  3D spatial metric tensor was shown separately in §5.10 (diag recovered to a few %).")
else:
    print(f"- NOT CLEAN: cos(meas,GR)={c_gr:.4f}, cos(meas,iso)={c_iso:.4f} -- tensor character not confirmed here.")
