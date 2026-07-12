#!/usr/bin/env python3
"""Exact finite witnesses for V10 Investigation D7.

This executable tests structural constraints on a null-inclusive extension
rulebook.  It does not fit a physical law.  All probabilities are Fraction
objects; Decimal is used only to print high-precision information values.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
from itertools import permutations


getcontext().prec = 110

checks = 0


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def qstr(q):
    return f"{q.numerator}/{q.denominator}"


def d(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


def binary_kl(p, q):
    return d(p) * (d(p) / d(q)).ln() + d(1 - p) * (d(1 - p) / d(1 - q)).ln()


# -------------------------------------------------------------------------
# A. A flat unnormalised transfer cocycle can lose diamond flatness after
# independent row normalisation.  Null weights are explicit.
# -------------------------------------------------------------------------

w0_a = Fraction(2)
w0_b = Fraction(3)
wa_b = Fraction(3)
wb_a = Fraction(2)

check(w0_a * wa_b == w0_b * wb_a, "flat transfer diamond")

z0 = Fraction(1) + w0_a + w0_b       # null + a + b
za = Fraction(1) + wa_b               # null + b
zb = Fraction(1) + wb_a               # null + a

k0_a, k0_b = w0_a / z0, w0_b / z0
ka_b, kb_a = wa_b / za, wb_a / zb

check(k0_a + k0_b + Fraction(1, z0) == 1, "root row normalised")
check(ka_b + Fraction(1, za) == 1, "a row normalised")
check(kb_a + Fraction(1, zb) == 1, "b row normalised")
check(k0_a * ka_b != k0_b * kb_a, "row normalisation can break diamond gauge")


# -------------------------------------------------------------------------
# B. A positive future-completion/h transform restores a normalized sampler
# on a finite extension DAG.  A and B commute; C is a distinct terminal.
# The free positive activity r changes physical terminal probabilities while
# preserving every tested structural constraint.
# -------------------------------------------------------------------------


def completion_law(r):
    # Terminal values h(AB)=h(C)=1.  From A or B exactly the other move remains.
    h_ab = Fraction(1)
    h_c = Fraction(1)
    h_a = h_ab
    h_b = h_ab
    h_0 = h_a + h_b + r * h_c
    law = {
        "K0(A)": h_a / h_0,
        "K0(B)": h_b / h_0,
        "K0(C)": r * h_c / h_0,
        "KA(B)": Fraction(1),
        "KB(A)": Fraction(1),
    }
    return h_0, law


families = {}
for r in (Fraction(1, 2), Fraction(1), Fraction(3)):
    h0, law = completion_law(r)
    families[r] = law
    check(h0 > 0, f"positive completion r={r}")
    check(law["K0(A)"] + law["K0(B)"] + law["K0(C)"] == 1,
          f"completion row normalized r={r}")
    check(law["K0(A)"] * law["KA(B)"] == law["K0(B)"] * law["KB(A)"],
          f"commuting path weights equal r={r}")
    check(2 * law["K0(A)"] + law["K0(C)"] == 1,
          f"canonical terminal pushforward normalized r={r}")

check(families[Fraction(1, 2)]["K0(C)"] != families[Fraction(3)]["K0(C)"],
      "structural gates do not select activity")


# Relabeling A <-> B leaves each law invariant.
for r, law in families.items():
    check(law["K0(A)"] == law["K0(B)"], f"Leibniz covariance r={r}")


# -------------------------------------------------------------------------
# C. Support-local continuation cannot bootstrap a root or join components.
# Explicit root and multileg bridge sectors repair eligibility but leave free
# weights.
# -------------------------------------------------------------------------


def support_local_extensions(component_count):
    if component_count == 0:
        return ()
    return tuple(("continue", i) for i in range(component_count))


check(support_local_extensions(0) == (), "strict support-local root stall")
check(all(kind == "continue" for kind, _ in support_local_extensions(2)),
      "strict support-local law has no bridge")

explicit_root = (("root", ()),)
explicit_bridge = (("bridge", (0, 1)),)
check(len(explicit_root) == 1, "root sector can be typed explicitly")
check(len(explicit_bridge[0][1]) == 2, "bridge sector has two recorded legs")


# -------------------------------------------------------------------------
# D. Closure-defect-only proposal has the same bootstrap problem when the
# empty history has zero defect.  An added base activity fixes support, not
# its numerical value.
# -------------------------------------------------------------------------

empty_defect = Fraction(0)
check(empty_defect == 0, "empty closure defect witness")
check(Fraction(7) * empty_defect == 0, "defect-only proposal cannot nucleate")
for immigration in (Fraction(1, 7), Fraction(2, 7)):
    check(immigration + empty_defect > 0, f"base activity nucleates {immigration}")


# -------------------------------------------------------------------------
# E. Full-history/projective consistency hosts many laws.  Two Bernoulli path
# measures have exactly consistent finite cylinders but different extension
# kernels and positive relative information.
# -------------------------------------------------------------------------


def cylinder_mass(bits, p):
    ones = sum(bits)
    return p ** ones * (1 - p) ** (len(bits) - ones)


for p in (Fraction(1, 3), Fraction(2, 3)):
    for n in range(5):
        # Enumerate binary words without floating point.
        words = [tuple((mask >> j) & 1 for j in range(n)) for mask in range(1 << n)]
        check(sum(cylinder_mass(word, p) for word in words) == 1,
              f"level-{n} cylinder normalization p={p}")
        if n:
            for prefix in words[: min(3, len(words))]:
                if len(prefix) != n:
                    continue
                parent = prefix[:-1]
                children = cylinder_mass(parent + (0,), p) + cylinder_mass(parent + (1,), p)
                check(children == cylinder_mass(parent, p),
                      f"projective consistency n={n} p={p} prefix={prefix}")

p, q = Fraction(1, 3), Fraction(2, 3)
check(p != q, "inequivalent next-click kernels")
kl = binary_kl(p, q)
check(kl > 0, "inequivalent projective laws have positive KL")


# -------------------------------------------------------------------------
# F. Construction order is gauge only for declared commuting moves.
# Three independent moves have 3! equal auxiliary orders under a symmetric
# completion law.  An oriented interaction is deliberately not quotientable.
# -------------------------------------------------------------------------

orders = list(permutations(("A", "B", "D")))
order_weight = Fraction(1, len(orders))
check(len(orders) == 6, "three commuting moves have six auxiliary orders")
check(sum(order_weight for _ in orders) == 1, "commuting-order pushforward normalized")
check(len({order_weight for _ in orders}) == 1, "commuting orders equiprobable")

oriented_ab = Fraction(2, 5)
oriented_ba = Fraction(3, 5)
check(oriented_ab != oriented_ba, "physical orientation need not be gauge")
check(oriented_ab + oriented_ba == 1, "oriented protocol alternatives normalized")


print("D7 RULEBOOK NONSELECTION RECEIPT")
print(f"checks={checks}")
print(f"flat_transfer_product={qstr(w0_a * wa_b)}")
print(f"normalized_path_A_then_B={qstr(k0_a * ka_b)}")
print(f"normalized_path_B_then_A={qstr(k0_b * kb_a)}")
for r in sorted(families):
    law = families[r]
    print(
        f"activity={qstr(r)} "
        f"P_terminal_AB={qstr(2 * law['K0(A)'])} "
        f"P_terminal_C={qstr(law['K0(C)'])}"
    )
print(f"KL(Bernoulli(1/3)||Bernoulli(2/3))={kl}")
payload = "|".join([
    str(checks),
    qstr(k0_a * ka_b),
    qstr(k0_b * kb_a),
    *(qstr(families[r]["K0(C)"]) for r in sorted(families)),
    str(kl),
])
print(f"receipt_sha256={sha256(payload.encode('ascii')).hexdigest()}")
