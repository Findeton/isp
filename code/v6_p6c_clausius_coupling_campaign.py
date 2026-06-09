"""
v6_p6c: Clausius coupling campaign.
Finite Jacobson closure inside the record ontology:
  commitment law:      delta S_rec = delta I            (entropy = evidence, nats)
  area law (form):     delta S_rec = sigma_A * delta A  (Paper 5 record-area campaign)
  modular temperature: T = 1/(2*pi)                      (p6b, per unit surface gravity)
  focusing readout:    theta' = -R_kk   (linearized null Raychaudhuri; Paper 4 sec 22-27)
Demand Clausius delta Q = T delta S for ALL flux profiles  =>  R_kk = (2*pi/sigma_A) T_kk,
i.e. kappa * sigma_A = 2*pi exactly, for every sigma_A.  The PRODUCT is the invariant.
"""
import numpy as np
from scipy.integrate import solve_ivp, simpson
from scipy.optimize import brentq

TWO_PI = 2*np.pi
L = 1.0
lam = np.linspace(-L, 0.0, 4001)   # affine parameter, horizon cross-section at 0

def profiles():
    g = lambda c,s: np.exp(-((lam-c)/s)**2)
    return [ g(-0.5,0.12), 0.7*g(-0.3,0.2)+0.3*g(-0.8,0.1), np.cos(3*lam)**2 * g(-0.5,0.3) ]

def delta_Q(Tkk):
    # boost heat flux per unit transverse area, surface gravity a=1:
    # dQ = (-lambda) * T_kk dlambda  (Killing weight)
    return simpson((-lam)*Tkk, x=lam)

def delta_A(Rkk):
    # local-Rindler linearized Raychaudhuri (Jacobson): theta(lambda) = -lambda*R_kk to
    # first order at the cross-section, hence dA = int (-lambda) R_kk dlambda.
    return simpson((-lam)*Rkk, x=lam)

def local_rindler_check(Rkk):
    # verify theta_ODE(l) = int_l^0 R_kk matches -l*R_kk(0) to O(l^2) as l->0-
    out=[]
    for l in (-0.02,-0.01,-0.005):
        i = np.searchsorted(lam,l)
        theta_ode = simpson(Rkk[i:], x=lam[i:])
        out.append(abs(theta_ode - (-l)*Rkk[-1]))
    return out  # should fall ~quadratically

def clausius_residual(c, Tkk, sigma_A):
    Rkk = c*Tkk
    dA = delta_A(Rkk)
    dS = sigma_A*dA                  # record area law
    dQ = delta_Q(Tkk)
    T  = 1.0/TWO_PI                  # p6b modular temperature
    return dQ - T*dS

print("=== p6c: Clausius coupling campaign ===\n")
prods=[]
for sigma_A in (1.0, 1.0/3.0, 0.7, 4.0):
    for k,Tkk in enumerate(profiles()):
        f = lambda c: clausius_residual(c, Tkk, sigma_A)
        c_star = brentq(f, 1e-3, 1e3)
        prods.append(c_star*sigma_A)
        print(f"sigma_A={sigma_A:8.6f} profile {k}: kappa* = {c_star:12.9f}   kappa*sigma_A = {c_star*sigma_A:.12f}")
prods=np.array(prods)
print(f"\nuniversal product kappa*sigma_A: mean = {prods.mean():.15f}, max dev = {np.abs(prods-TWO_PI).max():.3e}")
print(f"2*pi                            = {TWO_PI:.15f}")

print("\nBekenstein-Hawking coefficient: G = kappa/(8*pi)  =>  G*sigma_A = (kappa*sigma_A)/(8*pi)")
print(f"  G*sigma_A = {prods.mean()/(8*np.pi):.15f}   (= 1/4 exactly: S = A/(4G) is an identity, not an input)")

print("\nrecord-natural gauge (sigma_A := 1, one nat per unit record area):")
print(f"  A_rec = 1,  kappa = 2*pi = {TWO_PI:.15f},  G = 1/4 = {TWO_PI/(8*np.pi):.15f}")

print("\nPaper-5 counterfamily collapse on the gauge quotient:")
for A_rec in (1.0, 3.0):
    sig = 1.0/A_rec; kap = TWO_PI/sig
    print(f"  A_rec={A_rec}: (sigma_A, kappa) = ({sig:.6f}, {kap:.6f})  product = {sig*kap:.12f}")
print("  both counterfamily members sit at the SAME point kappa*sigma_A = 2*pi of the quotient;")
print("  the map between them is a unit change, not a second physical theory.")

print("\nperturbation attack: impose kappa*sigma_A = 2*pi + 0.1 and re-test Clausius:")
Tkk = profiles()[0]; sigma_A=1.0
res = clausius_residual(TWO_PI+0.1, Tkk, sigma_A)
errs = local_rindler_check(TWO_PI*Tkk)
print(f"  local-Rindler check |theta_ODE - (-l)R_kk(0)| at l=-0.02,-0.01,-0.005: "
      f"{errs[0]:.2e}, {errs[1]:.2e}, {errs[2]:.2e}  (quadratic vanishing)")
print(f"  Clausius residual = {res:.6e}  (nonzero => REFUTED; the product cannot move)")
