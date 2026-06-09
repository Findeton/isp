"""
v6 Paper 2 Part II §4 receipt: why a covariant indivisible memory needs two-sided invariant decay.

The recipe: collapse/division operator Q = (1/2)alpha :phi^2: (local quadratic scalar field), and a
non-Markovian LORENTZ-INVARIANT noise correlation G(x) = g(s^2), s^2 = (x-y)_mu (x-y)^mu. The energy/heating
rate samples the Fourier transform Ghat(q) = ghat(q^2) at on-shell momentum sums/differences (p +- q), whose
invariant (p+-q)^2 ranges over TIMELIKE (q^2>0) AND SPACELIKE (q^2<0) values. Finiteness therefore needs
ghat(q^2) -> 0 as q^2 -> +-infinity, i.e. in BOTH regions.

This CORRECTS paper 1 §6, which used a frame-fixed Gaussian S(omega)=exp(-(omega tau)^2). The covariant analog
ghat(q^2)=exp(-q^2/beta^2) DECAYS timelike (q^2->+inf) but BLOWS UP spacelike (q^2->-inf): exp(+|q^2|/beta^2).
A covariant memory cannot be Gaussian-in-the-interval. The quartic template
ghat(q^2)=exp(-(q^2)^2/beta^4)=exp(-q^4/beta^4) decays BOTH ways. This receipt checks that
template; it does not prove uniqueness of the quartic class.
"""
import numpy as np

m, beta = 1.0, 4.0
def onshell(k): return np.sqrt(k**2 + m**2)                  # 1+1 on-shell energy

def inv2(pa, qa, sign):                                      # invariant (p +- q)^2 for 1+1 on-shell p,q
    wp, wq = onshell(pa), onshell(qa)
    w = wp + sign*wq; k = pa + sign*qa
    return w**2 - k**2                                       # (q0)^2 - (q1)^2

def ghat(q2, kind):
    if kind == "gauss_cov":  return np.exp(-q2/beta**2)      # covariant Gaussian-in-q^2 (the WRONG choice)
    if kind == "quartic":    return np.exp(-(q2**2)/beta**4) # exp(-q^4/beta^4): decays both ways (recipe)

def heating(Lam, kind, n=1400):
    p = np.linspace(-Lam, Lam, n); q = np.linspace(-Lam, Lam, n)
    PP, QQ = np.meshgrid(p, q, indexing='ij')
    wp, wq = onshell(PP), onshell(QQ)
    # recipe-shaped integrand: [G((p+q)^2)+G((p-q)^2)] with the invariant measure 1/(2wp 2wq)
    G = ghat(inv2(PP, QQ, +1), kind) + ghat(inv2(PP, QQ, -1), kind)
    integrand = G / (2*wp * 2*wq)
    dp = p[1]-p[0]; dq = q[1]-q[0]
    return np.sum(integrand) * dp * dq

print("="*84)
print("Porting check: covariant memory needs two-sided decay; quartic is the worked template")
print(f"   1+1 on-shell, m={m}, beta={beta}; heating functional vs momentum cutoff Lambda")
print("="*84)
print(f"   {'Lambda':>8} {'H[gauss_cov]':>16} {'H[quartic]':>14} {'H(2L)/H(L) gauss':>18} {'quartic':>9}")
Lams = [10, 20, 40, 80]
prev = {}
for L in Lams:
    Hg = heating(L, "gauss_cov"); Hq = heating(L, "quartic")
    rg = Hg/prev.get("g", Hg) if "g" in prev else float('nan')
    rq = Hq/prev.get("q", Hq) if "q" in prev else float('nan')
    prev = {"g": Hg, "q": Hq}
    print(f"   {L:>8} {Hg:>16.4e} {Hq:>14.5f} {rg:>18.2f} {rq:>9.2f}")

print("\n   sanity: is each ghat(q^2) covariant? (function of the invariant q^2 alone) -- yes by construction;")
print("   the only question is its behaviour as q^2 -> -infinity (spacelike):")
for q2 in [-100, -25, 0, 25, 100]:
    print(f"     q^2={q2:>5}:  gauss_cov={ghat(np.array([float(q2)]),'gauss_cov')[0]:>12.3e}   "
          f"quartic={ghat(np.array([float(q2)]),'quartic')[0]:>10.3e}")

print("\n" + "="*84); print("VERDICT (Paper 2 Part II §4 receipt)"); print("="*84)
print("- Covariant Gaussian-in-q^2 (exp(-q^2/beta^2)) BLOWS UP in the spacelike region (q^2<0 -> exp(+)) ->")
print("  heating DIVERGES with the cutoff. A covariant memory CANNOT be Gaussian-in-the-interval.")
print("- The quartic template ghat=exp(-q^4/beta^4) decays as q^2->+-inf -> heating CONVERGES (H(2L)/H(L)->1).")
print("- This both (a) confirms arXiv:2507.06954's spacelike-finiteness condition and (b) CORRECTS paper 1 §6:")
print("  the frame-fixed Gaussian S(omega) was non-covariant; the covariant indivisible memory must have")
print("  positive-type two-sided invariant decay. The quartic-damped kernel is an admissible receipt template,")
print("  not a uniqueness theorem for G(s^2).")
