#!/usr/bin/env python3
"""
Correctness gate for mm_equations.py (abelian U(1)): the generated loop equations
must be SATISFIED by the exact 2D U(1) solution  W(C) = prod_p I_{w_p}(beta)/I_0(beta).
If every residual ~ 0, the loop-equation generator is correct (in 2D U(1)).
"""
import numpy as np
from loops import plaq_boundary, exact_W_2d, chain_add
from mm_equations import abelian_loop_equation

d = 2

def W_of_key(key, beta):
    return exact_W_2d(dict(key), beta)

def residual(C, link, beta):
    eq = abelian_loop_equation(C, link, d)
    return sum((a + b * beta) * W_of_key(k, beta) for k, (a, b) in eq.items())

# test cycles
P = plaq_boundary((0, 0), 0, 1, d)                       # 1x1
domino = chain_add(P, plaq_boundary((1, 0), 0, 1, d))    # 1x2 horizontal
square2 = chain_add(chain_add(P, plaq_boundary((1,0),0,1,d)),
                    chain_add(plaq_boundary((0,1),0,1,d), plaq_boundary((1,1),0,1,d)))  # 2x2
Lshape = chain_add(P, plaq_boundary((0,1),0,1,d))        # 1x2 vertical

cases = {"1x1 plaquette": P, "1x2 horiz": domino, "2x2 square": square2, "1x2 vert": Lshape}

print("Correctness gate: residual of the U(1) loop equation under the EXACT 2D solution")
print("(should be ~0 for all cycles, links, beta)\n")
maxres = 0.0
for beta in (0.7, 1.7, 3.0):
    for name, C in cases.items():
        # test on every link present in C, and one link NOT in C (n0=0 deformation eq)
        links = list(C.keys()) + [((5, 5), 0)]
        for link in links:
            r = residual(C, link, beta)
            maxres = max(maxres, abs(r))
    print(f"  beta={beta}: max |residual| over all tested cycles/links = "
          f"{max(abs(residual(C,link,beta)) for name,C in cases.items() for link in list(C.keys())+[((5,5),0)]):.2e}")

print(f"\nGLOBAL max |residual| = {maxres:.2e}")
print("PASS" if maxres < 1e-9 else "FAIL -- loop-equation generator has a bug")
