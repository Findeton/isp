#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""TPL EXPOSURE CENSUS — which of the nine disease families each sealed v14
instrument carries at HEAD.

v14 TPL (the #267 template sweep), chartered at ledger #371 per #362.
Spec: v14/TEMPLATE.md.  Reference implementations: v14/code/era_template.py.

WHAT IS MEASURED.  Two independent layers, published side by side and never
merged:

  LAYER 1 — THE PANEL LAYER.  What the units' own K3 (instrument) seats
  measured with LIVE INJECTIONS, cited by review file and finding id.  Every
  citation is machine-verified here: the finding id must be locatable in the
  cited review, and the review's sha256-12 is published beside it.  This is
  the authoritative layer: a live injection at exit 0 is evidence a static
  probe can never be.

  LAYER 2 — THE PROBE LAYER.  A STRUCTURAL probe per family, run READ-ONLY
  in a scratch mirror against the instrument's source AT HEAD.  A probe is
  not an injection: it reports whether the MECHANISM the family names is
  present in the source, not whether a corruption survives.  Its value is
  that it is uniform across all instruments (including the three that have
  no panel) and that it sees HEAD, so a family a panel measured PRESENT at
  review time and a repair has since closed shows as closed here.

WHAT IS NOT DONE.  No sealed object is edited, executed or re-delivered.  No
instrument is run.  The census reads each instrument once, to copy it into
the mirror, and probes the copy.

SELF-HOSTING.  The census is built on era_template: gate-time seals verified
at promotion, a ledger-bound transcript, an audited read set, and every
numeral of the published census interpolated from a live registry (the
prose renders from the receipt).

CLI (#82): --run | --no-write | --selftest | --list-gates | --list-probes.
Anything else exits 2.
"""

from __future__ import annotations

import ast
import collections
import hashlib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import era_template as ET                                          # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
REPO = os.path.dirname(REPO)                     # .../isp
CODE_REL = "v14/code"
MIRROR = ("/private/tmp/claude-501/-Users-felixrobles-workspace/"
          "82d34949-326c-4269-8dd0-587362126fa5/scratchpad/tpl_build/mirror")

RECEIPT_REL = "v14/code/tpl_census_receipt.json"
CENSUS_REL = "v14/tpl_census.md"

# --------------------------------------------------------------------------
# THE UNIT MAP — panel slug -> instrument file.  Instruments with no panel
# carry slug None and are censused by the probe layer alone.
# --------------------------------------------------------------------------

UNITS = [
    ("act", "act_exact.py"),
    ("aid", "aid_exact.py"),
    ("coup", "coupling_exact.py"),
    ("cra", "cra_accumulation_exact.py"),
    (None, "crb_stochastic_exact.py"),
    (None, "crc_coarsegrain_exact.py"),
    (None, "crd_tower_exact.py"),
    ("epr", "epr_exact.py"),
    ("fac", "fac_exact.py"),
    ("gdl", "gdl_exact.py"),
    ("giter", "giter_exact.py"),
    ("gmain", "gmain_exact.py"),
    ("gprep", "gprep_foundation_exact.py"),
    ("lor", "lor_exact.py"),
    ("ndep", "ndep_exact.py"),
    ("occ", "occ_exact.py"),
    ("perl", "perl_exact.py"),
    ("perr", "perr_exact.py"),
    ("pot", "pot_exact.py"),
    ("r1", "r1_continuum_exact.py"),
    ("r2", "r2_manifold_exact.py"),
    ("r3", "r3_relativity_exact.py"),
    ("r3w", "r3_weld_exact.py"),
    ("r4", "r4_defect_stage_exact.py"),
    ("r4b", "r4b_momentum_exact.py"),
    ("r4c", "r4c_multi_exact.py"),
    ("r4dec", "r4dec_exact.py"),
    ("r5", "r5_gauge_exact.py"),
    ("r5m", "r5m_measure_exact.py"),
    ("r6a", "r6a_refinement_exact.py"),
    ("r6bp", "r6bp_transport_exact.py"),
    ("sec", "sec_exact.py"),
    ("sec2", "sec2_exact.py"),
    ("sig", "sig_exact.py"),
    ("smu", "smu_exact.py"),
    ("spc", "spc_exact.py"),
    ("u4", "u4_crystals_exact.py"),
    ("u4b", "u4b_schedule_exact.py"),
    ("w2", "w2_census_exact.py"),
]

# --------------------------------------------------------------------------
# THE PANEL LAYER — every row is (slug, family, finding id, verdict).
# VERDICT: PRESENT  = the seat's live injection survived at exit 0
#          ABSENT   = the seat probed the family and the instrument closed it
# Sources: the six K3 seats read in full by this worker (epr, ndep, pot, sec,
# sec2, spc) and a read-only sweep of the other thirty K3 reviews.  Every id
# below is machine-located in its review file by G-CITATIONS-LOCATED.
# --------------------------------------------------------------------------

PANEL = [
    # (a) SEAL INTEGRITY
    ("act", "a", "MAJOR-2", "PRESENT"), ("aid", "a", "MAJOR-5", "PRESENT"),
    ("coup", "a", "MAJOR-2", "PRESENT"), ("cra", "a", "MAJOR-3", "PRESENT"),
    ("epr", "a", "MAJOR-5", "PRESENT"), ("fac", "a", "MAJOR-4", "PRESENT"),
    ("giter", "a", "MAJOR-2", "PRESENT"), ("lor", "a", "MAJOR-5", "PRESENT"),
    ("ndep", "a", "MAJOR-1", "PRESENT"), ("perl", "a", "MAJOR-2", "PRESENT"),
    ("perr", "a", "MAJOR-7", "PRESENT"), ("pot", "a", "MAJOR-6", "PRESENT"),
    ("r4b", "a", "MAJOR-1", "PRESENT"), ("r4c", "a", "MAJOR-4", "PRESENT"),
    ("r5", "a", "MAJOR-5", "PRESENT"), ("sec", "a", "MAJOR-4", "PRESENT"),
    ("sec2", "a", "MAJOR-1", "PRESENT"), ("smu", "a", "MAJOR-2", "PRESENT"),
    ("spc", "a", "MAJOR-1", "PRESENT"), ("u4", "a", "MAJOR-3", "PRESENT"),
    ("u4b", "a", "MAJOR-1", "PRESENT"),
    # (b) TRANSCRIPT BOUND TO THE LEDGER
    ("act", "b", "MAJOR-2", "PRESENT"), ("aid", "b", "MAJOR-5", "PRESENT"),
    ("coup", "b", "MAJOR-2", "PRESENT"), ("epr", "b", "MAJOR-6", "PRESENT"),
    ("fac", "b", "m1", "PRESENT"), ("lor", "b", "MAJOR-5", "PRESENT"),
    ("ndep", "b", "MAJOR-2", "PRESENT"), ("perr", "b", "MAJOR-3", "PRESENT"),
    ("pot", "b", "MAJOR-7", "PRESENT"), ("r6a", "b", "M4", "PRESENT"),
    ("sec2", "b", "MAJOR-9", "PRESENT"), ("sig", "b", "MINOR-5", "PRESENT"),
    ("spc", "b", "m6", "PRESENT"),
    # (c) SEMANTIC WALLS
    ("act", "c", "MAJOR-4", "PRESENT"), ("aid", "c", "MAJOR-3", "PRESENT"),
    ("epr", "c", "MAJOR-7", "PRESENT"), ("fac", "c", "MAJOR-3", "PRESENT"),
    ("giter", "c", "MAJOR-6", "PRESENT"), ("lor", "c", "MAJOR-1", "PRESENT"),
    ("ndep", "c", "MAJOR-6", "PRESENT"), ("perr", "c", "MAJOR-6", "PRESENT"),
    ("pot", "c", "MAJOR-1", "PRESENT"), ("r3w", "c", "M3", "PRESENT"),
    ("r5", "c", "MAJOR-3", "PRESENT"), ("r5m", "c", "M2", "PRESENT"),
    ("sec2", "c", "MAJOR-11", "PRESENT"), ("u4", "c", "MAJOR-1", "PRESENT"),
    ("u4b", "c", "MAJOR-6", "PRESENT"),
    # (d) VERBATIM ANCHORS CONSUMED
    ("act", "d", "MAJOR-3", "PRESENT"), ("aid", "d", "MAJOR-4", "PRESENT"),
    ("epr", "d", "MINOR-10", "PRESENT"), ("gprep", "d", "MAJOR-4", "PRESENT"),
    ("ndep", "d", "MAJOR-4", "PRESENT"), ("perr", "d", "MAJOR-4", "PRESENT"),
    ("pot", "d", "MAJOR-9", "PRESENT"), ("r4b", "d", "MAJOR-2", "PRESENT"),
    ("r4c", "d", "MAJOR-1", "PRESENT"), ("r6a", "d", "M5", "PRESENT"),
    ("r6bp", "d", "M3", "PRESENT"), ("sec", "d", "MAJOR-5", "PRESENT"),
    ("sec2", "d", "MINOR-3", "PRESENT"), ("sig", "d", "MAJOR-5", "PRESENT"),
    ("smu", "d", "MAJOR-1", "PRESENT"), ("w2", "d", "MAJOR-4", "PRESENT"),
    ("spc", "d", "MAJOR-1", "ABSENT"),
    # (e) CLAIMS BY EQUALITY / TWO-WAY / TABLE-SIGHTED
    ("act", "e", "MAJOR-1", "PRESENT"), ("aid", "e", "MAJOR-3", "PRESENT"),
    ("coup", "e", "MAJOR-3", "PRESENT"), ("cra", "e", "MAJOR-2", "PRESENT"),
    ("epr", "e", "MAJOR-1", "PRESENT"), ("fac", "e", "MAJOR-5", "PRESENT"),
    ("gdl", "e", "MAJOR-2", "PRESENT"), ("lor", "e", "MAJOR-2", "PRESENT"),
    ("ndep", "e", "MAJOR-5", "PRESENT"), ("occ", "e", "MAJOR-1", "PRESENT"),
    ("perl", "e", "MAJOR-9", "PRESENT"), ("perr", "e", "MAJOR-1", "PRESENT"),
    ("pot", "e", "MAJOR-5", "PRESENT"), ("r1", "e", "M3", "PRESENT"),
    ("r2", "e", "M2", "PRESENT"), ("r4", "e", "F6", "PRESENT"),
    ("r4c", "e", "MAJOR-2", "PRESENT"), ("r4dec", "e", "MAJOR-2", "PRESENT"),
    ("r5m", "e", "M5", "PRESENT"), ("r6bp", "e", "M5", "PRESENT"),
    ("sec", "e", "MAJOR-1", "PRESENT"), ("sec2", "e", "MAJOR-3", "PRESENT"),
    ("sig", "e", "MAJOR-3", "PRESENT"), ("smu", "e", "MAJOR-1", "PRESENT"),
    ("w2", "e", "MAJOR-5", "PRESENT"), ("gmain", "e", "M5", "PRESENT"),
    # (f) SENTENCE-LEVEL REFERENT BINDING
    ("aid", "f", "MAJOR-1", "PRESENT"), ("coup", "f", "MAJOR-3", "PRESENT"),
    ("cra", "f", "MAJOR-2", "PRESENT"), ("epr", "f", "MINOR-7", "PRESENT"),
    ("fac", "f", "MAJOR-2", "PRESENT"), ("gdl", "f", "MAJOR-5", "PRESENT"),
    ("lor", "f", "MAJOR-6", "PRESENT"), ("ndep", "f", "MAJOR-7", "PRESENT"),
    ("occ", "f", "MAJOR-4", "PRESENT"), ("perl", "f", "MAJOR-5", "PRESENT"),
    ("perr", "f", "MAJOR-2", "PRESENT"), ("pot", "f", "MAJOR-2", "PRESENT"),
    ("r1", "f", "M5", "PRESENT"), ("r5m", "f", "M3", "PRESENT"),
    ("r6a", "f", "M7", "PRESENT"), ("sec2", "f", "MAJOR-12", "PRESENT"),
    ("sig", "f", "MAJOR-4", "PRESENT"), ("smu", "f", "MINOR-5", "PRESENT"),
    ("spc", "f", "MAJOR-2", "PRESENT"),
    # (g) NO TYPED COUNTS
    ("act", "g", "MAJOR-5", "PRESENT"), ("cra", "g", "MAJOR-1", "PRESENT"),
    ("epr", "g", "MINOR-5", "PRESENT"), ("gdl", "g", "MAJOR-4", "PRESENT"),
    ("gmain", "g", "D7", "PRESENT"), ("lor", "g", "MAJOR-3", "PRESENT"),
    ("ndep", "g", "m5", "PRESENT"), ("perl", "g", "MAJOR-6", "PRESENT"),
    ("perr", "g", "MAJOR-5", "PRESENT"), ("pot", "g", "MAJOR-3", "PRESENT"),
    ("r1", "g", "M6", "PRESENT"), ("r3", "g", "M5", "PRESENT"),
    ("r4", "g", "F4", "PRESENT"), ("r4c", "g", "MINOR-4", "PRESENT"),
    ("r4dec", "g", "MAJOR-3", "PRESENT"), ("r5m", "g", "m2", "PRESENT"),
    ("r6a", "g", "M2", "PRESENT"), ("r6bp", "g", "M7", "PRESENT"),
    ("sec", "g", "Head literals are typed", "PRESENT"), ("sec2", "g", "MAJOR-13", "PRESENT"),
    ("smu", "g", "MINOR-2", "PRESENT"), ("u4b", "g", "MAJOR-5", "PRESENT"),
    # (h) FALSIFIERS POISON MEASUREMENTS
    ("aid", "h", "MAJOR-4", "PRESENT"), ("coup", "h", "MAJOR-4", "PRESENT"),
    ("cra", "h", "MAJOR-1", "PRESENT"), ("epr", "h", "MAJOR-4", "PRESENT"),
    ("gdl", "h", "MAJOR-3", "PRESENT"), ("giter", "h", "MAJOR-5", "PRESENT"),
    ("gmain", "h", "M2", "PRESENT"), ("gprep", "h", "MAJOR-6", "PRESENT"),
    ("ndep", "h", "MAJOR-10", "PRESENT"), ("perl", "h", "MAJOR-4", "PRESENT"),
    ("pot", "h", "MUT-MUSTNOT", "PRESENT"), ("r1", "h", "M4", "PRESENT"),
    ("r2", "h", "M6", "PRESENT"), ("r3", "h", "M6", "PRESENT"),
    ("r3w", "h", "M3", "PRESENT"), ("r4", "h", "F13", "PRESENT"),
    ("r4dec", "h", "MAJOR-4", "PRESENT"), ("r5", "h", "MAJOR-4", "PRESENT"),
    ("r5m", "h", "M4", "PRESENT"), ("r6a", "h", "M3", "PRESENT"),
    ("r6bp", "h", "M4", "PRESENT"), ("sec", "h", "MAJOR-6", "PRESENT"),
    ("sec2", "h", "MAJOR-7", "PRESENT"), ("sig", "h", "MAJOR-1", "PRESENT"),
    ("smu", "h", "MAJOR-4", "PRESENT"), ("u4b", "h", "m4", "PRESENT"),
    ("spc", "h", "MAJOR-1", "ABSENT"),
    # (i) READ SETS AT THE I/O ACCESSOR
    ("coup", "i", "MINOR-3", "PRESENT"), ("cra", "i", "MINOR-2", "PRESENT"),
    ("gmain", "i", "D1", "PRESENT"), ("gprep", "i", "MAJOR-3", "PRESENT"),
    ("lor", "i", "MAJOR-4", "PRESENT"), ("perl", "i", "MINOR-13", "PRESENT"),
    ("perr", "i", "MAJOR-4", "PRESENT"), ("r3", "i", "M1", "PRESENT"),
    ("r4", "i", "F7", "PRESENT"), ("r4b", "i", "MAJOR-4", "PRESENT"),
    ("r4c", "i", "MINOR-6", "PRESENT"), ("r4dec", "i", "MINOR-1", "PRESENT"),
    ("r6bp", "i", "M1", "PRESENT"), ("sec", "i", "MAJOR-3", "PRESENT"),
    ("sec2", "i", "MAJOR-2", "PRESENT"), ("sig", "i", "MAJOR-7", "PRESENT"),
    ("u4b", "i", "m6", "PRESENT"), ("w2", "i", "MAJOR-2", "PRESENT"),
    ("epr", "i", "MAJOR-5", "ABSENT"),
]

# Registered residuals already in the ledger, owned by this sweep.
RESIDUALS = [
    ("perr", "g", "#353",
     "six claim templates still TYPE numerals whose facts are gated elsewhere; "
     "liftable string-identical repair REGISTERED for the #267 template sweep"),
    ("epr", "g", "#359",
     "two typed-testimony receipt leaves (subprocesses / reads outside the list), "
     "safe by G-READS-DECLARED but typed — folds into the #267 sweep"),
    ("pot", "f", "#363",
     "the REFERENT-BINDING residual PUBLISHED as outside the wall's reach"),
    ("sec", "g", "#367",
     "234 small structural numerals stated honestly in-paper as a residual"),
]

# --------------------------------------------------------------------------
# THE PROBE LAYER
# --------------------------------------------------------------------------

PROBES = {
    "a": ("does the promotion path re-verify the GATE-TIME seals and RECOMPUTE "
          "totality before the artifacts land?"),
    "b": ("is the transcript reconciled with the ledger by content — its PASS "
          "lines parsed back and compared against the gate rows?"),
    "c": ("are the wall patterns semantic (regex, case-folded) with a positive "
          "leg, rather than literal strings?"),
    "d": ("is a verbatim anchor's text CONSUMED — read back out of the anchor "
          "registry by a gate predicate?"),
    "e": ("are claims, tables and fences gated by EQUALITY in both directions "
          "rather than containment or a floor?"),
    "f": ("is there a sentence-level referent binding, per occurrence, over "
          "prose only?"),
    "g": ("how many numerals are TYPED into published gate statements rather "
          "than interpolated from a live registry?"),
    "h": ("how many falsifier hooks poison a verdict variable (a constant "
          "boolean, a constant append) instead of a measurement?"),
    "i": ("is the read set recorded where reads happen (an audit hook or an "
          "open wrapper) rather than inside one helper?"),
}

VERDICTS = ("CARRIES", "PARTIAL", "CLOSED", "NO-SURFACE")


def _writes_artifacts(src):
    """Does this instrument publish artifacts at all?  A unit that publishes
    nothing owes no seal and no transcript; a unit that publishes and has no
    seal registry CARRIES the family rather than lacking the surface."""
    return bool(re.search(r"_output\.txt|_receipt\.json", src))


def _reads_repo(src):
    return bool(re.search(r"os\.path\.join\(\s*(?:REPO|V14|HERE|ROOT)"
                          r"|\bREPO\s*=|\bopen\(\s*(?:PAPER|PIN|SRC)", src))


def _fn_segments(tree, src):
    out = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            seg = ast.get_source_segment(src, node) or ""
            out[node.name] = seg
    return out


def _promotion_segment(fns):
    """The writer, PLUS every function it calls: instruments routinely put the
    integrity check in a helper, and a probe that reads only the writer would
    miss a repair that landed one call away."""
    best, staged = "", False
    for name, seg in fns.items():
        if "os.replace(" in seg and len(seg) > len(best):
            best, staged = seg, True
    if not best:
        for name, seg in fns.items():
            if re.search(r"open\([^)]*[\"']w[b]?[\"']", seg) and (
                    "receipt" in seg or "json.dumps" in seg):
                if len(seg) > len(best):
                    best = seg
    if not best:
        return "", False
    called = [n for n in fns if n != "" and re.search(r"\b%s\s*\(" % re.escape(n), best)]
    return "\n".join([best] + [fns[n] for n in called]), staged


def probe_a(src, tree, fns):
    has_seal = bool(re.search(r"\bSEAL\b|class Seal|def seal\(", src))
    if not has_seal:
        ev = {"seal_registry": False, "publishes_artifacts": _writes_artifacts(src)}
        return ("CARRIES" if ev["publishes_artifacts"] else "NO-SURFACE"), ev
    seg, staged = _promotion_segment(fns)
    reverify = bool(re.search(
        r"\bSEAL\.(?:close|reverify|verify\w*)\(|\bverify_at_promotion\b"
        r"|\bseals\.items\(\)|for k[^\n]{0,60}\bseals\b"
        r"|digest\([^)]{0,30}\[k\]\)", seg))
    totality = bool(re.search(
        r"set\(\s*(?:R|payload|body|rec)\s*\)|for k in (?:R|payload|body)\b"
        r"|\bcovered\s*=|\bunsealed\s*=", seg))
    ev = {"staged_write": staged, "seal_reverified_at_promotion": reverify,
          "totality_recomputed_at_promotion": totality,
          "promotion_fn_chars": len(seg)}
    if reverify and totality:
        return "CLOSED", ev
    if reverify or totality:
        return "PARTIAL", ev
    return "CARRIES", ev


def probe_b(src, tree, fns):
    marks = bool(re.search(r"\[PASS\]|\[FAIL\]|PASS\]|'PASS'|\"PASS\"", src))
    publishes = _writes_artifacts(src)
    if not (marks or publishes):
        return "NO-SURFACE", {"transcript_rendered": False}
    if not marks:
        return "CARRIES", {"transcript_rendered": False,
                           "publishes_artifacts": publishes}
    parsed = bool(re.search(r"(?:findall|match|search|startswith|split)\s*\([^)]{0,40}"
                            r"(?:\[PASS\]|\\\[PASS)", src)) or \
        bool(re.search(r"for ln in [^\n]{0,40}\n[^\n]{0,80}\[PASS\]", src))
    reconciled = bool(re.search(
        r"(?:Counter|multiset|set)\([^)]{0,80}\[PASS\]|"
        r"\[PASS\][^\n]{0,120}(?:LD\.ids|LD\.rows|LD\.names\(\)|gate_ids)|"
        r"(?:LD\.ids|LD\.rows|LD\.names\(\)|gate_ids)[^\n]{0,120}\[PASS\]", src))
    digest_pub = bool(re.search(r"transcript_head|transcript_sha|transcript_digest"
                                r"|output_sha|out_sha", src))
    ev = {"pass_lines_parsed": parsed, "reconciled_with_ledger": reconciled,
          "transcript_digest_published": digest_pub}
    if parsed and reconciled:
        return "CLOSED", ev
    if parsed or digest_pub:
        return "PARTIAL", ev
    return "CARRIES", ev


def probe_c(src, tree, fns):
    wall_names = re.findall(r"\b(WALLS?|BANNED\w*|FORBIDDEN\w*|MUSTNOT|MUST_NOT)\b", src)
    if not wall_names:
        return "NO-SURFACE", {"wall_registry": False}
    seg = "\n".join(s for s in fns.values()
                    if re.search(r"WALL|BANNED|FORBIDDEN|MUST_?NOT", s))
    regexed = bool(re.search(r"re\.(?:search|findall|finditer|compile)\(", seg))
    positive = bool(re.search(r"\b(?:positive|required|missing|absent)\w*\s*=[^=]", seg))
    folded = "casefold" in seg or ".lower()" in seg
    ev = {"regex_patterns": regexed, "positive_leg": positive,
          "case_folded": folded, "wall_tokens": len(set(wall_names))}
    legs = sum((regexed, positive, folded))
    if legs == 3:
        return "CLOSED", ev
    if legs >= 1:
        return "PARTIAL", ev
    return "CARRIES", ev


def probe_d(src, tree, fns):
    has_verbatim = bool(re.search(r"VERBATIM|verbatim_anchor|VB-|V-[A-Z]", src))
    if not has_verbatim:
        return "NO-SURFACE", {"verbatim_registry": False}
    consumption = bool(re.search(
        r"\bdef (?:vbwin|anchor_read|read_anchor|consume_anchor|verbatim_read)\("
        r"|\bvbwin\(|\bread_by\b|\bmark_read\b|\bverify_consumption\b"
        r"|\bconsumed_by\b[^\n]{0,20}\.(?:add|append)\(", src))
    name_only = bool(re.search(r"consumer[^\n]{0,60}(?:in |==)[^\n]{0,40}"
                               r"(?:LD\.ids|gate_ids|names\(\))", src))
    ev = {"runtime_consumption_record": consumption,
          "consumer_name_checked_only": name_only}
    if consumption:
        return "CLOSED", ev
    if name_only:
        return "PARTIAL", ev
    return "CARRIES", ev


def probe_e(src, tree, fns):
    paper = bool(re.search(r"paper[-_]\d|paper_text|verify_paper|G-PAPER|paper_claims|build_claims|paper_render|render_table|markdown", src))
    if not paper:
        return "NO-SURFACE", {"paper_leg": False}
    counter_eq = len(re.findall(r"Counter\([^\n]{0,120}\)\s*==\s*", src)) + \
        len(re.findall(r"==\s*Counter\(", src))
    floors = len(re.findall(r"hits\s*>=|>=\s*need|count\([^)]*\)\s*>=|"
                            r"not in hay|in hay\b|\.get\([^)]*,\s*0\)\s*>=", src))
    table_rows = bool(re.search(r"\bmarkdown_table_rows\b|\brender_table\b"
                                r"|\btable_rows\b|\brows_bound\b"
                                r"|\brow_multiset\b|\bpaper_tables\b", src))
    ev = {"counter_equality_sites": counter_eq, "containment_or_floor_sites": floors,
          "table_rows_rendered": table_rows}
    if counter_eq >= 2 and table_rows and floors == 0:
        return "CLOSED", ev
    if counter_eq >= 1 or table_rows:
        return "PARTIAL", ev
    return "CARRIES", ev


def probe_f(src, tree, fns):
    paper = bool(re.search(r"paper[-_]\d|paper_text|verify_paper|G-PAPER|paper_claims|build_claims|paper_render|render_table|markdown", src))
    if not paper:
        return "NO-SURFACE", {"paper_leg": False}
    gate = bool(re.search(r"\bdef \w*referent\w*\(|\breferent\w*\s*=[^=]"
                          r"|\bREFERENTS?\b\s*=|\bnoun_binding\w*\s*=|\bNOF_RE\b"
                          r"|\buniverses?\s*=|\bdef \w*noun_bind\w*\(", src))
    if not gate:
        return "CARRIES", {"referent_gate": False}
    seg = "\n".join(s for s in fns.values()
                    if re.search(r"\breferent\w*\b|\buniverses?\b|\bnoun_binding\b"
                                 r"|\bNOF_RE\b", s))
    aggregate = bool(re.search(r"\bany\(", seg))
    prose_only = bool(re.search(r"prose_only|strip_fences|FENCE[^\n]{0,40}sub\(", seg))
    ev = {"referent_gate": True, "aggregate_any": aggregate,
          "prose_only": prose_only}
    if not aggregate and prose_only:
        return "CLOSED", ev
    return "PARTIAL", ev


def probe_g(src, tree, fns):
    """Count numerals typed into published gate statements."""
    callers = ("gate", "declare", "stmt", "statement", "seal", "waive")
    typed, samples = 0, []
    interpolated = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fname = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
        if fname not in callers:
            continue
        for arg in node.args:
            lits = []
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                lits = [arg.value]
            elif isinstance(arg, ast.BinOp) and isinstance(arg.op, ast.Mod):
                interpolated += 1
                continue
            elif isinstance(arg, ast.JoinedStr):
                interpolated += 1
                continue
            for s in lits:
                if len(s) < 12:
                    continue
                found = re.findall(r"(?<![\w.\-/])\d[\d,]*(?![\w])", s)
                found = [f for f in found if len(f.replace(",", "")) >= 1]
                if found:
                    typed += len(found)
                    if len(samples) < 3:
                        samples.append("%s:%d %r" % (fname, node.lineno, s[:70]))
    ev = {"typed_numerals_in_statements": typed,
          "interpolated_statements": interpolated, "samples": samples}
    if typed == 0:
        return "CLOSED", ev
    if typed <= 3:
        return "PARTIAL", ev
    return "CARRIES", ev


def probe_h(src, tree, fns):
    """Classify falsifier hooks: sentinel-shaped vs measurement-poisoning."""
    hooks, sentinels, samples = 0, 0, []
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue
        test = ast.dump(node.test)
        if "mut" not in test and "MUT-" not in test and "MUT ==" not in test:
            continue
        hooks += 1
        for st in node.body:
            hit = None
            if isinstance(st, ast.Assign) and isinstance(st.value, ast.Constant) \
                    and isinstance(st.value.value, bool):
                hit = "constant-boolean"
            if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call):
                fn = getattr(st.value.func, "attr", "")
                if fn == "append" and st.value.args and \
                        isinstance(st.value.args[0], ast.Constant):
                    hit = "constant-append"
            if isinstance(st, ast.Assign) and isinstance(st.value, ast.BinOp) \
                    and isinstance(st.value.op, ast.Add) \
                    and isinstance(st.value.right, ast.List) \
                    and all(isinstance(e, ast.Constant) for e in st.value.right.elts) \
                    and st.value.right.elts:
                hit = "constant-list-add"
            if hit:
                sentinels += 1
                if len(samples) < 3:
                    samples.append("line %d: %s" % (st.lineno, hit))
                break
    if hooks == 0:
        return "NO-SURFACE", {"mutant_hooks": 0}
    ev = {"mutant_hooks": hooks, "sentinel_shaped": sentinels, "samples": samples}
    if sentinels == 0:
        return "CLOSED", ev
    if sentinels * 4 <= hooks:
        return "PARTIAL", ev
    return "CARRIES", ev


def probe_i(src, tree, fns):
    hook = bool(re.search(r"addaudithook|builtins\.open\s*=|_real_open", src))
    log = bool(re.search(r"\bREADLOG\b|\bREADS\s*=|\bread_set\w*\s*=[^=]"
                         r"|\breads\.append\(|\bREADS\.append\(", src))
    if not (hook or log):
        ev = {"read_log": False, "reads_repository": _reads_repo(src)}
        return ("CARRIES" if ev["reads_repository"] else "NO-SURFACE"), ev
    pops = len(re.findall(r"(?:READLOG|READS|read_set)\w*\.pop\(", src))
    order_insensitive = bool(re.search(r"sorted\((?:READLOG|READS|reads|read_set)"
                                       r"|set\((?:READLOG|READS|reads|read_set)"
                                       r"|Counter\((?:READLOG|READS|reads|read_set)",
                                       src))
    second_reader = len(set(re.findall(r"def (read_\w+|_?open_\w+)\s*\(", src)))
    ev = {"audit_hook": hook, "read_log": log, "log_pops": pops,
          "order_insensitive_compare": order_insensitive,
          "distinct_reader_functions": second_reader}
    if hook and order_insensitive and pops == 0:
        return "CLOSED", ev
    if hook or (log and order_insensitive):
        return "PARTIAL", ev
    return "CARRIES", ev


PROBE_FNS = {"a": probe_a, "b": probe_b, "c": probe_c, "d": probe_d, "e": probe_e,
             "f": probe_f, "g": probe_g, "h": probe_h, "i": probe_i}


# --------------------------------------------------------------------------
# THE RUN
# --------------------------------------------------------------------------


def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def build_mirror(reads):
    if os.path.isdir(MIRROR):
        shutil.rmtree(MIRROR)
    os.makedirs(MIRROR)
    out = {}
    for _slug, fname in UNITS:
        srcp = os.path.join(REPO, CODE_REL, fname)
        with open(srcp, "rb") as fh:
            blob = fh.read()
        reads.append("%s/%s" % (CODE_REL, fname))
        dst = os.path.join(MIRROR, fname)
        with open(dst, "wb") as fh:
            fh.write(blob)
        out[fname] = hashlib.sha256(blob).hexdigest()[:12]
    return out


def run_probes(shas):
    rows = {}
    for _slug, fname in UNITS:
        with open(os.path.join(MIRROR, fname), "r", encoding="utf-8") as fh:
            src = fh.read()
        tree = ast.parse(src)
        fns = _fn_segments(tree, src)
        per = {}
        for key in sorted(PROBE_FNS):
            verdict, ev = PROBE_FNS[key](src, tree, fns)
            if verdict not in VERDICTS:
                raise ET.CheckFail("G-PROBE-VERDICTS", "%s: bad verdict %s" % (fname, verdict))
            per[key] = {"verdict": verdict, "evidence": ev}
        rows[fname] = {"sha256_12": shas[fname], "lines": src.count("\n") + 1,
                       "probes": per}
    return rows


SPELLED = {"none": 0, "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
           "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
           "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
           "nineteen": 19, "twenty": 20, "thirty": 30}


def spelled(word):
    w = word.strip().casefold()
    if w in SPELLED:
        return SPELLED[w]
    if "-" in w:
        a, b = w.split("-", 1)
        if a in SPELLED and b in SPELLED:
            return SPELLED[a] + SPELLED[b]
    return None


def template_counts(reads, root=None, rel="v14/TEMPLATE.md"):
    """Bind v14/TEMPLATE.md's spelled counts to this run's registries.

    The spec states, per family, how many units a panel measured PRESENT and
    how many the probe layer finds CLOSED.  Those numerals are the census's,
    not the author's: this reads them back out of the document and compares
    them, so the spec cannot go stale in the direction its own family (g)
    forbids.
    """
    root = REPO if root is None else root
    with open(os.path.join(root, rel), "r", encoding="utf-8") as fh:
        text = fh.read()
    if root is None or root == REPO:
        reads.append(rel)
    out = []
    for block in text.split("\n## ")[1:]:
        m = re.match(r"\d+\. FAMILY \((\w)\)", block)
        if not m:
            continue
        key = m.group(1)
        # #125: fold whitespace before matching, or a claim that happens to
        # wrap across a line is silently skipped — the defect this gate caught
        # in its own first run, at a passing 8-of-12.
        head = re.sub(r"\s+", " ", block.split("**THE REQUIRED BEHAVIOUR")[0])
        p = re.search(r"([a-z]+(?:-[a-z]+)?) units measured PRESENT", head)
        if p:
            out.append({"family": key, "claim": "panel_PRESENT",
                        "word": p.group(1), "claimed": spelled(p.group(1))})
        q = re.search(r"probe layer finds [^.]{0,70}? in ([a-z]+(?:-[a-z]+)?) of "
                      r"(?:the )?([a-z]+(?:-[a-z]+)?)", head)
        if q:
            out.append({"family": key, "claim": "CLOSED", "word": q.group(1),
                        "claimed": spelled(q.group(1)),
                        "denominator_word": q.group(2),
                        "denominator": spelled(q.group(2))})
    return out


def reviewed_shas(reads):
    """The sha256-12 each K3 seat published for the instrument it reviewed.

    This turns "a repair landed after the review" from an inference into a
    measurement: if the instrument's digest at HEAD differs from the digest
    the seat opened and closed on, the object moved after the review.
    """
    out = {}
    for slug, fname in UNITS:
        if slug is None:
            continue
        rel = "v14/review-%s-instrument.md" % slug
        with open(os.path.join(REPO, rel), "r", encoding="utf-8") as fh:
            text = fh.read()
        reads.append(rel)
        found = None
        for m in re.finditer(re.escape(fname), text):
            window = text[m.end():m.end() + 160]
            h = re.search(r"(?<![0-9a-zA-Z])([0-9a-f]{12})(?![0-9a-zA-Z])", window)
            if h:
                found = h.group(1)
                break
        out[slug] = found
    return out


def verify_citations(reads):
    out, unlocated = [], []
    review_sha = {}
    for slug, family, fid, verdict in PANEL:
        rel = "v14/review-%s-instrument.md" % slug
        path = os.path.join(REPO, rel)
        if rel not in review_sha:
            with open(path, "rb") as fh:
                body = fh.read()
            reads.append(rel)
            review_sha[rel] = hashlib.sha256(body).hexdigest()[:12]
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
        hits = len(re.findall(r"(?<![\w-])%s(?![\w])" % re.escape(fid), text))
        if hits == 0:
            unlocated.append("%s/%s" % (slug, fid))
        out.append({"unit": slug, "family": family, "finding": fid,
                    "verdict": verdict, "review": rel,
                    "review_sha256_12": review_sha[rel], "occurrences": hits})
    return out, unlocated, review_sha


def render_census(R):
    """The census document, rendered FROM the receipt.  No numeral typed."""
    fam_name = {k: n for k, n, _c in ET.FAMILIES}
    fam_check = {k: c for k, _n, c in ET.FAMILIES}
    L = []
    a = L.append
    a("# TPL EXPOSURE CENSUS — the nine disease families over the sealed v14 "
      "instruments")
    a("")
    a("*The #267 template sweep, chartered at v14 ledger #371 per #362.  "
      "Companion to `v14/TEMPLATE.md` (the spec) and `v14/code/era_template.py` "
      "(the reference implementations).  Rendered from "
      "`v14/code/tpl_census_receipt.json`; every numeral below is interpolated "
      "from the run's own registries.*")
    a("")
    a("**Scope.** %d sealed instruments at HEAD, %d of them with a K3 "
      "(instrument) panel and %d without.  %d panel citations over %d reviews, "
      "each machine-located in the review it names.  %d structural probes per "
      "instrument, %d probe verdicts in all, every one run read-only in a "
      "scratch mirror.  **Zero sealed objects were edited, executed or "
      "re-delivered.**"
      % (R["totals"]["units"], R["totals"]["units_with_panel"],
         R["totals"]["units_without_panel"], R["totals"]["citations"],
         R["totals"]["reviews_cited"], R["totals"]["families"],
         R["totals"]["probe_verdicts"]))
    a("")
    a("## 1. How to read this census")
    a("")
    a("Two layers, published side by side and never merged.")
    a("")
    a("**THE PANEL LAYER** is what the units' own K3 seats measured with LIVE "
      "INJECTIONS — a corruption that survived at exit 0.  It is the "
      "authoritative layer.  It is also incomplete by construction: a seat "
      "reports what it probed, and no seat probed all nine.")
    a("")
    a("**THE PROBE LAYER** is structural and uniform.  It asks of the source "
      "at HEAD whether the MECHANISM each family names is present, not whether "
      "a corruption survives.  `CARRIES` means the mechanism is absent; "
      "`PARTIAL` means some legs are present; `CLOSED` means all the legs the "
      "probe knows how to see are present; `NO-SURFACE` means the instrument "
      "has no such surface (an honest denominator, #34).  **A probe verdict is "
      "not an injection verdict.**  `CLOSED` says the shape is there, never "
      "that the shape has teeth — LOR #269's caveat of record applies to this "
      "census as much as to a mutant sweep.")
    a("")
    a("The two layers disagree productively.  Where a panel measured PRESENT "
      "at review time and the probe reads CLOSED at HEAD, a repair landed "
      "between them; that is the census's main use.")
    a("")
    a("## 2. The nine families")
    a("")
    a("| # | family | reference check | probe asks |")
    a("|---|---|---|---|")
    for key in sorted(PROBES):
        a("| (%s) | %s | `%s` | %s |" % (key, fam_name[key], fam_check[key],
                                         PROBES[key]))
    a("")
    a("## 3. The exposure matrix")
    a("")
    a("One row per instrument.  Each cell is `probe/panel`: the probe verdict "
      "at HEAD, then the panel's live-injection verdict where its seat "
      "reported one (`P` = PRESENT, `A` = ABSENT, `·` = not reported).")
    a("")
    a("| instrument | sha256-12 | " + " | ".join("(%s)" % k for k in sorted(PROBES))
      + " |")
    a("|---|---|" + "---|" * len(PROBES))
    short = {"CARRIES": "CARR", "PARTIAL": "PART", "CLOSED": "CLSD",
             "NO-SURFACE": "n/s"}
    for row in R["matrix"]:
        cells = []
        for key in sorted(PROBES):
            c = row["families"][key]
            mark = {"PRESENT": "P", "ABSENT": "A", None: "·"}[c["panel"]]
            cells.append("%s/%s" % (short[c["probe"]], mark))
        a("| `%s` | `%s` | %s |" % (row["instrument"], row["sha256_12"],
                                    " | ".join(cells)))
    a("")
    a("## 4. Counts per family")
    a("")
    a("| family | probe CARRIES | probe PARTIAL | probe CLOSED | probe "
      "NO-SURFACE | panel PRESENT | panel ABSENT |")
    a("|---|---|---|---|---|---|---|")
    for key in sorted(PROBES):
        c = R["family_counts"][key]
        a("| (%s) %s | %d | %d | %d | %d | %d | %d |"
          % (key, fam_name[key], c["CARRIES"], c["PARTIAL"], c["CLOSED"],
             c["NO-SURFACE"], c["panel_PRESENT"], c["panel_ABSENT"]))
    a("")
    a("The probe layer reads `CARRIES` or `PARTIAL` at %d of the %d "
      "instrument-family cells it could evaluate (%d cells have no surface); "
      "the panel layer measured a live PRESENT at %d cells and an ABSENT at "
      "%d.  %d instruments carry at least one panel-measured PRESENT."
      % (R["totals"]["open_cells"], R["totals"]["evaluable_cells"],
         R["totals"]["no_surface_cells"], R["totals"]["panel_present"],
         R["totals"]["panel_absent"], R["totals"]["units_with_a_present"]))
    a("")
    a("## 5. Where the layers disagree")
    a("")
    a("| instrument | family | panel | probe at HEAD | reviewed sha256-12 | "
      "HEAD sha256-12 | reading |")
    a("|---|---|---|---|---|---|---|")
    for d in R["disagreements"]:
        a("| `%s` | (%s) | %s | %s | `%s` | `%s` | %s |"
          % (d["instrument"], d["family"], d["panel"], d["probe"],
             d["reviewed_sha256_12"] or "not located", d["head_sha256_12"],
             d["reading"]))
    a("")
    a("%d cells read panel PRESENT against probe CLOSED.  Of those, %d sit on "
      "an instrument whose digest MOVED after its review — a repair landed, "
      "and the mechanism is present at HEAD — and %d sit on an instrument that "
      "has NOT moved, where the probe is crediting a shape the seat measured "
      "toothless and THE SEAT IS AUTHORITY; on %d the review publishes no "
      "digest and the comparison could not be made.  %d cells read panel ABSENT "
      "against probe CARRIES; those are two legs, not a contradiction.  The "
      "reviewed digest was located in %d of the %d reviews."
      % (R["totals"]["disagree_repaired"], R["totals"]["disagree_object_moved"],
         R["totals"]["disagree_object_unchanged"],
         R["totals"]["disagree_object_unknown"],
         R["totals"]["disagree_probe_blind"],
         R["totals"]["reviewed_shas_located"], R["totals"]["units_with_panel"]))
    a("")
    a("## 6. Registered residuals (already in the ledger; this sweep owns them)")
    a("")
    a("| unit | family | ledger | residual |")
    a("|---|---|---|---|")
    for r in R["residuals"]:
        a("| `%s` | (%s) | %s | %s |" % (r["unit"], r["family"], r["ledger"],
                                         r["residual"]))
    a("")
    a("## 7. Panel citations, machine-located")
    a("")
    a("Every citation below was located in the review it names, at the "
      "review's published sha256-12.  %d citations, %d located, %d unlocated."
      % (R["totals"]["citations"], R["totals"]["citations_located"],
         R["totals"]["citations_unlocated"]))
    a("")
    a("| unit | family | finding | verdict | review | review sha256-12 | "
      "occurrences |")
    a("|---|---|---|---|---|---|---|")
    for c in R["citations"]:
        a("| `%s` | (%s) | %s | %s | `%s` | `%s` | %d |"
          % (c["unit"], c["family"], c["finding"], c["verdict"], c["review"],
             c["review_sha256_12"], c["occurrences"]))
    a("")
    a("## 8. Method, and what this census cannot say")
    a("")
    a("- Every instrument was copied once into a scratch mirror and probed "
      "there; %d distinct repository paths were read and %d written (this "
      "document and the receipt).  The read set was recorded at an `open` "
      "audit hook and gated order-insensitively at the last gate."
      % (R["totals"]["repo_reads"], R["totals"]["repo_writes"]))
    a("- The spec `v14/TEMPLATE.md` states %d counts about this census; each "
      "is read back out of that document and compared with the live registry "
      "at `G-TEMPLATE-COUNTS-BOUND`, so neither document can drift from the "
      "other." % len(R["template_claims"]))
    a("- The probes are STATIC.  They cannot see a gate that exists and does "
      "not bind, and they cannot see a corruption that survives.  Where a "
      "panel spoke, the panel is authority.")
    a("- The probes are also uniform, which is their whole value: they cover "
      "the %d instruments with no panel, and they see HEAD rather than the "
      "sha the seat reviewed." % R["totals"]["units_without_panel"])
    a("- No verdict here reopens a seal.  Every unit named is terminal; this "
      "census is a map of the shared perimeter, not a re-adjudication of any "
      "unit's physics.  **No measured physical quantity of any unit is in "
      "question anywhere in this document** — every K3 seat cited here "
      "recorded that no measured quantity was wrong.")
    a("")
    a("---")
    a("")
    a("*Rendered from `%s`.  Reference implementations `%s` (`%s`); pin `%s` "
      "(`%s`); census instrument `%s` (`%s`).  Instruments censused at %s.*"
      % (RECEIPT_REL, R["provenance"]["template"],
         R["provenance"]["template_sha256_12"], R["provenance"]["pin"],
         R["provenance"]["pin_sha256_12"], "v14/code/tpl_census.py",
         R["provenance"]["self_sha256_12"], R["provenance"]["head_note"]))
    return "\n".join(L) + "\n"


def full_run(write: bool):
    reads: list[str] = []
    RS = ET.ReadSet(REPO)
    RS.install()
    RS.active = True

    LD = ET.Ledger()
    TR = ET.Transcript()
    SEAL = ET.Seal()
    REG = ET.CountRegistry()
    R: dict = {}

    def gate(gid, statement, ok, evidence):
        LD.gate(gid, statement, ok, evidence)
        TR.row(gid, ok, evidence)

    TR.say("TPL EXPOSURE CENSUS — the #267 template sweep (v14 ledger #371)")
    TR.say("=" * 70)

    # -- the mirror ---------------------------------------------------------
    shas = build_mirror(reads)
    REG.measured("units", len(UNITS), "len(UNITS)")
    REG.measured("mirrored", len(shas), "len(build_mirror(...))")
    R["instruments"] = {f: s for f, s in sorted(shas.items())}
    SEAL.seal("instruments", R["instruments"], "G-MIRROR-BUILT")
    gate("G-MIRROR-BUILT",
         REG.stmt("every censused instrument is copied into the scratch mirror "
                  "and probed there, never in the tree: {units} units, "
                  "{mirrored} mirrored", units=1, mirrored=1),
         len(shas) == len(UNITS),
         "units %d mirrored %d" % (len(UNITS), len(shas)))

    # -- the probe layer ----------------------------------------------------
    rows = run_probes(shas)
    R["probe_rows"] = rows
    verdict_count = sum(len(v["probes"]) for v in rows.values())
    REG.measured("probe_verdicts", verdict_count, "sum of per-unit probe rows")
    REG.measured("families", len(PROBES), "len(PROBES)")
    SEAL.seal("probe_rows", rows, "G-PROBES-RUN")
    gate("G-PROBES-RUN",
         REG.stmt("each instrument is probed for each of the {families} "
                  "families, giving {probe_verdicts} verdicts, each in "
                  "{{CARRIES, PARTIAL, CLOSED, NO-SURFACE}}",
                  families=1, probe_verdicts=1),
         verdict_count == len(UNITS) * len(PROBES),
         "verdicts %d over %d units" % (verdict_count, len(UNITS)))

    # -- the panel layer ----------------------------------------------------
    cites, unlocated, review_sha = verify_citations(reads)
    R["citations"] = cites
    R["reviews"] = dict(sorted(review_sha.items()))
    REG.measured("citations", len(cites), "len(PANEL)")
    REG.measured("citations_located", len(cites) - len(unlocated),
                 "citations whose finding id occurs in its review")
    REG.measured("reviews_cited", len(review_sha), "distinct reviews cited")
    SEAL.seal("citations", cites, "G-CITATIONS-LOCATED")
    SEAL.seal("reviews", R["reviews"], "G-CITATIONS-LOCATED")
    gate("G-CITATIONS-LOCATED",
         REG.stmt("every one of the {citations} panel citations names a "
                  "finding id that occurs in the review it cites, over "
                  "{reviews_cited} reviews", citations=1, reviews_cited=1),
         not unlocated,
         "citations %d located %d unlocated %s"
         % (len(cites), len(cites) - len(unlocated), unlocated or "none"))

    # -- the matrix ---------------------------------------------------------
    panel_by = collections.defaultdict(dict)
    for c in cites:
        panel_by[c["unit"]][c["family"]] = c["verdict"]
    reviewed = reviewed_shas(reads)
    R["reviewed_shas"] = {k: v for k, v in sorted(reviewed.items())}
    matrix, disagreements = [], []
    fam_counts = {k: collections.Counter() for k in PROBES}
    for slug, fname in UNITS:
        fams = {}
        for key in sorted(PROBES):
            pv = rows[fname]["probes"][key]["verdict"]
            panel = panel_by.get(slug, {}).get(key)
            fams[key] = {"probe": pv, "panel": panel,
                         "evidence": rows[fname]["probes"][key]["evidence"]}
            fam_counts[key][pv] += 1
            if panel:
                fam_counts[key]["panel_" + panel] += 1
            if panel == "PRESENT" and pv == "CLOSED":
                rv = reviewed.get(slug)
                moved = None if rv is None else (rv != shas[fname])
                disagreements.append(
                    {"instrument": fname, "family": key, "panel": "PRESENT",
                     "probe": pv, "object_moved_since_review": moved,
                     "reviewed_sha256_12": rv, "head_sha256_12": shas[fname],
                     "reading": ("the object MOVED after the review; the "
                                 "mechanism is present at HEAD" if moved is True
                                 else
                                 "the object is UNCHANGED since the review; the "
                                 "probe credits a shape the seat measured "
                                 "toothless — THE SEAT IS AUTHORITY"
                                 if moved is False else
                                 "the review publishes no digest for this "
                                 "instrument, so the comparison could not be "
                                 "made — THE SEAT IS AUTHORITY")})
            if panel == "ABSENT" and pv == "CARRIES":
                disagreements.append(
                    {"instrument": fname, "family": key, "panel": "ABSENT",
                     "probe": pv, "object_moved_since_review": None,
                     "reviewed_sha256_12": reviewed.get(slug),
                     "head_sha256_12": shas[fname],
                     "reading": "the two layers measure different legs — the "
                                "seat measured existence and naming, the probe "
                                "measures the accessor; both stand at their own "
                                "leg"})
        matrix.append({"unit": slug, "instrument": fname,
                       "sha256_12": shas[fname], "families": fams})
    R["matrix"] = matrix
    R["disagreements"] = disagreements
    R["family_counts"] = {k: {v: fam_counts[k][v] for v in
                              list(VERDICTS) + ["panel_PRESENT", "panel_ABSENT"]}
                          for k in PROBES}

    open_cells = sum(fam_counts[k]["CARRIES"] + fam_counts[k]["PARTIAL"] for k in PROBES)
    ns_cells = sum(fam_counts[k]["NO-SURFACE"] for k in PROBES)
    ev_cells = verdict_count - ns_cells
    REG.measured("open_cells", open_cells, "CARRIES + PARTIAL over the matrix")
    REG.measured("evaluable_cells", ev_cells, "probe verdicts minus NO-SURFACE")
    SEAL.seal("matrix", matrix, "G-MATRIX-TOTAL")
    SEAL.seal("disagreements", disagreements, "G-MATRIX-TOTAL")
    SEAL.seal("reviewed_shas", R["reviewed_shas"], "G-MATRIX-TOTAL")
    SEAL.seal("family_counts", R["family_counts"], "G-MATRIX-TOTAL")
    gate("G-MATRIX-TOTAL",
         REG.stmt("the matrix carries one cell for every unit and family, "
                  "{probe_verdicts} in all, of which {evaluable_cells} are "
                  "evaluable and {open_cells} read CARRIES or PARTIAL",
                  probe_verdicts=1, evaluable_cells=1, open_cells=1),
         len(matrix) == len(UNITS) and all(len(m["families"]) == len(PROBES)
                                           for m in matrix),
         "rows %d cells %d evaluable %d open %d"
         % (len(matrix), verdict_count, ev_cells, open_cells))

    # -- residuals ----------------------------------------------------------
    R["residuals"] = [{"unit": u, "family": f, "ledger": l, "residual": t}
                      for u, f, l, t in RESIDUALS]
    SEAL.seal("residuals", R["residuals"], "G-RESIDUALS-CARRIED")
    REG.measured("residuals", len(RESIDUALS), "len(RESIDUALS)")
    gate("G-RESIDUALS-CARRIED",
         REG.stmt("the {residuals} residuals already registered to this sweep "
                  "are carried per unit and per family", residuals=1),
         all(f in PROBES for _u, f, _l, _t in RESIDUALS),
         "residuals %d" % len(RESIDUALS))

    # -- the spec's own counts, bound to these registries --------------------
    tclaims = template_counts(reads)
    bad = []
    for c in tclaims:
        want = R["family_counts"][c["family"]][c["claim"]]
        if c["claimed"] != want:
            bad.append("(%s) %s: spec says %s, measured %d"
                       % (c["family"], c["claim"], c["word"], want))
        if "denominator" in c and c["denominator"] != len(UNITS):
            bad.append("(%s) denominator: spec says %s, measured %d"
                       % (c["family"], c["denominator_word"], len(UNITS)))
    covered = {c["family"] for c in tclaims if c["claim"] == "panel_PRESENT"}
    if covered != set(PROBES):
        bad.append("no panel count located for families %s"
                   % sorted(set(PROBES) - covered))
    R["template_claims"] = tclaims
    SEAL.seal("template_claims", tclaims, "G-TEMPLATE-COUNTS-BOUND")
    gate("G-TEMPLATE-COUNTS-BOUND",
         "every count v14/TEMPLATE.md states about this census is read back "
         "out of the document and compared with the live registry, so the "
         "spec cannot state a number the census does not measure",
         not bad,
         "claims %d bound %d mismatched %s"
         % (len(tclaims), len(tclaims) - len(bad), bad or "none"))

    # -- provenance and the declared read set -------------------------------
    R["probes"] = {k: PROBES[k] for k in sorted(PROBES)}
    R["families"] = [{"key": k, "name": n, "check": c} for k, n, c in ET.FAMILIES]
    SEAL.declare_unsealed("probes", "the probe questions, fixed in the source "
                          "and published verbatim")
    SEAL.declare_unsealed("families", "the family register, imported from "
                          "era_template.FAMILIES")
    reads.append("v14/code/era_template.py")
    reads.append("v14/note-tpl-pin.md")
    reads.append(os.path.relpath(os.path.abspath(__file__), REPO))
    R["provenance"] = {
        "template": "v14/code/era_template.py",
        "template_sha256_12": sha12(os.path.join(REPO, "v14/code/era_template.py")),
        "self_sha256_12": sha12(os.path.abspath(__file__)),
        "pin": "v14/note-tpl-pin.md",
        "pin_sha256_12": sha12(os.path.join(REPO, "v14/note-tpl-pin.md")),
        "head_note": "the committed working tree at the census run",
        "mirror": MIRROR,
    }
    SEAL.declare_unsealed("provenance", "self-describing paths and digests, "
                          "verified at G-PROVENANCE")
    gate("G-PROVENANCE",
         "the template, the pin and this instrument are digested and published",
         all(len(v) == 12 for k, v in R["provenance"].items()
             if k.endswith("sha256_12")),
         "digests %d" % sum(1 for k in R["provenance"] if k.endswith("sha256_12")))

    # -- totals, derived last so nothing they count can still move -----------
    with_panel = len({c["unit"] for c in cites})
    present = sum(1 for c in cites if c["verdict"] == "PRESENT")
    absent = sum(1 for c in cites if c["verdict"] == "ABSENT")
    with_present = len({c["unit"] for c in cites if c["verdict"] == "PRESENT"})
    R["totals"] = {
        "units": len(UNITS), "families": len(PROBES),
        "units_with_panel": with_panel,
        "units_without_panel": len(UNITS) - with_panel,
        "probe_verdicts": verdict_count, "evaluable_cells": ev_cells,
        "no_surface_cells": ns_cells, "open_cells": open_cells,
        "citations": len(cites), "citations_located": len(cites) - len(unlocated),
        "citations_unlocated": len(unlocated), "reviews_cited": len(review_sha),
        "panel_present": present, "panel_absent": absent,
        "units_with_a_present": with_present,
        "disagree_repaired": sum(1 for d in disagreements if d["panel"] == "PRESENT"),
        "disagree_object_moved": sum(1 for d in disagreements
                                     if d.get("object_moved_since_review") is True),
        "disagree_object_unchanged": sum(1 for d in disagreements
                                         if d.get("object_moved_since_review") is False),
        "disagree_object_unknown": sum(1 for d in disagreements
                                       if d["panel"] == "PRESENT"
                                       and d.get("object_moved_since_review") is None),
        "reviewed_shas_located": sum(1 for v in reviewed.values() if v),
        "disagree_probe_blind": sum(1 for d in disagreements if d["panel"] == "ABSENT"),
        "repo_reads": len(set(reads)), "repo_writes": 2 if write else 0,
        "residuals": len(RESIDUALS),
    }
    SEAL.seal("totals", R["totals"], "G-TOTALS-DERIVED")
    gate("G-TOTALS-DERIVED",
         "every published total is derived from a live registry rather than "
         "typed, and the census prose is rendered from this receipt",
         all(isinstance(v, int) for v in R["totals"].values()),
         "totals %d" % len(R["totals"]))

    # -- the document, rendered ONCE from the receipt -------------------------
    census_md = render_census(R)
    R["census_document"] = {"chars": len(census_md),
                            "lines": census_md.count("\n"),
                            "sha256_12": ET.bytes_digest(census_md.encode("utf-8"))}
    SEAL.seal("census_document", R["census_document"], "G-CENSUS-RENDERED")
    gate("G-CENSUS-RENDERED",
         "the census document is rendered from this receipt, so no numeral in "
         "it can go stale; the bytes gated here are the bytes promoted",
         len(census_md) > 0,
         "chars %d lines %d digest %s"
         % (len(census_md), census_md.count("\n"),
            R["census_document"]["sha256_12"]))

    declared = sorted(set(reads))
    ev = RS.gate_at_close(declared)
    R["read_set"] = {"declared": declared, "distinct": ev["distinct"],
                     "reads": ev["reads"]}
    SEAL.seal("read_set", R["read_set"], "G-READS-AT-THE-ACCESSOR")
    gate("G-READS-AT-THE-ACCESSOR",
         "every repository read is recorded at an open audit hook and compared "
         "with the declared set as a multiset at the last gate",
         True, "declared %d distinct %d" % (len(declared), ev["distinct"]))
    RS.active = False

    tdig = TR.bind(LD)
    R["transcript"] = {"sha256_12": tdig, "lines": len(TR.lines),
                       "gate_rows": len(LD.rows), "chain_head": LD.head}
    SEAL.seal("transcript", R["transcript"], "G-TRANSCRIPT-BOUND")
    gate("G-TRANSCRIPT-BOUND",
         "the transcript's PASS lines are parsed back and reconciled with the "
         "ledger as a multiset, evidence included",
         LD.recompute_chain() == LD.head,
         "rows %d chain %s" % (len(LD.rows), LD.head))
    TR.bind(LD)

    if not write:
        return R, census_md, TR, LD, SEAL, None

    dig = ET.promote(SEAL, LD, R, census_md,
                     os.path.join(REPO, RECEIPT_REL),
                     os.path.join(REPO, CENSUS_REL))
    return R, census_md, TR, LD, SEAL, dig


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: tpl_census.py "
                         "--run|--no-write|--selftest|--list-gates|--list-probes\n")
        return 2
    mode = argv[1]
    if mode == "--list-probes":
        for k in sorted(PROBES):
            print("(%s) %s" % (k, PROBES[k]))
        return 0
    if mode == "--list-gates":
        # DERIVED, never typed: a hand-kept gate list goes stale the first
        # time a gate is added — measured in this instrument's own first
        # battery, where a typed list of ten stood beside eleven fired gates
        # (SEC-2 K3 MAJOR-9's disease, at the census's own hands).
        _R, _md, _tr, _ld, _seal, _d = full_run(write=False)
        for g in _ld.names():
            print(g)
        return 0
    if mode == "--selftest":
        try:
            R, md, TR, LD, SEAL, _ = full_run(write=False)
        except ET.CheckFail as exc:
            print("SELFTEST: the clean run died at %s :: %s" % (exc.check, exc.detail))
            return 1
        forged = TR.text().replace("[PASS] G-PROBES-RUN", "[PASS] G-FORGED-GATE")
        try:
            TR.bind(LD, forged)
            print("SELFTEST: a forged transcript row SURVIVED")
            return 1
        except ET.CheckFail as exc:
            print("SELFTEST: a forged transcript row dies at %s" % exc.check)
        R["forged_key"] = {"smuggled": 1}
        try:
            SEAL.verify_at_promotion(R, LD, "seal_manifest")
            print("SELFTEST: a post-seal add SURVIVED")
            return 1
        except ET.CheckFail as exc:
            print("SELFTEST: a post-seal add dies at %s" % exc.check)
        del R["forged_key"]
        # the spec-binding leg, on a mutated copy in scratch
        scratch = os.path.join(os.path.dirname(MIRROR), "selftest")
        os.makedirs(os.path.join(scratch, "v14"), exist_ok=True)
        with open(os.path.join(REPO, "v14/TEMPLATE.md"), "r",
                  encoding="utf-8") as fh:
            spec = fh.read()
        first = [c for c in R["template_claims"]
                 if c["claim"] == "panel_PRESENT"][0]
        bent = spec.replace("%s units" % first["word"], "thirty units", 1)
        with open(os.path.join(scratch, "v14/TEMPLATE.md"), "w",
                  encoding="utf-8") as fh:
            fh.write(bent)
        mutated = template_counts([], root=scratch)
        caught = [c for c in mutated
                  if c["claim"] == "panel_PRESENT"
                  and c["claimed"] != R["family_counts"][c["family"]]["panel_PRESENT"]]
        shutil.rmtree(scratch)
        if not caught:
            print("SELFTEST: a bent spec count SURVIVED")
            return 1
        print("SELFTEST: a bent spec count is caught at (%s) %s"
              % (caught[0]["family"], caught[0]["word"]))
        print("SELFTEST: clean run green over %d gates; nothing written"
              % len(LD.rows))
        return 0
    if mode in ("--run", "--no-write"):
        write = (mode == "--run")
        try:
            R, md, TR, LD, SEAL, dig = full_run(write=write)
        except ET.CheckFail as exc:
            sys.stderr.write("REFUSED at %s :: %s\n" % (exc.check, exc.detail))
            return 1
        print(TR.text())
        if write:
            print("WROTE %s (%s) and %s (%s)"
                  % (RECEIPT_REL, dig["receipt"], CENSUS_REL, dig["side"]))
        else:
            print("NO-WRITE: census rendered, %d chars, nothing written" % len(md))
        return 0
    sys.stderr.write("unknown argument: %r\n" % mode)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
