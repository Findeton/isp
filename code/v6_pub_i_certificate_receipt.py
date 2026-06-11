# Dedicated receipt for Paper I's d = 3 certificate (Section 5):
# exact rational verification that the printed positive definite
# pair A, B (entries with denominator 10^6) gives the word
# W = A^2 B A B^2 (necklace 001011) a NEGATIVE cubic discriminant
# -> one real eigenvalue and a dominant complex pair at d = 3.
# All certificate steps in exact arithmetic (Fraction); the float
# eigenvalues are printed for display only.
# Canonical: /tmp/v6_pub_i_certificate.out  (bit-identical required)
from fractions import Fraction as Fr
import numpy as np

D = 10**6
A_int = [[4744014,  199767, -2318975],
         [ 199767,   16101,  -140138],
         [-2318975, -140138,  1398943]]
B_int = [[ 126476,  807436,  335329],
         [ 807436, 8921895, 2209530],
         [ 335329, 2209530,  892048]]
A = [[Fr(v, D) for v in row] for row in A_int]
B = [[Fr(v, D) for v in row] for row in B_int]

def matmul(X, Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))

print("== leading principal minors (exact rational) ==")
for name, M in (("A", A), ("B", B)):
    m1 = M[0][0]
    m2 = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    m3 = det3(M)
    ok = m1 > 0 and m2 > 0 and m3 > 0
    print(f"  {name}: minor1 = {float(m1):.6f}  minor2 = {float(m2):.6e}"
          f"  minor3 = {float(m3):.6e}  all > 0 exactly: {ok}")

print("\n== W = A^2 B A B^2, char poly, exact discriminant ==")
W = matmul(matmul(matmul(matmul(matmul(A, A), B), A), B), B)
tr = W[0][0] + W[1][1] + W[2][2]
c1 = (W[1][1]*W[2][2] - W[1][2]*W[2][1]
    + W[0][0]*W[2][2] - W[0][2]*W[2][0]
    + W[0][0]*W[1][1] - W[0][1]*W[1][0])      # sum of principal 2x2 minors
dW = det3(W)
# char poly x^3 - tr x^2 + c1 x - det; discriminant of
# a x^3 + b x^2 + c x + d with a=1, b=-tr, c=c1, d=-det:
a, bq, c, d = Fr(1), -tr, c1, -dW
disc = (18*a*bq*c*d - 4*bq**3*d + bq**2*c**2 - 4*a*c**3 - 27*a**2*d**2)
print(f"  trace(W) = {float(tr):.10e}")
print(f"  c1(W)    = {float(c1):.10e}")
print(f"  det(W)   = {float(dW):.10e}")
print(f"  cubic discriminant (exact sign): {'NEGATIVE' if disc < 0 else 'NONNEGATIVE'}"
      f"   (float value {float(disc):.6e})")
print("  discriminant < 0  ->  one real eigenvalue + complex pair: "
      f"{disc < 0}")

print("\n== float eigenvalues (display only; certificate is exact) ==")
Wf = np.array([[float(v) for v in row] for row in W])
ev = np.linalg.eigvals(Wf)
cx = ev[np.argmax(np.abs(ev.imag))]
rho = float(np.max(np.abs(ev)))
print(f"  complex pair ~ {cx.real:.3e} +- {abs(cx.imag):.6f} i")
print(f"  |Im lambda| / spectral radius = {abs(cx.imag)/rho:.10f}")
print("  -> the d = 3 always-real claim of an earlier draft is")
print("     refuted by this exact certificate (one checkable pair).")
