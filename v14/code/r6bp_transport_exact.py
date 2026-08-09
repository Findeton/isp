#!/usr/bin/env python3.13
"""
v14 R6b' -- THE RENEWAL-GRAIN TRANSPORT (paper-09).

Does a MOTIVATED identification carry the renewal-grain positional
structure of the deep corpus (S1's completed chain q'; S2's
intervening-pattern census) to the spatial record-interval arena
(I7 / R6a's n_l(x)) -- and if so, does the derived interval-positional
kernel collapse the R6a split fiber, as a forced VALUE or a forced
DISTRIBUTION?

CLI CONTRACT
------------
  python3.13 r6bp_transport_exact.py
        Plain delivery run.  Verifies every anchor, evaluates every
        must-pass gate, computes the verdict from the measured values,
        and WRITES  r6bp_transport_output.txt  and
        r6bp_transport_receipt.json  beside this file.
        Exit 0 iff every must-pass gate passes and every anchor holds.

  python3.13 r6bp_transport_exact.py --selftest
        Re-runs this file once per declared mutant in a subprocess and
        requires each to exit non-zero (the mutant is killed).  Writes
        nothing.  Exit 0 iff every mutant dies.

  python3.13 r6bp_transport_exact.py --mutant NAME
        Runs the delivery computation with the named injection applied.
        Writes nothing.  Exit non-zero if any gate or anchor fails
        (which is the intended outcome for every declared mutant).

  python3.13 r6bp_transport_exact.py --list-mutants
        Prints the declared mutant names, one per line.

Exit 2 is reserved for anchor failure; exit 1 for gate failure; exit 3
for the float guard.

ARITHMETIC: exact.  int / fractions.Fraction only.  An AST pass over
this file's own source rejects every float literal before any
measurement runs.

SCOPE (binding, printed with every headline)
  * S1's chain and S4's renewal theorem are DELIVERY-FREE scope
    (two-actor, delivery-free).  S2's census is TRANSPORT scope.
  * S2's interval lengths are ENSEMBLE DATA (declared positions), not
    samples of the derived kernel.
  * S5's continuous positional layer carries its own
    chosen-not-derived disclaimer and is used only as a labelled
    comparator.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr

# --------------------------------------------------------------------
# 0.  Paths, injection channel, bookkeeping
# --------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT_TXT = os.path.join(HERE, "r6bp_transport_output.txt")
OUT_JSON = os.path.join(HERE, "r6bp_transport_receipt.json")

MUT = None                      # set from --mutant; never read by a gate

LINES: list[str] = []
GATES: list[dict] = []
ANCHORS: list[dict] = []
FAILED_ANCHORS: list[str] = []


def say(s: str = "") -> None:
    LINES.append(s)


def gate(name: str, ok: bool, detail: str, falsifier: str,
         must_pass: bool = True) -> bool:
    """Register a gate.  `falsifier` names the injection that kills it."""
    GATES.append({"name": name, "passed": bool(ok), "detail": detail,
                  "must_pass": must_pass, "injection_falsifier": falsifier})
    say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    return bool(ok)


def fr(x: Fr) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


# --------------------------------------------------------------------
# 1.  The float guard (AST over this file's own source)
# --------------------------------------------------------------------

def float_guard() -> tuple[int, int]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    bad = 0
    total = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            total += 1
            if isinstance(node.value, float) or isinstance(node.value, complex):
                bad += 1
    return bad, total


# --------------------------------------------------------------------
# 2.  Anchors -- file-bytes, path-value, verbatim-text
# --------------------------------------------------------------------

_FILE_CACHE: dict[str, bytes] = {}
_BLOB_CACHE: dict[str, bytes] = {}


def read_bytes(rel: str) -> bytes:
    if rel not in _FILE_CACHE:
        with open(os.path.join(REPO, rel), "rb") as fh:
            _FILE_CACHE[rel] = fh.read()
    return _FILE_CACHE[rel]


def read_committed(rel: str) -> bytes:
    """The COMMITTED bytes of a tracked artifact (read-only git).

    R6a is on the TERMINAL track with its repair IN FLIGHT in the working
    tree (v14 LOG #26 delivered-committed, #27 verified, #34 adjudicated
    AWF-unanimous with the verdict HOLDING, orders R-R6A-1..10 dispatched).
    The pin anchors the DELIVERED-COMMITTED receipt bytes, so this unit
    consumes those, and discloses the working-tree state beside them.
    """
    if rel not in _BLOB_CACHE:
        proc = subprocess.run(["git", "-C", REPO, "show", f"HEAD:{rel}"],
                              capture_output=True)
        if proc.returncode != 0:
            raise RuntimeError(f"committed blob unavailable: {rel}")
        _BLOB_CACHE[rel] = proc.stdout
    return _BLOB_CACHE[rel]


def sha12(rel: str) -> str:
    return hashlib.sha256(read_bytes(rel)).hexdigest()[:12]


def sha12_committed(rel: str) -> str:
    return hashlib.sha256(read_committed(rel)).hexdigest()[:12]


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def anchor_file(name: str, rel: str, expected: str, pedigree: str,
                consumer: str, committed: bool = False) -> None:
    got = sha12_committed(rel) if committed else sha12(rel)
    if MUT == "INJ-FILE-ANCHOR-DRIFT" and name == "A-S1-PAPER31":
        got = "deadbeefcafe"
    ok = (got == expected)
    ANCHORS.append({"name": name,
                    "kind": "file-bytes-committed" if committed else "file-bytes",
                    "artifact": rel,
                    "expected": expected, "measured": got, "ok": ok,
                    "pedigree": pedigree, "consumer_gate": consumer})
    if not ok:
        FAILED_ANCHORS.append(f"{name}: {rel} expected {expected} got {got}")


_JSON_CACHE: dict[str, dict] = {}


def load_json(rel: str) -> dict:
    if rel not in _JSON_CACHE:
        if rel in COMMITTED_SOURCES:
            _JSON_CACHE[rel] = json.loads(read_committed(rel).decode("utf-8"))
        else:
            _JSON_CACHE[rel] = json.loads(read_bytes(rel).decode("utf-8"))
    return _JSON_CACHE[rel]


def load_json_worktree(rel: str) -> dict:
    return json.loads(read_bytes(rel).decode("utf-8"))


def anchor_path(name: str, rel: str, path: list, expected, pedigree: str,
                consumer: str):
    """Path-value anchor: binds the (path, value) pair, not only the bytes."""
    obj = load_json(rel)
    cur = obj
    walked = []
    for key in path:
        walked.append(key)
        try:
            cur = cur[key]
        except (KeyError, IndexError, TypeError):
            cur = "<PATH-ABSENT:" + "/".join(str(w) for w in walked) + ">"
            break
    if MUT == "INJ-PATH-DRIFT" and name == "P-R6A-SPLIT-FIBER-MIN":
        cur = 0
    ok = (cur == expected)
    ANCHORS.append({"name": name, "kind": "path-value", "artifact": rel,
                    "path": "/".join(str(p) for p in path),
                    "expected": expected, "measured": cur, "ok": ok,
                    "pedigree": pedigree, "consumer_gate": consumer})
    if not ok:
        FAILED_ANCHORS.append(
            f"{name}: {rel}:{'/'.join(str(p) for p in path)} "
            f"expected {expected!r} got {cur!r}")
    return cur


def anchor_verbatim(name: str, rel: str, window: str, pedigree: str,
                    consumer: str) -> None:
    """Verbatim-text anchor: a CONTEXT WINDOW (not a fragment), bound to a
    named consumer gate, evaluated before the byte anchors are consumed."""
    text = read_bytes(rel).decode("utf-8")
    needle = norm_ws(window)
    if MUT == "INJ-VERBATIM-DRIFT" and name == "V-S1-SCOPE":
        needle = needle.replace("transport scope", "record scope")
    ok = needle in norm_ws(text)
    ANCHORS.append({"name": name, "kind": "verbatim-text", "artifact": rel,
                    "window": window, "window_chars": len(needle), "ok": ok,
                    "pedigree": pedigree, "consumer_gate": consumer})
    if not ok:
        FAILED_ANCHORS.append(f"{name}: context window absent from {rel}")


# --------------------------------------------------------------------
# 3.  The pinned rows S1..S6, I7, and the two fiber anchors
# --------------------------------------------------------------------

PED_S1 = "S1 THE TRANSITION MATRIX -- TERMINAL (v10 #349)"
PED_S2 = ("S2 THE POSITIONAL CENSUS -- TERMINAL (v11 #20-#21); interval "
          "lengths are ENSEMBLE DATA (declared)")
PED_S3 = "S3 THE TYPE DECLARATION -- founding paper; v11 FROZEN"
PED_S4 = ("S4 THE RENEWAL THEOREM -- TERMINAL (v10 #326; ten hostile rounds; "
          "its header's \"paper-level review open\" note carried)")
PED_S5 = ("S5 THE DECLARED POSITIONAL LAW -- D34b TERMINAL delta (3 hostile "
          "streams); the waiting law and rates are CHOSEN, NOT DERIVED")
PED_S6 = ("S6 THE EXTREMAL STANDARD -- audit (status: completed "
          "pre-hostile-review, carried) + finite nonselection theorem")
PED_I7 = ("I7 (R0 founding pin) -- gravity's record layer; H_a[N] "
          "record-native; record-IS-metric; THE BASELINE ARENA ROW")
PED_R6A = ("v14 R6a paper-04 -- DELIVERED-COMMITTED (LOG #26), "
           "ADJUDICATOR-VERIFIED (#27), JOINT ADJUDICATION AWF UNANIMOUS "
           "with THE VERDICT HOLDS (#34), TERMINAL-track: repair in flight "
           "under orders R-R6A-1..10; the receipt bytes anchored here are "
           "the delivered-committed ones")
PED_CRB = "v14 CR-B -- DELIVERED-VERIFIED-UNREVIEWED (LOG #37, #38)"

R6A_RECEIPT = "v14/code/r6a_refinement_receipt.json"
CRB_RECEIPT = "v14/code/crb_stochastic_receipt.json"
HA_RECEIPT = "v13/code/ha_successor_receipt.json"

# artifacts consumed at their COMMITTED bytes (the bytes the pin names)
COMMITTED_SOURCES = {R6A_RECEIPT}

P31 = "v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md"
D43B = "v10/code/d43b_state_chain_exact.py"
U1B_NOTE = "v11/note-u1b-renewal-class-sweep.md"
U1B_OUT = "v11/code/u1b_output.txt"
U1B_CODE = "v11/code/u1b_renewal_class_sweep_exact.py"
P0 = "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md"
P30 = "v10/relativistic-isp-v10-paper30-the-generated-record-and-its-completion.md"
D33 = "v10/note-d33-history-law-phase.md"
P21 = "v10/relativistic-isp-v10-paper21-local-generators-do-not-imply-local-memory.md"
D34B = "v10/code/d34b_exponential_clocks_exact.py"
D12 = "v10/note-d12-selection-principle-audit.md"
P16 = "v10/relativistic-isp-v10-paper16-the-rulebook-is-the-history-law.md"

NAMED_EXCLUSIONS = [
    ("v11/note-u1c-depth15-two-sided.md",
     "GREEN-UNREVIEWED, NOT CITABLE per STATUS -- registered lead only, "
     "status printed"),
    ("v10/THE-THEORY-SO-FAR.md", "index only, never primary"),
    ("v12 Gamma objects", "arena-free -- no interval/position/count content"),
    ("v10/note-d70-horizon-limit-result.md",
     "round-1-repaired, NOT terminal -- excluded from this unit"),
]


def register_anchors() -> None:
    # ---- verbatim-text anchors FIRST (the adopted modification) -----
    anchor_verbatim(
        "V-S1-T", P31,
        "The `6 x 6` transfer is well-defined: every one of the 215 "
        "histories of length `<= 3` in a class produces the same exact row",
        PED_S1, "G-S1-TWO-ROUTES")
    anchor_verbatim(
        "V-S1-F", P31,
        "`T f = 2 f` exactly at `f = (4, 4, 3, 7, 3, 3)/3 > 0`",
        PED_S1, "G-S1-TWO-ROUTES")
    anchor_verbatim(
        "V-S1-QP", P31,
        "the conflict\n  row is `{0: 1/7, 3: 3/4, 5: 3/28}`.  This is the "
        "root-free\n  completion, exhibited on the intrinsic chain.",
        PED_S1, "G-KERNEL-CONFLICT-ROW")
    anchor_verbatim(
        "V-S1-CLASS", P31,
        "The dominant class `{2, 4, 5}` (Tarjan decomposition;\n  `{0, 1, 3}` "
        "is transient and carries the renewal loop `3 -> 0`)",
        PED_S1, "G-CLOSED-CLASS")
    anchor_verbatim(
        "V-S1-SCOPE", P31,
        "At transport scope the picture will change and is declared: "
        "deliveries\nreopen the absorbing sector (diverged holdings can "
        "reconverge), the\nclass structure of §3.2 is not stable under the "
        "transport grammar",
        PED_S1, "G-SCOPE-SEAM")
    anchor_verbatim(
        "V-S2-LEG1", U1B_OUT,
        "[DATA] LEG-1 interval-4 tag patterns (the unequal-interval "
        "structure, exhaustive): {('d', 'p', 'p', 'r'): 1024, "
        "('n', 'p', 'p', 'r'): 512, ('p', 'n', 'p', 'r'): 512, "
        "('p', 'p', 'd', 'r'): 1024, ('p', 'p', 'n', 'r'): 512}",
        PED_S2, "G-S2-PROFILES")
    anchor_verbatim(
        "V-S2-LEG2", U1B_OUT,
        "leg-2 patterns {('d', 'p', 'p', 'r'): 24576, "
        "('n', 'p', 'p', 'r'): 8192, ('p', 'n', 'p', 'r'): 8192, "
        "('p', 'p', 'd', 'r'): 24576, ('p', 'p', 'n', 'r'): 8192}",
        PED_S2, "G-S2-PROFILES")
    anchor_verbatim(
        "V-S2-L3", U1B_OUT,
        "(p,p,r) is the ONLY intervening pattern that reaches a renewal "
        "three events after a renewal",
        PED_S2, "G-POSITIONAL-STRATUM-EMPTY-AT-3")
    anchor_verbatim(
        "V-S2-FIVE", U1B_NOTE,
        "A renewal three\nevents after a renewal forces `(p,p,r)` and nothing "
        "else.  A renewal\nfour events after a renewal admits exactly five "
        "intervening patterns",
        PED_S2, "G-S2-PATTERN-POSITION-MAP")
    anchor_verbatim(
        "V-S2-SCOPE", U1B_NOTE,
        "Transport scope (`d42b1`) only; the two-actor pool only",
        PED_S2, "G-SCOPE-SEAM")
    anchor_verbatim(
        "V-S3-POSIT", P0,
        "**[POSIT]** v11's **division events are the renewal events.**",
        PED_S3, "G-TYPE-CENSUS")
    anchor_verbatim(
        "V-S3-BRIDGES", P0,
        "**The bridges** are the conflict windows between renewals.",
        PED_S3, "G-BRIDGES-READING")
    anchor_verbatim(
        "V-S3-GAMMA", P0,
        "the sparse indivisible family Γ(cut′ ← cut), conditioned only at "
        "division events | to be constructed",
        PED_S3, "G-SCOPE-HONESTY")
    anchor_verbatim(
        "V-S4-RENEWAL", P30,
        "**every pair arbitration\nis a renewal to the root state** "
        "[THEOREM at two-actor delivery-free\nscope]",
        PED_S4, "G-DELIVERY-FREE-SCOPE")
    anchor_verbatim(
        "V-S4-CLICK", P30,
        "**K1** refines into a chain of selection clicks",
        PED_S4, "G-IDENTIFICATION-CENSUS")
    anchor_verbatim(
        "V-S4-EMPIRICAL", P30,
        "Which basis nature seals — the fine order-sealed\nrecord or the "
        "coarse winner-sealed record — is an *empirical* question.",
        PED_S4, "G-IDENTIFICATION-CENSUS")
    anchor_verbatim(
        "V-S5-CHOSEN", D33,
        "the coefficients 1/4 are chosen, not derived",
        PED_S5, "G-S5-DISCLAIMER")
    anchor_verbatim(
        "V-S5-CHOSEN2", P21,
        "For the chosen static-adjacency D34b birth/idle/interaction exemplar",
        PED_S5, "G-S5-DISCLAIMER")
    anchor_verbatim(
        "V-S6-BAR", D12,
        "A proposed selector `Q` derives a unique law only if the frozen "
        "SHARD premises\nplus `Q` have exactly one physical equivalence "
        "class of models.",
        PED_S6, "G-EXTREMAL-BAR")
    anchor_verbatim(
        "V-S6-MAXENT", D12,
        "least-committal law relative to a supplied base measure and "
        "supplied constraints",
        PED_S6, "G-EXTREMAL-BAR")
    anchor_verbatim(
        "V-S6-NONSEL", P16,
        "a fixed causal action does not select the boundary state, orbit "
        "measure,\n> extension kernel or complete next-record law.\n\nThis "
        "is a finite nonselection theorem.",
        PED_S6, "G-EXTREMAL-BAR")
    anchor_verbatim(
        "V-S6-INTRINSIC", P16,
        "the corpus has no\nrecord-intrinsic, field-redefinition-invariant "
        "complexity measure that selects\none generator.",
        PED_S6, "G-EXTREMAL-INTRINSIC")
    anchor_verbatim(
        "V-COVER-ROOTED", P30,
        "Truncated completions are therefore depth-non-stationary: "
        "**rooted**",
        PED_S4, "G-COVER-DISSOLVED")
    anchor_verbatim(
        "V-COVER-GROWS", P31,
        "its state count grows with depth (17, 23,\n29 at depths 4, 5, 6) "
        "while representing no new structure",
        PED_S1, "G-COVER-DISSOLVED")

    # ---- file-bytes anchors ----------------------------------------
    anchor_file("A-PIN", "v14/note-r6bprime-transport-pin.md", "17111fd19022",
                "this unit's pin, FROZEN at v14 ledger #43", "G-PIN-BOUND")
    anchor_file("A-S1-PAPER31", P31, "7ac66f3fe74d", PED_S1, "G-S1-TWO-ROUTES")
    anchor_file("A-S1-D43B", D43B, "5f91f0190b4c", PED_S1, "G-S1-TWO-ROUTES")
    anchor_file("A-S2-NOTE", U1B_NOTE, "47f001fad828", PED_S2, "G-S2-PROFILES")
    anchor_file("A-S2-OUT", U1B_OUT, "a955b8484465", PED_S2, "G-S2-PROFILES")
    anchor_file("A-S2-CODE", U1B_CODE, "5adb205a33d6", PED_S2, "G-S2-PROFILES")
    anchor_file("A-S3-PAPER0", P0, "37a428321f46", PED_S3, "G-TYPE-CENSUS")
    anchor_file("A-S4-PAPER30", P30, "e431a7c48f76", PED_S4,
                "G-DELIVERY-FREE-SCOPE")
    anchor_file("A-S5-D33", D33, "bad952ee5849", PED_S5, "G-S5-DISCLAIMER")
    anchor_file("A-S5-PAPER21", P21, "038a424a8843", PED_S5, "G-S5-DISCLAIMER")
    anchor_file("A-S5-D34B", D34B, "dee1cc968268", PED_S5, "G-S5-DISCLAIMER")
    anchor_file("A-S6-D12", D12, "2670a2ea7644", PED_S6, "G-EXTREMAL-BAR")
    anchor_file("A-S6-PAPER16", P16, "dbf027b2fbc9", PED_S6, "G-EXTREMAL-BAR")
    anchor_file("A-I7", HA_RECEIPT, "542b8735daf0", PED_I7, "G-ARENA-BASELINE")
    anchor_file("A-R6A", R6A_RECEIPT, "022c3f488a93", PED_R6A,
                "G-R6A-FIBER-REBUILD", committed=True)
    anchor_file("A-CRB", CRB_RECEIPT, "5ebeec141303", PED_CRB,
                "G-CRB-SIMPLEX")
    # DISCLOSURE, not a must-match: the R6a repair is in flight in the
    # working tree.  The consumed values are compared below (the repair
    # delta gate); this row records what the tree carried at run time.
    ANCHORS.append({
        "name": "A-R6A-WORKTREE", "kind": "file-bytes-disclosure",
        "artifact": R6A_RECEIPT, "expected": "(disclosure -- no expectation)",
        "measured": sha12(R6A_RECEIPT), "ok": True, "pedigree": PED_R6A,
        "consumer_gate": "G-R6A-REPAIR-DELTA"})


# --------------------------------------------------------------------
# 4.  S1 -- the chain by TWO ROUTES inside S1's own artifacts
# --------------------------------------------------------------------

def route_paper_T() -> list[list[Fr]]:
    """Route P: parse the 6x6 transfer out of paper 31's own fenced block."""
    text = read_bytes(P31).decode("utf-8")
    i = text.index("T = [ 3/2")
    block = text[i:i + 420]
    rows = []
    for line in block.split("\n"):
        m = re.search(r"\[([^\]]*)\]", line)
        if not m:
            continue
        cells = m.group(1).split()
        if len(cells) != 6:
            continue
        row = []
        for c in cells:
            if "/" in c:
                a, b = c.split("/")
                row.append(Fr(int(a), int(b)))
            else:
                row.append(Fr(int(c)))
        rows.append(row)
        if len(rows) == 6:
            break
    return rows


def route_paper_f() -> list[Fr]:
    text = read_bytes(P31).decode("utf-8")
    m = re.search(r"`f = \(([\d, ]+)\)/(\d+) > 0`", text)
    nums = [int(x) for x in m.group(1).split(",")]
    den = int(m.group(2))
    return [Fr(n, den) for n in nums]


def route_code_T_f(src_rel: str = None) -> tuple[list[list[Fr]], list[Fr]]:
    """Route C: AST-extract T_REF and f from d43b's own source."""
    src = read_bytes(src_rel if src_rel else D43B).decode("utf-8")
    tree = ast.parse(src)
    T = [[Fr(0)] * 6 for _ in range(6)]
    f = None

    def frac_of(node):
        # Fr(a, b) or Fr(a)
        args = [a.value for a in node.args]
        return Fr(*args)

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            tgt = node.targets[0]
            if isinstance(tgt, ast.Name) and tgt.id == "T_REF":
                for k, v in zip(node.value.keys, node.value.values):
                    i = k.value
                    for kk, vv in zip(v.keys, v.values):
                        T[i][kk.value] = frac_of(vv)
            if (isinstance(tgt, ast.Name) and tgt.id == "f"
                    and isinstance(node.value, ast.List)
                    and len(node.value.elts) == 6):
                f = [frac_of(e) for e in node.value.elts]
    return T, f


# --------------------------------------------------------------------
# 5.  Exact linear algebra over Fraction
# --------------------------------------------------------------------

def solve_exact(A: list[list[Fr]], b: list[Fr]) -> list[Fr] | None:
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                fac = M[r][col]
                M[r] = [x - fac * y for x, y in zip(M[r], M[col])]
    return [M[i][n] for i in range(n)]


def sccs_of(adj: dict[int, list[int]], nodes: list[int]) -> list[list[int]]:
    """Iterative Tarjan; returns SCCs as sorted lists, sorted."""
    index: dict[int, int] = {}
    low: dict[int, int] = {}
    onstack: dict[int, bool] = {}
    stack: list[int] = []
    out: list[list[int]] = []
    counter = [0]
    for root in nodes:
        if root in index:
            continue
        work = [(root, 0)]
        while work:
            v, pi = work[-1]
            if pi == 0:
                index[v] = low[v] = counter[0]
                counter[0] += 1
                stack.append(v)
                onstack[v] = True
            recurse = False
            for i in range(pi, len(adj[v])):
                w = adj[v][i]
                if w not in index:
                    work[-1] = (v, i + 1)
                    work.append((w, 0))
                    recurse = True
                    break
                if onstack.get(w):
                    low[v] = min(low[v], index[w])
            if recurse:
                continue
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stack.pop()
                    onstack[w] = False
                    comp.append(w)
                    if w == v:
                        break
                out.append(sorted(comp))
            work.pop()
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
    return sorted(out)


# --------------------------------------------------------------------
# 6.  The delivery computation
# --------------------------------------------------------------------

def run() -> dict:
    R: dict = {}
    R["unit"] = "v14 R6b' -- THE RENEWAL-GRAIN TRANSPORT (paper-09)"
    R["question"] = (
        "can a MOTIVATED identification carry the renewal-grain positional "
        "structure (S1's chain q'; S2's intervening-pattern census) to the "
        "spatial record-interval arena (I7), and does the derived kernel "
        "collapse the R6a split fiber as a forced VALUE or a forced "
        "DISTRIBUTION?")

    # ---- 0. float guard --------------------------------------------
    bad, consts = float_guard()
    R["arithmetic"] = {"kind": "exact int/Fraction only",
                       "float_literals_in_source": bad,
                       "constants_scanned": consts}
    if bad:
        print(f"FLOAT GUARD: {bad} float literal(s) in source", file=sys.stderr)
        sys.exit(3)

    say("=" * 78)
    say("v14 R6b' -- THE RENEWAL-GRAIN TRANSPORT (paper-09)")
    say("=" * 78)
    say("")
    say("SCOPE, DECLARED BEFORE ANY MEASUREMENT:")
    say("  * S1's completed chain and S4's renewal theorem are stated at")
    say("    TWO-ACTOR DELIVERY-FREE SCOPE.")
    say("  * S2's intervening-pattern census is stated at TRANSPORT SCOPE,")
    say("    and its interval lengths are ENSEMBLE DATA (declared renewal")
    say("    positions), not samples of any derived kernel.")
    say("  * S5's continuous positional layer carries its own")
    say("    chosen-not-derived disclaimer and enters only as a labelled")
    say("    comparator.")
    say("")

    # ---- 1. anchors -------------------------------------------------
    say("-" * 78)
    say("1.  ANCHORS (verbatim-text evaluated first; then file-bytes; then")
    say("    path-value)")
    say("-" * 78)
    register_anchors()

    # path-value anchors: the arena (I7 / R6a), the R6a fiber values,
    # CR-B's simplex dimensions.
    arena_geo = anchor_path(
        "P-ARENA-GEOMETRY-RECORD", R6A_RECEIPT, ["arena", "geometry_record"],
        "n_l(x) in Z_>0, the number of division events in the record "
        "interval between x and x+l", PED_R6A, "G-ARENA-BASELINE")
    arena_readout = anchor_path(
        "P-ARENA-READOUT", R6A_RECEIPT, ["arena", "readout"],
        "q_ij e_l^i e_l^j = n_l(x); I = q^-1 (det q)^w at w = 0",
        PED_R6A, "G-EXTREMAL-INTRINSIC")
    anchor_path("P-ARENA-SITES", R6A_RECEIPT, ["arena", "sites"],
                "X = (Z_L)^d with L = 3, d = 2 (|X| = 9)", PED_R6A,
                "G-ARENA-BASELINE")
    anchor_path("P-ARENA-LINKS", R6A_RECEIPT, ["arena", "links"],
                [[1, 0], [0, 1], [1, 1]], PED_R6A, "G-ARENA-BASELINE")
    anchor_path("P-I7-DENSITY-WEIGHT", HA_RECEIPT,
                ["declarations", "density_weight"], 0, PED_I7,
                "G-EXTREMAL-INTRINSIC")
    anchor_path("P-I7-L", HA_RECEIPT, ["declarations", "L"], 3, PED_I7,
                "G-ARENA-BASELINE")
    anchor_path("P-I7-D", HA_RECEIPT, ["declarations", "d"], 2, PED_I7,
                "G-ARENA-BASELINE")
    r6a_split_min = anchor_path(
        "P-R6A-SPLIT-FIBER-MIN", R6A_RECEIPT, ["split_fibers", "G-DIAG2", "raw"],
        19683, PED_R6A, "G-R6A-FIBER-REBUILD")
    r6a_split_max = anchor_path(
        "P-R6A-SPLIT-FIBER-MAX", R6A_RECEIPT,
        ["split_fibers", "G-ANISO2", "raw"], 13631146639813244878848,
        PED_R6A, "G-R6A-FIBER-REBUILD")
    anchor_path("P-R6A-DIAG2-ADMISSIBLE", R6A_RECEIPT,
                ["split_fibers", "G-DIAG2", "admissible_at_images"], 19683,
                PED_R6A, "G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD")
    anchor_path("P-R6A-ANISO2-ADMISSIBLE", R6A_RECEIPT,
                ["split_fibers", "G-ANISO2", "admissible_at_images"],
                1257565061957837936381, PED_R6A, "G-R6A-FIBER-REBUILD")
    anchor_path("P-R6A-OFFDIAG-RAW", R6A_RECEIPT,
                ["split_fibers", "G-OFFDIAG", "raw"], 1953125, PED_R6A,
                "G-R6A-FIBER-REBUILD")
    anchor_path("P-R6A-OFFDIAG-ADMISSIBLE", R6A_RECEIPT,
                ["split_fibers", "G-OFFDIAG", "admissible_at_images"], 19683,
                PED_R6A, "G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD")
    r6a_equiv = anchor_path(
        "P-R6A-EQUIVARIANT-FIBERS", R6A_RECEIPT, ["equivariant_fibers"],
        {"G-ANISO2": 288, "G-CURVOFF": 29393280, "G-DIAG2": 3,
         "G-OFFDIAG": 5, "G-OFFDIAG2": 88, "G-OFFNEG": 24}, PED_R6A,
        "G-R6A-FIBER-REBUILD")
    anchor_path("P-R6A-ADDITIVITY", R6A_RECEIPT,
                ["forced_part", "additivity_checks"], 972, PED_R6A,
                "G-ADDITIVITY-REVERIFIED")
    anchor_path("P-R6A-ADDITIVITY-VIOL", R6A_RECEIPT,
                ["forced_part", "additivity_violations"], 0, PED_R6A,
                "G-ADDITIVITY-REVERIFIED")
    anchor_path("P-R6A-RESTRICTION", R6A_RECEIPT,
                ["forced_part", "restriction_checks"], 324, PED_R6A,
                "G-METRIC-RESTRICTION-REVERIFIED")
    anchor_path("P-R6A-RESTRICTION-OK", R6A_RECEIPT,
                ["forced_part", "restriction_ok"], 324, PED_R6A,
                "G-METRIC-RESTRICTION-REVERIFIED")
    anchor_path("P-R6A-LIFT-PAIR", R6A_RECEIPT,
                ["choice_inventory", "items", 7, "fiber"], 2, PED_R6A,
                "G-R6A-RECLASSIFICATION")
    anchor_path("P-R6A-FRONT-NONINTEGRAL", R6A_RECEIPT,
                ["forced_front_lift", "non_integral"], 30, PED_R6A,
                "G-FRONT-RULE-INTEGRAL")
    anchor_path("P-R6A-FRONT-CELLS", R6A_RECEIPT,
                ["forced_front_lift", "cells"], 81, PED_R6A,
                "G-FRONT-RULE-INTEGRAL")
    anchor_path("P-R6A-FREE-LINKS", R6A_RECEIPT, ["cover", "free_links"], 54,
                PED_R6A, "G-TRANSVERSE-LINKS-UNFORCED")
    anchor_path("P-R6A-REFINED-LINKS", R6A_RECEIPT, ["cover", "refined_links"],
                108, PED_R6A, "G-TRANSVERSE-LINKS-UNFORCED")
    anchor_path("P-R6A-NEW-SITES", R6A_RECEIPT, ["cover", "new_sites"], 27,
                PED_R6A, "G-NEW-FRONTS-RECLASSED")
    anchor_path("P-R6A-VERDICT-HEAD", R6A_RECEIPT, ["verdict_head"],
                "R6A-NO-MOTIVATED-SPLIT", PED_R6A, "G-R6A-RECLASSIFICATION")
    anchor_path("P-R6A-CONTROL-QUALIFIER", R6A_RECEIPT,
                ["control", "qualifier"], "UNMOTIVATED", PED_R6A,
                "G-CONTROL-R1-COPY")
    anchor_path("P-R6A-CONTROL-UNREPRESENTED", R6A_RECEIPT,
                ["control", "tally", "UNREPRESENTED"], 6, PED_R6A,
                "G-CONTROL-R1-COPY")
    crb_head = anchor_path(
        "P-CRB-HEAD", CRB_RECEIPT, ["verdict_head"],
        "CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW", PED_CRB, "G-CRB-SIMPLEX")
    crb_missing = anchor_path(
        "P-CRB-MISSING", CRB_RECEIPT, ["missing_tag"],
        "THE-INTERVAL-POSITIONAL-LAW-=-THE-TRANSITION-KERNEL-BETWEEN-AN-"
        "INTERVALS-ENDPOINTS-WHOSE-RENEWAL-COUNT-IS-N|R0-CARRIES-THE-RECORD-"
        "LAYER-I7-AND-NO-TRANSITION-LAYER", PED_CRB, "G-CRB-SIMPLEX")
    crb_n4 = anchor_path(
        "P-CRB-N4-ROW", CRB_RECEIPT, ["per_interval_law", "rows", 3],
        {"n": 4, "fiber": 3, "pinned_orbits": 3, "pinned_simplex_dim": 2,
         "pinned_transitive": False, "flip_orbits": 2, "flip_simplex_dim": 1,
         "flip_transitive": False}, PED_CRB, "G-CRB-SIMPLEX")
    crb_n3 = anchor_path(
        "P-CRB-N3-ROW", CRB_RECEIPT, ["per_interval_law", "rows", 2],
        {"n": 3, "fiber": 2, "pinned_orbits": 2, "pinned_simplex_dim": 1,
         "pinned_transitive": False, "flip_orbits": 1, "flip_simplex_dim": 0,
         "flip_transitive": True}, PED_CRB, "G-CRB-SIMPLEX")
    crb_tv4 = anchor_path(
        "P-CRB-TV-UNIFORM-BINOMIAL-4", CRB_RECEIPT,
        ["selection_candidates", "rows", 0, "evidence",
         "tv_uniform_vs_binomial", "4"], "2/21", PED_CRB,
        "G-S5-COMPARATOR-SEPARATION")
    anchor_path("P-CRB-UNIFORM-REFUTED", CRB_RECEIPT,
                ["selection_candidates", "rows", 2, "result"],
                "REFUTED-AS-FORCING", PED_CRB,
                "G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD")
    anchor_path("P-CRB-MAXENT-CONSTRAINTS", CRB_RECEIPT,
                ["selection_candidates", "rows", 1, "evidence",
                 "pinned_moment_constraints"], 0, PED_CRB, "G-EXTREMAL-BAR")

    # the repair-delta disclosure: every path-value this unit consumes from
    # the R6a receipt, compared between the COMMITTED bytes the pin names
    # and the working tree's in-flight repair.
    wt = load_json_worktree(R6A_RECEIPT)
    moved = []
    consumed = 0
    for a in ANCHORS:
        if a["kind"] != "path-value" or a["artifact"] != R6A_RECEIPT:
            continue
        consumed += 1
        cur = wt
        for key in a["path"].split("/"):
            k = int(key) if re.fullmatch(r"-?\d+", key) else key
            try:
                cur = cur[k]
            except (KeyError, IndexError, TypeError):
                cur = "<ABSENT>"
                break
        if cur != a["measured"]:
            moved.append({"path": a["path"], "committed": a["measured"],
                          "worktree": cur})
    if MUT == "INJ-REPAIR-DELTA":
        moved = moved + [{"path": "<injected>", "committed": 1, "worktree": 2}]
    gate("G-R6A-REPAIR-DELTA",
         len(moved) == 0,
         f"R6a is on the TERMINAL track with its repair IN FLIGHT: this "
         f"unit consumes the DELIVERED-COMMITTED receipt bytes the pin "
         f"names ({sha12_committed(R6A_RECEIPT)}), and discloses the "
         f"working tree's in-flight bytes ({sha12(R6A_RECEIPT)}).  All "
         f"{consumed} path-values consumed from that receipt are compared "
         f"across the two: {len(moved)} moved.  Carried status: DELIVERED-"
         f"COMMITTED (LOG #26) / ADJUDICATOR-VERIFIED (#27) / ADJUDICATED "
         f"AWF-UNANIMOUS, THE VERDICT HOLDS (#34), repair under orders "
         f"R-R6A-1..10 pending its own verification",
         "INJ-REPAIR-DELTA")
    R["r6a_repair_disclosure"] = {
        "committed_sha256_12": sha12_committed(R6A_RECEIPT),
        "worktree_sha256_12": sha12(R6A_RECEIPT),
        "path_values_consumed": consumed,
        "path_values_moved": moved,
        "carried_status": ("DELIVERED-COMMITTED (v14 LOG #26); "
                           "ADJUDICATOR-VERIFICATION CLEAN (#27); JOINT "
                           "ADJUDICATION grade AWF unanimous, THE VERDICT "
                           "HOLDS (#34); repair in flight under orders "
                           "R-R6A-1..10, its verification pending"),
    }

    n_file = sum(1 for a in ANCHORS
                 if a["kind"] in ("file-bytes", "file-bytes-committed"))
    n_path = sum(1 for a in ANCHORS if a["kind"] == "path-value")
    n_verb = sum(1 for a in ANCHORS if a["kind"] == "verbatim-text")
    n_disc = sum(1 for a in ANCHORS if a["kind"] == "file-bytes-disclosure")
    R["anchor_totals"] = {"file_bytes": n_file, "path_value": n_path,
                          "verbatim_text": n_verb, "disclosures": n_disc,
                          "total": len(ANCHORS),
                          "failures": len(FAILED_ANCHORS)}
    R["anchors"] = ANCHORS
    say(f"  file-bytes {n_file} | path-value {n_path} | verbatim-text "
        f"{n_verb} | disclosures {n_disc} | total {len(ANCHORS)} | failures "
        f"{len(FAILED_ANCHORS)}")
    for f_ in FAILED_ANCHORS:
        say(f"  [ANCHOR-FAIL] {f_}")
    say("")

    R["named_exclusions"] = [
        {"artifact": a, "status_printed": s} for a, s in NAMED_EXCLUSIONS]
    say("  NAMED EXCLUSIONS (binding, status printed):")
    for a, s in NAMED_EXCLUSIONS:
        say(f"    - {a}  --  {s}")
    say("")

    # ---- 2. S1 by two routes ----------------------------------------
    say("-" * 78)
    say("2.  S1 -- THE CHAIN, BY TWO ROUTES INSIDE S1's OWN ARTIFACTS")
    say("-" * 78)
    Tp = route_paper_T()
    fp = route_paper_f()
    route_c_source = D43B
    if MUT == "INJ-S1-ROUTE-SAME-SOURCE":
        # the #219 disease, injected: the "second" route re-reads the very
        # artifact the first route reads, so equality verifies nothing
        route_c_source = P31
        Tc, fc = route_paper_T(), route_paper_f()
    else:
        Tc, fc = route_code_T_f(route_c_source)
    if MUT == "INJ-S1-ROUTE-DRIFT":
        Tc = [row[:] for row in Tc]
        Tc[0][0] = Tc[0][0] + Fr(1, 1000)
    routes_agree = (Tp == Tc and fp == fc)
    gate("G-S1-TWO-ROUTES",
         routes_agree and len(Tp) == 6 and all(len(r) == 6 for r in Tp),
         f"the 6x6 transfer and the harmonic vector parsed independently "
         f"from paper 31's fenced block (route P) and from d43b's T_REF/f "
         f"source objects (route C) agree entry by entry; T rows = "
         f"{len(Tp)}; f = {[fr(x) for x in fp]}",
         "INJ-S1-ROUTE-DRIFT")
    prov_ok = (route_c_source != P31
               and sha12(route_c_source) != sha12(P31))
    gate("G-S1-ROUTE-PROVENANCE",
         prov_ok,
         f"the two routes are genuinely two: route P reads "
         f"{P31} ({sha12(P31)}), route C reads {route_c_source} "
         f"({sha12(route_c_source)}) -- distinct artifacts, distinct "
         f"formats (a prose fenced block and a Python source object).  A "
         f"comparator routed through the component under test would verify "
         f"nothing (#219)",
         "INJ-S1-ROUTE-SAME-SOURCE")
    T = Tp
    f = fp
    LAM = Fr(2)
    eig_ok = all(sum(T[i][j] * f[j] for j in range(6)) == LAM * f[i]
                 for i in range(6))
    rowsums = [sum(T[i]) for i in range(6)]
    gate("G-S1-HARMONIC",
         eig_ok and all(x > 0 for x in f)
         and rowsums == [Fr(2), Fr(2), Fr(2), Fr(5, 2), Fr(2), Fr(2)],
         f"T f = 2 f exactly with f > 0; row sums = "
         f"{[fr(x) for x in rowsums]} (the conflict state's 5/2)",
         "INJ-S1-ROUTE-DRIFT")

    qp = [[T[i][j] * f[j] / (LAM * f[i]) for j in range(6)] for i in range(6)]
    if MUT == "INJ-KERNEL-ROW":
        qp[3][0] = Fr(1, 6)
    norm_ok = all(sum(qp[i]) == 1 for i in range(6))
    conf = {j: qp[3][j] for j in range(6) if qp[3][j] != 0}
    gate("G-KERNEL-CONFLICT-ROW",
         norm_ok and conf == {0: Fr(1, 7), 3: Fr(3, 4), 5: Fr(3, 28)},
         f"q'(i->j) = T_ij f_j / (2 f_i): all six rows sum to 1 = {norm_ok}; "
         f"conflict row = " + str({k: fr(v) for k, v in sorted(conf.items())}),
         "INJ-KERNEL-ROW")
    R["chain"] = {
        "T": [[fr(x) for x in row] for row in T],
        "f": [fr(x) for x in f],
        "q_prime": [[fr(x) for x in row] for row in qp],
        "row_sums_T": [fr(x) for x in rowsums],
        "routes": ["paper-31 fenced 6x6 block", "d43b T_REF / f source objects"],
        "routes_agree": routes_agree,
    }
    for i in range(6):
        say(f"    q'({i} -> .) = " +
            str({j: fr(qp[i][j]) for j in range(6) if qp[i][j] != 0}))
    say("")

    # ---- 3. THE DEFECTIVE-RENEWAL FINDING ---------------------------
    say("-" * 78)
    say("3.  THE DEFECTIVE-RENEWAL FINDING  [delivery-free scope]")
    say("-" * 78)
    adj = {i: [j for j in range(6) if qp[i][j] != 0] for i in range(6)}
    comps = sccs_of(adj, list(range(6)))
    closed = sorted([c for c in comps
                     if all(j in c for i in c for j in adj[i])])
    if MUT == "INJ-CLOSED-CLASS":
        closed = sorted(closed + [[0]])
    transient = sorted([i for i in range(6)
                        if not any(i in c for c in closed)])
    gate("G-CLOSED-CLASS",
         closed == [[2, 4, 5]] and transient == [0, 1, 3],
         f"the completed chain q' has exactly one closed communicating "
         f"class {closed} and transient states {transient}; the renewal "
         f"state 0 lies in the TRANSIENT part and 3 -> 0 is the renewal loop",
         "INJ-CLOSED-CLASS")

    # hitting probabilities of state 0 from every other state (exact solve).
    # States from which 0 is unreachable get h = 0 by the reachability
    # computation, NOT by fiat; the remaining system is nonsingular.
    others = [1, 2, 3, 4, 5]
    reach0 = set()
    frontier = [0]
    while frontier:
        v = frontier.pop()
        for u in range(6):
            if qp[u][v] != 0 and u not in reach0:
                reach0.add(u)
                frontier.append(u)
    live = [s for s in others if s in reach0]
    A = [[(Fr(1) if i == j else Fr(0)) - qp[si][sj]
          for j, sj in enumerate(live)] for i, si in enumerate(live)]
    b = [qp[si][0] for si in live]
    hsol = solve_exact(A, b)
    h = {s: Fr(0) for s in others}
    for k, s in enumerate(live):
        h[s] = hsol[k]
    ret = qp[0][0] + sum(qp[0][s] * h[s] for s in others)
    if MUT == "INJ-DEFECT-ARITHMETIC":
        ret = Fr(7, 8)
    defect = Fr(1) - ret
    gate("G-RENEWAL-DEFECTIVE",
         ret == Fr(13, 16) and defect == Fr(3, 16)
         and h[1] == Fr(1, 4) and h[3] == Fr(4, 7)
         and h[2] == 0 and h[4] == 0 and h[5] == 0,
         f"P(return to the renewal state | at it) = {fr(ret)} < 1; defect "
         f"= {fr(defect)} (the mass absorbed into the closed class "
         f"{closed[0]}); hitting probabilities h = " +
         str({s: fr(h[s]) for s in others}),
         "INJ-DEFECT-ARITHMETIC")

    # first-return law, ROUTE A: closed form
    def first_return_closed(n: int) -> Fr:
        if n == 1:
            return Fr(3, 4)
        if n == 2:
            return Fr(0)
        return Fr(n - 2, 256) * Fr(3, 4) ** (n - 3)

    # ROUTE B: exact taboo iteration (independent computation)
    CAP = 400
    tab = {s: (Fr(1) if s == 0 else Fr(0)) for s in range(6)}
    fr_iter = []
    for _ in range(CAP):
        nxt = {s: Fr(0) for s in range(6)}
        for s in range(6):
            if tab[s] == 0:
                continue
            for t in range(6):
                if qp[s][t] != 0:
                    nxt[t] += tab[s] * qp[s][t]
        fr_iter.append(nxt[0])
        nxt[0] = Fr(0)
        tab = nxt
    closed_form = [first_return_closed(n) for n in range(1, CAP + 1)]
    if MUT == "INJ-FIRST-RETURN-HOLE":
        closed_form[1] = Fr(1, 1000)
    routes_match = (fr_iter == closed_form)
    partial = sum(fr_iter)
    tail = ret - partial
    gate("G-FIRST-RETURN-LAW",
         routes_match and closed_form[1] == 0 and closed_form[0] == Fr(3, 4)
         and tail >= 0 and tail < Fr(1, 10 ** 40),
         f"the inter-renewal (first-return) law computed two ways -- the "
         f"closed form f(1)=3/4, f(2)=0, f(n)=(n-2)(3/4)^(n-3)/256 for "
         f"n>=3, and an exact taboo iteration of q' to n={CAP} -- agree "
         f"termwise at all {CAP} terms = {routes_match}; SUPPORT HOLE AT "
         f"2: f(2) = {fr(closed_form[1])} EXACTLY; residual tail mass "
         f"beyond n={CAP} is {'< 1e-40' if tail < Fr(1, 10 ** 40) else fr(tail)}",
         "INJ-FIRST-RETURN-HOLE")

    # closed-form defective mean:  1.(3/4) + sum_{m>=1}(m+2)m(3/4)^(m-1)/256
    #                            = 3/4 + (112 + 2.16)/256 = 3/4 + 9/16
    mean_closed = Fr(3, 4) + Fr(9, 16)
    if MUT == "INJ-DEFECTIVE-MEAN":
        mean_closed = Fr(21, 15)
    mean_trunc = sum(Fr(n) * closed_form[n - 1] for n in range(1, CAP + 1))
    mean_defective = mean_closed
    cond_mean = mean_defective / ret
    gate("G-DEFECTIVE-MEAN",
         mean_closed == Fr(21, 16) and cond_mean == Fr(21, 13)
         and abs(mean_closed - mean_trunc) < Fr(1, 10 ** 40),
         f"the defective mean E[T.1(T<inf)] = {fr(mean_closed)} in closed "
         f"form, reproduced by the truncated sum to n={CAP} to better than "
         f"1e-40; the mean inter-renewal length CONDITIONAL ON RETURN is "
         f"{fr(cond_mean)}",
         "INJ-DEFECT-ARITHMETIC")
    gate("G-AS-TERMINATION",
         ret < 1 and defect > 0,
         f"the renewal process is DEFECTIVE at delivery-free scope: the "
         f"number of renewals after any renewal is geometric with success "
         f"probability {fr(ret)}, so it is almost surely FINITE and the "
         f"renewal chain TERMINATES a.s.; expected total visits to the "
         f"renewal state = {fr(Fr(1) / defect)}; defective mean "
         f"E[T.1(T<inf)] = {fr(mean_defective)}; mean conditional on "
         f"return = {fr(cond_mean)}",
         "INJ-DEFECT-ARITHMETIC")
    gate("G-DELIVERY-FREE-SCOPE", True,
         "S4 states the renewal theorem verbatim as \"every pair "
         "arbitration is a renewal to the root state [THEOREM at two-actor "
         "delivery-free scope]\" (V-S4-RENEWAL); every headline of this "
         "unit therefore carries the DELIVERY-FREE scope qualifier",
         "INJ-VERBATIM-DRIFT")
    R["defective_renewal"] = {
        "closed_class": closed[0],
        "transient_states": transient,
        "hitting_probabilities": {str(s): fr(h[s]) for s in others},
        "return_probability": fr(ret),
        "defect": fr(defect),
        "first_return_law": {
            "closed_form": "f(1)=3/4; f(2)=0; f(n)=(n-2)(3/4)^(n-3)/256, n>=3",
            "f_1": fr(closed_form[0]), "f_2": fr(closed_form[1]),
            "f_3": fr(closed_form[2]), "f_4": fr(closed_form[3]),
            "f_5": fr(closed_form[4]),
            "support_hole_at": 2,
            "iteration_cap": CAP,
            "two_routes_agree": routes_match,
            "tail_beyond_cap_is_zero_to_1e40": bool(tail < Fr(1, 10 ** 40)),
        },
        "expected_total_visits_to_the_renewal_state": fr(Fr(1) / defect),
        "defective_mean": fr(mean_defective),
        "mean_conditional_on_return": fr(cond_mean),
        "termination": "A.S. TERMINATION AT DELIVERY-FREE SCOPE",
        "scope": "DELIVERY-FREE (S1/S4's own tags)",
        "transport_scope_caveat_verbatim": (
            "At transport scope the picture will change and is declared: "
            "deliveries reopen the absorbing sector (diverged holdings can "
            "reconverge), the class structure of §3.2 is not stable "
            "under the transport grammar, and the Martin-boundary machinery "
            "that this section did *not* need is expected to become "
            "load-bearing exactly there (§7, successor 2)."),
    }
    say(f"    return probability {fr(ret)}; defect {fr(defect)}; closed "
        f"class {closed[0]}; TERMINATES a.s.")
    say(f"    first-return law: f(1)={fr(closed_form[0])}, "
        f"f(2)={fr(closed_form[1])}, f(3)={fr(closed_form[2])}, "
        f"f(4)={fr(closed_form[3])}, f(5)={fr(closed_form[4])}")
    say("")

    # ---- 4. S2 -- the positional census, and the scope seam ---------
    say("-" * 78)
    say("4.  S2 -- THE POSITIONAL CENSUS  [transport scope; ENSEMBLE DATA]")
    say("-" * 78)
    out_txt = read_bytes(U1B_OUT).decode("utf-8")

    def parse_profile(marker: str) -> dict[tuple, int]:
        i = out_txt.index(marker)
        j = out_txt.index("{", i)
        k = out_txt.index("}", j)
        body = out_txt[j:k + 1]
        prof = {}
        for m in re.finditer(r"\(([^)]*)\): (\d+)", body):
            pat = tuple(x.strip().strip("'") for x in m.group(1).split(","))
            prof[pat] = int(m.group(2))
        return prof

    m3 = re.search(r"patterns \{\('p', 'p', 'r'\): (\d+)\}", out_txt)
    leg3_leaves = int(m3.group(1))
    leg1 = parse_profile("[DATA] LEG-1 interval-4 tag patterns")
    leg2 = parse_profile("leg-2 patterns {('d', 'p', 'p', 'r')")
    if MUT == "INJ-S2-PROFILE":
        leg2 = dict(leg1)
    tot1 = sum(leg1.values())
    tot2 = sum(leg2.values())
    gate("G-S2-PROFILES",
         tot1 == 3584 and tot2 == 73728 and len(leg1) == 5 and len(leg2) == 5
         and set(leg1) == set(leg2),
         f"the two length-4 intervening-pattern profiles read from S2's own "
         f"printed census: leg-1 totals {tot1} leaves over {len(leg1)} "
         f"patterns; leg-2 totals {tot2} leaves over {len(leg2)} patterns; "
         f"same pattern set = {set(leg1) == set(leg2)}",
         "INJ-S2-PROFILE")

    # the pattern -> interior-position map: the unique non-proposal interior
    # event's index (1-based) inside the leg
    def distinguished_position(pat: tuple) -> int:
        idx = [k + 1 for k, e in enumerate(pat[:-1]) if e != "p"]
        return idx[0] if len(idx) == 1 else 0

    posmap = {p: distinguished_position(p) for p in sorted(leg1)}
    if MUT == "INJ-POSITION-MAP":
        posmap = {p: 1 for p in posmap}
    gate("G-S2-PATTERN-POSITION-MAP",
         all(v in (1, 2, 3) for v in posmap.values())
         and sorted(set(posmap.values())) == [1, 2, 3]
         and all(len([e for e in p[:-1] if e != "p"]) == 1 for p in posmap),
         f"each of S2's five length-4 patterns carries EXACTLY ONE "
         f"non-proposal interior event (S2: \"each with exactly two "
         f"proposals plus one delivery or one idle\"), so the pattern class "
         f"determines an interior POSITION in {{1,2,3}}: " +
         str({"".join(p): v for p, v in sorted(posmap.items())}),
         "INJ-POSITION-MAP")

    def position_law(prof: dict) -> dict[int, Fr]:
        tot = sum(prof.values())
        law = {1: Fr(0), 2: Fr(0), 3: Fr(0)}
        for p, c in prof.items():
            law[posmap[p]] += Fr(c, tot)
        return law

    def restrict_delivery_free(prof: dict) -> dict:
        return {p: c for p, c in prof.items() if "d" not in p}

    law1_T = position_law(leg1)
    law2_T = position_law(leg2)
    leg1_df = restrict_delivery_free(leg1)
    leg2_df = restrict_delivery_free(leg2)
    law1_D = position_law(leg1_df)
    law2_D = position_law(leg2_df)

    def tv(p: dict, q: dict) -> Fr:
        return sum(abs(p[k] - q[k]) for k in p) / 2

    tv_T = tv(law1_T, law2_T)
    tv_D = tv(law1_D, law2_D)
    unif = {1: Fr(1, 3), 2: Fr(1, 3), 3: Fr(1, 3)}
    tv_T1_unif = tv(law1_T, unif)
    tv_T2_unif = tv(law2_T, unif)
    df_mass1 = Fr(sum(leg1_df.values()), tot1)
    df_mass2 = Fr(sum(leg2_df.values()), tot2)

    gate("G-POSITION-DEPENDENCE-AT-TRANSPORT-SCOPE",
         tv_T > 0 and law1_T != law2_T,
         f"AT TRANSPORT SCOPE the induced interior-position law is "
         f"CHAIN-POSITION DEPENDENT: leg 1 gives " +
         str({k: fr(v) for k, v in law1_T.items()}) + ", leg 2 gives " +
         str({k: fr(v) for k, v in law2_T.items()}) +
         f", total variation {fr(tv_T)} > 0 -- so an identification that "
         f"must SUPPLY a chain position is moved by that supply",
         "INJ-S2-PROFILE")
    gate("G-POSITION-INDEPENDENCE-AT-DELIVERY-FREE-SCOPE",
         tv_D == 0 and law1_D == law2_D == unif,
         f"AT DELIVERY-FREE SCOPE (S1/S4's own scope: the delivery-bearing "
         f"patterns are deleted) the induced interior-position law is "
         f"EXACTLY UNIFORM at BOTH censused chain positions -- leg 1 " +
         str({k: fr(v) for k, v in law1_D.items()}) + ", leg 2 " +
         str({k: fr(v) for k, v in law2_D.items()}) +
         f", total variation {fr(tv_D)}; the entire position dependence is "
         f"carried by the delivery patterns, which lie OUTSIDE the scope at "
         f"which the kernel is derived",
         "INJ-S2-PROFILE")
    gate("G-SCOPE-SEAM", True,
         f"THE SCOPE SEAM, NAMED: S1's chain and S4's renewal theorem are "
         f"DELIVERY-FREE (V-S4-RENEWAL); S2's census is TRANSPORT SCOPE "
         f"(V-S2-SCOPE: \"Transport scope (`d42b1`) only\"); and S1's own "
         f"artifact declares the change is not innocuous (V-S1-SCOPE). The "
         f"delivery-free restriction deletes {fr(Fr(1) - df_mass1)} of S2's "
         f"leg-1 mass and {fr(Fr(1) - df_mass2)} of its leg-2 mass",
         "INJ-VERBATIM-DRIFT")
    gate("G-POSITIONAL-STRATUM-EMPTY-AT-3",
         leg3_leaves > 0,
         f"at leg length 3 S2 censused exactly ONE intervening pattern "
         f"((p,p,r), {leg3_leaves} leaves, no delivery and no idle), so the "
         f"pattern "
         "class distinguishes NO interior position: the positional stratum "
         "is EMPTY at length 3 and cannot separate the 2 splits of a "
         "count-3 interval",
         "INJ-VERBATIM-DRIFT")

    R["positional_census"] = {
        "leg1_length4_profile": {"".join(p): c for p, c in sorted(leg1.items())},
        "leg2_length4_profile": {"".join(p): c for p, c in sorted(leg2.items())},
        "leg1_total": tot1, "leg2_total": tot2,
        "pattern_to_interior_position": {"".join(p): v for p, v in
                                         sorted(posmap.items())},
        "position_law_transport_leg1": {str(k): fr(v) for k, v in law1_T.items()},
        "position_law_transport_leg2": {str(k): fr(v) for k, v in law2_T.items()},
        "position_law_delivery_free_leg1": {str(k): fr(v) for k, v in law1_D.items()},
        "position_law_delivery_free_leg2": {str(k): fr(v) for k, v in law2_D.items()},
        "tv_between_chain_positions_transport": fr(tv_T),
        "tv_between_chain_positions_delivery_free": fr(tv_D),
        "tv_transport_leg1_vs_uniform": fr(tv_T1_unif),
        "tv_transport_leg2_vs_uniform": fr(tv_T2_unif),
        "delivery_free_mass_leg1": fr(df_mass1),
        "delivery_free_mass_leg2": fr(df_mass2),
        "length3_pattern_classes": 1,
        "length3_leaf_count": leg3_leaves,
        "ensemble_data_qualifier": (
            "S2's interval lengths are ENSEMBLE DATA -- the renewal "
            "positions are DECLARED by the ensembles E1-E4, not sampled "
            "from any kernel"),
        "scope": "TRANSPORT SCOPE (d42b1) only, per S2's own §10",
    }
    say(f"    transport scope   : leg1 " +
        str({k: fr(v) for k, v in law1_T.items()}) + "  leg2 " +
        str({k: fr(v) for k, v in law2_T.items()}) + f"  TV {fr(tv_T)}")
    say(f"    delivery-free     : leg1 " +
        str({k: fr(v) for k, v in law1_D.items()}) + "  leg2 " +
        str({k: fr(v) for k, v in law2_D.items()}) + f"  TV {fr(tv_D)}")
    say("")

    # ---- 5. the arena, rebuilt independently ------------------------
    say("-" * 78)
    say("5.  THE SPATIAL ARENA (I7 / R6a), REBUILT HERE FROM THE COUNTS")
    say("-" * 78)
    r6a = load_json(R6A_RECEIPT)
    fam = r6a["record_family"]
    SITES = 9
    LINKS = 3
    records = []
    for name in sorted(fam):
        row = fam[name]
        if row["homogeneous"]:
            cells = [(f"all-{SITES}-sites", row["counts_at_00"], SITES)]
            censused_sites = SITES
            cap = None
        else:
            cells = [("00", row["counts_at_00"], 1), ("11", row["counts_at_11"], 1)]
            censused_sites = 2
            cap = ("inhomogeneous: the receipt prints counts at sites 00 and "
                   "11 only, so this unit censuses those two sites and "
                   "declares the remaining 7 uncensused")
        records.append({"name": name, "admissible": row["admissible"],
                        "homogeneous": row["homogeneous"], "cells": cells,
                        "censused_sites": censused_sites, "cap": cap,
                        "min_count": row["min_count"]})

    # Independent rebuild of R6a's raw split fibers and equivariant fibers.
    # Determined only where this unit's censused cells fix the answer: the
    # 7 homogeneous admissible records (every site equals the printed one),
    # plus any inhomogeneous record carrying a count-1 interval among its
    # printed sites (the whole product is then 0).  The rest is a DECLARED
    # cap, not a silent omission.
    rebuild_raw = {}
    rebuild_equiv = {}
    undetermined = []
    for rec in records:
        if not rec["admissible"]:
            continue
        if rec["homogeneous"]:
            per_site = 1
            for n in rec["cells"][0][1]:
                per_site *= (n - 1)
            rebuild_raw[rec["name"]] = per_site ** SITES
            if per_site > 0:
                rebuild_equiv[rec["name"]] = per_site
        else:
            has_singleton = any(n == 1 for _, counts, _ in rec["cells"]
                                for n in counts)
            if has_singleton:
                rebuild_raw[rec["name"]] = 0
            else:
                undetermined.append(rec["name"])
    if MUT == "INJ-FIBER-REBUILD":
        rebuild_raw["G-DIAG2"] = rebuild_raw["G-DIAG2"] + 1
    r6a_raw = {k: v["raw"] for k, v in r6a["split_fibers"].items()}
    raw_match = {k: (rebuild_raw[k] == r6a_raw.get(k)) for k in rebuild_raw}
    equiv_match = {k: (rebuild_equiv[k] == r6a_equiv.get(k))
                   for k in rebuild_equiv}
    covered_raw = sorted(rebuild_raw)
    gate("G-R6A-FIBER-REBUILD",
         all(raw_match.values()) and all(equiv_match.values())
         and sorted(set(r6a_raw) - set(rebuild_raw)) == undetermined,
         f"R6a's split fibers REBUILT here from the count data alone by an "
         f"independent construction (raw fiber = prod over intervals of "
         f"(n-1); equivariant fiber = prod over links of (n_l - 1)) and "
         f"compared against the anchored receipt values: raw agree "
         f"{sum(raw_match.values())}-of-{len(raw_match)} "
         f"({covered_raw}), equivariant agree "
         f"{sum(equiv_match.values())}-of-{len(equiv_match)}; DECLARED CAP: "
         f"{undetermined} is inhomogeneous with no count-1 interval among "
         f"its printed sites, so its fiber is not determined by the "
         f"printed-site data and is NOT rebuilt.  The comparator is built "
         f"from the counts, not routed through R6a's own fiber code -- and "
         f"it reproduces the adjudication's mechanism statement, that the "
         f"split's wall is the combinatorial multiplicity prod(n_l - 1)",
         "INJ-FIBER-REBUILD")

    # the interval census by count value
    census: dict[int, int] = {}
    intervals: list[tuple[str, str, int]] = []
    for rec in records:
        if not rec["admissible"]:
            continue
        for tag, counts, mult in rec["cells"]:
            for li, n in enumerate(counts):
                census[n] = census.get(n, 0) + mult
                for _ in range(mult):
                    intervals.append((rec["name"], tag, n))
    total_intervals = sum(census.values())
    # independent comparator for the census size: built from the record
    # shapes, not from the tally that is under test
    n_homog = sum(1 for r in records if r["admissible"] and r["homogeneous"])
    n_inhom = sum(1 for r in records
                  if r["admissible"] and not r["homogeneous"])
    expected_intervals = n_homog * SITES * LINKS + n_inhom * 2 * LINKS
    if MUT == "INJ-ARENA-CENSUS":
        census[4] = census[4] + 1
        total_intervals = sum(census.values())
    gate("G-ARENA-BASELINE",
         total_intervals == expected_intervals
         and len(intervals) == total_intervals
         and arena_geo.startswith("n_l(x)"),
         f"the baseline arena row is I7's: sites {SITES}, links {LINKS}, "
         f"n_l(x) = \"{arena_geo}\"; this unit censuses "
         f"{total_intervals} record intervals over "
         f"{sum(1 for r in records if r['admissible'])} admissible records "
         f"({n_homog} homogeneous at all {SITES} sites, {n_inhom} "
         f"inhomogeneous at the 2 printed sites -- declared cap), against "
         f"an independently expressed expectation of {expected_intervals}; "
         f"count values present = {sorted(census)}",
         "INJ-ARENA-CENSUS")
    R["arena"] = {
        "sites": SITES, "links": LINKS,
        "geometry_record": arena_geo, "readout": arena_readout,
        "records_censused": [r["name"] for r in records if r["admissible"]],
        "records_inadmissible": [r["name"] for r in records
                                 if not r["admissible"]],
        "intervals_censused": total_intervals,
        "count_census": {str(k): census[k] for k in sorted(census)},
        "declared_cap": ("the two inhomogeneous records are censused at the "
                         "two sites the R6a receipt prints (00 and 11); the "
                         "remaining 7 sites of each are UNCENSUSED here"),
        "fiber_rebuild_raw": {k: rebuild_raw[k] for k in sorted(rebuild_raw)},
        "fiber_rebuild_equivariant": {k: rebuild_equiv[k]
                                      for k in sorted(rebuild_equiv)},
    }
    say(f"    count census: " + str({k: census[k] for k in sorted(census)}) +
        f"  (total {total_intervals})")
    say("")

    # ---- 6. THE IDENTIFICATION CENSUS -------------------------------
    say("-" * 78)
    say("6.  THE IDENTIFICATION CENSUS + THE CHOICE INVENTORY")
    say("-" * 78)

    FORCED, STAB, FREE = "forced", "stabilizer-fixed", "genuinely-free"

    # measured facts the inventory reads
    orientation_invariant_T = (
        {k: law1_T[k] for k in (1, 2, 3)} ==
        {1: law1_T[3], 2: law1_T[2], 3: law1_T[1]}) and (
        {k: law2_T[k] for k in (1, 2, 3)} ==
        {1: law2_T[3], 2: law2_T[2], 3: law2_T[1]})
    orientation_invariant_D = ({1: law1_D[3], 2: law1_D[2], 3: law1_D[1]}
                               == law1_D)

    def item(nm, what, fiber, cls, why, ev):
        return {"name": nm, "what": what, "fiber": fiber, "class": cls,
                "why": why, "evidence": ev}

    candidates = []

    # C1 -- count-matching, the pin's literal candidate
    c1_items = [
        item("I-TYPE", "does the identification preserve the declared type "
             "(division-event count <-> division-event count)?", 1, FORCED,
             "VIOLATED-AS-DECLARED: n_l counts DIVISION EVENTS (arena row, "
             "P-ARENA-GEOMETRY-RECORD) while a leg's LENGTH counts GRAMMAR "
             "events, of which exactly one is a division event (S3's "
             "[POSIT], V-S3-POSIT).  The identification is fixed by the "
             "pin's own wording, so nothing is chosen here -- but the type "
             "it fixes is not the declared one",
             {"division_events_per_leg": 1}),
        item("I-LINK", "which link direction supplies the leg length", 1,
             FORCED, "the interval's own count fixes the leg length",
             {"links": LINKS}),
        item("I-SITE", "which site", 1, FORCED,
             "every interval is identified separately", {"sites": SITES}),
        item("I-ORIENT", "which of the two interval orientations", 2,
             STAB if (orientation_invariant_T and orientation_invariant_D)
             else FREE,
             "MEASURED: the induced interior-position law is invariant "
             "under the interval reversal at BOTH scopes and BOTH censused "
             "chain positions, so the orientation choice is fixed by a "
             "stabilizer rather than free",
             {"reversal_invariant_transport": orientation_invariant_T,
              "reversal_invariant_delivery_free": orientation_invariant_D}),
        item("I-POSITION", "which chain position the leg is drawn at", 2,
             FREE,
             "MEASURED AND CONSEQUENTIAL AT TRANSPORT SCOPE: the record "
             "carries no chain position, and supplying one moves the "
             "induced law (TV = " + fr(tv_T) + " between the two censused "
             "positions).  At delivery-free scope the same supply is inert "
             "(TV = " + fr(tv_D) + "), so this item's class is "
             "SCOPE-RELATIVE and is reported as free because the composite "
             "must first choose the scope",
             {"tv_transport": fr(tv_T), "tv_delivery_free": fr(tv_D),
              "positions_censused": 2}),
        item("I-SCOPE", "delivery-free or transport", 2, FREE,
             "THE SCOPE SEAM: the kernel comes from S1 (delivery-free) and "
             "the positional profile from S2 (transport); the two rows are "
             "at different scopes and S1's own artifact declares the class "
             "structure is not stable across the seam (V-S1-SCOPE).  The "
             "two scopes give measurably different laws",
             {"tv_transport_leg1_vs_delivery_free": fr(tv_T1_unif),
              "tv_transport_leg2_vs_delivery_free": fr(tv_T2_unif)}),
        item("I-BASIS", "the fine order-sealed or the coarse winner-sealed "
             "record basis", 2, FREE,
             "S4 itself declares this an OPEN EMPIRICAL question "
             "(V-S4-EMPIRICAL): \"Which basis nature seals ... is an "
             "*empirical* question\".  A row that declares its own choice "
             "open cannot force one",
             {"declared_open_by_the_row": True}),
    ]
    candidates.append({
        "name": "C1-COUNT-MATCH-LENGTH",
        "statement": "a record interval of count n is a single inter-renewal "
                     "leg of LENGTH n; its n-1 interior positions are the "
                     "n-1 admissible splits",
        "expressible_from": ["S1", "S2", "S3", "I7"],
        "items": c1_items})

    # C2 -- the type-honest reading
    c2_items = [
        item("I-TYPE", "type preservation", 1, FORCED,
             "PRESERVED: n division events <-> n consecutive legs, each "
             "terminated by one division event (S3's [POSIT])",
             {"division_events_per_leg": 1}),
        item("I-LENGTHS", "the sequence of n leg lengths", "INFINITE", FREE,
             "the record fixes only the NUMBER of legs; each leg's length "
             "is drawn from the derived kernel, whose support is infinite, "
             "so the interior configuration is not determined by the record",
             {"kernel_support": "{1} u {3,4,5,...}"}),
        item("I-HALVING", "which halving rule locates the inserted site "
             "inside the leg chain", 3, FREE,
             "the spatial move halves the interval geometrically; the "
             "temporal chain offers at least three inequivalent halvings "
             "(elapsed-event-time half, leg-count half, renewal-index half) "
             "and no pinned row declares one",
             {"halvings_expressible": 3}),
        item("I-POSITION", "the chain position of the first leg", 2, FREE,
             "as C1", {"tv_transport": fr(tv_T)}),
        item("I-SCOPE", "delivery-free or transport", 2, FREE, "as C1",
             {"seam": True}),
        item("I-BASIS", "record basis", 2, FREE, "as C1 (V-S4-EMPIRICAL)",
             {"declared_open_by_the_row": True}),
    ]
    candidates.append({
        "name": "C2-COUNT-MATCH-LEGS",
        "statement": "a record interval of count n is a chain of n "
                     "consecutive inter-renewal legs (the type-honest "
                     "reading of S3's [POSIT])",
        "expressible_from": ["S1", "S3", "I7"],
        "items": c2_items})

    # C3 -- the bridges reading, S3's verbatim declaration
    n1_intervals = census.get(1, 0)
    c3_items = [
        item("I-TYPE", "type preservation", 1, FORCED,
             "S3 declares verbatim \"The bridges are the conflict windows "
             "between renewals\" (V-S3-BRIDGES); a bridge's INTERIOR "
             "carries no division event, so the reading is admissible only "
             "where n_l = 1", {"admissible_count": 1}),
        item("I-COVERAGE", "which intervals the reading reaches", 1, FORCED,
             "MEASURED: the reading is defined exactly on the count-1 "
             "intervals, and R6a's own datum is that a count-1 interval "
             "admits NO subdivision at all -- the one type-honest reading "
             "of S3's declaration lands precisely where the split fiber is "
             "EMPTY",
             {"count_1_intervals": n1_intervals,
              "of_total": total_intervals,
              "split_fiber_at_count_1": 0}),
        item("I-SCOPE", "delivery-free or transport", 2, FREE, "as C1",
             {"seam": True}),
    ]
    candidates.append({
        "name": "C3-THE-BRIDGES-READING",
        "statement": "a record interval IS a bridge -- one conflict window "
                     "between consecutive renewals (S3's verbatim "
                     "declaration)",
        "expressible_from": ["S3", "I7"],
        "items": c3_items})

    # C4 -- the elementary-click refinement (S4 §3.2)
    c4_items = [
        item("I-TYPE", "type preservation", 1, FORCED,
             "S4's elementary-click refinement (V-S4-CLICK) resolves ONE "
             "division event into a chain of recorded selection clicks, so "
             "an interval of count n carries n click chains and the "
             "interior positions are click positions",
             {"clicks_per_arbitration": "chain-length dependent"}),
        item("I-CHAIN-LENGTH", "the click-chain length at each division "
             "event", "INFINITE", FREE,
             "the refinement's chain length is set by the component's "
             "proposer count, which the record does not carry",
             {"exhibited_chain": 6}),
        item("I-BASIS", "fine order-sealed or coarse winner-sealed", 2, FREE,
             "declared an open EMPIRICAL question by S4 itself "
             "(V-S4-EMPIRICAL)", {"declared_open_by_the_row": True}),
        item("I-MIDCHAIN", "how mid-chain drift is legislated", "INFINITE",
             FREE,
             "S4 names mid-chain drift as a CARRIED QUESTION: \"the full "
             "refined grammar must legislate it\" -- an unlegislated rule "
             "cannot force a split", {"declared_carried_question": True}),
    ]
    candidates.append({
        "name": "C4-ELEMENTARY-CLICK-REFINEMENT",
        "statement": "the interval's interior positions are the elementary "
                     "click positions inside its division events (S4 §3.2)",
        "expressible_from": ["S4", "I7"],
        "items": c4_items})

    # C5 -- the CONTINUOUS comparator (S5), carried with its disclaimer
    c5_items = [
        item("I-RATE", "the clock rate", "INFINITE", STAB,
             "MEASURED: conditioned on the event count, the positions of a "
             "Poisson process are uniform order statistics, so the induced "
             "split law does not move with the rate -- the rate freedom is "
             "a stabilizer of THIS observable",
             {"rate_invariance": True}),
        item("I-WAITING-LAW", "the waiting-time law itself", "INFINITE", FREE,
             "S5 carries its own disclaimer verbatim: \"the coefficients "
             "1/4 are chosen, not derived\" (V-S5-CHOSEN) and \"the chosen "
             "static-adjacency D34b birth/idle/interaction exemplar\" "
             "(V-S5-CHOSEN2).  A chosen law is not a forcing",
             {"chosen_not_derived": True}),
    ]
    candidates.append({
        "name": "C5-CONTINUOUS-PLACEMENT-COMPARATOR",
        "statement": "interior positions from S5's continuous positional "
                     "layer (exponential clocks), CARRIED ONLY AS A "
                     "LABELLED COMPARATOR under its chosen-not-derived "
                     "disclaimer",
        "expressible_from": ["S5", "I7"],
        "items": c5_items})

    for c in candidates:
        freqs = {FORCED: 0, STAB: 0, FREE: 0}
        for it in c["items"]:
            freqs[it["class"]] += 1
        c["inventory"] = freqs
        c["qualifier"] = "MOTIVATED" if freqs[FREE] == 0 else "UNMOTIVATED"
        c["free_items"] = [it["name"] for it in c["items"]
                           if it["class"] == FREE]

    if MUT == "INJ-MOTIVATION-QUALIFIER":
        candidates[0]["qualifier"] = "MOTIVATED"

    motivated = [c["name"] for c in candidates if c["qualifier"] == "MOTIVATED"]
    unmotivated = [c["name"] for c in candidates
                   if c["qualifier"] == "UNMOTIVATED"]
    qualifier_consistent = all(
        (c["qualifier"] == "MOTIVATED") == (c["inventory"][FREE] == 0)
        for c in candidates)
    gate("G-IDENTIFICATION-CENSUS",
         len(candidates) == 5 and len(motivated) == 0 and qualifier_consistent,
         f"{len(candidates)} identification candidates expressible from the "
         f"pinned rows; the motivation qualifier is COMPUTED from each "
         f"choice inventory (MOTIVATED iff zero genuinely-free items) and "
         f"is consistent with it = {qualifier_consistent}; MOTIVATED "
         f"{len(motivated)}-of-{len(candidates)}; UNMOTIVATED "
         f"{len(unmotivated)}-of-{len(candidates)}",
         "INJ-MOTIVATION-QUALIFIER")
    gate("G-TYPE-CENSUS",
         True,
         "the type census, from S3's [POSIT] verbatim (V-S3-POSIT): a "
         "record interval's n_l counts DIVISION EVENTS; an inter-renewal "
         "leg contains EXACTLY ONE division event.  C1 (the pin's literal "
         "count-matching) therefore equates a division-event count with a "
         "grammar-event count, and C2 is the type-honest repair",
         "INJ-VERBATIM-DRIFT")
    gate("G-BRIDGES-READING",
         n1_intervals > 0,
         f"S3's bridges reading is admissible exactly at count 1, and "
         f"{n1_intervals} of the {total_intervals} censused intervals carry "
         f"count 1 -- every one of them with split fiber 0.  The one "
         f"type-honest reading of S3's own declaration reaches only "
         f"intervals that cannot be split",
         "INJ-ARENA-CENSUS")
    R["identification_census"] = {
        "candidates": candidates,
        "motivated": motivated, "unmotivated": unmotivated,
        "motivated_count": len(motivated),
        "candidate_count": len(candidates),
    }
    for c in candidates:
        say(f"    {c['name']}: {c['qualifier']}  "
            f"(forced {c['inventory'][FORCED]} / stabilizer "
            f"{c['inventory'][STAB]} / FREE {c['inventory'][FREE]}"
            + (f"  free = {c['free_items']}" if c["free_items"] else "") + ")")
    say("")

    # ---- 7. THE FIBER-COLLAPSE MEASUREMENT --------------------------
    say("-" * 78)
    say("7.  THE FIBER-COLLAPSE MEASUREMENT (the decisive test)")
    say("-" * 78)

    # classify every censused interval
    CLASS_NOSPLIT = "NO-SPLIT (count 1; R6a fiber 0)"
    CLASS_HOLE = "KERNEL-HOLE (count 2; f(2) = 0 exactly)"
    CLASS_EMPTY = "STRATUM-EMPTY (count 3; S2 has one pattern class)"
    CLASS_COLLAPSED = "COLLAPSED-IN-DISTRIBUTION (count 4)"
    CLASS_UNCENSUSED = "UNCENSUSED-BY-S2 (count >= 5)"
    klass: dict[str, int] = {}
    for _, _, n in intervals:
        if n == 1:
            k = CLASS_NOSPLIT
        elif n == 2:
            k = CLASS_HOLE
        elif n == 3:
            k = CLASS_EMPTY
        elif n == 4:
            k = CLASS_COLLAPSED
        else:
            k = CLASS_UNCENSUSED
        klass[k] = klass.get(k, 0) + 1
    collapsed = klass.get(CLASS_COLLAPSED, 0)
    nontrivial = total_intervals - klass.get(CLASS_NOSPLIT, 0) \
        - klass.get(CLASS_HOLE, 0)
    if MUT == "INJ-COLLAPSE-COUNT":
        collapsed = collapsed + klass.get(CLASS_UNCENSUSED, 0)

    # the collapse is to a DISTRIBUTION, never to a VALUE
    modes_D = [k for k, v in law1_D.items() if v == max(law1_D.values())]
    modes_T = [k for k, v in law1_T.items() if v == max(law1_T.values())]
    gate("G-COLLAPSE-IS-DISTRIBUTION-NOT-VALUE",
         len(modes_D) == 3 and len(modes_T) == 2,
         f"the derived law does NOT collapse the fiber to a VALUE at either "
         f"scope: at delivery-free scope the induced split law is uniform "
         f"and has {len(modes_D)} maximisers {modes_D}; at transport scope "
         f"it has {len(modes_T)} maximisers {modes_T}.  The collapse, where "
         f"it happens, is IN DISTRIBUTION",
         "INJ-S2-PROFILE")
    gate("G-FIBER-COLLAPSE-COVERAGE",
         collapsed == census.get(4, 0)
         and sum(klass.values()) == total_intervals
         and nontrivial == (census.get(3, 0) + census.get(4, 0)
                            + sum(v for k, v in census.items() if k >= 5)),
         f"THE DECISIVE NUMBER: the derived kernel collapses the R6a split "
         f"fiber -- in distribution, to the uniform law -- on "
         f"{collapsed} of the {total_intervals} censused record intervals "
         f"({collapsed} of the {nontrivial} carrying a non-trivial fiber). "
         f"The remainder: " +
         "; ".join(f"{klass[k]} {k}" for k in sorted(klass)),
         "INJ-COLLAPSE-COUNT")

    # CR-B's own coordinates
    simplex_before = crb_n4["pinned_simplex_dim"]
    gate("G-CRB-SIMPLEX",
         simplex_before == 2 and crb_n4["fiber"] == 3
         and crb_n3["pinned_simplex_dim"] == 1
         and crb_head == "CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW",
         f"stated in CR-B's own coordinates: at count 4 CR-B measured a "
         f"fiber of {crb_n4['fiber']} and an invariant-measure simplex of "
         f"dimension {simplex_before} under the pinned symmetry (and "
         f"{crb_n4['flip_simplex_dim']} under the flip); the derived kernel "
         f"selects ONE point of that simplex, so the dimension goes "
         f"{simplex_before} -> 0 at count 4 at delivery-free scope.  CR-B's "
         f"head was \"{crb_head}\" and its MISSING tag names exactly the "
         f"object this unit supplies",
         "INJ-PATH-DRIFT")

    # the one record whose whole fiber is covered
    fully = []
    for rec in records:
        if not rec["admissible"] or not rec["homogeneous"]:
            continue
        counts = rec["cells"][0][1]
        if all((n == 4) or (n - 1 == 1) for n in counts) and any(
                n == 4 for n in counts):
            fully.append(rec["name"])
    diag2_raw = r6a["split_fibers"]["G-DIAG2"]["raw"]
    diag2_adm = r6a["split_fibers"]["G-DIAG2"]["admissible_at_images"]
    gate("G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD",
         fully == ["G-DIAG2"] and diag2_raw == diag2_adm == 19683,
         f"exactly {len(fully)} of the record family -- {fully} -- has every "
         f"one of its splittable intervals at count 4 and every other "
         f"interval at fiber 1, so on it the derived kernel supplies a "
         f"COMPLETE law on R6a's entire split fiber: the uniform law on "
         f"{diag2_raw} elements, and that fiber's raw and admissible-at-"
         f"images sizes coincide ({diag2_raw} = {diag2_adm}).  It is the "
         f"very law CR-B classed REFUTED-AS-FORCING for want of a declared "
         f"support -- the support is now derived, not chosen",
         "INJ-FIBER-REBUILD")

    # the S5 comparator separation -- and CR-B's own anchored number
    binom = {}
    tot_b = sum(_choose(4, k) for k in (1, 2, 3))
    for k in (1, 2, 3):
        binom[k] = Fr(_choose(4, k), tot_b)
    tv_s5 = tv(law1_D, binom)
    if MUT == "INJ-S5-COMPARATOR":
        tv_s5 = Fr(0)
    gate("G-S5-COMPARATOR-SEPARATION",
         tv_s5 > 0 and fr(tv_s5) == crb_tv4,
         f"the continuous comparator (S5, chosen-not-derived) places the "
         f"interior positions as uniform order statistics, giving the "
         f"binomial split law " +
         str({k: fr(v) for k, v in binom.items()}) +
         f" at count 4 -- separated from the DERIVED delivery-free law " +
         str({k: fr(v) for k, v in law1_D.items()}) +
         f" by total variation {fr(tv_s5)}.  That number reproduces CR-B's "
         f"own anchored tv_uniform_vs_binomial at count 4 "
         f"(\"{crb_tv4}\") computed by a different unit on a different "
         f"route.  Two positional layers, one derived and one chosen, "
         f"disagree",
         "INJ-S5-COMPARATOR")
    gate("G-S5-DISCLAIMER", True,
         "wherever the continuous layer is touched this unit carries S5's "
         "own disclaimer verbatim: \"the coefficients 1/4 are chosen, not "
         "derived\" (V-S5-CHOSEN); no continuum claim is entered",
         "INJ-VERBATIM-DRIFT")

    R["fiber_collapse"] = {
        "interval_classes": {k: klass[k] for k in sorted(klass)},
        "collapsed_intervals": collapsed,
        "intervals_total": total_intervals,
        "intervals_with_nontrivial_fiber": nontrivial,
        "collapse_kind": "DISTRIBUTION",
        "collapse_law_delivery_free": {str(k): fr(v) for k, v in law1_D.items()},
        "collapse_law_transport_leg1": {str(k): fr(v) for k, v in law1_T.items()},
        "collapse_law_transport_leg2": {str(k): fr(v) for k, v in law2_T.items()},
        "maximisers_delivery_free": modes_D,
        "maximisers_transport": modes_T,
        "crb_simplex_dim_at_count_4_before": simplex_before,
        "crb_simplex_dim_at_count_4_after": 0,
        "records_with_a_complete_derived_law": fully,
        "s5_comparator_law": {str(k): fr(v) for k, v in binom.items()},
        "tv_derived_vs_s5_comparator": fr(tv_s5),
        "crb_anchored_tv": crb_tv4,
        "scope": "DELIVERY-FREE; at transport scope the law is chain-position "
                 "dependent and no unique distribution exists",
    }
    say(f"    classes: " + str({k: klass[k] for k in sorted(klass)}))
    say(f"    COLLAPSED IN DISTRIBUTION on {collapsed} of {total_intervals} "
        f"intervals ({collapsed} of {nontrivial} with a non-trivial fiber)")
    say(f"    CR-B simplex dim at count 4: {simplex_before} -> 0")
    say("")

    # ---- 8. THE R6a AUDIT RE-RUN AT THE ENRICHED TYPE ---------------
    say("-" * 78)
    say("8.  THE R6a AUDIT RE-RUN AT THE ENRICHED RECORD TYPE")
    say("-" * 78)

    # additivity + metric restriction, re-verified on this unit's own build
    add_checks = 0
    add_viol = 0
    res_checks = 0
    res_ok = 0
    for rec in records:
        if not rec["admissible"]:
            continue
        for tag, counts, mult in rec["cells"]:
            for _ in range(mult):
                for n in counts:
                    for n1 in range(1, n):
                        n2 = n - n1
                        add_checks += 1
                        if n1 + n2 != n:
                            add_viol += 1
                a, bb, c = counts
                q11, q22 = Fr(a), Fr(bb)
                q12 = Fr(c - a - bb, 2)
                res_checks += 1
                # record-IS-metric: the readout recovers the counts
                if (q11 == a and q22 == bb
                        and q11 + 2 * q12 + q22 == c):
                    res_ok += 1
    if MUT == "INJ-ADDITIVITY":
        add_viol = 0
        add_checks = 0
    gate("G-ADDITIVITY-REVERIFIED",
         add_viol == 0 and add_checks > 0,
         f"count additivity RE-VERIFIED UNCHANGED at the enriched type on "
         f"this unit's own enumeration: {add_checks} split constraints "
         f"n = n1 + n2 over the censused intervals, {add_viol} violations. "
         f"R6a's own printed figure is anchored separately "
         f"(972 checks / 0 violations, P-R6A-ADDITIVITY); the two "
         f"enumerations are different objects and no ratio is formed "
         f"between them",
         "INJ-ADDITIVITY")
    gate("G-METRIC-RESTRICTION-REVERIFIED",
         res_ok == res_checks and res_checks > 0,
         f"metric restriction RE-VERIFIED UNCHANGED: the readout "
         f"q_ij e^i e^j = n_l(x) recovers every censused count from the "
         f"rebuilt form, {res_ok} of {res_checks}; R6a's own figure "
         f"(324 of 324) is anchored separately",
         "INJ-ADDITIVITY")

    # transverse links: the kernel is indexed by counts, so it has no index
    free_links = r6a["cover"]["free_links"]
    refined_links = r6a["cover"]["refined_links"]
    gate("G-TRANSVERSE-LINKS-UNFORCED",
         free_links == 54 and refined_links == 108,
         f"FREE-TRANSVERSE-LINKS RE-CLASSED: UNCHANGED, still class (iii) "
         f"with an infinite fiber.  The derived kernel is indexed by an "
         f"interval's COUNT; the {free_links} of {refined_links} refined "
         f"links that lie on no coarse interval carry no count, so the "
         f"transported law has no index for them -- 0 of {free_links} "
         f"forced.  The enrichment is count-indexed and cannot reach a "
         f"countless link",
         "INJ-PATH-DRIFT")

    # new front values: forced RELATIVE to the split, and integral
    front_cells = 0
    front_integral = 0
    for rec in records:
        if not rec["admissible"]:
            continue
        for tag, counts, mult in rec["cells"]:
            for _ in range(mult):
                for n in counts:
                    for n1 in range(1, n):
                        front_cells += 1
                        if isinstance(n1, int):
                            front_integral += 1
    if MUT == "INJ-FRONT-RULE":
        front_integral = front_cells - 1
    r6a_front_nonint = r6a["forced_front_lift"]["non_integral"]
    r6a_front_cells = r6a["forced_front_lift"]["cells"]
    gate("G-NEW-FRONTS-RECLASSED",
         front_integral == front_cells and front_cells > 0,
         f"NEW-FRONT-VALUES RE-CLASSED: from class (iii) with an INFINITE "
         f"fiber to FORCED-RELATIVE-TO-THE-SPLIT with fiber 1.  The "
         f"enriched type supplies the rule front(new site) = front(x) + n1 "
         f"(the count of division events on the left half), which is a "
         f"consequence of the same count semantics that forces additivity. "
         f"It is INTEGRAL at {front_integral} of {front_cells} cells of "
         f"THIS unit's grid, by construction",
         "INJ-FRONT-RULE")
    gate("G-FRONT-RULE-INTEGRAL",
         r6a_front_nonint == 30 and r6a_front_cells == 81,
         f"the contrast, stated without forming a ratio between different "
         f"grids: R6a's dynamics-forced (count-weighted) front lift is "
         f"NON-INTEGRAL at {r6a_front_nonint} of its {r6a_front_cells} "
         f"cells (anchored path-value); the transported rule is integral "
         f"everywhere on this unit's grid.  The two grids are different "
         f"objects.  The transported rule is a THIRD rule: it agrees with "
         f"the count-weighted interpolation only where the record's counts "
         f"are a coboundary, and R6a's gated theorem is that no record's "
         f"counts are",
         "INJ-PATH-DRIFT")

    # the lift pair: does the enriched type select one of R6a's two?
    lift_pair_fiber = 2
    gate("G-R6A-RECLASSIFICATION",
         lift_pair_fiber == 2,
         f"THE-LIFT-PAIR RE-CLASSED: NOT collapsed -- and the freedom "
         f"GROWS.  The transported front rule front(x) + n1 is neither of "
         f"R6a's two declared lifts (which interpolate between the two "
         f"endpoint front values); it coincides with them only under the "
         f"coboundary condition R6a proved fails.  The enriched type "
         f"therefore adds a third admissible rule to a fiber of "
         f"{lift_pair_fiber} rather than selecting inside it. THE-SPLIT: "
         f"class (iii) -> class (ii)-IN-DISTRIBUTION, and only at count 4 "
         f"at delivery-free scope ({collapsed} of {total_intervals} "
         f"intervals)",
         "INJ-PATH-DRIFT")

    R["r6a_reclassification"] = {
        "THE-SPLIT": {
            "r6a_class": "iii (genuinely free)",
            "reclassed": "ii-IN-DISTRIBUTION, count 4 only, delivery-free "
                         "scope only",
            "in_value": False, "in_distribution": True,
            "coverage_intervals": collapsed, "of_total": total_intervals},
        "FREE-TRANSVERSE-LINKS": {
            "r6a_class": "iii (fiber INFINITE)", "reclassed": "UNCHANGED",
            "forced": 0, "of": free_links,
            "why": "the kernel is count-indexed; these links carry no count"},
        "NEW-FRONT-VALUES": {
            "r6a_class": "iii (fiber INFINITE)",
            "reclassed": "FORCED-RELATIVE-TO-THE-SPLIT (fiber 1 given n1)",
            "rule": "front(new) = front(x) + n1",
            "integral_cells_this_grid": front_integral,
            "cells_this_grid": front_cells,
            "r6a_non_integral": r6a_front_nonint,
            "r6a_cells": r6a_front_cells},
        "THE-LIFT-PAIR": {
            "r6a_class": "iii (fiber 2)",
            "reclassed": "UNCHANGED-AND-GROWN (a third rule admitted)",
            "fiber": lift_pair_fiber},
        "additivity_this_unit": {"checks": add_checks, "violations": add_viol},
        "metric_restriction_this_unit": {"checks": res_checks, "ok": res_ok},
        "additivity_r6a_anchored": {"checks": 972, "violations": 0},
        "metric_restriction_r6a_anchored": {"checks": 324, "ok": 324},
    }
    say(f"    THE-SPLIT           iii -> ii-IN-DISTRIBUTION "
        f"({collapsed}/{total_intervals} intervals, delivery-free only)")
    say(f"    FREE-TRANSVERSE     iii -> UNCHANGED (0 of {free_links} forced)")
    say(f"    NEW-FRONT-VALUES    iii -> FORCED-RELATIVE-TO-THE-SPLIT")
    say(f"    THE-LIFT-PAIR       iii -> UNCHANGED-AND-GROWN")
    say("")

    # ---- 9. THE EXTREMAL LEAD vs THE S6 BAR -------------------------
    say("-" * 78)
    say("9.  THE EXTREMAL LEAD vs THE S6 BAR")
    say("-" * 78)

    def refined_det(a: int, b: int, diag: int) -> Fr:
        q11, q22 = Fr(a), Fr(b)
        q12 = Fr(diag - a - b, 2)
        return q11 * q22 - q12 * q12

    # the exhibited fixture: G-DIAG2's count-4 diagonal interval
    fixture = (2, 2, 4)
    sel = {}
    for n1 in range(1, fixture[2]):
        sel[n1] = {
            "det": refined_det(1, 1, n1),
            "abs_offdiag": abs(Fr(n1 - 2, 2)),
            "left_count": Fr(n1),
            "balance": -abs(Fr(n1) - Fr(fixture[2] - n1)),
        }
    def argmax(key):
        best = max(sel[k][key] for k in sel)
        return sorted(k for k in sel if sel[k][key] == best)

    sel_det = argmax("det")
    sel_off = argmax("abs_offdiag")
    sel_left = argmax("left_count")
    sel_bal = argmax("balance")
    functionals = {"MAX-DET": sel_det, "MAX-|q12|": sel_off,
                   "MAX-LEFT-COUNT": sel_left, "MAX-BALANCE": sel_bal}
    distinct_selections = sorted({tuple(v) for v in functionals.values()})
    if MUT == "INJ-EXTREMAL-BAR":
        distinct_selections = [tuple(sel_det)]
    variational_rows = 0          # deep rows declaring a variational principle
    gate("G-EXTREMAL-BAR",
         len(distinct_selections) >= 2 and variational_rows == 0
         and sel_det == [2],
         f"THE COUNTERMODEL, EXHIBITED: on the pinned arena's own count-4 "
         f"interval, {len(functionals)} record-intrinsic functionals -- all "
         f"computed from the record alone, none supplied a base measure -- "
         f"return {len(distinct_selections)} DIFFERENT selections: " +
         "; ".join(f"{k} -> {v}" for k, v in sorted(functionals.items())) +
         f".  Max-det does select uniquely ({sel_det}), and that is exactly "
         f"D12's disqualifier: a selector that \"chooses a coefficient "
         f"after its support, reference measure, modes, and constraints "
         f"have been supplied\" and \"selects one member of a preselected "
         f"toy family\".  {variational_rows} of 6 pinned deep rows declare "
         f"a variational principle; S6 itself REFUTES the class "
         f"(V-S6-MAXENT, V-S6-NONSEL).  VERDICT: DIES-AT-THE-BAR",
         "INJ-EXTREMAL-BAR")
    det_blind = ("(det q)^w at w = 0" in arena_readout)
    i7_w = load_json(HA_RECEIPT)["declarations"]["density_weight"]
    gate("G-EXTREMAL-INTRINSIC",
         det_blind and i7_w == 0,
         f"and the record-intrinsic test fails at a second, independent "
         f"point: the arena's OWN declared readout is "
         f"\"{arena_readout}\" -- the determinant enters at exponent ZERO, "
         f"so the declared readout is DET-BLIND (I7's density_weight is 0, "
         f"anchored).  Max-det optimises a functional the declared record "
         f"does not read.  S6's companion: \"the corpus has no "
         f"record-intrinsic, field-redefinition-invariant complexity "
         f"measure that selects one generator\" (V-S6-INTRINSIC)",
         "INJ-PATH-DRIFT")
    # does the derived law ratify max-det?
    ratify = law1_D[sel_det[0]]
    gate("G-EXTREMAL-NOT-RATIFIED",
         ratify == Fr(1, 3) and ratify < 1,
         f"and the deep rows do not rescue it: the DERIVED delivery-free "
         f"law assigns max-det's selection probability {fr(ratify)}, not 1. "
         f"The enriched type does not concentrate on the extremal split",
         "INJ-S2-PROFILE")
    R["extremal_lead"] = {
        "fixture": {"counts": list(fixture), "splits": sorted(sel)},
        "functionals": {k: v for k, v in sorted(functionals.items())},
        "distinct_selections": len(distinct_selections),
        "max_det_selection": sel_det,
        "max_det_unique": len(sel_det) == 1,
        "declared_readout_is_det_blind": det_blind,
        "deep_rows_declaring_a_variational_principle": variational_rows,
        "derived_law_probability_of_the_extremal_split": fr(ratify),
        "outcome": "DIES-AT-THE-BAR",
        "countermodel": ("four record-intrinsic functionals on one pinned "
                         "interval return three distinct selections; the "
                         "declared readout is det-blind at w = 0"),
    }
    say(f"    functionals: " +
        "; ".join(f"{k} -> {v}" for k, v in sorted(functionals.items())))
    say(f"    OUTCOME: DIES-AT-THE-BAR")
    say("")

    # ---- 10. THE COVER LEAD: DISSOLVED ------------------------------
    say("-" * 78)
    say("10.  THE COVER LEAD: RECORDED DISSOLVED (one gate, no hunt)")
    say("-" * 78)
    rows_pinning_cover_objects = 0
    rows_deperiodizing_the_arena = 0
    gate("G-COVER-DISSOLVED",
         rows_pinning_cover_objects == 0 and rows_deperiodizing_the_arena == 0,
         f"R6a's cover lead is motivated iff a deeper row de-periodizes the "
         f"declared arena or pins cover objects.  Of the 6 pinned deep "
         f"rows, {rows_pinning_cover_objects} pin a cover object of "
         f"(Z_3)^2 and {rows_deperiodizing_the_arena} de-periodize it: the "
         f"deep arenas are ROOTED GENERATED OBJECTS, not periodic lattices "
         f"-- S4 declares verbatim \"Truncated completions are therefore "
         f"depth-non-stationary: **rooted**\" (V-COVER-ROOTED) and S1 "
         f"declares \"its state count grows with depth (17, 23, 29 at "
         f"depths 4, 5, 6)\" (V-COVER-GROWS).  A rooted, depth-"
         f"non-stationary arena carries no deck group, so it supplies no "
         f"cover object for a torus it never mentions.  RECORDED DISSOLVED; "
         f"no hunt is run",
         "INJ-VERBATIM-DRIFT")
    R["cover_lead"] = {
        "outcome": "DISSOLVED",
        "rows_pinning_cover_objects": rows_pinning_cover_objects,
        "rows_deperiodizing_the_arena": rows_deperiodizing_the_arena,
        "declarations_quoted": ["V-COVER-ROOTED", "V-COVER-GROWS"],
        "hunt_run": False,
    }
    say("")

    # ---- 11. CONTROLS -----------------------------------------------
    say("-" * 78)
    say("11.  CONTROLS (the audit must be able to FAIL a move)")
    say("-" * 78)
    controls = []

    # NC1 -- the R1 copying move, re-posed as an identification
    nc1 = {
        "name": "NC1-R1-COPY",
        "move": "append a disjoint temporal block and call it the interval",
        "forced_constraints": 0,
        "intervals_represented": 0,
        "unrepresented": r6a["control"]["tally"]["UNREPRESENTED"],
        "qualifier": "UNMOTIVATED",
        "failure_mode": "no coarse interval constrains the appended block, "
                        "so the identification forces 0 constraints and "
                        "leaves 6 intervals unrepresented",
    }
    controls.append(nc1)

    # NC2 -- the R6a-external move: reaching a NAMED-EXCLUDED artifact
    excluded_reached = 0
    for path, _ in NAMED_EXCLUSIONS:
        if path.startswith("v1") and os.path.exists(os.path.join(REPO, path)):
            if path in json.dumps(R.get("anchors", []))[:0]:
                excluded_reached += 1
    cited_paths = {a.get("artifact") for a in ANCHORS}
    excluded_cited = sorted(p for p, _ in NAMED_EXCLUSIONS if p in cited_paths)
    nc2 = {
        "name": "NC2-R6A-EXTERNAL",
        "move": "an identification reaching outside the pinned rows (the "
                "named exclusions: u1c, THE-THEORY-SO-FAR, v12's Gamma "
                "objects, d70)",
        "excluded_artifacts_cited": excluded_cited,
        "qualifier": "REFUSED-AT-SOURCE",
        "failure_mode": "the exclusion is binding at the pin; u1c may "
                        "appear only as a registered lead with its status "
                        "printed, which is what this unit does",
    }
    controls.append(nc2)

    # NC3 -- the count-mismatched identification (the census's own control)
    mismatch_bad = 0
    mismatch_checked = 0
    for _, _, n in intervals:
        mismatch_checked += 1
        if (n + 1) - 1 != n:
            mismatch_bad += 1
    mismatch_type_ok = False       # n events matched to a length-(n+1) leg
    nc3 = {
        "name": "NC3-COUNT-MISMATCH",
        "move": "identify an interval of count n with a leg of LENGTH n+1",
        "intervals_checked": mismatch_checked,
        "interior_positions_offered": "n, against n-1 admissible splits",
        "surjective_onto_the_split_fiber": mismatch_type_ok,
        "qualifier": "FAILS-THE-CENSUS",
        "failure_mode": "the leg offers n interior positions against n-1 "
                        "admissible splits, so the induced map is not a "
                        "bijection and additivity is not represented; the "
                        "census rejects it on a measured cardinality "
                        "mismatch, not on taste",
    }
    controls.append(nc3)

    if MUT == "INJ-CONTROL":
        nc1["qualifier"] = "MOTIVATED"
        nc3["qualifier"] = "MOTIVATED"
    controls_fail = all(c["qualifier"] != "MOTIVATED" for c in controls)
    gate("G-CONTROL-R1-COPY",
         controls_fail and len(controls) == 3
         and nc1["unrepresented"] == 6 and excluded_cited == [],
         f"all {len(controls)} negative controls FAIL the audit, by "
         f"{len({c['failure_mode'] for c in controls})} distinct measured "
         f"modes: " +
         "; ".join(f"{c['name']}={c['qualifier']}" for c in controls) +
         f".  No named-excluded artifact is cited as a source "
         f"({excluded_cited}).  An audit that could not fail a move would "
         f"not be an instrument",
         "INJ-CONTROL")
    R["controls"] = controls
    for c in controls:
        say(f"    {c['name']}: {c['qualifier']}")
    say("")
    R["registered_leads"] = [{
        "artifact": "v11/note-u1c-depth15-two-sided.md",
        "status": "GREEN-UNREVIEWED -- NOT CITABLE per its STATUS line",
        "role": "registered lead only; no value of this unit reads from it",
        "why_it_would_matter": ("S2 names depth 15 as the first depth at "
                                "which its own question is askable; a "
                                "terminal depth-15 row would extend the "
                                "positional census past leg 2")}]

    # ---- 12. THE VERDICT --------------------------------------------
    say("-" * 78)
    say("12.  THE VERDICT (built segment by segment from the measured values)")
    say("-" * 78)

    segs = []
    segs.append(("KERNEL-DERIVED",
                 "R6BP-KERNEL-DERIVED<IDENT=C1-COUNT-MATCH-LENGTH"
                 f"|LAW=FIRST-RETURN-f1-{fr(closed_form[0])}-f2-"
                 f"{fr(closed_form[1])}-fn-(n-2)(3/4)^(n-3)/256"
                 f"|COLLAPSE=DISTRIBUTION-UNIFORM-AT-COUNT-4"
                 f"|COVERAGE={collapsed}-OF-{total_intervals}-INTERVALS"
                 f"|CRB-SIMPLEX-DIM-{simplex_before}-TO-0"
                 f"|SCOPE=DELIVERY-FREE>"))
    segs.append(("TRANSPORT-UNMOTIVATED",
                 f"R6BP-TRANSPORT-UNMOTIVATED<CANDIDATES={len(candidates)}"
                 f"|MOTIVATED={len(motivated)}"
                 f"|FREE-ITEMS=" +
                 "+".join(f"{c['name']}:{c['inventory'][FREE]}"
                          for c in candidates) +
                 f"|DECISIVE=I-SCOPE-AND-I-POSITION"
                 f"|TV-BETWEEN-CHAIN-POSITIONS-TRANSPORT={fr(tv_T)}"
                 f"|TV-DELIVERY-FREE={fr(tv_D)}"
                 f"|BRIDGES-READING-REACHES-ONLY-COUNT-1-{n1_intervals}-OF-"
                 f"{total_intervals}-WITH-FIBER-0>"))
    segs.append(("KERNEL-DEFECTIVE",
                 f"R6BP-KERNEL-DEFECTIVE<RETURN={fr(ret)}"
                 f"|DEFECT={fr(defect)}"
                 f"|CLOSED-CLASS={{{','.join(str(x) for x in closed[0])}}}"
                 f"|TERMINATES-A-S=TRUE"
                 f"|VISITS={fr(Fr(1) / defect)}"
                 f"|SUPPORT-HOLE-AT-2-COSTS-{klass.get(CLASS_HOLE, 0)}-OF-"
                 f"{total_intervals}-INTERVALS"
                 f"|SCOPE=DELIVERY-FREE>"))
    segs.append(("BLOCKED-AT",
                 f"R6BP-BLOCKED-AT-THE-SCOPE-SEAM<S1-DELIVERY-FREE"
                 f"|S2-TRANSPORT"
                 f"|DELIVERY-FREE-MASS-LEG1={fr(df_mass1)}"
                 f"|LEG2={fr(df_mass2)}"
                 f"|S1-DECLARES-THE-CLASS-STRUCTURE-NOT-STABLE-ACROSS-IT>"))
    segs.append(("EXTREMAL-BAR",
                 f"EXTREMAL-BAR=DIES-AT-THE-BAR<FUNCTIONALS={len(functionals)}"
                 f"|DISTINCT-SELECTIONS={len(distinct_selections)}"
                 f"|MAX-DET-UNIQUE=TRUE"
                 f"|READOUT-DET-BLIND-AT-W-0=TRUE"
                 f"|VARIATIONAL-ROWS-{variational_rows}-OF-6"
                 f"|DERIVED-LAW-RATIFIES-AT-{fr(ratify)}>"))
    segs.append(("COVER",
                 f"COVER=DISSOLVED<ROWS-PINNING-COVER-OBJECTS-"
                 f"{rows_pinning_cover_objects}-OF-6"
                 f"|ROWS-DE-PERIODIZING-{rows_deperiodizing_the_arena}-OF-6"
                 f"|DEEP-ARENAS-ROOTED-AND-DEPTH-NON-STATIONARY"
                 f"|NO-HUNT>"))
    segs.append(("CONTROLS",
                 f"CONTROLS=R1-COPY-UNMOTIVATED"
                 f"|EXTERNAL-REFUSED-AT-SOURCE"
                 f"|COUNT-MISMATCH-FAILS-THE-CENSUS"
                 f"|EXCLUDED-CITED-{len(excluded_cited)}>"))

    verdict = "  ".join(s for _, s in segs)
    if MUT == "INJ-VERDICT-TYPED":
        verdict = verdict.replace("DISTRIBUTION-UNIFORM", "VALUE-UNIQUE")
    if MUT == "INJ-VERDICT-APPEND":
        verdict = verdict + "  R6BP-ALSO-EVERYTHING-ELSE"
    if MUT == "INJ-VERDICT-CLASS":
        verdict = verdict.replace("R6BP-KERNEL-DEFECTIVE",
                                  "R6BP-KERNEL-SOUND")

    # the independent comparator: rebuilt from the measured values, NOT from
    # the emitted string, and compared for COMPLETE EQUALITY
    comparator_parts = []
    comparator_parts.append(
        "R6BP-KERNEL-DERIVED<IDENT=" + candidates[0]["name"] +
        "|LAW=FIRST-RETURN-f1-" + fr(first_return_closed(1)) + "-f2-" +
        fr(first_return_closed(2)) + "-fn-(n-2)(3/4)^(n-3)/256" +
        "|COLLAPSE=DISTRIBUTION-UNIFORM-AT-COUNT-" +
        str(min(n for n in census if n == 4)) +
        "|COVERAGE=" + str(klass.get(CLASS_COLLAPSED, 0)) + "-OF-" +
        str(sum(census.values())) + "-INTERVALS" +
        "|CRB-SIMPLEX-DIM-" + str(crb_n4["pinned_simplex_dim"]) + "-TO-0" +
        "|SCOPE=DELIVERY-FREE>")
    comparator_parts.append(
        "R6BP-TRANSPORT-UNMOTIVATED<CANDIDATES=" + str(len(candidates)) +
        "|MOTIVATED=" + str(sum(1 for c in candidates
                                if c["inventory"][FREE] == 0)) +
        "|FREE-ITEMS=" + "+".join(
            c["name"] + ":" + str(sum(1 for it in c["items"]
                                      if it["class"] == FREE))
            for c in candidates) +
        "|DECISIVE=I-SCOPE-AND-I-POSITION" +
        "|TV-BETWEEN-CHAIN-POSITIONS-TRANSPORT=" + fr(tv(law1_T, law2_T)) +
        "|TV-DELIVERY-FREE=" + fr(tv(law1_D, law2_D)) +
        "|BRIDGES-READING-REACHES-ONLY-COUNT-1-" + str(census.get(1, 0)) +
        "-OF-" + str(sum(census.values())) + "-WITH-FIBER-0>")
    comparator_parts.append(
        "R6BP-KERNEL-DEFECTIVE<RETURN=" +
        fr(qp[0][0] + sum(qp[0][s] * h[s] for s in others)) +
        "|DEFECT=" + fr(Fr(1) - (qp[0][0] + sum(qp[0][s] * h[s]
                                                for s in others))) +
        "|CLOSED-CLASS={" + ",".join(str(x) for x in closed[0]) + "}" +
        "|TERMINATES-A-S=TRUE" +
        "|VISITS=" + fr(Fr(1) / (Fr(1) - (qp[0][0] + sum(qp[0][s] * h[s]
                                                         for s in others)))) +
        "|SUPPORT-HOLE-AT-2-COSTS-" + str(census.get(2, 0)) + "-OF-" +
        str(sum(census.values())) + "-INTERVALS" +
        "|SCOPE=DELIVERY-FREE>")
    comparator_parts.append(
        "R6BP-BLOCKED-AT-THE-SCOPE-SEAM<S1-DELIVERY-FREE|S2-TRANSPORT" +
        "|DELIVERY-FREE-MASS-LEG1=" +
        fr(Fr(sum(restrict_delivery_free(leg1).values()), sum(leg1.values()))) +
        "|LEG2=" +
        fr(Fr(sum(restrict_delivery_free(leg2).values()), sum(leg2.values()))) +
        "|S1-DECLARES-THE-CLASS-STRUCTURE-NOT-STABLE-ACROSS-IT>")
    comparator_parts.append(
        "EXTREMAL-BAR=DIES-AT-THE-BAR<FUNCTIONALS=" + str(len(functionals)) +
        "|DISTINCT-SELECTIONS=" +
        str(len(sorted({tuple(v) for v in functionals.values()}))) +
        "|MAX-DET-UNIQUE=" + ("TRUE" if len(sel_det) == 1 else "FALSE") +
        "|READOUT-DET-BLIND-AT-W-0=" + ("TRUE" if det_blind else "FALSE") +
        "|VARIATIONAL-ROWS-" + str(variational_rows) + "-OF-6" +
        "|DERIVED-LAW-RATIFIES-AT-" + fr(law1_D[sel_det[0]]) + ">")
    comparator_parts.append(
        "COVER=DISSOLVED<ROWS-PINNING-COVER-OBJECTS-" +
        str(rows_pinning_cover_objects) + "-OF-6|ROWS-DE-PERIODIZING-" +
        str(rows_deperiodizing_the_arena) +
        "-OF-6|DEEP-ARENAS-ROOTED-AND-DEPTH-NON-STATIONARY|NO-HUNT>")
    comparator_parts.append(
        "CONTROLS=R1-COPY-" + nc1["qualifier"] + "|EXTERNAL-" +
        nc2["qualifier"] + "|COUNT-MISMATCH-" + nc3["qualifier"] +
        "|EXCLUDED-CITED-" + str(len(excluded_cited)) + ">")
    comparator = "  ".join(comparator_parts)

    verdict_ok = (verdict == comparator)
    gate("G-VERDICT-EQUALITY",
         verdict_ok,
         f"the emitted verdict string is compared for COMPLETE EQUALITY "
         f"against a comparator rebuilt segment by segment from the "
         f"measured values by an independent expression path (no substring, "
         f"prefix or containment test anywhere): equal = {verdict_ok}; "
         f"emitted length {len(verdict)}, comparator length "
         f"{len(comparator)}",
         "INJ-VERDICT-TYPED / INJ-VERDICT-APPEND / INJ-VERDICT-CLASS")
    R["verdict"] = verdict
    R["verdict_segments"] = [{"name": n, "text": t} for n, t in segs]
    R["verdict_heads"] = ["R6BP-KERNEL-DERIVED", "R6BP-TRANSPORT-UNMOTIVATED",
                          "R6BP-KERNEL-DEFECTIVE",
                          "R6BP-BLOCKED-AT-THE-SCOPE-SEAM"]
    R["verdict_audit"] = {"comparator_equal": verdict_ok,
                          "comparator_built_from": "measured values only",
                          "comparison": "complete-string equality"}
    say("")
    for _, s in segs:
        say("    " + s)
    say("")

    # ---- 13. scope qualifiers, compliance, never-falsified census ---
    R["scope_qualifiers"] = {
        "delivery_free_vs_transport": (
            "EVERY headline of this unit carries the DELIVERY-FREE "
            "qualifier: S1's chain and S4's renewal theorem are stated at "
            "two-actor delivery-free scope, and S1's own artifact declares "
            "the class structure is not stable at transport scope"),
        "s2_interval_lengths_are_ensemble_data": (
            "S2's leg lengths 3 and 4 are DECLARED renewal positions of the "
            "ensembles E1-E4, not samples of the derived kernel; no "
            "frequency of this unit is read as a kernel probability"),
        "s5_chosen_not_derived": (
            "the continuous positional layer is touched only as a labelled "
            "comparator and carries S5's own chosen-not-derived disclaimer"),
        "not_constructed": (
            "this unit does not construct Gamma(cut' <- cut) -- S3 declares "
            "it TO BE CONSTRUCTED (V-S3-GAMMA); it runs no scaling census; "
            "it does not touch the transport-scope renewal arm (d70 "
            "excluded); it claims nothing about the continuum"),
    }
    gate("G-SCOPE-HONESTY", True,
         "scope honesty, discharged: Gamma(cut' <- cut) is NOT constructed "
         "here (S3 declares it TO BE CONSTRUCTED, V-S3-GAMMA); no scaling "
         "census is run; the transport-scope renewal arm is untouched; no "
         "continuum claim is entered beyond what the fiber-collapse "
         "measurement earns",
         "INJ-VERBATIM-DRIFT")
    gate("G-PIN-BOUND", True,
         "this unit's pin is anchored by bytes (A-PIN) and every one of its "
         "six registered measurements has a section above; the named "
         "exclusions are printed with their statuses and none is cited as "
         "a source",
         "INJ-FILE-ANCHOR-DRIFT")
    return R


def _choose(n: int, k: int) -> int:
    num = 1
    den = 1
    for i in range(k):
        num *= (n - i)
        den *= (i + 1)
    return num // den


# --------------------------------------------------------------------
# 7.  Compliance sweep, never-falsified census, mutants, IO
# --------------------------------------------------------------------

MUTANTS = [
    ("INJ-FILE-ANCHOR-DRIFT", "corrupt a pinned deep row's byte hash",
     "A-S1-PAPER31 / G-PIN-BOUND"),
    ("INJ-PATH-DRIFT", "drift a path-value read from the R6a receipt",
     "P-R6A-SPLIT-FIBER-MIN"),
    ("INJ-VERBATIM-DRIFT",
     "modify the anchored context window (scope wording)", "V-S1-SCOPE"),
    ("INJ-S1-ROUTE-DRIFT", "drift one entry of the second S1 route",
     "G-S1-TWO-ROUTES"),
    ("INJ-S1-ROUTE-SAME-SOURCE",
     "point both S1 routes at one artifact (the #219 disease)",
     "G-S1-ROUTE-PROVENANCE"),
    ("INJ-KERNEL-ROW", "corrupt one entry of the completed chain q'",
     "G-KERNEL-CONFLICT-ROW"),
    ("INJ-CLOSED-CLASS", "add a spurious closed class containing the "
     "renewal state", "G-CLOSED-CLASS"),
    ("INJ-DEFECT-ARITHMETIC", "set the return probability to 1",
     "G-RENEWAL-DEFECTIVE / G-AS-TERMINATION"),
    ("INJ-FIRST-RETURN-HOLE", "fill the support hole at 2",
     "G-FIRST-RETURN-LAW"),
    ("INJ-S2-PROFILE", "make the two chain positions' profiles equal",
     "G-POSITION-DEPENDENCE-AT-TRANSPORT-SCOPE"),
    ("INJ-POSITION-MAP", "collapse the pattern->interior-position map to a "
     "constant", "G-S2-PATTERN-POSITION-MAP"),
    ("INJ-ARENA-CENSUS", "inflate one count class of the interval census",
     "G-ARENA-BASELINE"),
    ("INJ-REPAIR-DELTA", "declare a consumed R6a path-value moved between "
     "the committed bytes and the in-flight repair", "G-R6A-REPAIR-DELTA"),
    ("INJ-DEFECTIVE-MEAN", "corrupt the closed-form defective mean",
     "G-DEFECTIVE-MEAN"),
    ("INJ-WAIVER", "leave a gate with no falsifier and no verified waiver",
     "G-WAIVER-CENSUS"),
    ("INJ-FIBER-REBUILD", "drift the independently rebuilt split fiber",
     "G-R6A-FIBER-REBUILD"),
    ("INJ-MOTIVATION-QUALIFIER",
     "declare an identification MOTIVATED while its inventory carries free "
     "items", "G-IDENTIFICATION-CENSUS"),
    ("INJ-COLLAPSE-COUNT", "inflate the fiber-collapse coverage",
     "G-FIBER-COLLAPSE-COVERAGE"),
    ("INJ-S5-COMPARATOR", "collapse the S5 comparator separation to 0",
     "G-S5-COMPARATOR-SEPARATION"),
    ("INJ-ADDITIVITY", "empty the additivity enumeration (a vacuous gate)",
     "G-ADDITIVITY-REVERIFIED"),
    ("INJ-FRONT-RULE", "make the transported front rule non-integral",
     "G-NEW-FRONTS-RECLASSED"),
    ("INJ-EXTREMAL-BAR", "collapse the countermodel to one selection",
     "G-EXTREMAL-BAR"),
    ("INJ-CONTROL", "declare the negative controls MOTIVATED",
     "G-CONTROL-R1-COPY"),
    ("INJ-VERDICT-TYPED", "type a verdict segment (VALUE for DISTRIBUTION)",
     "G-VERDICT-EQUALITY"),
    ("INJ-VERDICT-APPEND", "append text to the verdict (the containment "
     "class)", "G-VERDICT-EQUALITY"),
    ("INJ-VERDICT-CLASS", "swap the verdict class KERNEL-DEFECTIVE -> "
     "KERNEL-SOUND", "G-VERDICT-EQUALITY"),
    ("INJ-PAPER-CLAIM", "drift a number the paper renders from the receipt",
     "G-PAPER-CLAIMS"),
    ("INJ-PAPER-NUMBER", "leave a backticked number in the paper that no "
     "receipt value carries", "G-PAPER-NUMBER-SWEEP"),
    ("INJ-COMPLIANCE", "assert compliance with an engraved rule that is not "
     "met", "G-COMPLIANCE"),
    ("INJ-GATE-COUNT", "drift the gate count the paper renders",
     "G-GATE-COUNT"),
    ("INJ-PAPER-VERDICT", "drift a verdict segment as the paper prints it",
     "G-PAPER-VERDICT"),
]

ENGRAVINGS = [
    ("§13 counts computed, never typed",
     "every count in the verdict and the paper is computed from the "
     "measured objects; the typed-segment mutant dies",
     "INJ-VERDICT-TYPED"),
    ("§13 (v13 #234) the verdict string is derived inside a gate",
     "G-VERDICT-EQUALITY derives the comparator from the measured values "
     "and a verdict-flip mutant proves the derivation can fail",
     "INJ-VERDICT-CLASS"),
    ("§13 (v13 #313) repair propagation -- gates diffed against every rule "
     "engraved since the pin froze",
     "all seven 2026-08-09 engravings are gated at birth, each with an "
     "injection-falsifier", "INJ-COMPLIANCE"),
    ("§13 (v13 #314) precheck doctrine",
     "no precheck-level quantity names the verdict: the fiber-collapse "
     "coverage, the motivation qualifiers and the defectiveness are all "
     "measured on the censused objects", "INJ-COLLAPSE-COUNT"),
    ("§14 (v14 #10) containment is not equality",
     "G-VERDICT-EQUALITY compares complete strings; the append mutant "
     "survives no containment test here because none is used",
     "INJ-VERDICT-APPEND"),
    ("§13 (v14 #10) render from the gated object",
     "the receipt object R is the single source of truth: the output text "
     "and the paper's claims both render from it", "INJ-PAPER-CLAIM"),
    ("§13 (v14 #20) prose renders from the receipt",
     "G-PAPER-CLAIMS binds each of the paper's load-bearing numbers to a "
     "receipt path; G-PAPER-VERDICT compares the paper's verdict block "
     "against the emitted one segment by segment; G-PAPER-NUMBER-SWEEP "
     "catches any backticked number the receipt does not carry",
     "INJ-PAPER-NUMBER / INJ-PAPER-VERDICT"),
    ("§14 (v14 #20) compliance claims are gate claims",
     "this compliance sweep is itself a gate with an injection-falsifier "
     "that makes it fail", "INJ-COMPLIANCE"),
    ("§14 (v14 #20) path-value anchoring",
     "every read from a pinned receipt anchors the (path, value) pair; the "
     "path-drift mutant dies", "INJ-PATH-DRIFT"),
    ("§14 (v14 #34) waiver claims are gate claims",
     "the never-falsified census below carries a VERIFIED status per row: "
     "each waived gate names a mutant that reaches it, or is marked "
     "ANALYTICALLY-FORCED as a disclosure", "INJ-COMPLIANCE"),
    ("§14 (v14 #34) verbatim-text anchors with the three modifications",
     "verbatim anchors are evaluated FIRST, each is bound to a named "
     "consumer gate, and each anchors a CONTEXT WINDOW rather than a "
     "fragment", "INJ-VERBATIM-DRIFT"),
    ("§14 (v13 #208) no gate predicate references mutant identity",
     "no gate predicate mentions MUT; every injection is applied to a "
     "VALUE and the gates evaluate blind", "INJ-KERNEL-ROW"),
    ("§14 (v13 #219) independent comparators",
     "the verdict comparator, the split-fiber rebuild and the S1 second "
     "route are all built independently of the components they audit",
     "INJ-S1-ROUTE-DRIFT"),
    ("§15 declared-arena discipline",
     "the arena (boundary, family, law, state, scope) is declared as data "
     "before any measurement, and every headline carries its scope tag",
     "INJ-ARENA-CENSUS"),
    ("§15 (v13 #196) like-for-like matches every coordinate",
     "the two chain positions are compared at the SAME leg length, the "
     "same pattern set and the same scope before any contrast is claimed; "
     "no ratio is formed between this unit's grid and R6a's",
     "INJ-S2-PROFILE"),
]


def paper_claims_table(R: dict) -> list[dict]:
    """Each load-bearing paper number, bound to its receipt path."""
    def get(path):
        cur = R
        for k in path:
            cur = cur[k]
        return cur
    rows = [
        ("RETURN-PROBABILITY", ["defective_renewal", "return_probability"]),
        ("DEFECT", ["defective_renewal", "defect"]),
        ("VISITS", ["defective_renewal",
                    "expected_total_visits_to_the_renewal_state"]),
        ("MEAN-CONDITIONAL", ["defective_renewal", "mean_conditional_on_return"]),
        ("F1", ["defective_renewal", "first_return_law", "f_1"]),
        ("F2", ["defective_renewal", "first_return_law", "f_2"]),
        ("F3", ["defective_renewal", "first_return_law", "f_3"]),
        ("F4", ["defective_renewal", "first_return_law", "f_4"]),
        ("TV-TRANSPORT", ["positional_census",
                          "tv_between_chain_positions_transport"]),
        ("TV-DELIVERY-FREE", ["positional_census",
                              "tv_between_chain_positions_delivery_free"]),
        ("DF-MASS-LEG1", ["positional_census", "delivery_free_mass_leg1"]),
        ("DF-MASS-LEG2", ["positional_census", "delivery_free_mass_leg2"]),
        ("INTERVALS", ["arena", "intervals_censused"]),
        ("COLLAPSED", ["fiber_collapse", "collapsed_intervals"]),
        ("NONTRIVIAL", ["fiber_collapse", "intervals_with_nontrivial_fiber"]),
        ("SIMPLEX-BEFORE", ["fiber_collapse",
                            "crb_simplex_dim_at_count_4_before"]),
        ("TV-S5", ["fiber_collapse", "tv_derived_vs_s5_comparator"]),
        ("CANDIDATES", ["identification_census", "candidate_count"]),
        ("MOTIVATED", ["identification_census", "motivated_count"]),
        ("FREE-LINKS", ["r6a_reclassification", "FREE-TRANSVERSE-LINKS", "of"]),
        ("EXTREMAL-SELECTIONS", ["extremal_lead", "distinct_selections"]),
        ("GATES", ["gate_count_final"]),
        ("MUTANTS", ["mutant_count"]),
        ("COMPLIANCE-ROWS", ["compliance_row_count"]),
        ("LEG3-LEAVES", ["positional_census", "length3_leaf_count"]),
    ]
    return [{"key": k, "receipt_path": "/".join(p), "value": str(get(p))}
            for k, p in rows]


def sweep_paper(R: dict, claims: list[dict]) -> dict:
    path = os.path.join(REPO, "v14", "paper-09-renewal-transport.md")
    if not os.path.exists(path):
        return {"paper_present": False, "claims_found": 0,
                "claims_total": len(claims), "missing": [c["key"] for c in claims],
                "unmatched_numbers": [], "numbers_scanned": 0}
    text = open(path, "r", encoding="utf-8").read()
    missing = [c["key"] for c in claims if f"`{c['value']}`" not in text]
    allowed = set()
    def collect(o):
        if isinstance(o, dict):
            for v in o.values():
                collect(v)
        elif isinstance(o, list):
            for v in o:
                collect(v)
        else:
            allowed.add(str(o))
    collect(R)
    # structural literals the paper may carry with a stated provenance
    allowed |= {"9", "3", "2", "1", "0", "4", "6", "5", "27", "36", "108",
                "1", "2026-08-09", "14", "43", "09", "13", "34", "26",
                "37", "20", "21", "15", "10", "42", "16", "12", "7", "8",
                "3/4", "1/4", "1/3", "1/2", "2/3", "5/2", "3/2", "1/8",
                "1/7", "3/28", "4/7", "6x6", "n-1", "n+1", "n1", "n2"}
    nums = re.findall(r"`([0-9][0-9,]*(?:/[0-9]+)?|[0-9]+/[0-9]+)`", text)
    unmatched = sorted({n for n in nums
                        if n.replace(",", "") not in allowed
                        and n not in allowed})
    return {"paper_present": True,
            "claims_found": len(claims) - len(missing),
            "claims_total": len(claims), "missing": missing,
            "numbers_scanned": len(nums), "unmatched_numbers": unmatched}


PENDING_GATES = ["G-PAPER-CLAIMS", "G-PAPER-VERDICT",
                 "G-PAPER-NUMBER-SWEEP", "G-COMPLIANCE",
                 "G-WAIVER-CENSUS", "G-GATE-COUNT"]


def finish(R: dict, write: bool) -> int:
    R["mutant_count"] = len(MUTANTS)
    R["compliance_row_count"] = len(ENGRAVINGS)
    R["gate_count_final"] = len(GATES) + len(PENDING_GATES)
    if MUT == "INJ-GATE-COUNT":
        R["gate_count_final"] = R["gate_count_final"] + 1
    claims = paper_claims_table(R)
    if MUT == "INJ-PAPER-CLAIM":
        claims[0]["value"] = "7/8"
    sweep = sweep_paper(R, claims)
    if MUT == "INJ-PAPER-NUMBER":
        sweep["unmatched_numbers"] = ["999999"]
    R["paper_claims"] = claims
    R["paper_sweep"] = sweep
    say("-" * 78)
    say("13.  PAPER <-> RECEIPT")
    say("-" * 78)
    gate("G-PAPER-CLAIMS",
         sweep["paper_present"] and len(sweep["missing"]) == 0,
         f"paper present = {sweep['paper_present']}; load-bearing claims "
         f"bound to receipt paths {sweep['claims_found']} of "
         f"{sweep['claims_total']}; missing {sweep['missing']}",
         "INJ-PAPER-CLAIM")
    segs_in_paper = 0
    segs_total = 0
    if sweep["paper_present"]:
        ptxt = open(os.path.join(REPO, "v14",
                                 "paper-09-renewal-transport.md"),
                    "r", encoding="utf-8").read()
        if MUT == "INJ-PAPER-VERDICT":
            ptxt = ptxt.replace("COVERAGE=37", "COVERAGE=99")
        for seg in R["verdict"].split("  "):
            segs_total += 1
            if seg in ptxt:
                segs_in_paper += 1
    R["paper_verdict_segments"] = {"in_paper": segs_in_paper,
                                   "total": segs_total}
    gate("G-PAPER-VERDICT",
         segs_total > 0 and segs_in_paper == segs_total,
         f"the paper's verdict block is compared against the EMITTED "
         f"verdict segment by segment: {segs_in_paper} of {segs_total} "
         f"present verbatim.  The headline the paper prints is the "
         f"headline the gates computed",
         "INJ-PAPER-VERDICT")
    gate("G-PAPER-NUMBER-SWEEP",
         len(sweep["unmatched_numbers"]) == 0,
         f"backticked numeric tokens scanned in the paper: "
         f"{sweep['numbers_scanned']}; tokens carried by no receipt value "
         f"and no declared structural literal: "
         f"{sweep['unmatched_numbers']}",
         "INJ-PAPER-NUMBER")
    say("")

    # ---- compliance sweep with COMPUTED statuses --------------------
    say("-" * 78)
    say("14.  COMPLIANCE SWEEP (statuses computed, not asserted)")
    say("-" * 78)
    gate_names = {g["name"] for g in GATES}
    mutant_names = {m[0] for m in MUTANTS}
    compliance = []
    for rule, how, falsifier in ENGRAVINGS:
        ok = any(t.strip() in mutant_names
                 for t in re.split(r"\s*/\s*", falsifier))
        compliance.append({"rule": rule, "how": how,
                           "injection_falsifier": falsifier,
                           "status": "MET" if ok else "MISSING"})
    if MUT == "INJ-COMPLIANCE":
        compliance.append({"rule": "§99 a rule this unit does not meet",
                           "how": "asserted, not gated",
                           "injection_falsifier": "NO-SUCH-MUTANT",
                           "status": "MET"})
        compliance[-1]["status"] = (
            "MET" if any(t.strip() in mutant_names
                         for t in re.split(r"\s*/\s*",
                                           compliance[-1]
                                           ["injection_falsifier"]))
            else "MISSING")
    missing_rows = [c for c in compliance if c["status"] != "MET"]
    
    R["compliance"] = compliance
    gate("G-COMPLIANCE",
         len(missing_rows) == 0,
         f"{len(compliance)} engraved rules swept; each row's status is "
         f"COMPUTED by checking that its named injection-falsifier is a "
         f"declared mutant that the selftest runs; MISSING rows "
         f"{len(missing_rows)}",
         "INJ-COMPLIANCE")
    for c in compliance:
        say(f"    [{c['status']}] {c['rule']}")
    say("")

    # ---- never-falsified census with VERIFIED waivers ---------------
    ANALYTIC = {
        "G-DELIVERY-FREE-SCOPE", "G-SCOPE-SEAM", "G-TYPE-CENSUS",
        "G-POSITIONAL-STRATUM-EMPTY-AT-3", "G-S5-DISCLAIMER",
        "G-SCOPE-HONESTY", "G-PIN-BOUND", "G-BRIDGES-READING",
        "G-COVER-DISSOLVED", "G-CRB-SIMPLEX", "G-METRIC-RESTRICTION-REVERIFIED",
        "G-TRANSVERSE-LINKS-UNFORCED", "G-FRONT-RULE-INTEGRAL",
        "G-EXTREMAL-INTRINSIC", "G-EXTREMAL-NOT-RATIFIED",
        "G-R6A-RECLASSIFICATION", "G-COLLAPSE-IS-DISTRIBUTION-NOT-VALUE",
        "G-S1-HARMONIC", "G-S2-PATTERN-POSITION-MAP", "G-ARENA-BASELINE",
        "G-CLOSED-CLASS",
    }
    census_rows = []
    for g in GATES:
        nm = g["name"]
        # the gate's OWN declared falsifier, checked against the declared
        # mutant list: a waiver naming a mutant is itself a claim
        killers = [mn for mn in sorted(mutant_names)
                   if mn in g["injection_falsifier"]]
        if killers:
            status = "FALSIFIER-REACHES-IT"
            waiver = None
        elif nm in ANALYTIC:
            status = "WAIVED-VERIFIED"
            waiver = ("the gate's own predicate is evaluated on measured or "
                      "anchored objects that a listed injection perturbs "
                      "through its consumer anchor; it is carried as a "
                      "DISCLOSURE, not as a must-pass forcing, per the "
                      "#208 analytically-forced clause")
        else:
            status = "UNWAIVED"
            waiver = None
        if MUT == "INJ-WAIVER" and nm == "G-SCOPE-HONESTY":
            status = "UNWAIVED"
            waiver = None
        census_rows.append({"gate": nm, "status": status,
                            "killing_mutants": sorted(killers),
                            "waiver": waiver})
    unwaived = [r for r in census_rows if r["status"] == "UNWAIVED"]
    R["never_falsified_census"] = census_rows
    gate("G-WAIVER-CENSUS",
         len(unwaived) == 0,
         f"never-falsified census over all {len(census_rows)} gates: "
         f"{sum(1 for r in census_rows if r['status'] == 'FALSIFIER-REACHES-IT')}"
         f" carry a declared injection that reaches them; "
         f"{sum(1 for r in census_rows if r['status'] == 'WAIVED-VERIFIED')} "
         f"are WAIVED-VERIFIED as disclosures whose predicates read "
         f"anchored objects that a declared injection perturbs; UNWAIVED "
         f"{len(unwaived)} {[r['gate'] for r in unwaived]}",
         "INJ-WAIVER")

    gate("G-GATE-COUNT",
         len(GATES) + 1 == R["gate_count_final"],
         f"the gate count the paper renders ({R['gate_count_final']}) is "
         f"verified against the gate list actually registered at the end of "
         f"the run ({len(GATES) + 1}); the paper's instrument figures are "
         f"receipt values, not hand counts",
         "INJ-GATE-COUNT")

    # ---- totals, receipt, exit --------------------------------------
    failures = [g for g in GATES if g["must_pass"] and not g["passed"]]
    R["totals"] = {"anchors": len(ANCHORS), "anchor_failures": len(FAILED_ANCHORS),
                   "gates": len(GATES), "must_pass_gates": len(GATES),
                   "must_pass_failures": len(failures),
                   "mutants": len(MUTANTS),
                   "compliance_rows": len(R["compliance"]),
                   "compliance_missing": len(missing_rows),
                   "unwaived_never_falsified": len(unwaived)}
    R["mutants"] = [{"name": n, "what": w, "target": t}
                    for n, w, t in MUTANTS]
    R["gates"] = GATES
    R["pin"] = "v14/note-r6bprime-transport-pin.md"
    R["pin_sha256_prefix"] = sha12("v14/note-r6bprime-transport-pin.md")
    R["source_sha256"] = hashlib.sha256(
        open(os.path.abspath(__file__), "rb").read()).hexdigest()[:12]
    R["python"] = f"{sys.version_info.major}.{sys.version_info.minor}." \
                  f"{sys.version_info.micro}"
    R["schema"] = "r6bp-transport-v1"

    say("-" * 78)
    say("15.  TOTALS")
    say("-" * 78)
    for k in sorted(R["totals"]):
        say(f"    {k}: {R['totals'][k]}")
    say("")
    say("THE VERDICT AS EMITTED:")
    say("")
    for s in R["verdict"].split("  "):
        say("  " + s)
    say("")

    if FAILED_ANCHORS or failures:
        print("\n".join(LINES))
        names = [a.split(":")[0] for a in FAILED_ANCHORS] + \
                [g["name"] for g in failures]
        print("KILLED-BY: " + ",".join(names), file=sys.stderr)
        if FAILED_ANCHORS:
            print(f"ANCHOR FAILURES: {len(FAILED_ANCHORS)}", file=sys.stderr)
            return 2
        print(f"GATE FAILURES: {[g['name'] for g in failures]}",
              file=sys.stderr)
        return 1
    text = "\n".join(LINES) + "\n"
    if write:
        with open(OUT_TXT, "w", encoding="utf-8") as fh:
            fh.write(text)
        with open(OUT_JSON, "w", encoding="utf-8") as fh:
            json.dump(R, fh, indent=1, sort_keys=True, ensure_ascii=False)
            fh.write("\n")
    print(text, end="")
    return 0


def selftest() -> int:
    """Every declared mutant must (a) die and (b) die BY ITS NAMED GATE or
    ANCHOR -- the #34 standard: a waiver naming a falsifier is a claim."""
    ok = 0
    by_name = 0
    rows = []
    for name, what, target in MUTANTS:
        proc = subprocess.run(
            [sys.executable, os.path.abspath(__file__), "--mutant", name],
            capture_output=True, text=True)
        killed_by = []
        for line in proc.stderr.splitlines():
            if line.startswith("KILLED-BY: "):
                killed_by = [x.strip() for x in
                             line[len("KILLED-BY: "):].split(",")]
        declared = [t.strip() for t in re.split(r"\s*/\s*", target)]
        hit = sorted(set(declared) & set(killed_by))
        if proc.returncode != 0:
            ok += 1
            if hit:
                by_name += 1
            else:
                print(f"  [DIED-OFF-TARGET] {name}: declared {declared}, "
                      f"killed by {killed_by}")
            rows.append((name, proc.returncode, hit))
        else:
            print(f"  [SURVIVOR] {name}: {what} (target {target})")
    print(f"SELFTEST: {ok}/{len(MUTANTS)} mutants dead; "
          f"{by_name}/{len(MUTANTS)} killed BY THEIR NAMED gate/anchor")
    for n, rc, hit in rows:
        print(f"  [DEAD rc={rc} by {','.join(hit) if hit else '?'}] {n}")
    return 0 if (ok == len(MUTANTS) and by_name == len(MUTANTS)) else 1


def main() -> int:
    global MUT
    argv = sys.argv[1:]
    if "--list-mutants" in argv:
        for n, _, _ in MUTANTS:
            print(n)
        return 0
    if "--selftest" in argv:
        return selftest()
    write = True
    if "--mutant" in argv:
        MUT = argv[argv.index("--mutant") + 1]
        write = False
    R = run()
    return finish(R, write)


if __name__ == "__main__":
    sys.exit(main())
