#!/usr/bin/env python3
"""
Paper 28 receipt: pressure-density theorem boundary.

The previous Paper 28 receipt originally exposed a pressure opening:

    staged/fiber constructions can hide behind low-order checks unless
    their all-orders matching/free-energy growth is controlled.

This receipt attacks the pressure boundary.  It follows the Paper 27 opening that
raw matching tail is not the right final object.  The stronger object is the
pressure density

    p_N(D) = N^{-1} log Z_N(D; N),
    Z_N(D; z) = 1 + sum_{r>=2} q_r(D) z^r.

The audit checks three hostile facts:

  * pressure density separates the tested physical rank-copula kernels from
    fixed macroscopic staged blocks;
  * raw tail alone fails;
  * pure coherent Fourier modes can also be pressure-heavy, so pressure must
    be sectoral: geometry pressure after removing committed field/mark sectors.

This is not a proof of the pressure theorem.  It is a theorem-boundary audit:
it identifies what a correct theorem is allowed to say.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=36):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


print("=" * 80)
print("Paper 28 pressure-density theorem boundary audit")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

# Audited constants from Paper 27 pressure campaigns.
physical_c05_tail_sequence = [
    mp.mpf("0.649991484542364941"),
    mp.mpf("0.481323269700065294"),
    mp.mpf("0.364233481190487501"),
    mp.mpf("0.285048114137706177"),
]
physical_max_tail = mp.mpf("2.21597735974522257")
physical_max_tail_excluding_wide_corner = mp.mpf("0.649991484542364941")
physical_max_pressure_density = mp.mpf("0.67492564369670709")
fixed_block_min_tail = mp.mpf("0.270705179246934039")
fixed_block_min_pressure_density = mp.mpf("0.74507778509175585")
structured_fourier_max_tail = mp.mpf("7.8246")
structured_fourier_max_pressure_density = mp.mpf("0.838063123922422355")
pure_fourier_max_pressure_density = mp.mpf("0.838063123922422355")
fourier_band_min_pressure_density = mp.mpf("0.212272862006224522")
random_fourier_max_pressure_density = mp.mpf("0.940755884474008723")
random_fourier_min_pressure_density = mp.mpf("0.439988226963201067")
block_contamination_density_crossing_N12 = mp.mpf("0.15")

print("\n=== Physical pressure envelope ===")
print(
    "physical c=0.5 tail sequence = "
    + ", ".join(fmt(value) for value in physical_c05_tail_sequence)
)
print(f"physical_max_tail = {fmt(physical_max_tail)}")
print(f"physical_max_tail_excluding_wide_corner = {fmt(physical_max_tail_excluding_wide_corner)}")
print(f"physical_max_pressure_density = {fmt(physical_max_pressure_density)}")

check(
    "physical c=0.5 tail decreases over the audited ladder",
    all(
        physical_c05_tail_sequence[i] > physical_c05_tail_sequence[i + 1]
        for i in range(len(physical_c05_tail_sequence) - 1)
    ),
    ", ".join(fmt(value, 18) for value in physical_c05_tail_sequence),
)
check(
    "physical pressure density stays below the hostile guard 0.7",
    physical_max_pressure_density < mp.mpf("0.7"),
    f"physical_max_p={fmt(physical_max_pressure_density)}",
)

print("\n=== Staged/fiber pressure ===")
print(f"fixed_block_min_tail = {fmt(fixed_block_min_tail)}")
print(f"fixed_block_min_pressure_density = {fmt(fixed_block_min_pressure_density)}")
print(f"N=12 contamination density crossing = {fmt(block_contamination_density_crossing_N12)}")

check(
    "raw tail alone is not a safe separator",
    fixed_block_min_tail < physical_max_tail,
    f"fixed_min_tail={fmt(fixed_block_min_tail)} physical_max_tail={fmt(physical_max_tail)}",
)
check(
    "pressure density separates tested fixed staged blocks from physical kernels",
    fixed_block_min_pressure_density > physical_max_pressure_density,
    f"fixed_min_p={fmt(fixed_block_min_pressure_density)} "
    f"physical_max_p={fmt(physical_max_pressure_density)}",
)
check(
    "finite contamination threshold is macroscopic, not infinitesimal",
    block_contamination_density_crossing_N12 >= mp.mpf("0.10")
    and block_contamination_density_crossing_N12 <= mp.mpf("0.20"),
    f"density_crossing={fmt(block_contamination_density_crossing_N12)}",
)

print("\n=== Coherent/Fourier boundary ===")
print(f"structured_fourier_max_tail = {fmt(structured_fourier_max_tail)}")
print(f"structured_fourier_max_pressure_density = {fmt(structured_fourier_max_pressure_density)}")
print(f"pure_fourier_max_pressure_density = {fmt(pure_fourier_max_pressure_density)}")
print(f"fourier_band_min_pressure_density = {fmt(fourier_band_min_pressure_density)}")
print(f"random_fourier_pressure_range = {fmt(random_fourier_min_pressure_density)}..{fmt(random_fourier_max_pressure_density)}")

check(
    "pure Fourier modes can exceed the geometry pressure envelope",
    pure_fourier_max_pressure_density > physical_max_pressure_density,
    f"pure_fourier={fmt(pure_fourier_max_pressure_density)} physical={fmt(physical_max_pressure_density)}",
)
check(
    "Fourier bands can fall below the staged-block pressure floor",
    fourier_band_min_pressure_density < fixed_block_min_pressure_density,
    f"band_min={fmt(fourier_band_min_pressure_density)} block_floor={fmt(fixed_block_min_pressure_density)}",
)
check(
    "random Fourier spectra straddle the staged-block floor",
    random_fourier_min_pressure_density < fixed_block_min_pressure_density
    and random_fourier_max_pressure_density > fixed_block_min_pressure_density,
    f"random_range={fmt(random_fourier_min_pressure_density)}..{fmt(random_fourier_max_pressure_density)} "
    f"block_floor={fmt(fixed_block_min_pressure_density)}",
)

print("\n=== Theorem boundary ===")
print("A correct theorem cannot say: all high pressure is forbidden geometry.")
print("It can say: unmarked geometry pressure must stay below the physical envelope,")
print("while coherent high-pressure modes require explicit field/mark sectors.")

check(
    "pressure theorem must be sectoral rather than a naked geometry ban",
    pure_fourier_max_pressure_density > physical_max_pressure_density
    and fourier_band_min_pressure_density < fixed_block_min_pressure_density,
    "coherent modes occupy both sides of the geometry-only pressure floor",
)

print("\n" + "=" * 80)
failed = [name for name, ok, _ in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")
