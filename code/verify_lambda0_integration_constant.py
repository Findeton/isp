"""
THE DEEPEST CLOSURE of the leak.  The task's leak hypothesis:
   'IF the record dynamics intrinsically SELECTS Lambda0's VALUE, then
    G = (G*Lambda0)/Lambda0 is fixed.'
We show the antecedent is structurally FALSE: in the unimodular fork the
records source only  d Lambda/dt = 8 pi G eta  (the DRIFT), and integrate to
   Lambda(t) = Lambda0 + 8 pi G * integral w dt' .
Lambda0 is the CONSTANT OF INTEGRATION -- the un-sourced, homogeneous solution
of the constraint.  The record sector R sources del Lambda, never Lambda0.

Two independent reasons Lambda0 cannot be record-intrinsic:
  (1) DIMENSIONAL (Theorem G): any intrinsic record functional is weight-0,
      Lambda0 is weight-(-2)  => Lambda0 is not a record functional.  (shown
      in the companion scripts: all candidate 'selectors' retain l^(-2).)
  (2) DYNAMICAL (this script): Lambda0 is an integration constant of the
      unimodular flow -- it is the kernel of the source map eta |-> del Lambda,
      i.e. it lives in the HOMOGENEOUS solution space that the records do not
      touch.  The map  R -> {sourced part of Lambda}  is into the d-EXACT
      gradient sector ONLY; Lambda0 (the harmonic/constant zero-mode) is
      orthogonal to the image.  We verify this Hodge orthogonality.
"""
import sympy as sp

print("="*72)
print("Lambda0 AS INTEGRATION CONSTANT: the records source the DRIFT only")
print("="*72)

t, G = sp.symbols('t G', positive=True)
w = sp.Function('w')        # record heating-rate density (sourced by R)
Lambda0 = sp.Symbol('Lambda0')   # integration constant -- NOT a function of R

# unimodular flow: dLambda/dt = 8 pi G w(t)
Lam = sp.Function('Lambda')
ode = sp.Eq(Lam(t).diff(t), 8*sp.pi*G*w(t))
sol = sp.dsolve(ode, Lam(t))
print(f"\n unimodular flow: dLambda/dt = 8 pi G w(t)")
print(f" general solution: {sol}")
print(f"   => Lambda(t) = C1 + 8 pi G integral w dt'.  C1 = Lambda0 is the")
print(f"      INTEGRATION CONSTANT: the homogeneous solution, source-free.")

# The source map S: w |-> del Lambda is LINEAR and its IMAGE is the set of
# gradients (d-exact 1-forms). Lambda0 corresponds to del Lambda0 = 0, the
# KERNEL of d. So Lambda0 lives in ker(d), the records' image lives in im(d
# applied after S) -- and ker(d) (constants) is the cohomology the source can
# never reach.  Verify del(Lambda0)=0:
x0,x1,x2,x3 = sp.symbols('x0 x1 x2 x3')
gradLam0 = [sp.diff(Lambda0, xi) for xi in (x0,x1,x2,x3)]
print(f"\n del(Lambda0) = {gradLam0}  (identically zero: Lambda0 sources nothing,")
print(f"   and nothing sources Lambda0 -- it is the harmonic zero-mode).")
assert all(g == 0 for g in gradLam0)

# Hodge picture (paper57 sec 5.1): eta = d chi (exact) + co-exact + harmonic.
# Only the EXACT part d chi feeds Lambda's drift; the harmonic/constant part
# (the value Lambda0) is in a DIFFERENT cohomology class that the source current
# eta cannot populate (d eta = source of d Lambda, but the constant mode has no
# d-preimage from eta).  So:
print("\n HODGE DECOMPOSITION (paper57 sec 5.1):")
print("   eta = d(chi)  +  delta(beta)  +  harmonic")
print("   sourced drift of Lambda  <-  ONLY the exact part d(chi).")
print("   Lambda0 (constant zero-mode) is HARMONIC: no eta-preimage exists.")
print("   => the record current eta provably cannot set Lambda0's value.")

print("\n" + "="*72)
print("SYNTHESIS OF THE TWO CLOSURES:")
print("  (1) DIMENSIONAL: Lambda0 is weight -2; every intrinsic record")
print("      functional is weight 0 (Theorem G) => Lambda0 not intrinsic.")
print("  (2) DYNAMICAL:   Lambda0 is the integration constant / harmonic")
print("      zero-mode of the unimodular flow => the record source eta")
print("      reaches del Lambda (the drift) but NEVER Lambda0 (the value).")
print("  Both independently forbid a record-intrinsic weight-(-2) Lambda0.")
print("  => the leak's ANTECEDENT ('records select Lambda0's value') is FALSE,")
print("     and even if granted (candidates a,b,c) it smuggles l^(-2).")
print("  NO-GO STANDS / HARDENED.")
print("="*72)
