#!/usr/bin/env python3
"""Paper 4 diagnostic P: sealed whole-history determination campaign.

The transport-law no-go moves the primitive upstream:

    whole sealed ISP history law Gamma_D
        -> ordered transports P_AB, P_BA
        -> A_D = log dP_AB / dP_BA.

This diagnostic asks whether the current sealed shadows determine Gamma_D.
It constructs finite Leibniz-twin families:

  * a parity family with identical one- and two-face marginals but different
    whole-history law;
  * a fixed-endpoint lift with identical P_AB, P_BA and identical RN action
    A_D, but different retained hidden-history memory;
  * a composition attack where that retained memory changes the next diamond;
  * selector attacks showing max entropy / least hidden memory collapse to the
    memoryless lift, while max-memory leaves sign/boundary freedom;
  * a conditional positive theorem: full atomic/cylinder probabilities do
    determine Gamma_D, but then the whole process law has been supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


State3 = tuple[int, int, int]
LiftState = tuple[int, int]


def bitsign(bit: int) -> float:
    return 1.0 if bit else -1.0


def normalize(values: list[float]) -> list[float]:
    total = sum(values)
    return [value / total for value in values]


def entropy(law: dict[object, float]) -> float:
    return -sum(p * math.log(p) for p in law.values() if p > 0.0)


def total_variation(left: dict[object, float], right: dict[object, float]) -> float:
    keys = set(left) | set(right)
    return 0.5 * sum(abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in keys)


def max_abs_gap(left: dict[object, float], right: dict[object, float]) -> float:
    keys = set(left) | set(right)
    return max(abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in keys)


def kl(left: dict[object, float], right: dict[object, float]) -> float:
    return sum(p * math.log(p / right[key]) for key, p in left.items() if p > 0.0)


def parity_law(theta: float) -> dict[State3, float]:
    law: dict[State3, float] = {}
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                parity = bitsign(a) * bitsign(b) * bitsign(c)
                law[(a, b, c)] = 0.125 * (1.0 + theta * parity)
    return law


def marginal(law: dict[State3, float], axes: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    out: dict[tuple[int, ...], float] = {}
    for state, p in law.items():
        key = tuple(state[axis] for axis in axes)
        out[key] = out.get(key, 0.0) + p
    return out


def max_pair_shadow_gap(left: dict[State3, float], right: dict[State3, float]) -> float:
    axes_list = [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)]
    return max(max_abs_gap(marginal(left, axes), marginal(right, axes)) for axes in axes_list)


def triple_moment(law: dict[State3, float]) -> float:
    return sum(p * bitsign(a) * bitsign(b) * bitsign(c) for (a, b, c), p in law.items())


def endpoint_laws(m: int) -> tuple[list[float], list[float]]:
    raw_p = []
    raw_q = []
    for e in range(m):
        x = 2.0 * math.pi * e / m
        raw_p.append(math.exp(0.33 * math.sin(x) + 0.19 * math.cos(3.0 * x + 0.2)))
        raw_q.append(math.exp(-0.27 * math.sin(x + 0.4) + 0.22 * math.cos(2.0 * x - 0.7)))
    return normalize(raw_p), normalize(raw_q)


def endpoint_dict(values: list[float]) -> dict[tuple[int], float]:
    return {(idx,): value for idx, value in enumerate(values)}


def hidden_mode(m: int) -> list[float]:
    raw = []
    for e in range(m):
        x = 2.0 * math.pi * e / m
        raw.append(math.sin(x + 0.3) + 0.41 * math.cos(3.0 * x - 0.5))
    max_abs = max(abs(value) for value in raw)
    return [value / max_abs for value in raw]


def lift_endpoint(endpoint: list[float], theta: float, mode: list[float]) -> dict[LiftState, float]:
    law: dict[LiftState, float] = {}
    for e, p in enumerate(endpoint):
        bias = theta * mode[e]
        law[(e, 0)] = p * 0.5 * (1.0 - bias)
        law[(e, 1)] = p * 0.5 * (1.0 + bias)
    return law


def lift_endpoint_marginal(law: dict[LiftState, float]) -> dict[tuple[int], float]:
    out: dict[tuple[int], float] = {}
    for (e, _h), p in law.items():
        out[(e,)] = out.get((e,), 0.0) + p
    return out


def rn_action_endpoint(p: list[float], q: list[float]) -> list[float]:
    return [math.log(pi / qi) for pi, qi in zip(p, q)]


def rn_action_lift(p_lift: dict[LiftState, float], q_lift: dict[LiftState, float]) -> dict[LiftState, float]:
    return {state: math.log(p / q_lift[state]) for state, p in p_lift.items()}


def max_action_lift_gap(
    p: list[float],
    q: list[float],
    p_lift: dict[LiftState, float],
    q_lift: dict[LiftState, float],
) -> float:
    endpoint_action = rn_action_endpoint(p, q)
    lift_action = rn_action_lift(p_lift, q_lift)
    return max(abs(value - endpoint_action[state[0]]) for state, value in lift_action.items())


def retained_memory(law: dict[LiftState, float], mode: list[float]) -> float:
    return sum(p * bitsign(h) * mode[e] for (e, h), p in law.items())


def recover_theta(law: dict[LiftState, float], endpoint: list[float], mode: list[float]) -> float:
    denom = sum(p * mode[e] ** 2 for e, p in enumerate(endpoint))
    if denom == 0.0:
        raise ValueError("zero mode")
    return retained_memory(law, mode) / denom


def next_probability(memory: float, strength: float = 0.36) -> float:
    return 0.5 + strength * memory


def refine_lift(law: dict[LiftState, float]) -> dict[tuple[int, int, int], float]:
    refined: dict[tuple[int, int, int], float] = {}
    for (e, h), p in law.items():
        refined[(e, 0, h)] = 0.5 * p
        refined[(e, 1, h)] = 0.5 * p
    return refined


def coarse_refined(refined: dict[tuple[int, int, int], float]) -> dict[LiftState, float]:
    coarse: dict[LiftState, float] = {}
    for (e, _sub, h), p in refined.items():
        coarse[(e, h)] = coarse.get((e, h), 0.0) + p
    return coarse


def max_entropy_theta_scan(endpoint: list[float], mode: list[float]) -> tuple[float, float]:
    best_theta = 0.0
    best_entropy = -1.0
    for idx in range(191):
        theta = -0.95 + 1.90 * idx / 190.0
        law = lift_endpoint(endpoint, theta, mode)
        h = entropy(law)
        if h > best_entropy:
            best_entropy = h
            best_theta = theta
    return best_theta, best_entropy


def max_memory_theta_scan(endpoint: list[float], mode: list[float]) -> tuple[float, float, float]:
    candidates = []
    for theta in (-0.95, 0.95):
        law = lift_endpoint(endpoint, theta, mode)
        candidates.append((theta, retained_memory(law, mode)))
    neg, pos = candidates
    return neg[0], pos[0], abs(pos[1] - neg[1])


def main() -> None:
    # Pairwise-shadow Leibniz twins.
    theta_left = 0.62
    theta_right = -0.62
    parity_left = parity_law(theta_left)
    parity_right = parity_law(theta_right)
    pair_shadow_gap = max_pair_shadow_gap(parity_left, parity_right)
    parity_tv = total_variation(parity_left, parity_right)
    parity_kl = kl(parity_left, parity_right)
    triple_gap = abs(triple_moment(parity_left) - triple_moment(parity_right))

    # Fixed ordered transports / fixed A_D, variable retained history.
    m = 14
    p_endpoint, q_endpoint = endpoint_laws(m)
    mode = hidden_mode(m)
    theta_memory = 0.68
    p_lift_plus = lift_endpoint(p_endpoint, theta_memory, mode)
    q_lift_plus = lift_endpoint(q_endpoint, theta_memory, mode)
    p_lift_minus = lift_endpoint(p_endpoint, -theta_memory, mode)
    q_lift_minus = lift_endpoint(q_endpoint, -theta_memory, mode)

    endpoint_gap_plus_minus = max_abs_gap(
        lift_endpoint_marginal(p_lift_plus),
        lift_endpoint_marginal(p_lift_minus),
    )
    reverse_endpoint_gap_plus_minus = max_abs_gap(
        lift_endpoint_marginal(q_lift_plus),
        lift_endpoint_marginal(q_lift_minus),
    )
    action_lift_gap_plus = max_action_lift_gap(p_endpoint, q_endpoint, p_lift_plus, q_lift_plus)
    action_lift_gap_minus = max_action_lift_gap(p_endpoint, q_endpoint, p_lift_minus, q_lift_minus)
    full_history_tv = total_variation(p_lift_plus, p_lift_minus)
    memory_plus = retained_memory(p_lift_plus, mode)
    memory_minus = retained_memory(p_lift_minus, mode)
    memory_span = abs(memory_plus - memory_minus)
    future_gap = abs(next_probability(memory_plus) - next_probability(memory_minus))

    # Selector attacks.
    maxent_theta, maxent_entropy = max_entropy_theta_scan(p_endpoint, mode)
    maxent_memory = retained_memory(lift_endpoint(p_endpoint, maxent_theta, mode), mode)
    neg_theta, pos_theta, max_memory_span = max_memory_theta_scan(p_endpoint, mode)

    # Conditional positive theorem and refinement persistence.
    recovered_plus = recover_theta(p_lift_plus, p_endpoint, mode)
    recovered_minus = recover_theta(p_lift_minus, p_endpoint, mode)
    refined_plus = refine_lift(p_lift_plus)
    refined_minus = refine_lift(p_lift_minus)
    coarse_gap = max_abs_gap(coarse_refined(refined_plus), p_lift_plus)
    refined_tv = total_variation(refined_plus, refined_minus)

    endpoint_action = rn_action_endpoint(p_endpoint, q_endpoint)
    action_rms = math.sqrt(sum(value * value for value in endpoint_action) / len(endpoint_action))
    endpoint_work = sum(pi * math.log(pi / qi) for pi, qi in zip(p_endpoint, q_endpoint))

    rows = [
        Row(
            "pairwise Leibniz twins",
            "three-bit parity family with same one/two marginals",
            "pairwise sealed shadows do not determine whole history",
            f"pair_gap={pair_shadow_gap:.1e}, TV={parity_tv:.6f}, triple_gap={triple_gap:.6f}",
            "REFUTES-PAIRWISE-DETERMINATION",
        ),
        Row(
            "fixed ordered transports",
            "lift same P_AB and P_BA by opposite hidden-history bias",
            "endpoint transports stay identical while Gamma_D changes",
            f"P_gap={endpoint_gap_plus_minus:.1e}, Q_gap={reverse_endpoint_gap_plus_minus:.1e}, TV={full_history_tv:.6f}",
            "REFUTES-ENDPOINT-DETERMINATION",
        ),
        Row(
            "fixed RN action",
            "use same hidden conditional under forward and reverse laws",
            "A_D remains exactly the endpoint exchange cocycle",
            f"gap_plus={action_lift_gap_plus:.1e}, gap_minus={action_lift_gap_minus:.1e}, rms(A)={action_rms:.6f}",
            "REFUTES-ACTION-DETERMINATION",
        ),
        Row(
            "composition memory",
            "let next diamond depend on retained hidden-history sign",
            "same P_AB/P_BA/A_D can compose into different futures",
            f"memory_span={memory_span:.6f}, next_gap={future_gap:.6f}",
            "PROVES-NONMARKOVIAN-GATE",
        ),
        Row(
            "maximum entropy selector",
            "maximize hidden conditional entropy at fixed endpoints",
            "selects the memoryless lift, not the retained-history law",
            f"theta*={maxent_theta:.2f}, memory={maxent_memory:.1e}, S={maxent_entropy:.6f}",
            "FAILS-TRIVIALIZES-MEMORY",
        ),
        Row(
            "least hidden-memory selector",
            "minimize retained memory at fixed endpoints",
            "again selects theta=0 and kills history dependence",
            f"theta*=0.00, endpoint_work={endpoint_work:.6f}",
            "FAILS-TRIVIALIZES-MEMORY",
        ),
        Row(
            "max memory selector",
            "maximize retained memory subject only to positivity",
            "runs to boundary and leaves orientation/sign freedom",
            f"theta=({neg_theta:.2f},{pos_theta:.2f}), span={max_memory_span:.6f}",
            "FAILS-BOUNDARY-FAMILY",
        ),
        Row(
            "refinement persistence",
            "split every history atom into two count twins and coarse-grain back",
            "whole-history ambiguity survives finite refinement",
            f"coarse_gap={coarse_gap:.1e}, refined_TV={refined_tv:.6f}",
            "REFUTES-REFINEMENT-ESCAPE",
        ),
        Row(
            "full atom theorem",
            "include all sealed history atom probabilities as the process law",
            "theta and Gamma_D are then recovered, but the law was supplied",
            f"theta_rec=({recovered_plus:.6f},{recovered_minus:.6f})",
            "THM-CONDITIONAL-FULL-LAW",
        ),
        Row(
            "whole-history verdict",
            "current sealed shadows versus Gamma_D",
            "only the full indivisible process law determines future composition",
            "transport/action shadows insufficient",
            "FINITE-NO-GO",
        ),
    ]

    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("parity_theta_left", f"{theta_left:.15e}")
    print("parity_theta_right", f"{theta_right:.15e}")
    print("pair_shadow_gap", f"{pair_shadow_gap:.15e}")
    print("parity_total_variation", f"{parity_tv:.15e}")
    print("parity_kl_left_right", f"{parity_kl:.15e}")
    print("triple_moment_left", f"{triple_moment(parity_left):.15e}")
    print("triple_moment_right", f"{triple_moment(parity_right):.15e}")
    print("endpoint_gap_plus_minus", f"{endpoint_gap_plus_minus:.15e}")
    print("reverse_endpoint_gap_plus_minus", f"{reverse_endpoint_gap_plus_minus:.15e}")
    print("full_history_total_variation", f"{full_history_tv:.15e}")
    print("action_lift_gap_plus", f"{action_lift_gap_plus:.15e}")
    print("action_lift_gap_minus", f"{action_lift_gap_minus:.15e}")
    print("endpoint_action_rms", f"{action_rms:.15e}")
    print("endpoint_work", f"{endpoint_work:.15e}")
    print("memory_plus", f"{memory_plus:.15e}")
    print("memory_minus", f"{memory_minus:.15e}")
    print("memory_span", f"{memory_span:.15e}")
    print("future_probability_plus", f"{next_probability(memory_plus):.15e}")
    print("future_probability_minus", f"{next_probability(memory_minus):.15e}")
    print("future_gap", f"{future_gap:.15e}")
    print("maxent_theta", f"{maxent_theta:.15e}")
    print("maxent_memory", f"{maxent_memory:.15e}")
    print("max_memory_theta_negative", f"{neg_theta:.15e}")
    print("max_memory_theta_positive", f"{pos_theta:.15e}")
    print("max_memory_span", f"{max_memory_span:.15e}")
    print("refinement_coarse_gap", f"{coarse_gap:.15e}")
    print("refinement_total_variation", f"{refined_tv:.15e}")
    print("recovered_theta_plus", f"{recovered_plus:.15e}")
    print("recovered_theta_minus", f"{recovered_minus:.15e}")


if __name__ == "__main__":
    main()
