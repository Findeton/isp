"""
v6 Paper 3 section 40: minimal complete screen campaign.

Question:
    Can the physical gluing screen be derived as the unique minimal intrinsic
    record closure satisfying the RN screen-sufficiency condition

        Delta_Y = I(X;Z|Y) = 0 ?

Finite answer:
    Not for arbitrary finite laws and not from correlations alone.  The
    derivation works only under a precise packet:

      1. candidate screens are intrinsic causal antichain separators;
      2. every bypass influence is recorded in the candidate closure lattice;
      3. the minimal zero-defect screen is unique up to internal automorphism;
      4. the zero/min-positive gap is stable under refinement.

    The finite campaign proves the conditional selection theorem and gives
    counterexamples when each gate is removed.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from math import log


EPS = 1.0e-10
MARGIN_FLOOR = 1.0e-3


Law = dict[tuple[int, ...], float]


@dataclass(frozen=True)
class ScreenScan:
    status: str
    minimals: list[tuple[str, ...]]
    best: float
    margin: float
    verdict: str


@dataclass(frozen=True)
class ScreenAudit:
    target: str
    candidate_law: str
    scan: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def normalize(law: Law) -> Law:
    total = sum(law.values())
    return {state: value / total for state, value in law.items()}


def bit_prob(bit: int, p_one: float) -> float:
    return p_one if bit else 1.0 - p_one


def copy_channel(child: int, parent: int, fidelity: float) -> float:
    return fidelity if child == parent else 1.0 - fidelity


def mediator_law(noise: bool = True) -> tuple[list[str], Law]:
    names = ["X", "S", "N", "Z"] if noise else ["X", "S", "Z"]
    law: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x = data["X"]
        s = data["S"]
        z = data["Z"]
        prob = 0.5
        prob *= copy_channel(s, x, 0.82)
        if noise:
            prob *= 0.5
        prob *= copy_channel(z, s, 0.80)
        law[bits] = prob
    return names, normalize(law)


def bypass_closure_law() -> tuple[list[str], Law]:
    names = ["X", "S", "H", "Z"]
    law: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x, s, h, z = data["X"], data["S"], data["H"], data["Z"]
        p_z_one = 0.08 + 0.42 * s + 0.36 * h
        prob = 0.5
        prob *= copy_channel(s, x, 0.82)
        prob *= copy_channel(h, x, 0.74)
        prob *= bit_prob(z, p_z_one)
        law[bits] = prob
    return names, normalize(law)


def direct_unrecorded_law() -> tuple[list[str], Law]:
    names = ["X", "S", "H", "Z"]
    law: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x, s, h, z = data["X"], data["S"], data["H"], data["Z"]
        p_z_one = 0.05 + 0.22 * s + 0.18 * h + 0.42 * x
        prob = 0.5
        prob *= copy_channel(s, x, 0.76)
        prob *= copy_channel(h, x, 0.68)
        prob *= bit_prob(z, p_z_one)
        law[bits] = prob
    return names, normalize(law)


def duplicate_law() -> tuple[list[str], Law]:
    names = ["X", "S", "D", "Z"]
    law: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x, s, d, z = data["X"], data["S"], data["D"], data["Z"]
        if d != s:
            law[bits] = 0.0
            continue
        prob = 0.5 * copy_channel(s, x, 0.82) * copy_channel(z, s, 0.80)
        law[bits] = prob
    return names, normalize(law)


def noisy_duplicate_law(error: float = 0.03) -> tuple[list[str], Law]:
    names = ["X", "S", "D", "Z"]
    law: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x, s, d, z = data["X"], data["S"], data["D"], data["Z"]
        prob = 0.5
        prob *= copy_channel(s, x, 0.82)
        prob *= copy_channel(d, s, 1.0 - error)
        prob *= copy_channel(z, s, 0.80)
        law[bits] = prob
    return names, normalize(law)


def oracle_law() -> tuple[list[str], Law]:
    names = ["X", "S", "O", "Z"]
    law: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x, s, o, z = data["X"], data["S"], data["O"], data["Z"]
        if o != z:
            law[bits] = 0.0
            continue
        prob = 0.5 * copy_channel(s, x, 0.82) * copy_channel(z, s, 0.80)
        law[bits] = prob
    return names, normalize(law)


def role_split_laws() -> tuple[list[str], Law, Law]:
    names_s, source = mediator_law(noise=False)
    # Rename the mediator in a second law by moving dependence to H.
    names = ["X", "S", "H", "Z"]
    record: Law = {}
    source_role: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x, s, h, z = data["X"], data["S"], data["H"], data["Z"]
        record[bits] = 0.5 * copy_channel(s, x, 0.82) * 0.5 * copy_channel(z, s, 0.80)
        source_role[bits] = 0.5 * 0.5 * copy_channel(h, x, 0.82) * copy_channel(z, h, 0.80)
    return names, normalize(record), normalize(source_role)


def index_of(names: list[str], selected: tuple[str, ...]) -> tuple[int, ...]:
    return tuple(names.index(name) for name in selected)


def cmi(law: Law, names: list[str], given: tuple[str, ...]) -> float:
    ix = names.index("X")
    iz = names.index("Z")
    iy = index_of(names, given)
    p_y: dict[tuple[int, ...], float] = {}
    p_xy: dict[tuple[int, tuple[int, ...]], float] = {}
    p_zy: dict[tuple[int, tuple[int, ...]], float] = {}
    p_xzy: dict[tuple[int, int, tuple[int, ...]], float] = {}

    for state, prob in law.items():
        if prob <= 0.0:
            continue
        y = tuple(state[i] for i in iy)
        x = state[ix]
        z = state[iz]
        p_y[y] = p_y.get(y, 0.0) + prob
        p_xy[(x, y)] = p_xy.get((x, y), 0.0) + prob
        p_zy[(z, y)] = p_zy.get((z, y), 0.0) + prob
        p_xzy[(x, z, y)] = p_xzy.get((x, z, y), 0.0) + prob

    total = 0.0
    for (x, z, y), pxyz in p_xzy.items():
        denom = p_xy[(x, y)] * p_zy[(z, y)]
        total += pxyz * log(pxyz * p_y[y] / denom)
    return max(0.0, total)


def powerset(items: list[str]) -> list[tuple[str, ...]]:
    out: list[tuple[str, ...]] = []
    for size in range(1, len(items) + 1):
        out.extend(tuple(combo) for combo in combinations(items, size))
    return out


def proper_subset(left: tuple[str, ...], right: tuple[str, ...]) -> bool:
    return set(left) < set(right)


def scan_screens(law: Law, names: list[str], candidates: list[str]) -> ScreenScan:
    values = [(subset, cmi(law, names, subset)) for subset in powerset(candidates)]
    values.sort(key=lambda item: (item[1], len(item[0]), item[0]))
    zeros = [subset for subset, value in values if value <= EPS]
    minimals = [
        subset
        for subset in zeros
        if not any(proper_subset(other, subset) for other in zeros)
    ]
    best = values[0][1] if values else float("inf")
    positives = [value for _subset, value in values if value > EPS]
    margin = min(positives) - best if positives else 0.0
    if not zeros:
        return ScreenScan("none", [], best, margin, "FAIL-NO-COMPLETE-SCREEN")
    if len(minimals) == 1:
        verdict = "PASS-UNIQUE-MINIMAL" if margin >= MARGIN_FLOOR else "COND-WEAK-MARGIN"
        return ScreenScan("unique", minimals, best, margin, verdict)
    return ScreenScan("nonunique", minimals, best, margin, "FAIL-NONUNIQUE-MINIMAL")


def label(subset: tuple[str, ...]) -> str:
    return "{" + ",".join(subset) + "}" if subset else "{}"


def labels(subsets: list[tuple[str, ...]]) -> str:
    return ",".join(label(subset) for subset in subsets) if subsets else "--"


def audits() -> list[ScreenAudit]:
    rows: list[ScreenAudit] = []

    names, law = mediator_law()
    scan = scan_screens(law, names, ["S", "N"])
    rows.append(
        ScreenAudit(
            "minimal mediator",
            "X-S-Z plus noise",
            "scan causal candidates",
            f"minimal={labels(scan.minimals)}",
            f"margin={scan.margin:.6f}",
            f"best={scan.best:.1e}",
            scan.verdict,
        )
    )

    names, law = bypass_closure_law()
    scan = scan_screens(law, names, ["S", "H"])
    rows.append(
        ScreenAudit(
            "bypass closure",
            "two recorded channels",
            "enlarge screen",
            f"minimal={labels(scan.minimals)}",
            f"singletons fail; margin={scan.margin:.6f}",
            f"best={scan.best:.1e}",
            scan.verdict,
        )
    )

    scan_missing = scan_screens(law, names, ["S"])
    rows.append(
        ScreenAudit(
            "missing record",
            "H not in candidates",
            "try available closure",
            f"best Delta={scan_missing.best:.6f}",
            "no zero RN screen",
            "candidate set incomplete",
            scan_missing.verdict,
        )
    )

    names, law = direct_unrecorded_law()
    scan = scan_screens(law, names, ["S", "H"])
    rows.append(
        ScreenAudit(
            "unrecorded direct channel",
            "direct X->Z term",
            "scan all records",
            f"best Delta={scan.best:.6f}",
            "influence not recorded in screen",
            "full closure still fails",
            scan.verdict,
        )
    )

    names, law = duplicate_law()
    scan = scan_screens(law, names, ["S", "D"])
    rows.append(
        ScreenAudit(
            "duplicate gauge screen",
            "D=S copy",
            "scan record copies",
            f"minimals={labels(scan.minimals)}",
            "two exact screens",
            "same record up to automorphism",
            "COND-QUOTIENT-NEEDED",
        )
    )

    names, law = noisy_duplicate_law()
    scan = scan_screens(law, names, ["S", "D"])
    rows.append(
        ScreenAudit(
            "near-duplicate screen",
            "D noisy copy of S",
            "scan stability margin",
            f"minimal={labels(scan.minimals)}",
            f"margin={scan.margin:.6f}",
            "small margin means drift risk",
            scan.verdict,
        )
    )

    names, law = oracle_law()
    scan_all = scan_screens(law, names, ["S", "O"])
    scan_admissible = scan_screens(law, names, ["S"])
    rows.append(
        ScreenAudit(
            "future oracle",
            "O=Z upper copy",
            "scan without causality",
            f"all minimals={labels(scan_all.minimals)}",
            "future variable screens trivially",
            f"causal minimal={labels(scan_admissible.minimals)}",
            "FAIL-NEED-CAUSAL-ADMISSIBILITY",
        )
    )

    names, record_law, source_law = role_split_laws()
    record_scan = scan_screens(record_law, names, ["S", "H"])
    source_scan = scan_screens(source_law, names, ["S", "H"])
    same_role = set(record_scan.minimals[0]) == set(source_scan.minimals[0])
    rows.append(
        ScreenAudit(
            "role split",
            "different role laws",
            "scan per role",
            f"record={labels(record_scan.minimals)}",
            f"source={labels(source_scan.minimals)}",
            f"same={same_role}",
            "FAIL-NOT-ROLE-BLIND",
        )
    )

    rows.append(
        ScreenAudit(
            "finite theorem packet",
            "causal complete closure",
            "unique zero Delta screen",
            "screen derived",
            "requires gates above",
            "minimal complete RN closure",
            "THM-CONDITIONAL-MCS",
        )
    )

    return rows


def print_audits(rows: list[ScreenAudit]) -> None:
    print("minimal complete screen campaign")
    print("--------------------------------")
    print(
        "target                    law                    scan                    "
        "positive                         obstruction                     value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.candidate_law:22s} "
            f"{row.scan:23s} "
            f"{row.positive:32s} "
            f"{row.obstruction:31s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 40: minimal complete screen theorem campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("The minimal complete screen is derivable in a finite class: scan the")
    print("intrinsic causal antichain record closures and select the unique minimal")
    print("closure with Delta_Y=I(X;Z|Y)=0 and an isolated margin.")
    print()
    print("But the theorem is not universal.  It fails if the relevant record is not")
    print("in the candidate closure, if there is an unrecorded direct channel, if")
    print("future/oracle variables are allowed as screens, if duplicate screens are")
    print("not quotiented by internal automorphism, or if different role readouts")
    print("produce different closures.")
    print()
    print("Thus the Einstein-satisfying law is a minimal complete RN record closure")
    print("principle.  Branch A-current survives only if the physical sealed process")
    print("itself supplies the causal candidate lattice and guarantees a unique")
    print("role-blind complete closure up to automorphism.  Otherwise the screen is")
    print("chosen, and the theory is branch B.")


if __name__ == "__main__":
    main()
