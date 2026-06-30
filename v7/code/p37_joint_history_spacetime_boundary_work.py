#!/usr/bin/env python3
"""Paper 37 finite receipt.

Exact finite audit for the algebraic claim:

    a joint click-plus-GR boundary-work functional selects the coarsest
    non-reconstructive history panel sufficient for both the future click and
    the finite spacetime readout.

This is a theorem-pattern receipt, not a physical record-law derivation.
All arithmetic is exact Fraction arithmetic.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product


FIELDS = ("a", "b", "c", "d")


def build_histories():
    histories = []
    for idx, bits in enumerate(product((0, 1), repeat=len(FIELDS))):
        h = dict(zip(FIELDS, bits))
        h["id"] = idx
        # The future click needs the older a,b part of the history.
        h["S"] = h["a"] ^ h["b"]
        # The finite GR packet needs a,c; b is click-only and d is irrelevant.
        h["G"] = (h["a"], h["c"])
        histories.append(h)
    return histories


def powerset_fields():
    for r in range(len(FIELDS) + 1):
        for combo in combinations(FIELDS, r):
            yield combo


def key_for(fields, h):
    return tuple(h[f] for f in fields)


def conditional_distributions(histories, fields, target):
    counts = defaultdict(lambda: defaultdict(int))
    totals = defaultdict(int)
    for h in histories:
        key = key_for(fields, h)
        counts[key][h[target]] += 1
        totals[key] += 1
    dists = {}
    for key, row in counts.items():
        total = totals[key]
        dists[key] = {value: Fraction(count, total) for value, count in row.items()}
    return dists


def expected_delta_tv(histories, fields, target):
    """E TV(delta_target(H), Law(target | panel))."""
    dists = conditional_distributions(histories, fields, target)
    n = len(histories)
    total = Fraction(0, 1)
    for h in histories:
        key = key_for(fields, h)
        total += Fraction(1, 1) - dists[key].get(h[target], Fraction(0, 1))
    return total / n


def cell_count(histories, fields):
    return len({key_for(fields, h) for h in histories})


def action(histories, fields, click_weight=Fraction(1, 1), geom_weight=Fraction(1, 1),
           complexity_weight=Fraction(1, 100)):
    click = expected_delta_tv(histories, fields, "S")
    geom = expected_delta_tv(histories, fields, "G")
    complexity = Fraction(cell_count(histories, fields), len(histories))
    return click_weight * click + geom_weight * geom + complexity_weight * complexity


def fmt(fr):
    return f"{fr.numerator}/{fr.denominator} = {float(fr):.12f}"


def main():
    histories = build_histories()
    rows = []
    for fields in powerset_fields():
        rows.append(
            {
                "fields": fields,
                "cells": cell_count(histories, fields),
                "click": expected_delta_tv(histories, fields, "S"),
                "geom": expected_delta_tv(histories, fields, "G"),
                "total": action(histories, fields),
            }
        )

    click_only = min(rows, key=lambda r: (r["click"] + Fraction(1, 100) * Fraction(r["cells"], len(histories)), r["cells"]))
    geom_only = min(rows, key=lambda r: (r["geom"] + Fraction(1, 100) * Fraction(r["cells"], len(histories)), r["cells"]))
    total = min(rows, key=lambda r: (r["total"], r["cells"]))
    full = next(r for r in rows if r["fields"] == FIELDS)
    abc = next(r for r in rows if r["fields"] == ("a", "b", "c"))

    print("P37 joint history-spacetime boundary-work receipt")
    print(f"histories = {len(histories)}")
    print()
    print("best click-only panel:")
    print(click_only)
    print("best geometry-only panel:")
    print(geom_only)
    print("best joint panel:")
    print(total)
    print("full reconstructive panel:")
    print(full)
    print()

    checks = []
    checks.append(("click-only uses a,b", click_only["fields"] == ("a", "b")))
    checks.append(("geometry-only uses a,c", geom_only["fields"] == ("a", "c")))
    checks.append(("joint uses a,b,c", total["fields"] == ("a", "b", "c")))
    checks.append(("joint click residual zero", total["click"] == 0))
    checks.append(("joint geometry residual zero", total["geom"] == 0))
    checks.append(("full also sufficient", full["click"] == 0 and full["geom"] == 0))
    checks.append(("joint beats full by complexity", total["total"] < full["total"]))
    checks.append(("click-only not geometry sufficient", click_only["geom"] > 0))
    checks.append(("geometry-only not click sufficient", geom_only["click"] > 0))

    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
    if not all(ok for _, ok in checks):
        raise SystemExit(1)

    print()
    print("Exact residuals:")
    for name, row in (("click", click_only), ("geometry", geom_only), ("joint", total), ("full", full)):
        print(
            f"{name:8s} fields={row['fields']!s:18s} "
            f"click={fmt(row['click'])} geom={fmt(row['geom'])} total={fmt(row['total'])}"
        )
    print()
    print(f"CHECKS PASSED: {sum(ok for _, ok in checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
