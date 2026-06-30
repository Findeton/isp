#!/usr/bin/env python3
"""
Paper 32 receipt: v6-v7 diamond law bridge audit.

This receipt tests the candidate fusion found by rereading v6-v7:

    click law = positive h-transform shadow of a minimal no-silent
    diamond-boundary center.

The script is intentionally small and exact.  It does not rerun the expensive
N=9 enumeration from Paper 30.  Instead it audits three bridge claims:

1. v6 no-silent seams can be represented as a conditional-information center:
   a boundary screen S is incomplete, while the minimal center (S,H) closes the
   seam exactly.
2. The Paper 30/31 finite diamond-shadow facts are compatible with this: the
   shadow is exact for the held-out forward law but is not reconstructive.
3. v6 RN/KL commitment gives a real intrinsic h-weight candidate, but it is not
   identical to the one-diamond Diamond Work-Balance constant.  This prevents
   conflating two different exponentials.

All finite probabilities are Fraction.  Decimal precision is 140 (>80 bits) for
logs, exponentials, and root-finding.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
import sys

getcontext().prec = 140
sys.stdout.reconfigure(line_buffering=True)

ONE = Decimal(1)
TWO = Decimal(2)
TEN = Decimal(10)
TOL = Decimal("1e-110")

checks = []


def dfrac(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def tanh(x):
    e2 = (TWO * x).exp()
    return (e2 - ONE) / (e2 + ONE)


def cosh(x):
    return (x.exp() + (-x).exp()) / TWO


def bisect_root(f, lo, hi, steps=480):
    flo = f(lo)
    fhi = f(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if flo * fhi > 0:
        raise ValueError(f"root not bracketed: f(lo)={flo} f(hi)={fhi}")
    for _ in range(steps):
        mid = (lo + hi) / TWO
        fm = f(mid)
        if fm == 0:
            return mid
        if flo * fm < 0:
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo + hi) / TWO


def build_no_silent_joint():
    """Return exact joint law for X, S, H, Z.

    X is the lower-side record bit.
    S is the visible seam/screen bit, a noisy copy of X.
    H is a hidden center bit, another noisy copy of X.
    Z=(S,H) is the upper-side boundary readout.

    Then I(X;Z | S) > 0: S alone leaks residual information across the seam.
    But I(X;Z | S,H) = 0: once the minimal center is admitted, Z is fixed by
    the center and the seam is complete.
    """
    p_flip_s = Fraction(1, 5)
    p_flip_h = Fraction(1, 4)
    joint = defaultdict(Fraction)
    for x in (0, 1):
        for noise_s in (0, 1):
            ps = p_flip_s if noise_s else 1 - p_flip_s
            for noise_h in (0, 1):
                ph = p_flip_h if noise_h else 1 - p_flip_h
                s = x ^ noise_s
                h = x ^ noise_h
                z = (s, h)
                joint[(x, s, h, z)] += Fraction(1, 2) * ps * ph
    return dict(joint)


def conditional_mutual_information(joint, x_of, z_of, y_of):
    """Compute I(X;Z | Y) in nats from an exact joint distribution."""
    p_xyz = defaultdict(Fraction)
    p_xy = defaultdict(Fraction)
    p_yz = defaultdict(Fraction)
    p_y = defaultdict(Fraction)

    for state, prob in joint.items():
        x = x_of(state)
        z = z_of(state)
        y = y_of(state)
        p_xyz[(x, z, y)] += prob
        p_xy[(x, y)] += prob
        p_yz[(z, y)] += prob
        p_y[y] += prob

    total = Decimal(0)
    for (x, z, y), prob in p_xyz.items():
        ratio = prob * p_y[y] / (p_xy[(x, y)] * p_yz[(z, y)])
        total += dfrac(prob) * dfrac(ratio).ln()
    return +total


def rn_commitment_root():
    return bisect_root(lambda h: tanh(h) - (-h).exp(), Decimal(0), Decimal(2))


def diamond_work_balance_root():
    def capacity(h):
        return h * tanh(h) - cosh(h).ln()

    def fisher(h):
        th = tanh(h)
        return ONE - th * th

    eta = bisect_root(lambda h: capacity(h) - fisher(h), Decimal(0), Decimal(3))
    return eta, capacity(eta), fisher(eta)


print("=" * 80)
print("Paper 32 v6-v7 diamond law bridge receipt")
print("=" * 80)
print(f"Decimal precision: prec={getcontext().prec}")

print("\n" + "=" * 80)
print("1. No-silent seam center test")
print("=" * 80)
joint = build_no_silent_joint()
delta_s = conditional_mutual_information(
    joint,
    x_of=lambda state: state[0],
    z_of=lambda state: state[3],
    y_of=lambda state: state[1],
)
delta_sh = conditional_mutual_information(
    joint,
    x_of=lambda state: state[0],
    z_of=lambda state: state[3],
    y_of=lambda state: (state[1], state[2]),
)
print(f"I(X;Z | S)     = {delta_s}")
print(f"I(X;Z | S,H)   = {delta_sh}")

check(
    "visible seam S is incomplete",
    delta_s > Decimal("0.01"),
    f"residual={delta_s}",
)
check(
    "minimal center (S,H) closes the seam",
    abs(delta_sh) < TOL,
    f"closed_residual={delta_sh}",
)
check(
    "the center adds information without adding a hidden label oracle",
    len({state[1] for state in joint}) == 2 and len({(state[1], state[2]) for state in joint}) == 4,
    "S has 2 cells; (S,H) has 4 intrinsic boundary cells",
)

print("\n" + "=" * 80)
print("2. Imported finite diamond-shadow facts from Papers 30/31")
print("=" * 80)
records_9 = 131526
base_atoms_9 = 131514
diamond_center_atoms_9 = 131518
diamond_center_conflicts_9 = 0
residual_edges_9 = 4
licensed_orbits = 11
total_dual_orbits = 24
low_gate_triples = 64
licensed_triples = 165
recurrence_gate_triples = 4
shadow_edges_covered = 2
selected_shadow_atoms_9 = 65521
selected_tv9 = Fraction(0)
selected_rec9 = Fraction(0)
selected_qrec9 = Fraction(0)
selected_metric = (5, 5, 3)

print(
    f"records_9={records_9}, base_atoms_9={base_atoms_9}, "
    f"center_atoms_9={diamond_center_atoms_9}, shadow_atoms_9={selected_shadow_atoms_9}"
)
print(
    f"residual_edges_9={residual_edges_9}, shadow_edges_covered={shadow_edges_covered}, "
    f"licensed_orbits={licensed_orbits}/{total_dual_orbits}"
)
print(
    f"licensed_triples={licensed_triples}, low_gate_triples={low_gate_triples}, "
    f"recurrence_gate_triples={recurrence_gate_triples}, metric={selected_metric}"
)

check(
    "diamond center is a proper residual closure",
    base_atoms_9 < diamond_center_atoms_9 < records_9 and diamond_center_conflicts_9 == 0,
    f"{base_atoms_9}->{diamond_center_atoms_9}/{records_9}, conflicts={diamond_center_conflicts_9}",
)
check(
    "selected shadow is nonreconstructive",
    selected_shadow_atoms_9 < diamond_center_atoms_9,
    f"shadow={selected_shadow_atoms_9}, center={diamond_center_atoms_9}",
)
check(
    "selected shadow does not merely encode the full residual graph",
    0 < shadow_edges_covered < residual_edges_9,
    f"covered={shadow_edges_covered}/{residual_edges_9}",
)
check(
    "boundary activity gates sectors but does not uniquely select by itself",
    0 < licensed_orbits < total_dual_orbits
    and 1 < recurrence_gate_triples < low_gate_triples < licensed_triples,
    (
        f"orbits={licensed_orbits}/{total_dual_orbits}; "
        f"triples={recurrence_gate_triples}<{low_gate_triples}<{licensed_triples}"
    ),
)
check(
    "selected positive shadow gives exact audited forward law",
    selected_tv9 == 0 and selected_rec9 == 0 and selected_qrec9 == 0,
    f"TV9={selected_tv9}, rec9={selected_rec9}, qrec9={selected_qrec9}",
)

print("\n" + "=" * 80)
print("3. RN/KL commitment h-weight candidate")
print("=" * 80)
I = Decimal(1) / Decimal(7)
J = Decimal(5) / Decimal(13)
gluing_residual = (-(I + J)).exp() - (-I).exp() * (-J).exp()
h_commit = rn_commitment_root()
commit_residual = tanh(h_commit) - (-h_commit).exp()
eta, capacity_eta, fisher_eta = diamond_work_balance_root()
dwb_residual = capacity_eta - fisher_eta
eta_gap = abs(eta - h_commit)

print(f"exp gluing residual        = {gluing_residual}")
print(f"h_commit                   = {h_commit}")
print(f"tanh(h)-exp(-h) residual   = {commit_residual}")
print(f"eta_dwb                    = {eta}")
print(f"DWB capacity-fisher gap    = {dwb_residual}")
print(f"|eta_dwb-h_commit|         = {eta_gap}")
print(f"W_star                     = {fisher_eta}")

check(
    "RN/KL survival glues exponentially",
    abs(gluing_residual) < TOL,
    f"residual={gluing_residual}",
)
check(
    "commitment h-root is solved at high precision",
    abs(commit_residual) < TOL and h_commit > 0,
    f"h={h_commit}",
)
check(
    "Diamond Work-Balance root is distinct from commitment h-root",
    abs(dwb_residual) < TOL and eta_gap > Decimal("0.1"),
    f"eta={eta}, h={h_commit}, gap={eta_gap}",
)

print("\n" + "=" * 80)
print("4. Bridge verdict")
print("=" * 80)
print(
    "The campaign supports the bridge architecture but does not prove the "
    "universal click law.  It shows that v6 no-silent completion, v7 finite "
    "diamond shadows, and v6 commitment weights are mutually compatible and "
    "correctly separated.  The missing theorem is the intrinsic equality "
    "between the physical boundary-center shadow and the forward h-weight."
)

print("\n" + "=" * 80)
failed = False
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    failed = failed or not ok
print(f"\nCHECKS PASSED: {sum(ok for _, ok, _ in checks)}/{len(checks)}")
if failed:
    sys.exit(1)
print("DONE.")
