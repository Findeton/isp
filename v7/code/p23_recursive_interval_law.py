#!/usr/bin/env python3
"""
Receipt for v7 Paper XXIII: recursive interval laws and no hidden staging.

The receipt investigates the opening left by Paper XXII.  A finite list of
Laplace samples of the interval-size histogram is underdetermined, and even the
full interval-size histogram is only a first-order shadow of the order.  The
next candidate law is hereditary: intervals of size k should themselves look,
in order statistics, like k-record sprinklings.  The receipt tests a pooled
first recursive statistic and then attacks it with an adversary that reuses one
first-order-good inner block as the interior of many different outer intervals.

All asserted non-integer arithmetic uses mpmath with dps=140.  Poset statistics
are integer bitset counts; no float64 arithmetic is used for asserted values.
"""

import itertools
import random

import mpmath as mp

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


def linreg_slope(xs, ys):
    xs = [mp.mpf(x) for x in xs]
    ys = [mp.mpf(y) for y in ys]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    return num / den


def mm_f(d):
    d = mp.mpf(d)
    return mp.gamma(d + 1) * mp.gamma(d / 2) / (2 * mp.gamma(3 * d / 2))


def mm_inv(r):
    r = mp.mpf(r)
    if r <= 0:
        return mp.inf
    if r >= 1:
        return mp.mpf(1)
    lo = mp.mpf(1)
    hi = mp.mpf(64)
    for _ in range(600):
        mid = (lo + hi) / 2
        if mm_f(mid) > r:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


class Poset:
    def __init__(self, future):
        self.future = list(future)
        self.N = len(self.future)
        self.past = [0] * self.N
        for x, mask in enumerate(self.future):
            for y in iter_bits(mask):
                self.past[y] |= 1 << x

    def relation_count(self):
        return sum(mask.bit_count() for mask in self.future)

    def ordering_fraction(self):
        total = self.N * (self.N - 1) // 2
        return mp.mpf(self.relation_count()) / total

    def height(self):
        memo = [0] * self.N
        visiting = [False] * self.N

        def depth(x):
            if memo[x]:
                return memo[x]
            if visiting[x]:
                raise ValueError("cycle detected in future relation")
            visiting[x] = True
            best = 1
            for y in iter_bits(self.future[x]):
                best = max(best, 1 + depth(y))
            visiting[x] = False
            memo[x] = best
            return best

        return max(depth(x) for x in range(self.N))

    def interval_audit(self, load_k_min=8, keep_band_masks=False):
        hist = [0] * self.N
        recursive_num = 0
        recursive_den = 0
        recursive_intervals = 0
        band_intervals = 0
        band_interior_mass = 0
        loads = [0] * self.N
        duplicate = {}
        band_masks = [] if keep_band_masks else None

        for x in range(self.N):
            for y in iter_bits(self.future[x]):
                interior = self.future[x] & self.past[y]
                k = interior.bit_count()
                hist[k] += 1
                if k >= 2:
                    den = k * (k - 1) // 2
                    inner_rel = 0
                    for z in iter_bits(interior):
                        inner_rel += (self.future[z] & interior).bit_count()
                    recursive_num += inner_rel
                    recursive_den += den
                    recursive_intervals += 1
                if k >= load_k_min:
                    band_intervals += 1
                    band_interior_mass += k
                    duplicate[interior] = duplicate.get(interior, 0) + 1
                    if keep_band_masks:
                        band_masks.append(interior)
                    for z in iter_bits(interior):
                        loads[z] += 1

        if recursive_den:
            recursive_r = mp.mpf(recursive_num) / recursive_den
        else:
            recursive_r = mp.nan
        load_l2 = sum(v * v for v in loads)
        if band_interior_mass and load_l2:
            effective_support = mp.mpf(band_interior_mass) ** 2 / load_l2
            max_load_ratio = mp.mpf(max(loads)) / (mp.mpf(band_interior_mass) / self.N)
        else:
            effective_support = mp.mpf(0)
            max_load_ratio = mp.nan
        max_duplicate = max(duplicate.values()) if duplicate else 0
        return {
            "hist": hist,
            "recursive_num": recursive_num,
            "recursive_den": recursive_den,
            "recursive_intervals": recursive_intervals,
            "recursive_r": recursive_r,
            "band_intervals": band_intervals,
            "band_interior_mass": band_interior_mass,
            "effective_support": effective_support,
            "effective_support_ratio": effective_support / self.N,
            "max_load": max(loads) if loads else 0,
            "max_load_ratio": max_load_ratio,
            "max_duplicate": max_duplicate,
            "max_duplicate_fraction": (
                mp.mpf(max_duplicate) / band_intervals if band_intervals else mp.mpf(0)
            ),
            "band_masks": band_masks,
        }


def sprinkled2_poset(N, seed):
    N = int(N)
    rng = random.Random(seed)
    perm = list(range(N))
    rng.shuffle(perm)
    future = [0] * N
    for i in range(N):
        vi = perm[i]
        mask = 0
        for j in range(i + 1, N):
            if vi < perm[j]:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


def coordinate_order_poset(points):
    """Build the 1+1 product order from exact integer coordinates."""
    future = [0] * len(points)
    for i, (ui, vi) in enumerate(points):
        mask = 0
        for j, (uj, vj) in enumerate(points):
            if ui < uj and vi < vj:
                mask |= 1 << j
        future[i] = mask
    return Poset(future)


def clustered_jittered_fiber_poset(base_N, width, seed, jitter_num, jitter_den):
    """A hidden-fiber attack that borrows actual coordinate jitter.

    Each base sprinkling point is replaced by a small cluster of records.  The
    cluster is not lifted as a complete quotient fiber; instead each clone gets
    a small integer displacement in both light-cone coordinates, and the final
    order is the exact product order of the displaced points.

    When the jitter is small this behaves like a hidden fiber and should leave a
    soft near-twin tail.  When the jitter is large enough to erase that tail, the
    construction is no longer a clean non-manifold quotient: it has become a
    clustered/inhomogeneous 1+1 point process.
    """
    base_N = int(base_N)
    width = int(width)
    jitter_num = int(jitter_num)
    jitter_den = int(jitter_den)
    if jitter_den <= 0:
        raise ValueError("jitter_den must be positive")
    rng = random.Random(seed)
    perm = list(range(base_N))
    rng.shuffle(perm)

    scale = 10000 * jitter_den
    span = 10000 * jitter_num
    points = []
    cluster_labels = []
    for i, vi in enumerate(perm):
        for local in range(width):
            if span:
                du = rng.randint(-span, span)
                dv = rng.randint(-span, span)
            else:
                du = 0
                dv = 0
            # The local tie-breaker is tiny compared with one base spacing.  It
            # makes equal-jitter coincidences deterministic without using floats.
            u = i * scale + width * du + local
            v = vi * scale + width * dv + (width - 1 - local)
            points.append((u, v))
            cluster_labels.append(i)

    poset = coordinate_order_poset(points)
    return poset, {
        "base_N": base_N,
        "width": width,
        "seed": seed,
        "jitter": f"{jitter_num}/{jitter_den}",
        "span_over_spacing": mp.mpf(jitter_num) / jitter_den,
        "cluster_labels": cluster_labels,
        "points": points,
    }


def chain_poset(N):
    N = int(N)
    return Poset([sum(1 << j for j in range(i + 1, N)) for i in range(N)])


def bit_range(start, stop):
    mask = 0
    for i in range(start, stop):
        mask |= 1 << i
    return mask


def thin_middle_chain_poset(n, middle):
    n = int(n)
    middle = int(middle)
    h = n
    N = n * n
    remainder = N - h - middle
    a = remainder // 2
    b = remainder - a
    m0 = a
    b0 = a + middle
    c0 = a + middle + b
    future = [0] * N
    middle_mask = sum(1 << i for i in range(m0, b0))
    top_mask = sum(1 << i for i in range(b0, c0))
    for x in range(0, a):
        future[x] = middle_mask | top_mask
    for x in range(m0, b0):
        future[x] = top_mask
    for x in range(c0, N):
        future[x] = sum(1 << j for j in range(x + 1, N))
    return Poset(future)


def shifted_sprinkled_future(m, seed, offset):
    inner = sprinkled2_poset(m, seed)
    shifted = []
    for mask in inner.future:
        out = 0
        for y in iter_bits(mask):
            out |= 1 << (offset + y)
        shifted.append(out)
    return shifted, inner


def wrapped_sprinkling_sandwich_poset(N, middle, seed, chain_height=None):
    """A staged adversary with one reused sprinkling-like middle interval.

    Bottom A is below every middle and top element; every middle element is below
    every top element; the middle block carries a 1+1 sprinkling order internally.
    An isolated chain supplies the expected height scale.
    """
    N = int(N)
    middle = int(middle)
    if chain_height is None:
        chain_height = int(mp.floor(mp.sqrt(N)))
    h = int(chain_height)
    side = N - h - middle
    a = side // 2
    b = side - a
    p0 = a
    top0 = a + middle
    chain0 = a + middle + b
    future = [0] * N
    middle_mask = sum(1 << i for i in range(p0, top0))
    top_mask = sum(1 << i for i in range(top0, chain0))
    for x in range(0, a):
        future[x] = middle_mask | top_mask
    shifted_inner, inner = shifted_sprinkled_future(middle, seed, p0)
    for local, mask in enumerate(shifted_inner):
        future[p0 + local] = mask | top_mask
    for x in range(chain0, N):
        future[x] = sum(1 << j for j in range(x + 1, N))
    return Poset(future), inner, {"A": a, "middle": middle, "B": b, "chain": h}


def fiber_blowup_poset(base_N, fiber, seed, fiber_order="antichain"):
    """Replace each sprinkling point by a hidden fiber.

    If base point i precedes base point j, every point in fiber i precedes
    every point in fiber j.  Internally each fiber is either an antichain or a
    chain.  This is a simple hidden-thickness adversary: the quotient order can
    look sprinkling-like while the record order has extra unresolved fibers.
    """
    base_N = int(base_N)
    fiber = int(fiber)
    if fiber_order not in {"antichain", "chain"}:
        raise ValueError("fiber_order must be 'antichain' or 'chain'")

    base = sprinkled2_poset(base_N, seed)
    N = base_N * fiber
    future = [0] * N
    fiber_masks = [bit_range(i * fiber, (i + 1) * fiber) for i in range(base_N)]

    for i in range(base_N):
        inherited = 0
        for j in iter_bits(base.future[i]):
            inherited |= fiber_masks[j]
        start = i * fiber
        for local in range(fiber):
            x = start + local
            future[x] |= inherited
            if fiber_order == "chain":
                future[x] |= bit_range(x + 1, start + fiber)

    return Poset(future), base


def deterministic_fraction_hit(index, seed, numerator, denominator):
    """A small integer-only pseudo-random selector."""
    value = (1103515245 * (index + 1) + 12345 * (seed + 1)) & 0x7FFFFFFF
    return value % denominator < numerator


def mixed_fiber_blowup_poset(base_N, fiber, seed, numerator, denominator):
    """A height-tuned fiber blow-up with mixed chain and antichain fibers."""
    base_N = int(base_N)
    fiber = int(fiber)
    numerator = int(numerator)
    denominator = int(denominator)
    base = sprinkled2_poset(base_N, seed)
    N = base_N * fiber
    future = [0] * N
    fiber_masks = [bit_range(i * fiber, (i + 1) * fiber) for i in range(base_N)]
    chain_fibers = []

    for i in range(base_N):
        inherited = 0
        for j in iter_bits(base.future[i]):
            inherited |= fiber_masks[j]
        start = i * fiber
        is_chain = deterministic_fraction_hit(i, seed, numerator, denominator)
        if is_chain:
            chain_fibers.append(i)
        for local in range(fiber):
            x = start + local
            future[x] |= inherited
            if is_chain:
                future[x] |= bit_range(x + 1, start + fiber)

    return Poset(future), base, {
        "base_N": base_N,
        "fiber": fiber,
        "chain_fibers": len(chain_fibers),
        "chain_fraction": mp.mpf(len(chain_fibers)) / base_N,
        "selector": f"{numerator}/{denominator}",
    }


def decorated_mixed_fiber_poset(base_N, seed, numerator, denominator):
    """Break exact fiber twins with one local tag per quotient point.

    Each base record becomes three records (a,b,t).  Base comparabilities lift
    to complete relations between triples.  Internally, selected triples carry
    a<t<b; unselected triples carry one short tag relation, alternating a<t and
    b<t deterministically.  This is the next adversary after exact twin tests:
    it destroys exact twins while keeping near-identical causal roles.
    """
    base_N = int(base_N)
    numerator = int(numerator)
    denominator = int(denominator)
    base = sprinkled2_poset(base_N, seed)
    width = 3
    N = base_N * width
    future = [0] * N
    fiber_masks = [bit_range(i * width, (i + 1) * width) for i in range(base_N)]
    chain_fibers = []

    for i in range(base_N):
        inherited = 0
        for j in iter_bits(base.future[i]):
            inherited |= fiber_masks[j]
        a = i * width
        b = a + 1
        tag = a + 2
        is_chain = deterministic_fraction_hit(i, seed, numerator, denominator)
        if is_chain:
            chain_fibers.append(i)
            future[a] |= (1 << tag) | (1 << b)
            future[tag] |= 1 << b
        elif deterministic_fraction_hit(i, seed + 17, 1, 2):
            future[a] |= 1 << tag
        else:
            future[b] |= 1 << tag
        future[a] |= inherited
        future[b] |= inherited
        future[tag] |= inherited

    return Poset(future), base, {
        "base_N": base_N,
        "width": width,
        "chain_fibers": len(chain_fibers),
        "chain_fraction": mp.mpf(len(chain_fibers)) / base_N,
        "selector": f"{numerator}/{denominator}",
    }


def double_decorated_mixed_fiber_poset(base_N, seed, numerator, denominator):
    """Use two local tags per quotient point to break exact twin roles harder."""
    base_N = int(base_N)
    numerator = int(numerator)
    denominator = int(denominator)
    base = sprinkled2_poset(base_N, seed)
    width = 4
    N = base_N * width
    future = [0] * N
    fiber_masks = [bit_range(i * width, (i + 1) * width) for i in range(base_N)]
    chain_fibers = []

    for i in range(base_N):
        inherited = 0
        for j in iter_bits(base.future[i]):
            inherited |= fiber_masks[j]
        a = i * width
        b = a + 1
        tag_a = a + 2
        tag_b = a + 3
        is_chain = deterministic_fraction_hit(i, seed, numerator, denominator)
        if is_chain:
            chain_fibers.append(i)
            future[a] |= (1 << tag_a) | (1 << tag_b) | (1 << b)
            future[tag_a] |= (1 << tag_b) | (1 << b)
            future[tag_b] |= 1 << b
        else:
            future[a] |= 1 << tag_a
            future[b] |= 1 << tag_b
        future[a] |= inherited
        future[b] |= inherited
        future[tag_a] |= inherited
        future[tag_b] |= inherited

    return Poset(future), base, {
        "base_N": base_N,
        "width": width,
        "chain_fibers": len(chain_fibers),
        "chain_fraction": mp.mpf(len(chain_fibers)) / base_N,
        "selector": f"{numerator}/{denominator}",
    }


def twin_free_decorated_fiber_poset(base_N, seed, numerator, denominator):
    """Use small twin-free local motifs to break exact external twins.

    The unselected motif has relations 0<2, 1<2, 1<3.  The selected motif has
    relations 0<1<3 and 0<2.  Both four-record motifs have no internal external
    twin pair: after removing any two tested records, their remaining local
    causal neighborhoods still differ.
    """
    base_N = int(base_N)
    numerator = int(numerator)
    denominator = int(denominator)
    base = sprinkled2_poset(base_N, seed)
    width = 4
    N = base_N * width
    future = [0] * N
    fiber_masks = [bit_range(i * width, (i + 1) * width) for i in range(base_N)]
    tall_fibers = []

    for i in range(base_N):
        inherited = 0
        for j in iter_bits(base.future[i]):
            inherited |= fiber_masks[j]
        x0 = i * width
        x1 = x0 + 1
        x2 = x0 + 2
        x3 = x0 + 3
        is_tall = deterministic_fraction_hit(i, seed, numerator, denominator)
        if is_tall:
            tall_fibers.append(i)
            future[x0] |= (1 << x1) | (1 << x2) | (1 << x3)
            future[x1] |= 1 << x3
        else:
            future[x0] |= 1 << x2
            future[x1] |= (1 << x2) | (1 << x3)
        for x in [x0, x1, x2, x3]:
            future[x] |= inherited

    return Poset(future), base, {
        "seed": seed,
        "base_N": base_N,
        "width": width,
        "tall_fibers": len(tall_fibers),
        "tall_fraction": mp.mpf(len(tall_fibers)) / base_N,
        "selector": f"{numerator}/{denominator}",
    }


def random_local_future(width, seed, numerator, denominator):
    future = [0] * width
    for i in range(width):
        for j in range(i + 1, width):
            key = i * width + j
            if deterministic_fraction_hit(key, seed, numerator, denominator):
                future[i] |= 1 << j
    for i in range(width - 1, -1, -1):
        closure = future[i]
        for j in iter_bits(future[i]):
            closure |= future[j]
        future[i] = closure
    return future


def random_motif_fiber_poset(base_N, width, base_seed, motif_seed, numerator, denominator):
    """Use varied random local motifs to attack the soft near-twin tail."""
    base_N = int(base_N)
    width = int(width)
    base = sprinkled2_poset(base_N, base_seed)
    N = base_N * width
    future = [0] * N
    fiber_masks = [bit_range(i * width, (i + 1) * width) for i in range(base_N)]
    local_heights = []

    for i in range(base_N):
        inherited = 0
        for j in iter_bits(base.future[i]):
            inherited |= fiber_masks[j]
        local = random_local_future(width, motif_seed + i, numerator, denominator)
        local_poset = Poset(local)
        local_heights.append(local_poset.height())
        offset = i * width
        for x in range(width):
            shifted = 0
            for y in iter_bits(local[x]):
                shifted |= 1 << (offset + y)
            future[offset + x] = shifted | inherited

    return Poset(future), base, {
        "base_N": base_N,
        "width": width,
        "base_seed": base_seed,
        "motif_seed": motif_seed,
        "selector": f"{numerator}/{denominator}",
        "min_local_height": min(local_heights),
        "max_local_height": max(local_heights),
        "mean_local_height": mp.mpf(sum(local_heights)) / len(local_heights),
    }


def multi_staged_reservoir_poset(N, module_count, middle, seed0, chain_height):
    """Many independent staged reservoirs plus one height-supplying chain.

    This tries to lower exact duplicate interiors by distributing the hidden
    staging across several reservoirs.  The price is global: absent cross-links,
    it loses the 1+1 related-pair fraction and MM dimension.
    """
    N = int(N)
    module_count = int(module_count)
    middle = int(middle)
    chain_height = int(chain_height)
    if module_count <= 0:
        raise ValueError("module_count must be positive")

    module_total = N - chain_height
    if module_total <= module_count * (middle + 2):
        raise ValueError("not enough records for requested modules")

    base_size = module_total // module_count
    extra = module_total % module_count
    sizes = [base_size + (1 if i < extra else 0) for i in range(module_count)]

    future = [0] * N
    parts = []
    offset = 0
    for module_index, size in enumerate(sizes):
        mid = min(middle, size - 2)
        rem = size - mid
        a = rem // 2
        b = rem - a
        p0 = offset + a
        top0 = p0 + mid
        end = offset + size
        middle_mask = bit_range(p0, top0)
        top_mask = bit_range(top0, end)

        for x in range(offset, p0):
            future[x] = middle_mask | top_mask

        shifted_inner, _ = shifted_sprinkled_future(mid, seed0 + module_index, p0)
        for local, mask in enumerate(shifted_inner):
            future[p0 + local] = mask | top_mask

        parts.append({"A": a, "middle": mid, "B": b, "offset": offset})
        offset = end

    for x in range(offset, N):
        future[x] = bit_range(x + 1, N)

    return Poset(future), {"modules": parts, "chain": chain_height}


def cross_linked_staged_reservoir_poset(N, module_count, middle, base_seed, seed0):
    """Staged reservoirs whose modules are cross-linked by a sprinkling quotient.

    Each module is an A<P<B sandwich.  The modules themselves are ordered by a
    1+1 sprinkling quotient; if quotient module i precedes j, every record in
    module i precedes every record in module j.  This is the direct attempt to
    repair the independent-reservoir MM failure without abandoning staging.
    """
    N = int(N)
    module_count = int(module_count)
    middle = int(middle)
    if module_count <= 0:
        raise ValueError("module_count must be positive")
    if N <= module_count * (middle + 2):
        raise ValueError("not enough records for requested modules")

    base_size = N // module_count
    extra = N % module_count
    sizes = [base_size + (1 if i < extra else 0) for i in range(module_count)]
    base = sprinkled2_poset(module_count, base_seed)

    future = [0] * N
    parts = []
    module_masks = []
    offset = 0
    for module_index, size in enumerate(sizes):
        mid = min(middle, size - 2)
        rem = size - mid
        a = rem // 2
        b = rem - a
        p0 = offset + a
        top0 = p0 + mid
        end = offset + size
        middle_mask = bit_range(p0, top0)
        top_mask = bit_range(top0, end)
        module_masks.append(bit_range(offset, end))

        for x in range(offset, p0):
            future[x] = middle_mask | top_mask

        shifted_inner, _ = shifted_sprinkled_future(mid, seed0 + module_index, p0)
        for local, mask in enumerate(shifted_inner):
            future[p0 + local] = mask | top_mask

        parts.append({"A": a, "middle": mid, "B": b, "offset": offset, "size": size})
        offset = end

    for i in range(module_count):
        cross_mask = 0
        for j in iter_bits(base.future[i]):
            cross_mask |= module_masks[j]
        start = parts[i]["offset"]
        end = start + parts[i]["size"]
        for x in range(start, end):
            future[x] |= cross_mask

    return Poset(future), base, {"modules": parts, "base_seed": base_seed}


def expected_hist_density_2d(N, k):
    """E[H_k/N] for a fixed-N 1+1 binomial sprinkling in an Alexandrov interval."""
    N = int(N)
    k = int(k)
    if k < 0 or k > N - 2:
        return mp.mpf(0)
    guard_dps = max(mp.mp.dps + 60, int(mp.ceil(mp.mpf("0.4") * N)) + 100)
    with mp.workdps(guard_dps):
        remaining = N - 2 - k
        s = mp.mpf(0)
        term = mp.mpf(1)
        for j in range(remaining + 1):
            if j > 0:
                term *= mp.mpf(remaining - j + 1) / j * (-1)
            denom = mp.mpf(k + j + 1) ** 2 * mp.mpf(k + j + 2) ** 2
            s += term / denom
        return +(mp.mpf(N - 1) * mp.binomial(N - 2, k) * s)


def sprinkle_pair_density_expectation(N, alpha):
    N = int(N)
    guard_dps = max(mp.mp.dps + 40, int(mp.ceil(mp.mpf("0.25") * N)) + 80)
    with mp.workdps(guard_dps):
        q = mp.e ** (-mp.mpf(alpha))
        c = 1 - q
        m = N - 2
        s = mp.mpf(0)
        term = mp.mpf(1)
        for k in range(0, m + 1):
            if k > 0:
                term *= mp.mpf(m - k + 1) / mp.mpf(k) * (-c)
            denom = mp.mpf(k + 1) ** 2 * mp.mpf(k + 2) ** 2
            s += term / denom
        return +(mp.mpf(N - 1) * s)


def hist_density_from_poset(poset):
    audit = poset.interval_audit(load_k_min=8)
    return [mp.mpf(v) / poset.N for v in audit["hist"]]


def bin_histogram(densities, bins):
    rows = []
    for label, lo, hi in bins:
        if hi is None:
            val = sum(densities[lo:])
        else:
            val = sum(densities[lo : hi + 1])
        rows.append((label, val))
    return rows


def profile_P_from_hist_density(densities, alpha):
    q = mp.e ** (-mp.mpf(alpha))
    total = mp.mpf(0)
    power = mp.mpf(1)
    for density in densities:
        total += density * power
        power *= q
    return total


def continuum_2d_load_effective_support_no_threshold():
    """Mean-field S_eff/N for all interval interiors in a 1+1 unit diamond.

    For a point (u,v), the no-threshold expected load profile is proportional to
    f(u,v)=u v (1-u)(1-v).  The continuum participation ratio is

      (int f)^2 / int f^2 = (1/36)^2 / (1/30)^2 = 25/36.

    This is region-shape dependent; it is a calibration point, not a universal
    no-hidden-staging constant.
    """
    integral_f = mp.mpf(1) / 36
    integral_f2 = mp.mpf(1) / 900
    return integral_f**2 / integral_f2


def sampled_jaccard_stats(masks, sample_limit=512):
    """Deterministic sampled Jaccard-overlap statistics for interval interiors."""
    if not masks:
        return {
            "sample": 0,
            "pairs": 0,
            "mean": mp.nan,
            "p95": mp.nan,
            "max": mp.nan,
        }
    if len(masks) <= sample_limit:
        sample = list(masks)
    else:
        sample = []
        last = len(masks) - 1
        denom = sample_limit - 1
        for i in range(sample_limit):
            sample.append(masks[(i * last) // denom])
    vals = []
    for i, a in enumerate(sample):
        for b in sample[i + 1 :]:
            union = (a | b).bit_count()
            if union:
                vals.append(mp.mpf((a & b).bit_count()) / union)
    vals.sort()
    if not vals:
        return {
            "sample": len(sample),
            "pairs": 0,
            "mean": mp.nan,
            "p95": mp.nan,
            "max": mp.nan,
        }
    p95_index = min(len(vals) - 1, int(mp.floor(mp.mpf("0.95") * (len(vals) - 1))))
    return {
        "sample": len(sample),
        "pairs": len(vals),
        "mean": sum(vals) / len(vals),
        "p95": vals[p95_index],
        "max": vals[-1],
    }


def quantile_from_sorted(values, q_num, q_den):
    if not values:
        return 0
    index = (q_num * (len(values) - 1)) // q_den
    return values[index]


def small_interval_endpoint_stats(poset, k_max):
    """Order-only density proxy from endpoint loads of small intervals.

    For each comparable pair with interval cardinality at most k_max, add one
    unit of load to both endpoints.  A finite-density sprinkling should spread
    these small causal neighborhoods in a calibrated way.  Clustered point
    processes can match scalar interval counts while making these loads too
    uneven.
    """
    k_max = int(k_max)
    relation_count, loads = small_interval_endpoint_loads(poset, k_max)
    total_load = 2 * relation_count
    load_l2 = sum(v * v for v in loads)
    sorted_loads = sorted(loads)
    mean = mp.mpf(total_load) / poset.N if poset.N else mp.nan
    if total_load and load_l2:
        eff = mp.mpf(total_load) ** 2 / load_l2
        max_ratio = mp.mpf(sorted_loads[-1]) / mean
        p95_ratio = mp.mpf(quantile_from_sorted(sorted_loads, 95, 100)) / mean
        p99_ratio = mp.mpf(quantile_from_sorted(sorted_loads, 99, 100)) / mean
    else:
        eff = mp.mpf(0)
        max_ratio = mp.nan
        p95_ratio = mp.nan
        p99_ratio = mp.nan
    return {
        "k_max": k_max,
        "relations": relation_count,
        "density": mp.mpf(relation_count) / poset.N,
        "mean": mean,
        "effective_support_ratio": eff / poset.N,
        "p95_load": quantile_from_sorted(sorted_loads, 95, 100),
        "p99_load": quantile_from_sorted(sorted_loads, 99, 100),
        "max_load": sorted_loads[-1] if sorted_loads else 0,
        "p95_ratio": p95_ratio,
        "p99_ratio": p99_ratio,
        "max_ratio": max_ratio,
    }


def small_interval_endpoint_loads(poset, k_max):
    k_max = int(k_max)
    loads = [0] * poset.N
    relation_count = 0
    for x in range(poset.N):
        for y in iter_bits(poset.future[x]):
            k = (poset.future[x] & poset.past[y]).bit_count()
            if k <= k_max:
                relation_count += 1
                loads[x] += 1
                loads[y] += 1
    return relation_count, loads


def endpoint_profile_distance(profile_a, profile_b):
    """Small log-distance between two endpoint-load profiles."""
    total = mp.mpf(0)
    for key in ["density", "effective_support_ratio", "p95_ratio", "max_ratio"]:
        a = profile_a[key]
        b = profile_b[key]
        if a > 0 and b > 0:
            total += abs(mp.log(a / b))
    return total


def quantile_bins(values, bins):
    bins = int(bins)
    out = [0] * len(values)
    ranked = sorted(range(len(values)), key=lambda i: (values[i], i))
    for rank, index in enumerate(ranked):
        out[index] = min(bins - 1, (rank * bins) // len(values))
    return out


def conditional_endpoint_residual_stats(poset, k_max, bins=4):
    """Small-interval endpoint-load unevenness after boundary conditioning.

    Boundary records naturally have different link/small-interval loads.  This
    bins records by past-size and future-size quantiles, then measures how
    uneven the small-interval endpoint load remains inside those order-only
    bins.  It is a multiscale density-regularity shadow without coordinates.
    """
    _, loads = small_interval_endpoint_loads(poset, k_max)
    past_sizes = [mask.bit_count() for mask in poset.past]
    future_sizes = [mask.bit_count() for mask in poset.future]
    past_bins = quantile_bins(past_sizes, bins)
    future_bins = quantile_bins(future_sizes, bins)
    groups = {}
    for index, load in enumerate(loads):
        key = (past_bins[index], future_bins[index])
        groups.setdefault(key, []).append(load)

    normalized = []
    group_eff_sum = mp.mpf(0)
    residual_num = mp.mpf(0)
    residual_den = mp.mpf(0)
    active_groups = 0
    for group_loads in groups.values():
        total = sum(group_loads)
        if not total:
            continue
        active_groups += 1
        n = len(group_loads)
        mean = mp.mpf(total) / n
        group_l2 = sum(v * v for v in group_loads)
        group_eff_sum += mp.mpf(total) ** 2 / group_l2
        for value in group_loads:
            ratio = mp.mpf(value) / mean
            normalized.append(ratio)
            residual_num += (mp.mpf(value) - mean) ** 2
            residual_den += mean**2

    normalized.sort()
    if not normalized:
        return {
            "k_max": k_max,
            "bins": bins,
            "active_groups": 0,
            "group_effective_support_ratio": mp.mpf(0),
            "residual_rms_ratio": mp.nan,
            "p95_ratio": mp.nan,
            "p99_ratio": mp.nan,
            "max_ratio": mp.nan,
        }
    return {
        "k_max": k_max,
        "bins": bins,
        "active_groups": active_groups,
        "group_effective_support_ratio": group_eff_sum / poset.N,
        "residual_rms_ratio": mp.sqrt(residual_num / residual_den)
        if residual_den
        else mp.nan,
        "p95_ratio": quantile_from_sorted(normalized, 95, 100),
        "p99_ratio": quantile_from_sorted(normalized, 99, 100),
        "max_ratio": normalized[-1],
    }


def conditional_profile_distance(profile_a, profile_b):
    total = mp.mpf(0)
    for key in [
        "group_effective_support_ratio",
        "residual_rms_ratio",
        "p95_ratio",
        "max_ratio",
    ]:
        a = profile_a[key]
        b = profile_b[key]
        if a > 0 and b > 0:
            total += abs(mp.log(a / b))
    return total


def induced_pattern_code(poset, vertices):
    """Canonical unlabeled code for the induced order on a small vertex set."""
    m = len(vertices)
    best = None
    for perm in itertools.permutations(range(m)):
        code = 0
        bit = 1
        for a in range(m):
            va = vertices[perm[a]]
            for b in range(m):
                if a == b:
                    continue
                vb = vertices[perm[b]]
                if (poset.future[va] >> vb) & 1:
                    code |= bit
                bit <<= 1
        if best is None or code < best:
            best = code
    return best


def sampled_induced_pattern_distribution(poset, size, sample_count, seed):
    """Deterministic sampled distribution of small induced posets."""
    rng = random.Random(seed)
    counts = {}
    for _ in range(sample_count):
        vertices = tuple(rng.sample(range(poset.N), size))
        code = induced_pattern_code(poset, vertices)
        counts[code] = counts.get(code, 0) + 1
    return {
        "size": size,
        "sample_count": sample_count,
        "counts": counts,
    }


def pattern_total_variation(dist_a, dist_b):
    total = mp.mpf(0)
    keys = set(dist_a["counts"]) | set(dist_b["counts"])
    sample_a = mp.mpf(dist_a["sample_count"])
    sample_b = mp.mpf(dist_b["sample_count"])
    for key in keys:
        pa = mp.mpf(dist_a["counts"].get(key, 0)) / sample_a
        pb = mp.mpf(dist_b["counts"].get(key, 0)) / sample_b
        total += abs(pa - pb)
    return total / 2


def summarize(name, poset, audit):
    r = poset.ordering_fraction()
    dmm = mm_inv(r)
    print(
        f"{name:24s} N={poset.N:4d} rel={poset.relation_count():8d} "
        f"r={fmt(r, 18):>22s} dMM={fmt(dmm, 14):>16s} "
        f"H={poset.height():4d} rec_r={fmt(audit['recursive_r'], 18):>22s} "
        f"eff/N={fmt(audit['effective_support_ratio'], 18):>22s} "
        f"maxdup={fmt(audit['max_duplicate_fraction'], 18):>22s}"
    )


def height_scale_ratio(poset):
    return mp.mpf(poset.height()) / (2 * mp.sqrt(poset.N))


def tune_score(poset):
    """Score closeness to the crude 1+1 global MM and height targets."""
    return abs(poset.ordering_fraction() - mp.mpf("0.5")) + abs(
        height_scale_ratio(poset) - 1
    )


def hist_density_at(poset, audit, k):
    if k < 0 or k >= len(audit["hist"]):
        return mp.mpf(0)
    return mp.mpf(audit["hist"][k]) / poset.N


def external_twin_audit(poset):
    """Find pairs with identical causal environment outside the pair.

    For records x,y, ignore x and y themselves and compare their past and future
    sets.  Fiber blow-ups create many such pairs even when the two records are
    internally related; a generic sprinkling should not.
    """
    parent = list(range(poset.N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra

    pairs = 0
    for x in range(poset.N):
        clear_x = ~(1 << x)
        for y in range(x + 1, poset.N):
            clear_y = ~(1 << y)
            if (
                (poset.past[x] & clear_y) == (poset.past[y] & clear_x)
                and (poset.future[x] & clear_y) == (poset.future[y] & clear_x)
            ):
                pairs += 1
                union(x, y)

    classes = {}
    for x in range(poset.N):
        root = find(x)
        classes[root] = classes.get(root, 0) + 1
    nontrivial = [size for size in classes.values() if size > 1]
    total_pairs = poset.N * (poset.N - 1) // 2
    return {
        "pairs": pairs,
        "pair_fraction": mp.mpf(pairs) / total_pairs,
        "classes": len(nontrivial),
        "max_class": max(nontrivial) if nontrivial else 1,
    }


def external_near_twin_audit(poset, thresholds):
    """Count pairs whose external causal environments differ by few records."""
    thresholds = sorted(int(t) for t in thresholds)
    counts = {t: 0 for t in thresholds}
    min_diff = None
    examples = []
    for x in range(poset.N):
        clear_x = ~(1 << x)
        for y in range(x + 1, poset.N):
            clear_y = ~(1 << y)
            past_x = poset.past[x] & clear_y
            past_y = poset.past[y] & clear_x
            future_x = poset.future[x] & clear_y
            future_y = poset.future[y] & clear_x
            diff = (past_x ^ past_y).bit_count() + (future_x ^ future_y).bit_count()
            if min_diff is None or diff < min_diff:
                min_diff = diff
                examples = [(x, y, diff)]
            elif diff == min_diff and len(examples) < 5:
                examples.append((x, y, diff))
            for threshold in thresholds:
                if diff <= threshold:
                    counts[threshold] += 1
    total_pairs = poset.N * (poset.N - 1) // 2
    return {
        "counts": counts,
        "fractions": {t: mp.mpf(counts[t]) / total_pairs for t in thresholds},
        "min_diff": min_diff if min_diff is not None else 0,
        "examples": examples,
    }


def labeled_near_twin_audit(poset, labels, thresholds):
    """Near-twin counts split by whether pairs came from the same hidden label."""
    thresholds = sorted(int(t) for t in thresholds)
    same_counts = {t: 0 for t in thresholds}
    different_counts = {t: 0 for t in thresholds}
    same_total = 0
    different_total = 0
    for x in range(poset.N):
        clear_x = ~(1 << x)
        for y in range(x + 1, poset.N):
            clear_y = ~(1 << y)
            past_x = poset.past[x] & clear_y
            past_y = poset.past[y] & clear_x
            future_x = poset.future[x] & clear_y
            future_y = poset.future[y] & clear_x
            diff = (past_x ^ past_y).bit_count() + (future_x ^ future_y).bit_count()
            target = same_counts if labels[x] == labels[y] else different_counts
            if labels[x] == labels[y]:
                same_total += 1
            else:
                different_total += 1
            for threshold in thresholds:
                if diff <= threshold:
                    target[threshold] += 1
    return {
        "same_counts": same_counts,
        "different_counts": different_counts,
        "same_total": same_total,
        "different_total": different_total,
    }


print("=" * 80)
print("P23 recursive interval law / no-hidden-staging receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

print("\n(1) Exact fixed-N interval histogram expectation")
hist_N = 96
alpha = mp.log(2)
expected_densities = [expected_hist_density_2d(hist_N, k) for k in range(hist_N - 1)]
expected_total_density = sum(expected_densities)
expected_relation_density = mp.mpf(hist_N - 1) / 4
expected_P_from_hist = profile_P_from_hist_density(expected_densities, alpha)
expected_P_direct = sprinkle_pair_density_expectation(hist_N, alpha)
print("N =", hist_N)
print("sum_k E[H_k/N] =", fmt(expected_total_density, 40))
print("(N-1)/4 =", fmt(expected_relation_density, 40))
print("P_log2 from full histogram =", fmt(expected_P_from_hist, 40))
print("P_log2 from generating formula =", fmt(expected_P_direct, 40))
check(
    "Full histogram expectation sums to expected relation density",
    abs(expected_total_density - expected_relation_density) < mp.mpf("1e-80"),
    f"gap={fmt(abs(expected_total_density - expected_relation_density), 12)}",
)
check(
    "Full histogram expectation reproduces generating-function expectation",
    abs(expected_P_from_hist - expected_P_direct) < mp.mpf("1e-80"),
    f"gap={fmt(abs(expected_P_from_hist - expected_P_direct), 12)}",
)

print("\n(2) Coarse full-histogram calibration on a fixed sprinkling")
spr_hist_N = 192
spr = sprinkled2_poset(spr_hist_N, 11012203)
spr_audit = spr.interval_audit(load_k_min=8)
spr_densities = [mp.mpf(v) / spr.N for v in spr_audit["hist"]]
expected_spr_densities = [expected_hist_density_2d(spr_hist_N, k) for k in range(spr_hist_N - 1)]
bins = [
    ("0", 0, 0),
    ("1", 1, 1),
    ("2-3", 2, 3),
    ("4-7", 4, 7),
    ("8-15", 8, 15),
    ("16-31", 16, 31),
    ("32+", 32, None),
]
spr_bins = bin_histogram(spr_densities, bins)
exp_bins = bin_histogram(expected_spr_densities, bins)
max_bin_log_gap = mp.mpf(0)
for (label, obs), (_, exp) in zip(spr_bins, exp_bins):
    ratio = obs / exp if exp else mp.nan
    if obs > 0 and exp > 0:
        max_bin_log_gap = max(max_bin_log_gap, abs(mp.log(ratio)))
    print(
        f"bin={label:5s} observed H/N={fmt(obs, 18):>22s} "
        f"expected H/N={fmt(exp, 18):>22s} ratio={fmt(ratio, 12):>14s}"
    )
check(
    "Fixed sprinkling coarse interval histogram stays in a broad finite-N band",
    max_bin_log_gap < mp.mpf("0.45"),
    f"max_log_gap={fmt(max_bin_log_gap, 20)}",
)

print("\n(3) Recursive interval relation statistic")
spr_rec_N = 384
spr_rec = sprinkled2_poset(spr_rec_N, 910246)
spr_rec_audit = spr_rec.interval_audit(load_k_min=8, keep_band_masks=True)
spr_rec_all_load_audit = spr_rec.interval_audit(load_k_min=1)
chain = chain_poset(256)
chain_audit = chain.interval_audit(load_k_min=8)
thin = thin_middle_chain_poset(32, 6)
thin_audit = thin.interval_audit(load_k_min=4)
for name, poset, audit in [
    ("sprinkling", spr_rec, spr_rec_audit),
    ("chain", chain, chain_audit),
    ("thin-middle+chain", thin, thin_audit),
]:
    summarize(name, poset, audit)
check(
    "Sprinkling recursive interval relation fraction is near 1/2",
    abs(spr_rec_audit["recursive_r"] - mp.mpf("0.5")) < mp.mpf("0.035"),
    f"recursive_r={fmt(spr_rec_audit['recursive_r'], 20)}",
)
check(
    "Chain fails recursive interval relation fraction",
    abs(chain_audit["recursive_r"] - mp.mpf("0.5")) > mp.mpf("0.45"),
    f"recursive_r={fmt(chain_audit['recursive_r'], 20)}",
)
check(
    "Thin-middle adversary fails recursive interval relation fraction",
    abs(thin_audit["recursive_r"] - mp.mpf("0.5")) > mp.mpf("0.20"),
    f"recursive_r={fmt(thin_audit['recursive_r'], 20)}",
)

print("\n(4) A staged adversary spoofs the recursive mean by reusing one good block")
staged_middle = 31
staged_seed = 7307
staged, staged_inner, staged_parts = wrapped_sprinkling_sandwich_poset(
    512, staged_middle, staged_seed, chain_height=45
)
staged_audit = staged.interval_audit(load_k_min=8, keep_band_masks=True)
staged_all_load_audit = staged.interval_audit(load_k_min=1)
inner_audit = staged_inner.interval_audit(load_k_min=4)
summarize("staged reused interval", staged, staged_audit)
summarize("inner reused block", staged_inner, inner_audit)
print("staged parts =", staged_parts, "middle_seed =", staged_seed)
check(
    "Staged adversary keeps MM dimension in the 2D band",
    abs(mm_inv(staged.ordering_fraction()) - 2) < mp.mpf("0.20"),
    f"dMM={fmt(mm_inv(staged.ordering_fraction()), 20)}",
)
check(
    "Staged adversary has 2D longest-chain height from the isolated chain",
    abs(mp.mpf(staged.height()) - 2 * mp.sqrt(staged.N)) < mp.mpf("1.0"),
    f"H={staged.height()}, 2sqrtN={fmt(2 * mp.sqrt(staged.N), 20)}",
)
check(
    "Staged adversary spoofs the recursive interval relation mean",
    abs(staged_audit["recursive_r"] - mp.mpf("0.5")) < mp.mpf("0.035"),
    f"recursive_r={fmt(staged_audit['recursive_r'], 20)}",
)

staged_expected_k = expected_hist_density_2d(staged.N, staged_middle)
staged_observed_k = mp.mpf(staged_audit["hist"][staged_middle]) / staged.N
staged_hist_ratio = staged_observed_k / staged_expected_k
print(
    f"staged full-histogram spike at k={staged_middle}: "
    f"observed H_k/N={fmt(staged_observed_k, 24)} "
    f"expected H_k/N={fmt(staged_expected_k, 24)} "
    f"ratio={fmt(staged_hist_ratio, 24)}"
)
check(
    "Full interval histogram rejects the staged recursive-mean spoof",
    staged_hist_ratio > mp.mpf("50"),
    f"ratio={fmt(staged_hist_ratio, 20)}",
)

print("\n(5) Interior-load concentration exposes the staged reuse")
spr_load = spr_rec_audit
staged_load = staged_audit
continuum_load_eff = continuum_2d_load_effective_support_no_threshold()
print(
    "sprinkling load: band_intervals=",
    spr_load["band_intervals"],
    "effective_support/N=",
    fmt(spr_load["effective_support_ratio"], 24),
    "max_load/mean=",
    fmt(spr_load["max_load_ratio"], 24),
    "max_duplicate_fraction=",
    fmt(spr_load["max_duplicate_fraction"], 24),
)
print(
    "staged load:    band_intervals=",
    staged_load["band_intervals"],
    "effective_support/N=",
    fmt(staged_load["effective_support_ratio"], 24),
    "max_load/mean=",
    fmt(staged_load["max_load_ratio"], 24),
    "max_duplicate_fraction=",
    fmt(staged_load["max_duplicate_fraction"], 24),
)
print(
    "2D continuum no-threshold mean-field S_eff/N =",
    fmt(continuum_load_eff, 24),
)
print(
    "sprinkling all-interior S_eff/N =",
    fmt(spr_rec_all_load_audit["effective_support_ratio"], 24),
)
print(
    "staged all-interior S_eff/N =",
    fmt(staged_all_load_audit["effective_support_ratio"], 24),
)
check(
    "Sprinkling has broad interior support in the tested band",
    spr_load["effective_support_ratio"] > mp.mpf("0.55")
    and spr_load["max_duplicate_fraction"] < mp.mpf("0.02"),
    f"eff/N={fmt(spr_load['effective_support_ratio'], 20)}, maxdup={fmt(spr_load['max_duplicate_fraction'], 20)}",
)
check(
    "Staged adversary has concentrated reused interiors",
    staged_load["effective_support_ratio"] < mp.mpf("0.18")
    and staged_load["max_duplicate_fraction"] > mp.mpf("0.20"),
    f"eff/N={fmt(staged_load['effective_support_ratio'], 20)}, maxdup={fmt(staged_load['max_duplicate_fraction'], 20)}",
)
check(
    "Load concentration separates staged adversary from sprinkling by a large factor",
    spr_load["effective_support_ratio"] / staged_load["effective_support_ratio"] > mp.mpf("4"),
    f"ratio={fmt(spr_load['effective_support_ratio'] / staged_load['effective_support_ratio'], 20)}",
)
check(
    "Sprinkling all-interior load is close to the 2D continuum mean-field null",
    abs(spr_rec_all_load_audit["effective_support_ratio"] - continuum_load_eff)
    < mp.mpf("0.06"),
    f"spr={fmt(spr_rec_all_load_audit['effective_support_ratio'], 20)}, null={fmt(continuum_load_eff, 20)}",
)
check(
    "Staged all-interior load is far below the 2D continuum mean-field null",
    staged_all_load_audit["effective_support_ratio"] < mp.mpf("0.15"),
    f"staged={fmt(staged_all_load_audit['effective_support_ratio'], 20)}, null={fmt(continuum_load_eff, 20)}",
)

print("\n(5b) Soft interior-overlap check")
spr_jaccard = sampled_jaccard_stats(spr_load["band_masks"], sample_limit=384)
staged_jaccard = sampled_jaccard_stats(staged_load["band_masks"], sample_limit=384)
print(
    "sprinkling Jaccard: sample=",
    spr_jaccard["sample"],
    "pairs=",
    spr_jaccard["pairs"],
    "mean=",
    fmt(spr_jaccard["mean"], 24),
    "p95=",
    fmt(spr_jaccard["p95"], 24),
    "max=",
    fmt(spr_jaccard["max"], 24),
)
print(
    "staged Jaccard:    sample=",
    staged_jaccard["sample"],
    "pairs=",
    staged_jaccard["pairs"],
    "mean=",
    fmt(staged_jaccard["mean"], 24),
    "p95=",
    fmt(staged_jaccard["p95"], 24),
    "max=",
    fmt(staged_jaccard["max"], 24),
)
check(
    "Sprinkling sampled interior overlaps are not near-duplicate dominated",
    spr_jaccard["mean"] < mp.mpf("0.30") and spr_jaccard["p95"] < mp.mpf("0.75"),
    f"mean={fmt(spr_jaccard['mean'], 20)}, p95={fmt(spr_jaccard['p95'], 20)}",
)
check(
    "Staged sampled interior overlaps are near-duplicate dominated",
    staged_jaccard["mean"] > mp.mpf("0.75") and staged_jaccard["p95"] > mp.mpf("0.95"),
    f"mean={fmt(staged_jaccard['mean'], 20)}, p95={fmt(staged_jaccard['p95'], 20)}",
)

print("\n(5c) Fiber/blow-up and distributed-staging adversaries")
fiber_base_N = 96
fiber_size = 4
fiber_antichain, fiber_antichain_base = fiber_blowup_poset(
    fiber_base_N, fiber_size, 202603, "antichain"
)
fiber_chain, fiber_chain_base = fiber_blowup_poset(
    fiber_base_N, fiber_size, 202603, "chain"
)
fiber_antichain_audit = fiber_antichain.interval_audit(load_k_min=8)
fiber_chain_audit = fiber_chain.interval_audit(load_k_min=8)
for name, poset, audit in [
    ("fiber antichain", fiber_antichain, fiber_antichain_audit),
    ("fiber chain", fiber_chain, fiber_chain_audit),
]:
    height_ratio = mp.mpf(poset.height()) / (2 * mp.sqrt(poset.N))
    summarize(name, poset, audit)
    print(
        f"{name:24s} height/(2sqrtN)={fmt(height_ratio, 24)} "
        f"base_N={fiber_base_N} fiber={fiber_size}"
    )

fiber_antichain_height_ratio = mp.mpf(fiber_antichain.height()) / (
    2 * mp.sqrt(fiber_antichain.N)
)
fiber_chain_height_ratio = mp.mpf(fiber_chain.height()) / (2 * mp.sqrt(fiber_chain.N))
check(
    "Antichain fiber blow-up exposes hidden thickness by too-low height",
    fiber_antichain_height_ratio < mp.mpf("0.75"),
    f"H/(2sqrtN)={fmt(fiber_antichain_height_ratio, 20)}",
)
check(
    "Chain fiber blow-up exposes hidden thickness by too-high height",
    fiber_chain_height_ratio > mp.mpf("1.25"),
    f"H/(2sqrtN)={fmt(fiber_chain_height_ratio, 20)}",
)
check(
    "Fiber variants keep similar quotient MM scale but not the 1+1 height law",
    abs(mm_inv(fiber_antichain.ordering_fraction()) - mm_inv(fiber_chain.ordering_fraction()))
    < mp.mpf("0.35")
    and fiber_antichain_height_ratio < mp.mpf("0.75")
    and fiber_chain_height_ratio > mp.mpf("1.25"),
    (
        f"dMM_antichain={fmt(mm_inv(fiber_antichain.ordering_fraction()), 20)}, "
        f"dMM_chain={fmt(mm_inv(fiber_chain.ordering_fraction()), 20)}"
    ),
)

distributed_staging, distributed_parts = multi_staged_reservoir_poset(
    512, module_count=4, middle=17, seed0=5519, chain_height=45
)
distributed_audit = distributed_staging.interval_audit(load_k_min=8, keep_band_masks=True)
distributed_jaccard = sampled_jaccard_stats(
    distributed_audit["band_masks"], sample_limit=384
)
summarize("distributed staging", distributed_staging, distributed_audit)
print("distributed parts =", distributed_parts)
print(
    "distributed Jaccard: sample=",
    distributed_jaccard["sample"],
    "pairs=",
    distributed_jaccard["pairs"],
    "mean=",
    fmt(distributed_jaccard["mean"], 24),
    "p95=",
    fmt(distributed_jaccard["p95"], 24),
    "max=",
    fmt(distributed_jaccard["max"], 24),
)
check(
    "Distributed staging lowers exact duplicate concentration versus one reused block",
    distributed_audit["max_duplicate_fraction"]
    < staged_load["max_duplicate_fraction"] / 2,
    (
        f"distributed={fmt(distributed_audit['max_duplicate_fraction'], 20)}, "
        f"single={fmt(staged_load['max_duplicate_fraction'], 20)}"
    ),
)
check(
    "Independent distributed staging pays by leaving the MM 2D band",
    abs(mm_inv(distributed_staging.ordering_fraction()) - 2) > mp.mpf("0.50"),
    f"dMM={fmt(mm_inv(distributed_staging.ordering_fraction()), 20)}",
)
check(
    "Distributed staging still has concentrated overlap compared with sprinkling",
    distributed_jaccard["mean"] > 2 * spr_jaccard["mean"],
    (
        f"distributed_mean={fmt(distributed_jaccard['mean'], 20)}, "
        f"sprinkling_mean={fmt(spr_jaccard['mean'], 20)}"
    ),
)

print("\n(5d) Tuned cross-linked adversary search")
mixed_candidates = []
for numerator, denominator in [
    (0, 1),
    (1, 4),
    (1, 3),
    (2, 5),
    (1, 2),
    (3, 5),
    (3, 4),
    (1, 1),
]:
    candidate, _, meta = mixed_fiber_blowup_poset(
        192, 2, 42023, numerator, denominator
    )
    mixed_candidates.append((tune_score(candidate), numerator, denominator, candidate, meta))
mixed_candidates.sort(key=lambda row: row[0])
mixed_score, mixed_num, mixed_den, mixed_fiber, mixed_meta = mixed_candidates[0]
mixed_audit = mixed_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
mixed_jaccard = sampled_jaccard_stats(mixed_audit["band_masks"], sample_limit=384)
mixed_expected_h0 = expected_hist_density_2d(mixed_fiber.N, 0)
mixed_observed_h0 = hist_density_at(mixed_fiber, mixed_audit, 0)
mixed_h0_ratio = mixed_observed_h0 / mixed_expected_h0
mixed_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / mixed_fiber.N for v in mixed_audit["hist"]], mp.log(2)
)
mixed_expected_p_log2 = sprinkle_pair_density_expectation(mixed_fiber.N, mp.log(2))
summarize("tuned mixed fiber", mixed_fiber, mixed_audit)
print(
    "mixed fiber selector=",
    mixed_meta["selector"],
    "actual_chain_fraction=",
    fmt(mixed_meta["chain_fraction"], 24),
    "score=",
    fmt(mixed_score, 24),
    "height/(2sqrtN)=",
    fmt(height_scale_ratio(mixed_fiber), 24),
)
print(
    "mixed fiber H_0/N observed=",
    fmt(mixed_observed_h0, 24),
    "expected=",
    fmt(mixed_expected_h0, 24),
    "ratio=",
    fmt(mixed_h0_ratio, 24),
    "P_log2_ratio=",
    fmt(mixed_p_log2 / mixed_expected_p_log2, 24),
)
print(
    "mixed fiber Jaccard: sample=",
    mixed_jaccard["sample"],
    "pairs=",
    mixed_jaccard["pairs"],
    "mean=",
    fmt(mixed_jaccard["mean"], 24),
    "p95=",
    fmt(mixed_jaccard["p95"], 24),
    "max=",
    fmt(mixed_jaccard["max"], 24),
)
spr_twin = external_twin_audit(spr_rec)
mixed_twin = external_twin_audit(mixed_fiber)
print(
    "external twins: sprinkling pairs=",
    spr_twin["pairs"],
    "classes=",
    spr_twin["classes"],
    "max_class=",
    spr_twin["max_class"],
    "mixed_fiber pairs=",
    mixed_twin["pairs"],
    "classes=",
    mixed_twin["classes"],
    "max_class=",
    mixed_twin["max_class"],
)
check(
    "Baseline sprinkling has negligible exact external twin pairs in this receipt",
    spr_twin["pair_fraction"] < mp.mpf("0.0001"),
    f"pairs={spr_twin['pairs']}, fraction={fmt(spr_twin['pair_fraction'], 20)}",
)
check(
    "Tuned mixed fiber reaches the global height/MM band",
    abs(height_scale_ratio(mixed_fiber) - 1) < mp.mpf("0.02")
    and abs(mm_inv(mixed_fiber.ordering_fraction()) - 2) < mp.mpf("0.15"),
    (
        f"height_ratio={fmt(height_scale_ratio(mixed_fiber), 20)}, "
        f"dMM={fmt(mm_inv(mixed_fiber.ordering_fraction()), 20)}"
    ),
)
check(
    "Tuned mixed fiber is exposed by exact external twins",
    mixed_twin["pairs"] >= 100 * spr_twin["pairs"],
    (
        f"mixed_pairs={mixed_twin['pairs']}, "
        f"spr_pairs={spr_twin['pairs']}, classes={mixed_twin['classes']}"
    ),
)
check(
    "Tuned mixed fiber shifts the log-2 interval profile by more than five percent",
    abs(mixed_p_log2 / mixed_expected_p_log2 - 1) > mp.mpf("0.05"),
    f"P_ratio={fmt(mixed_p_log2 / mixed_expected_p_log2, 20)}",
)

cross_candidates = []
for module_count in [6, 8, 9, 10, 12]:
    for middle in [5, 7, 9, 11]:
        if 512 <= module_count * (middle + 2):
            continue
        for base_seed in range(8101, 8111):
            candidate, _, meta = cross_linked_staged_reservoir_poset(
                512, module_count, middle, base_seed, 9917
            )
            cross_candidates.append(
                (tune_score(candidate), module_count, middle, base_seed, candidate, meta)
            )
cross_candidates.sort(key=lambda row: row[0])
cross_score, cross_modules, cross_middle, cross_base_seed, cross_linked, cross_meta = (
    cross_candidates[0]
)
cross_audit = cross_linked.interval_audit(load_k_min=8, keep_band_masks=True)
cross_jaccard = sampled_jaccard_stats(cross_audit["band_masks"], sample_limit=384)
cross_expected_middle = expected_hist_density_2d(cross_linked.N, cross_middle)
cross_observed_middle = hist_density_at(cross_linked, cross_audit, cross_middle)
cross_middle_ratio = cross_observed_middle / cross_expected_middle
cross_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / cross_linked.N for v in cross_audit["hist"]], mp.log(2)
)
cross_expected_p_log2 = sprinkle_pair_density_expectation(cross_linked.N, mp.log(2))
summarize("cross-linked staging", cross_linked, cross_audit)
print(
    "cross-linked staging modules=",
    cross_modules,
    "middle=",
    cross_middle,
    "base_seed=",
    cross_base_seed,
    "score=",
    fmt(cross_score, 24),
    "height/(2sqrtN)=",
    fmt(height_scale_ratio(cross_linked), 24),
)
print(
    "cross-linked H_middle/N observed=",
    fmt(cross_observed_middle, 24),
    "expected=",
    fmt(cross_expected_middle, 24),
    "ratio=",
    fmt(cross_middle_ratio, 24),
    "P_log2_ratio=",
    fmt(cross_p_log2 / cross_expected_p_log2, 24),
)
print(
    "cross-linked Jaccard: sample=",
    cross_jaccard["sample"],
    "pairs=",
    cross_jaccard["pairs"],
    "mean=",
    fmt(cross_jaccard["mean"], 24),
    "p95=",
    fmt(cross_jaccard["p95"], 24),
    "max=",
    fmt(cross_jaccard["max"], 24),
)
cross_twin = external_twin_audit(cross_linked)
print(
    "cross-linked external twins: pairs=",
    cross_twin["pairs"],
    "pair_fraction=",
    fmt(cross_twin["pair_fraction"], 24),
    "classes=",
    cross_twin["classes"],
    "max_class=",
    cross_twin["max_class"],
)
check(
    "Cross-linked staging search restores height but not the full 2D global profile",
    abs(height_scale_ratio(cross_linked) - 1) < mp.mpf("0.05")
    and (
        abs(mm_inv(cross_linked.ordering_fraction()) - 2) > mp.mpf("0.25")
        or abs(cross_audit["recursive_r"] - mp.mpf("0.5")) > mp.mpf("0.20")
    ),
    (
        f"height_ratio={fmt(height_scale_ratio(cross_linked), 20)}, "
        f"dMM={fmt(mm_inv(cross_linked.ordering_fraction()), 20)}, "
        f"recursive_r={fmt(cross_audit['recursive_r'], 20)}"
    ),
)
check(
    "Cross-linked staging still has a visible module-middle histogram spike",
    cross_middle_ratio > mp.mpf("3"),
    f"ratio={fmt(cross_middle_ratio, 20)}",
)
check(
    "Cross-linked staging has exact external twin classes",
    cross_twin["pairs"] > mixed_twin["pairs"],
    f"pairs={cross_twin['pairs']}, max_class={cross_twin['max_class']}",
)

print("\n(5e) Decorated near-twin fiber adversary")
decorated_candidates = []
for numerator, denominator in [
    (0, 1),
    (1, 5),
    (1, 4),
    (1, 3),
    (2, 5),
    (1, 2),
    (3, 5),
    (2, 3),
    (3, 4),
    (1, 1),
]:
    candidate, _, meta = decorated_mixed_fiber_poset(
        128, 62029, numerator, denominator
    )
    decorated_candidates.append(
        (tune_score(candidate), numerator, denominator, candidate, meta)
    )
decorated_candidates.sort(key=lambda row: row[0])
decor_score, decor_num, decor_den, decorated_fiber, decor_meta = decorated_candidates[0]
decor_audit = decorated_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
decor_jaccard = sampled_jaccard_stats(decor_audit["band_masks"], sample_limit=384)
decor_twin = external_twin_audit(decorated_fiber)
thresholds = [0, 2, 4, 8, 16]
spr_near = external_near_twin_audit(spr_rec, thresholds)
mixed_near = external_near_twin_audit(mixed_fiber, thresholds)
decor_near = external_near_twin_audit(decorated_fiber, thresholds)
decor_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / decorated_fiber.N for v in decor_audit["hist"]], mp.log(2)
)
decor_expected_p_log2 = sprinkle_pair_density_expectation(
    decorated_fiber.N, mp.log(2)
)
decor_expected_h0 = expected_hist_density_2d(decorated_fiber.N, 0)
decor_observed_h0 = hist_density_at(decorated_fiber, decor_audit, 0)
decor_h0_ratio = decor_observed_h0 / decor_expected_h0
summarize("decorated near-fiber", decorated_fiber, decor_audit)
print(
    "decorated selector=",
    decor_meta["selector"],
    "actual_chain_fraction=",
    fmt(decor_meta["chain_fraction"], 24),
    "score=",
    fmt(decor_score, 24),
    "height/(2sqrtN)=",
    fmt(height_scale_ratio(decorated_fiber), 24),
)
print(
    "decorated H_0/N observed=",
    fmt(decor_observed_h0, 24),
    "expected=",
    fmt(decor_expected_h0, 24),
    "ratio=",
    fmt(decor_h0_ratio, 24),
    "P_log2_ratio=",
    fmt(decor_p_log2 / decor_expected_p_log2, 24),
)
print(
    "decorated Jaccard: sample=",
    decor_jaccard["sample"],
    "pairs=",
    decor_jaccard["pairs"],
    "mean=",
    fmt(decor_jaccard["mean"], 24),
    "p95=",
    fmt(decor_jaccard["p95"], 24),
    "max=",
    fmt(decor_jaccard["max"], 24),
)
print(
    "decorated exact twins: pairs=",
    decor_twin["pairs"],
    "pair_fraction=",
    fmt(decor_twin["pair_fraction"], 24),
    "classes=",
    decor_twin["classes"],
    "max_class=",
    decor_twin["max_class"],
)
for threshold in thresholds:
    print(
        f"near twins diff<={threshold}: "
        f"spr={spr_near['counts'][threshold]} "
        f"mixed={mixed_near['counts'][threshold]} "
        f"decorated={decor_near['counts'][threshold]} "
        f"decor/spr={fmt((mp.mpf(decor_near['counts'][threshold]) + 1) / (spr_near['counts'][threshold] + 1), 20)}"
    )
print(
    "near twin minimum diffs: spr=",
    spr_near["min_diff"],
    "mixed=",
    mixed_near["min_diff"],
    "decorated=",
    decor_near["min_diff"],
)
check(
    "Decorated fiber reaches the broad global height/MM band",
    abs(height_scale_ratio(decorated_fiber) - 1) < mp.mpf("0.08")
    and abs(mm_inv(decorated_fiber.ordering_fraction()) - 2) < mp.mpf("0.20"),
    (
        f"height_ratio={fmt(height_scale_ratio(decorated_fiber), 20)}, "
        f"dMM={fmt(mm_inv(decorated_fiber.ordering_fraction()), 20)}"
    ),
)
check(
    "Single-tag decoration does not close the exact-twin opening",
    decor_twin["pairs"] > mixed_twin["pairs"] / 2,
    f"decorated_pairs={decor_twin['pairs']}, mixed_pairs={mixed_twin['pairs']}",
)
check(
    "Single-tag decorated fiber is exposed by the soft near-twin tail",
    decor_near["counts"][4] > 10 * (spr_near["counts"][4] + 1),
    (
        f"decorated_diff4={decor_near['counts'][4]}, "
        f"spr_diff4={spr_near['counts'][4]}"
    ),
)
check(
    "Decorated fiber still shifts the log-2 interval profile",
    abs(decor_p_log2 / decor_expected_p_log2 - 1) > mp.mpf("0.04"),
    f"P_ratio={fmt(decor_p_log2 / decor_expected_p_log2, 20)}",
)

print("\n(5f) Double-decorated near-twin fiber adversary")
double_candidates = []
for numerator, denominator in [
    (0, 1),
    (1, 6),
    (1, 5),
    (1, 4),
    (1, 3),
    (2, 5),
    (1, 2),
    (3, 5),
    (2, 3),
    (3, 4),
    (1, 1),
]:
    candidate, _, meta = double_decorated_mixed_fiber_poset(
        96, 73061, numerator, denominator
    )
    double_candidates.append(
        (tune_score(candidate), numerator, denominator, candidate, meta)
    )
double_candidates.sort(key=lambda row: row[0])
double_score, double_num, double_den, double_fiber, double_meta = double_candidates[0]
double_audit = double_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
double_jaccard = sampled_jaccard_stats(double_audit["band_masks"], sample_limit=384)
double_twin = external_twin_audit(double_fiber)
double_near = external_near_twin_audit(double_fiber, thresholds)
double_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / double_fiber.N for v in double_audit["hist"]], mp.log(2)
)
double_expected_p_log2 = sprinkle_pair_density_expectation(double_fiber.N, mp.log(2))
double_expected_h0 = expected_hist_density_2d(double_fiber.N, 0)
double_observed_h0 = hist_density_at(double_fiber, double_audit, 0)
double_h0_ratio = double_observed_h0 / double_expected_h0
summarize("double decorated fiber", double_fiber, double_audit)
print(
    "double selector=",
    double_meta["selector"],
    "actual_chain_fraction=",
    fmt(double_meta["chain_fraction"], 24),
    "score=",
    fmt(double_score, 24),
    "height/(2sqrtN)=",
    fmt(height_scale_ratio(double_fiber), 24),
)
print(
    "double H_0/N observed=",
    fmt(double_observed_h0, 24),
    "expected=",
    fmt(double_expected_h0, 24),
    "ratio=",
    fmt(double_h0_ratio, 24),
    "P_log2_ratio=",
    fmt(double_p_log2 / double_expected_p_log2, 24),
)
print(
    "double Jaccard: sample=",
    double_jaccard["sample"],
    "pairs=",
    double_jaccard["pairs"],
    "mean=",
    fmt(double_jaccard["mean"], 24),
    "p95=",
    fmt(double_jaccard["p95"], 24),
    "max=",
    fmt(double_jaccard["max"], 24),
)
print(
    "double exact twins: pairs=",
    double_twin["pairs"],
    "pair_fraction=",
    fmt(double_twin["pair_fraction"], 24),
    "classes=",
    double_twin["classes"],
    "max_class=",
    double_twin["max_class"],
)
for threshold in thresholds:
    print(
        f"double near twins diff<={threshold}: "
        f"spr={spr_near['counts'][threshold]} "
        f"double={double_near['counts'][threshold]} "
        f"double/spr={fmt((mp.mpf(double_near['counts'][threshold]) + 1) / (spr_near['counts'][threshold] + 1), 20)}"
    )
check(
    "Double-decorated fiber reaches the broad global height/MM band",
    abs(height_scale_ratio(double_fiber) - 1) < mp.mpf("0.10")
    and abs(mm_inv(double_fiber.ordering_fraction()) - 2) < mp.mpf("0.20"),
    (
        f"height_ratio={fmt(height_scale_ratio(double_fiber), 20)}, "
        f"dMM={fmt(mm_inv(double_fiber.ordering_fraction()), 20)}"
    ),
)
check(
    "Naive double decoration still does not close the exact-twin opening",
    double_twin["pairs"] > mixed_twin["pairs"],
    f"double_pairs={double_twin['pairs']}, mixed_pairs={mixed_twin['pairs']}",
)
check(
    "Double-decorated fiber is still exposed by the soft near-twin tail",
    double_near["counts"][8] > 3 * (spr_near["counts"][8] + 1),
    (
        f"double_diff8={double_near['counts'][8]}, "
        f"spr_diff8={spr_near['counts'][8]}"
    ),
)
check(
    "Double-decorated fiber still shifts the log-2 interval profile",
    abs(double_p_log2 / double_expected_p_log2 - 1) > mp.mpf("0.04"),
    f"P_ratio={fmt(double_p_log2 / double_expected_p_log2, 20)}",
)

print("\n(5g) Twin-free local motif fiber adversary")
twinfree_candidates = []
for tf_seed in range(81031, 81051):
    for numerator, denominator in [
        (0, 1),
        (1, 6),
        (1, 5),
        (1, 4),
        (1, 3),
        (2, 5),
        (1, 2),
        (3, 5),
        (2, 3),
        (3, 4),
        (1, 1),
    ]:
        candidate, _, meta = twin_free_decorated_fiber_poset(
            96, tf_seed, numerator, denominator
        )
        hgap = abs(height_scale_ratio(candidate) - 1)
        dgap = abs(mm_inv(candidate.ordering_fraction()) - 2)
        if hgap < mp.mpf("0.10") and dgap < mp.mpf("0.20"):
            twin_pairs = external_twin_audit(candidate)["pairs"]
            selection_score = mp.mpf(twin_pairs) + tune_score(candidate)
        else:
            twin_pairs = candidate.N * candidate.N
            selection_score = mp.mpf(twin_pairs) + tune_score(candidate)
        twinfree_candidates.append(
            (
                selection_score,
                twin_pairs,
                tune_score(candidate),
                numerator,
                denominator,
                candidate,
                meta,
            )
        )
twinfree_candidates.sort(key=lambda row: row[0])
tf_selection_score, tf_search_twins, tf_score, tf_num, tf_den, twinfree_fiber, tf_meta = (
    twinfree_candidates[0]
)
tf_audit = twinfree_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
tf_jaccard = sampled_jaccard_stats(tf_audit["band_masks"], sample_limit=384)
tf_twin = external_twin_audit(twinfree_fiber)
tf_near = external_near_twin_audit(twinfree_fiber, thresholds)
tf_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / twinfree_fiber.N for v in tf_audit["hist"]], mp.log(2)
)
tf_expected_p_log2 = sprinkle_pair_density_expectation(twinfree_fiber.N, mp.log(2))
tf_expected_h0 = expected_hist_density_2d(twinfree_fiber.N, 0)
tf_observed_h0 = hist_density_at(twinfree_fiber, tf_audit, 0)
tf_h0_ratio = tf_observed_h0 / tf_expected_h0
summarize("twin-free motif fiber", twinfree_fiber, tf_audit)
print(
    "twin-free selector=",
    tf_meta["selector"],
    "seed=",
    tf_meta["seed"],
    "actual_tall_fraction=",
    fmt(tf_meta["tall_fraction"], 24),
    "score=",
    fmt(tf_score, 24),
    "height/(2sqrtN)=",
    fmt(height_scale_ratio(twinfree_fiber), 24),
)
print(
    "twin-free H_0/N observed=",
    fmt(tf_observed_h0, 24),
    "expected=",
    fmt(tf_expected_h0, 24),
    "ratio=",
    fmt(tf_h0_ratio, 24),
    "P_log2_ratio=",
    fmt(tf_p_log2 / tf_expected_p_log2, 24),
)
print(
    "twin-free Jaccard: sample=",
    tf_jaccard["sample"],
    "pairs=",
    tf_jaccard["pairs"],
    "mean=",
    fmt(tf_jaccard["mean"], 24),
    "p95=",
    fmt(tf_jaccard["p95"], 24),
    "max=",
    fmt(tf_jaccard["max"], 24),
)
print(
    "twin-free exact twins: pairs=",
    tf_twin["pairs"],
    "pair_fraction=",
    fmt(tf_twin["pair_fraction"], 24),
    "classes=",
    tf_twin["classes"],
    "max_class=",
    tf_twin["max_class"],
)
for threshold in thresholds:
    print(
        f"twin-free near twins diff<={threshold}: "
        f"spr={spr_near['counts'][threshold]} "
        f"tf={tf_near['counts'][threshold]} "
        f"tf/spr={fmt((mp.mpf(tf_near['counts'][threshold]) + 1) / (spr_near['counts'][threshold] + 1), 20)}"
    )
check(
    "Twin-free motif fiber reaches the broad global height/MM band",
    abs(height_scale_ratio(twinfree_fiber) - 1) < mp.mpf("0.10")
    and abs(mm_inv(twinfree_fiber.ordering_fraction()) - 2) < mp.mpf("0.20"),
    (
        f"height_ratio={fmt(height_scale_ratio(twinfree_fiber), 20)}, "
        f"dMM={fmt(mm_inv(twinfree_fiber.ordering_fraction()), 20)}"
    ),
)
check(
    "Twin-free motif sharply lowers exact twins relative to naive double decoration",
    tf_twin["pairs"] < double_twin["pairs"] / 10,
    f"tf_pairs={tf_twin['pairs']}, double_pairs={double_twin['pairs']}",
)
check(
    "Twin-free motif is still exposed by the soft near-twin tail",
    tf_near["counts"][8] > 3 * (spr_near["counts"][8] + 1),
    f"tf_diff8={tf_near['counts'][8]}, spr_diff8={spr_near['counts'][8]}",
)
check(
    "Twin-free motif closes exact-twin and log-2 scalar alarms",
    tf_twin["pairs"] == 0
    and abs(tf_p_log2 / tf_expected_p_log2 - 1) < mp.mpf("0.04"),
    f"P_ratio={fmt(tf_p_log2 / tf_expected_p_log2, 20)}",
)

print("\n(5h) Rich random-motif fiber adversary")
rich_candidates = []
for width, base_N in [(6, 64), (8, 48), (12, 32), (16, 24)]:
    for numerator, denominator in [
        (1, 8),
        (1, 6),
        (1, 5),
        (1, 4),
        (1, 3),
        (2, 5),
        (1, 2),
        (3, 5),
    ]:
        for base_seed in range(9101, 9106):
            candidate, _, meta = random_motif_fiber_poset(
                base_N, width, base_seed, 12031, numerator, denominator
            )
            hgap = abs(height_scale_ratio(candidate) - 1)
            dgap = abs(mm_inv(candidate.ordering_fraction()) - 2)
            if hgap < mp.mpf("0.18") and dgap < mp.mpf("0.25"):
                near = external_near_twin_audit(candidate, [8])["counts"][8]
                selection_score = mp.mpf(near) + 100 * tune_score(candidate)
            else:
                near = candidate.N * candidate.N
                selection_score = mp.mpf(near) + 100 * tune_score(candidate)
            rich_candidates.append(
                (
                    selection_score,
                    near,
                    tune_score(candidate),
                    width,
                    base_N,
                    numerator,
                    denominator,
                    candidate,
                    meta,
                )
            )
rich_candidates.sort(key=lambda row: row[0])
(
    rich_selection,
    rich_search_near8,
    rich_score,
    rich_width,
    rich_base_N,
    rich_num,
    rich_den,
    rich_fiber,
    rich_meta,
) = rich_candidates[0]
rich_audit = rich_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
rich_jaccard = sampled_jaccard_stats(rich_audit["band_masks"], sample_limit=384)
rich_twin = external_twin_audit(rich_fiber)
rich_near = external_near_twin_audit(rich_fiber, thresholds)
rich_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / rich_fiber.N for v in rich_audit["hist"]], mp.log(2)
)
rich_expected_p_log2 = sprinkle_pair_density_expectation(rich_fiber.N, mp.log(2))
rich_expected_h0 = expected_hist_density_2d(rich_fiber.N, 0)
rich_observed_h0 = hist_density_at(rich_fiber, rich_audit, 0)
rich_h0_ratio = rich_observed_h0 / rich_expected_h0
summarize("rich random motif", rich_fiber, rich_audit)
print(
    "rich width=",
    rich_width,
    "base_N=",
    rich_base_N,
    "selector=",
    rich_meta["selector"],
    "base_seed=",
    rich_meta["base_seed"],
    "motif_seed=",
    rich_meta["motif_seed"],
    "local_height_range=",
    (rich_meta["min_local_height"], rich_meta["max_local_height"]),
    "mean_local_height=",
    fmt(rich_meta["mean_local_height"], 24),
    "height/(2sqrtN)=",
    fmt(height_scale_ratio(rich_fiber), 24),
)
print(
    "rich H_0/N observed=",
    fmt(rich_observed_h0, 24),
    "expected=",
    fmt(rich_expected_h0, 24),
    "ratio=",
    fmt(rich_h0_ratio, 24),
    "P_log2_ratio=",
    fmt(rich_p_log2 / rich_expected_p_log2, 24),
)
print(
    "rich Jaccard: sample=",
    rich_jaccard["sample"],
    "pairs=",
    rich_jaccard["pairs"],
    "mean=",
    fmt(rich_jaccard["mean"], 24),
    "p95=",
    fmt(rich_jaccard["p95"], 24),
    "max=",
    fmt(rich_jaccard["max"], 24),
)
print(
    "rich exact twins: pairs=",
    rich_twin["pairs"],
    "pair_fraction=",
    fmt(rich_twin["pair_fraction"], 24),
    "classes=",
    rich_twin["classes"],
    "max_class=",
    rich_twin["max_class"],
)
for threshold in thresholds:
    print(
        f"rich near twins diff<={threshold}: "
        f"spr={spr_near['counts'][threshold]} "
        f"rich={rich_near['counts'][threshold]} "
        f"rich/spr={fmt((mp.mpf(rich_near['counts'][threshold]) + 1) / (spr_near['counts'][threshold] + 1), 20)}"
    )
check(
    "Rich random motif remains in a broad global height/MM band",
    abs(height_scale_ratio(rich_fiber) - 1) < mp.mpf("0.18")
    and abs(mm_inv(rich_fiber.ordering_fraction()) - 2) < mp.mpf("0.25"),
    (
        f"height_ratio={fmt(height_scale_ratio(rich_fiber), 20)}, "
        f"dMM={fmt(mm_inv(rich_fiber.ordering_fraction()), 20)}"
    ),
)
check(
    "Rich random motif search does not improve the soft diff<=8 tail",
    rich_near["counts"][8] >= tf_near["counts"][8],
    f"rich_diff8={rich_near['counts'][8]}, tf_diff8={tf_near['counts'][8]}",
)
check(
    "Rich random motif still has excess near-twin mass over sprinkling",
    rich_near["counts"][16] > mp.mpf("1.25") * spr_near["counts"][16],
    f"rich_diff16={rich_near['counts'][16]}, spr_diff16={spr_near['counts'][16]}",
)
check(
    "Rich random motif pays through interval profile or recursive-content drift",
    abs(rich_p_log2 / rich_expected_p_log2 - 1) > mp.mpf("0.04")
    or abs(rich_audit["recursive_r"] - mp.mpf("0.5")) > mp.mpf("0.04"),
    (
        f"P_ratio={fmt(rich_p_log2 / rich_expected_p_log2, 20)}, "
        f"recursive_r={fmt(rich_audit['recursive_r'], 20)}"
    ),
)

print("\n(5i) Clustered coordinate-jitter fiber adversary")
cluster_candidates = []
for jitter_num, jitter_den in [
    (0, 1),
    (1, 24),
    (1, 16),
    (1, 12),
    (1, 8),
    (1, 6),
    (1, 4),
    (1, 3),
    (1, 2),
    (2, 3),
    (3, 4),
    (1, 1),
    (4, 3),
    (3, 2),
    (2, 1),
    (3, 1),
]:
    for cluster_seed in range(16001, 16009):
        candidate, meta = clustered_jittered_fiber_poset(
            96, 4, cluster_seed, jitter_num, jitter_den
        )
        hgap = abs(height_scale_ratio(candidate) - 1)
        dgap = abs(mm_inv(candidate.ordering_fraction()) - 2)
        broad = hgap < mp.mpf("0.20") and dgap < mp.mpf("0.25")
        near8 = (
            external_near_twin_audit(candidate, [8])["counts"][8]
            if broad
            else candidate.N * candidate.N
        )
        cluster_candidates.append(
            (
                near8,
                tune_score(candidate),
                jitter_num,
                jitter_den,
                candidate,
                meta,
            )
        )

bounded_cluster_candidates = [
    row for row in cluster_candidates if row[5]["span_over_spacing"] <= 1
]
bounded_cluster_candidates.sort(key=lambda row: (row[0], row[1]))
(
    cluster_near8_search,
    cluster_score,
    cluster_jitter_num,
    cluster_jitter_den,
    cluster_fiber,
    cluster_meta,
) = bounded_cluster_candidates[0]
cluster_audit = cluster_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
cluster_jaccard = sampled_jaccard_stats(cluster_audit["band_masks"], sample_limit=384)
cluster_twin = external_twin_audit(cluster_fiber)
cluster_near = external_near_twin_audit(cluster_fiber, thresholds)
cluster_labeled = labeled_near_twin_audit(
    cluster_fiber, cluster_meta["cluster_labels"], thresholds
)
endpoint_ks = [0, 2, 8]
conditional_ks = [0, 2, 8]
spr_endpoint_profiles = {
    k: small_interval_endpoint_stats(spr_rec, k) for k in endpoint_ks
}
spr_conditional_profiles = {
    k: conditional_endpoint_residual_stats(spr_rec, k, bins=4)
    for k in conditional_ks
}
cluster_endpoint_profiles = {
    k: small_interval_endpoint_stats(cluster_fiber, k) for k in endpoint_ks
}
cluster_conditional_profiles = {
    k: conditional_endpoint_residual_stats(cluster_fiber, k, bins=4)
    for k in conditional_ks
}
cluster_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / cluster_fiber.N for v in cluster_audit["hist"]], mp.log(2)
)
cluster_expected_p_log2 = sprinkle_pair_density_expectation(
    cluster_fiber.N, mp.log(2)
)
cluster_expected_h0 = expected_hist_density_2d(cluster_fiber.N, 0)
cluster_observed_h0 = hist_density_at(cluster_fiber, cluster_audit, 0)
cluster_h0_ratio = cluster_observed_h0 / cluster_expected_h0
summarize("bounded jitter fiber", cluster_fiber, cluster_audit)
print(
    "bounded jitter seed=",
    cluster_meta["seed"],
    "jitter=",
    cluster_meta["jitter"],
    "span/spacing=",
    fmt(cluster_meta["span_over_spacing"], 24),
    "score=",
    fmt(cluster_score, 24),
    "height/(2sqrtN)=",
    fmt(height_scale_ratio(cluster_fiber), 24),
)
print(
    "bounded jitter H_0/N observed=",
    fmt(cluster_observed_h0, 24),
    "expected=",
    fmt(cluster_expected_h0, 24),
    "ratio=",
    fmt(cluster_h0_ratio, 24),
    "P_log2_ratio=",
    fmt(cluster_p_log2 / cluster_expected_p_log2, 24),
)
print(
    "bounded jitter Jaccard: sample=",
    cluster_jaccard["sample"],
    "pairs=",
    cluster_jaccard["pairs"],
    "mean=",
    fmt(cluster_jaccard["mean"], 24),
    "p95=",
    fmt(cluster_jaccard["p95"], 24),
    "max=",
    fmt(cluster_jaccard["max"], 24),
)
print(
    "bounded jitter exact twins: pairs=",
    cluster_twin["pairs"],
    "pair_fraction=",
    fmt(cluster_twin["pair_fraction"], 24),
    "classes=",
    cluster_twin["classes"],
    "max_class=",
    cluster_twin["max_class"],
)
for threshold in thresholds:
    print(
        f"bounded jitter near twins diff<={threshold}: "
        f"spr={spr_near['counts'][threshold]} "
        f"bounded={cluster_near['counts'][threshold]} "
        f"same_cluster={cluster_labeled['same_counts'][threshold]} "
        f"bounded/spr={fmt((mp.mpf(cluster_near['counts'][threshold]) + 1) / (spr_near['counts'][threshold] + 1), 20)}"
    )
for k in endpoint_ks:
    spr_profile = spr_endpoint_profiles[k]
    cluster_profile = cluster_endpoint_profiles[k]
    print(
        f"endpoint load k<={k}: "
        f"spr_density={fmt(spr_profile['density'], 18)} "
        f"bounded_density={fmt(cluster_profile['density'], 18)} "
        f"spr_eff/N={fmt(spr_profile['effective_support_ratio'], 18)} "
        f"bounded_eff/N={fmt(cluster_profile['effective_support_ratio'], 18)} "
        f"spr_p95/mean={fmt(spr_profile['p95_ratio'], 18)} "
        f"bounded_p95/mean={fmt(cluster_profile['p95_ratio'], 18)} "
        f"spr_max/mean={fmt(spr_profile['max_ratio'], 18)} "
        f"bounded_max/mean={fmt(cluster_profile['max_ratio'], 18)}"
    )
for k in conditional_ks:
    spr_profile = spr_conditional_profiles[k]
    cluster_profile = cluster_conditional_profiles[k]
    print(
        f"conditional endpoint k<={k}: "
        f"spr_group_eff/N={fmt(spr_profile['group_effective_support_ratio'], 18)} "
        f"bounded_group_eff/N={fmt(cluster_profile['group_effective_support_ratio'], 18)} "
        f"spr_rms={fmt(spr_profile['residual_rms_ratio'], 18)} "
        f"bounded_rms={fmt(cluster_profile['residual_rms_ratio'], 18)} "
        f"spr_p95={fmt(spr_profile['p95_ratio'], 18)} "
        f"bounded_p95={fmt(cluster_profile['p95_ratio'], 18)} "
        f"spr_max={fmt(spr_profile['max_ratio'], 18)} "
        f"bounded_max={fmt(cluster_profile['max_ratio'], 18)}"
    )

washout_candidates = [
    row for row in cluster_candidates if row[5]["span_over_spacing"] > 1
]
washout_candidates.sort(
    key=lambda row: (
        abs(mp.mpf(row[0]) - spr_near["counts"][8]),
        row[1],
    )
)
(
    washout_near8_search,
    washout_score,
    washout_jitter_num,
    washout_jitter_den,
    washout_fiber,
    washout_meta,
) = washout_candidates[0]
washout_audit = washout_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
washout_jaccard = sampled_jaccard_stats(washout_audit["band_masks"], sample_limit=384)
washout_twin = external_twin_audit(washout_fiber)
washout_near = external_near_twin_audit(washout_fiber, thresholds)
washout_labeled = labeled_near_twin_audit(
    washout_fiber, washout_meta["cluster_labels"], thresholds
)
washout_endpoint_profiles = {
    k: small_interval_endpoint_stats(washout_fiber, k) for k in endpoint_ks
}
washout_conditional_profiles = {
    k: conditional_endpoint_residual_stats(washout_fiber, k, bins=4)
    for k in conditional_ks
}
washout_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / washout_fiber.N for v in washout_audit["hist"]], mp.log(2)
)
washout_expected_p_log2 = sprinkle_pair_density_expectation(
    washout_fiber.N, mp.log(2)
)
washout_expected_h0 = expected_hist_density_2d(washout_fiber.N, 0)
washout_observed_h0 = hist_density_at(washout_fiber, washout_audit, 0)
washout_h0_ratio = washout_observed_h0 / washout_expected_h0
summarize("over-jitter washout", washout_fiber, washout_audit)
print(
    "over-jitter seed=",
    washout_meta["seed"],
    "jitter=",
    washout_meta["jitter"],
    "span/spacing=",
    fmt(washout_meta["span_over_spacing"], 24),
    "score=",
    fmt(washout_score, 24),
    "height/(2sqrtN)=",
    fmt(height_scale_ratio(washout_fiber), 24),
)
print(
    "over-jitter H_0/N observed=",
    fmt(washout_observed_h0, 24),
    "expected=",
    fmt(washout_expected_h0, 24),
    "ratio=",
    fmt(washout_h0_ratio, 24),
    "P_log2_ratio=",
    fmt(washout_p_log2 / washout_expected_p_log2, 24),
)
print(
    "over-jitter Jaccard: sample=",
    washout_jaccard["sample"],
    "pairs=",
    washout_jaccard["pairs"],
    "mean=",
    fmt(washout_jaccard["mean"], 24),
    "p95=",
    fmt(washout_jaccard["p95"], 24),
    "max=",
    fmt(washout_jaccard["max"], 24),
)
print(
    "over-jitter exact twins: pairs=",
    washout_twin["pairs"],
    "pair_fraction=",
    fmt(washout_twin["pair_fraction"], 24),
    "classes=",
    washout_twin["classes"],
    "max_class=",
    washout_twin["max_class"],
)
for threshold in thresholds:
    print(
        f"over-jitter near twins diff<={threshold}: "
        f"spr={spr_near['counts'][threshold]} "
        f"washout={washout_near['counts'][threshold]} "
        f"same_cluster={washout_labeled['same_counts'][threshold]} "
        f"washout/spr={fmt((mp.mpf(washout_near['counts'][threshold]) + 1) / (spr_near['counts'][threshold] + 1), 20)}"
    )
for k in endpoint_ks:
    spr_profile = spr_endpoint_profiles[k]
    washout_profile = washout_endpoint_profiles[k]
    print(
        f"washout endpoint load k<={k}: "
        f"spr_density={fmt(spr_profile['density'], 18)} "
        f"washout_density={fmt(washout_profile['density'], 18)} "
        f"spr_eff/N={fmt(spr_profile['effective_support_ratio'], 18)} "
        f"washout_eff/N={fmt(washout_profile['effective_support_ratio'], 18)} "
        f"spr_p95/mean={fmt(spr_profile['p95_ratio'], 18)} "
        f"washout_p95/mean={fmt(washout_profile['p95_ratio'], 18)} "
        f"spr_max/mean={fmt(spr_profile['max_ratio'], 18)} "
        f"washout_max/mean={fmt(washout_profile['max_ratio'], 18)}"
    )
for k in conditional_ks:
    spr_profile = spr_conditional_profiles[k]
    washout_profile = washout_conditional_profiles[k]
    print(
        f"washout conditional endpoint k<={k}: "
        f"spr_group_eff/N={fmt(spr_profile['group_effective_support_ratio'], 18)} "
        f"washout_group_eff/N={fmt(washout_profile['group_effective_support_ratio'], 18)} "
        f"spr_rms={fmt(spr_profile['residual_rms_ratio'], 18)} "
        f"washout_rms={fmt(washout_profile['residual_rms_ratio'], 18)} "
        f"spr_p95={fmt(spr_profile['p95_ratio'], 18)} "
        f"washout_p95={fmt(washout_profile['p95_ratio'], 18)} "
        f"spr_max={fmt(spr_profile['max_ratio'], 18)} "
        f"washout_max={fmt(washout_profile['max_ratio'], 18)}"
    )
check(
    "Bounded coordinate jitter remains in a broad global height/MM band",
    abs(height_scale_ratio(cluster_fiber) - 1) < mp.mpf("0.20")
    and abs(mm_inv(cluster_fiber.ordering_fraction()) - 2) < mp.mpf("0.25"),
    (
        f"height_ratio={fmt(height_scale_ratio(cluster_fiber), 20)}, "
        f"dMM={fmt(mm_inv(cluster_fiber.ordering_fraction()), 20)}"
    ),
)
check(
    "Bounded coordinate jitter reduces the soft diff<=8 tail versus twin-free motifs",
    cluster_near["counts"][8] < tf_near["counts"][8],
    f"bounded_diff8={cluster_near['counts'][8]}, tf_diff8={tf_near['counts'][8]}",
)
check(
    "Bounded coordinate jitter still leaves excess near-twin mass over sprinkling",
    cluster_near["counts"][8] > mp.mpf("1.5") * spr_near["counts"][8],
    f"bounded_diff8={cluster_near['counts'][8]}, spr_diff8={spr_near['counts'][8]}",
)
check(
    "Over-jitter washout moves closer to the sprinkling soft tail",
    abs(washout_near["counts"][8] - spr_near["counts"][8])
    < abs(tf_near["counts"][8] - spr_near["counts"][8]),
    (
        f"washout_diff8={washout_near['counts'][8]}, "
        f"spr_diff8={spr_near['counts'][8]}, tf_diff8={tf_near['counts'][8]}"
    ),
)
check(
    "Over-jitter washout pays through density/profile drift or ceases to preserve hidden-cluster nearness",
    abs(washout_p_log2 / washout_expected_p_log2 - 1) > mp.mpf("0.04")
    or washout_labeled["same_counts"][8] < cluster_labeled["same_counts"][8] / 4,
    (
        f"P_ratio={fmt(washout_p_log2 / washout_expected_p_log2, 20)}, "
        f"same_cluster_diff8={washout_labeled['same_counts'][8]}"
    ),
)

print("\n(5j) Regularity-aware clustered search")
regular_candidates = []
for near8, _, jitter_num, jitter_den, candidate, meta in cluster_candidates:
    hgap = abs(height_scale_ratio(candidate) - 1)
    dgap = abs(mm_inv(candidate.ordering_fraction()) - 2)
    if hgap >= mp.mpf("0.22") or dgap >= mp.mpf("0.28"):
        continue
    endpoint_profiles = {
        k: small_interval_endpoint_stats(candidate, k) for k in endpoint_ks
    }
    endpoint_gap = sum(
        endpoint_profile_distance(endpoint_profiles[k], spr_endpoint_profiles[k])
        for k in endpoint_ks
    )
    near_gap = abs(
        mp.log((mp.mpf(near8) + 1) / (mp.mpf(spr_near["counts"][8]) + 1))
    )
    global_gap = abs(height_scale_ratio(candidate) - 1) + abs(
        mm_inv(candidate.ordering_fraction()) - 2
    )
    selection_score = near_gap + endpoint_gap + 2 * global_gap
    regular_candidates.append(
        (
            selection_score,
            near_gap,
            endpoint_gap,
            global_gap,
            near8,
            jitter_num,
            jitter_den,
            candidate,
            meta,
            endpoint_profiles,
        )
    )
regular_candidates.sort(key=lambda row: row[0])
(
    regular_selection,
    regular_near_gap,
    regular_endpoint_gap,
    regular_global_gap,
    regular_search_near8,
    regular_jitter_num,
    regular_jitter_den,
    regular_fiber,
    regular_meta,
    regular_endpoint_profiles,
) = regular_candidates[0]
regular_audit = regular_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
regular_jaccard = sampled_jaccard_stats(regular_audit["band_masks"], sample_limit=384)
regular_twin = external_twin_audit(regular_fiber)
regular_near = external_near_twin_audit(regular_fiber, thresholds)
regular_labeled = labeled_near_twin_audit(
    regular_fiber, regular_meta["cluster_labels"], thresholds
)
regular_conditional_profiles = {
    k: conditional_endpoint_residual_stats(regular_fiber, k, bins=4)
    for k in conditional_ks
}
regular_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / regular_fiber.N for v in regular_audit["hist"]], mp.log(2)
)
regular_expected_p_log2 = sprinkle_pair_density_expectation(
    regular_fiber.N, mp.log(2)
)
regular_expected_h0 = expected_hist_density_2d(regular_fiber.N, 0)
regular_observed_h0 = hist_density_at(regular_fiber, regular_audit, 0)
regular_h0_ratio = regular_observed_h0 / regular_expected_h0
summarize("regularity-aware cluster", regular_fiber, regular_audit)
print(
    "regularity-aware seed=",
    regular_meta["seed"],
    "jitter=",
    regular_meta["jitter"],
    "span/spacing=",
    fmt(regular_meta["span_over_spacing"], 24),
    "selection=",
    fmt(regular_selection, 24),
    "near_gap=",
    fmt(regular_near_gap, 24),
    "endpoint_gap=",
    fmt(regular_endpoint_gap, 24),
    "global_gap=",
    fmt(regular_global_gap, 24),
)
print(
    "regularity-aware H_0/N observed=",
    fmt(regular_observed_h0, 24),
    "expected=",
    fmt(regular_expected_h0, 24),
    "ratio=",
    fmt(regular_h0_ratio, 24),
    "P_log2_ratio=",
    fmt(regular_p_log2 / regular_expected_p_log2, 24),
)
print(
    "regularity-aware Jaccard: sample=",
    regular_jaccard["sample"],
    "pairs=",
    regular_jaccard["pairs"],
    "mean=",
    fmt(regular_jaccard["mean"], 24),
    "p95=",
    fmt(regular_jaccard["p95"], 24),
    "max=",
    fmt(regular_jaccard["max"], 24),
)
print(
    "regularity-aware exact twins: pairs=",
    regular_twin["pairs"],
    "pair_fraction=",
    fmt(regular_twin["pair_fraction"], 24),
    "classes=",
    regular_twin["classes"],
    "max_class=",
    regular_twin["max_class"],
)
for threshold in thresholds:
    print(
        f"regularity-aware near twins diff<={threshold}: "
        f"spr={spr_near['counts'][threshold]} "
        f"regular={regular_near['counts'][threshold]} "
        f"same_cluster={regular_labeled['same_counts'][threshold]} "
        f"regular/spr={fmt((mp.mpf(regular_near['counts'][threshold]) + 1) / (spr_near['counts'][threshold] + 1), 20)}"
    )
for k in endpoint_ks:
    spr_profile = spr_endpoint_profiles[k]
    regular_profile = regular_endpoint_profiles[k]
    print(
        f"regularity-aware endpoint load k<={k}: "
        f"spr_density={fmt(spr_profile['density'], 18)} "
        f"regular_density={fmt(regular_profile['density'], 18)} "
        f"spr_eff/N={fmt(spr_profile['effective_support_ratio'], 18)} "
        f"regular_eff/N={fmt(regular_profile['effective_support_ratio'], 18)} "
        f"spr_p95/mean={fmt(spr_profile['p95_ratio'], 18)} "
        f"regular_p95/mean={fmt(regular_profile['p95_ratio'], 18)} "
        f"spr_max/mean={fmt(spr_profile['max_ratio'], 18)} "
        f"regular_max/mean={fmt(regular_profile['max_ratio'], 18)}"
    )
for k in conditional_ks:
    spr_profile = spr_conditional_profiles[k]
    regular_profile = regular_conditional_profiles[k]
    print(
        f"regularity-aware conditional endpoint k<={k}: "
        f"spr_group_eff/N={fmt(spr_profile['group_effective_support_ratio'], 18)} "
        f"regular_group_eff/N={fmt(regular_profile['group_effective_support_ratio'], 18)} "
        f"spr_rms={fmt(spr_profile['residual_rms_ratio'], 18)} "
        f"regular_rms={fmt(regular_profile['residual_rms_ratio'], 18)} "
        f"spr_p95={fmt(spr_profile['p95_ratio'], 18)} "
        f"regular_p95={fmt(regular_profile['p95_ratio'], 18)} "
        f"spr_max={fmt(spr_profile['max_ratio'], 18)} "
        f"regular_max={fmt(regular_profile['max_ratio'], 18)}"
    )

regular_conditional_gap = sum(
    conditional_profile_distance(
        spr_conditional_profiles[k], regular_conditional_profiles[k]
    )
    for k in conditional_ks
)
spr_alt = sprinkled2_poset(spr_rec_N, 910247)
spr_alt_conditional_profiles = {
    k: conditional_endpoint_residual_stats(spr_alt, k, bins=4)
    for k in conditional_ks
}
spr_conditional_gap = sum(
    conditional_profile_distance(
        spr_conditional_profiles[k], spr_alt_conditional_profiles[k]
    )
    for k in conditional_ks
)
print(
    "conditional endpoint calibration: "
    f"spr_vs_spr={fmt(spr_conditional_gap, 24)} "
    f"regularity_aware={fmt(regular_conditional_gap, 24)}"
)

pattern_specs = [(4, 4096, 20260701), (5, 2048, 20260702)]
spr_patterns = {
    size: sampled_induced_pattern_distribution(spr_rec, size, count, seed)
    for size, count, seed in pattern_specs
}
spr_alt_patterns = {
    size: sampled_induced_pattern_distribution(spr_alt, size, count, seed)
    for size, count, seed in pattern_specs
}
cluster_patterns = {
    size: sampled_induced_pattern_distribution(cluster_fiber, size, count, seed)
    for size, count, seed in pattern_specs
}
washout_patterns = {
    size: sampled_induced_pattern_distribution(washout_fiber, size, count, seed)
    for size, count, seed in pattern_specs
}
regular_patterns = {
    size: sampled_induced_pattern_distribution(regular_fiber, size, count, seed)
    for size, count, seed in pattern_specs
}
for size, _, _ in pattern_specs:
    print(
        f"sampled induced pattern TV size={size}: "
        f"spr_vs_spr={fmt(pattern_total_variation(spr_patterns[size], spr_alt_patterns[size]), 24)} "
        f"bounded={fmt(pattern_total_variation(spr_patterns[size], cluster_patterns[size]), 24)} "
        f"washout={fmt(pattern_total_variation(spr_patterns[size], washout_patterns[size]), 24)} "
        f"regularity_aware={fmt(pattern_total_variation(spr_patterns[size], regular_patterns[size]), 24)}"
    )

print("\n(5k) Pattern-aware clustered search")
pattern_aware_candidates = []
for row in regular_candidates[:12]:
    (
        selection_score,
        near_gap,
        endpoint_gap,
        global_gap,
        near8,
        jitter_num,
        jitter_den,
        candidate,
        meta,
        endpoint_profiles,
    ) = row
    candidate_patterns = {
        size: sampled_induced_pattern_distribution(candidate, size, count, seed)
        for size, count, seed in pattern_specs
    }
    pattern_gap = sum(
        pattern_total_variation(spr_patterns[size], candidate_patterns[size])
        for size, _, _ in pattern_specs
    )
    pattern_score = selection_score + pattern_gap
    pattern_aware_candidates.append(
        (
            pattern_score,
            pattern_gap,
            selection_score,
            near_gap,
            endpoint_gap,
            global_gap,
            near8,
            candidate,
            meta,
            endpoint_profiles,
            candidate_patterns,
        )
    )
pattern_aware_candidates.sort(key=lambda row: row[0])
(
    pattern_score,
    pattern_gap,
    pattern_regular_score,
    pattern_near_gap,
    pattern_endpoint_gap,
    pattern_global_gap,
    pattern_search_near8,
    pattern_fiber,
    pattern_meta,
    pattern_endpoint_profiles,
    pattern_patterns,
) = pattern_aware_candidates[0]
pattern_audit = pattern_fiber.interval_audit(load_k_min=8, keep_band_masks=True)
pattern_jaccard = sampled_jaccard_stats(pattern_audit["band_masks"], sample_limit=384)
pattern_twin = external_twin_audit(pattern_fiber)
pattern_near = external_near_twin_audit(pattern_fiber, thresholds)
pattern_labeled = labeled_near_twin_audit(
    pattern_fiber, pattern_meta["cluster_labels"], thresholds
)
pattern_conditional_profiles = {
    k: conditional_endpoint_residual_stats(pattern_fiber, k, bins=4)
    for k in conditional_ks
}
pattern_p_log2 = profile_P_from_hist_density(
    [mp.mpf(v) / pattern_fiber.N for v in pattern_audit["hist"]], mp.log(2)
)
pattern_expected_p_log2 = sprinkle_pair_density_expectation(
    pattern_fiber.N, mp.log(2)
)
summarize("pattern-aware cluster", pattern_fiber, pattern_audit)
print(
    "pattern-aware seed=",
    pattern_meta["seed"],
    "jitter=",
    pattern_meta["jitter"],
    "span/spacing=",
    fmt(pattern_meta["span_over_spacing"], 24),
    "score=",
    fmt(pattern_score, 24),
    "pattern_gap=",
    fmt(pattern_gap, 24),
    "regular_score=",
    fmt(pattern_regular_score, 24),
)
print(
    "pattern-aware P_log2_ratio=",
    fmt(pattern_p_log2 / pattern_expected_p_log2, 24),
    "Jaccard_mean=",
    fmt(pattern_jaccard["mean"], 24),
    "Jaccard_p95=",
    fmt(pattern_jaccard["p95"], 24),
    "exact_twins=",
    pattern_twin["pairs"],
)
for threshold in thresholds:
    print(
        f"pattern-aware near twins diff<={threshold}: "
        f"spr={spr_near['counts'][threshold]} "
        f"pattern={pattern_near['counts'][threshold]} "
        f"same_cluster={pattern_labeled['same_counts'][threshold]} "
        f"pattern/spr={fmt((mp.mpf(pattern_near['counts'][threshold]) + 1) / (spr_near['counts'][threshold] + 1), 20)}"
    )
for k in endpoint_ks:
    spr_profile = spr_endpoint_profiles[k]
    pattern_profile = pattern_endpoint_profiles[k]
    print(
        f"pattern-aware endpoint load k<={k}: "
        f"spr_density={fmt(spr_profile['density'], 18)} "
        f"pattern_density={fmt(pattern_profile['density'], 18)} "
        f"spr_eff/N={fmt(spr_profile['effective_support_ratio'], 18)} "
        f"pattern_eff/N={fmt(pattern_profile['effective_support_ratio'], 18)} "
        f"spr_p95/mean={fmt(spr_profile['p95_ratio'], 18)} "
        f"pattern_p95/mean={fmt(pattern_profile['p95_ratio'], 18)} "
        f"spr_max/mean={fmt(spr_profile['max_ratio'], 18)} "
        f"pattern_max/mean={fmt(pattern_profile['max_ratio'], 18)}"
    )
for k in conditional_ks:
    spr_profile = spr_conditional_profiles[k]
    pattern_profile = pattern_conditional_profiles[k]
    print(
        f"pattern-aware conditional endpoint k<={k}: "
        f"spr_group_eff/N={fmt(spr_profile['group_effective_support_ratio'], 18)} "
        f"pattern_group_eff/N={fmt(pattern_profile['group_effective_support_ratio'], 18)} "
        f"spr_rms={fmt(spr_profile['residual_rms_ratio'], 18)} "
        f"pattern_rms={fmt(pattern_profile['residual_rms_ratio'], 18)} "
        f"spr_p95={fmt(spr_profile['p95_ratio'], 18)} "
        f"pattern_p95={fmt(pattern_profile['p95_ratio'], 18)} "
        f"spr_max={fmt(spr_profile['max_ratio'], 18)} "
        f"pattern_max={fmt(pattern_profile['max_ratio'], 18)}"
    )
for size, _, _ in pattern_specs:
    print(
        f"pattern-aware sampled pattern TV size={size}: "
        f"spr_vs_spr={fmt(pattern_total_variation(spr_patterns[size], spr_alt_patterns[size]), 24)} "
        f"pattern={fmt(pattern_total_variation(spr_patterns[size], pattern_patterns[size]), 24)}"
    )
spr_pattern_gap = sum(
    pattern_total_variation(spr_patterns[size], spr_alt_patterns[size])
    for size, _, _ in pattern_specs
)
pattern_candidate_gap = sum(
    pattern_total_variation(spr_patterns[size], pattern_patterns[size])
    for size, _, _ in pattern_specs
)
check(
    "Regularity-aware clustered search matches the soft near-tail and scalar profile",
    regular_near["counts"][8] <= mp.mpf("1.10") * spr_near["counts"][8]
    and abs(regular_p_log2 / regular_expected_p_log2 - 1) < mp.mpf("0.02")
    and abs(height_scale_ratio(regular_fiber) - 1) < mp.mpf("0.02")
    and abs(mm_inv(regular_fiber.ordering_fraction()) - 2) < mp.mpf("0.02"),
    (
        f"regular_diff8={regular_near['counts'][8]}, spr_diff8={spr_near['counts'][8]}, "
        f"P_ratio={fmt(regular_p_log2 / regular_expected_p_log2, 20)}, "
        f"dMM={fmt(mm_inv(regular_fiber.ordering_fraction()), 20)}"
    ),
)
check(
    "Endpoint-load density projection is not enough against the regularity-aware cluster",
    regular_endpoint_gap < mp.mpf("0.25")
    and regular_endpoint_profiles[8]["max_ratio"]
    < mp.mpf("1.10") * spr_endpoint_profiles[8]["max_ratio"],
    (
        f"endpoint_gap={fmt(regular_endpoint_gap, 20)}, "
        f"k8_max_regular={fmt(regular_endpoint_profiles[8]['max_ratio'], 20)}, "
        f"k8_max_spr={fmt(spr_endpoint_profiles[8]['max_ratio'], 20)}"
    ),
)
check(
    "Conditional endpoint residuals stay within calibrated finite sprinkling variability",
    regular_conditional_gap < mp.mpf("1.30") * spr_conditional_gap,
    (
        f"conditional_gap={fmt(regular_conditional_gap, 20)}, "
        f"spr_gap={fmt(spr_conditional_gap, 20)}"
    ),
)
check(
    "Sampled small induced-pattern densities stay within finite sprinkling variability",
    pattern_candidate_gap < mp.mpf("1.30") * spr_pattern_gap,
    (
        f"pattern_gap={fmt(pattern_candidate_gap, 20)}, "
        f"spr_gap={fmt(spr_pattern_gap, 20)}"
    ),
)

print("\n(6) Consequence for the click-law target")
print("A first-order interval-size law is not enough.")
print("A pooled recursive mean catches thin staging but can be spoofed by reused first-order-good interiors.")
print("A no-hidden-staging law must also control interior support/overlap concentration.")
print("Simple hidden-fiber blow-ups are caught by height; distributed staging lowers exact duplicates")
print("but loses the global MM scale unless it pays new cross-link/interval-profile costs.")
print("Bounded tuning found closer hidden-fiber and cross-linked reservoir candidates,")
print("but they still pay visible interval-profile, exact-twin, or near-twin costs.")
print("Coordinate jitter can reduce the fiber near-tail only by moving toward a clustered")
print("1+1 point process, so the next law projection is density/regularity, not just order heredity.")
print("But finite endpoint, conditional endpoint, and small-pattern density projections can be tuned too;")
print("the surviving target is the full calibrated finite-dimensional record law, not another small checklist.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
