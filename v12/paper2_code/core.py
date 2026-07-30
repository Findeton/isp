#!/usr/bin/env python3
"""Exact finite tools for record co-reference and descent.

The module uses only Python's standard library and fractions.Fraction.
All permutations are tuples p with p[x] equal to the image of x.
A map phi_ab is represented as a permutation from chart b's token set
to chart a's token set.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

Q = Fraction
Perm = Tuple[int, ...]
Matrix = Tuple[Tuple[Fraction, ...], ...]
Vector = Tuple[Fraction, ...]


def identity_perm(n: int) -> Perm:
    return tuple(range(n))


def compose_perm(p: Perm, q: Perm) -> Perm:
    """Return p after q: x -> p[q[x]]."""
    if len(p) != len(q):
        raise ValueError("permutation sizes differ")
    return tuple(p[q[x]] for x in range(len(p)))


def inverse_perm(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def all_perms(n: int, fixed: Optional[Mapping[int, int]] = None) -> Iterable[Perm]:
    fixed = dict(fixed or {})
    for p in permutations(range(n)):
        if all(p[i] == j for i, j in fixed.items()):
            yield tuple(p)


def permute_vector(v: Sequence[Fraction], p: Perm) -> Vector:
    """Push a vector forward: out[p[i]] = v[i]."""
    if len(v) != len(p):
        raise ValueError("size mismatch")
    out = [Q(0)] * len(v)
    for i, x in enumerate(v):
        out[p[i]] = x
    return tuple(out)


def conjugate_matrix(M: Matrix, p: Perm) -> Matrix:
    """Return P M P^{-1}: out[p[i],p[j]] = M[i,j]."""
    n = len(M)
    if len(p) != n or any(len(row) != n for row in M):
        raise ValueError("matrix/permutation size mismatch")
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[p[i]][p[j]] = M[i][j]
    return tuple(tuple(row) for row in out)


def matrix_column(M: Matrix, j: int) -> Vector:
    return tuple(row[j] for row in M)


def is_column_stochastic(M: Matrix) -> bool:
    n = len(M)
    return (
        all(len(row) == n for row in M)
        and all(x >= 0 for row in M for x in row)
        and all(sum(M[i][j] for i in range(n)) == 1 for j in range(n))
    )


@dataclass(frozen=True)
class Token:
    """A chart-local record token.

    values_by_configuration is the declared record value at each configuration.
    provenance is intentionally structural and chart-local. It may distinguish an
    original from a copy, or an erased from a preserved occurrence.
    """

    name: str
    values_by_configuration: Tuple[str, ...]
    provenance: Tuple[str, ...] = ()
    occurred: bool = True
    available: bool = True


@dataclass(frozen=True)
class DynamicChart:
    name: str
    transition: Matrix
    initial: int
    tokens: Tuple[Token, ...]

    def __post_init__(self) -> None:
        n = len(self.transition)
        if not is_column_stochastic(self.transition):
            raise ValueError(f"{self.name}: transition is not column stochastic")
        if not (0 <= self.initial < n):
            raise ValueError("initial configuration out of range")
        for token in self.tokens:
            if len(token.values_by_configuration) != n:
                raise ValueError("token/configuration size mismatch")

    @property
    def n(self) -> int:
        return len(self.transition)

    def realized_distribution(self) -> Vector:
        return matrix_column(self.transition, self.initial)

    def record_law(self) -> Dict[Tuple[str, ...], Fraction]:
        out: Dict[Tuple[str, ...], Fraction] = {}
        for cfg, prob in enumerate(self.realized_distribution()):
            if prob == 0:
                continue
            key = tuple(t.values_by_configuration[cfg] for t in self.tokens if t.occurred)
            out[key] = out.get(key, Q(0)) + prob
        return out


def induced_token_maps(
    source: DynamicChart,
    target: DynamicChart,
    p: Perm,
    configurations: Optional[Iterable[int]] = None,
) -> Tuple[Perm, ...]:
    """Token bijections induced by p on the declared comparison scope.

    Full-law comparisons use every configuration. Realized-process
    comparisons pass only the initial configuration and the positive support
    of the realized column. Provenance, occurrence, and availability are
    structural token data and are checked at either scope.
    """
    if len(source.tokens) != len(target.tokens):
        return ()
    m = len(source.tokens)
    tested = tuple(range(source.n) if configurations is None else configurations)
    out: List[Perm] = []
    for tau in permutations(range(m)):
        ok = True
        for s_ix, t_ix in enumerate(tau):
            if not provenance_compatible(source.tokens[s_ix], target.tokens[t_ix]):
                ok = False
                break
            sv = source.tokens[s_ix].values_by_configuration
            tv = target.tokens[t_ix].values_by_configuration
            if any(sv[x] != tv[p[x]] for x in tested):
                ok = False
                break
        if ok:
            out.append(tuple(tau))
    return tuple(out)


def full_isomorphisms(target: DynamicChart, source: DynamicChart) -> Tuple[Tuple[Perm, Perm], ...]:
    """All full-law chart isomorphisms source -> target."""
    if target.n != source.n:
        return ()
    out: List[Tuple[Perm, Perm]] = []
    for p in all_perms(source.n, {source.initial: target.initial}):
        if conjugate_matrix(source.transition, p) != target.transition:
            continue
        for tau in induced_token_maps(source, target, p, range(source.n)):
            out.append((p, tau))
    return tuple(out)


def realized_isomorphisms(target: DynamicChart, source: DynamicChart) -> Tuple[Tuple[Perm, Perm], ...]:
    """All one-run isomorphisms using only realized-support token values."""
    if target.n != source.n:
        return ()
    tgt = target.realized_distribution()
    src = source.realized_distribution()
    realized_scope = tuple(
        sorted({source.initial} | {x for x, probability in enumerate(src) if probability > 0})
    )
    out: List[Tuple[Perm, Perm]] = []
    for p in all_perms(source.n, {source.initial: target.initial}):
        if permute_vector(src, p) != tgt:
            continue
        for tau in induced_token_maps(source, target, p, realized_scope):
            out.append((p, tau))
    return tuple(out)


def full_automorphisms(chart: DynamicChart) -> Tuple[Tuple[Perm, Perm], ...]:
    return full_isomorphisms(chart, chart)


# ---------------------------------------------------------------------------
# Fact certification
# ---------------------------------------------------------------------------
Joint2 = Mapping[Tuple[str, str], Fraction]
Joint3 = Mapping[Tuple[str, str, str], Fraction]


def normalized_joint(joint: Mapping[Tuple[str, ...], Fraction]) -> bool:
    return all(v >= 0 for v in joint.values()) and sum(joint.values(), Q(0)) == 1


def graph_supported(joint: Joint2, value_map: Mapping[str, str]) -> bool:
    """Positive support lies on y=value_map[x]."""
    if not normalized_joint(joint):
        return False
    return all(prob == 0 or value_map.get(x) == y for (x, y), prob in joint.items())


def same_fact_by_extension(joint: Joint2) -> bool:
    """Identity-of-values extension certificate."""
    values = {x for x, _ in joint} | {y for _, y in joint}
    return graph_supported(joint, {x: x for x in values})


def same_fact_by_witness(joint: Joint3) -> bool:
    """A common witness z is perfectly value-correlated with x and y."""
    if not normalized_joint(joint):
        return False
    return all(prob == 0 or (x == z and y == z) for (x, y, z), prob in joint.items())


def provenance_compatible(source: Token, target: Token) -> bool:
    """Structural token identity, deliberately stricter than fact identity."""
    return (
        source.provenance == target.provenance
        and source.occurred == target.occurred
        and source.available == target.available
    )


# ---------------------------------------------------------------------------
# Finite effective descent
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class DescentResult:
    verdict: str
    coherent_families: int
    gauge_orbits: int
    representative_stabilizer: int
    injective_colimit: bool


def _family_key(fam: Mapping[Tuple[int, int], Perm], n_charts: int) -> Tuple[Perm, ...]:
    return tuple(fam[(a, b)] for a in range(n_charts) for b in range(n_charts) if a != b)


def _check_family(fam: Mapping[Tuple[int, int], Perm], token_sizes: Sequence[int]) -> bool:
    n = len(token_sizes)
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if inverse_perm(fam[(a, b)]) != fam[(b, a)]:
                return False
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if len({a, b, c}) < 3:
                    continue
                # phi_ab after phi_bc equals phi_ac, all maps c -> a
                if compose_perm(fam[(a, b)], fam[(b, c)]) != fam[(a, c)]:
                    return False
    return True


def enumerate_coherent_families(
    token_sizes: Sequence[int],
    phi: Mapping[Tuple[int, int], Sequence[Perm]],
) -> Tuple[Dict[Tuple[int, int], Perm], ...]:
    n = len(token_sizes)
    edges = [(a, b) for a in range(n) for b in range(n) if a != b]
    if any(not phi.get(edge) for edge in edges):
        return ()
    out: List[Dict[Tuple[int, int], Perm]] = []
    choices = [tuple(phi[e]) for e in edges]
    for selected in product(*choices):
        fam = dict(zip(edges, selected))
        if _check_family(fam, token_sizes):
            out.append(fam)
    return tuple(out)


def gauge_transform(
    fam: Mapping[Tuple[int, int], Perm],
    gauges: Sequence[Perm],
) -> Dict[Tuple[int, int], Perm]:
    out: Dict[Tuple[int, int], Perm] = {}
    n = len(gauges)
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            out[(a, b)] = compose_perm(
                gauges[a], compose_perm(fam[(a, b)], inverse_perm(gauges[b]))
            )
    return out


def _in_phi(fam: Mapping[Tuple[int, int], Perm], phi: Mapping[Tuple[int, int], Sequence[Perm]]) -> bool:
    return all(fam[e] in tuple(phi[e]) for e in fam)


def _is_permutation(p: Perm, size: int) -> bool:
    return len(p) == size and set(p) == set(range(size))


def descent_data_errors(
    token_sizes: Sequence[int],
    phi: Mapping[Tuple[int, int], Sequence[Perm]],
    automorphisms: Sequence[Sequence[Perm]],
) -> Tuple[str, ...]:
    """Validate the group action required by the descent classification.

    Empty required pairs are a pre-registered ABSENT-PAIR outcome and are
    handled before this validator. All nonempty data must be typed bijections;
    each automorphism family must be a group; candidate maps must be closed
    under inverses and under independent endpoint gauge actions.
    """
    n = len(token_sizes)
    errors: List[str] = []
    if len(automorphisms) != n:
        return ("one automorphism family is required per chart",)

    aut_sets: List[set[Perm]] = []
    automorphisms_are_groups = True
    for a, (size, declared) in enumerate(zip(token_sizes, automorphisms)):
        group = set(declared)
        aut_sets.append(group)
        if not group:
            errors.append(f"chart {a}: empty automorphism family")
            automorphisms_are_groups = False
            continue
        if any(not _is_permutation(g, size) for g in group):
            errors.append(f"chart {a}: ill-typed automorphism")
            automorphisms_are_groups = False
            continue
        ident = identity_perm(size)
        if ident not in group:
            errors.append(f"chart {a}: automorphisms omit identity")
            automorphisms_are_groups = False
        if any(inverse_perm(g) not in group for g in group):
            errors.append(f"chart {a}: automorphisms not inverse-closed")
            automorphisms_are_groups = False
        if any(compose_perm(g, h) not in group for g in group for h in group):
            errors.append(f"chart {a}: automorphisms not composition-closed")
            automorphisms_are_groups = False

    edges = [(a, b) for a in range(n) for b in range(n) if a != b]
    for a, b in edges:
        candidates = tuple(phi.get((a, b), ()))
        if any(
            token_sizes[a] != token_sizes[b]
            or not _is_permutation(p, token_sizes[b])
            for p in candidates
        ):
            errors.append(f"edge {(a, b)}: candidate is not a typed bijection")
            continue
        reverse = set(phi.get((b, a), ()))
        if any(inverse_perm(p) not in reverse for p in candidates):
            errors.append(f"edge {(a, b)}: candidates not inverse-closed")
        if not automorphisms_are_groups:
            continue
        for p in candidates:
            for ga in aut_sets[a]:
                for gb in aut_sets[b]:
                    moved = compose_perm(ga, compose_perm(p, inverse_perm(gb)))
                    if moved not in candidates:
                        errors.append(f"edge {(a, b)}: candidate set not gauge-closed")
                        break
                if errors and errors[-1].startswith(f"edge {(a, b)}: candidate set"):
                    break
            if errors and errors[-1].startswith(f"edge {(a, b)}: candidate set"):
                break
    return tuple(dict.fromkeys(errors))


def _colimit_injective(
    token_sizes: Sequence[int], fam: Mapping[Tuple[int, int], Perm]
) -> bool:
    """Build the finite colimit equivalence relation and test each chart injects."""
    offsets = []
    total = 0
    for size in token_sizes:
        offsets.append(total)
        total += size
    parent = list(range(total))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    n = len(token_sizes)
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            p = fam[(a, b)]  # b -> a
            for x in range(token_sizes[b]):
                union(offsets[b] + x, offsets[a] + p[x])

    for a, size in enumerate(token_sizes):
        roots = [find(offsets[a] + x) for x in range(size)]
        if len(set(roots)) != size:
            return False
    return True


def solve_descent(
    token_sizes: Sequence[int],
    phi: Mapping[Tuple[int, int], Sequence[Perm]],
    automorphisms: Sequence[Sequence[Perm]],
) -> DescentResult:
    n = len(token_sizes)
    edges = [(a, b) for a in range(n) for b in range(n) if a != b]
    if any(not phi.get(e) for e in edges):
        return DescentResult("ABSENT-PAIR", 0, 0, 0, False)

    errors = descent_data_errors(token_sizes, phi, automorphisms)
    if errors:
        raise ValueError("invalid descent data: " + "; ".join(errors))

    families = enumerate_coherent_families(token_sizes, phi)
    if not families:
        return DescentResult("NO-DESCENT", 0, 0, 0, False)

    by_key = {_family_key(f, n): f for f in families}
    unseen = set(by_key)
    orbits: List[set] = []
    all_gauges = tuple(product(*[tuple(a) for a in automorphisms]))
    while unseen:
        seed = next(iter(unseen))
        orbit = set()
        frontier = [seed]
        while frontier:
            key = frontier.pop()
            if key in orbit:
                continue
            orbit.add(key)
            fam = by_key[key]
            for gs in all_gauges:
                moved = gauge_transform(fam, gs)
                if _in_phi(moved, phi) and _check_family(moved, token_sizes):
                    mkey = _family_key(moved, n)
                    if mkey in by_key and mkey not in orbit:
                        frontier.append(mkey)
        unseen -= orbit
        orbits.append(orbit)

    rep = families[0]
    stabilizer = 0
    for gs in all_gauges:
        moved = gauge_transform(rep, gs)
        if _family_key(moved, n) == _family_key(rep, n):
            stabilizer += 1

    injective = _colimit_injective(token_sizes, rep)
    if len(orbits) > 1:
        verdict = "UNDERDETERMINED"
    elif stabilizer > 1:
        verdict = "GROUPOID-AMALGAM"
    else:
        verdict = "SET-AMALGAM"
    return DescentResult(verdict, len(families), len(orbits), stabilizer, injective)


def canonical_maps(
    candidates: Sequence[Perm], aut_target: Sequence[Perm], aut_source: Sequence[Perm]
) -> Tuple[Perm, ...]:
    """Candidate identifications fixed under every independent chart automorphism.

    A canonical identification cannot change when either copy is re-presented by
    an automorphism. Thus g f h^{-1}=f for all g,h.
    """
    out = []
    for f in candidates:
        if all(
            compose_perm(g, compose_perm(f, inverse_perm(h))) == f
            for g in aut_target
            for h in aut_source
        ):
            out.append(f)
    return tuple(out)
