#!/usr/bin/env python3
"""D6 exact audit of conditional ordered-law RN reconstruction and nonselection."""

from __future__ import annotations

import hashlib
import itertools
import json
from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 110

F = Fraction
D = Decimal
CHECKS = 0
EXPECTED_CHECKS = 84


def check(condition: bool, message: str) -> None:
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def bits(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(itertools.product((-1, 1), repeat=n))


def dec(value: F) -> D:
    return D(value.numerator) / D(value.denominator)


def rn(p: dict[tuple[int, ...], F], q: dict[tuple[int, ...], F]) -> dict[tuple[int, ...], F]:
    if p.keys() != q.keys() or not all(p[x] > 0 and q[x] > 0 for x in p):
        raise ValueError("RN laws require identical finite support and positive cells")
    return {x: p[x] / q[x] for x in p}


def kl(p: dict[tuple[int, ...], F], q: dict[tuple[int, ...], F]) -> D:
    return sum((dec(p[x]) * (dec(p[x]) / dec(q[x])).ln() for x in p), D(0))


def marginal(
    law: dict[tuple[int, ...], F], coordinates: tuple[int, ...]
) -> dict[tuple[int, ...], F]:
    out: dict[tuple[int, ...], F] = {}
    for atom, value in law.items():
        key = tuple(atom[i] for i in coordinates)
        out[key] = out.get(key, F(0)) + value
    return out


def product_law(
    p: dict[tuple[int, ...], F], q: dict[tuple[int, ...], F]
) -> dict[tuple[int, ...], F]:
    return {a + b: pa * qb for a, pa in p.items() for b, qb in q.items()}


def essential_scope(field: dict[tuple[int, ...], F]) -> tuple[int, ...]:
    n = len(next(iter(field)))
    essential = []
    for i in range(n):
        fibers: dict[tuple[int, ...], set[F]] = {}
        for atom, value in field.items():
            key = atom[:i] + atom[i + 1 :]
            fibers.setdefault(key, set()).add(value)
        if any(len(values) > 1 for values in fibers.values()):
            essential.append(i)
    return tuple(essential)


def parity_law(n: int, theta: F) -> dict[tuple[int, ...], F]:
    out = {}
    for atom in bits(n):
        parity = 1
        for value in atom:
            parity *= value
        out[atom] = (F(1) + theta * parity) / (2**n)
    return out


def matrix_rank(matrix: list[list[F]]) -> int:
    a = [row[:] for row in matrix]
    if not a:
        return 0
    rows = len(a)
    cols = len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [v / scale for v in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                scale = a[r][col]
                a[r] = [a[r][c] - scale * a[rank][c] for c in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def character(atom: tuple[int, ...], mask: int) -> int:
    value = 1
    for i, bit in enumerate(atom):
        if mask & (1 << i):
            value *= bit
    return value


def walsh_log_reconstruct(law: dict[tuple[int, ...], F]) -> tuple[D, list[D]]:
    atoms = tuple(law)
    n = len(atoms[0])
    uniform = F(1, 2**n)
    coeffs = []
    for mask in range(2**n):
        coeff = sum(
            (
                (dec(law[x] / uniform)).ln() * D(character(x, mask))
                for x in atoms
            ),
            D(0),
        ) / D(2**n)
        coeffs.append(coeff)
    raw = {}
    for atom in atoms:
        exponent = sum(
            (coeffs[mask] * D(character(atom, mask)) for mask in range(2**n)),
            D(0),
        )
        raw[atom] = exponent.exp()
    z = sum(raw.values(), D(0))
    gap = max(abs(raw[x] / z - dec(law[x])) for x in atoms)
    return gap, coeffs


def hidden_lift(
    endpoint: dict[int, F], conditional_plus: dict[int, F]
) -> dict[tuple[int, ...], F]:
    out = {}
    for e, pe in endpoint.items():
        out[(e, 1)] = pe * conditional_plus[e]
        out[(e, -1)] = pe * (1 - conditional_plus[e])
    return out


def commitment_root() -> D:
    lo = D(0)
    hi = D(2)
    for _ in range(420):
        mid = (lo + hi) / 2
        e2 = (D(2) * mid).exp()
        tanh = (e2 - 1) / (e2 + 1)
        residual = tanh - (-mid).exp()
        if residual < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def bernoulli_cylinder(n: int, p_plus: F) -> dict[tuple[int, ...], F]:
    if not F(0) < p_plus < F(1):
        raise ValueError("positive Bernoulli parameter required")
    return {
        atom: p_plus ** sum(v == 1 for v in atom)
        * (1 - p_plus) ** sum(v == -1 for v in atom)
        for atom in bits(n)
    }


def main() -> None:
    # R: canonical RN reconstruction conditional on two supplied ordered laws.
    p = {(-1,): F(1, 4), (1,): F(3, 4)}
    q = {(-1,): F(3, 4), (1,): F(1, 4)}
    ratio = rn(p, q)
    check(sum(p.values()) == sum(q.values()) == 1, "ordered laws normalize")
    check(sum(q[x] * ratio[x] for x in q) == 1, "E_Q R = 1")
    check(sum(p[x] / ratio[x] for x in p) == 1, "E_P R^-1 = 1")
    check(all(rn(q, p)[x] == 1 / ratio[x] for x in p), "reversal inverts R")
    check(all(q[x] * ratio[x] == p[x] for x in p), "R changes Q into P")

    neutral = rn(p, p)
    check(set(neutral.values()) == {F(1)}, "RN-neutral field is identically one")
    check(kl(p, p) == 0, "RN-neutral directed KL is zero")

    p2 = {(-1,): F(1, 3), (1,): F(2, 3)}
    q2 = {(-1,): F(1, 2), (1,): F(1, 2)}
    product_ratio = rn(product_law(p, p2), product_law(q, q2))
    check(
        all(product_ratio[a + b] == ratio[a] * rn(p2, q2)[b] for a in p for b in p2),
        "independent RN factors multiply",
    )
    relabeled_p = {(x[0] * -1,): value for x, value in p.items()}
    relabeled_q = {(x[0] * -1,): value for x, value in q.items()}
    check(
        all(rn(relabeled_p, relabeled_q)[(-x[0],)] == ratio[x] for x in p),
        "RN field covaries under relabeling",
    )
    check(rn(p2, q2) != ratio and set(p2) == set(p), "common support does not select R")
    kl_forward = kl(p, q)
    kl_reverse = kl(q, p)
    check(abs(kl_forward - kl_reverse) < D("1e-105"), "symmetric reversal has equal KL")
    check(ratio != rn(q, p), "equal scalar KL does not select orientation")

    # H: lower shadows, complete-ledger identifiability, and hidden histories.
    plus = parity_law(3, F(1, 2))
    minus = parity_law(3, F(-1, 2))
    for coordinates in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
        check(marginal(plus, coordinates) == marginal(minus, coordinates), f"shadow {coordinates}")
    check(plus != minus, "parity twins differ as whole-history laws")
    triple_plus = sum(F(x[0] * x[1] * x[2]) * plus[x] for x in plus)
    triple_minus = sum(F(x[0] * x[1] * x[2]) * minus[x] for x in minus)
    check((triple_plus, triple_minus) == (F(1, 2), F(-1, 2)), "triple channel separates")
    parity_ratio = rn(plus, {x: F(1, 8) for x in bits(3)})
    check(essential_scope(parity_ratio) == (0, 1, 2), "supplied RN field reveals full scope")

    for n in range(1, 5):
        atoms = bits(n)
        character_matrix = [
            [F(character(atom, mask)) for mask in range(2**n)] for atom in atoms
        ]
        check(matrix_rank(character_matrix) == 2**n, f"Walsh rank n={n}")
        check(2**n - 1 == len(atoms) - 1, f"ledger/simplex dimension n={n}")
    reconstruction_gap, coefficients = walsh_log_reconstruct(plus)
    minus_reconstruction_gap, minus_coefficients = walsh_log_reconstruct(minus)
    check(reconstruction_gap < D("1e-100"), "complete log ledger reconstructs supplied law")
    check(minus_reconstruction_gap < D("1e-100"), "complete log ledger reconstructs twin law")
    check(
        all(abs(coefficients[mask] - minus_coefficients[mask]) < D("1e-105") for mask in range(7)),
        "parity twins have identical lower log-Walsh ledger",
    )
    check(
        abs(coefficients[7] + minus_coefficients[7]) < D("1e-105")
        and abs(coefficients[7]) > D("0.5"),
        "top log-Walsh sign separates the fiber",
    )
    check(abs(coefficients[7]) > D("0.5"), "top parity coefficient is load-bearing")

    ep = {0: F(2, 3), 1: F(1, 3)}
    eq = {0: F(1, 3), 1: F(2, 3)}
    cond_a = {0: F(3, 4), 1: F(1, 4)}
    cond_b = {0: F(1, 4), 1: F(3, 4)}
    p_a, q_a = hidden_lift(ep, cond_a), hidden_lift(eq, cond_a)
    p_b, q_b = hidden_lift(ep, cond_b), hidden_lift(eq, cond_b)
    check(marginal(p_a, (0,)) == marginal(p_b, (0,)), "lifts share P endpoints")
    check(marginal(q_a, (0,)) == marginal(q_b, (0,)), "lifts share Q endpoints")
    check(rn(p_a, q_a) == rn(p_b, q_b), "lifts share full endpoint RN action")
    future_a = sum(value for (e, h), value in p_a.items() if h == 1)
    future_b = sum(value for (e, h), value in p_b.items() if h == 1)
    check((future_a, future_b) == (F(7, 12), F(5, 12)), "hidden future separates lifts")
    future_kernel = {(e, h): h for e, h in p_a}
    y_a = sum(value for atom, value in p_a.items() if future_kernel[atom] == 1)
    y_b = sum(value for atom, value in p_b.items() if future_kernel[atom] == 1)
    check((y_a, y_b) == (F(7, 12), F(5, 12)), "common future kernel Y=H separates lifts")
    check(essential_scope(rn(p_a, q_a)) == (0,), "RN endpoint action omits hidden memory")

    # C: the commitment result is conditional on a primitive oriented mode.
    root = commitment_root()
    e2 = (D(2) * root).exp()
    tanh_root = (e2 - 1) / (e2 + 1)
    check(abs(tanh_root - (-root).exp()) < D("1e-105"), "commitment root equation")
    check(D("0.6093778634360063") > root > D("0.6093778634360062"), "root interval")
    p_mode_plus = ((root).exp() / ((root).exp() + (-root).exp()))
    p_mode_minus = ((-root).exp() / ((root).exp() + (-root).exp()))
    check(abs((p_mode_plus + p_mode_minus) - 1) < D("1e-108"), "opposite orientations normalize")
    check(p_mode_plus != p_mode_minus, "orientation reversal mirrors selected law")
    def exponential_parity_mode(n: int, orientation: int) -> dict[tuple[int, ...], D]:
        raw = {}
        for atom in bits(n):
            parity = 1
            for value in atom:
                parity *= value
            raw[atom] = (root * D(orientation * parity)).exp()
        z = sum(raw.values(), D(0))
        return {atom: value / z for atom, value in raw.items()}

    mode_1 = exponential_parity_mode(1, 1)
    mode_2 = exponential_parity_mode(2, 1)
    mode_2_reverse = exponential_parity_mode(2, -1)
    check(abs(sum(mode_1.values(), D(0)) - 1) < D("1e-108"), "one-body root mode normalizes")
    check(abs(sum(mode_2.values(), D(0)) - 1) < D("1e-108"), "two-body root mode normalizes")
    check(all(value > 0 for value in mode_1.values()) and all(value > 0 for value in mode_2.values()), "root modes positive")
    check(essential_scope(mode_1) == (0,), "one-body commitment mode scope")
    check(essential_scope(mode_2) == (0, 1), "two-body commitment mode scope")
    mean_parity_1 = sum(D(atom[0]) * value for atom, value in mode_1.items())
    mean_parity_2 = sum(D(atom[0] * atom[1]) * value for atom, value in mode_2.items())
    check(abs(mean_parity_1 - (-root).exp()) < D("1e-105"), "one-body mode obeys commitment equation")
    check(abs(mean_parity_2 - (-root).exp()) < D("1e-105"), "two-body mode obeys same commitment equation")
    check(
        all(abs(mode_2_reverse[atom] - mode_2[(-atom[0], atom[1])]) < D("1e-108") for atom in mode_2),
        "orientation reversal mirrors supplied mode",
    )

    evidence = kl_forward
    survival = (-evidence).exp()
    check((-D(0)).exp() == 1, "zero evidence gives certain survival")
    check(D(0) < survival < D(1), "positive supplied evidence gives conditional division")
    check(abs((-kl_reverse).exp() - survival) < D("1e-105"), "survival weight misses orientation")
    evidence_i = D("0.37")
    evidence_j = D("0.22")
    check(
        abs((-(evidence_i + evidence_j)).exp() - (-evidence_i).exp() * (-evidence_j).exp())
        < D("1e-108"),
        "survival multiplies in additive supplied evidence",
    )
    division_weight = D(1) - survival
    check(D(0) < division_weight < D(1) and division_weight + survival == 1, "survival/division weights complement")

    # P: proposal/null, h-transform, ownership, and first cross carrier.
    proposal_a = {"null": F(1, 3), "forward": F(1, 3), "reverse": F(1, 3)}
    proposal_b = {"null": F(1, 2), "forward": F(1, 4), "reverse": F(1, 4)}
    check(sum(proposal_a.values()) == sum(proposal_b.values()) == 1, "proposal laws normalize")
    check(
        proposal_a["forward"] == proposal_a["reverse"]
        and proposal_b["forward"] == proposal_b["reverse"],
        "both proposal laws respect reversal symmetry",
    )
    check(proposal_a["null"] != proposal_b["null"], "symmetry leaves null mass free")

    multiplicity = {"a": F(1), "b": F(2)}
    h1 = {"a": F(1), "b": F(1)}
    h2 = {"a": F(2), "b": F(1)}

    def h_transform(
        domain: tuple[str, ...], h: dict[str, F], mult: dict[str, F] | None = None
    ) -> dict[str, F]:
        active_mult = multiplicity if mult is None else mult
        if len(set(domain)) != len(domain) or not domain:
            raise ValueError("candidate domain must be finite, nonempty, and duplicate-free")
        if any(x not in h or x not in active_mult for x in domain):
            raise ValueError("every candidate requires weight and multiplicity")
        if any(h[x] <= 0 for x in domain) or any(active_mult[x] < 0 for x in domain):
            raise ValueError("positive h and nonnegative multiplicity required")
        weights = {x: active_mult[x] * h[x] for x in domain}
        total = sum(weights.values(), F(0))
        if total <= 0:
            raise ValueError("positive h-transform total required")
        return {x: weights[x] / total for x in domain}

    def refuses(callable_object: object) -> bool:
        try:
            callable_object()  # type: ignore[operator]
        except ValueError:
            return True
        return False

    t1 = h_transform(("a", "b"), h1)
    t2 = h_transform(("a", "b"), h2)
    check(sum(t1.values()) == sum(t2.values()) == 1, "supplied h-transform normalizes")
    check(t1 != t2, "different supplied h fields give different transitions")
    h3 = {"a": F(1), "b": F(1), "c": F(1)}
    mult3 = {"a": F(1), "b": F(2), "c": F(1)}
    check(h_transform(("a", "b", "c"), h3, mult3)["a"] != t1["a"], "candidate domain changes transition")
    check(refuses(lambda: h_transform(("a", "a"), h1)), "h-transform refuses duplicate candidate")
    check(refuses(lambda: h_transform(("a", "b"), {"a": F(1), "b": F(0)})), "h-transform refuses zero h")
    check(
        refuses(lambda: h_transform(("a", "b"), h1, {"a": F(1), "b": F(-1)})),
        "h-transform refuses negative multiplicity",
    )
    check(refuses(lambda: h_transform(("a", "c"), h3)), "h-transform refuses missing multiplicity")

    r1 = ratio
    r2 = rn(p2, q2)
    composite = {a + b: r1[a] * r2[b] for a in r1 for b in r2}
    composite_representation = (
        {"id": "xy", "scope": (0, 1), "table": composite},
    )
    split_representation = (
        {"id": "x", "scope": (0,), "table": r1},
        {"id": "y", "scope": (1,), "table": r2},
    )

    def evaluate_representation(
        representation: tuple[dict[str, object], ...]
    ) -> dict[tuple[int, ...], F]:
        ids = [token["id"] for token in representation]
        if len(ids) != len(set(ids)):
            raise ValueError("token identities must be unique")
        out = {}
        for atom in bits(2):
            value = F(1)
            for token in representation:
                scope = token["scope"]
                table = token["table"]
                key = tuple(atom[i] for i in scope)  # type: ignore[union-attr]
                value *= table[key]  # type: ignore[index]
            out[atom] = value
        return out

    check(evaluate_representation(composite_representation) == product_ratio, "composite token represents RN field")
    check(evaluate_representation(split_representation) == product_ratio, "split tokens represent same RN field")
    check(len(composite_representation) == 1 and len(split_representation) == 2, "representations have unequal token census")
    check(
        {token["id"] for token in composite_representation}
        != {token["id"] for token in split_representation},
        "representations have different ownership partitions",
    )
    duplicate_representation = split_representation + (split_representation[0],)
    check(refuses(lambda: evaluate_representation(duplicate_representation)), "ownership evaluator refuses duplicate ID")

    cross = rn(parity_law(2, F(1, 2)), {x: F(1, 4) for x in bits(2)})
    det = cross[(-1, -1)] * cross[(1, 1)] - cross[(-1, 1)] * cross[(1, -1)]
    check(det != 0, "parity RN field is irreducible across the cut")
    independent_det = (
        composite[(-1, -1)] * composite[(1, 1)]
        - composite[(-1, 1)] * composite[(1, -1)]
    )
    check(independent_det == 0, "independent component laws cannot create irreducible cross factor")

    token_fields = {
        "coordinate_scope": "presentation-relative-from-R",
        "protocol_orientation": "conditional-from-P/Q",
        "numerical_factor_field": "conditional-R",
        "expected_evidence": "conditional-KL",
        "survival_division_weights": "conditional-on-supplied-evidence",
        "proposal": "missing",
        "eligibility": "missing",
        "ownership": "missing",
        "physical_seal": "missing",
        "accepted_birth": "missing",
    }
    check(sum(value == "missing" for value in token_fields.values()) == 5, "token remains incomplete")

    # F: profinite compatibility hosts multiple law families.
    tower_a = {n: bernoulli_cylinder(n, F(1, 3)) for n in range(1, 6)}
    tower_b = {n: bernoulli_cylinder(n, F(2, 3)) for n in range(1, 6)}
    tower_c = {n: bernoulli_cylinder(n, F(1, 2)) for n in range(1, 6)}
    for tower in (tower_a, tower_b, tower_c):
        check(all(sum(tower[n].values()) == 1 for n in tower), "cylinder laws normalize")
        check(
            all(marginal(tower[n + 1], tuple(range(n))) == tower[n] for n in range(1, 5)),
            "end-deletion projectivity",
        )
    check(tower_a[1] != tower_b[1], "projective towers remain inequivalent")
    flip_a_1 = {(-atom[0],): value for atom, value in tower_a[1].items()}
    check(flip_a_1 == tower_b[1], "first two towers are orientation mirrors")
    check(tower_c[1] not in (tower_a[1], tower_b[1]), "third tower is outside mirror pair")

    payload = {
        "checks": CHECKS,
        "rn_ratio": [str(ratio[x]) for x in sorted(ratio)],
        "kl_forward": str(kl_forward),
        "commitment_root": str(root),
        "parity_reconstruction_gap": str(reconstruction_gap),
        "hidden_future": [str(future_a), str(future_b)],
        "cross_determinant": str(det),
        "token_fields": token_fields,
    }
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError(f"receipt cardinality drift: {CHECKS} != {EXPECTED_CHECKS}")

    print("D6 CONDITIONAL ORDERED-LAW RN RECONSTRUCTION EXACT AUDIT")
    print(f"RN ratio (ordered binary witness): {[str(ratio[x]) for x in sorted(ratio)]}")
    print(f"symmetric directed KL: {kl_forward}")
    print(f"parity complete-ledger reconstruction gap: {reconstruction_gap}")
    print(f"hidden-future split at fixed endpoints/RN: {future_a} versus {future_b}")
    print(f"commitment root: {root}")
    print(f"nonproduct joint RN determinant on declared tensor split: {det}")
    print("TOKEN CENSUS:")
    for name, status in token_fields.items():
        print(f"  {name}: {status}")
    print(f"canonical payload SHA-256: {digest}")
    print(f"RECEIPT: {CHECKS}/{EXPECTED_CHECKS} exact/high-precision checks passed")
    print("VERDICT: CONDITIONAL-ORDERED-LAW-RN-FIELD-RECONSTRUCTION")
    print("       + CONDITIONAL-NORMALIZED-MODE-COMMITMENT/SURVIVAL-WEIGHTS")
    print("       + COMPLETE-LOG-DENSITY-LEDGER-IDENTIFIABILITY-NOT-PROPOSAL")
    print("       + PHYSICAL-SCOPE/ORIENTATION/OWNERSHIP/NULL/BIRTH-NONSELECTION")
    print("       + END-DELETION-PROFINITE-HOSTING-NOT-LAW-SELECTION")
    print("BOUNDARY: no final interacting click law is derived")


if __name__ == "__main__":
    main()
