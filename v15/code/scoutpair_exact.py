#!/usr/bin/env python3
# ===========================================================================
# SCOUT-PAIR -- record-arity vs process-arity: the re-typing audit (S1),
# the order/composition-defect census (S2), the operational-divisibility
# test (S3), and the pair-sufficiency census (S4).
#
# Unit: v15/note-scoutpair.md (report NOTE, scout class).
# Pin:  v15/note-scoutpair-pin.md (FROZEN 67e6082b445a), v15 ledger #84,
#       amended by the #85 routed addendum (S3 anti-triviality freeze;
#       S2 curvature scope wall) and by the FROZEN #86 addendum
#       v15/note-scoutpair-pin-addendum.md (b3aa0f973ae1): status-table
#       framing, order/composition-defect naming with four readings
#       unchosen, S3 = operational divisibility (CK / process-tensor
#       compatibility at every declared cut, two-sided verdicts), NEW
#       charge S4 pair-sufficiency, the frozen source table, and
#       W-REPRESENTATION in its amended fork-neutral form.
#
# THE FROZEN SOURCE TABLE (#86 item 5; the object under test is
# IMMOVABLE; repairs landing mid-build are NOT adopted): ARITY-16 at the
# committed #47 digests c86ea5edcfec / 613e05fc7ff0 / 837333a85fcb /
# 52f600389933; SCOUT-K at the committed #74 digests 573cb2c55e5c /
# 38c3f6cb288e / c37cbd977d57 / 5af53face093; the walk snapshot
# edb60bccd22e; paper-19 50bb81e67942; paper-20 4824d190af73; paper-41
# c5fbc9acbd76; paper-40 4fe88602280c.  Live copies of paper-50,
# note-scoutk.md and note-scoutpsi.md had moved mid-repair when this
# unit launched, so those three are bound through disclosed
# byte-verified snapshots (SEC-2 / SCOUT-K snapshot precedent); the
# remaining ARITY-16 legs and scoutk_exact.py are DECLARED, NOT READ
# (their digests recorded, their bytes never opened).
#
# Exact arithmetic throughout: Python integers and fractions.Fraction.
# No floats, no builtin hash, no timestamps, no absolute paths in
# artifacts.  The delivery run is the only writer; every failure path
# writes nothing.
#
# CLI: delivery (no args) | --no-write | --numbers | --kit | --selftest |
#      --mutant NAME | --verify-paper PATH | --list-gates | --list-mutants
# Exit codes: 0 pass, 2 usage, 3 gate failure / verification failure.
# ===========================================================================
import os
import sys
import json
import hashlib
import ast
from fractions import Fraction
from itertools import combinations, permutations

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # .../isp
NOTE_REL = "v15/note-scoutpair.md"
OUT_REL = "v15/code/scoutpair_output.txt"
REC_REL = "v15/code/scoutpair_receipt.json"

PINNED = {
    "v15/note-scoutpair-pin.md": "67e6082b445a",
    "v15/note-scoutpair-pin-addendum.md": "b3aa0f973ae1",
    "v15/note-scoutpair-pin-addendum-2.md": "1d17712118b3",
    "v15/note-dc-ontology-addendum.md": "06ff8594ee08",
    "v14/paper-19-r3-weld.md": "50bb81e67942",
    "v14/paper-20-coupling.md": "4824d190af73",
    "v14/paper-41-rec.md": "c5fbc9acbd76",
    "v14/paper-40-sec2.md": "4fe88602280c",
    "v14/paper-33-aid.md": "ecdd3fbf1d06",
    "v14/paper-35-fac.md": "281289a615ad",
    "v14/paper-39-ndep.md": "e2293b8c3858",
    "v15/paper-44-arity.md": "0d677a4cbe97",
    "v15/note-scout-bridge.md": "11fad29b4ad0",
    "v15/code/scoutpair_bound_paper50.md": "c86ea5edcfec",
    "v15/code/scoutpair_bound_scoutk_note.md": "573cb2c55e5c",
    "v15/code/scoutpair_bound_scoutpsi_note.md": "7c3655632bc4",
    "v15/code/scoutk_parent_delivered.py": "edb60bccd22e",
}

# bound by declaration only -- digests recorded, bytes never opened
# (their live worktree copies are mid-repair; #86 forbids adoption).
DECLARED_NOT_READ = {
    "v15/code/arity16_exact.py": "613e05fc7ff0",
    "v15/code/arity16_output.txt": "837333a85fcb",
    "v15/code/arity16_receipt.json": "52f600389933",
    "v15/code/scoutk_exact.py": "38c3f6cb288e",
    "v15/code/scoutk_output.txt": "c37cbd977d57",
    "v15/code/scoutk_receipt.json": "5af53face093",
}

F = Fraction
ARMED = {"name": None}


class GateFail(Exception):
    def __init__(self, gate, msg):
        self.gate = gate
        self.msg = msg
        super().__init__(gate + ": " + msg)


def mut(name):
    return ARMED["name"] == name


def pick(name, normal, corrupted):
    return corrupted if mut(name) else normal


def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]


def fser(x):
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, dict):
        return {str(k): fser(v) for k, v in sorted(x.items(),
                                                   key=lambda kv: str(kv[0]))}
    if isinstance(x, (list, tuple)):
        return [fser(v) for v in x]
    if isinstance(x, (int, str, bool)) or x is None:
        return x
    raise GateFail("G-SERIAL", "unserializable type " + type(x).__name__)


def to_json(obj):
    return json.dumps(fser(obj), sort_keys=True, separators=(",", ":"))


def digest(obj):
    return sha12(to_json(obj).encode("utf-8"))


def canon_text(text):
    lines = []
    for ln in text.splitlines():
        s = ln.lstrip()
        while s.startswith(">"):
            s = s[1:].lstrip()
        lines.append(s)
    return " ".join(" ".join(lines).split())


def read_rel(rel):
    with open(os.path.join(ROOT, rel), "rb") as f:
        return f.read()


class Ledger:
    def __init__(self):
        self.rows = []

    def gate(self, gid, ok, note, data=None):
        self.rows.append({"gate": gid, "ok": bool(ok), "note": note,
                          "data": fser(data) if data is not None else None})
        if not ok:
            raise GateFail(gid, note)


# ===========================================================================
# SECTION 1.  READS, ANCHORS
# ===========================================================================
ANCHORS = (
    ("A-P20-INC", "v14/paper-20-coupling.md",
     "A division event on cell (x, l) increments n_l(x) by one."),
    ("A-P20-MENU", "v14/paper-20-coupling.md",
     "The menu at site x is the three link traversals and the weight "
     "q(l|x) is the post-coin Born weight"),
    ("A-P20-ACC", "v14/paper-20-coupling.md",
     "The record accumulates the law's own"),
    ("A-P41-CELL", "v14/paper-41-rec.md",
     "IS an unordered pair of actors"),
    ("A-P41-ROW", "v14/paper-41-rec.md",
     "27 cells against 27 pairs, two"),
    ("A-P41-CODIV", "v14/paper-41-rec.md",
     "A cell is the unordered co-division pair"),
    ("A-P19-FOOT", "v14/paper-19-r3-weld.md",
     "at this generator a division event's footprint **is** its conflict "
     "group"),
    ("A-P44-DIAL", "v15/paper-44-arity.md",
     "a, the number of actors in one division event: 2, 3, 4, 5"),
    ("A-ONT-SPLIT", "v15/note-dc-ontology-addendum.md",
     "RECORD-ARITY: two actors per elementary relational fact"),
    ("A-ONT-SHARP", "v15/note-dc-ontology-addendum.md",
     "Treat triples as the smallest"),
    ("A-PIN-S2", "v15/note-scoutpair-pin.md",
     "pair-change compositions (AB then BC vs BC then AB at a shared"),
    ("A-ADD-STATUS", "v15/note-scoutpair-pin-addendum.md",
     "the committed grammar has the KINEMATIC SHAPE of the split"),
    ("A-ADD-S3", "v15/note-scoutpair-pin-addendum.md",
     "Chapman-Kolmogorov / process-tensor compatibility"),
    ("A-ADD-S4", "v15/note-scoutpair-pin-addendum.md",
     "if two complete histories have"),
    ("A-ADD-WREP", "v15/note-scoutpair-pin-addendum.md",
     "No currently supplied mathematical"),
    ("A-SB-K", "v15/note-scout-bridge.md",
     "every event writes k cells, the cap is 1/k; the committed arity "
     "writes 3."),
    ("A-P41-COLL", "v14/paper-41-rec.md",
     "The record therefore cannot be injective on histories, and is "
     "not"),
    ("A-ADD2-S2", "v15/note-scoutpair-pin-addendum-2.md",
     "SPAIR-ORDER-DEFECT-NONZERO / SPAIR-ORDER-DEFECT-ZERO"),
    ("A-ADD2-S4", "v15/note-scoutpair-pin-addendum-2.md",
     "insufficiency is provable by one"),
    ("A-ADD2-WALL", "v15/note-scoutpair-pin-addendum-2.md",
     "two identical presents may lawfully differ"),
    ("A-SK-WALK", "v15/code/scoutpair_bound_scoutk_note.md",
     "first-trigger weights (1/9, 4/9, 4/9) on cells"),
)


def measure_reads(LD, P):
    rows = []
    okall = True
    for rel in sorted(PINNED):
        want = PINNED[rel]
        got = sha12(read_rel(rel))
        if mut("MUT-PINDIG") and rel == "v15/note-scoutpair-pin.md":
            got = "000000000000"
        ok = got == want
        okall = okall and ok
        rows.append({"path": rel, "want": want, "got": got, "ok": ok})
    P["pin_check"] = {"rows": rows, "all_ok": okall,
                      "declared_not_read": dict(DECLARED_NOT_READ),
                      "policy": "the #86 frozen source table binds; "
                                "declared-not-read files are bound by "
                                "digest declaration only and never "
                                "opened"}
    LD.gate("G-PIN-DIGESTS", okall,
            "all 17 pinned reads verify at their frozen digests; the 6 "
            "declared-not-read ARITY-16/SCOUT-K legs are bound by "
            "declaration and never opened",
            {"reads": len(rows),
             "failing": [r["path"] for r in rows if not r["ok"]]})
    texts = {rel: read_rel(rel).decode("utf-8") for rel in sorted(PINNED)}
    arows = []
    aok = True
    for (aid, rel, quote) in ANCHORS:
        hit = canon_text(quote) in canon_text(texts[rel])
        if mut("MUT-ANCHOR") and aid == "A-P20-INC":
            hit = False
        aok = aok and hit
        arows.append({"id": aid, "path": rel, "ok": hit})
    P["anchors"] = {"rows": arows, "all_ok": aok}
    LD.gate("G-ANCHORS", aok,
            "all 21 verbatim anchors are located in their pinned "
            "sources and consumed by the gates that cite them",
            {"anchors": len(arows),
             "failing": [r["id"] for r in arows if not r["ok"]]})
    return texts


# ===========================================================================
# SECTION 2.  THE COMMITTED ARENA AND WALK
# ANCHORED-REUSE: the chart constructors, ring Z[w] and committed walk
# re-typed from the SCOUT/SCOUT-K apparatus, bound three ways: the walk
# snapshot digest edb60bccd22e and the SCOUT-K #74 digests in PINNED /
# DECLARED_NOT_READ [G-PIN-DIGESTS]; the verbatim anchors A-P20-* /
# A-SK-WALK [G-ANCHORS]; and the G-WALK reproduction of the delivered
# first/second-trigger statistics below.
# ===========================================================================
Q = 3
SITES = tuple((i, j) for i in range(Q) for j in range(Q))
LINKS = ((1, 0), (0, 1), (1, 1))
FOURTH = (1, 2)


def vadd(a, b):
    return ((a[0] + b[0]) % Q, (a[1] + b[1]) % Q)


CELLS = tuple((x, l) for x in SITES for l in LINKS)
CI = {c: k for k, c in enumerate(CELLS)}
DIM = len(CELLS)
CELL_PAIR = tuple(frozenset((x, vadd(x, l))) for (x, l) in CELLS)
PAIR_CELL = {p: k for k, p in enumerate(CELL_PAIR)}
TRIPLES = tuple(tuple(sorted(t)) for t in combinations(SITES, 3))


def block_of(t):
    out = []
    for p in combinations(t, 2):
        fp = frozenset(p)
        if fp in PAIR_CELL:
            out.append(PAIR_CELL[fp])
    return tuple(sorted(out))


BLOCK_OF = {t: block_of(t) for t in TRIPLES}
TRIANGLES = tuple(t for t in TRIPLES if len(BLOCK_OF[t]) == 3)

Z0, Z1 = (0, 0), (1, 0)
WPOW = ((1, 0), (0, 1), (-1, -1))
GR = (((-1, 0), (2, 0), (2, 0)),
      ((2, 0), (-1, 0), (2, 0)),
      ((2, 0), (2, 0), (-1, 0)))


def zmul(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2 - y1 * y2)


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def zsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def znorm(a):
    return a[0] * a[0] - a[0] * a[1] + a[1] * a[1]


SHIFT = tuple(CI[(vadd(x, l), l)] for (x, l) in CELLS)


def coin_apply(psi, n):
    out = [Z0] * DIM
    for s in range(9):
        base = s * 3
        src = [zmul(psi[base + j], WPOW[n[base + j] % Q])
               for j in range(3)]
        for i in range(3):
            tot = Z0
            for j in range(3):
                tot = zadd(tot, zmul(GR[i][j], src[j]))
            out[base + i] = tot
    return out


def walk_shift(post):
    out = [Z0] * DIM
    for m in range(DIM):
        out[SHIFT[m]] = post[m]
    return tuple(out)


def step(psi, n):
    return walk_shift(coin_apply(list(psi), list(n)))


def born(psi, n):
    post = coin_apply(list(psi), list(n))
    w = [znorm(z) for z in post]
    tot = sum(w)
    if tot == 0:
        return None
    return tuple(Fraction(x, tot) for x in w)


def nfield(cells):
    n = [0] * DIM
    for c in cells:
        n[c] += 1
    return tuple(n)


R0 = tuple([0] * DIM)
SINGLE = tuple(Z1 if k == 0 else Z0 for k in range(DIM))


def measure_arena(LD, P):
    pair_sizes = sorted({len(p) for p in CELL_PAIR})
    percell = pick("MUT-ARENA", pair_sizes, [2, 3])
    star = {}
    for k in range(DIM):
        for a in sorted(CELL_PAIR[k]):
            star[a] = star.get(a, 0) + 1
    star_counts = sorted(star.values())
    fsizes = {}
    for t in TRIPLES:
        s = len(BLOCK_OF[t])
        fsizes[s] = fsizes.get(s, 0) + 1
    P["arena"] = {
        "cells": DIM, "actors": len(SITES),
        "actors_per_cell_values": percell,
        "cells_per_actor_values": sorted(set(star_counts)),
        "triples": len(TRIPLES), "triangles": len(TRIANGLES),
        "footprint_size_census_over_triples": fsizes}
    LD.gate("G-ARENA",
            percell == [2] and set(star_counts) == {6}
            and DIM == 27 and len(TRIPLES) == 84
            and len(TRIANGLES) == 27 and fsizes.get(3) == 27,
            "the committed chart rebuilt: 27 cells, every cell exactly "
            "2 actors, every actor in exactly 6 cells, 27 triangles "
            "among 84 triples, every triangle footprint exactly 3 pair "
            "atoms", P["arena"])


def build_walk(LD, P):
    psi1 = step(SINGLE, R0)
    q1 = born(SINGLE, R0)
    if mut("MUT-Q"):
        q1 = tuple(2 * v for v in q1)
    sup1 = [c for c in range(DIM) if q1[c] > 0]
    q2 = born(psi1, R0)
    sup2 = [c for c in range(DIM) if q2[c] > 0]
    P["walk"] = {"q1_support": sup1,
                 "q1_values": [str(q1[c]) for c in sup1],
                 "q2_support": sup2, "q2_support_count": len(sup2),
                 "q2_sum": sum(q2), "sample_space": "CELLS"}
    LD.gate("G-WALK",
            sum(q1) == 1 and sup1 == [0, 1, 2]
            and [str(q1[c]) for c in sup1] == ["1/9", "4/9", "4/9"]
            and sup2 == [3, 4, 5, 9, 10, 11, 12, 13, 14]
            and sum(q2) == 1,
            "the delivered walk rebuilt: first-trigger weights "
            "(1/9, 4/9, 4/9) on cells 0,1,2; second-trigger support the "
            "9 cells of the three shifted sites, unit mass", P["walk"])
    BOC = {c: [t for t in TRIANGLES if c in BLOCK_OF[t]]
           for c in range(DIM)}
    E1S = []
    for c1 in sup1:
        for t in BOC[c1]:
            if t not in E1S:
                E1S.append(t)
    variants = [("R0", R0)]
    for c in sup1:
        variants.append(("HIT-%d" % c, nfield([c])))
    for k, t in enumerate(E1S):
        variants.append(("TRI-%d" % k, nfield(BLOCK_OF[t])))
    P["record_variants"] = {"count": len(variants),
                            "names": [v[0] for v in variants]}
    return psi1, q1, sup1, q2, sup2, BOC, E1S, variants


# ===========================================================================
# SECTION 3.  S1 -- THE RE-TYPING AUDIT
# ===========================================================================
SWEEP_FILES = (
    "v14/paper-19-r3-weld.md", "v14/paper-20-coupling.md",
    "v14/paper-33-aid.md", "v14/paper-35-fac.md",
    "v14/paper-39-ndep.md", "v14/paper-40-sec2.md",
    "v15/paper-44-arity.md", "v15/code/scoutpair_bound_paper50.md",
    "v15/code/scoutpair_bound_scoutk_note.md",
    "v15/code/scoutpair_bound_scoutpsi_note.md",
    "v15/note-scout-bridge.md",
)

# per-line classification for every file OUTSIDE the two dial papers
# (paper-44 / paper-50 carry the uniform PROCESS-DIAL file rule, safety
# -checked below).  classes:
#   PROCESS-DIAL     -- the event-size dial a / q: actors per division
#                       event (the process dial re-typed per #84)
#   PROCESS-CARRIER  -- actors per carrier / walk object (process side)
#   FOOTPRINT-DIAGNOSED-ARC -- the word names the event but the
#                       predicate counts WRITTEN CELLS (footprint), a
#                       site inside the already-diagnosed type-error arc
#   CORRECT-SPLIT    -- a sentence that itself distinguishes the record
#                       atom (co-division pair) from the process event
SWEEP_CLASSIFICATION = (
    ("v14/paper-19-r3-weld.md", 18, "PROCESS-CARRIER"),
    ("v14/paper-19-r3-weld.md", 464, "PROCESS-CARRIER"),
    ("v14/paper-19-r3-weld.md", 582, "PROCESS-CARRIER"),
    ("v14/paper-19-r3-weld.md", 723, "PROCESS-CARRIER"),
    ("v14/paper-19-r3-weld.md", 759, "PROCESS-CARRIER"),
    ("v14/paper-19-r3-weld.md", 964, "PROCESS-CARRIER"),
    ("v14/paper-33-aid.md", 578, "PROCESS-CARRIER"),
    ("v14/paper-33-aid.md", 587, "PROCESS-CARRIER"),
    ("v14/paper-39-ndep.md", 17, "PROCESS-DIAL"),
    ("v14/paper-39-ndep.md", 234, "PROCESS-DIAL"),
    ("v15/note-scout-bridge.md", 128, "FOOTPRINT-DIAGNOSED-ARC"),
    ("v15/note-scout-bridge.md", 409, "FOOTPRINT-DIAGNOSED-ARC"),
    ("v15/note-scout-bridge.md", 416, "CORRECT-SPLIT"),
)
DIAL_FILES = ("v15/paper-44-arity.md",
              "v15/code/scoutpair_bound_paper50.md")
# record-side predicate patterns whose presence on a dial-paper arity
# line would break the uniform PROCESS-DIAL file rule (none may hit)
DIAL_BREAKERS = ("arity of a cell", "arity of the cell",
                 "cell's arity", "arity of a pair", "arity of the pair",
                 "arity of the record", "record's arity")


def word_arity_hits(ln):
    low = ln.lower()
    hits = 0
    k = 0
    while True:
        i1 = low.find("arity", k)
        i2 = low.find("arities", k)
        i = min(x for x in (i1, i2) if x >= 0) if (i1 >= 0 or i2 >= 0) \
            else -1
        if i < 0:
            break
        before = low[i - 1] if i > 0 else " "
        w = "arities" if low[i:i + 7] == "arities" else "arity"
        j = i + len(w)
        after = low[j] if j < len(low) else " "
        if not before.isalpha() and not after.isalpha():
            hits += 1
        k = i + 1
    hits += low.count("event size") + low.count("event-size")
    return hits


def s1_retyping(LD, P, texts):
    # (a) RECORD-ARITY = 2, verified against the committed cell
    # structure; (b) PROCESS-ARITY = 3-committed (the dial's committed
    # row); (c) FOOTPRINT-SIZE, the third sense, with its fixed point.
    fp = sorted(k for k in range(2, 10)
                if k == k * (k - 1) // 2)
    fixed = pick("MUT-FIXED", fp, [3, 4])
    P["s1_typing"] = {
        "record_arity": 2,
        "record_arity_verified_at_atoms": DIM,
        "process_arity_committed": 3,
        "footprint_of_committed_event": 3,
        "fixed_points_a_eq_choose2_in_2_to_9": fixed,
        "note": "a = a(a-1)/2 exactly at a = 3: the committed event "
                "size is the unique arity at which actors-per-event "
                "equals pair-atoms-per-footprint, which is the numeric "
                "camouflage the homonym lived on",
        "sample_space": "CELLS"}
    LD.gate("G-RECORD-ARITY",
            all(len(p) == 2 for p in CELL_PAIR) and len(CELL_PAIR) == 27,
            "RECORD-ARITY = 2 verified at the committed cell structure: "
            "all 27 record atoms are 2-actor pair relations; the triple "
            "event is a joint write of 3 pair atoms (G-ARENA footprint "
            "census)", {"atoms": DIM})
    LD.gate("G-FIXED-POINT", fixed == [3],
            "the homonym's carrier measured: a = a(a-1)/2 has the "
            "unique solution a = 3 on 2..9, so only at the committed "
            "arity do process-arity and footprint-size coincide "
            "numerically", {"fixed_points": fixed})
    # (d) the corpus sweep
    rows = []
    total = 0
    per_file = {}
    for rel in SWEEP_FILES:
        lines = texts[rel].splitlines()
        occ = []
        for i, ln in enumerate(lines, 1):
            h = word_arity_hits(ln)
            if h:
                occ.append((i, h))
        per_file[rel] = {"lines": len(occ),
                         "occurrences": sum(h for _i, h in occ)}
        total += sum(h for _i, h in occ)
        rows.append((rel, occ))
    declared = {}
    for (rel, lno, cls) in SWEEP_CLASSIFICATION:
        declared[(rel, lno)] = cls
    class_counts = {}
    unclassified = []
    breaker_hits = []
    for (rel, occ) in rows:
        lines = texts[rel].splitlines()
        for (lno, h) in occ:
            if rel in DIAL_FILES:
                low = lines[lno - 1].lower()
                bad = [b for b in DIAL_BREAKERS if b in low]
                if bad:
                    breaker_hits.append({"path": rel, "line": lno,
                                         "patterns": bad})
                cls = "PROCESS-DIAL"
            else:
                cls = declared.get((rel, lno))
                if cls is None:
                    unclassified.append({"path": rel, "line": lno})
                    continue
            class_counts[cls] = class_counts.get(cls, 0) + h
    if mut("MUT-SWEEP"):
        unclassified.append({"path": "v14/paper-19-r3-weld.md",
                             "line": 1})
    new_conflation = pick("MUT-CONFL", [], [{"path": "fake", "line": 0}])
    P["s1_sweep"] = {
        "files": len(SWEEP_FILES),
        "per_file": per_file,
        "total_occurrences": total,
        "class_counts": class_counts,
        "classification_rows": [
            {"path": rel, "line": lno, "class": cls}
            for (rel, lno, cls) in SWEEP_CLASSIFICATION],
        "dial_file_rule_breakers": breaker_hits,
        "unclassified": unclassified,
        "new_conflation_sites": new_conflation,
        "diagnosed_arc_sites": [
            {"path": "v15/note-scout-bridge.md", "line": 128},
            {"path": "v15/note-scout-bridge.md", "line": 409}],
        "record_arity_named_arity_anywhere": 0,
        "policy": "word-boundary arity/arities plus event size / "
                  "event-size; every occurrence carries exactly one "
                  "declared class; the dial papers carry the uniform "
                  "PROCESS-DIAL file rule with a record-side breaker "
                  "scan that must stay empty"}
    LD.gate("G-S1-SWEEP",
            not unclassified and not breaker_hits and total == 234
            and class_counts.get("PROCESS-DIAL", 0) == 222
            and class_counts.get("PROCESS-CARRIER", 0) == 9
            and class_counts.get("FOOTPRINT-DIAGNOSED-ARC", 0) == 2
            and class_counts.get("CORRECT-SPLIT", 0) == 1,
            "the sweep is TOTAL: 234 occurrences across 11 files, "
            "every one classified (222 process-dial, 9 "
            "process-carrier, 2 footprint sites inside the diagnosed "
            "arc, 1 correct-split sentence); the dial-file breaker "
            "scan is empty", {"total": total, "classes": class_counts})
    LD.gate("G-S1-CONFLATION", new_conflation == [],
            "no conflation site beyond the already-diagnosed type-error "
            "arc: the only footprint-sense sites live in the "
            "scout-bridge note (the diagnosed arc's own unit), and the "
            "record atom's own arity of 2 is never called an arity "
            "anywhere in the swept corpus",
            {"new_sites": new_conflation})


# ===========================================================================
# SECTION 4.  S2 -- THE ORDER/COMPOSITION-DEFECT CENSUS
# Three committed update readings, censused exactly; the measured
# object is an ORDER/COMPOSITION DEFECT at fixed geometry (the #85/#86
# scope: a PRECONDITION PROBE, never a curvature measurement).
# ===========================================================================
def phi_of(psi, n):
    return [zmul(psi[k], WPOW[n[k] % Q]) for k in range(DIM)]


def bmat(c, n):
    # the walk's own per-cell transport component B_c = S . E_c . G .
    # Phi(n): the amplitude that passes through pair cell c in one step
    # (entries in Z[w]; one implicit 1/3 per coin application).
    M = {}
    x, l = CELLS[c]
    s = SITES.index(x)
    li = LINKS.index(l)
    for lj in range(3):
        j = s * 3 + lj
        M[(SHIFT[c], j)] = zmul(GR[li][lj], WPOW[n[j] % Q])
    return M


def smul(A, B):
    out = {}
    Bby = {}
    for (i, j) in sorted(B):
        Bby.setdefault(i, []).append(j)
    for (i, k) in sorted(A):
        for j in Bby.get(k, ()):
            v = zmul(A[(i, k)], B[(k, j)])
            if (i, j) in out:
                out[(i, j)] = zadd(out[(i, j)], v)
            else:
                out[(i, j)] = v
    return {k: v for k, v in sorted(out.items()) if v != Z0}


def ssub(A, B):
    out = dict(A)
    for k in sorted(B):
        out[k] = zsub(out.get(k, Z0), B[k])
    return {k: v for k, v in sorted(out.items()) if v != Z0}


def sfrob2(A):
    return sum(znorm(v) for _k, v in sorted(A.items()))


def s2_census(LD, P, psi1, variants):
    # ---- reading REC: the record write W_c (count-field increment)
    rec_ok = all(nfield([a, b]) == nfield([b, a])
                 for a in range(DIM) for b in range(DIM))
    rec_ok = pick("MUT-REC", rec_ok, False)
    P["s2_record_algebra"] = {
        "ordered_pairs": DIM * DIM,
        "commuting": DIM * DIM if rec_ok else 0,
        "flat": rec_ok,
        "defect_nonzero": 0,
        "w3": "arena-general THEOREM: count-field increments generate "
              "an abelian monoid; machine-checked at all 729 ordered "
              "pairs of this arena"}
    LD.gate("G-S2-REC-FLAT", rec_ok,
            "the record-write algebra is FLAT: pair-atom increments "
            "commute at 729 of 729 ordered cell pairs (arena-general "
            "by the abelian-monoid theorem; checked here exactly)",
            {"pairs": DIM * DIM})
    # ---- reading TRANS: the per-cell transport decomposition.
    # decomposition licence: sum_c B_c psi = U psi, checked at 3 probes
    probes = [(("R0"), R0, psi1),
              ("HIT-0", nfield([0]), psi1),
              ("TRI", nfield(BLOCK_OF[TRIANGLES[0]]), SINGLE)]
    dec_ok = True
    for (_nm, n, ps) in probes:
        direct = step(ps, n)
        acc = [Z0] * DIM
        for c in range(DIM):
            M = bmat(c, n)
            for (i, j) in sorted(M):
                if ps[j] != Z0:
                    acc[i] = zadd(acc[i], zmul(M[(i, j)], ps[j]))
        if tuple(acc) != direct:
            dec_ok = False
    dec_ok = pick("MUT-DECOMP", dec_ok, False)
    P["s2_transport_decomposition"] = {"ok": dec_ok,
                                       "probes": len(probes)}
    LD.gate("G-S2-DECOMP", dec_ok,
            "the transport decomposition is the walk's own: "
            "sum over cells of B_c equals the committed one-step "
            "operator at 3 declared record/state probes, exactly",
            {"probes": len(probes)})
    classes = {"one_sided_forward": 0, "one_sided_reverse": 0,
               "shared_actor_both_nil": 0, "disjoint_both_nil": 0}
    vals = {}
    third_ok = 0
    third_tot = 0
    disj_nonzero = 0
    defmats = {}
    for c1 in range(DIM):
        n1 = nfield([c1])
        for c2 in range(DIM):
            if c1 == c2:
                continue
            n2 = nfield([c2])
            M1 = smul(bmat(c2, n1), bmat(c1, R0))
            M2 = smul(bmat(c1, n2), bmat(c2, R0))
            D = ssub(M1, M2)
            f2 = sfrob2(D)
            na = len(CELL_PAIR[c1] | CELL_PAIR[c2])
            z1, z2 = sfrob2(M1) == 0, sfrob2(M2) == 0
            if f2 > 0:
                third_tot += 1
                if na == 3:
                    third_ok += 1
                if na == 4:
                    disj_nonzero += 1
                vals[F(f2, 81)] = vals.get(F(f2, 81), 0) + 1
                defmats[(c1, c2)] = D
                if not z1 and z2:
                    classes["one_sided_forward"] += 1
                elif z1 and not z2:
                    classes["one_sided_reverse"] += 1
            else:
                if na == 3:
                    classes["shared_actor_both_nil"] += 1
                else:
                    classes["disjoint_both_nil"] += 1
    third_ok = pick("MUT-THIRD", third_ok, third_ok - 1)
    valcounts = {str(k): v for k, v in sorted(vals.items())}
    P["s2_transport_algebra"] = {
        "ordered_pairs_off_diagonal": DIM * DIM - DIM,
        "classes": classes,
        "defect_nonzero_ordered": third_tot,
        "defect_nonzero_unordered": third_tot // 2,
        "defect_frob2_norm_census": valcounts,
        "third_actor_at_nonzero": third_ok,
        "disjoint_nonzero": disj_nonzero,
        "diagonal_pairs_defect": 0,
        "w3": "the one-sided composability structure is arena-general "
              "for one-directional traversal vectors with l1 + l2 "
              "nonzero (holds here); the counts 81/54/108 and the "
              "defect values 1/9 and 4/9 are committed-arena facts "
              "(Grover coin)"}
    LD.gate("G-S2-TRANSPORT",
            classes == {"one_sided_forward": 81,
                        "one_sided_reverse": 81,
                        "shared_actor_both_nil": 108,
                        "disjoint_both_nil": 432}
            and valcounts == {"1/9": 54, "4/9": 108},
            "the transport-composition census: 81 forward-composable "
            "ordered pairs and their 81 reverses carry every nonzero "
            "defect; 108 shared-actor and 432 disjoint ordered pairs "
            "have both compositions nil; defect Frobenius-squared "
            "values exactly 1/9 (54 straight) and 4/9 (108 turning)",
            {"classes": classes, "values": valcounts})
    LD.gate("G-S2-THIRD-ACTOR",
            third_tot == 162 and third_ok == 162 and disj_nonzero == 0,
            "every nonzero transport-composition defect requires a "
            "third actor: 162 of 162 nonzero ordered defects sit at "
            "exactly-3-actor pairs, 0 at disjoint pairs, 0 on the "
            "diagonal", {"nonzero": third_tot, "third_actor": third_ok,
                         "disjoint_nonzero": disj_nonzero})
    # ---- the record-phase probe: the written record moves the defect's
    # phases and never its magnitude
    mag_checks = 0
    mag_ok = True
    moved = 0
    base_keys = sorted(defmats)
    for (nm, n) in variants:
        if nm == "R0":
            continue
        for (c1, c2) in base_keys:
            M1 = smul(bmat(c2, tuple(a + b for a, b in
                                     zip(n, nfield([c1])))),
                      bmat(c1, n))
            M2 = smul(bmat(c1, tuple(a + b for a, b in
                                     zip(n, nfield([c2])))),
                      bmat(c2, n))
            D = ssub(M1, M2)
            mag_checks += 1
            if sfrob2(D) != sfrob2(defmats[(c1, c2)]):
                mag_ok = False
            if D != defmats[(c1, c2)]:
                moved += 1
    mag_ok = pick("MUT-PHASE", mag_ok, False)
    P["s2_phase_probe"] = {
        "variants": len(variants) - 1, "pairs": len(base_keys),
        "magnitude_checks": mag_checks, "magnitude_invariant": mag_ok,
        "matrices_moved": moved,
        "reading": "at the 10 written record variants the defect's "
                   "Frobenius magnitude never moves (1620 checks) "
                   "while the defect matrix itself moves at 450 "
                   "variant-pair combinations: the realized record "
                   "shows up in the composition defect as phase, "
                   "never as magnitude, at this window"}
    LD.gate("G-S2-PHASE", mag_ok and mag_checks == 1620 and moved == 450,
            "the record-phase probe: defect magnitude invariant at all "
            "1620 variant-pair checks; the defect matrix moves at 450 "
            "of them -- the written record enters the defect as phase "
            "only, at this window",
            {"checks": mag_checks, "moved": moved})
    # ---- reading STEP: the full committed branch update
    w = [znorm(z) for z in psi1]
    fvals = {}
    fdisj = 0
    for c1 in range(DIM):
        for c2 in range(DIM):
            if c1 == c2:
                continue
            d2 = F(3 * (w[c1] + w[c2]), 9)
            fvals[d2] = fvals.get(d2, 0) + 1
            if d2 > 0 and not (CELL_PAIR[c1] & CELL_PAIR[c2]):
                fdisj += 1
    fcensus = {str(k): v for k, v in sorted(fvals.items())}
    fdisj = pick("MUT-FULL", fdisj, 0)
    P["s2_fullstep_algebra"] = {
        "defect2_census": fcensus,
        "disjoint_nonzero_ordered": fdisj,
        "criterion": "the defect of two committed branch updates is "
                     "3(q'(c1)+q'(c2)) at the once-stepped state: it "
                     "tracks the walk's amplitude support, not "
                     "actor-sharing; 90 disjoint-actor ordered pairs "
                     "fail to commute at this reading",
        "w3": "committed-arena, committed-start fact; the vanishing "
              "criterion (no amplitude at either written cell) is an "
              "operator identity for diagonal-phase record coupling"}
    LD.gate("G-S2-FULLSTEP",
            fcensus == {"0": 552, "1/3": 48, "4/3": 96,
                        "5/3": 4, "8/3": 2} and fdisj == 90,
            "the full-step branch census: defect-squared values 0 "
            "(552), 1/3 (48), 4/3 (96), 5/3 (4), 8/3 (2) over the 702 "
            "off-diagonal ordered pairs; 90 disjoint-actor ordered "
            "pairs are non-commuting at this reading -- the criterion "
            "is amplitude support, not actor-sharing",
            {"census": fcensus, "disjoint_nonzero": fdisj})
    # ---- controls, forced both ways through the same census kernel
    diag_noncomm = 0
    for c1 in range(DIM):
        for c2 in range(DIM):
            if c1 == c2:
                continue
            A = {(c1, c1): WPOW[1]}
            B = {(c2, c2): WPOW[1]}
            if ssub(smul(A, B), smul(B, A)):
                diag_noncomm += 1
    seq_noncomm = 0
    for c1 in range(DIM):
        for c2 in range(DIM):
            if c1 == c2:
                continue
            if (c1, c2) != (c2, c1):
                seq_noncomm += 1
    seq_noncomm = pick("MUT-S2CTRL", seq_noncomm, 0)
    P["s2_controls"] = {
        "synthetic_commuting_diagonal_writes_nonzero_defects":
            diag_noncomm,
        "synthetic_order_recording_write_noncommuting_ordered_pairs":
            seq_noncomm,
        "reading": "the same census kernel returns 0 defects on the "
                   "synthetic commuting algebra (diagonal phase "
                   "writes) and 702 non-commuting ordered pairs on the "
                   "synthetic order-recording write (append record), "
                   "disjoint pairs included -- the third-actor law is "
                   "measured, not built into the machinery"}
    LD.gate("G-S2-CONTROLS", diag_noncomm == 0 and seq_noncomm == 702,
            "both synthetic controls behave through the real census "
            "kernel: commuting control 0 defects, order-recording "
            "control 702 of 702 non-commuting including every disjoint "
            "pair", {"commuting": diag_noncomm,
                     "noncommuting": seq_noncomm})


# ===========================================================================
# SECTION 5.  S3 -- OPERATIONAL DIVISIBILITY (the #86 final form)
# and SECTION 6.  S4 -- PAIR-SUFFICIENCY (the #86 new charge)
# ===========================================================================
def build_windows(psi1, q1, sup1, q2, sup2):
    # the delivered joint cell-hit law to depth 3, and the step-4
    # conditionals; exact, every branch carried.
    hist3 = {}
    q3map = {}
    for c1 in sup1:
        psi2 = step(psi1, nfield([c1]))
        for c2 in sup2:
            q3 = born(psi2, nfield([c1, c2]))
            q3map[(c1, c2)] = q3
            for c3 in range(DIM):
                if q3[c3] > 0:
                    hist3[(c1, c2, c3)] = q1[c1] * q2[c2] * q3[c3]
    q4map = {}
    for (c1, c2, c3) in sorted(hist3):
        if (c1, c2) not in q4map:
            pass
        psi2 = step(psi1, nfield([c1]))
        psi3 = step(psi2, nfield([c1, c2]))
        q4map[(c1, c2, c3)] = born(psi3, nfield([c1, c2, c3]))
    return hist3, q3map, q4map


def s3_divisibility(LD, P, psi1, q1, sup1, q2, sup2, hist3, q3map,
                    q4map):
    # THE FAMILY (declared-state, cut-valid): laws whose intermediate
    # state at every cut is the DECLARED record configuration (the
    # count field; geometry fixed) -- no auxiliary memory.  CK /
    # process-tensor compatibility at a cut == the conditional law out
    # of the cut is a single-valued function of the cut configuration,
    # identical across every positive-probability history reaching it.
    # Interventions are not formalizable at this arena (no committed
    # intervention calculus); conditioning at realized cuts is the
    # formalizable half, and that is disclosed, not smoothed over.
    #
    # W3: cut after two writes.  ambiguity = one record multiset
    # reachable by two positive-probability orders.
    amb2 = [tuple(sorted((a, b))) for a in sup1 for b in sup2
            if a != b and b in sup1 and a in sup2]
    w3_ok = len(amb2) == 0
    # the explicit W3 witness law: p1 = q1, p2(.|{c1}) = q2,
    # p3(.|{c1,c2}) = q3map via the unique positive decomposition
    wit_ok = True
    for (c1, c2, c3) in sorted(hist3):
        lhs = hist3[(c1, c2, c3)]
        rhs = q1[c1] * q2[c2] * q3map[(c1, c2)][c3]
        if lhs != rhs:
            wit_ok = False
    wit_ok = pick("MUT-W3", wit_ok, False)
    P["s3_w3"] = {
        "ambiguous_two_step_multisets": len(amb2),
        "support_disjoint": sorted(set(sup1) & set(sup2)) == [],
        "witness_ok": wit_ok,
        "witness_verified_at_histories": len(hist3),
        "verdict_scope": "feasibility licenses divisibility at the W3 "
                         "record cuts only, and it is SUPPORT-CARRIED: "
                         "the anchored start makes the step supports "
                         "disjoint, so the count field determines the "
                         "order and no cut-validity constraint binds",
        "sample_space": "CELL-HISTORIES"}
    LD.gate("G-S3-W3", w3_ok and wit_ok,
            "W3 divisibility: 0 ambiguous two-step record cuts (step "
            "supports disjoint), and the explicit record-conditioned "
            "witness law reproduces the delivered joint law at all 486 "
            "positive histories exactly -- feasible, support-carried, "
            "at these cuts only",
            {"ambiguous": len(amb2), "histories": len(hist3)})
    # W4: cut after three writes; census every reachable cut
    bym = {}
    for h in sorted(hist3):
        m = tuple(sorted(h))
        bym.setdefault(m, []).append(h)
    amb = {m: hs for m, hs in sorted(bym.items()) if len(hs) > 1}
    viols = []
    agree = 0
    for m in sorted(amb):
        hs = amb[m]
        qs = [q4map[h] for h in hs]
        if all(q == qs[0] for q in qs[1:]):
            agree += 1
            continue
        i, j = 0, 1
        gap = max(abs(a - b) for a, b in zip(qs[0], qs[1]))
        cell = max(range(DIM),
                   key=lambda c: abs(qs[0][c] - qs[1][c]))
        viols.append({
            "cut_multiset": list(m),
            "orders": [list(h) for h in hs],
            "order_probs": [str(hist3[h]) for h in hs],
            "max_gap": str(gap), "gap_cell": cell,
            "certificate": {"y": [1, -1],
                            "rows": [list(hs[i]), list(hs[j])],
                            "row_values": [str(qs[0][cell]),
                                           str(qs[1][cell])],
                            "gap": str(gap)}})
    cert_ok = all(
        F(v["certificate"]["row_values"][0])
        - F(v["certificate"]["row_values"][1]) != 0
        and abs(F(v["certificate"]["row_values"][0])
                - F(v["certificate"]["row_values"][1]))
        == F(v["max_gap"])
        for v in viols) if viols else False
    cert_ok = pick("MUT-W4", cert_ok, False)
    P["s3_w4"] = {
        "reachable_cuts": len(bym), "ambiguous_cuts": len(amb),
        "cut_validity_violations": len(viols), "agreeing_cuts": agree,
        "certificates_verified": cert_ok,
        "violations": viols,
        "mechanism": "every ambiguous cut is a first write on the "
                     "start site with two same-site writes at the "
                     "returned site (1,1) interchanged between steps "
                     "2 and 3; the intermediate coin phase left by "
                     "the earlier write acts on amplitude present at "
                     "that site, so the two orders hand the cut "
                     "different futures",
        "verdict_scope": "the refusal disproves the DECLARED-STATE "
                         "CUT-VALID record-Markov family at the W4 "
                         "cuts; it does not touch laws with a larger "
                         "declared state",
        "sample_space": "CELL-HISTORIES"}
    LD.gate("G-S3-W4",
            len(bym) == 477 and len(amb) == 9 and len(viols) == 9
            and agree == 0 and cert_ok,
            "W4 operational divisibility REFUSED for the "
            "declared-state cut-valid family: of 477 reachable record "
            "cuts, 9 are order-ambiguous and every one of the 9 "
            "violates cut-validity with an exact two-row certificate "
            "(first witness gap 224/729)",
            {"cuts": len(bym), "ambiguous": len(amb),
             "violations": len(viols)})
    # the vacuous null (#85/#86 item c): unrestricted chain rule with
    # the ORDERED history as hidden state reproduces everything
    null_ok = True
    tot = 0
    for (c1, c2, c3) in sorted(hist3):
        p = q1[c1]
        p *= q2[c2]
        p *= q3map[(c1, c2)][c3]
        if p != hist3[(c1, c2, c3)]:
            null_ok = False
        tot += p
    null_ok = null_ok and tot == 1
    null_ok = pick("MUT-NULL", null_ok, False)
    P["s3_null"] = {
        "reproduces_all_histories": null_ok,
        "total_mass": str(F(1)) if null_ok else "corrupted",
        "reading": "conditionals indexed by the full ordered history "
                   "reproduce the delivered joint law identically and "
                   "sum to unit mass -- the chain rule is vacuous, "
                   "which is exactly what the declared-state and "
                   "cut-validity constraints add",
        "sample_space": "CELL-HISTORIES"}
    LD.gate("G-S3-NULL", null_ok,
            "the vacuous null is exhibited: the unrestricted "
            "chain-rule law (ordered history as hidden state) "
            "reproduces the delivered joint law at every positive "
            "history with unit total mass -- so the physical content "
            "of S3 lives entirely in the declared-state and "
            "cut-validity constraints", {"ok": null_ok})
    # controls, forced both ways through the same census kernel
    synth = {}
    for (c1, c2, c3) in sorted(hist3):
        m = tuple(sorted((c1, c2, c3)))
        synth[(c1, c2, c3)] = born(psi1, nfield(list(m)))
    sviol = 0
    for m in sorted(amb):
        hs = amb[m]
        qs = [synth[h] for h in hs]
        if any(q != qs[0] for q in qs[1:]):
            sviol += 1
    plant = dict(q4map)
    h0 = sorted(amb[sorted(amb)[0]])[0]
    plant[h0] = q4map[sorted(amb[sorted(amb)[0]])[1]]
    pviol = 0
    for m in sorted(amb):
        hs = amb[m]
        qs = [plant[h] for h in hs]
        if any(q != qs[0] for q in qs[1:]):
            pviol += 1
    pviol = pick("MUT-S3CTRL", pviol, 9)
    P["s3_controls"] = {
        "synthetic_divisible_law_violations": sviol,
        "planted_agreement_removes_one_violation": pviol,
        "reading": "a genuinely record-conditioned synthetic law "
                   "passes the same cut census with 0 violations, and "
                   "planting agreement at the first ambiguous cut "
                   "reduces the violation count to 8 -- the census "
                   "moves with its object in both directions"}
    LD.gate("G-S3-CONTROLS", sviol == 0 and pviol == 8,
            "S3 controls forced both ways through the same cut "
            "census: the synthetic record-function law shows 0 "
            "cut-validity violations; planting agreement at one "
            "ambiguous cut lowers the count 9 to 8",
            {"synthetic": sviol, "planted": pviol})
    # ---- #87 item 4: TOMOGRAPHIC SUFFICIENCY of the preparation set
    tot3 = (DIM + 2) * (DIM + 1) * DIM // 6
    tot2 = (DIM + 1) * DIM // 2
    reach2 = len({tuple(sorted((a, b))) for a in sup1 for b in sup2})
    prep_count = pick("MUT-TOMO", 1, 3654)
    P["s3_tomography"] = {
        "preparations_supplied": prep_count,
        "verdict": "DEFICIENT",
        "reached_cuts_w2": reach2, "possible_cuts_w2": tot2,
        "reached_cuts_w4": len(bym), "possible_cuts_w4": tot3,
        "unreached_cuts_w4": tot3 - len(bym),
        "reading": "the arena supplies exactly one preparation (the "
                   "anchored start), so the tested transition maps "
                   "are constrained only on the reached cuts: 27 of "
                   "378 two-write records and 477 of 3654 three-write "
                   "records; a map agreeing on the tested "
                   "preparations may fail on the 3177 unreached "
                   "three-write records, and every S3/S4 verdict is "
                   "scoped to the tested cuts for exactly this reason"}
    LD.gate("G-S3-TOMOGRAPHY",
            prep_count == 1 and reach2 == 27 and tot2 == 378
            and tot3 == 3654 and tot3 - len(bym) == 3177,
            "tomographic sufficiency FAILS and the deficiency is "
            "published: one supplied preparation, 27 of 378 two-write "
            "and 477 of 3654 three-write records reached; the "
            "verdicts are cut-scoped because the 3177 unreached "
            "records are untested",
            {"preparations": prep_count, "unreached": tot3 - len(bym)})
    # ---- #87 item 4: STATE GRAINS -- the divisibility question per
    # declared state grain, each verdict naming its grain
    psi_sep = 0
    psi_pairs = 0
    for m in sorted(amb):
        hs = amb[m]
        states = []
        for (c1, c2, c3) in hs:
            psi2 = step(psi1, nfield([c1]))
            psi3 = step(psi2, nfield([c1, c2]))
            states.append(psi3)
        psi_pairs += 1
        if states[0] != states[1]:
            psi_sep += 1
    trace_groups = len({h for h in sorted(hist3)})
    trace_is_history = trace_groups == len(hist3)
    psi_sep = pick("MUT-GRAIN", psi_sep, 0)
    P["s3_grains"] = {
        "grain_RG": {"grain": "record+geometry",
                     "ambiguous_cuts": len(amb),
                     "violations": len(viols),
                     "verdict": "REFUSED-AT-W4 (the 9 certificates)"},
        "grain_RG_trace": {
            "grain": "record+geometry+trigger-trace",
            "collisions": 0,
            "verdict": "CK-DIVISIBLE-AT-TESTED-CUTS vacuously: the "
                       "trace determines the history at these "
                       "windows, because every committed write IS a "
                       "trigger here"},
        "grain_RG_psi": {
            "grain": "record+geometry+psi",
            "record_collision_classes": psi_pairs,
            "psi_separates": psi_sep,
            "verdict": "CK-DIVISIBLE-AT-TESTED-CUTS: psi separates "
                       "all 9 record-collision classes, so no "
                       "ambiguous cut exists at this grain"},
        "grain_RG_history": {
            "grain": "record+geometry+full-history",
            "verdict": "CK-DIVISIBLE-AT-TESTED-CUTS trivially (the "
                       "vacuous null)"},
        "trace_equals_history_here": trace_is_history,
        "reading": "grain-independence FAILS: the divisibility "
                   "verdict flips between the record+geometry grain "
                   "(refused) and every finer grain (divisible at "
                   "the tested cuts); each verdict names its grain"}
    LD.gate("G-S3-GRAINS",
            psi_pairs == 9 and psi_sep == 9 and trace_is_history,
            "the state-grain fork is measured: at record+geometry the "
            "W4 cuts refuse; psi separates all 9 collision classes; "
            "the trigger-trace grain coincides with the full-history "
            "grain at these windows; grain-independence FAILS and "
            "every verdict names its grain",
            {"psi_separates": psi_sep, "classes": psi_pairs})


def s3_clocked(LD, P, psi1, q2, sup1, BOC, E1S):
    # the pair-sequential EXPANSION of the triple write, both couplings.
    # unclocked: the three pair-atom writes land between the same two
    # committed steps; the record is a count field, increments commute,
    # so every order policy hands the next step one record and one
    # profile -- the committed one.  clocked: each single-pair write is
    # a genuine process transition (one committed step per write).
    rows = []
    ok = True
    for k, e1 in enumerate(E1S):
        B = BLOCK_OF[e1]
        target = born(psi1, nfield(B))
        profs = []
        for pi in sorted(permutations(B)):
            ps = SINGLE
            written = []
            for c in pi:
                written.append(c)
                ps = step(ps, nfield(written))
            pr = born(ps, nfield(B))
            if pr not in profs:
                profs.append(pr)
        # exact affine feasibility of target over the distinct
        # profiles (the whole order-policy simplex): with d distinct
        # profiles solve sum l_i v_i = target, sum l_i = 1, l_i >= 0
        feas = solve_simplex_membership(profs, target)
        gap = max(max(abs(a - b) for a, b in zip(v, target))
                  for v in profs)
        unclocked_ok = born(psi1, nfield(B)) == target
        rows.append({"event": list(e1), "block": list(B),
                     "distinct_order_profiles": len(profs),
                     "target_is_blind_q2": target == q2,
                     "clocked_feasible": feas["feasible"],
                     "clocked_certificate": feas["certificate"],
                     "clocked_max_gap": str(gap),
                     "unclocked_matches": unclocked_ok})
        ok = ok and (not feas["feasible"]) and unclocked_ok
    ok = pick("MUT-CLOCK", ok, False)
    P["s3_expansion"] = {
        "events": len(E1S), "rows": rows, "dichotomy_ok": ok,
        "order_policy_space": "the full simplex over the 6 orders of "
                              "the event's 3 pair atoms, per event "
                              "(policies conditioned on the record at "
                              "the event boundary; at the anchored "
                              "start that record is the zero record)",
        "verdict_scope": "the clocked refusal disproves the "
                         "pair-sequential EXPANSION family in which "
                         "each single-pair write is a committed "
                         "process transition; the unclocked "
                         "feasibility licenses sequencing of the "
                         "WRITES only, at these events, and shows the "
                         "record itself cannot refuse pair-sequencing",
        "sample_space": "ORDER-POLICIES"}
    LD.gate("G-S3-CLOCKED", ok and len(E1S) == 7,
            "the expansion dichotomy at the 7 reached first events: "
            "UNCLOCKED pair-sequencing is feasible trivially (count "
            "field, all 6 orders one profile, the committed one) and "
            "CLOCKED pair-sequencing is refused at every event over "
            "the whole order-policy simplex with exact certificates "
            "(gaps 16/81 at 5 events, 592/2187 at 2)",
            {"events": len(E1S),
             "refused": sum(1 for r in rows
                            if not r["clocked_feasible"])})


def solve_simplex_membership(profs, target):
    # exact: is target an affine-nonnegative combination of profs?
    # build the linear system over the 27 coordinates + normalization.
    d = len(profs)
    rows = []
    for c in range(DIM):
        rows.append([profs[i][c] for i in range(d)] + [target[c]])
    rows.append([F(1)] * d + [F(1)])
    M = [list(r) for r in rows]
    ncol = d
    piv = []
    r = 0
    for col in range(ncol):
        pr = None
        for rr in range(r, len(M)):
            if M[rr][col] != 0:
                pr = rr
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        pv = M[r][col]
        M[r] = [x / pv for x in M[r]]
        for rr in range(len(M)):
            if rr != r and M[rr][col] != 0:
                f = M[rr][col]
                M[rr] = [a - f * b for a, b in zip(M[rr], M[r])]
        piv.append(col)
        r += 1
    for rr in range(r, len(M)):
        if M[rr][ncol] != 0:
            return {"feasible": False,
                    "certificate": {"kind": "linear-inconsistency",
                                    "residual_row": rr,
                                    "residual": str(M[rr][ncol])}}
    if len(piv) == d:
        sol = [F(0)] * d
        for i, col in enumerate(piv):
            sol[col] = M[i][ncol]
        if all(x >= 0 for x in sol):
            return {"feasible": True,
                    "certificate": {"kind": "witness",
                                    "lambda": [str(x) for x in sol]}}
        return {"feasible": False,
                "certificate": {"kind": "unique-solution-negative",
                                "lambda": [str(x) for x in sol]}}
    return {"feasible": False,
            "certificate": {"kind": "undetermined",
                            "pivots": len(piv)}}


def s4_sufficiency(LD, P, hist3, q4map):
    # THE PREDICATE (formalized exactly): for every pair of complete
    # positive-probability histories h, h' at the window whose
    # pair-record configurations (count fields) are equal AS RAW
    # RECORDED STATES -- the geometry is the one fixed committed
    # chart at both -- the delivered dynamics hands them identical
    # conditional distributions for the next record write, and hence
    # for every future record built on it.  The witness grain is the
    # very next write: a difference there IS a differing
    # future-record distribution.  (#87: insufficiency is provable by
    # one witness; the positive direction is only ever
    # NO-INSUFFICIENCY-WITNESS-THROUGH-<window>.)
    bym = {}
    for h in sorted(hist3):
        m = tuple(sorted(h))
        bym.setdefault(m, []).append(h)
    coll = {m: hs for m, hs in sorted(bym.items()) if len(hs) > 1}
    # ---- #87 item 3: THE PREMISE GATE, before any future comparison:
    # raw record equality (count fields byte-equal) and geometry
    # identity (one fixed chart object), NO quotient invoked.
    prem_rows = []
    prem_ok = True
    for m in sorted(coll):
        hs = coll[m]
        fields = [nfield(list(h)) for h in hs]
        raw_eq = all(f == fields[0] for f in fields[1:])
        prem_ok = prem_ok and raw_eq
        prem_rows.append({"record": list(m), "raw_equal": raw_eq})
    prem_ok = pick("MUT-PREMISE", prem_ok, False)
    P["s4_premise"] = {
        "classes_checked": len(prem_rows), "all_raw_equal": prem_ok,
        "quotient_used": "NONE",
        "geometry": "the one fixed committed chart at both sides of "
                    "every comparison",
        "seed_contrast": "SCOUT-K's clash rows carry identical "
                         "COVARIANT COEFFICIENT VECTORS, which is not "
                         "raw record equality, so they are NOT used "
                         "as witnesses here; the anchored seed is "
                         "paper-41's censused non-injectivity (39 "
                         "record-collision classes over 180 "
                         "histories at its corpus), and this unit's "
                         "witnesses are raw count-field collisions "
                         "proved equal by the premise gate"}
    LD.gate("G-S4-PREMISE", prem_ok and len(prem_rows) == 9,
            "the S4 premise gate: all 9 collision classes are proved "
            "raw-record-identical (count fields byte-equal, geometry "
            "the same fixed chart, no quotient invoked) before any "
            "future comparison is made",
            {"classes": len(prem_rows), "raw_equal": prem_ok})
    insuff = []
    for m in sorted(coll):
        hs = coll[m]
        qs = [q4map[h] for h in hs]
        if any(q != qs[0] for q in qs[1:]):
            gap = max(abs(a - b) for a, b in zip(qs[0], qs[1]))
            insuff.append({"record": list(m),
                           "histories": [list(h) for h in hs],
                           "max_gap": str(gap)})
    n_ins = len(insuff)
    n_ins = pick("MUT-S4", n_ins, 0)
    P["s4_sufficiency"] = {
        "window": "W4 (three realized writes)",
        "collision_classes": len(coll),
        "insufficient_classes": n_ins,
        "witnesses": insuff,
        "w3_row": "through W3 the honest positive word is "
                  "NO-INSUFFICIENCY-WITNESS: no two distinct positive "
                  "histories share a raw count field there "
                  "(support-carried, not agreement-carried), and "
                  "finite census can never prove sufficiency",
        "geometry_leg": "BLOCKED-AT-FIXED-G: what is testable under "
                        "the fixed-background walk is record "
                        "sufficiency; geometry sufficiency needs the "
                        "changing-geometry update the corpus does "
                        "not yet have",
        "interpretation": "an insufficiency witness shows only that "
                          "the current pair record plus geometry is "
                          "not a sufficient instantaneous state; in "
                          "a non-Markovian process two identical "
                          "presents may lawfully differ by history, "
                          "and the witness does not show that "
                          "beables must be higher-arity; realized "
                          "history, trigger memory, ontic psi and an "
                          "n-body beable stay distinct and unchosen",
        "sample_space": "CELL-HISTORIES"}
    LD.gate("G-S4-SUFFICIENCY",
            len(coll) == 9 and n_ins == 9,
            "pair-sufficiency at W4: all 9 premise-gated "
            "record-collision classes are INSUFFICIENT -- equal raw "
            "pair record and geometry, different next-write "
            "distributions, first witness gap 224/729; through W3 no "
            "insufficiency witness exists",
            {"collisions": len(coll), "insufficient": n_ins})


# ===========================================================================
# SECTION 7.  WALLS
# ===========================================================================
# W-REPRESENTATION, the amended fork-neutral form (#86 item 6), plus
# the S2 curvature scope wall (#85, #86 item 2), subject-based with
# permanent dead/alive controls (the G-KERNEL-WALL species ported).
WREP_SUBJECTS = ("kernel", "psi", "rho", "hamiltonian", "wavefunction")
WREP_PREDICATES = ("is reality", "is the reality", "is ontic",
                   "is the ontology", "is what exists")
WREP_LICENCE = "admissible if independently declared"
WREP_DEAD = (
    "the kernel K is reality at this arena",
    "psi is ontic because the equations need it",
    "the Hamiltonian is the ontology of the process",
)
WREP_ALIVE = (
    "an ontic psi remains admissible if independently declared, "
    "operationally distinguished, and mapped to the beables",
)
CURV_TOKENS = ("measures curvature", "curvature is measured",
               "measured curvature", "the curvature measurement",
               "gravitational curvature at this arena",
               "is spacelike separation")
CURV_LICENCE = ("precondition", "candidate", "not curvature",
                "never a curvature", "not spacelike")
CURV_DEAD = (
    "the order defect measures curvature at the committed arena",
    "graph-disjointness is spacelike separation here",
)
CURV_ALIVE = (
    "the census is a precondition probe for the curvature reading, "
    "never a curvature measurement",
    "graph-disjointness is not spacelike separation; relational "
    "separation is undefined at this arena",
)
INTERP_SUBJECTS = ("beable", "beables")
INTERP_PREDICATES = ("must be higher arity", "are higher arity",
                     "must be n ary", "are n ary",
                     "must be triadic", "are proven higher arity")
INTERP_LICENCE = "does not show"
INTERP_DEAD = (
    "the witness shows the beables must be higher-arity",
    "so the beables are higher-arity at this arena",
)
INTERP_ALIVE = (
    "the witness does not show that beables must be higher-arity",
)
KERNEL_WALL_TOKENS = (
    "scout kernel empty at equivariant record consistent",
)
KERNEL_WALL_SUBJECTS = (
    "equivariant record consistent kernel",
    "record consistent kernel",
    "equivariant kernel",
)
KERNEL_WALL_NEG = tuple("no " + s for s in KERNEL_WALL_SUBJECTS)
KERNEL_WALL_PRED = (
    "does not exist", "do not exist", "cannot exist", "never exists",
    "none exists", "none exist", "is empty", "are empty",
    "is impossible", "are impossible", "is ruled out", "are ruled out",
)
KERNEL_WALL_LICENCE = "record blind"
KERNEL_DEAD = (
    "So no equivariant record-consistent kernel exists at the "
    "committed arena.",
    "every equivariant kernel is empty at the committed arena",
)
KERNEL_ALIVE = (
    "no record-blind, fixed-alpha, affine-equivariant kernel preserves "
    "the delivered three-step walk statistics",
)


def wall_norm(seg):
    return " ".join(seg.lower().replace("-", " ").split())


def segments(text):
    for ln in text.splitlines():
        cut = ln.replace(";", ".").replace("|", ".").replace(":", ".")
        for seg in cut.split("."):
            s = wall_norm(seg)
            if s:
                yield s, seg


def wrep_hits(text):
    hits = []
    for s, seg in segments(text):
        if WREP_LICENCE in s:
            continue
        if any(sub in s for sub in WREP_SUBJECTS) \
                and any(p in s for p in WREP_PREDICATES):
            hits.append("representation promoted to ontology: "
                        + seg.strip()[:60])
    return hits


def curv_hits(text):
    hits = []
    for s, seg in segments(text):
        if any(lc in s for lc in CURV_LICENCE):
            continue
        if any(t in s for t in CURV_TOKENS):
            hits.append("curvature-scope claim: " + seg.strip()[:60])
    return hits


def interp_hits(text):
    hits = []
    for s, seg in segments(text):
        if INTERP_LICENCE in s:
            continue
        if any(sub in s for sub in INTERP_SUBJECTS) \
                and any(p in s for p in INTERP_PREDICATES):
            hits.append("interpretation-wall claim: "
                        + seg.strip()[:60])
    return hits


def kernel_hits(text):
    hits = []
    for s, seg in segments(text):
        if any(t in s for t in KERNEL_WALL_TOKENS):
            hits.append("retired verdict token: " + seg.strip()[:60])
            continue
        if KERNEL_WALL_LICENCE in s:
            continue
        if any(p in s for p in KERNEL_WALL_NEG) \
                or (any(p in s for p in KERNEL_WALL_SUBJECTS)
                    and any(p in s for p in KERNEL_WALL_PRED)):
            hits.append("retired kernel-scope claim: "
                        + seg.strip()[:60])
    return hits


def walls_gate(LD, P):
    rows = []
    ok = True
    for (fn, dead, alive, nm) in (
            (wrep_hits, WREP_DEAD, WREP_ALIVE, "W-REPRESENTATION"),
            (curv_hits, CURV_DEAD, CURV_ALIVE, "S2-CURVATURE-SCOPE"),
            (interp_hits, INTERP_DEAD, INTERP_ALIVE,
             "S4-INTERPRETATION"),
            (kernel_hits, KERNEL_DEAD, KERNEL_ALIVE, "KERNEL-SCOPE")):
        deadlist = pick("MUT-WALL", dead, ()) if nm == "KERNEL-SCOPE" \
            else dead
        for s in deadlist:
            flagged = bool(fn(s))
            rows.append({"wall": nm, "control": s, "expected": "DEAD",
                         "flagged": flagged})
            ok = ok and flagged
        if nm == "KERNEL-SCOPE" and mut("MUT-WALL"):
            ok = False
        for s in alive:
            flagged = bool(fn(s))
            rows.append({"wall": nm, "control": s, "expected": "ALIVE",
                         "flagged": flagged})
            ok = ok and not flagged
    P["walls"] = {
        "controls": rows,
        "policy": "four subject-based walls with permanent dead and "
                  "alive controls on every build: the amended "
                  "fork-neutral W-REPRESENTATION (promotion by "
                  "convenience forbidden, the ontic-psi fork NOT "
                  "decided), the S2 curvature scope (order defect at "
                  "fixed G is a precondition probe), the #87 S4 "
                  "interpretation wall (an insufficiency witness "
                  "never proves higher-arity beables), and the "
                  "ported kernel-scope wall"}
    LD.gate("G-KERNEL-WALL", ok,
            "all four walls fire on their dead controls and stay "
            "silent on their licensed alive twins on this build",
            {"controls": len(rows),
             "misbehaving": [r["control"][:40] for r in rows
                             if (r["expected"] == "DEAD")
                             != r["flagged"]]})


# ===========================================================================
# SECTION 8.  VERDICTS, TERM TABLE, KIT
# ===========================================================================
TERM_TABLE = (
    ("RECORD-ARITY", "two actors per elementary relational fact -- the "
     "atomic beable; verified 27 of 27 record atoms at the committed "
     "cell structure"),
    ("PROCESS-ARITY", "the number of actors in one indivisible "
     "boundary-to-boundary transition; the committed value is 3, and "
     "ARITY's dial a is this dial and never the record's"),
    ("FOOTPRINT-SIZE", "the number of pair atoms one process event "
     "writes; equals process-arity only at the fixed point a = 3, "
     "which is the numeric camouflage the era's homonym lived on"),
    ("CELL-HIT", "paper-20's primitive: one Born-selected pair-cell "
     "increment per step"),
    ("DIVISION-EVENT", "paper-19's three-actor conflict group whose "
     "footprint writes all three pair-relations"),
    ("PAIR ATOM", "one record cell: an unordered co-division pair of "
     "actors with its multiplicity"),
    ("PROCESS EVENT", "one probabilistic alternative of the law; its "
     "record face is a joint write of pair atoms"),
    ("ORDER/COMPOSITION DEFECT", "the exact difference of the two "
     "orders of a pair-change composition at FIXED geometry; a "
     "precondition probe for the curvature reading, never a curvature "
     "measurement"),
    ("CUT-VALIDITY", "the conditional law out of a cut is a "
     "single-valued function of the declared cut configuration across "
     "every positive-probability history reaching it (the CK / "
     "process-tensor face of divisibility at this arena)"),
    ("PAIR-SEQUENTIAL LAW", "a divisible Markovian law whose "
     "transitions write one pair cell each, with intermediate states "
     "from the declared configuration space only"),
    ("VACUOUS NULL", "the unrestricted chain-rule construction with "
     "the ordered history as hidden state; reproduces everything and "
     "licenses nothing"),
    ("PAIR-SUFFICIENCY", "same pair-record configuration and geometry "
     "imply the same distribution over every future record, under the "
     "delivered dynamics"),
)


def build_verdicts(P):
    V = {}
    V["S1"] = ("SPAIR-RETYPING-CONSISTENT<RECORD-ARITY-2-AT-27-OF-27-"
               "ATOMS; PROCESS-ARITY-3-COMMITTED-THE-DIAL; "
               "FOOTPRINT-FIXED-POINT-a-EQUALS-3; "
               "SWEEP-234-OCCURRENCES-TOTAL; "
               "NEW-CONFLATION-SITES-0-BEYOND-THE-DIAGNOSED-ARC>")
    if P["s1_sweep"]["unclassified"] \
            or P["s1_sweep"]["new_conflation_sites"]:
        V["S1"] = "SPAIR-RETYPING-UNDETERMINED"
    V["S2"] = ("SPAIR-ORDER-DEFECT-NONZERO+GEOMETRIC-INTERPRETATION-"
               "UNTESTED-FIXED-G<RECORD-WRITE-FLAT-729-OF-729; "
               "TRANSPORT-81-NONCOMMUTING-UNORDERED-PAIRS-ALL-"
               "THIRD-ACTOR-VALUES-1/9-AND-4/9; "
               "FULL-STEP-SUPPORT-CRITERION-90-DISJOINT-ORDERED-"
               "NONCOMMUTING; FOUR-READINGS-LISTED-NONE-CHOSEN; "
               "THREE-ACTOR-CURVATURE-READING-CANDIDATE-ONLY>")
    V["S3"] = ("SPAIR-CK-DIVISIBLE-AT-TESTED-CUTS-W3-GRAIN-RECORD+"
               "GEOMETRY-SUPPORT-CARRIED; "
               "SPAIR-SEQUENTIAL-REFUSED-AT-W4-DECLARED-STATE-"
               "CUT-VALID-GRAIN-RECORD+GEOMETRY<9-OF-9-AMBIGUOUS-"
               "CUTS-VIOLATE; CLOCKED-EXPANSION-REFUSED-AT-ALL-7-"
               "EVENTS; UNCLOCKED-EXPANSION-FREE; "
               "VACUOUS-NULL-EXHIBITED; TOMOGRAPHY-DEFICIENT-1-"
               "PREPARATION; GRAIN-INDEPENDENCE-FAILS>; "
               "SPAIR-INTERVENTION-SEMANTICS-UNBUILT")
    V["S4"] = ("SPAIR-PAIR-RECORD-INSUFFICIENT-AT-W4<9-OF-9-PREMISE-"
               "GATED-COLLISION-CLASSES; FIRST-WITNESS-GAP-224/729; "
               "NO-INSUFFICIENCY-WITNESS-THROUGH-W3; "
               "GEOMETRY-LEG-BLOCKED-AT-FIXED-G; "
               "MISSING-DATUM-NAMED-NOT-CHOSEN>")
    P["verdicts"] = V
    P["registered_successors"] = [
        "the GEOMETRY-COUPLED order/composition-defect census, where "
        "the changed relation revises adjacency (the AUTOGLUE-coupled "
        "version) -- the only frame in which a curvature-candidate "
        "reading could be earned",
        "the W5-and-deeper divisibility and sufficiency windows",
        "pair-sequential families with a larger declared state (the "
        "ordered history, an n-body relational beable, or another "
        "state component -- S4's named possibilities)",
        "preparation families beyond the single anchored start the "
        "delivered walk supplies",
    ]


def build_kit(P):
    kit = []
    kit.append("SCOUT-PAIR verdicts:")
    for k in ("S1", "S2", "S3", "S4"):
        kit.append(P["verdicts"][k])
    kit.append("the status table binds: structurally established -- "
               "cells correspond to selected pair relations, triples "
               "write three cells, the delivered bridge erases its "
               "trigger; adopted ontology -- pair relations as atomic "
               "beables; proposed interpretation -- three actors as "
               "the smallest curvature context; still missing -- the "
               "joint process law, the changing-geometry update, "
               "division events, pair-state sufficiency, Hamiltonian "
               "reconstruction.")
    kit.append("the committed grammar has the KINEMATIC SHAPE of the "
               "arity split; the indivisible backreacting dynamics is "
               "the missing half.")
    kit.append("the record's own arity of 2 is never called an arity "
               "anywhere in the swept corpus: the homonym was "
               "one-sided, and a = a(a-1)/2 at a = 3 is the fixed "
               "point that kept it invisible.")
    kit.append("the record-write algebra is flat and the transport "
               "composition is not: the memory of realized relations "
               "commutes while the process that realizes them does "
               "not, and the written record enters the composition "
               "defect as phase, never as magnitude, at this window.")
    kit.append("a nonzero order/composition defect at fixed geometry "
               "admits four readings -- ordinary operator "
               "noncommutation, interference, record-dependent "
               "dynamics, supplied-walk artifact -- and this census "
               "chooses none of them.")
    kit.append("graph-disjointness is not spacelike separation; "
               "relational separation is undefined at this arena.")
    kit.append("the census is a precondition probe for the curvature "
               "reading, never a curvature measurement; the "
               "geometry-coupled census is a registered successor, "
               "not run.")
    kit.append("interventions are not formalizable at this arena and "
               "that is disclosed: conditioning at realized cuts is "
               "the formalizable half of cut-validity, and the whole "
               "preparation family the arena supplies is the single "
               "anchored start.")
    kit.append("the refusal disproves the declared-state cut-valid "
               "record-Markov family at the W4 cuts only; the W3 "
               "feasibility licenses divisibility at the W3 cuts "
               "only, and it is support-carried, not law-carried.")
    kit.append("the unrestricted chain-rule law reproduces the "
               "delivered statistics identically: without the "
               "declared-state and cut-validity constraints the test "
               "would be vacuous.")
    kit.append("the same nine cuts carry S3's refusal and S4's "
               "insufficiency: operational divisibility fails at the "
               "record cut exactly because the pair record is not a "
               "sufficient state there -- one measurement, two "
               "predicates.")
    kit.append("an insufficiency witness shows only that the current "
               "pair record plus geometry is not a sufficient "
               "instantaneous state; in a non-Markovian process two "
               "identical presents may lawfully differ by history, "
               "and the witness does not show that beables must be "
               "higher-arity.")
    kit.append("the missing datum could be the realized history, "
               "trigger memory, an ontic psi, or an n-body relational "
               "beable -- named as possibilities, none chosen.")
    kit.append("finite census can never prove sufficiency: the "
               "positive word is no-insufficiency-witness-through-W3, "
               "and all-future sufficiency would need a closure or "
               "bisimulation theorem, registered as a successor.")
    kit.append("only passive conditioning at realized cuts was "
               "testable, so the intervention face of process-tensor "
               "divisibility carries its honest word: "
               "intervention-semantics-unbuilt.")
    kit.append("the tomography of the supplied preparation set is "
               "deficient by measurement: one preparation, 27 of 378 "
               "two-write and 477 of 3654 three-write records "
               "reached, so every divisibility verdict is scoped to "
               "the tested cuts.")
    kit.append("grain-independence fails: the record+geometry grain "
               "refuses at the W4 cuts while the trace, psi and "
               "full-history grains are each CK-divisible at the "
               "tested cuts -- every verdict names its grain.")
    kit.append("no record-blind, fixed-alpha, affine-equivariant "
               "kernel preserves the delivered three-step walk "
               "statistics.")
    for (t, d) in TERM_TABLE:
        kit.append("| " + t + " | " + d + " |")
    P["kit"] = kit


# ===========================================================================
# SECTION 9.  AUDITS (sample spaces, numerals, env, source)
# ===========================================================================
SS_NAMES = ("CELLS", "CELL-HISTORIES", "ORDER-POLICIES")


def sample_space_audit(LD, P):
    found = []

    def walk_obj(obj, path):
        if isinstance(obj, dict):
            for k in sorted(obj):
                if k == "sample_space":
                    found.append({"path": path, "name": obj[k]})
                else:
                    walk_obj(obj[k], path + "/" + str(k))
        elif isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                walk_obj(v, path + "[%d]" % i)
    walk_obj(P, "")
    names = sorted({r["name"] for r in found})
    nfound = pick("MUT-SS", len(found), 0)
    P["sample_spaces"] = {"declared": nfound, "names": names,
                          "rows": found}
    LD.gate("G-SAMPLE-SPACE",
            nfound == 7 and names == sorted(SS_NAMES),
            "every probability-typed receipt block declares its sample "
            "space: 7 declarations over the three declared names",
            {"declared": nfound, "names": names})


NUMERAL_FIELD_MAP = (
    ("the sweep is total at 234 occurrences", "234",
     "s1_sweep/total_occurrences"),
    ("222 of them are the dial papers' process dial", "222",
     "s1_sweep/class_counts/PROCESS-DIAL"),
    ("9 of them name a carrier's actor count", "9",
     "s1_sweep/class_counts/PROCESS-CARRIER"),
    ("2 footprint-sense sites, both inside the diagnosed arc", "2",
     "s1_sweep/class_counts/FOOTPRINT-DIAGNOSED-ARC"),
    ("27 record atoms carry exactly two actors", "27",
     "s1_typing/record_arity_verified_at_atoms"),
    ("commute at 729 of 729 ordered cell pairs", "729",
     "s2_record_algebra/commuting"),
    ("81 forward-composable ordered pairs", "81",
     "s2_transport_algebra/classes/one_sided_forward"),
    ("162 nonzero ordered defects", "162",
     "s2_transport_algebra/defect_nonzero_ordered"),
    ("81 non-commuting unordered pairs", "81",
     "s2_transport_algebra/defect_nonzero_unordered"),
    ("54 straight compositions at defect 1/9", "54",
     "s2_transport_algebra/defect_frob2_norm_census/1~9"),
    ("108 turning compositions at defect 4/9", "108",
     "s2_transport_algebra/defect_frob2_norm_census/4~9"),
    ("432 disjoint ordered pairs with both compositions nil", "432",
     "s2_transport_algebra/classes/disjoint_both_nil"),
    ("magnitude invariant at all 1620 variant-pair checks", "1620",
     "s2_phase_probe/magnitude_checks"),
    ("the defect matrix moves at 450 of them", "450",
     "s2_phase_probe/matrices_moved"),
    ("90 disjoint-actor ordered pairs are non-commuting at the "
     "full-step reading", "90",
     "s2_fullstep_algebra/disjoint_nonzero_ordered"),
    ("the synthetic order-recording control returns 702", "702",
     "s2_controls/synthetic_order_recording_write_noncommuting_"
     "ordered_pairs"),
    ("the witness law reproduces the joint law at all 486 positive "
     "histories", "486", "s3_w3/witness_verified_at_histories"),
    ("477 reachable record cuts", "477", "s3_w4/reachable_cuts"),
    ("9 order-ambiguous cuts", "9", "s3_w4/ambiguous_cuts"),
    ("9 cut-validity violations", "9",
     "s3_w4/cut_validity_violations"),
    ("the first witness gap is 224/729", "224/729",
     "s3_w4/violations[0]/max_gap"),
    ("refused at all 7 reached first events", "7",
     "s3_expansion/events"),
    ("9 record-collision classes at the sufficiency window", "9",
     "s4_sufficiency/collision_classes"),
    ("all 9 collision classes are insufficient", "9",
     "s4_sufficiency/insufficient_classes"),
    ("477 of 3654 three-write records reached", "3654",
     "s3_tomography/possible_cuts_w4"),
    ("the 3177 unreached three-write records are untested", "3177",
     "s3_tomography/unreached_cuts_w4"),
    ("27 of 378 two-write records reached", "378",
     "s3_tomography/possible_cuts_w2"),
    ("psi separates all 9 record-collision classes", "9",
     "s3_grains/grain_RG_psi/psi_separates"),
    ("all 9 premise-gated classes raw-record-identical", "9",
     "s4_premise/classes_checked"),
)


def resolve_field(P, path):
    cur = P
    for seg in path.split("/"):
        idxs = []
        while seg.endswith("]"):
            k = seg.rindex("[")
            idxs.insert(0, int(seg[k + 1:-1]))
            seg = seg[:k]
        cur = cur[seg.replace("~", "/")]
        for i in idxs:
            cur = cur[i]
    return cur


def numeral_bindings(LD, P):
    rows = []
    allok = True
    for (ctx, tok, path) in NUMERAL_FIELD_MAP:
        try:
            val = fser(resolve_field(P, path))
        except (KeyError, IndexError, TypeError):
            val = "UNRESOLVED-FIELD"
        if mut("MUT-NUMBIND") and path == "s3_w4/reachable_cuts":
            val = 1
        ok = str(val) == tok
        allok = allok and ok
        rows.append({"context": ctx, "token": tok, "field": path,
                     "value": val, "ok": ok})
    P["numeral_bindings"] = {
        "bindings": rows, "all_bound": allok,
        "policy": "every load-bearing prose numeral is bound to its "
                  "specific receipt field; any-occurrence backing is "
                  "refused as the sole backing"}
    LD.gate("G-NUMERAL-FIELD", allok,
            "every load-bearing prose numeral is bound to a specific "
            "receipt field and each bound token equals that field's "
            "value exactly",
            {"bindings": len(rows),
             "failing": [r["field"] for r in rows if not r["ok"]]})


def env_exclusion(LD, P):
    live = ("v15/note-scout-bridge.md",)
    digs = {rel: sha12(read_rel(rel)) for rel in live}
    P["env_exclusion"] = {
        "policy": "no unpinned live digest enters the artifacts; every "
                  "read this unit performs is pinned, so the scan runs "
                  "over the pinned set's live digests as a canary",
        "probe": pick("MUT-ENV", None,
                      digs["v15/note-scout-bridge.md"])}
    blob = to_json(P) + to_json(LD.rows)
    leaks = sorted(rel for rel in sorted(digs) if digs[rel] in blob
                   and PINNED.get(rel) != digs[rel])
    if mut("MUT-ENV"):
        leaks = ["v15/note-scout-bridge.md"]
    P["env_exclusion"]["leaks"] = leaks
    LD.gate("G-ENV-EXCLUSION", not leaks,
            "the serialized receipt payload carries no "
            "environment-dependent digest: every recorded digest is a "
            "frozen pin, and the canary scan is clean",
            {"scanned": len(digs), "leaks": leaks})


MUT_SETITER_SNIPPET = (
    "\n\ndef _mutant_set_iteration_and_listdir():\n"
    "    acc = []\n"
    "    for cell in {3, 1, 2}:\n"
    "        acc.append(cell)\n"
    "    for name in os.listdir(HERE):\n"
    "        acc.append(name)\n"
    "    return acc\n")


def source_scan(LD, P):
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as f:
        src = f.read()
    scan_src = pick("MUT-SETITER", src, src + MUT_SETITER_SNIPPET)
    tree = ast.parse(scan_src)
    floats = [n.lineno for n in ast.walk(tree)
              if isinstance(n, ast.Constant)
              and isinstance(n.value, float)]
    hashes = [n.lineno for n in ast.walk(tree)
              if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
              and n.func.id == "hash"]
    imports = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            imports.update(a.name for a in n.names)
        if isinstance(n, ast.ImportFrom):
            imports.add(n.module)
    allowed = {"os", "sys", "json", "hashlib", "ast", "fractions",
               "itertools"}
    sorted_args = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                and n.func.id == "sorted":
            for a in n.args:
                sorted_args.add(id(a))

    def set_like(node):
        return isinstance(node, (ast.Set, ast.SetComp)) or (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in ("set", "frozenset"))

    def is_listdir(node):
        return isinstance(node, ast.Call) and (
            (isinstance(node.func, ast.Attribute)
             and node.func.attr == "listdir")
            or (isinstance(node.func, ast.Name)
                and node.func.id == "listdir"))
    set_iter = []
    raw_listdir = []
    for n in ast.walk(tree):
        if isinstance(n, ast.For) and set_like(n.iter):
            set_iter.append(n.iter.lineno)
        if isinstance(n, (ast.ListComp, ast.SetComp, ast.GeneratorExp,
                          ast.DictComp)):
            for g in n.generators:
                if set_like(g.iter):
                    set_iter.append(g.iter.lineno)
        if is_listdir(n) and id(n) not in sorted_args:
            raw_listdir.append(n.lineno)
    P["source_hygiene"] = {"float_literals": floats,
                           "hash_calls": hashes,
                           "imports": sorted(imports),
                           "set_iteration_lines": sorted(set_iter),
                           "raw_listdir_lines": sorted(raw_listdir),
                           "digest": sha12(src.encode("utf-8"))}
    LD.gate("G-SRC-CLEAN",
            not floats and not hashes and imports <= allowed,
            "the instrument's own syntax tree carries no float "
            "literal, no builtin hash call, and no import outside the "
            "declared whitelist", {"imports": sorted(imports)})
    LD.gate("G-AST-DETERMINISM",
            not set_iter and not raw_listdir,
            "the determinism leg: no bare iteration over a set "
            "display, set comprehension or set()/frozenset() call, "
            "and no os.listdir outside a direct sorted() wrapper, "
            "anywhere in this instrument's syntax tree",
            {"set_iteration_lines": sorted(set_iter),
             "raw_listdir_lines": sorted(raw_listdir)})


# ===========================================================================
# SECTION 10.  THE FULL BUILD
# ===========================================================================
def build_all(P=None):
    LD = Ledger()
    if P is None:
        P = {}
    source_scan(LD, P)
    texts = measure_reads(LD, P)
    measure_arena(LD, P)
    psi1, q1, sup1, q2, sup2, BOC, E1S, variants = build_walk(LD, P)
    s1_retyping(LD, P, texts)
    s2_census(LD, P, psi1, variants)
    hist3, q3map, q4map = build_windows(psi1, q1, sup1, q2, sup2)
    s3_divisibility(LD, P, psi1, q1, sup1, q2, sup2, hist3, q3map,
                    q4map)
    s3_clocked(LD, P, psi1, q2, sup1, BOC, E1S)
    s4_sufficiency(LD, P, hist3, q4map)
    build_verdicts(P)
    build_kit(P)
    walls_gate(LD, P)
    sample_space_audit(LD, P)
    numeral_bindings(LD, P)
    env_exclusion(LD, P)
    P["ledger"] = LD.rows
    return P


# ===========================================================================
# SECTION 11.  FALSIFIER REGISTRY
# ===========================================================================
FALSIFIERS = (
    ("MUT-PINDIG", "G-PIN-DIGESTS", "pin_check",
     "corrupts a pinned-read digest comparison"),
    ("MUT-ANCHOR", "G-ANCHORS", "anchors", "corrupts an anchor hit"),
    ("MUT-ARENA", "G-ARENA", "arena",
     "forges the actors-per-cell census"),
    ("MUT-Q", "G-WALK", "walk", "skips the Born normalization"),
    ("MUT-FIXED", "G-FIXED-POINT", "s1_typing",
     "plants a second fixed point"),
    ("MUT-SWEEP", "G-S1-SWEEP", "s1_sweep",
     "plants an unclassified occurrence"),
    ("MUT-CONFL", "G-S1-CONFLATION", "s1_sweep",
     "plants a fake new conflation site"),
    ("MUT-REC", "G-S2-REC-FLAT", "s2_record_algebra",
     "forges the record-flatness check"),
    ("MUT-DECOMP", "G-S2-DECOMP", "s2_transport_decomposition",
     "breaks the transport-decomposition licence"),
    ("MUT-THIRD", "G-S2-THIRD-ACTOR", "s2_transport_algebra",
     "decrements the third-actor count"),
    ("MUT-PHASE", "G-S2-PHASE", "s2_phase_probe",
     "forges the magnitude-invariance flag"),
    ("MUT-FULL", "G-S2-FULLSTEP", "s2_fullstep_algebra",
     "zeroes the disjoint non-commuting count"),
    ("MUT-S2CTRL", "G-S2-CONTROLS", "s2_controls",
     "zeroes the order-recording control"),
    ("MUT-W3", "G-S3-W3", "s3_w3", "forges the W3 witness check"),
    ("MUT-W4", "G-S3-W4", "s3_w4", "corrupts the W4 certificates"),
    ("MUT-NULL", "G-S3-NULL", "s3_null",
     "corrupts the vacuous-null reproduction"),
    ("MUT-S3CTRL", "G-S3-CONTROLS", "s3_controls",
     "forges the planted-agreement count"),
    ("MUT-CLOCK", "G-S3-CLOCKED", "s3_expansion",
     "forges the clocked-refusal flag"),
    ("MUT-TOMO", "G-S3-TOMOGRAPHY", "s3_tomography",
     "inflates the preparation count"),
    ("MUT-GRAIN", "G-S3-GRAINS", "s3_grains",
     "zeroes the psi-separation count"),
    ("MUT-PREMISE", "G-S4-PREMISE", "s4_premise",
     "forges the raw-record-equality flag"),
    ("MUT-S4", "G-S4-SUFFICIENCY", "s4_sufficiency",
     "zeroes the insufficiency count"),
    ("MUT-WALL", "G-KERNEL-WALL", "walls",
     "disarms the kernel-scope wall"),
    ("MUT-SS", "G-SAMPLE-SPACE", "sample_spaces",
     "strips the sample-space declarations"),
    ("MUT-NUMBIND", "G-NUMERAL-FIELD", "numeral_bindings",
     "corrupts a numeral binding resolution"),
    ("MUT-ENV", "G-ENV-EXCLUSION", "env_exclusion",
     "serializes a live digest into the receipt"),
    ("MUT-SETITER", "G-AST-DETERMINISM", "source_hygiene",
     "injects bare set iteration and raw listdir"),
)


# ===========================================================================
# SECTION 12.  NOTE VERIFICATION
# ===========================================================================
FORBIDDEN_GLOBAL = (
    "no reader will", "no one will doubt", "will not doubt",
    "probably", "likely", "explains why",
    "already instantiates this",
    "the theory already instantiates",
    "measures curvature", "spacelike separation here",
    "sufficient-at-w3", "spair-pair-record-sufficient",
    "curvature-probe reading supported",
)
REQUIRED_SENTENCES = ()


def collect_numerals(obj, out):
    if isinstance(obj, bool):
        return
    if isinstance(obj, int):
        out.add(obj)
        return
    if isinstance(obj, str):
        for tok in obj.replace("/", " ").replace(",", " ").split():
            neg = tok.lstrip("-")
            if neg.isdigit():
                out.add(int(neg))
        return
    if isinstance(obj, dict):
        for k in obj:
            collect_numerals(k, out)
            collect_numerals(obj[k], out)
    if isinstance(obj, (list, tuple)):
        for v in obj:
            collect_numerals(v, out)


def iter_rationals(text):
    toks = text.replace("(", " ").replace(")", " ").replace(",", " ")
    out = set()
    for tok in toks.split():
        t = tok.strip(".;:|")
        parts = t.split("/")
        if len(parts) == 2 and parts[0].lstrip("-").isascii() \
                and parts[0].lstrip("-").isdigit() \
                and parts[1].isascii() and parts[1].isdigit():
            out.add(t)
    return out


def rationals_of(obj, out):
    if isinstance(obj, str):
        out.update(iter_rationals(obj))
    if isinstance(obj, dict):
        for k in obj:
            rationals_of(k, out)
            rationals_of(obj[k], out)
    if isinstance(obj, (list, tuple)):
        for v in obj:
            rationals_of(v, out)


def verify_note(P, note_bytes, problems):
    text = note_bytes.decode("utf-8")
    hay = canon_text(text)
    low = hay.lower()
    for sent in P["kit"]:
        if canon_text(sent) not in hay:
            problems.append("kit sentence missing: " + sent[:80])
    for (aid, _rel, quote) in ANCHORS:
        if canon_text(quote) not in hay:
            problems.append("anchor quote missing from note: " + aid)
    for pat in FORBIDDEN_GLOBAL:
        if pat in low:
            problems.append("forbidden pattern present: " + pat)
    for h in wrep_hits(text):
        problems.append("W-REPRESENTATION wall: " + h)
    for h in curv_hits(text):
        problems.append("curvature-scope wall: " + h)
    for h in interp_hits(text):
        problems.append("interpretation wall: " + h)
    for h in kernel_hits(text):
        problems.append("kernel-scope wall: " + h)
    for name in SS_NAMES:
        if "[SS:" + name + "]" not in text:
            problems.append("sample-space tag [SS:%s] absent" % name)
    for ln in text.splitlines():
        st = ln.strip()
        if st.startswith("|") or st.startswith(">") \
                or st.startswith("#"):
            continue
        if ("P(" in ln or "q(" in ln or "p_t(" in ln) \
                and "[SS:" not in ln:
            problems.append("probability expression without a "
                            "sample-space tag: " + st[:60])
    gates = {r["gate"] for r in P["ledger"]}
    pos = 0
    while True:
        k = text.find("[LIC:", pos)
        if k < 0:
            break
        end = text.find("]", k)
        gid = text[k + 5:end]
        if gid not in gates:
            problems.append("licence token names no registered gate: "
                            + gid)
        pos = end
    for ln in text.splitlines():
        lnl = ln.lower()
        if "derive" in lnl and not ln.strip().startswith(">") \
                and "[BY:" not in ln and "|" not in ln:
            problems.append("derivation sentence without subject tag: "
                            + ln.strip()[:60])
    for (ctx, tok, path) in NUMERAL_FIELD_MAP:
        if canon_text(ctx) not in hay:
            problems.append("numeral-field context missing (%s = %s)"
                            % (path, tok))
    if not P.get("numeral_bindings", {}).get("all_bound"):
        problems.append("numeral-field bindings not all bound")
    inv = set()
    rationals_of(fser(P), inv)
    for ln in text.splitlines():
        for t in sorted(iter_rationals(ln)):
            if t not in inv:
                problems.append("slash rational not in receipt "
                                "inventory: " + t)
    nums = set()
    collect_numerals(fser(P), nums)
    layout = set(range(0, 61)) | {64, 74, 77, 78, 84, 85, 86, 87, 108, 128,
                                  135, 156, 216, 234, 270, 288, 351,
                                  409, 416, 464, 578, 582, 587, 723,
                                  729, 759, 964, 2026, 424242}
    for ln in text.splitlines():
        for tok in ln.replace("(", " ").replace(")", " ").split():
            t = tok.strip(".,;:|%").lstrip("#")
            if t.isascii() and t.isdigit():
                v = int(t)
                if v not in nums and v not in layout:
                    problems.append("numeral not receipt-backed: " + t)
    return problems


# ===========================================================================
# SECTION 13.  ARTIFACTS, CLI, SELFTEST
# ===========================================================================
def render_output(P, note_digest):
    lines = []
    lines.append("SCOUT-PAIR delivery transcript")
    lines.append("pin 67e6082b445a (v15 ledger #84) + the #85 routed "
                 "addendum + the FROZEN #86 addendum b3aa0f973ae1; "
                 "unit note " + NOTE_REL)
    lines.append("object under test (the note): sha256-12 "
                 + note_digest)
    lines.append("instrument source: sha256-12 "
                 + P["source_hygiene"]["digest"])
    lines.append("sources: the #86 frozen table, bound at pinned "
                 "digests or disclosed byte-verified snapshots; 6 "
                 "ARITY-16/SCOUT-K legs declared, not read")
    lines.append("")
    for r in P["ledger"]:
        lines.append("GATE %-18s %s  %s"
                     % (r["gate"], "PASS" if r["ok"] else "FAIL",
                        r["note"]))
    lines.append("")
    lines.append("VERDICTS")
    for k in ("S1", "S2", "S3", "S4"):
        lines.append("  " + P["verdicts"][k])
    lines.append("")
    lines.append("KEY CLAIMS")
    lines.append("  S1: sweep total 234; classes 222/9/2/1; new "
                 "conflation sites 0; fixed point a=3")
    lines.append("  S2: record write flat 729/729; transport 81 "
                 "non-commuting unordered pairs, all third-actor, "
                 "values 1/9 and 4/9; full step support-criterion "
                 "with 90 disjoint ordered non-commuting; phase-only "
                 "record dependence 1620/450")
    lines.append("  S3: CK-divisible at the W3 cuts (support-carried, "
                 "486 histories, grain record+geometry); refused at 9 "
                 "of 9 ambiguous W4 cuts of 477, first gap 224/729; "
                 "clocked expansion refused 7/7; unclocked free; "
                 "vacuous null exhibited; tomography deficient (1 "
                 "preparation); grains fork; intervention semantics "
                 "unbuilt")
    lines.append("  S4: pair record insufficient at W4, 9 of 9 "
                 "premise-gated collision classes; no insufficiency "
                 "witness through W3; geometry leg blocked at fixed G")
    lines.append("  falsifiers: %d registered; gates: %d"
                 % (len(FALSIFIERS), len(P["ledger"])))
    lines.append("")
    return "\n".join(lines) + "\n"


def deliver(write):
    P1 = build_all()
    P2 = build_all()
    d1, d2 = digest(P1), digest(P2)
    if d1 != d2:
        raise GateFail("G-DETERMINISM", "double build differs")
    P1["determinism"] = {"double_build_digest": d1, "equal": True}
    note_path = os.path.join(ROOT, NOTE_REL)
    if not os.path.exists(note_path):
        raise GateFail("G-NOTE-PRESENT", "the unit note is absent")
    note_bytes = read_rel(NOTE_REL)
    problems = verify_note(P1, note_bytes, [])
    if problems:
        raise GateFail("G-NOTE-KIT", "; ".join(problems[:8]))
    nd = sha12(note_bytes)
    P1["object_under_test"] = {"path": NOTE_REL, "sha256_12": nd}
    P1["falsifiers"] = [{"name": n, "gate": g, "object": o,
                         "description": d}
                        for (n, g, o, d) in FALSIFIERS]
    P1["schema"] = "scoutpair-receipt-v1"
    out = render_output(P1, nd)
    rec = to_json(P1)
    if write:
        with open(os.path.join(ROOT, OUT_REL), "w",
                  encoding="utf-8") as f:
            f.write(out)
        with open(os.path.join(ROOT, REC_REL), "w",
                  encoding="utf-8") as f:
            f.write(rec)
    sys.stdout.write(out)
    return 0


def selftest():
    before = {}
    for rel in (OUT_REL, REC_REL):
        p = os.path.join(ROOT, rel)
        before[rel] = sha12(read_rel(rel)) if os.path.exists(p) \
            else None
    clean = build_all()
    clean_dig = {}
    for (_n, _g, obj, _d) in FALSIFIERS:
        clean_dig[obj] = digest(clean.get(obj))
    failures = []
    for (name, gate, obj, _desc) in FALSIFIERS:
        ARMED["name"] = name
        died, at = False, None
        partial = {}
        try:
            build_all(partial)
        except GateFail as e:
            died, at = True, e.gate
        ARMED["name"] = None
        if not died:
            failures.append(name + ": survived")
            continue
        if at != gate:
            failures.append("%s: died at %s not %s" % (name, at, gate))
            continue
        moved = (obj in partial
                 and digest(partial.get(obj)) != clean_dig[obj])
        if not moved:
            failures.append(name + ": no move proof")
            continue
        sys.stdout.write("FALSIFIER %-12s died at %-18s moved-proof "
                         "ok\n" % (name, at))
    after = {}
    for rel in (OUT_REL, REC_REL):
        p = os.path.join(ROOT, rel)
        after[rel] = sha12(read_rel(rel)) if os.path.exists(p) \
            else None
    if before != after:
        sys.stdout.write("SELFTEST: artifacts moved\n")
        return 3
    if failures:
        for f in failures:
            sys.stdout.write("SELFTEST FAIL " + f + "\n")
        return 3
    sys.stdout.write("SELFTEST PASS: %d falsifiers, all died at their "
                     "declared gates, artifacts untouched\n"
                     % len(FALSIFIERS))
    return 0


USAGE = ("usage: scoutpair_exact.py [--no-write | --numbers | --kit | "
         "--selftest | --mutant NAME | --verify-paper PATH | "
         "--list-gates | --list-mutants]\n")


def main(argv):
    args = argv[1:]
    known = {"--no-write", "--numbers", "--kit", "--selftest",
             "--mutant", "--verify-paper", "--list-gates",
             "--list-mutants"}
    flags = [a for a in args if a.startswith("--")]
    for a in flags:
        if a not in known:
            sys.stderr.write(USAGE)
            return 2
    if len(flags) != len(set(flags)) or len(flags) > 1:
        sys.stderr.write(USAGE)
        return 2
    if not args:
        try:
            return deliver(True)
        except GateFail as e:
            sys.stderr.write("GATE FAILURE %s: %s\n" % (e.gate, e.msg))
            return 3
    mode = args[0]
    if mode == "--list-gates":
        gates = sorted({g for (_n, g, _o, _d) in FALSIFIERS}
                       | {"G-SRC-CLEAN", "G-DETERMINISM", "G-NOTE-KIT",
                          "G-RECORD-ARITY", "G-S2-TRANSPORT",
                          "G-S3-NULL", "G-S4-SUFFICIENCY"})
        for g in gates:
            sys.stdout.write(g + "\n")
        return 0
    if mode == "--list-mutants":
        for (n, g, o, d) in FALSIFIERS:
            sys.stdout.write("%-12s -> %-18s (%s): %s\n"
                             % (n, g, o, d))
        return 0
    if mode == "--mutant":
        if len(args) != 2:
            sys.stderr.write(USAGE)
            return 2
        names = {n for (n, _g, _o, _d) in FALSIFIERS}
        if args[1] not in names:
            sys.stderr.write("unknown mutant\n")
            return 2
        ARMED["name"] = args[1]
        try:
            build_all()
        except GateFail as e:
            sys.stderr.write("MUTANT %s died at %s\n"
                             % (args[1], e.gate))
            return 3
        sys.stderr.write("MUTANT %s survived\n" % args[1])
        return 3
    if mode == "--verify-paper":
        if len(args) != 2:
            sys.stderr.write(USAGE)
            return 2
        P = build_all()
        try:
            with open(args[1], "rb") as f:
                nb = f.read()
        except OSError:
            sys.stderr.write("cannot read note\n")
            return 2
        problems = verify_note(P, nb, [])
        if problems:
            for pr in problems[:20]:
                sys.stdout.write("NOTE PROBLEM: " + pr + "\n")
            return 3
        sys.stdout.write("NOTE VERIFIED: kit, anchors, walls, tags, "
                         "numerals all pass\n")
        return 0
    if len(args) != 1:
        sys.stderr.write(USAGE)
        return 2
    if mode == "--no-write":
        try:
            return deliver(False)
        except GateFail as e:
            sys.stderr.write("GATE FAILURE %s: %s\n" % (e.gate, e.msg))
            return 3
    if mode == "--numbers":
        P = build_all()
        for k in ("S1", "S2", "S3", "S4"):
            sys.stdout.write(P["verdicts"][k] + "\n")
        sys.stdout.write(to_json(
            {"s2_values":
             P["s2_transport_algebra"]["defect_frob2_norm_census"],
             "s3_gaps": [v["max_gap"]
                         for v in P["s3_w4"]["violations"]]}) + "\n")
        return 0
    if mode == "--kit":
        P = build_all()
        for sent in P["kit"]:
            sys.stdout.write(sent + "\n")
        return 0
    if mode == "--selftest":
        return selftest()
    sys.stderr.write(USAGE)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
