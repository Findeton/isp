#!/usr/bin/env python3
"""Exact comparison of coherent and objective hard-seal finite rulebooks."""

from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "v10" / "data" / "d21-two-rulebook-discriminator-exact.json"
EXPECTED_CHECKS = 40
EXPECTED_SEMANTIC_SHA256 = "46f9e4ff8a6627f289a4786d2d5fd43c21e936c6a05f22c3e7a8a58be0c07533"
CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1
    print(f"PASS {CHECKS:03d}: {label}")


@dataclass(frozen=True)
class G:
    """Gaussian rational number re + i im."""

    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, G) else G(F(value), F(0))

    def __add__(self, other):
        other = self.coerce(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        denominator = other.re * other.re + other.im * other.im
        return G((self.re * other.re + self.im * other.im) / denominator,
                 (self.im * other.re - self.re * other.im) / denominator)

    def conj(self):
        return G(self.re, -self.im)


ZERO = G()
ONE = G(F(1))
IUNIT = G(F(0), F(1))


def matrix(rows):
    return tuple(tuple(G.coerce(value) for value in row) for row in rows)


def zero_matrix(n, m=None):
    m = n if m is None else m
    return tuple(tuple(ZERO for _ in range(m)) for _ in range(n))


def identity(n):
    return tuple(tuple(ONE if i == j else ZERO for j in range(n))
                 for i in range(n))


def madd(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))


def mscale(scalar, a):
    scalar = G.coerce(scalar)
    return tuple(tuple(scalar * value for value in row) for row in a)


def mmul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO)
                       for j in range(len(b[0])))
                 for i in range(len(a)))


def dagger(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def kron(a, b):
    return tuple(
        tuple(a[i][j] * b[k][ell]
              for j in range(len(a[0])) for ell in range(len(b[0])))
        for i in range(len(a)) for k in range(len(b))
    )


@lru_cache(maxsize=None)
def tensor(matrices):
    out = matrix(((1,),))
    for factor in matrices:
        out = kron(out, factor)
    return out


PAULI = {
    "I": identity(2),
    "X": matrix(((0, 1), (1, 0))),
    "Y": matrix(((0, -IUNIT), (IUNIT, 0))),
    "Z": matrix(((1, 0), (0, -1))),
}


@lru_cache(maxsize=None)
def projector(setting, outcome):
    return mscale(F(1, 2), madd(PAULI["I"], mscale(outcome, PAULI[setting])))


@lru_cache(maxsize=None)
def embed_local(operator, site):
    return tensor(tuple(operator if index == site else PAULI["I"]
                        for index in range(3)))


def rho(eta):
    eta = F(eta)
    rows = [list(row) for row in zero_matrix(8)]
    rows[0][0] = G(F(1, 2))
    rows[7][7] = G(F(1, 2))
    rows[0][7] = G(eta / 2)
    rows[7][0] = G(eta / 2)
    return tuple(tuple(row) for row in rows)


def post_hadamard_seed():
    """Density matrix after H on site 0 of |000>, kept Gaussian-rational."""
    rows = [list(row) for row in zero_matrix(8)]
    for i in (0, 4):
        for j in (0, 4):
            rows[i][j] = G(F(1, 2))
    return tuple(tuple(row) for row in rows)


def cnot(control, target):
    rows = [list(row) for row in zero_matrix(8)]
    for source in range(8):
        bits = [(source >> (2 - site)) & 1 for site in range(3)]
        if bits[control]:
            bits[target] ^= 1
        destination = sum(bits[site] << (2 - site) for site in range(3))
        rows[destination][source] = ONE
    return tuple(tuple(row) for row in rows)


def conjugate(operator, state):
    return mmul(mmul(operator, state), dagger(operator))


def expectation(state, operator):
    value = trace(mmul(state, operator))
    if value.im != 0:
        raise AssertionError(("non-real expectation", value))
    return value.re


@lru_cache(maxsize=None)
def joint_operator(settings, outcomes, order=(0, 1, 2)):
    out = identity(8)
    for site in order:
        out = mmul(out, embed_local(projector(settings[site], outcomes[site]), site))
    return out


@lru_cache(maxsize=None)
def probability(state, settings, outcomes, order=(0, 1, 2)):
    return expectation(state, joint_operator(settings, outcomes, order))


def pauli_expectation(state, word):
    return expectation(state, tensor(tuple(PAULI[letter] for letter in word)))


@lru_cache(maxsize=None)
def distribution(state, settings, order=(0, 1, 2)):
    return {outcomes: probability(state, settings, outcomes, order)
            for outcomes in product((-1, 1), repeat=3)}


def marginal(table, fixed):
    return sum((p for outcomes, p in table.items()
                if all(outcomes[site] == value for site, value in fixed.items())), F(0))


def conditional(table, past, site, value):
    denominator = marginal(table, past)
    if denominator <= 0:
        raise ZeroDivisionError((past, site, value))
    extended = dict(past)
    extended[site] = value
    return marginal(table, extended) / denominator


def purity(state):
    return expectation(state, state)


def dephase_site(state, site, setting="Z"):
    out = zero_matrix(8)
    for value in (-1, 1):
        effect = embed_local(projector(setting, value), site)
        out = madd(out, mmul(mmul(effect, state), effect))
    return out


def normalized_branch(state, effect):
    unnormalized = mmul(mmul(effect, state), effect)
    weight = trace(unnormalized)
    if weight.im != 0 or weight.re <= 0:
        raise ValueError(weight)
    return weight.re, mscale(F(1, 1) / weight.re, unnormalized)


def decoherence_matrix(state, settings):
    outcomes = tuple(product((-1, 1), repeat=3))
    projectors = tuple(joint_operator(settings, outcome) for outcome in outcomes)
    return tuple(tuple(trace(mmul(mmul(projectors[i], state), projectors[j]))
                       for j in range(8)) for i in range(8))


def main():
    coherent = rho(F(1))
    collapsed = rho(F(0))

    check(dagger(coherent) == coherent and dagger(collapsed) == collapsed,
          "both candidate density operators are exactly Hermitian")
    check(trace(coherent) == ONE and trace(collapsed) == ONE,
          "both candidate laws have exact unit trace")
    check(all((F(1) + eta) / 2 >= 0 and (F(1) - eta) / 2 >= 0
              for eta in (F(0), F(1))),
          "candidate spectra are nonnegative")
    check(purity(coherent) == 1 and purity(collapsed) == F(1, 2),
          "purity separates coherent rank-one and collapsed rank-two laws")
    check(mmul(coherent, coherent) == coherent
          and mmul(collapsed, collapsed) != collapsed,
          "Q is a pure source law while C is a genuine stochastic mixture")
    generated_q = conjugate(cnot(0, 2),
                            conjugate(cnot(0, 1), post_hadamard_seed()))
    check(generated_q == coherent,
          "Q is generated by an explicit two-interaction finite source circuit")
    check(coherent != collapsed,
          "the two complete finite history operators are inequivalent")

    pvm_ok = True
    for setting in "XYZ":
        plus = projector(setting, 1)
        minus = projector(setting, -1)
        pvm_ok &= mmul(plus, plus) == plus
        pvm_ok &= mmul(minus, minus) == minus
        pvm_ok &= mmul(plus, minus) == zero_matrix(2)
        pvm_ok &= madd(plus, minus) == identity(2)
    check(pvm_ok, "all local record instruments are exact orthogonal PVMs")
    check(dephase_site(coherent, 0, "Z") == collapsed,
          "C is generated from Q by an explicit local objective hard-seal channel")
    minus_effect = embed_local(projector("Z", -1), 0)
    plus_effect = embed_local(projector("Z", 1), 0)
    minus_weight, minus_branch = normalized_branch(coherent, minus_effect)
    plus_weight, plus_branch = normalized_branch(coherent, plus_effect)
    check(minus_weight == plus_weight == F(1, 2)
          and minus_branch[7][7] == ONE and trace(minus_branch) == ONE
          and plus_branch[0][0] == ONE and trace(plus_branch) == ONE
          and madd(mscale(minus_weight, minus_branch),
                   mscale(plus_weight, plus_branch)) == collapsed,
          "C prints its objective source variable, branch states and exact mixture")

    all_settings = tuple(product("XYZ", repeat=3))
    all_outcomes = tuple(product((-1, 1), repeat=3))
    for state, label in ((coherent, "Q"), (collapsed, "C")):
        normalized = all(sum(distribution(state, settings).values(), F(0)) == 1
                         for settings in all_settings)
        nonnegative = all(min(distribution(state, settings).values()) >= 0
                          for settings in all_settings)
        check(normalized, f"{label} normalizes for every local setting triple")
        check(nonnegative, f"{label} assigns no negative record probability")

    local_commutation = True
    for first, second in ((0, 1), (0, 2), (1, 2)):
        for s1, s2 in product("XYZ", repeat=2):
            for a1, a2 in product((-1, 1), repeat=2):
                p1 = embed_local(projector(s1, a1), first)
                p2 = embed_local(projector(s2, a2), second)
                local_commutation &= mmul(p1, p2) == mmul(p2, p1)
    check(local_commutation, "spacelike local record instruments commute exactly")

    # Exhaustive pairwise commutation proves permutation invariance for every
    # triple.  Explicitly exercise all six serializations on a dense complex
    # generator triple as a reconstruction guard.
    generator_settings = ("X", "Y", "X")
    generator_outcomes = (1, -1, 1)
    generator_operators = {
        joint_operator(generator_settings, generator_outcomes, order)
        for order in permutations(range(3))
    }
    check(len(generator_operators) == 1,
          "all six generator serializations agree; exhaustive commutation lifts the result")

    no_signalling = True
    for state in (coherent, collapsed):
        for settings in all_settings:
            table = distribution(state, settings)
            for site in range(3):
                for outcome in (-1, 1):
                    local = marginal(table, {site: outcome})
                    alternatives = []
                    for remote_settings in all_settings:
                        if remote_settings[site] == settings[site]:
                            alternatives.append(marginal(distribution(state, remote_settings),
                                                         {site: outcome}))
                    no_signalling &= all(value == local for value in alternatives)
    check(no_signalling, "every one-site marginal is remote-setting independent")

    pair_no_signalling = True
    for state in (coherent, collapsed):
        for sites in ((0, 1), (0, 2), (1, 2)):
            remote = ({0, 1, 2} - set(sites)).pop()
            for local_settings in product("XYZ", repeat=2):
                tables = []
                for remote_setting in "XYZ":
                    settings = [None, None, None]
                    settings[sites[0]], settings[sites[1]] = local_settings
                    settings[remote] = remote_setting
                    tables.append(distribution(state, tuple(settings)))
                for values in product((-1, 1), repeat=2):
                    fixed = dict(zip(sites, values))
                    pair_no_signalling &= len({marginal(table, fixed) for table in tables}) == 1
    check(pair_no_signalling, "every two-site marginal is remote-setting independent")

    proper_words = tuple(word for word in product("IXYZ", repeat=3)
                         if "I" in word)
    check(all(pauli_expectation(coherent, word) == pauli_expectation(collapsed, word)
              for word in proper_words),
          "every proper-subsystem Pauli observable agrees")
    check(len(proper_words) == 37,
          "proper-subsystem observable census is complete")

    for subset in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
        complement = tuple(site for site in range(3) if site not in subset)
        equal = True
        for settings in all_settings:
            q_table = distribution(coherent, settings)
            c_table = distribution(collapsed, settings)
            for values in product((-1, 1), repeat=len(subset)):
                fixed = dict(zip(subset, values))
                equal &= marginal(q_table, fixed) == marginal(c_table, fixed)
        check(equal, f"all {len(subset)}-record marginals agree for subset {subset}")

    zq = distribution(coherent, ("Z", "Z", "Z"))
    zc = distribution(collapsed, ("Z", "Z", "Z"))
    check(zq == zc,
          "the complete computational-record distribution agrees")
    check(zq[(-1, -1, -1)] == F(1, 2)
          and zq[(1, 1, 1)] == F(1, 2)
          and sum(p for outcome, p in zq.items()
                  if outcome not in ((-1, -1, -1), (1, 1, 1))) == 0,
          "both Z-record laws contain exactly two equally weighted histories")
    check(conditional(zq, {0: 1}, 1, 1) == 1
          and conditional(zc, {0: 1}, 1, 1) == 1,
          "positive Z next-click conditionals agree after one record")
    check(conditional(zq, {0: 1, 1: 1}, 2, 1) == 1
          and conditional(zc, {0: 1, 1: 1}, 2, 1) == 1,
          "positive Z next-click conditionals agree after two records")

    history_conditionals_complete = True
    for state in (coherent, collapsed):
        for settings in all_settings:
            table = distribution(state, settings)
            for order in permutations(range(3)):
                for depth in range(3):
                    past_sites = order[:depth]
                    next_site = order[depth]
                    for values in product((-1, 1), repeat=depth):
                        past = dict(zip(past_sites, values))
                        if marginal(table, past) > 0:
                            total = sum((conditional(table, past, next_site, value)
                                         for value in (-1, 1)), F(0))
                            history_conditionals_complete &= total == 1
    check(history_conditionals_complete,
          "every positive finite past supplies a normalized next-record conditional")

    for state, label in ((coherent, "Q"), (collapsed, "C")):
        dmatrix = decoherence_matrix(state, ("X", "Y", "Z"))
        diagonal = all(dmatrix[i][j] == ZERO for i in range(8) for j in range(8)
                       if i != j)
        nonnegative_diagonal = all(dmatrix[i][i].im == 0 and dmatrix[i][i].re >= 0
                                   for i in range(8))
        check(diagonal and nonnegative_diagonal,
              f"{label} sealed outcome histories form a positive decoherent sector")

    mermin_words = ((1, "XXX"), (-1, "XYY"), (-1, "YXY"), (-1, "YYX"))

    def mermin(state):
        return sum((coefficient * pauli_expectation(state, word)
                    for coefficient, word in mermin_words), F(0))

    check(pauli_expectation(coherent, "XXX") == 1
          and pauli_expectation(collapsed, "XXX") == 0,
          "preregistered XXX closed-history discriminator separates Q and C")
    check(mermin(coherent) == 4 and mermin(collapsed) == 0,
          "preregistered Mermin discriminator is exactly 4 versus 0")

    interpolation_ok = True
    lower_shadow_ok = True
    for eta in (F(0), F(1, 7), F(1, 3), F(3, 4), F(1)):
        state = rho(eta)
        interpolation_ok &= mermin(state) == 4 * eta
        interpolation_ok &= pauli_expectation(state, "XXX") == eta
        lower_shadow_ok &= all(pauli_expectation(state, word)
                               == pauli_expectation(collapsed, word)
                               for word in proper_words)
    check(interpolation_ok, "the exact scale family obeys <M>=4 eta and <XXX>=eta")
    check(lower_shadow_ok, "all proper-subsystem shadows are eta-independent")

    xq = distribution(coherent, ("X", "X", "X"))
    xc = distribution(collapsed, ("X", "X", "X"))
    check(all(xq[outcome] == F(1 + outcome[0] * outcome[1] * outcome[2], 8)
              and xc[outcome] == F(1, 8) for outcome in all_outcomes),
          "XXX outcome law is exact parity support versus uniform support")
    check(conditional(xq, {0: 1, 1: 1}, 2, 1) == 1
          and conditional(xc, {0: 1, 1: 1}, 2, 1) == F(1, 2),
          "conditioning on two X records exposes complete-support correlation")

    check(CHECKS + 1 == EXPECTED_CHECKS, "pre-final exact check count is frozen")
    if CHECKS != EXPECTED_CHECKS:
        raise AssertionError((CHECKS, EXPECTED_CHECKS))

    semantic = {
        "schema": "d21-two-rulebook-discriminator-exact-v1",
        "scope": "three spacelike binary record instruments on a fixed finite source carrier",
        "checks_passed": CHECKS,
        "candidate_q_purity": "1",
        "candidate_c_purity": "1/2",
        "shared_proper_pauli_observables": len(proper_words),
        "xxx_q": "1",
        "xxx_c": "0",
        "mermin_q": "4",
        "mermin_c": "0",
        "verdict": "FINITE-COMPLETE-RULEBOOK-DISCRIMINATOR",
        "ceiling": "complete fixed-carrier instrument laws, not complete cosmological generators",
    }
    semantic_bytes = json.dumps(semantic, sort_keys=True,
                                separators=(",", ":")).encode()
    semantic_hash = sha256(semantic_bytes).hexdigest()
    if (EXPECTED_SEMANTIC_SHA256 != "TO_BE_FROZEN"
            and semantic_hash != EXPECTED_SEMANTIC_SHA256):
        raise AssertionError((semantic_hash, EXPECTED_SEMANTIC_SHA256))
    packet = dict(semantic)
    packet.update({
        "semantic_sha256": semantic_hash,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    })
    OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(f"CHECKS PASSED: {CHECKS}/{EXPECTED_CHECKS}")
    print(f"SEMANTIC SHA256: {semantic_hash}")
    print(f"SOURCE SHA256: {packet['source_sha256']}")
    print("VERDICT: FINITE-COMPLETE-RULEBOOK-DISCRIMINATOR")


if __name__ == "__main__":
    main()
