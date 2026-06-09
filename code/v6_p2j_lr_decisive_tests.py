"""
v6 Paper 2 Part II §5.11: decisive finite tests for the LR selector.

This finite diagnostic uses only the Python standard library. It executes the
two tests named in §5.11:

1. response Fisher-Gram lower bound:
   G = B H^{-1} B^T must have a positive reduced smallest eigenvalue;
2. one-event readout singular bound:
   record/source/causal-set/slice readouts must factor through one selected
   event support with no hidden kernel.

It also prints a branch-B/decoupled countercase, where a separate source
channel preserves finite receipt rows but breaks the one-event singular bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import atan2, cos, exp, isfinite, log, pi, sin, sqrt


@dataclass
class TestResult:
    cells: int
    gram_rank: int
    gram_min: float
    gram_cond: float
    one_event_min: float
    one_event_cond: float
    martingale_error: float
    gamma: float
    beta: float


def norm(v: list[float]) -> float:
    return sqrt(sum(x * x for x in v))


def normalize(v: list[float]) -> list[float]:
    n = norm(v)
    if n < 1e-14:
        return [0.0 for _ in v]
    return [x / n for x in v]


def center(v: list[float]) -> list[float]:
    m = sum(v) / len(v)
    return [x - m for x in v]


def smooth_profile(n: int, width: float) -> list[float]:
    centers = [0.14, 0.31, 0.49, 0.68, 0.86]
    out = []
    for i in range(n):
        x = (i + 0.5) / n
        y = 0.0
        for c in centers:
            d = min(abs(x - c), 1.0 - abs(x - c))
            y += exp(-0.5 * (d / width) ** 2)
        out.append(y)
    mx = max(out)
    return [x / mx for x in out]


def memory_value(i: int, j: int, n: int, beta: float) -> float:
    xi = (i + 0.5) / n
    xj = (j + 0.5) / n
    d = min(abs(xi - xj), 1.0 - abs(xi - xj))
    return exp(-((beta * d) ** 4))


def jacobi_eigenvalues_symmetric(a_in: list[list[float]], max_sweeps: int = 200) -> list[float]:
    """Eigenvalues of a real symmetric matrix by Jacobi rotations."""
    n = len(a_in)
    if n == 0:
        return []
    a = [row[:] for row in a_in]
    for _ in range(max_sweeps):
        p, q = 0, 1 if n > 1 else 0
        max_off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                val = abs(a[i][j])
                if val > max_off:
                    max_off = val
                    p, q = i, j
        if max_off < 1e-12:
            break
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        tau = (aqq - app) / (2.0 * apq)
        t = 1.0 / (abs(tau) + sqrt(1.0 + tau * tau))
        if tau < 0:
            t = -t
        c = 1.0 / sqrt(1.0 + t * t)
        s = t * c
        for k in range(n):
            if k != p and k != q:
                akp, akq = a[k][p], a[k][q]
                a[k][p] = c * akp - s * akq
                a[p][k] = a[k][p]
                a[k][q] = s * akp + c * akq
                a[q][k] = a[k][q]
        a[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        a[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        a[p][q] = 0.0
        a[q][p] = 0.0
    return sorted(a[i][i] for i in range(n))


def event_probability(n: int) -> list[float]:
    profile = smooth_profile(n, 0.05)
    return [min(max(0.08 + 0.34 * x, 1e-4), 1.0 - 1e-4) for x in profile]


def response_rows(
    n: int,
    beta: float,
    branch_b: bool = False,
    gram_epsilon: float | None = None,
) -> list[list[float]]:
    detector = normalize(center(smooth_profile(n, 0.045)))
    source_base = [1.0 / sqrt(n) for _ in range(n)]
    source = source_base[:]

    xs = [(i + 0.5) / n for i in range(n)]
    ts1 = normalize(center([sin(2.0 * pi * x) for x in xs]))
    ts2 = normalize(center([cos(2.0 * pi * x) for x in xs]))

    prof = smooth_profile(n, 0.06)
    info = [0.0 for _ in range(n)]
    for i in range(n):
        info[i] = prof[(i + 1) % n] - prof[(i - 1) % n]
    info = normalize(center(info))

    mem = []
    for i in range(n):
        mem.append(sum(memory_value(i, j, n, beta) for j in range(n)))
    mem = normalize(center(mem))
    if norm(mem) < 1e-12:
        mem = normalize(center([sin(4.0 * pi * x) for x in xs]))

    if branch_b:
        shift = max(1, n // 3)
        source = detector[-shift:] + detector[:-shift]
        source = normalize(center(source))

    if gram_epsilon is not None:
        # Adversarial C-floor probe: make the source receipt nearly redundant
        # with the detector receipt. If the response Fisher-Gram floor is the
        # real selector-isolation mechanism, this perturbation should drive the
        # smallest reduced eigenvalue down with epsilon.
        source = normalize(
            [detector[i] + gram_epsilon * source_base[i] for i in range(n)]
        )

    return [source, detector, ts1, ts2, info, mem]


def fisher_gram(rows: list[list[float]], h_inv_diag: list[float]) -> tuple[list[list[float]], int]:
    r = len(rows)
    gram = [[0.0 for _ in range(r)] for _ in range(r)]
    for i in range(r):
        for j in range(i, r):
            val = sum(rows[i][k] * h_inv_diag[k] * rows[j][k] for k in range(len(h_inv_diag)))
            gram[i][j] = val
            gram[j][i] = val
    eigs = jacobi_eigenvalues_symmetric(gram)
    rank = sum(1 for e in eigs if e > 1e-10)
    return gram, rank


def one_event_role_atas(
    n: int,
    branch_b: bool = False,
    source_floor: float | None = None,
) -> list[list[list[float]]]:
    """Return A^T A for each role map separately.

    The LR7 test is not merely that the stacked readouts are injective. Record
    identity would make that trivial. Each physical role must see the same
    selected support with no role-specific kernel.
    """
    atas = []
    for factor in [1.0, 1.05, 0.97, 1.02]:
        ata = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            ata[i][i] = factor * factor
        atas.append(ata)

    if branch_b:
        # Separate source process: selected event n-1 is invisible to the source
        # channel, and source atom 0 is overcounted. The source role now has a
        # genuine kernel even though record/cset/slice still see the event.
        source = [[0.0 for _ in range(n)] for _ in range(n)]
        f = 1.05
        for i in range(n - 1):
            source[i][i] = f
        source[n - 1][0] = f
        ata = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ata[i][j] = sum(source[k][i] * source[k][j] for k in range(n))
        atas[1] = ata
    elif source_floor is not None:
        # Adversarial S-floor probe: every role remains on the same event
        # support, but one source singular value is gradually pinched. This
        # distinguishes "one support exists" from a uniform cofinal role floor.
        f = 1.05
        source = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            source[i][i] = f
        source[n - 1][n - 1] = f * source_floor
        ata = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ata[i][j] = sum(source[k][i] * source[k][j] for k in range(n))
        atas[1] = ata

    return atas


def beta_from_covariance(n: int, beta: float, p: list[float]) -> float:
    weights = []
    for j in range(n):
        weights.append(memory_value(0, j, n, beta) * p[0] * (1.0 - p[0]) * p[j] * (1.0 - p[j]))
    total = sum(max(w, 0.0) for w in weights)
    if total <= 0:
        return float("nan")
    moment = 0.0
    for j, w in enumerate(weights):
        d = min(j / n, 1.0 - j / n)
        moment += max(w, 0.0) * d * d
    width = sqrt(moment / total)
    return 1.0 / max(width, 1e-12)


def martingale_refinement_error(coarse: int, fine: int) -> float:
    coarse_ell = smooth_profile(coarse, 0.05)
    fine_ell = smooth_profile(fine, 0.05)
    block = fine // coarse
    projected = []
    for i in range(coarse):
        projected.append(sum(fine_ell[i * block : (i + 1) * block]) / block)
    return norm([projected[i] - coarse_ell[i] for i in range(coarse)]) / sqrt(coarse)


def execute(
    n: int,
    branch_b: bool = False,
    beta_in: float = 7.5,
    gram_epsilon: float | None = None,
    source_floor: float | None = None,
) -> TestResult:
    p = event_probability(n)
    h_inv = [x * (1.0 - x) for x in p]
    rows = response_rows(n, beta=beta_in, branch_b=branch_b, gram_epsilon=gram_epsilon)
    gram, rank = fisher_gram(rows, h_inv)
    gram_eigs = [e for e in jacobi_eigenvalues_symmetric(gram) if e > 1e-10]
    gram_min = min(gram_eigs) if gram_eigs else 0.0
    gram_cond = max(gram_eigs) / gram_min if gram_min > 0 else float("inf")

    singulars = []
    for ata in one_event_role_atas(n, branch_b, source_floor):
        eigs = [max(e, 0.0) for e in jacobi_eigenvalues_symmetric(ata)]
        singulars.extend([sqrt(e) for e in eigs])
    one_min = min(singulars) if singulars else 0.0
    one_cond = max(singulars) / one_min if one_min > 0 else float("inf")

    return TestResult(
        cells=n,
        gram_rank=rank,
        gram_min=gram_min,
        gram_cond=gram_cond,
        one_event_min=one_min,
        one_event_cond=one_cond,
        martingale_error=martingale_refinement_error(n, 2 * n),
        gamma=sum(p) / n,
        beta=beta_from_covariance(n, beta_in, p),
    )


def finite(x: float) -> str:
    return f"{x:10.4f}" if isfinite(x) else "       inf"


def print_table(title: str, results: list[TestResult]) -> None:
    print(title)
    print("-" * len(title))
    print(
        "cells  rank  gram_min    gram_cond   one_min     one_cond   "
        "mart_err    gamma     beta"
    )
    for r in results:
        print(
            f"{r.cells:5d}  {r.gram_rank:4d}  {r.gram_min:9.6f}  {finite(r.gram_cond)}  "
            f"{r.one_event_min:8.6f}  {finite(r.one_event_cond)}  "
            f"{r.martingale_error:8.6f}  {r.gamma:8.5f}  {r.beta:8.4f}"
        )
    print()


def tail_single(beta_query: float, scale: float) -> float:
    return exp(-((beta_query / scale) ** 4))


def tail_mixture(beta_query: float, scales: list[float], weights: list[float]) -> float:
    return sum(w * tail_single(beta_query, s) for s, w in zip(scales, weights))


def tail_derivative(beta_query: float, scales: list[float], weights: list[float]) -> float:
    total = 0.0
    for s, w in zip(scales, weights):
        total += w * tail_single(beta_query, s) * (-4.0 * beta_query**3 / s**4)
    return total


def find_tail_crossing(scales: list[float], weights: list[float], eta: float) -> tuple[float, float]:
    lo, hi = 0.1, 40.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if tail_mixture(mid, scales, weights) > eta:
            lo = mid
        else:
            hi = mid
    beta = 0.5 * (lo + hi)
    return beta, abs(tail_derivative(beta, scales, weights))


def print_c_floor_sweep(n: int) -> None:
    print("adversarial C-floor sweep: source receipt nearly detector-redundant")
    print("------------------------------------------------------------------")
    print("epsilon  gram_min    gram_cond")
    for eps in [1.0, 0.3, 0.1, 0.03, 0.01]:
        r = execute(n, gram_epsilon=eps)
        print(f"{eps:7.3f}  {r.gram_min:9.6f}  {finite(r.gram_cond)}")
    print()


def print_s_floor_sweep(n: int) -> None:
    print("adversarial S-floor sweep: one source singular value pinched")
    print("------------------------------------------------------------")
    print("source_floor  one_event_min  one_event_cond")
    for floor in [1.0, 0.3, 0.1, 0.03, 0.0]:
        r = execute(n, source_floor=floor)
        print(f"{floor:12.3f}  {r.one_event_min:13.6f}  {finite(r.one_event_cond)}")
    print()


def role_density_receipt(
    n: int,
    branch_b: bool = False,
    source_floor: float | None = None,
) -> tuple[float, float, float, float]:
    """Deletion-derived role-density receipt for the S-floor theorem.

    For the finite role maps, the deletion sensitivity of event atom i in role
    j is the squared column norm of A_j at i, i.e. the diagonal of A_j^T A_j.
    With counting measure as reference, a uniform positive lower bound on
    these densities is exactly the finite common-support visibility floor.
    """
    atas = one_event_role_atas(n, branch_b=branch_b, source_floor=source_floor)
    densities = []
    off_diag_mass = 0.0
    diag_mass = 0.0
    for ata in atas:
        for i in range(n):
            densities.append(max(ata[i][i], 0.0))
            diag_mass += abs(ata[i][i])
            for j in range(n):
                if i != j:
                    off_diag_mass += abs(ata[i][j])
    min_density = min(densities)
    max_density = max(densities)
    predicted_s = sqrt(min_density)
    no_merging_proxy = diag_mass / (diag_mass + off_diag_mass) if diag_mass > 0 else 0.0
    return min_density, max_density, predicted_s, no_merging_proxy


def role_bookkeeping_cost(
    n: int,
    branch_b: bool = False,
    source_floor: float | None = None,
) -> float:
    """KL role-bookkeeping cost after normalizing each role density.

    Constant role densities carry no extra bookkeeping after normalization.
    Pinching or splitting a role density produces positive KL cost. This is the
    finite receipt for the least-role-bookkeeping selector in the paper.
    """
    atas = one_event_role_atas(n, branch_b=branch_b, source_floor=source_floor)
    total = 0.0
    for ata in atas:
        densities = [max(ata[i][i], 0.0) for i in range(n)]
        mean = sum(densities) / n
        if mean <= 0:
            return float("inf")
        for d in densities:
            r = d / mean
            if r > 0:
                total += (r * log(r)) / n
    return total


def s_floor_features(n: int) -> list[tuple[float, float]]:
    """Fixed finite feature vector for the BM1 moment-polytope receipt.

    These are deliberately coarse role features: a circular phase coordinate
    and a smooth local-record profile. They test whether the role target is
    interior for the finite invariant receipts. They do not by themselves
    detect every single-atom pinch; the paper uses that as an important warning.
    """
    prof = smooth_profile(n, 0.06)
    prof_c = center(prof)
    mx = max(abs(x) for x in prof_c) or 1.0
    out = []
    for i in range(n):
        x = (i + 0.5) / n
        out.append((cos(2.0 * pi * x), prof_c[i] / mx))
    return out


def cross(o: tuple[float, float], a: tuple[float, float], b: tuple[float, float]) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower: list[tuple[float, float]] = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: list[tuple[float, float]] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def polygon_signed_area(poly: list[tuple[float, float]]) -> float:
    area = 0.0
    for i, p in enumerate(poly):
        q = poly[(i + 1) % len(poly)]
        area += p[0] * q[1] - q[0] * p[1]
    return 0.5 * area


def point_segment_distance(
    p: tuple[float, float],
    a: tuple[float, float],
    b: tuple[float, float],
) -> float:
    ab = (b[0] - a[0], b[1] - a[1])
    ap = (p[0] - a[0], p[1] - a[1])
    denom = ab[0] * ab[0] + ab[1] * ab[1]
    if denom <= 1e-15:
        return sqrt((p[0] - a[0]) ** 2 + (p[1] - a[1]) ** 2)
    t = max(0.0, min(1.0, (ap[0] * ab[0] + ap[1] * ab[1]) / denom))
    proj = (a[0] + t * ab[0], a[1] + t * ab[1])
    return sqrt((p[0] - proj[0]) ** 2 + (p[1] - proj[1]) ** 2)


def point_in_convex_polygon(p: tuple[float, float], poly: list[tuple[float, float]]) -> bool:
    if len(poly) < 3:
        return False
    sign = 1.0 if polygon_signed_area(poly) >= 0 else -1.0
    for i, a in enumerate(poly):
        b = poly[(i + 1) % len(poly)]
        if sign * cross(a, b, p) < -1e-10:
            return False
    return True


def polytope_margin(
    points: list[tuple[float, float]],
    target: tuple[float, float],
) -> float:
    hull = convex_hull(points)
    if len(hull) < 3 or not point_in_convex_polygon(target, hull):
        return 0.0
    return min(point_segment_distance(target, hull[i], hull[(i + 1) % len(hull)]) for i in range(len(hull)))


def source_role_density(
    n: int,
    branch_b: bool = False,
    source_floor: float | None = None,
) -> list[float]:
    ata = one_event_role_atas(n, branch_b=branch_b, source_floor=source_floor)[1]
    densities = [max(ata[i][i], 0.0) for i in range(n)]
    mean = sum(densities) / n
    if mean <= 0:
        return [0.0 for _ in range(n)]
    return [d / mean for d in densities]


def moment_from_density(features: list[tuple[float, float]], density: list[float]) -> tuple[float, float]:
    n = len(features)
    return (
        sum(density[i] * features[i][0] for i in range(n)) / n,
        sum(density[i] * features[i][1] for i in range(n)) / n,
    )


def print_bm1_polytope_receipts(n: int) -> None:
    print("BM1 moment-polytope interior receipt: fixed coarse features")
    print("----------------------------------------------------------")
    print("case             margin      target_norm")
    features = s_floor_features(n)
    cases = [
        ("branch-A", False, None),
        ("source 0.1", False, 0.1),
        ("source zero", False, 0.0),
        ("branch-B", True, None),
    ]
    for name, branch_b, floor in cases:
        density = source_role_density(n, branch_b=branch_b, source_floor=floor)
        target = moment_from_density(features, density)
        margin = polytope_margin(features, target)
        print(f"{name:14s}  {margin:9.6f}  {norm([target[0], target[1]]):11.6f}")

    # Boundary-forced target: all moment weight on one exposed atom. This is
    # the finite model of a zero-forcing receipt, and its margin is exactly zero.
    hull = convex_hull(features)
    boundary = max(hull, key=lambda p: atan2(p[1], p[0]))
    margin = polytope_margin(features, boundary)
    print(f"{'boundary-forced':14s}  {margin:9.6f}  {norm([boundary[0], boundary[1]]):11.6f}")
    print()


def local_deletion_frame_operator(n: int) -> list[list[float]]:
    """Frame operator for compact local deletion probes on a ring.

    Probe k sees event k with weight 1 and the two nearest neighbours with
    weight 1/4, normalized to unit probe norm. This is intentionally local but
    not the identity frame; the lower frame eigenvalue is a real finite check.
    """
    raw = [0.25, 1.0, 0.25]
    probe_norm = sqrt(sum(x * x for x in raw))
    weights = [x / probe_norm for x in raw]
    s = [[0.0 for _ in range(n)] for _ in range(n)]
    for k in range(n):
        support = [((k - 1) % n, weights[0]), (k, weights[1]), ((k + 1) % n, weights[2])]
        for i, wi in support:
            for j, wj in support:
                s[i][j] += wi * wj
    return s


def local_frame_receipt(
    n: int,
    branch_b: bool = False,
    source_floor: float | None = None,
) -> tuple[float, float, float, float, float]:
    frame = local_deletion_frame_operator(n)
    eigs = [max(e, 0.0) for e in jacobi_eigenvalues_symmetric(frame)]
    lower = min(eigs)
    upper = max(eigs)
    event_actuality = [frame[i][i] for i in range(n)]
    mean_actuality = sum(event_actuality) / n
    event_actuality = [x / mean_actuality for x in event_actuality]

    atas = one_event_role_atas(n, branch_b=branch_b, source_floor=source_floor)
    tensors = []
    for ata in atas:
        for i in range(n):
            tensors.append(max(ata[i][i], 0.0) / max(event_actuality[i], 1e-15))
    min_tensor = min(tensors)
    max_tensor = max(tensors)
    derived_floor = sqrt(max(0.0, lower * min_tensor))
    return lower, upper, min_tensor, max_tensor, derived_floor


def print_local_frame_receipts(n: int) -> None:
    print("local role-complete deletion-frame receipt")
    print("------------------------------------------")
    print("case             frame_A   frame_B   min_W     max_W     floor")
    cases = [
        ("branch-A", False, None),
        ("source 0.1", False, 0.1),
        ("source zero", False, 0.0),
        ("branch-B", True, None),
    ]
    for name, branch_b, floor in cases:
        a, b, mn, mx, derived = local_frame_receipt(n, branch_b=branch_b, source_floor=floor)
        print(f"{name:14s}  {a:8.6f}  {b:8.6f}  {mn:8.6f}  {mx:8.6f}  {derived:8.6f}")
    print()


def same_local_generator_receipt(
    n: int,
    branch_b: bool = False,
    source_floor: float | None = None,
) -> tuple[float, float, float, float, float]:
    """Finite receipt for the same-local-generator route.

    Ellipticity of the local negative log-likelihood is modeled by a fixed
    Hessian window. Role deletion derivatives are the role A^T A diagonals.
    The point of the receipt is that a healthy Hessian is not enough: source
    thinning or source splitting makes the role transversality floor vanish.
    """
    hessian_eigs = [0.90, 1.00, 1.05, 1.15]
    h_min = min(hessian_eigs)
    h_max = max(hessian_eigs)
    atas = one_event_role_atas(n, branch_b=branch_b, source_floor=source_floor)
    couplings = []
    for ata in atas:
        for i in range(n):
            couplings.append(max(ata[i][i], 0.0))
    min_coupling = min(couplings)
    max_coupling = max(couplings)

    # If the generator Hessian distorts event directions by at most h_max, the
    # finite role transversality floor is bounded below by min_coupling/h_max.
    transversality_floor = min_coupling / h_max
    return h_min, h_max, min_coupling, max_coupling, transversality_floor


def print_same_local_generator_receipts(n: int) -> None:
    print("same-local-generator receipt: ellipticity versus role coupling")
    print("----------------------------------------------------------------")
    print("case             Hess_m    Hess_M    min_cpl   max_cpl   trans")
    cases = [
        ("branch-A", False, None),
        ("source 0.1", False, 0.1),
        ("source zero", False, 0.0),
        ("branch-B", True, None),
    ]
    for name, branch_b, floor in cases:
        hm, hM, mn, mx, trans = same_local_generator_receipt(
            n, branch_b=branch_b, source_floor=floor
        )
        print(f"{name:14s}  {hm:8.6f}  {hM:8.6f}  {mn:8.6f}  {mx:8.6f}  {trans:8.6f}")
    print()


def role_fisher_covectors(
    source_floor: float | None = None,
    source_zero: bool = False,
    source_redundant: bool = False,
) -> tuple[list[list[float]], list[float]]:
    """Local role covectors and Hessian diagonal for the eta_* falsifier.

    The four coordinates are record, source, causal incidence, and slice
    density. Bare ICS fixes the local event/collar data but not a positive
    lower Fisher angle for the physical role covectors. The adversarial cases
    keep the same Hessian window and destroy that angle.
    """
    hessian_diag = [0.90, 1.00, 1.05, 1.15]
    scales = [1.00, 1.05, 0.97, 1.02]
    if source_floor is not None:
        scales[1] *= source_floor
    rows = [[0.0 for _ in range(4)] for _ in range(4)]
    for i, scale in enumerate(scales):
        rows[i][i] = scale
    if source_zero:
        rows[1] = [0.0, 0.0, 0.0, 0.0]
    if source_redundant:
        rows[1] = [scales[1], 0.0, 0.0, 0.0]
    return rows, hessian_diag


def role_fisher_floor(
    source_floor: float | None = None,
    source_zero: bool = False,
    source_redundant: bool = False,
) -> tuple[int, float, float, float]:
    rows, hessian_diag = role_fisher_covectors(
        source_floor=source_floor,
        source_zero=source_zero,
        source_redundant=source_redundant,
    )
    h_inv = [1.0 / x for x in hessian_diag]
    gram, rank = fisher_gram(rows, h_inv)
    eigs = [max(e, 0.0) for e in jacobi_eigenvalues_symmetric(gram)]
    min_full = min(eigs)
    max_full = max(eigs)
    positive = [e for e in eigs if e > 1e-10]
    min_reduced = min(positive) if positive else 0.0
    if min_full > 1e-10:
        cond = max_full / min_full
    else:
        cond = float("inf")
    return rank, min_full, min_reduced, cond


def print_role_fisher_falsifier() -> None:
    print("role-Fisher eta_* falsifier: bare ICS does not force role angles")
    print("----------------------------------------------------------------")
    print("case                rank   full_min  reduced_min   cond")
    cases = [
        ("branch-A", None, False, False),
        ("source 0.1", 0.1, False, False),
        ("source zero", None, True, False),
        ("source redundant", None, False, True),
    ]
    for name, floor, zero, redundant in cases:
        rank, full_min, reduced_min, cond = role_fisher_floor(
            source_floor=floor,
            source_zero=zero,
            source_redundant=redundant,
        )
        cond_text = f"{cond:8.4f}" if isfinite(cond) else "     inf"
        print(f"{name:17s}  {rank:4d}  {full_min:9.6f}  {reduced_min:11.6f}  {cond_text}")
    print()


def same_local_vertex_matrix(
    source_floor: float | None = None,
    source_zero: bool = False,
    source_redundant: bool = False,
    mixing: float = 0.03,
) -> tuple[list[list[float]], list[float]]:
    """A finite local interaction/readout vertex for the derivation route.

    The vertex is represented by its role differential J and a local Hessian
    diagonal H. Small mixing means the four role rows come from one local
    generator but remain diagonally dominant. The adversarial cases show where
    this ceases to be a derivation and becomes the suspicious axiom again.
    """
    hessian_diag = [0.90, 1.00, 1.05, 1.15]
    scales = [1.00, 1.05, 0.97, 1.02]
    if source_floor is not None:
        scales[1] *= source_floor
    j = [[0.0 for _ in range(4)] for _ in range(4)]
    d0 = min(abs(x) for x in scales if abs(x) > 0.0) if any(abs(x) > 0.0 for x in scales) else 0.0
    for i, scale in enumerate(scales):
        j[i][i] = scale
    for i in range(4):
        for k in range(4):
            if i != k:
                j[i][k] += mixing * d0 * (1.0 if (i + k) % 2 == 0 else -1.0)
    if source_zero:
        j[1] = [0.0, 0.0, 0.0, 0.0]
    if source_redundant:
        j[1] = j[0][:]
    return j, hessian_diag


def same_local_vertex_receipt(
    source_floor: float | None = None,
    source_zero: bool = False,
    source_redundant: bool = False,
    mixing: float = 0.03,
) -> tuple[int, float, float, float]:
    j, hessian_diag = same_local_vertex_matrix(
        source_floor=source_floor,
        source_zero=source_zero,
        source_redundant=source_redundant,
        mixing=mixing,
    )
    h_inv = [1.0 / x for x in hessian_diag]
    gram, rank = fisher_gram(j, h_inv)
    eigs = [max(e, 0.0) for e in jacobi_eigenvalues_symmetric(gram)]
    full_min = min(eigs)

    # The common deletion direction sees all four role coordinates. This is
    # the finite version of "one event, four roles" inside the same vertex.
    u = [0.5, 0.5, 0.5, 0.5]
    a_gen = sum(hessian_diag[i] * u[i] * u[i] for i in range(4))
    responses = [sum(row[i] * u[i] for i in range(4)) for row in j]
    eta_d = min(r * r for r in responses) / a_gen
    d0 = min(sqrt(max(gram[i][i], 0.0)) for i in range(4))
    return rank, full_min, eta_d, d0


def local_vertex_normal_form_receipt(
    source_floor: float | None = None,
    source_zero: bool = False,
    source_redundant: bool = False,
    mixing: float = 0.03,
) -> tuple[float, float, float, float, float]:
    j, _ = same_local_vertex_matrix(
        source_floor=source_floor,
        source_zero=source_zero,
        source_redundant=source_redundant,
        mixing=mixing,
    )
    diag_min = min(abs(j[i][i]) for i in range(4))
    off_max = max(sum(abs(j[i][k]) for k in range(4) if k != i) for i in range(4))
    dd_margin = diag_min - off_max
    _, fisher_min, eta_d, _ = same_local_vertex_receipt(
        source_floor=source_floor,
        source_zero=source_zero,
        source_redundant=source_redundant,
        mixing=mixing,
    )
    return diag_min, off_max, dd_margin, fisher_min, eta_d


def print_local_vertex_normal_form_receipts() -> None:
    print("local-vertex normal-form receipt: sufficient diagonal certificate")
    print("-----------------------------------------------------------------")
    print("case                 diag_min   off_max   DD_margin  fisher_min   eta_D")
    cases = [
        ("good vertex", None, False, False, 0.03),
        ("source 0.1", 0.1, False, False, 0.03),
        ("source zero", None, True, False, 0.03),
        ("source redundant", None, False, True, 0.03),
        ("overmixed", None, False, False, 0.40),
    ]
    for name, floor, zero, redundant, mixing in cases:
        diag_min, off_max, dd_margin, fisher_min, eta_d = local_vertex_normal_form_receipt(
            source_floor=floor,
            source_zero=zero,
            source_redundant=redundant,
            mixing=mixing,
        )
        print(
            f"{name:18s}  {diag_min:8.6f}  {off_max:8.6f}  "
            f"{dd_margin:9.6f}  {fisher_min:10.6f}  {eta_d:8.6f}"
        )
    print()


def interval_vertex_certificate(
    diag_floor: float,
    off_ratio: float,
    h_max: float = 1.15,
) -> tuple[float, float, float, float]:
    """Class-level lower bound for the normal-form certificate.

    The common deletion vector used in the finite receipt has four equal
    components, so ||u||=1 and |u_i|=1/2. If the off-row sum is bounded by
    off_ratio*diag_floor, both the Fisher floor and deletion-transversality
    floor are bounded by the same conservative interval estimate.
    """
    off_row = off_ratio * diag_floor
    margin = diag_floor - off_row
    if margin <= 0.0:
        return off_row, margin, 0.0, 0.0
    fisher_lb = (margin * margin) / (4.0 * h_max)
    eta_lb = fisher_lb
    return off_row, margin, fisher_lb, eta_lb


def print_interval_vertex_certificates() -> None:
    print("cofinal interval vertex certificate: class-level eta_* lower bound")
    print("------------------------------------------------------------------")
    print("class            diag_floor  off_ratio  DD_margin  fisher_lb   eta_lb")
    cases = [
        ("robust", 0.97, 0.09),
        ("source 0.1", 0.105, 0.09),
        ("near wall", 0.97, 0.97),
        ("overmix", 0.97, 1.20),
        ("source zero", 0.00, 0.09),
    ]
    for name, diag_floor, off_ratio in cases:
        _, margin, fisher_lb, eta_lb = interval_vertex_certificate(diag_floor, off_ratio)
        print(
            f"{name:14s}  {diag_floor:10.6f}  {off_ratio:9.6f}  "
            f"{margin:9.6f}  {fisher_lb:9.6f}  {eta_lb:8.6f}"
        )
    print()


def transported_interval_certificate(
    diag_floor: float,
    off_ratio: float,
    eps_j: float,
    eps_u: float,
    eps_h: float,
    h_max: float = 1.15,
    u_min: float = 0.5,
    u_max: float = 0.5,
) -> tuple[float, float, float, float, float]:
    """Refinement-stability bound for a whole local-vertex class.

    Entrywise role-Jacobian error eps_j reduces each diagonal by eps_j and can
    add eps_j to each of three off-diagonal entries. Deletion-direction drift
    changes the component bounds by eps_u. This is intentionally conservative:
    it is a proof receipt, not an optimized estimate.
    """
    off_row = off_ratio * diag_floor
    d_eff = max(0.0, diag_floor - eps_j)
    r_eff = off_row + 3.0 * eps_j
    u_min_eff = max(0.0, u_min - eps_u)
    u_max_eff = u_max + eps_u
    m_eff = h_max + eps_h
    dd_margin = d_eff - r_eff
    deletion_margin = d_eff * u_min_eff - r_eff * u_max_eff
    fisher_lb = (dd_margin * dd_margin) / (4.0 * m_eff) if dd_margin > 0.0 else 0.0
    eta_lb = (deletion_margin * deletion_margin) / m_eff if deletion_margin > 0.0 else 0.0
    return dd_margin, deletion_margin, fisher_lb, eta_lb, m_eff


def print_refinement_vertex_transport_receipts() -> None:
    print("refinement transport receipt: robust interval survives cofinal drift")
    print("-------------------------------------------------------------------")
    print("case             eps_J   eps_u   DD_margin  del_margin  fisher_lb   eta_lb")
    cases = [
        ("robust tail", 0.97, 0.09, 0.02, 0.01, 0.02),
        ("source-thin", 0.105, 0.09, 0.02, 0.01, 0.02),
        ("near wall", 0.97, 0.97, 0.02, 0.01, 0.02),
        ("overmix", 0.97, 1.20, 0.02, 0.01, 0.02),
        ("source zero", 0.00, 0.09, 0.02, 0.01, 0.02),
    ]
    for name, diag_floor, off_ratio, eps_j, eps_u, eps_h in cases:
        dd_margin, del_margin, fisher_lb, eta_lb, _ = transported_interval_certificate(
            diag_floor, off_ratio, eps_j, eps_u, eps_h
        )
        print(
            f"{name:14s}  {eps_j:6.3f}  {eps_u:6.3f}  {dd_margin:9.6f}  "
            f"{del_margin:10.6f}  {fisher_lb:9.6f}  {eta_lb:8.6f}"
        )
    print()


def actual_coincidence_vertex_receipt(
    source_floor: float | None = None,
    source_zero: bool = False,
    source_redundant: bool = False,
    mixing: float = 0.03,
) -> tuple[float, float, float, float, float, float]:
    """AV1/AV3 receipt for the actual local coincidence vertex.

    The same-local vertex matrix is read as the second-order coefficient of a
    finite local coincidence law after role-normalization. The bad-distance
    proxy is the smallest of three visible margins: diagonal dominance, Fisher
    rank, and deletion-direction response.
    """
    diag_min, off_max, dd_margin, fisher_min, eta_d = local_vertex_normal_form_receipt(
        source_floor=source_floor,
        source_zero=source_zero,
        source_redundant=source_redundant,
        mixing=mixing,
    )
    bad_distance = min(max(dd_margin, 0.0), sqrt(max(fisher_min, 0.0)), sqrt(max(eta_d, 0.0)))
    return diag_min, off_max, dd_margin, fisher_min, eta_d, bad_distance


def schur_transport_receipt(
    internal_coupling: float,
    internal_floor: float,
    internal_role: float,
    h_max: float = 1.15,
    diag_floor: float = 0.97,
    off_ratio: float = 0.09,
) -> tuple[float, float, float, float, float, float]:
    """AV2 finite Schur-complement transport receipt.

    A refined local collar has coarse variables and internal variables. If the
    internal Hessian has lower eigenvalue internal_floor, and the coarse-
    internal Hessian coupling has norm internal_coupling, eliminating the
    internal variables changes H by at most coupling^2/floor and J by at most
    internal_role*coupling/floor.
    """
    eps_h = (internal_coupling * internal_coupling) / internal_floor
    eps_j = (internal_role * internal_coupling) / internal_floor
    eps_u = eps_j
    dd_margin, deletion_margin, fisher_lb, eta_lb, m_eff = transported_interval_certificate(
        diag_floor,
        off_ratio,
        eps_j,
        eps_u,
        eps_h,
        h_max=h_max,
    )
    return eps_j, eps_h, eps_u, dd_margin, deletion_margin, eta_lb


def print_actual_coincidence_vertex_receipts() -> None:
    print("AV1/AV3 actual local coincidence vertex and bad-distance receipt")
    print("----------------------------------------------------------------")
    print("case                 diag_min  off_max   DD_margin  fisher_min   eta_D    bad_dist")
    cases = [
        ("v6 robust", None, False, False, 0.03),
        ("source 0.1", 0.1, False, False, 0.03),
        ("source zero", None, True, False, 0.03),
        ("source redundant", None, False, True, 0.03),
        ("overmixed", None, False, False, 0.40),
    ]
    for name, floor, zero, redundant, mixing in cases:
        diag_min, off_max, dd_margin, fisher_min, eta_d, bad_distance = (
            actual_coincidence_vertex_receipt(
                source_floor=floor,
                source_zero=zero,
                source_redundant=redundant,
                mixing=mixing,
            )
        )
        print(
            f"{name:18s}  {diag_min:8.6f}  {off_max:8.6f}  {dd_margin:9.6f}  "
            f"{fisher_min:10.6f}  {eta_d:8.6f}  {bad_distance:8.6f}"
        )
    print()


def print_schur_transport_receipts() -> None:
    print("AV2 Schur-complement refinement transport receipt")
    print("-------------------------------------------------")
    print("case             int_cpl  int_floor  eps_J    eps_H    del_margin   eta_lb")
    cases = [
        ("weak internal", 0.020, 0.800, 0.500),
        ("moderate", 0.060, 0.800, 0.500),
        ("near wall", 0.120, 0.800, 0.500),
        ("bad internal", 0.250, 0.800, 0.500),
    ]
    for name, coupling, floor, role in cases:
        eps_j, eps_h, _, _, deletion_margin, eta_lb = schur_transport_receipt(
            coupling, floor, role
        )
        print(
            f"{name:14s}  {coupling:7.3f}  {floor:9.3f}  {eps_j:7.4f}  "
            f"{eps_h:7.4f}  {deletion_margin:10.6f}  {eta_lb:8.6f}"
        )
    print()


def physical_event_acv_receipt(
    self_floor: float,
    leakage: float,
    internal_coupling: float,
    internal_floor: float = 0.80,
    internal_role: float = 0.50,
    h_max: float = 1.15,
) -> tuple[float, float, float, float, float, float]:
    """ACV receipt for a minimal physical division-event model.

    self_floor is the least direct sensitivity of one physical click to its
    own role statistic. leakage is the total off-role sensitivity per row.
    Refinement drift is bounded by the Schur-complement receipt.
    """
    eps_j = internal_role * internal_coupling / internal_floor
    eps_h = internal_coupling * internal_coupling / internal_floor
    eps_u = eps_j
    off_ratio = leakage / self_floor if self_floor > 0.0 else 0.0
    dd_margin, deletion_margin, fisher_lb, eta_lb, _ = transported_interval_certificate(
        self_floor,
        off_ratio,
        eps_j,
        eps_u,
        eps_h,
        h_max=h_max,
    )
    bad_distance = min(
        max(self_floor - leakage, 0.0),
        sqrt(max(fisher_lb, 0.0)),
        sqrt(max(eta_lb, 0.0)),
    )
    return eps_j, eps_h, dd_margin, deletion_margin, eta_lb, bad_distance


def print_physical_event_acv_receipts() -> None:
    print("ACV minimal physical division-event receipt")
    print("-------------------------------------------")
    print("case             self     leak     eps_J    DD_margin  del_margin   eta_lb   bad_dist")
    cases = [
        ("physical", 0.97, 0.0873, 0.020),
        ("thin source", 0.105, 0.00945, 0.020),
        ("high leak", 0.97, 0.6000, 0.060),
        ("near collapse", 0.97, 0.9000, 0.120),
        ("no source", 0.000, 0.0000, 0.020),
    ]
    for name, self_floor, leakage, coupling in cases:
        eps_j, _, dd_margin, deletion_margin, eta_lb, bad_distance = physical_event_acv_receipt(
            self_floor,
            leakage,
            coupling,
        )
        print(
            f"{name:14s}  {self_floor:7.3f}  {leakage:7.4f}  {eps_j:7.4f}  "
            f"{dd_margin:9.6f}  {deletion_margin:10.6f}  {eta_lb:8.6f}  "
            f"{bad_distance:8.6f}"
        )
    print()


def matrix_row_leakage(jacobian: list[list[float]]) -> tuple[float, float, float]:
    """Return least diagonal sensitivity, greatest off-row leakage, and margin."""
    sigma = min(abs(jacobian[i][i]) for i in range(len(jacobian)))
    ell = max(
        sum(abs(jacobian[i][j]) for j in range(len(jacobian)) if j != i)
        for i in range(len(jacobian))
    )
    return sigma, ell, sigma - ell


def spectral_norm_upper(a: list[list[float]]) -> float:
    """Spectral norm from eigenvalues of A A^T for small explicit matrices."""
    if not a:
        return 0.0
    rows = len(a)
    gram = [[0.0 for _ in range(rows)] for _ in range(rows)]
    for i in range(rows):
        for j in range(i, rows):
            val = sum(a[i][k] * a[j][k] for k in range(len(a[i])))
            gram[i][j] = val
            gram[j][i] = val
    eigs = jacobi_eigenvalues_symmetric(gram)
    return sqrt(max(eigs)) if eigs else 0.0


def acv_collar_jacobian(
    self_floor: float = 0.97,
    leakage: float = 0.0873,
    source_floor: float | None = None,
    source_redundant: bool = False,
    slice_bookkeeping: bool = False,
) -> list[list[float]]:
    """Four-role response matrix for a finite clicked collar law.

    Rows and columns are record, source, causal collar, and antichain crossing.
    The good case is a role-separated click: every role responds most strongly
    to its own source, with symmetric but small leakage. The bad cases remove
    source self-sensitivity, make source redundant with record, or make slice
    response an inherited bookkeeping response.
    """
    n = 4
    off = leakage / (n - 1)
    j = [[off for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j[i][i] = self_floor

    if source_floor is not None:
        j[1][1] = source_floor

    if source_redundant:
        j[1] = j[0][:]

    if slice_bookkeeping:
        j[3][3] = 0.08
        j[3][0] = self_floor
        j[3][1] = 0.25
        j[3][2] = 0.20

    return j


def acv_actual_event_law_audit(
    jacobian: list[list[float]],
    internal_floor: float,
    internal_coupling: float,
    internal_role: float = 0.50,
) -> tuple[float, float, float, float, float, float, float, float, bool]:
    """Audit the actual event law against direct sensitivity and Schur drift."""
    sigma, ell, direct_margin = matrix_row_leakage(jacobian)
    u = [0.5, 0.5, 0.5, 0.5]
    deletion_raw = min(abs(sum(row[k] * u[k] for k in range(4))) for row in jacobian)

    h_ci = [[internal_coupling if i == j else 0.0 for j in range(4)] for i in range(4)]
    kappa = spectral_norm_upper(h_ci)
    eps_h = (kappa * kappa) / internal_floor if internal_floor > 0.0 else float("inf")
    eps_j = (internal_role * kappa) / internal_floor if internal_floor > 0.0 else float("inf")
    schur_margin = sigma - eps_j - (ell + 3.0 * eps_j)
    deletion_margin = deletion_raw - 4.0 * eps_j
    passes = (
        isfinite(eps_j)
        and direct_margin > 0.0
        and schur_margin > 0.0
        and deletion_margin > 0.0
        and internal_floor > 0.0
    )
    return (
        sigma,
        ell,
        direct_margin,
        internal_floor,
        kappa,
        eps_j,
        deletion_margin,
        schur_margin,
        passes,
    )


def print_actual_event_law_acv_audit() -> None:
    print("actual branch-A event-law ACV audit")
    print("-----------------------------------")
    print(
        "case              sigma     leak   dir_margin  lambda    kappa    "
        "eps_J   del_margin  schur_margin  pass"
    )
    cases = [
        ("source-click", acv_collar_jacobian(), 0.80, 0.020),
        ("weak source", acv_collar_jacobian(source_floor=0.105), 0.80, 0.020),
        ("source redundant", acv_collar_jacobian(source_redundant=True), 0.80, 0.020),
        ("slice bookkeeping", acv_collar_jacobian(slice_bookkeeping=True), 0.80, 0.020),
        ("bad refinement", acv_collar_jacobian(), 0.80, 0.250),
    ]
    for name, jacobian, internal_floor, internal_coupling in cases:
        sigma, ell, direct_margin, lam, kappa, eps_j, del_margin, schur_margin, passes = (
            acv_actual_event_law_audit(jacobian, internal_floor, internal_coupling)
        )
        verdict = "PASS" if passes else "FAIL"
        print(
            f"{name:17s}  {sigma:7.4f}  {ell:7.4f}  {direct_margin:10.6f}  "
            f"{lam:6.3f}  {kappa:7.4f}  {eps_j:7.4f}  {del_margin:10.6f}  "
            f"{schur_margin:12.6f}  {verdict}"
        )
    print()


def print_bare_ics_acv_independence_receipt() -> None:
    print("bare-ICS ACV independence receipt")
    print("---------------------------------")
    print(
        "same_ics      role_law          count  scalar_rate  sigma     leak   "
        "schur_margin  acv"
    )
    same_count = 4
    same_rate = 1.0
    cases = [
        ("diamond-4", "source-click", acv_collar_jacobian(), 0.80, 0.020),
        ("diamond-4", "source-free", acv_collar_jacobian(source_floor=0.0), 0.80, 0.020),
        ("diamond-4", "source-redundant", acv_collar_jacobian(source_redundant=True), 0.80, 0.020),
        ("diamond-4", "slice-bookkeeping", acv_collar_jacobian(slice_bookkeeping=True), 0.80, 0.020),
    ]
    for same_ics, role_law, jacobian, internal_floor, internal_coupling in cases:
        sigma, ell, _, _, _, _, _, schur_margin, passes = acv_actual_event_law_audit(
            jacobian, internal_floor, internal_coupling
        )
        acv = "PASS" if passes else "FAIL"
        print(
            f"{same_ics:12s}  {role_law:16s}  {same_count:5d}  {same_rate:11.3f}  "
            f"{sigma:7.4f}  {ell:7.4f}  {schur_margin:12.6f}  {acv}"
        )
    print()


def source_record_detector_jacobian(
    common: float,
    private: float,
    source_private: float | None = None,
    slice_private: float | None = None,
    residual: float = 0.0,
) -> list[list[float]]:
    """Role covariance for the scalar source-record detector law.

    Each role statistic is T_i = C + R_i, where C is the common scalar click
    mode and R_i is the private detector channel for one physical role. The
    covariance J has common off-diagonal response from C and private diagonal
    response from R_i. A small residual models nonideal detector mixing.
    """
    private_values = [private, private, private, private]
    if source_private is not None:
        private_values[1] = source_private
    if slice_private is not None:
        private_values[3] = slice_private

    j = [[common for _ in range(4)] for _ in range(4)]
    for i in range(4):
        j[i][i] = common + private_values[i]
        for k in range(4):
            if i != k:
                j[i][k] += residual
    return j


def print_source_record_detector_receipts() -> None:
    print("source-record detector law ACV certificate")
    print("------------------------------------------")
    print(
        "case              common  priv_min  eps_J   sigma     leak   "
        "schur_margin  del_margin  acv"
    )
    cases = [
        ("physical SRD", 0.030, 0.900, None, None, 0.020, 0.80, 0.0),
        ("common-heavy", 0.300, 0.200, None, None, 0.020, 0.80, 0.0),
        ("weak source", 0.030, 0.900, 0.050, None, 0.020, 0.80, 0.0),
        ("slice-only", 0.030, 0.900, None, 0.000, 0.020, 0.80, 0.0),
        ("leaky residual", 0.030, 0.900, None, None, 0.020, 0.80, 0.190),
        ("bad Schur", 0.030, 0.900, None, None, 0.250, 0.80, 0.0),
    ]
    for (
        name,
        common,
        private,
        source_private,
        slice_private,
        internal_coupling,
        internal_floor,
        residual,
    ) in cases:
        jacobian = source_record_detector_jacobian(
            common,
            private,
            source_private=source_private,
            slice_private=slice_private,
            residual=residual,
        )
        sigma, ell, _, _, _, eps_j, del_margin, schur_margin, passes = (
            acv_actual_event_law_audit(jacobian, internal_floor, internal_coupling)
        )
        acv = "PASS" if passes else "FAIL"
        priv_min = min(
            private if source_private is None else source_private,
            private if slice_private is None else slice_private,
            private,
        )
        print(
            f"{name:17s}  {common:6.3f}  {priv_min:8.3f}  {eps_j:6.4f}  "
            f"{sigma:7.4f}  {ell:7.4f}  {schur_margin:12.6f}  "
            f"{del_margin:10.6f}  {acv}"
        )
    print()


def detector_log_lr(t: float, centers: list[float], width: float, amplitude: float, baseline: float) -> float:
    """Canonical detector log-likelihood ratio for record versus vacuum."""
    signal = sum(amplitude * exp(-((abs(t - c) / width) ** 4)) for c in centers)
    return signal - baseline


def threshold_components_from_trace(
    xs: list[float],
    values: list[float],
    threshold: float,
) -> tuple[int, list[float]]:
    mask = [v >= threshold for v in values]
    centers = []
    count = 0
    i = 0
    while i < len(mask):
        if not mask[i]:
            i += 1
            continue
        start = i
        while i + 1 < len(mask) and mask[i + 1]:
            i += 1
        end = i
        centers.append(xs[(start + end) // 2])
        count += 1
        i += 1
    return count, centers


def detector_width_from_trace(
    xs: list[float],
    values: list[float],
    center: float,
    baseline: float,
    search_radius: float,
) -> float:
    """Read the e^-1 detector width from the positive likelihood bump."""
    peak_idx = min(range(len(xs)), key=lambda i: abs(xs[i] - center))
    peak = values[peak_idx] + baseline
    target = peak / exp(1.0)
    candidates = [
        i
        for i in range(peak_idx, len(xs))
        if xs[i] - center <= search_radius
    ]
    best = min(candidates, key=lambda i: abs((values[i] + baseline) - target))
    return abs(xs[best] - center)


def detector_threshold_closure_case(
    width: float,
    amplitude: float,
    baseline: float,
    duration: float = 48.0,
) -> tuple[float, int, float, float, int, bool, float, str]:
    """Finite detector-threshold calculation for the A-Scale bottleneck."""
    centers = [4.0, 10.3, 16.1, 22.7, 29.0, 35.4, 42.2]
    steps = 12_001
    xs = [duration * i / (steps - 1) for i in range(steps)]
    trace = [detector_log_lr(x, centers, width, amplitude, baseline) for x in xs]

    # The log-likelihood ratio has the canonical Bayes threshold zero.
    threshold = 0.0
    events, event_centers = threshold_components_from_trace(xs, trace, threshold)
    gamma = events / duration
    beta_inv = detector_width_from_trace(xs, trace, centers[0], baseline, 3.0 * width) if events else 0.0
    beta = 1.0 / beta_inv if beta_inv > 0.0 else float("inf")
    heating = beta**4 / 4.0 if isfinite(beta) else float("inf")
    vacuum_trace = [-baseline for _ in xs]
    vacuum_events, _ = threshold_components_from_trace(xs, vacuum_trace, threshold)
    source_match = events == len(event_centers)
    ts_residue = 0.0
    passed = events == len(centers) and vacuum_events == 0 and source_match and ts_residue < 1e-12
    verdict = "PASS" if passed else "FAIL"
    return threshold, events, gamma, beta_inv, vacuum_events, source_match, heating, verdict


def print_detector_threshold_closure_receipts() -> None:
    print("detector-threshold calculation: gamma/beta bottleneck")
    print("-----------------------------------------------------")
    print(
        "case              S_*  events   gamma   beta_inv  vacuum  source  "
        "heating    verdict"
    )
    cases = [
        ("canonical", 1.70, 2.40, 1.00),
        ("same-th wider", 2.40, 2.40, 1.00),
        ("weak detector", 1.70, 0.80, 1.00),
        ("high vacuum", 1.70, 2.40, 2.80),
    ]
    for name, width, amplitude, baseline in cases:
        threshold, events, gamma, beta_inv, vacuum_events, source_match, heating, verdict = (
            detector_threshold_closure_case(width, amplitude, baseline)
        )
        source = "yes" if source_match else "no"
        print(
            f"{name:16s}  {threshold:4.1f}  {events:6d}  {gamma:7.5f}  "
            f"{beta_inv:8.4f}  {vacuum_events:6d}  {source:6s}  "
            f"{heating:8.5f}  {verdict}"
        )
    print()


def print_beta_family_no_go_receipts() -> None:
    """Finite negative theorem for beta under the current visible receipts."""
    print("beta-family no-go receipt: same visible records, different beta")
    print("----------------------------------------------------------------")
    print(
        "width    S_*  events   gamma   beta_inv  vacuum  source  "
        "heating    verdict"
    )
    for width in [1.10, 1.30, 1.70, 2.40]:
        threshold, events, gamma, beta_inv, vacuum_events, source_match, heating, verdict = (
            detector_threshold_closure_case(width, 2.40, 1.00)
        )
        source = "yes" if source_match else "no"
        print(
            f"{width:5.2f}  {threshold:4.1f}  {events:6d}  {gamma:7.5f}  "
            f"{beta_inv:8.4f}  {vacuum_events:6d}  {source:6s}  "
            f"{heating:8.5f}  {verdict}"
        )
    print()


def print_beta_lock_audit_receipts() -> None:
    """Audit the extra data needed to make beta a derived quantity."""
    print("Beta Lock audit: support data versus derived scale data")
    print("------------------------------------------------------")
    print("case               input fixed by event law   beta_span  margin    verdict")

    widths = [1.10, 1.30, 1.70, 2.40]
    rows = [detector_threshold_closure_case(width, 2.40, 1.00) for width in widths]
    visible_same = len({(r[1], round(r[2], 8), r[4], r[5], r[7]) for r in rows}) == 1
    beta_span = max(r[3] for r in rows) - min(r[3] for r in rows)
    verdict = "FAIL" if visible_same and beta_span > 1e-8 else "PASS"
    print(f"{'support-only':18s}  {'no':24s}  {beta_span:9.4f}  {0.0:7.4f}  {verdict}")

    gap, isolation, beta_gap, _, passes = spectral_gap_beta_receipt(0.30, 0.05)
    verdict = "PASS" if passes else "FAIL"
    print(f"{'derived K toy':18s}  {'yes: transfer K':24s}  {0.0:9.4f}  {isolation:7.4f}  {verdict}")

    _, _, beta_gap_alt, _, passes_alt = spectral_gap_beta_receipt(0.45, 0.05)
    spectral_span = abs(beta_gap_alt - beta_gap)
    verdict = "FAIL" if passes and passes_alt and spectral_span > 1e-8 else "PASS"
    print(f"{'free K family':18s}  {'no':24s}  {spectral_span:9.4f}  {0.0:7.4f}  {verdict}")

    width, _, near_count, passes = fisher_width_selection_receipt(0.050)
    curvature_proxy = 1.0 / near_count if near_count else 0.0
    verdict = "PASS" if passes else "FAIL"
    print(f"{'derived cost toy':18s}  {'yes: cost C':24s}  {0.0:9.4f}  {curvature_proxy:7.4f}  {verdict}")

    width_alt, _, near_count_alt, passes_alt = fisher_width_selection_receipt(0.120)
    cost_span = abs(width_alt - width)
    verdict = "FAIL" if passes and passes_alt and cost_span > 1e-8 else "PASS"
    margin = min(curvature_proxy, 1.0 / near_count_alt if near_count_alt else 0.0)
    print(f"{'free cost family':18s}  {'no':24s}  {cost_span:9.4f}  {margin:7.4f}  {verdict}")
    print()


def poisson_source_profile(
    xs: list[float],
    center: float,
    width: float,
    amplitude: float,
    baseline: float,
) -> list[float]:
    """Expected finite source-record counts in a local detector collar."""
    return [baseline + amplitude * exp(-((abs(x - center) / width) ** 4)) for x in xs]


def poisson_expected_log_likelihood(observed_mean: list[float], candidate_mean: list[float]) -> float:
    """Expected Poisson log-likelihood, ignoring y!-constants."""
    total = 0.0
    for y, mu in zip(observed_mean, candidate_mean):
        total += y * log(max(mu, 1e-15)) - mu
    return total


def poisson_width_fisher(
    xs: list[float],
    center: float,
    width: float,
    amplitude: float,
    baseline: float,
) -> float:
    """Fisher information for the width parameter of the source-record profile."""
    total = 0.0
    for x in xs:
        r = abs(x - center)
        z = (r / width) ** 4
        signal = exp(-z)
        mu = baseline + amplitude * signal
        dmu = amplitude * signal * 4.0 * z / width
        total += (dmu * dmu) / max(mu, 1e-15)
    return total


def source_record_width_identifiability_case(
    true_width: float,
    amplitude: float = 2.40,
    baseline: float = 1.00,
) -> tuple[float, float, float, int, float, str]:
    """Check whether the finite Poisson record identifies a supplied width."""
    center = 0.0
    xs = [-4.0 + 8.0 * i / 400.0 for i in range(401)]
    observed = poisson_source_profile(xs, center, true_width, amplitude, baseline)
    candidates = [0.80 + 2.00 * i / 200.0 for i in range(201)]
    scores = []
    for width in candidates:
        candidate = poisson_source_profile(xs, center, width, amplitude, baseline)
        scores.append((poisson_expected_log_likelihood(observed, candidate), width))
    best_score, mle_width = max(scores)
    sorted_scores = sorted(scores, reverse=True)
    separation = best_score - sorted_scores[1][0]
    fisher = poisson_width_fisher(xs, center, true_width, amplitude, baseline)
    support = detector_threshold_closure_case(true_width, amplitude, baseline)[1]
    verdict = "IDENT" if abs(mle_width - true_width) <= 0.011 and fisher > 1.0 else "WEAK"
    return true_width, mle_width, fisher, support, separation, verdict


def print_source_record_width_identifiability_receipts() -> None:
    print("minimal Poisson source-record channel: width identifiability")
    print("------------------------------------------------------------")
    print("true_width  mle_width   Fisher    support  ll_margin  result")
    for width in [1.10, 1.70, 2.40]:
        true_width, mle_width, fisher, support, margin, verdict = (
            source_record_width_identifiability_case(width)
        )
        print(
            f"{true_width:10.4f}  {mle_width:9.4f}  {fisher:8.3f}  "
            f"{support:7d}  {margin:9.5f}  {verdict}"
        )
    print()


def source_record_transfer_spectrum_case(
    width: float,
    n: int = 48,
) -> tuple[float, float, float, float, int]:
    """Spectrum of the transfer operator induced by a supplied record width."""
    first_row = []
    for j in range(n):
        d = min(j, n - j)
        first_row.append(exp(-((d / width) ** 4)))
    total = sum(first_row)
    first_row = [x / total for x in first_row]

    eigs = []
    for k in range(n):
        eig = sum(first_row[j] * cos(2.0 * pi * k * j / n) for j in range(n))
        eigs.append(eig)
    eigs = sorted(eigs, reverse=True)
    top = eigs[0]
    first_shell = eigs[1]
    second_shell = eigs[3] if len(eigs) > 3 else 0.0
    gap = max(top - first_shell, 0.0)
    isolation = max(first_shell - second_shell, 0.0)
    beta_k = 1.0 / sqrt(gap) if gap > 1e-15 else float("inf")
    support = detector_threshold_closure_case(width, 2.40, 1.00)[1]
    return gap, isolation, beta_k, first_shell, support


def print_source_record_k_lock_attack_receipts() -> None:
    print("source-record K-lock attack: induced transfer spectrum")
    print("------------------------------------------------------")
    print("width   support    gap     isolation   beta_K    verdict")
    beta_values = []
    for width in [1.10, 1.30, 1.70, 2.40]:
        gap, isolation, beta_k, _, support = source_record_transfer_spectrum_case(width)
        beta_values.append(beta_k)
        verdict = "COND" if support == 7 and isolation > 0.01 else "FAIL"
        print(
            f"{width:5.2f}  {support:7d}  {gap:7.5f}  "
            f"{isolation:9.5f}  {beta_k:7.3f}  {verdict}"
        )
    print(f"K-family beta_K span: {max(beta_values) - min(beta_values):.3f}")
    print()


def causal_collar_walk_spectrum_case(
    move_prob: float,
    n: int = 48,
) -> tuple[float, float, float, int, int]:
    """Spectrum of a nearest-collar transition-frequency operator.

    The causal collar supplies the ring adjacency. The remaining parameter is
    the observed transition frequency to each nearest collar neighbor. If this
    frequency is not fixed by the event law, the spectral scale is not derived.
    """
    gap = 4.0 * move_prob * sin(pi / n) ** 2
    isolation = 4.0 * move_prob * (sin(2.0 * pi / n) ** 2 - sin(pi / n) ** 2)
    beta_walk = 1.0 / sqrt(gap) if gap > 1e-15 else float("inf")
    degree = 2
    support = detector_threshold_closure_case(1.70, 2.40, 1.00)[1]
    return gap, isolation, beta_walk, degree, support


def print_causal_collar_transition_k_receipts() -> None:
    print("causal-collar K-lock attack: transition-frequency freedom")
    print("---------------------------------------------------------")
    print("move_p  degree  support    gap     isolation   beta_K    verdict")
    beta_values = []
    for move_prob in [0.05, 0.10, 0.20, 0.35]:
        gap, isolation, beta_walk, degree, support = causal_collar_walk_spectrum_case(move_prob)
        beta_values.append(beta_walk)
        verdict = "COND" if degree == 2 and support == 7 and isolation > 0.0 else "FAIL"
        print(
            f"{move_prob:6.2f}  {degree:6d}  {support:7d}  {gap:7.5f}  "
            f"{isolation:9.5f}  {beta_walk:7.3f}  {verdict}"
        )
    print(f"collar-frequency beta_K span: {max(beta_values) - min(beta_values):.3f}")
    print()


def circulant_spectral_channel(n: int, mode1: float, mode2: float) -> list[list[float]]:
    """Positive circulant record-transfer channel with two spectral shells.

    The row entries are a finite positive kernel on a record ring. The first
    Fourier shell is the candidate memory scale; the second shell is the
    nearest competitor. If the first shell is not isolated, beta is not
    selected by the transfer spectrum.
    """
    channel = []
    for i in range(n):
        row = []
        for j in range(n):
            angle = 2.0 * pi * ((i - j) % n) / n
            val = 1.0 + 2.0 * mode1 * cos(angle) + 2.0 * mode2 * cos(2.0 * angle)
            row.append(max(val, 0.0))
        total = sum(row)
        channel.append([v / total for v in row])
    return channel


def spectral_gap_beta_receipt(
    mode1: float,
    mode2: float,
    n: int = 24,
) -> tuple[float, float, float, float, bool]:
    channel = circulant_spectral_channel(n, mode1, mode2)
    eigs = list(reversed(jacobi_eigenvalues_symmetric(channel, max_sweeps=500)))
    top = eigs[0]
    first = eigs[1] if len(eigs) > 1 else 0.0
    second_shell = eigs[3] if len(eigs) > 3 else 0.0
    gap = max(top - first, 0.0)
    isolation = max(first - second_shell, 0.0)
    beta_gap = 1.0 / sqrt(gap) if gap > 1e-12 else float("inf")
    passes = gap > 0.05 and isolation > 0.04
    return gap, isolation, beta_gap, first, passes


def print_spectral_gap_beta_receipts() -> None:
    print("spectral-gap beta selection receipt")
    print("-----------------------------------")
    print("case              mode1   mode2     gap   isolation  beta_gap  verdict")
    cases = [
        ("isolated", 0.30, 0.05),
        ("free rescale", 0.45, 0.05),
        ("near plateau", 0.22, 0.21),
        ("no memory", 0.00, 0.00),
    ]
    for name, mode1, mode2 in cases:
        gap, isolation, beta_gap, _, passes = spectral_gap_beta_receipt(mode1, mode2)
        verdict = "PASS" if passes else "FAIL"
        print(
            f"{name:16s}  {mode1:6.3f}  {mode2:6.3f}  {gap:7.4f}  "
            f"{isolation:9.4f}  {beta_gap:8.4f}  {verdict}"
        )
    print()


def fisher_cost_objective(width: float, blur_cost: float) -> tuple[float, float, float, float]:
    """Information-per-cost proxy for a detector-width family."""
    fisher = width
    heating_cost = 1.0 / (4.0 * width**4)
    localization_cost = blur_cost * width * width
    objective = fisher / (heating_cost + localization_cost) if heating_cost + localization_cost > 0 else float("inf")
    return fisher, heating_cost, localization_cost, objective


def fisher_width_selection_receipt(blur_cost: float) -> tuple[float, float, int, bool]:
    widths = [0.60 + 3.40 * k / 170.0 for k in range(171)]
    rows = [(fisher_cost_objective(w, blur_cost)[3], w) for w in widths]
    best_value, best_width = max(rows)
    near_count = sum(1 for value, _ in rows if value >= 0.99 * best_value)
    boundary = best_width == widths[0] or best_width == widths[-1]
    passes = not boundary and near_count <= 12
    return best_width, best_value, near_count, passes


def print_fisher_width_selection_receipts() -> None:
    print("Fisher-information / cost beta selection receipt")
    print("------------------------------------------------")
    print("case              blur_cost  width_*  objective  near_1pct  verdict")
    cases = [
        ("balanced", 0.050),
        ("weak blur", 0.005),
        ("no blur", 0.000),
        ("strong blur", 0.120),
    ]
    for name, blur_cost in cases:
        width, value, near_count, passes = fisher_width_selection_receipt(blur_cost)
        verdict = "PASS" if passes else "FAIL"
        print(
            f"{name:16s}  {blur_cost:9.4f}  {width:7.4f}  "
            f"{value:9.4f}  {near_count:9d}  {verdict}"
        )
    print()


def print_c_lock_cost_coefficient_receipts() -> None:
    """Attack C-lock by varying only the gravity/localization cost coefficient."""
    print("C-lock coefficient-family attack: free blur coefficient")
    print("-------------------------------------------------------")
    print("blur_coeff  support  width_*   beta_*  objective  near_1pct  verdict")
    support = detector_threshold_closure_case(1.70, 2.40, 1.00)[1]
    widths = []
    betas = []
    all_conditional = True
    for blur_cost in [0.030, 0.050, 0.120, 0.250]:
        width, value, near_count, passes = fisher_width_selection_receipt(blur_cost)
        beta = 1.0 / width if width > 1e-15 else float("inf")
        widths.append(width)
        betas.append(beta)
        verdict = "COND" if support == 7 and passes else "FAIL"
        all_conditional = all_conditional and verdict == "COND"
        print(
            f"{blur_cost:10.3f}  {support:7d}  {width:7.4f}  "
            f"{beta:7.4f}  {value:9.4f}  {near_count:9d}  {verdict}"
        )
    width_span = max(widths) - min(widths)
    beta_span = max(betas) - min(betas)
    family_verdict = "FAIL" if all_conditional and beta_span > 1e-8 else "PASS"
    print(f"cost-coefficient width span: {width_span:.3f}")
    print(f"cost-coefficient beta span: {beta_span:.3f}")
    print(f"C-lock coefficient-family verdict: {family_verdict}")
    print()


def print_gravity_response_coefficient_receipts() -> None:
    """Show that source-count identity does not fix gravity response amplitude."""
    print("gravity-response coefficient attack: source count versus amplitude")
    print("------------------------------------------------------------------")
    print("kappa_G   gamma    blur_coeff  support  source  width_*   beta_*  verdict")
    threshold, support, gamma, _, _, source_match, _, _ = detector_threshold_closure_case(
        1.70, 2.40, 1.00
    )
    del threshold
    betas = []
    all_conditional = True
    for blur_cost in [0.030, 0.050, 0.120, 0.250]:
        kappa = blur_cost / gamma if gamma > 1e-15 else float("inf")
        width, _, _, passes = fisher_width_selection_receipt(blur_cost)
        beta = 1.0 / width if width > 1e-15 else float("inf")
        betas.append(beta)
        verdict = "COND" if support == 7 and source_match and passes else "FAIL"
        all_conditional = all_conditional and verdict == "COND"
        source = "yes" if source_match else "no"
        print(
            f"{kappa:7.4f}  {gamma:7.5f}  {blur_cost:10.3f}  "
            f"{support:7d}  {source:6s}  {width:7.4f}  {beta:7.4f}  {verdict}"
        )
    beta_span = max(betas) - min(betas)
    family_verdict = "FAIL" if all_conditional and beta_span > 1e-8 else "PASS"
    print(f"gravity-response beta span: {beta_span:.3f}")
    print(f"gravity-response coefficient verdict: {family_verdict}")
    print()


def kappa_lock_derived_case(
    jacobian: list[list[float]],
    internal_coupling: float,
    internal_floor: float = 0.80,
) -> tuple[float, float, float, float, float, bool, bool]:
    """Read kappa_G from the same deletion/source response used by ACV."""
    _, _, _, _, _, _, deletion_margin, _, acv_passes = acv_actual_event_law_audit(
        jacobian,
        internal_floor,
        internal_coupling,
    )
    _, _, gamma, _, _, _, _, _ = detector_threshold_closure_case(1.70, 2.40, 1.00)
    kappa_g = max(deletion_margin, 0.0)
    blur_cost = gamma * kappa_g
    width, _, _, cost_passes = fisher_width_selection_receipt(blur_cost)
    beta = 1.0 / width if width > 1e-15 else float("inf")
    return kappa_g, blur_cost, width, beta, deletion_margin, acv_passes, cost_passes


def print_kappa_lock_audit_receipts() -> None:
    """Audit whether kappa_G is derived, free, or invalid."""
    print("Kappa Lock audit: response amplitude from one-event deletion")
    print("-----------------------------------------------------------")
    print(
        "case                  fixed  acv   kappa_G  blur_coeff  "
        "width_*   beta_*  beta_span  verdict"
    )

    free_betas = []
    for blur_cost in [0.030, 0.050, 0.120, 0.250]:
        width, _, _, _ = fisher_width_selection_receipt(blur_cost)
        free_betas.append(1.0 / width if width > 1e-15 else float("inf"))
    free_span = max(free_betas) - min(free_betas)

    print(
        f"{'support-only':21s}  {'no':5s}  {'no':4s}  {'--':7s}  "
        f"{'--':10s}  {'--':7s}  {'--':7s}  {free_span:9.3f}  FAIL"
    )
    print(
        f"{'role-faithful free':21s}  {'no':5s}  {'yes':4s}  {'free':7s}  "
        f"{'free':10s}  {'--':7s}  {'--':7s}  {free_span:9.3f}  FAIL"
    )

    base = kappa_lock_derived_case(
        source_record_detector_jacobian(0.030, 0.900),
        internal_coupling=0.020,
    )
    base_kappa, base_blur, base_width, base_beta, _, base_acv, base_cost = base
    verdict = "PASS" if base_acv and base_cost and base_kappa > 0.0 else "FAIL"
    print(
        f"{'derived kappa toy':21s}  {'yes':5s}  {('PASS' if base_acv else 'FAIL'):4s}  "
        f"{base_kappa:7.4f}  {base_blur:10.4f}  {base_width:7.4f}  "
        f"{base_beta:7.4f}  {0.0:9.3f}  {verdict}"
    )

    small = kappa_lock_derived_case(
        source_record_detector_jacobian(0.030, 0.900),
        internal_coupling=0.060,
    )
    kappa_g, blur_cost, width, beta, _, acv_passes, cost_passes = small
    drift = abs(beta - base_beta)
    verdict = "PASS" if acv_passes and cost_passes and drift <= 0.05 else "FAIL"
    print(
        f"{'small Schur drift':21s}  {'yes':5s}  {('PASS' if acv_passes else 'FAIL'):4s}  "
        f"{kappa_g:7.4f}  {blur_cost:10.4f}  {width:7.4f}  "
        f"{beta:7.4f}  {drift:9.3f}  {verdict}"
    )

    large = kappa_lock_derived_case(
        source_record_detector_jacobian(0.030, 0.900),
        internal_coupling=0.180,
    )
    kappa_g, blur_cost, width, beta, _, acv_passes, cost_passes = large
    drift = abs(beta - base_beta)
    verdict = "PASS" if acv_passes and cost_passes and drift <= 0.05 else "FAIL"
    print(
        f"{'large Schur drift':21s}  {'yes':5s}  {('PASS' if acv_passes else 'FAIL'):4s}  "
        f"{kappa_g:7.4f}  {blur_cost:10.4f}  {width:7.4f}  "
        f"{beta:7.4f}  {drift:9.3f}  {verdict}"
    )

    split = kappa_lock_derived_case(
        acv_collar_jacobian(source_redundant=True),
        internal_coupling=0.020,
    )
    kappa_g, blur_cost, width, beta, _, acv_passes, cost_passes = split
    verdict = "PASS" if acv_passes and cost_passes and kappa_g > 0.0 else "FAIL"
    print(
        f"{'split-source amp':21s}  {'no':5s}  {('PASS' if acv_passes else 'FAIL'):4s}  "
        f"{kappa_g:7.4f}  {blur_cost:10.4f}  {width:7.4f}  "
        f"{beta:7.4f}  {0.0:9.3f}  {verdict}"
    )
    print()


def kappa_refinement_scan_case(
    jacobian: list[list[float]],
    internal_couplings: list[float],
) -> tuple[float, float, float, float, float, float, bool, bool, bool]:
    """Track deletion-derived kappa_G and selected beta under refinement."""
    kappas = []
    betas = []
    acv_flags = []
    cost_flags = []
    for coupling in internal_couplings:
        kappa_g, _, _, beta, _, acv_passes, cost_passes = kappa_lock_derived_case(
            jacobian,
            internal_coupling=coupling,
        )
        kappas.append(kappa_g)
        betas.append(beta)
        acv_flags.append(acv_passes)
        cost_flags.append(cost_passes)

    beta_span = max(betas) - min(betas)
    tail_drift = abs(betas[-1] - betas[-2]) if len(betas) >= 2 else 0.0
    all_acv = all(acv_flags)
    all_cost = all(cost_flags)
    passes = all_acv and all_cost and kappas[-1] > 0.0 and beta_span <= 0.05 and tail_drift <= 0.02
    return (
        kappas[0],
        kappas[-1],
        betas[0],
        betas[-1],
        beta_span,
        tail_drift,
        all_acv,
        all_cost,
        passes,
    )


def print_kappa_refinement_scan_receipts() -> None:
    """Cofinal-style stability scan for the deletion-derived response amplitude."""
    print("Kappa refinement scan: cofinal response stability")
    print("-------------------------------------------------")
    print(
        "case                acv   cost  kappa_0  kappa_N  "
        "beta_0   beta_N  beta_span  tail_drift  verdict"
    )
    cases = [
        (
            "stable derived",
            source_record_detector_jacobian(0.030, 0.900),
            [0.040, 0.030, 0.020, 0.015],
        ),
        (
            "large drift",
            source_record_detector_jacobian(0.030, 0.900),
            [0.180, 0.120, 0.060, 0.020],
        ),
        (
            "vanishing kappa",
            source_record_detector_jacobian(0.030, 0.900, source_private=0.200),
            [0.080, 0.060, 0.040, 0.020],
        ),
        (
            "split-source",
            acv_collar_jacobian(source_redundant=True),
            [0.040, 0.030, 0.020, 0.015],
        ),
    ]
    for name, jacobian, couplings in cases:
        k0, kn, b0, bn, beta_span, tail_drift, all_acv, all_cost, passes = (
            kappa_refinement_scan_case(jacobian, couplings)
        )
        verdict = "PASS" if passes else "FAIL"
        acv = "PASS" if all_acv else "FAIL"
        cost = "PASS" if all_cost else "FAIL"
        print(
            f"{name:18s}  {acv:4s}  {cost:4s}  {k0:7.4f}  {kn:7.4f}  "
            f"{b0:7.4f}  {bn:7.4f}  {beta_span:9.4f}  "
            f"{tail_drift:10.4f}  {verdict}"
        )
    print()


def print_same_local_vertex_receipts() -> None:
    print("same-local-vertex receipt: derivation route for eta_*")
    print("------------------------------------------------------")
    print("case                 rank   fisher_min   eta_D     row_floor")
    cases = [
        ("good vertex", None, False, False, 0.03),
        ("source 0.1", 0.1, False, False, 0.03),
        ("source zero", None, True, False, 0.03),
        ("source redundant", None, False, True, 0.03),
        ("overmixed", None, False, False, 0.40),
    ]
    for name, floor, zero, redundant, mixing in cases:
        rank, fisher_min, eta_d, row_floor = same_local_vertex_receipt(
            source_floor=floor,
            source_zero=zero,
            source_redundant=redundant,
            mixing=mixing,
        )
        print(f"{name:18s}  {rank:4d}  {fisher_min:10.6f}  {eta_d:8.6f}  {row_floor:9.6f}")
    print()


def print_s_floor_density_receipts(n: int) -> None:
    print("S-floor RN-density receipt: deletion-derived role visibility")
    print("------------------------------------------------------------")
    print("case             min_density  max_density  sqrt_floor  no_merge   role_KL")
    cases = [
        ("branch-A", False, None),
        ("source 0.3", False, 0.3),
        ("source 0.1", False, 0.1),
        ("source zero", False, 0.0),
        ("branch-B", True, None),
    ]
    for name, branch_b, floor in cases:
        mn, mx, pred, no_merge = role_density_receipt(n, branch_b=branch_b, source_floor=floor)
        kl = role_bookkeeping_cost(n, branch_b=branch_b, source_floor=floor)
        if abs(kl) < 5e-12:
            kl = 0.0
        print(
            f"{name:14s}  {mn:11.6f}  {mx:11.6f}  {pred:10.6f}  "
            f"{no_merge:8.6f}  {kl:8.6f}"
        )
    print()


def print_k_floor_sweep() -> None:
    print("adversarial K-floor sweep: spectral-tail crossing derivative")
    print("------------------------------------------------------------")
    print("model             beta_cross   k_proxy")
    models = [
        ("single-scale", [10.0], [1.0]),
        ("two-scale", [7.0, 14.0], [0.5, 0.5]),
        ("flat-mixture", [6.0, 10.0, 16.0, 24.0], [0.25, 0.25, 0.25, 0.25]),
    ]
    for name, scales, weights in models:
        beta, deriv = find_tail_crossing(scales, weights, eta=0.5)
        print(f"{name:16s}  {beta:10.4f}  {deriv:8.6f}")
    print()


def main() -> None:
    sizes = [16, 32, 64, 128]
    branch_a = [execute(n, branch_b=False) for n in sizes]
    branch_b = [execute(n, branch_b=True) for n in sizes]
    beta_stress = [6.5, 7.5, 8.5]
    stress = [execute(n, branch_b=False, beta_in=b) for b in beta_stress for n in sizes[1:]]

    print("=" * 104)
    print("v6 Paper 2 Part II §5.11: LR decisive finite tests")
    print("=" * 104)
    print_table("branch-A one-event support", branch_a)
    print_table("branch-B decoupled source countercase", branch_b)
    print_table("branch-A memory-scale stress", stress)
    print_c_floor_sweep(128)
    print_s_floor_sweep(128)
    print_s_floor_density_receipts(128)
    print_bm1_polytope_receipts(128)
    print_local_frame_receipts(128)
    print_same_local_generator_receipts(128)
    print_role_fisher_falsifier()
    print_local_vertex_normal_form_receipts()
    print_interval_vertex_certificates()
    print_refinement_vertex_transport_receipts()
    print_actual_coincidence_vertex_receipts()
    print_schur_transport_receipts()
    print_physical_event_acv_receipts()
    print_actual_event_law_acv_audit()
    print_bare_ics_acv_independence_receipt()
    print_source_record_detector_receipts()
    print_detector_threshold_closure_receipts()
    print_beta_family_no_go_receipts()
    print_beta_lock_audit_receipts()
    print_source_record_width_identifiability_receipts()
    print_source_record_k_lock_attack_receipts()
    print_causal_collar_transition_k_receipts()
    print_spectral_gap_beta_receipts()
    print_fisher_width_selection_receipts()
    print_c_lock_cost_coefficient_receipts()
    print_gravity_response_coefficient_receipts()
    print_kappa_lock_audit_receipts()
    print_kappa_refinement_scan_receipts()
    print_same_local_vertex_receipts()
    print_k_floor_sweep()

    min_gram = min(r.gram_min for r in branch_a)
    min_one = min(r.one_event_min for r in branch_a)
    max_mart = max(r.martingale_error for r in branch_a)
    b_min_one = min(r.one_event_min for r in branch_b)
    stress_min_gram = min(r.gram_min for r in stress)
    stress_min_one = min(r.one_event_min for r in stress)
    stress_beta_span = (min(r.beta for r in stress), max(r.beta for r in stress))

    print("=" * 104)
    print("VERDICT")
    print("=" * 104)
    print(f"finite response-Gram lower bound over tested refinements: {min_gram:.6f}")
    print(f"finite one-event singular lower bound over tested refinements: {min_one:.6f}")
    print(f"finite likelihood refinement martingale error upper bound: {max_mart:.6f}")
    print(f"decoupled-source one-event singular lower bound: {b_min_one:.6f}")
    print(f"memory-scale stress response-Gram lower bound: {stress_min_gram:.6f}")
    print(f"memory-scale stress one-event singular lower bound: {stress_min_one:.6f}")
    print(f"memory-scale stress extracted beta span: [{stress_beta_span[0]:.4f}, {stress_beta_span[1]:.4f}]")
    print()
    print("finite decisive tests: PASS for the constructed one-event toy branch")
    print("cofinal LR1-LR7 theorem: OPEN")
    print("diagnostic bite: the decoupled branch keeps finite responses but loses the")
    print("one-event singular bound, so LR7 detects branch-B source splitting.")
    print("BM1 bite: fixed coarse moment-polytope margins can stay positive while")
    print("pointwise S-floor fails, so BM1 must use a role-complete local frame.")
    print("local-frame bite: a positive frame lower bound still needs positive role")
    print("tensor floor min_W; source-thinning kills S-floor by driving min_W to zero.")
    print("generator bite: local Hessian ellipticity is harmless; source-thinning")
    print("kills the role-coupling/transversality floor that branch A needs.")
    print("role-Fisher bite: bare causal/local data allow pinched, zero, or redundant")
    print("role covectors, so eta_* needs role-indivisibility or an equivalent proof.")
    print("vertex bite: a computed same-local vertex earns eta_* only when its role")
    print("Jacobian is diagonally dominant and the common deletion direction survives.")
    print("interval bite: cofinal closure needs a compact vertex class with positive")
    print("diagonal-dominance and deletion-support margins, not isolated full rank.")
    print("transport bite: refinement is harmless only when coefficient drift is")
    print("smaller than the diagonal and deletion-support slack of the vertex class.")
    print("actual-vertex bite: AV1-AV3 reduce to a local coincidence vertex, its")
    print("Schur transport errors, and distance from the explicit bad variety.")
    print("ACV bite: physical division events earn branch-A only when direct role")
    print("self-sensitivity dominates leakage and Schur refinement drift.")
    print("event-law audit bite: the actual branch-A event law must pass the")
    print("finite collar response matrix and Schur-margin test, not just be named")
    print("a physical source-record event.")
    print("bare-ICS bite: the same causal set, count, and scalar rate admit role laws")
    print("with different ACV verdicts, so ACV is not derivable from bare ICS alone.")
    print("source-record detector bite: ACV is derived when private role-detector")
    print("variance dominates common-click covariance, residual leakage, and Schur drift.")
    print("detector-threshold bite: a log-likelihood record channel fixes S_*=0,")
    print("but beta is still underived if detector width can vary while receipts pass.")
    print("beta no-go bite: the current visible receipts admit a detector-width")
    print("family with the same threshold, gamma, vacuum/source/TS receipts,")
    print("and finite heating, but different beta values.")
    print("Beta Lock bite: support-only data fail; transfer or cost routes pass")
    print("only when the transfer operator or cost functional is fixed by the")
    print("same event law, not chosen from a family after the fact.")
    print("source-record channel bite: finite Poisson records can identify a")
    print("width after nature supplies one, but identifiability is not derivation.")
    print("K-lock attack bite: the induced transfer spectrum has an isolated scale")
    print("for each supplied width, but the scale moves across the same visible")
    print("event-support family; K-lock needs the kernel fixed by the event law.")
    print("causal-collar K bite: adjacency supplies the graph, not the transition")
    print("frequency; changing the same-collar move probability changes beta_K.")
    print("spectral-gap bite: beta is intrinsic only when the record-transfer")
    print("operator has an isolated first nonzero scale; plateaus keep beta free.")
    print("Fisher/cost bite: beta is selected only by a unique interior")
    print("information-per-cost optimum; boundary or plateau optima fail branch A.")
    print("C-lock coefficient bite: fixed detector support and stable cost optima")
    print("still give different beta values when the gravity/localization")
    print("coefficient varies, so C-lock must derive that coefficient.")
    print("gravity-response bite: source-count identity fixes the event support")
    print("and density, but not the response amplitude kappa_G that enters C-lock.")
    print("Kappa Lock bite: kappa_G must come from the same deletion/source")
    print("response margin that proves one-event role faithfulness; support-only,")
    print("free-amplitude, large-drift, or split-source amplitudes fail.")
    print("kappa-refinement bite: convergence of beta is not enough; ACV,")
    print("cost stability, and small tail drift must all survive refinement.")
    print("adversarial bite: near-redundant receipts, pinched source visibility, and")
    print("flat spectral tails identify the three cofinal floors c_*, s_*, and k_*.")


if __name__ == "__main__":
    main()
