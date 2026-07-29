"""
v13 GW1 STEP 0 — the census receipt.

A failed instrument gate needs a receipt as much as a successful experiment.
This script IS that receipt: it re-executes the census's evidence and emits a
machine-readable record.  It runs no GW1 STEP 1-5: no closure relation is
solved, no q-tilde is fitted, nothing is claimed about geometry.

Emits
  v13/receipts/gw1_step0_census.json   the full record
  v13/receipts/gw1_step0_runs.txt      per-run stdout digests and key lines

Records
  1. audited commit SHA, working-tree status, interpreter and library versions;
  2. every inspected path with its working-tree blob hash and its HEAD blob
     hash (and whether they differ);
  3. every search command of the census's token sweep, re-executed, with counts;
  4. every committed-script re-run: exit code, wall time, stdout sha256, and the
     anchor lines the census quotes;
  5. the classification table in the 15-field schema, covering the four
     runnable families, v3 p2 Candidate B, and the v4 p7 declared family.

Anchors (committed numbers reused) exit 1.  Substantive negatives exit 0.
Caps: 9 re-runs, ~40 s of re-run wall time; total runtime < 2 min.
Substrate for the re-runs: whatever each committed script declares; this script
changes no file in the corpus.
"""
import hashlib
import json
import os
import platform
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PY = os.path.join(REPO, "code", ".venv", "bin", "python3.13")
OUT = os.path.join(REPO, "v13", "receipts")
FAIL = []


def sh(cmd, cwd=REPO):
    p = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def note(msg=""):
    print(msg, flush=True)


# =====================================================================
# 1. ENVIRONMENT
# =====================================================================
note("=" * 78)
note("1. ENVIRONMENT AND AUDITED STATE")
note("=" * 78)
_, head, _ = sh("git rev-parse HEAD")
_, head_short, _ = sh("git rev-parse --short HEAD")
_, porcelain, _ = sh("git status --porcelain")
dirty = [ln for ln in porcelain.splitlines() if ln.strip()]
try:
    import numpy
    import scipy
    numpy_v, scipy_v = numpy.__version__, scipy.__version__
except Exception:                                          # pragma: no cover
    numpy_v = scipy_v = "unavailable"
env = {
    "audited_commit": head,
    "audited_commit_short": head_short,
    "working_tree_clean": len(dirty) == 0,
    "working_tree_entries": dirty,
    "python": platform.python_version(),
    "python_executable": sys.executable,
    "numpy": numpy_v,
    "scipy": scipy_v,
    "platform": platform.platform(),
}
note(f"  audited commit      {head}")
note(f"  working tree        {'CLEAN' if not dirty else f'DIRTY ({len(dirty)} entries)'}")
for ln in dirty:
    note(f"                      {ln}")
note(f"  interpreter         {sys.executable}  python {platform.python_version()}")
note(f"  numpy {numpy_v}   scipy {scipy_v}")

# =====================================================================
# 2. INSPECTED PATHS
# =====================================================================
note()
note("=" * 78)
note("2. INSPECTED PATHS (working-tree blob hash vs HEAD blob hash)")
note("=" * 78)
PATHS = [
    # instrument (i): order/count diagnostics
    "code/v6_task2b_metric_extraction.py",
    "code/v6_p2d_curved_coefficient.py",
    "code/v6_p2_spatial_direction.py",
    "code/v6_p2b_local_frame.py",
    "v8/code/r1_order_to_conformal_direction.py",
    "v8/code/r2_number_volume_lstep.py",
    "v8/code/r3_manifoldlikeness_myrheim_meyer.py",
    "v8/code/k3_decoration_probe.py",
    "v8/code/l2_intrinsic_finder.py",
    "v8/code/m1_intrinsic_4d.py",
    "v8/code/m2_intrinsic_4d_scale.py",
    "v9/code/n1_chi_dictionary.py",
    "v9/code/n2_chi_geometry.py",
    "v9/code/dimwall_lorentz1.py",
    "v10/code/d29_ruler_validation.py",
    # family 1: record-growth updates
    "code/v6_task2_antichain_deformations.py",
    "code/v6_task2d_bracket_closure.py",
    "code/v6_task2e_AvsB_diagnostic.py",
    "code/v6_task2f_nogo_confirm.py",
    # family 2: embedding-flow
    "code/v6_p2c_flow_drift.py",
    "code/v6_p2e_3d_tensor_coefficient.py",
    "code/v6_p2f_4d_tensor_coefficient.py",
    # family 3: Gamma-level lattice
    "v10/code/d43a_lie_trotter_exact.py",
    "validate_minimal_interacting_gauge_matter_benchmark.py",
    "validate_truncated_u1_benchmark.py",
    # family 4: record-history holonomies
    "v10/code/d42b3_placement_exact.py",
    "v10/code/d49_dichotomy_settlement_exact.py",
    "v10/code/d44f_foliation_measure_exact.py",
    "v10/code/d74_transport_holonomy_exact.py",
    "v10/code/d72_weld_exact.py",
    "v11/code/ld_reversal_probe_exact.py",
    "v11/code/u2_three_address_weld_exact.py",
    "v11/code/u3_unistochasticity_screen_exact.py",
    "code/v6_p4n_exchange_cocycle_law.py",
    # definition-only sources
    "v2/relativistic-isp-v2-paper1-free-stochastic-curvature-theorem.md",
    "v2/relativistic-isp-v2-paper10-metric-data-from-stochastic-exchange-curvature-investigation.md",
    "v3/relativistic-isp-v3-paper2-primitive-smooth-lapse-hypersurface-kernels.md",
    "v4/relativistic-isp-v4-paper2-fixed-background-metric-data-from-exchange-curvature.md",
    "v4/relativistic-isp-v4-paper4-operational-orientation-quorum-or-enriched-only-metric-diagnostic.md",
    "v4/relativistic-isp-v4-paper5-operational-curvature-compatibility-source.md",
    "v4/relativistic-isp-v4-paper7-finite-constraint-dynamics-or-gr-no-go.md",
    "v4/relativistic-isp-v4-paper12-residual-source-ward-stein-four-route-decision.md",
    "v4/relativistic-isp-v4-paper13-three-normal-switch-decision-or-floor.md",
    "v6/relativistic-isp-v6-paper2-spatial-direction-and-interacting-integrability.md",
    "publishable/paper2-hypersurface-deformation-obstruction.md",
    # the unit's own binding documents
    "v13/relativistic-isp-v13-paper0-gravity.md",
    "v13/note-gw1-metric-from-closure-pin.md",
]
paths_rec = []
for p in PATHS:
    full = os.path.join(REPO, p)
    if not os.path.exists(full):
        FAIL.append(f"missing path {p}")
        paths_rec.append({"path": p, "exists": False})
        note(f"  MISSING  {p}")
        continue
    _, wt, _ = sh(f"git hash-object {p!r}")
    rc, hd, _ = sh(f"git rev-parse HEAD:{p}")
    hd = hd if rc == 0 else None
    paths_rec.append({"path": p, "exists": True, "worktree_blob": wt,
                      "head_blob": hd, "modified": (hd is not None and hd != wt)})
    flag = "  MODIFIED-VS-HEAD" if (hd is not None and hd != wt) else ""
    note(f"  {wt[:12]}  {p}{flag}")
note(f"  {len(paths_rec)} paths inspected; "
     f"{sum(1 for r in paths_rec if r.get('modified'))} differ from HEAD")

# =====================================================================
# 3. SEARCH PROTOCOL
# =====================================================================
note()
note("=" * 78)
note("3. SEARCH PROTOCOL (token sweeps, re-executed, with counts)")
note("=" * 78)
TREES = ["code", "v6/code", "v7/code", "v8/code", "v9/code", "v10/code", "v11/code",
         "v12/code", "bc/code", "external/walsh-delta-code",
         "_archive_low_value_2026-06-14/code"]
searches = []


def count_py(tree):
    cmd = f"find {tree} -name '*.py' -not -path '*/.venv/*' | wc -l"
    _, o, _ = sh(cmd)
    return int(o.strip()), cmd


def count_token(tree, token):
    cmd = f"grep -rlwi {token!r} {tree} --include='*.py' | wc -l"
    _, o, _ = sh(cmd)
    return int(o.strip()), cmd


note(f"  {'tree':<36} {'.py':>5} {'lapse':>6} {'hypersurface':>13} {'antichain':>10}")
for tree in TREES:
    npy, c0 = count_py(tree)
    nl, c1 = count_token(tree, "lapse")
    nh, c2 = count_token(tree, "hypersurface")
    na, c3 = count_token(tree, "antichain")
    searches.append({"tree": tree, "py_files": npy, "lapse_files": nl,
                     "hypersurface_files": nh, "antichain_files": na,
                     "commands": [c0, c1, c2, c3]})
    note(f"  {tree:<36} {npy:>5} {nl:>6} {nh:>13} {na:>10}")
# repository root .py files
_, o, _ = sh("ls *.py | wc -l")
nroot = int(o.strip())
_, o, _ = sh("grep -lwi 'lapse' *.py | wc -l")
nrootl = int(o.strip())
_, o, _ = sh("grep -lwi 'hypersurface' *.py | wc -l")
nrooth = int(o.strip())
_, o, _ = sh("grep -lwi 'antichain' *.py | wc -l")
nroota = int(o.strip())
searches.append({"tree": "<repository root>", "py_files": nroot, "lapse_files": nrootl,
                 "hypersurface_files": nrooth, "antichain_files": nroota,
                 "commands": ["ls *.py", "grep -lwi lapse *.py",
                              "grep -lwi hypersurface *.py", "grep -lwi antichain *.py"]})
note(f"  {'<repository root>':<36} {nroot:>5} {nrootl:>6} {nrooth:>13} {nroota:>10}")
_, o, _ = sh("for d in v1 v2 v3 v4 v5 publishable; do find $d -name '*.py'; done | wc -l")
n_paper_py = int(o.strip())
searches.append({"tree": "v1..v5 + publishable", "py_files": n_paper_py,
                 "lapse_files": 0, "hypersurface_files": 0, "antichain_files": 0,
                 "commands": ["find v1 v2 v3 v4 v5 publishable -name '*.py'"]})
note(f"  {'v1..v5 + publishable':<36} {n_paper_py:>5}   (paper trees: definition-only)")

# the census's load-bearing search results
if sum(s["lapse_files"] for s in searches if s["tree"] != "code") != 0:
    FAIL.append("lapse token found outside code/")
if sum(s["hypersurface_files"] for s in searches if s["tree"] != "code") != 0:
    FAIL.append("hypersurface token found outside code/")
if n_paper_py != 0:
    FAIL.append("a .py appeared under a paper tree")
note(f"  RESULT: 'lapse' occurs only under code/ ({searches[0]['lapse_files']} of 353 files); "
     f"'hypersurface' likewise ({searches[0]['hypersurface_files']} files, both prose "
     f"references to the Dirac-Schwinger algebra); every other runnable tree returns 0 for "
     f"both tokens; the paper trees carry no .py at all.")

# =====================================================================
# 4. RE-RUNS
# =====================================================================
note()
note("=" * 78)
note("4. RE-RUNS OF COMMITTED SCRIPTS (exit code, wall time, stdout sha256)")
note("=" * 78)
RUNS = [
    ("code/v6_task2b_metric_extraction.py", ["structure function g^xx = +0.99"]),
    ("code/v6_task2d_bracket_closure.py",
     ["CONTROL holds: equal lapses commute exactly (|comm|=0) in every run"]),
    ("code/v6_task2e_AvsB_diagnostic.py", ["(A) STRUCTURAL BLINDNESS"]),
    ("code/v6_task2f_nogo_confirm.py", ["IDEAL pointwise-additive deformation: |commutator| = 0 EXACTLY"]),
    ("code/v6_p2c_flow_drift.py", ["= +1.0000", "mean +0.540", "mean 1.26"]),
    ("code/v6_p2d_curved_coefficient.py",
     ["corr(C, 1/Omega^2)=+1.0000", "corr(C, 1/Omega^2)=+0.0109",
      "corr(C_chain, 1/Omega^2_true) = +0.993", "corr(C_dens , 1/Omega^2_true) = +1.000",
      "corr(C_chain, C_dens)         = +0.995",
      "centre/wing of C_chain = 0.214  (GR target 0.160"]),
    ("code/v6_p2e_3d_tensor_coefficient.py", ["cos=1.0000", "0.9729", "13.38"]),
    ("code/v6_p2f_4d_tensor_coefficient.py", ["cos=1.0000", "0.9739", "13.13"]),
    ("code/v6_p2_spatial_direction.py", ["mean=0.94", "x from (v2,v3): mean=0.95;  y: mean=0.92"]),
]
runs_rec, runs_txt = [], []
for script, anchors in RUNS:
    t0 = time.time()
    p = subprocess.run([PY, script], cwd=REPO, capture_output=True, text=True)
    dt = time.time() - t0
    digest = hashlib.sha256(p.stdout.encode()).hexdigest()
    hits = {a: (a in p.stdout) for a in anchors}
    ok = all(hits.values()) and p.returncode == 0
    if not ok:
        FAIL.append(f"anchor {script}")
    runs_rec.append({"script": script, "exit_code": p.returncode,
                     "wall_seconds": round(dt, 2), "stdout_sha256": digest,
                     "anchors": hits, "anchors_ok": ok})
    note(f"  {os.path.basename(script):<36} exit {p.returncode}  {dt:>6.2f} s  "
         f"{digest[:16]}  anchors {'OK' if ok else 'FAIL'}")
    runs_txt.append("=" * 78)
    runs_txt.append(f"{script}  exit={p.returncode}  wall={dt:.2f}s  sha256={digest}")
    for a, h in hits.items():
        runs_txt.append(f"  anchor [{'HIT ' if h else 'MISS'}] {a}")
    runs_txt.append("--- stdout ---")
    runs_txt.append(p.stdout.rstrip())
total_wall = sum(r["wall_seconds"] for r in runs_rec)
note(f"  total re-run wall time {total_wall:.1f} s over {len(runs_rec)} scripts")
note("  error control: none of the nine scripts prints a standard error, a")
note("  standard deviation, or a repeat-to-repeat spread; every quoted number is")
note("  a single-seed point estimate.  Declared here, not repaired here.")

# =====================================================================
# 5. THE CLASSIFICATION TABLE
# =====================================================================
note()
note("=" * 78)
note("5. CLASSIFICATION TABLE (15-field schema, every located family)")
note("=" * 78)
SCHEMA = ["family", "substrate", "object_type", "runnable", "spatial_dimension",
          "takes_lapse_profile", "primitive_signed_lapse", "metric_explicitly_supplied",
          "background_geometry_encoded", "transported_second_step",
          "invertible_comparison_map", "forward_swap_nontrivial",
          "group_twocell_defined", "group_twocell_nontrivial", "q_order_same_substrate"]
TABLE = [
    {
        "family": "1. record-growth updates (v6 task2/2d/2e/2f)",
        "substrate": "sprinkled causal set (1+1)",
        "object_type": "Phi — monotone history update (down-set advance)",
        "runnable": "yes",
        "spatial_dimension": 1,
        "takes_lapse_profile": "yes (eventwise N(x_e), coordinate-assisted at task2d:11-13)",
        "primitive_signed_lapse": "no (threshold shift; sign untested)",
        "metric_explicitly_supplied": "no",
        "background_geometry_encoded": "partial — the lapse is applied at the embedding coordinate x_e",
        "transported_second_step": "no — two forward orders on a fixed event set",
        "invertible_comparison_map": "threshold rule: empirically yes, bitwise, on tested instances; "
                                     "recomputed-height rule: no (non-injective set union)",
        "forward_swap_nontrivial": "threshold rule: no, delta_swap = 0 exactly [theorem, v6_task2f:4-8]; "
                                   "recomputed-height rule: yes but gradient-blind",
        "group_twocell_defined": "threshold rule: yes (additive translations); "
                                 "recomputed-height rule: no (no inverse)",
        "group_twocell_nontrivial": "threshold rule: no, Omega = I exactly; "
                                    "recomputed-height rule: undefined",
        "q_order_same_substrate": "yes (v6_task2b, v6_p2d PART 2 run on the same sprinkling)",
    },
    {
        "family": "2. embedding-flow / grid (v6 p2c/p2d/p2e/p2f PART 1; v4 p5 Def 3.3)",
        "substrate": "coordinate grid with a declared background metric",
        "object_type": "Phi — embedding flow on tracer labels (v4 p5: J^emb = T_a(Phi_N^eps))",
        "runnable": "yes",
        "spatial_dimension": "1, 2, 3",
        "takes_lapse_profile": "yes",
        "primitive_signed_lapse": "yes (a real-valued profile field)",
        "metric_explicitly_supplied": "yes — the unit normal is normalized with it "
                                      "(p2c:32-36, p2d:50-54, p2e:42-47, p2f:38-47)",
        "background_geometry_encoded": "yes",
        "transported_second_step": "yes — the second push acts on the pushed slice",
        "invertible_comparison_map": "not formed; the flow is inverted only in the small-eps expansion",
        "forward_swap_nontrivial": "yes — the O(eps^2) tracer-label difference",
        "group_twocell_defined": "not as supplied — no J^-1 is constructed; the measured object is "
                                 "x1 - x2 at leading order",
        "group_twocell_nontrivial": "the leading-order surrogate is nonzero and equals "
                                    "-eps^2 q^ij(N d_j M - M d_j N)",
        "q_order_same_substrate": "no — the metric is declared input on this substrate",
    },
    {
        "family": "3. Gamma-level lattice (v2 p1, p10; v10 d43a; the root validators)",
        "substrate": "fixed lattice Dirac benchmark",
        "object_type": "Gamma endpoint kernel -> J algebraic comparison map -> Omega group two-cell",
        "runnable": "yes at Delta-parameterized code level; the lapse-parameterized family is "
                    "theorem-level only",
        "spatial_dimension": "1 (theorem); d >= 2 posed and blocked",
        "takes_lapse_profile": "yes at paper level (v2 p10:747-760 J[N;Delta] = exp L[N;Delta]); "
                               "no in any committed .py (region + slab thickness only)",
        "primitive_signed_lapse": "no — pseudo-stochastic for sign-changing N (v2 p10:765-768)",
        "metric_explicitly_supplied": "yes — the frame E_A^j fixes h_0^ij and enters the "
                                      "Hamiltonian (v2 p10:655-671)",
        "background_geometry_encoded": "yes",
        "transported_second_step": "no — a fixed-space group commutator",
        "invertible_comparison_map": "yes for small |Delta| (v2 p10:804-808)",
        "forward_swap_nontrivial": "yes",
        "group_twocell_defined": "yes — E[N,M;Delta] = J_N J_M J_N^-1 J_M^-1 (v2 p10:773-778)",
        "group_twocell_nontrivial": "yes, exact; recovery blocked at h^12 to all orders (Prop 10.6)",
        "q_order_same_substrate": "no",
    },
    {
        "family": "4. record-history holonomies (v10 d42b3/d49/d44f/d72/d74; v11 ld/u2/u3; v6_p4n)",
        "substrate": "exact record histories, Fraction-exact weights",
        "object_type": "record-holonomy weight ratio (path-order ratio of admission weights)",
        "runnable": "yes, exact",
        "spatial_dimension": "not defined — no slice, no spatial index",
        "takes_lapse_profile": "no — advance is by one event",
        "primitive_signed_lapse": "not applicable",
        "metric_explicitly_supplied": "no",
        "background_geometry_encoded": "no",
        "transported_second_step": "path-order ratios on closed squares",
        "invertible_comparison_map": "weight ratios invert; no comparison-map family is declared",
        "forward_swap_nontrivial": "yes — 36 chain-consistency violations of 202 diamonds; "
                                   "88 of 1546 closed squares non-unit",
        "group_twocell_defined": "not in the pinned form — no N, no eps, no d_j",
        "group_twocell_nontrivial": "the holonomy census is nontrivial; the pinned Omega is not posed",
        "q_order_same_substrate": "partial — the same order data, no metric extraction run there",
    },
    {
        "family": "5. smooth-lapse convex mixture (v3 p2 Candidate B) — definition-only",
        "substrate": "fixed flat lattice Dirac benchmark (V2 singleton kernels imported)",
        "object_type": "Gamma endpoint kernel -> J algebraic comparison map -> Omega group two-cell",
        "runnable": "no — v3 carries no code; definition only",
        "spatial_dimension": 1,
        "takes_lapse_profile": "yes — smooth compactly supported N",
        "primitive_signed_lapse": "no — positive cone only; signed lapses reached by "
                                  "continuum polarization (Thm 7.2), finite-regulator signed "
                                  "kernel declared an open burden (v3 p2:596-610)",
        "metric_explicitly_supplied": "no metric symbol in the kernel",
        "background_geometry_encoded": "yes — the singleton kernels come from the fixed flat "
                                       "lattice benchmark; fails the no-smuggling test",
        "transported_second_step": "no — a fixed-space group commutator",
        "invertible_comparison_map": "yes (J^mix = I + O(eta a))",
        "forward_swap_nontrivial": "yes at theorem level",
        "group_twocell_defined": "yes — E^mix[N,M;Delta] = J_N J_M J_N^-1 J_M^-1 (v3 p2:298-313)",
        "group_twocell_nontrivial": "yes at Theorem 6.1, positive cone, conditional on a "
                                    "uniform singleton-remainder bound",
        "q_order_same_substrate": "no",
    },
    {
        "family": "6. declared normal comparison maps (v4 p7 Defs 1.3/1.4/2.3; p12/p13 switch) — the fifth family of v13 LOG #3",
        "substrate": "finite total matter-geometry records, general regulator a",
        "object_type": "H_a[N] algebraic comparison map + D_a[v]; R_HH,a the pinned residual",
        "runnable": "no — v4 carries no code; declaration only",
        "spatial_dimension": "general d (the metric candidate is I_a(g)^ij)",
        "takes_lapse_profile": "yes — a finite lapse test N",
        "primitive_signed_lapse": "unconstrained by declaration",
        "metric_explicitly_supplied": "no — I_a(g)^ij is READ from the finite geometry record g_a",
        "background_geometry_encoded": "no (g is a finite configuration variable, v4 p7:238)",
        "transported_second_step": "declared via D_a[-beta_a(g;N,M)] in R_HH,a",
        "invertible_comparison_map": "yes BY DECLARATION (v4 p7:161-166) — never constructed",
        "forward_swap_nontrivial": "not excluded; p13 Prop 3.6 exhibits a nonzero three-normal "
                                   "switch detector on a two-state metric alphabet",
        "group_twocell_defined": "yes — R_HH,a[N,M] is the pinned object exactly (v4 p7:227-236)",
        "group_twocell_nontrivial": "undecided — no construction exists to measure",
        "q_order_same_substrate": "no — no order/count instrument runs on a v4 record substrate",
    },
]
for row in TABLE:
    missing = [f for f in SCHEMA if f not in row]
    if missing:
        FAIL.append(f"schema fields missing in {row.get('family')}: {missing}")
    note()
    note(f"  {row['family']}")
    for f in SCHEMA[1:]:
        note(f"      {f:<28} {row[f]}")

# =====================================================================
# 6. EMIT
# =====================================================================
os.makedirs(OUT, exist_ok=True)
record = {
    "unit": "v13 GW1",
    "step": "STEP 0 — instrument census",
    "verdict": "GW1-NOT-RUNNABLE — PRIMARY LOCATED BLOCK AT THE DEFORMATION INTERFACE",
    "steps_1_5_run": False,
    "environment": env,
    "inspected_paths": paths_rec,
    "search_protocol": searches,
    "reruns": runs_rec,
    "rerun_total_wall_seconds": round(total_wall, 2),
    "error_control_declared_by_any_rerun": False,
    "schema": SCHEMA,
    "classification": TABLE,
    "anchor_failures": FAIL,
}
with open(os.path.join(OUT, "gw1_step0_census.json"), "w") as fh:
    json.dump(record, fh, indent=2, sort_keys=False)
with open(os.path.join(OUT, "gw1_step0_runs.txt"), "w") as fh:
    fh.write("\n".join(runs_txt) + "\n")
note()
note("=" * 78)
note(f"  wrote {os.path.relpath(os.path.join(OUT, 'gw1_step0_census.json'), REPO)}")
note(f"  wrote {os.path.relpath(os.path.join(OUT, 'gw1_step0_runs.txt'), REPO)}")
if FAIL:
    note("  ANCHOR FAILURES: " + ", ".join(FAIL))
    sys.exit(1)
note("  all anchors hold.  STEP 0 does not pass; STEPS 1-5 are not run.")
note("=" * 78)
