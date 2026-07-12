#!/usr/bin/env python3
"""D10 80-digit finite celestial-clock covering calculation.

The calculation uses Decimal arithmetic for all load-bearing geometry.  The
worst directional support is found by enumerating spherical Voronoi vertices
(normals to every non-collinear direction triple), then independently checked
with a deterministic dense float probe.  Direction sets are Platonic and
nested unions; no random sample selects the result.
"""

from __future__ import annotations

from decimal import Decimal as D, getcontext
from hashlib import sha256
from itertools import combinations, product
from math import cos, pi, sin, sqrt


getcontext().prec = 90
CHECKS = 0
EXPECTED_CHECKS = 99


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:02d}: {label}")


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), D(0))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def det3(a, b, c):
    return dot(a, cross(b, c))


def norm(a):
    return dot(a, a).sqrt()


def unit(a):
    a = tuple(D(x) for x in a)
    n = norm(a)
    if n == 0:
        raise ValueError("zero direction")
    return tuple(x / n for x in a)


def canonical_key(u):
    # 70 significant decimal places are much finer than any separation here.
    return tuple(format(x, ".70E") for x in u)


def unique(points):
    found = {}
    for p in points:
        u = unit(p)
        found[canonical_key(u)] = u
    return tuple(found[key] for key in sorted(found))


phi = (D(1) + D(5).sqrt()) / D(2)
invphi = D(1) / phi

tetra = unique(((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)))
octa = unique(((s, 0, 0) for s in (-1, 1))).__add__(
    unique(((0, s, 0) for s in (-1, 1))))
octa = unique(octa + unique(((0, 0, s) for s in (-1, 1))))
cube = unique(product((-1, 1), repeat=3))
icosa = unique(
    [(0, s, t * phi) for s, t in product((-1, 1), repeat=2)]
    + [(s, t * phi, 0) for s, t in product((-1, 1), repeat=2)]
    + [(t * phi, 0, s) for s, t in product((-1, 1), repeat=2)]
)
dodeca = unique(
    list(product((-1, 1), repeat=3))
    + [(0, s * invphi, t * phi) for s, t in product((-1, 1), repeat=2)]
    + [(s * invphi, t * phi, 0) for s, t in product((-1, 1), repeat=2)]
    + [(t * phi, 0, s * invphi) for s, t in product((-1, 1), repeat=2)]
)

check(len(tetra) == 4, "tetrahedron has four directions")
check(len(octa) == 6, "octahedron has six directions")
check(len(cube) == 8, "cube has eight directions")
check(len(icosa) == 12, "icosahedron has twelve directions")
check(len(dodeca) == 20, "dodecahedron has twenty directions")

for label, points in (("tetra", tetra), ("octa", octa), ("cube", cube),
                      ("icosa", icosa), ("dodeca", dodeca)):
    for u in points:
        check(abs(dot(u, u) - D(1)) < D("1e-84"), f"{label} unit normalization")
    center = tuple(sum((u[j] for u in points), D(0)) for j in range(3))
    check(max(abs(x) for x in center) < D("1e-84"), f"{label} zero directional bias")


def support(points, x):
    return max(dot(u, x) for u in points)


def covering_support(points):
    """Return min_|x|=1 max_u u.x for a full-dimensional origin-interior set.

    The minimum is the origin-centered inradius of conv(points).  A closest
    supporting facet contains three affinely independent vertices, and its
    unit normal is therefore among the enumerated triple normals.  Extra
    non-facet normals are harmless actual sphere points and cannot fall below
    the global minimum.
    """
    best = D(2)
    best_x = None
    candidates = 0
    for a, b, c in combinations(points, 3):
        normal = cross(sub(b, a), sub(c, a))
        n = norm(normal)
        if n < D("1e-70"):
            continue
        v = tuple(x / n for x in normal)
        for sign in (D(1), D(-1)):
            x = tuple(sign * y for y in v)
            value = support(points, x)
            candidates += 1
            if value < best:
                best, best_x = value, x
    if best_x is None:
        raise AssertionError("no Voronoi candidates")
    return best, best_x, candidates


def dense_probe(points, count=120000):
    """Independent float Fibonacci probe; returns the smallest sampled support."""
    fp = [[float(x) for x in u] for u in points]
    golden = pi * (3.0 - sqrt(5.0))
    best = 2.0
    for k in range(count):
        z = 1.0 - 2.0 * (k + 0.5) / count
        r = sqrt(max(0.0, 1.0 - z * z))
        az = golden * k
        x = (r * cos(az), r * sin(az), z)
        value = max(u[0] * x[0] + u[1] * x[1] + u[2] * x[2] for u in fp)
        best = min(best, value)
    return best


families = {
    "K4_tetra": tetra,
    "K6_octa": octa,
    "K8_cube": cube,
    "K12_icosa": icosa,
    "K20_dodeca": dodeca,
    "K32_dual_union": unique(icosa + dodeca),
}

# Nested sequence: refinement can add questions without altering earlier ones.
nested = {}
running = tuple()
for label, addition in (("tetra", tetra), ("octa", octa), ("cube", cube),
                        ("icosa", icosa), ("dodeca", dodeca)):
    running = unique(running + addition)
    nested[f"nested_{label}_K{len(running)}"] = running

rows = []
for name, points in {**families, **nested}.items():
    m, witness, candidates = covering_support(points)
    epsilon = D(1) - m
    radial_excess = D(1) / m - D(1)
    probe = D(str(dense_probe(points)))
    # The dense sample cannot beat the true minimum; its discretization gap is small.
    check(probe + D("1e-12") >= m, f"{name} dense probe respects exact candidate minimum")
    check(probe - m < D("0.008"), f"{name} dense probe independently approaches minimum")
    check(D(0) < m <= D(1), f"{name} covers every direction within a hemisphere")
    rows.append((name, len(points), m, epsilon, radial_excess, probe, candidates, witness))

# Special exact controls.
tetra_m = next(row[2] for row in rows if row[0] == "K4_tetra")
octa_m = next(row[2] for row in rows if row[0] == "K6_octa")
check(abs(tetra_m - D(1) / D(3)) < D("1e-80"), "tetra covering support exactly 1/3")
check(abs(octa_m - D(1) / D(3).sqrt()) < D("1e-80"),
      "octa covering support exactly 1/sqrt(3)")

nested_rows = [row for row in rows if row[0].startswith("nested_")]
check(all(b[2] + D("1e-80") >= a[2] for a, b in zip(nested_rows, nested_rows[1:])),
      "nested direction refinement never worsens covering support")
check(nested_rows[-1][4] < nested_rows[0][4], "nested refinement reduces cone radial excess")

all_test_sets = tuple({**families, **nested}.values())
check(all(any(abs(det3(a, b, c)) > D("1e-70")
                  for a, b, c in combinations(points, 3))
              for points in all_test_sets),
      "every covering set spans three dimensions")
check(all(max(abs(sum((u[j] for u in points), D(0))) for j in range(3))
              < D("1e-80") for points in all_test_sets),
      "positive equal-weight zero barycenter puts origin in every hull interior")

if CHECKS != EXPECTED_CHECKS:
    raise AssertionError(f"expected {EXPECTED_CHECKS} checks, observed {CHECKS}")

print("\nname K support_min epsilon radial_excess dense_probe candidates")
for name, k, m, eps, rex, probe, candidates, _ in rows:
    print(f"{name} {k} {m:.18E} {eps:.18E} {rex:.18E} {probe:.18E} {candidates}")

summary_lines = [
    "D10 FINITE CLOCK CONVERGENCE RECEIPT",
    f"checks={CHECKS}",
    "precision_decimal_digits=90",
    "load_bearing_method=spherical_voronoi_triple_enumeration",
    "independent_probe=fibonacci_120000",
    "finite_outer_polyhedral_approximations=PASS",
    "infinite_sequence_convergence=CONDITIONAL_ON_DENSE_NESTED_UNION",
    "external_global_s2_diagnostic=FIBONACCI_120000",
]
for name, k, m, eps, rex, _, _, _ in rows:
    summary_lines.append(f"{name}:K={k}:support={m:.24E}:radial_excess={rex:.24E}")
summary = "\n".join(summary_lines) + "\n"
print("\n" + summary, end="")
print("receipt_sha256=" + sha256(summary.encode()).hexdigest())
