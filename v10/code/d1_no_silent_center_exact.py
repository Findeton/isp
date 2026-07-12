#!/usr/bin/env python3
"""D1: exact no-silent center and support-birth census.

All probability gates use integer counts and exact cross products.  Python's
standard-library Decimal arithmetic at precision=120 is used only to report
conditional mutual information.  No external environment or package is
required.  Partitions are canonical restricted-growth strings over occupied
boundary atoms.
"""

from decimal import Decimal, getcontext, localcontext
from itertools import permutations, product

getcontext().prec = 120

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def canon(labels):
    """Canonicalize arbitrary finite labels to a restricted-growth string."""
    remap = {}
    out = []
    for x in labels:
        if x not in remap:
            remap[x] = len(remap)
        out.append(remap[x])
    return tuple(out)


def partitions_rgs(n):
    """All set partitions of range(n), as canonical RGS tuples."""
    if n == 0:
        yield ()
        return

    seq = [0]

    def rec(pos, current_max):
        if pos == n:
            yield tuple(seq)
            return
        for lab in range(current_max + 2):
            seq.append(lab)
            yield from rec(pos + 1, max(current_max, lab))
            seq.pop()

    yield from rec(1, 0)


def refines(fine, coarse):
    """True iff every fine cell is contained in a coarse cell."""
    if len(fine) != len(coarse):
        return False
    seen = {}
    for f, c in zip(fine, coarse):
        if f in seen and seen[f] != c:
            return False
        seen[f] = c
    return True


def nblocks(p):
    return 0 if not p else max(p) + 1


def outer(u, v):
    return [[int(a * b) for b in v] for a in u]


def sum_mats(mats):
    nx = len(mats[0])
    nz = len(mats[0][0])
    return [[sum(m[x][z] for m in mats) for z in range(nz)]
            for x in range(nx)]


def matrix_rank1_exact(mat):
    """Nonnegative matrix has rank <=1 by vanishing all 2x2 minors."""
    nx = len(mat)
    nz = len(mat[0])
    for x1 in range(nx):
        for x2 in range(x1 + 1, nx):
            for z1 in range(nz):
                for z2 in range(z1 + 1, nz):
                    if (mat[x1][z1] * mat[x2][z2]
                            != mat[x1][z2] * mat[x2][z1]):
                        return False
    return True


def normalized_exact(tables):
    return all(v >= 0 for m in tables for row in m for v in row) \
        and all(sum(sum(row) for row in m) > 0 for m in tables) \
        and sum(v for m in tables for row in m for v in row) > 0


def strictly_positive(tables):
    return all(v > 0 for m in tables for row in m for v in row)


def complete(tables, partition):
    """Exact X independent Z conditional on the boundary partition."""
    for cell in range(nblocks(partition)):
        ids = [i for i, c in enumerate(partition) if c == cell]
        if not matrix_rank1_exact(sum_mats([tables[i] for i in ids])):
            return False
    return True


def admissible_partitions(tables, screen):
    return [p for p in partitions_rgs(len(tables)) if refines(p, screen)]


def complete_partitions(tables, screen):
    return [p for p in admissible_partitions(tables, screen)
            if complete(tables, p)]


def minimal_complete_partitions(tables, screen):
    comps = complete_partitions(tables, screen)
    mins = []
    for p in comps:
        has_strict_complete_coarsening = any(
            q != p and refines(p, q) for q in comps
        )
        if not has_strict_complete_coarsening:
            mins.append(p)
    return sorted(mins)


def cmi(tables, partition):
    """Conditional mutual information in nats, for reporting only."""
    total = sum(v for m in tables for row in m for v in row)
    with localcontext() as ctx:
        ctx.prec = 120
        ans = Decimal(0)
        for cell in range(nblocks(partition)):
            ids = [i for i, c in enumerate(partition) if c == cell]
            mat = sum_mats([tables[i] for i in ids])
            nc = sum(sum(row) for row in mat)
            rows = [sum(row) for row in mat]
            cols = [sum(mat[x][z] for x in range(len(mat)))
                    for z in range(len(mat[0]))]
            for x, row in enumerate(mat):
                for z, val in enumerate(row):
                    if val:
                        ratio = (Decimal(val) * Decimal(nc)) / (
                            Decimal(rows[x]) * Decimal(cols[z])
                        )
                        ans += (Decimal(val) / Decimal(total)) * ratio.ln()
        return +ans


def fmt(x):
    if abs(x) < Decimal("1e-110"):
        return "0"
    return format(x, ".42g")


def partition_blocks(p):
    return tuple(tuple(i for i, c in enumerate(p) if c == lab)
                 for lab in range(nblocks(p)))


def transport_partition_from_permuted(p_new, perm):
    """perm[new_index]=old_index; return partition on old indices."""
    labels_old = [None] * len(perm)
    for new_i, old_i in enumerate(perm):
        labels_old[old_i] = p_new[new_i]
    return canon(labels_old)


def covariance_ok(tables, screen):
    base = set(minimal_complete_partitions(tables, screen))
    n = len(tables)
    if n <= 4:
        perms = list(permutations(range(n)))
    else:
        # Reversal and a full cycle generate the dihedral subgroup used as the
        # executable check at n=8. General partition transport covariance is
        # proved by reindexing the defining sums; the paper scopes this test.
        perms = [tuple(reversed(range(n))),
                 tuple(list(range(1, n)) + [0])]
    for perm in perms:
        t2 = [tables[i] for i in perm]
        s2 = canon([screen[i] for i in perm])
        got = {
            transport_partition_from_permuted(p, perm)
            for p in minimal_complete_partitions(t2, s2)
        }
        if got != base:
            return False

    # Outcome relabelings cannot change a boundary-partition verdict.
    tx = [[row[:] for row in reversed(m)] for m in tables]
    if set(minimal_complete_partitions(tx, screen)) != base:
        return False
    tz = [[list(reversed(row)) for row in m] for m in tables]
    if set(minimal_complete_partitions(tz, screen)) != base:
        return False
    return True


class Scenario:
    def __init__(self, name, tables, screen, support, parents, note):
        self.name = name
        self.tables = tables
        self.screen = canon(screen)
        self.support = tuple(support)
        self.parents = tuple(parents)
        self.note = note


def repeat(mat, n):
    return [[row[:] for row in mat] for _ in range(n)]


def build_scenarios():
    scenarios = []

    # S0: product law; boundary nuisance is irrelevant.
    scenarios.append(Scenario(
        "S0-factorized", repeat(outer([2, 1], [3, 1]), 4),
        [0, 0, 0, 0], ("A", "B"), (),
        "truly factorized disconnected control"))

    # S1: mixture over visible Y is dependent, but each Y-cell is product.
    y0 = outer([3, 1], [3, 1])
    y1 = outer([1, 3], [1, 3])
    scenarios.append(Scenario(
        "S1-complete-screen", repeat(y0, 2) + repeat(y1, 2),
        [0, 0, 1, 1], ("A", "B"), (),
        "visible screen carries the complete common cause"))

    # S2: B=(Y,H,N), N duplicate nuisance.  Cells may not mix H exactly.
    mats_yh = [
        outer([3, 1], [3, 1]),
        outer([1, 3], [1, 3]),
        outer([4, 1], [1, 4]),
        outer([1, 4], [4, 1]),
    ]
    s2_tables = []
    s2_screen = []
    for yh, mat in enumerate(mats_yh):
        y = yh // 2
        for _n in range(2):
            s2_tables.append([row[:] for row in mat])
            s2_screen.append(y)
    scenarios.append(Scenario(
        "S2-unique-nonlookup", s2_tables, s2_screen,
        ("A", "B"), ("lower", "upper"),
        "unique (Y,H) center forgets nuisance N"))

    # S3: common ancestor H plus nuisance N, visible screen constant.
    h0 = outer([3, 1], [4, 1])
    h1 = outer([1, 3], [1, 4])
    scenarios.append(Scenario(
        "S3-common-ancestor", repeat(h0, 2) + repeat(h1, 2),
        [0, 0, 0, 0], ("A", "B"), ("root",),
        "recorded ancestor is the minimal joint center"))

    # S4: X=(A,B) has four values; Z=C.  A supplied common-root field H closes
    # the cut; this probability table does not prove an irreducible event.
    t40 = outer([4, 1, 1, 1], [3, 1])
    t41 = outer([1, 1, 1, 4], [1, 3])
    scenarios.append(Scenario(
        "S4-common-root-three-variable", repeat(t40, 2) + repeat(t41, 2),
        [0, 0, 0, 0], ("A", "B", "C"), ("root",),
        "supplied three-record common-root cut with shared H and nuisance N"))

    # S5: robust strictly positive adversary supplied by hostile referee B.
    # Every atomic B-cell is itself rank one and has equal mass 25. Two
    # incomparable three-cell minima remain complete under every refinement;
    # block count and center entropy tie and cannot select between them.
    s5 = [
        [[16, 4], [4, 1]],
        [[3, 2], [12, 8]],
        [[1, 4], [4, 16]],
        [[2, 8], [3, 12]],
    ]
    scenarios.append(Scenario(
        "S5-competing-centers", s5, [0, 0, 0, 0],
        ("A", "B"), (),
        "strictly positive refinement-stable tied minimal separators"))

    # S6: each singleton boundary table is product, while every union of two
    # or more frozen tables has rank two.  Full boundary lookup is the only
    # complete partition.
    s6 = [
        outer([1, 1], [1, 1]),
        outer([1, 2], [1, 3]),
        outer([2, 1], [3, 1]),
        outer([1, 3], [2, 1]),
    ]
    scenarios.append(Scenario(
        "S6-lookup-only", s6, [0, 0, 0, 0],
        ("A", "B"), (),
        "only singleton boundary lookup closes every cell"))

    # S7: even singleton boundary cells contain a dependent matrix.
    s7mat = [[2, 1], [1, 2]]
    scenarios.append(Scenario(
        "S7-no-boundary-center", repeat(s7mat, 3), [0, 0, 0],
        ("A", "B"), (),
        "dependence remains after conditioning on complete boundary"))

    return scenarios


def marginalize_x(tables, mapping, nx_new):
    out = []
    for mat in tables:
        nz = len(mat[0])
        new = [[0 for _ in range(nz)] for _ in range(nx_new)]
        for x, row in enumerate(mat):
            for z, v in enumerate(row):
                new[mapping[x]][z] += v
        out.append(new)
    return out


def scenario_report(s):
    mins = minimal_complete_partitions(s.tables, s.screen)
    comps = complete_partitions(s.tables, s.screen)
    print(f"\n[{s.name}] {s.note}")
    print(f"  support={s.support} parents={s.parents}")
    print(f"  boundary_atoms={len(s.tables)} screen={partition_blocks(s.screen)}")
    print(f"  exact_screen_complete={complete(s.tables, s.screen)} "
          f"CMI_screen={fmt(cmi(s.tables, s.screen))}")
    print(f"  complete_partitions={len(comps)} minimal={len(mins)}")
    for p in mins:
        print(f"  minimal blocks={partition_blocks(p)} cells={nblocks(p)} "
              f"lookup={nblocks(p) == len(s.tables)} CMI={fmt(cmi(s.tables, p))}")
    if not mins:
        print("  minimal=NONE")
    return mins, comps


print("D1 EXACT NO-SILENT CENTER CENSUS")
print("arithmetic=integer exact gates; CMI=stdlib Decimal precision=120 report")

scenarios = build_scenarios()
results = {}

for s in scenarios:
    check(f"G0 {s.name} nonnegative nonzero rational table",
          normalized_exact(s.tables))
    mins, comps = scenario_report(s)
    results[s.name] = (s, mins, comps)
    check(f"covariance {s.name}", covariance_ok(s.tables, s.screen))
    exact_cmi_agree = (complete(s.tables, s.screen)
                       == (abs(cmi(s.tables, s.screen)) < Decimal("1e-100")))
    check(f"G8 exact/CMI screen agreement {s.name}", exact_cmi_agree)
    check(f"G8 exact/CMI minimal agreement {s.name}",
          all(abs(cmi(s.tables, p)) < Decimal("1e-100") for p in mins))

# Registered scenario gates.
s0, m0, _ = results["S0-factorized"]
check("G1 factorized control refuses promotion",
      complete(s0.tables, s0.screen) and m0 == [s0.screen])

s1, m1, _ = results["S1-complete-screen"]
constant1 = tuple(0 for _ in s1.screen)
check("G2 S1 is dependent before Y but complete at Y",
      not complete(s1.tables, constant1)
      and complete(s1.tables, s1.screen) and m1 == [s1.screen])

s2, m2, _ = results["S2-unique-nonlookup"]
check("G3 S2 unique minimal nonlookup center",
      len(m2) == 1 and m2[0] != s2.screen
      and nblocks(m2[0]) < len(s2.tables),
      f"minimal={len(m2)} cells={nblocks(m2[0]) if m2 else 'NA'}")

s3, m3, _ = results["S3-common-ancestor"]
s4, m4, _ = results["S4-common-root-three-variable"]
check("G4 supplied common-root cells have unique nonlookup centers",
      len(m3) == 1 and len(m4) == 1
      and nblocks(m3[0]) < len(s3.tables)
      and nblocks(m4[0]) < len(s4.tables)
      and bool(s3.parents) and len(s4.support) == 3)

s5, m5, _ = results["S5-competing-centers"]
incomparable_pairs = [
    (a, b) for i, a in enumerate(m5) for b in m5[i + 1:]
    if not refines(a, b) and not refines(b, a)
]
check("G5 competing incomparable minimal centers exhibited",
      len(m5) >= 2 and bool(incomparable_pairs),
      f"minimal={len(m5)} incomparable_pairs={len(incomparable_pairs)}")
check("G5 robust positivity/refinement/cardinality/entropy tie",
      strictly_positive(s5.tables)
      and all(matrix_rank1_exact(m) for m in s5.tables)
      and len(m5) == 2
      and len({nblocks(p) for p in m5}) == 1
      and all(sorted(sum(sum(row) for row in sum_mats(
          [s5.tables[i] for i, c in enumerate(p) if c == cell]))
          for cell in range(nblocks(p))) == [25, 25, 50] for p in m5),
      "all atoms rank1/mass25; minima have cell masses 25,25,50")

s6, m6, _ = results["S6-lookup-only"]
s7, m7, _ = results["S7-no-boundary-center"]
check("G6 lookup-only and no-boundary-center refusals",
      len(m6) == 1 and nblocks(m6[0]) == len(s6.tables) and len(m7) == 0)

# Target-marginalization positive: S4 X=(A,B) -> A retains the same H center.
# Encoding x=0,1,2,3 follows (A,B)=(00,01,10,11); A=x//2.
s4_to_a = marginalize_x(s4.tables, [0, 0, 1, 1], 2)
m4a = minimal_complete_partitions(s4_to_a, s4.screen)
print("\n[S8 target-marginalization and screen/grain classification]")
print(f"  S4 ABC center={list(map(partition_blocks, m4))}")
print(f"  S4 AC center ={list(map(partition_blocks, m4a))}")
restriction_positive = set(m4a) == set(m4)
check("G7a marginalizing one target port retains the center", restriction_positive)

# Restriction adversary 1: full X=(A,R), Z, center H; remove R.  A has the
# same distribution for both H values, so the restricted A,Z law is already
# independent and the minimal center disappears.
s8_tables = []
for h in (0, 1):
    zvec = [3, 1] if h == 0 else [1, 3]
    mat = [[0, 0] for _ in range(4)]
    for a in (0, 1):
        x = 2 * a + h
        mat[x] = zvec[:]
    s8_tables.extend(repeat(mat, 2))  # nuisance duplicate
s8_screen = (0, 0, 0, 0)
m8full = minimal_complete_partitions(s8_tables, s8_screen)
s8_to_a = marginalize_x(s8_tables, [0, 0, 1, 1], 2)
m8rest = minimal_complete_partitions(s8_to_a, s8_screen)
print(f"  center-loss full={list(map(partition_blocks, m8full))}")
print(f"  center-loss rest={list(map(partition_blocks, m8rest))}")
center_loss = (len(m8full) == 1 and m8full[0] != s8_screen
               and m8rest == [s8_screen])
check("G7b target marginalization can erase the need for a center", center_loss)

# Screen/grain adversary: the same boundary law is evaluated first with a
# visible copy of H and then with a constant visible screen.  This is not a
# restriction map: it changes which boundary field is declared visible.
s9_tables = [[row[:] for row in mat] for mat in s3.tables]
s9_full_screen = (0, 0, 1, 1)
s9_restricted_screen = (0, 0, 0, 0)
m9full = minimal_complete_partitions(s9_tables, s9_full_screen)
m9rest = minimal_complete_partitions(s9_tables, s9_restricted_screen)
print(f"  center-appearance full={list(map(partition_blocks, m9full))}")
print(f"  center-appearance rest={list(map(partition_blocks, m9rest))}")
center_appearance = (m9full == [canon(s9_full_screen)]
                     and len(m9rest) == 1
                     and m9rest[0] != canon(s9_restricted_screen))
check("G7c hiding a screen field can create center eligibility", center_appearance)

check("G7 distinct target-marginalization and screen-change effects are classified",
      restriction_positive and center_loss and center_appearance)

# Every minimal center is selected only by exact minimality.  S5 deliberately
# remains a set; no preference is inserted.
check("G9 no hidden selector among S5 minima",
      len(m5) >= 2 and all(complete(s5.tables, p) for p in m5))

# O1 / G10: support arity is not selected.  One strictly positive latent-H
# law for A,B,C is conditionally product given H (plus duplicated nuisance N).
# Every pair marginal and the three-way AB|C split therefore has the same
# unique minimal H-center.  No-silent eligibility alone licenses three pair
# edges and one hyperedge; it does not choose their decomposition.
print("\n[O1 support-arity census]")
a0, a1 = [3, 1], [1, 3]
b0, b1 = [4, 1], [1, 4]
c0, c1 = [5, 1], [1, 5]


def pair_candidate(u0, u1, v0, v1, third_sums):
    tabs = []
    for u, v, scale in ((u0, v0, third_sums[0]),
                        (u1, v1, third_sums[1])):
        mat = [[scale * x for x in row] for row in outer(u, v)]
        tabs.extend(repeat(mat, 2))
    return tabs


ab_tabs = pair_candidate(a0, a1, b0, b1, (sum(c0), sum(c1)))
ac_tabs = pair_candidate(a0, a1, c0, c1, (sum(b0), sum(b1)))
bc_tabs = pair_candidate(b0, b1, c0, c1, (sum(a0), sum(a1)))

abc_tabs = []
for av, bv, cv in ((a0, b0, c0), (a1, b1, c1)):
    abvec = [av[a] * bv[b] for a in range(2) for b in range(2)]
    abc_tabs.extend(repeat(outer(abvec, cv), 2))

arity_candidates = {
    ("A", "B"): ab_tabs,
    ("A", "C"): ac_tabs,
    ("B", "C"): bc_tabs,
    ("AB", "C"): abc_tabs,
}

# The other two cuts of the same three-variable law.
acb_tabs = []
bac_tabs = []
for av, bv, cv in ((a0, b0, c0), (a1, b1, c1)):
    acvec = [av[a] * cv[c] for a in range(2) for c in range(2)]
    bavec = [bv[b] * cv[c] for b in range(2) for c in range(2)]
    acb_tabs.extend(repeat(outer(acvec, bv), 2))
    bac_tabs.extend(repeat(outer(bavec, av), 2))
arity_candidates[("AC", "B")] = acb_tabs
arity_candidates[("BC", "A")] = bac_tabs
arity_eligible = []
for support, tabs in arity_candidates.items():
    screen = (0, 0, 0, 0)
    mins = minimal_complete_partitions(tabs, screen)
    eligible = (not complete(tabs, screen) and len(mins) == 1
                and nblocks(mins[0]) < len(tabs))
    if eligible:
        arity_eligible.append(support)
    print(f"  support={support} residual={fmt(cmi(tabs, screen))} "
          f"minimal={list(map(partition_blocks, mins))} eligible={eligible}")

check("G10 cutwise no-silent eligibility does not select one support",
      len(arity_eligible) == 6
      and all(strictly_positive(t) for t in arity_candidates.values()),
      f"eligible={arity_eligible}")

print("\nD1 THEOREM BOUNDARY")
print("  positive: exact no-silent residue can identify a unique minimal center in scoped cells")
print("  refusal: minimal complete boundary centers are not unique in general")
print("  refusal: cutwise eligibility does not select one support from a supplied family")
print("  classification: target marginalization can retain or erase a center")
print("  classification: changing the visible screen is not record restriction")
print("  refusal: some seams close only by lookup; some do not close inside B")
print("  verdict: CENTER-NONSELECTION + SUPPORT-OVERELIGIBILITY")

TOTAL = PASS + FAIL
print(f"\nALL CHECKS PASS ({PASS}/{TOTAL})" if FAIL == 0
      else f"\nFAILURES ({FAIL}/{TOTAL})")
raise SystemExit(1 if FAIL else 0)
