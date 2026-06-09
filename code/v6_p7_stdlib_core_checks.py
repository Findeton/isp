"""Pure-stdlib verifier (no numpy/scipy needed) for the core Paper 6-7 constants."""
import math, cmath
def bisect(f,a,b,n=200):
    for _ in range(n):
        m=(a+b)/2
        if f(a)*f(m)<=0: b=m
        else: a=m
    return (a+b)/2
sat=lambda e: e*math.tanh(e)-math.log(math.cosh(e))-(1-math.tanh(e)**2)
com=lambda e: math.tanh(e)-math.exp(-e)
e1=bisect(sat,0.5,2.0); e2=bisect(com,0.1,2.0); th=math.tanh(e2)
print("eta_evt  =",e1," (expect 1.090344354879492)")
print("eta_hist =",e2," (expect 0.609377863436006)")
print("cubic identity theta+theta^2+theta^3 =",th+th**2+th**3," (expect 1)")
print("W_evt =",1-math.tanh(e1)**2," W_hist =",e2*th-math.log(math.cosh(e2)))
a=[complex(0.7,0.2),complex(-0.3,0.9),complex(0.5,-0.4)]
I=lambda S:abs(sum(a[s] for s in S))**2
k3=I([0,1,2])-I([0,1])-I([0,2])-I([1,2])+I([0])+I([1])+I([2])
print("Sorkin kappa_3 (p=2) =",k3," (expect 0)")
print("kappa*sigma_A = 2*pi =",2*math.pi)
