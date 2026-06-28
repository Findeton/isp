#!/usr/bin/env python3
"""
Collapsed Paper 23 receipt: overlap-component factorization audit.

The transfer-operator cycle theorem is conditional on a pair-factor picture:
overlap-graph components should contribute multiplicatively.  This receipt
hostile-tests that assumption directly at exact unlabeled P_8.

It reuses the width-2 hidden-matching setup.  For every hidden matching H it
samples the conditional clustered law Q_H, computes every cross factor

    sum_o q_H(o) q_H'(o) / p(o),

and groups by overlap signature.  It then asks whether the five N=8 signatures

    (4,), (2,2), (1,3), (1,1,2), (1,1,1,1)

can be explained by component weights beta_1,beta_2,beta_3,beta_4 via

    M(signature) ~= product beta_part.

The result is a hostile test of the transfer-operator toy theorem.  If
component factorization fails, the next theorem target must be conditional
order-likelihood factorization itself, not only spectral control of a centered
pair operator.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
import random
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def iter_bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


class Poset:
    def __init__(self, future):
        self.future = tuple(future)
        self.N = len(self.future)
        self.past = [0] * self.N
        for x, mask in enumerate(self.future):
            for y in iter_bits(mask):
                self.past[y] |= 1 << x
        self.past = tuple(self.past)


def poset_from_permutation(perm):
    n = len(perm)
    future = [0] * n
    for i in range(n):
        vi = perm[i]
        mask = 0
        for j in range(i + 1, n):
            if vi < perm[j]:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


def coordinate_order_poset(points):
    future = [0] * len(points)
    for i, (ui, vi) in enumerate(points):
        mask = 0
        for j, (uj, vj) in enumerate(points):
            if ui < uj and vi < vj:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


CANON_CACHE = {}


def refined_color_classes(poset):
    n = poset.N
    all_mask = (1 << n) - 1
    colors = tuple((poset.past[i].bit_count(), poset.future[i].bit_count()) for i in range(n))
    while True:
        signatures = []
        for i in range(n):
            bit = 1 << i
            incomparable = all_mask ^ bit ^ poset.past[i] ^ poset.future[i]
            signatures.append(
                (
                    colors[i],
                    tuple(sorted(colors[j] for j in iter_bits(poset.past[i]))),
                    tuple(sorted(colors[j] for j in iter_bits(poset.future[i]))),
                    tuple(sorted(colors[j] for j in iter_bits(incomparable))),
                )
            )
        unique = {sig: rank for rank, sig in enumerate(sorted(set(signatures), key=repr))}
        new_colors = tuple(unique[sig] for sig in signatures)
        if new_colors == colors:
            break
        colors = new_colors
    classes = {}
    for i, color in enumerate(colors):
        classes.setdefault(color, []).append(i)
    return [tuple(classes[color]) for color in sorted(classes)]


def code_for_order(poset, order):
    bits = []
    for i, a in enumerate(order):
        future = poset.future[a]
        for j, b in enumerate(order):
            if i != j:
                bits.append("1" if future & (1 << b) else "0")
    return "".join(bits)


def canonical_unlabeled_code(poset):
    cached = CANON_CACHE.get(poset.future)
    if cached is not None:
        return cached
    classes = refined_color_classes(poset)
    best = None
    for selected in product(*(permutations(cls) for cls in classes)):
        order = tuple(v for block in selected for v in block)
        code = code_for_order(poset, order)
        if best is None or code < best:
            best = code
    CANON_CACHE[poset.future] = best
    return best


def exact_unlabeled_sprinkling_law(n):
    counts = Counter()
    for perm in permutations(range(n)):
        counts[canonical_unlabeled_code(poset_from_permutation(perm))] += 1
    total = mp.mpf(sum(counts.values()))
    return {code: mp.mpf(count) / total for code, count in counts.items()}


def perfect_matchings(labels):
    labels = tuple(labels)
    if not labels:
        yield tuple()
        return
    first = labels[0]
    rest = labels[1:]
    for index, second in enumerate(rest):
        pair = frozenset((first, second))
        remaining = rest[:index] + rest[index + 1 :]
        for tail in perfect_matchings(remaining):
            yield tuple(sorted((pair,) + tail, key=lambda e: tuple(e)))


def overlap_graph_signature(matching_a, matching_b, n):
    set_a = set(matching_a)
    set_b = set(matching_b)
    adj = [[] for _ in range(n)]
    for edge in set_a | set_b:
        x, y = tuple(edge)
        adj[x].append(y)
        adj[y].append(x)
    seen = [False] * n
    parts = []
    for start in range(n):
        if seen[start]:
            continue
        stack = [start]
        seen[start] = True
        vertices = []
        while stack:
            x = stack.pop()
            vertices.append(x)
            for y in adj[x]:
                if not seen[y]:
                    seen[y] = True
                    stack.append(y)
        vertex_set = set(vertices)
        h_edges = sum(1 for edge in set_a if edge <= vertex_set)
        parts.append(h_edges)
    return tuple(sorted(parts))


def sample_conditional_unlabeled_counts(n, matching, sample_count, seed_base, jitter_num, jitter_den):
    rng = random.Random(seed_base)
    blocks = [tuple(sorted(edge)) for edge in matching]
    width = 2
    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    counts = Counter()
    tie = n + 1
    for _ in range(sample_count):
        u_block_order = list(range(len(blocks)))
        v_block_order = list(range(len(blocks)))
        rng.shuffle(u_block_order)
        rng.shuffle(v_block_order)
        u_rank = [0] * len(blocks)
        v_rank = [0] * len(blocks)
        for rank, block_index in enumerate(u_block_order):
            u_rank[block_index] = rank
        for rank, block_index in enumerate(v_block_order):
            v_rank[block_index] = rank

        points = [None] * n
        for block_index, block in enumerate(blocks):
            local_order = list(block)
            rng.shuffle(local_order)
            for local, label in enumerate(local_order):
                du = rng.randint(-span, span) if span else 0
                dv = rng.randint(-span, span) if span else 0
                u = (u_rank[block_index] * scale + width * du + local) * tie + label
                v = (v_rank[block_index] * scale + width * dv + (width - 1 - local)) * tie + label
                points[label] = (u, v)
        counts[canonical_unlabeled_code(coordinate_order_poset(points))] += 1
    return counts


def weights_from_counts(counts):
    total = mp.mpf(sum(counts.values()))
    return {code: mp.mpf(count) / total for code, count in counts.items()}


def cross_factor(weights_a, weights_b, p_inv):
    if len(weights_a) > len(weights_b):
        weights_a, weights_b = weights_b, weights_a
    value = mp.mpf(0)
    for code, qa in weights_a.items():
        qb = weights_b.get(code)
        if qb is not None:
            value += qa * qb * p_inv[code]
    return value


def log_linear_fit(signature_means):
    signatures = sorted(signature_means)
    rows = []
    y = []
    for signature in signatures:
        rows.append([mp.mpf(signature.count(part)) for part in [1, 2, 3, 4]])
        y.append(mp.log(signature_means[signature]))
    x_mat = mp.matrix(rows)
    y_vec = mp.matrix(y)
    normal = x_mat.T * x_mat
    rhs = x_mat.T * y_vec
    coeff = mp.lu_solve(normal, rhs)
    predictions = {}
    residuals = {}
    for signature, row, target in zip(signatures, rows, y):
        pred_log = mp.fsum(row[i] * coeff[i] for i in range(4))
        pred = mp.e ** pred_log
        predictions[signature] = pred
        residuals[signature] = pred / signature_means[signature]
    return coeff, predictions, residuals


print("=" * 80)
print("Collapsed P23 overlap-component factorization audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 8
sample_count = 1024
matchings = list(perfect_matchings(range(n)))
p_law = exact_unlabeled_sprinkling_law(n)
p_inv = {code: 1 / p for code, p in p_law.items()}
print(f"N={n} exact_P_support={len(p_law)} matchings={len(matchings)} sample_count_per_H={sample_count}")

schedules = [
    ("linear_half", n // 2, 2),
    ("linear_one", n, 2),
    ("linear_two", 2 * n, 2),
]

all_support_ok = True
all_factorization_rejected = True
all_nonidentity_near_one = True
all_identity_rare = True

for schedule_index, (schedule_name, jitter_num, jitter_den) in enumerate(schedules):
    print(f"\nSchedule {schedule_name}: jitter={jitter_num}/{jitter_den}")
    q_weights = {}
    for h_index, matching in enumerate(matchings):
        counts = sample_conditional_unlabeled_counts(
            n,
            matching,
            sample_count,
            5700000 + schedule_index * 500000 + h_index * 1009,
            jitter_num,
            jitter_den,
        )
        all_support_ok = all_support_ok and all(code in p_law for code in counts)
        q_weights[matching] = weights_from_counts(counts)

    groups = defaultdict(list)
    for ha in matchings:
        for hb in matchings:
            signature = overlap_graph_signature(ha, hb, n)
            groups[signature].append(cross_factor(q_weights[ha], q_weights[hb], p_inv))

    signature_means = {signature: mp.fsum(values) / len(values) for signature, values in groups.items()}
    for signature in sorted(signature_means):
        print(f"  mean {signature}: {fmt(signature_means[signature], 18)}")

    beta1_from_identity = signature_means[(1, 1, 1, 1)] ** mp.mpf("0.25")
    beta2_from_zero = mp.sqrt(signature_means[(2, 2)])
    beta4 = signature_means[(4,)]
    beta3_from_mixed = signature_means[(1, 3)] / beta1_from_identity
    predicted_112 = beta1_from_identity ** 2 * beta2_from_zero
    ratio_112 = predicted_112 / signature_means[(1, 1, 2)]
    print(
        "  edge-calibrated betas: "
        f"beta1={fmt(beta1_from_identity, 18)} beta2={fmt(beta2_from_zero, 18)} "
        f"beta3={fmt(beta3_from_mixed, 18)} beta4={fmt(beta4, 18)}"
    )
    print(
        f"  predicted mean(1,1,2)={fmt(predicted_112, 18)} "
        f"observed={fmt(signature_means[(1, 1, 2)], 18)} ratio={fmt(ratio_112, 18)}"
    )

    coeff, predictions, residuals = log_linear_fit(signature_means)
    max_residual = max(max(value, 1 / value) for value in residuals.values())
    print(f"  least-squares component residual max-factor={fmt(max_residual, 18)}")
    for signature in sorted(residuals):
        print(
            f"    fit {signature}: observed={fmt(signature_means[signature], 12)} "
            f"pred={fmt(predictions[signature], 12)} pred/obs={fmt(residuals[signature], 12)}"
        )

    nonidentity_max_mean = max(
        value for signature, value in signature_means.items() if signature != (1, 1, 1, 1)
    )
    identity_contribution = signature_means[(1, 1, 1, 1)] / len(matchings)
    print(
        f"  nonidentity_max_mean={fmt(nonidentity_max_mean, 18)} "
        f"identity_mean/matchings={fmt(identity_contribution, 18)}"
    )

    all_factorization_rejected = all_factorization_rejected and ratio_112 > mp.mpf("3")
    all_nonidentity_near_one = all_nonidentity_near_one and nonidentity_max_mean < mp.mpf("1.02")
    all_identity_rare = all_identity_rare and identity_contribution < mp.mpf("0.2")

check("Exact P_8 support and all matchings are used", len(p_law) == 14794 and len(matchings) == 105, "")
check("Conditional samples remain inside exact P_8 support", all_support_ok, "")
check("Naive multiplicative component factorization is rejected", all_factorization_rejected, "edge-calibrated (1,1,2) ratio > 3")
check("All non-identical overlap signatures stay near the null mean", all_nonidentity_near_one, "nonidentity max mean < 1.02")
check("The full-identity spike is rare after averaging over hidden matchings", all_identity_rare, "same-H mean / #matchings < 0.2")

print("\n=== Consequence ===")
print("The transfer-operator toy theorem is not yet the actual unlabeled")
print("likelihood theorem.  At exact P_8, naive component factorization fails:")
print("common hidden edges do not multiply locally unless the whole hidden")
print("matching is identical.  The better target is now a conditional")
print("factorization theorem or a direct proof that all non-identical hidden")
print("overlap signatures are asymptotically null.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
