#!/usr/bin/env python3
"""Exact witness models for Paper 2."""
from __future__ import annotations

from fractions import Fraction
from typing import Dict, Tuple

from core import DynamicChart, Matrix, Q, Token, conjugate_matrix


def same_fact_joint() -> Dict[Tuple[str, str], Fraction]:
    return {("0", "0"): Q(1, 2), ("1", "1"): Q(1, 2)}


def accidental_equal_marginals_joint() -> Dict[Tuple[str, str], Fraction]:
    return {
        ("0", "0"): Q(1, 4),
        ("0", "1"): Q(1, 4),
        ("1", "0"): Q(1, 4),
        ("1", "1"): Q(1, 4),
    }


def anticorrelated_joint() -> Dict[Tuple[str, str], Fraction]:
    return {("0", "1"): Q(1, 2), ("1", "0"): Q(1, 2)}


def common_witness_joint() -> Dict[Tuple[str, str, str], Fraction]:
    return {("0", "0", "0"): Q(1, 2), ("1", "1", "1"): Q(1, 2)}


def counterfactual_completion_charts() -> Tuple[DynamicChart, DynamicChart, DynamicChart, Tuple[int, ...]]:
    """Five-configuration completion-sensitivity witness.

    A and B_id have the same full law. B_swap is obtained by the permutation
    P=(1 2)(3 4). P fixes the initial configuration and the realized initial
    column, but swaps the two record tokens.
    """
    cols = (
        (Q(0), Q(1, 2), Q(1, 2), Q(0), Q(0)),
        (Q(0), Q(0), Q(0), Q(1), Q(0)),
        (Q(0), Q(0), Q(0), Q(0), Q(1)),
        (Q(1), Q(0), Q(0), Q(0), Q(0)),
        (Q(0), Q(1), Q(0), Q(0), Q(0)),
    )
    T: Matrix = tuple(tuple(cols[j][i] for j in range(5)) for i in range(5))
    P = (0, 2, 1, 4, 3)
    T_swap = conjugate_matrix(T, P)

    tok_a = Token("A", tuple("1" if i in {1, 3} else "0" for i in range(5)))
    tok_b = Token("B", tuple("1" if i in {2, 4} else "0" for i in range(5)))
    tokens = (tok_a, tok_b)
    A = DynamicChart("A", T, 0, tokens)
    B_id = DynamicChart("B_id", T, 0, tokens)
    B_swap = DynamicChart("B_swap", T_swap, 0, tokens)
    return A, B_id, B_swap, P
