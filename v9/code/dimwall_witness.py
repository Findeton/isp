#!/usr/bin/env python3
"""
dimwall_witness.py — v9 round 35: THE COMMITTED WITNESS CERTIFICATION
(note-3p1-witness §1; pin committed at 089c115 strictly before this
receipt; the paper-6 hostile review's MAJOR-4a).
The round-30 reserved review's S_{C+1} witness certification ran
uncommitted; this receipt carries it.  Searcher = openings_pass.py's
find_s4, generic-k (S3 variant: 3 + 3, sum(above) = 2), bucket step
vectorized, tries = 20000 FROZEN (the round-35 0/5 was tries = 200
underpower; validated 5/5 at 20k by the paper-6 review); one search
RNG, seed 20261440.
W1 (validation): S4 in iid 4-orthant 5/5 (seeds 700-704); S4 0/5 on
    iid 3-orthant (800-804); S4 0/10 on C = 2 windows (web seeds
    20261420-20261424, 2 draws each) — theorem-guaranteed absences;
    S3 in iid 3-orthant 5/5; S3 0/5 on iid 2-orthant (900-904).
W2 (the certification): S4 witnesses in Delta = 512 central windows
    (N = 128 subsamples, <= 6 draws/seed, first witness stops the
    seed) of the five PINNED C = 3 seeds 20260960-20260964 on 5/5,
    AND S3 witnesses in the same seeds' C = 2 windows on 5/5.
Every witness explicitly re-verified against the relation matrix
(the full S_k pattern asserted) and printed.  Exit 1 on any refusal.
"""
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def orthant_rel(rng, N, k):
    Z = rng.random((N, k))
    rel = np.ones((N, N), dtype=bool)
    for j in range(k):
        rel &= Z[:, None, j] < Z[None, :, j]
    np.fill_diagonal(rel, False)
    return rel

def web_chiv(sd, C, N=2048, M=32, L=16, alpha=0.75):
    rng = np.random.default_rng(sd)
    acc = np.zeros((M, C))
    pref = np.arange(M) % C
    chiV = np.zeros((N, C))
    for t in range(N):
        c = int(rng.integers(M))
        if C > 1 and rng.random() < alpha:
            k = int(pref[c])
        else:
            k = int(rng.integers(C))
        acc[c, k] += rng.exponential(0.109551)
        chiV[t] = acc[c]
        for kk in range(C):
            if rng.random() < 1.0 / L:
                acc[int(rng.integers(M)), kk] = 0.0
    return chiV, rng

def rel_win(idx, chiV, C):
    b = idx
    rel = b[:, None] < b[None, :]
    for k in range(C):
        rel &= chiV[idx][:, None, k] <= chiV[idx][None, :, k]
    np.fill_diagonal(rel, False)
    return rel

def find_sk(rel, rng, k, tries=20000):
    """openings_pass.find_s4, generic k, bucket step vectorized;
    RNG-equivalent to the original at k = 4 (same permutation, same
    buckets, same 60-draw B sampling); first witness returns."""
    n = rel.shape[0]
    comp = rel | rel.T
    nodes = np.arange(n)
    for _ in range(tries):
        perm = rng.permutation(n)
        A = []
        for v in perm:
            if not A or not comp[v, A].any():
                A.append(int(v))
                if len(A) == k:
                    break
        if len(A) < k:
            continue
        Aa = np.array(A)
        mask = np.ones(n, dtype=bool)
        mask[Aa] = False
        others = nodes[mask]
        above = rel[np.ix_(Aa, others)]          # above[i, j]: A[i] < b_j
        cand = above.sum(0) == k - 1
        if not cand.any():
            continue
        cnodes = others[cand]
        miss = np.argmin(above[:, cand], axis=0)  # the one missing a
        keep = ~comp[Aa[miss], cnodes]            # incomparable to it
        buckets = [cnodes[keep & (miss == i)] for i in range(k)]
        if any(len(bk) == 0 for bk in buckets):
            continue
        for _ in range(60):
            B = [int(bk[int(rng.integers(len(bk)))]) for bk in buckets]
            if len(set(B)) == k and not any(
                    comp[B[i], B[j]]
                    for i in range(k) for j in range(i + 1, k)):
                return A, B
    return None

def verify_sk(rel, A, B, k):
    """The full induced-S_k standard-example pattern, asserted against
    the relation matrix: A antichain, B antichain, a_i < b_j iff
    i != j (and never b_j < a_i), a_i incomparable b_i."""
    for i in range(k):
        for j in range(k):
            if i != j and (rel[A[i], A[j]] or rel[B[i], B[j]]):
                return False
            if bool(rel[A[i], B[j]]) != (i != j):
                return False
            if rel[B[j], A[i]]:
                return False
        if rel[A[i], B[i]] or rel[B[i], A[i]]:
            return False
    return True

print("[dimwall witness: the S_{C+1} certification, receipt-carried]")
SR = np.random.default_rng(20261440)
TRIES = 20000

# ---- W1: the searcher validation ----
pos4 = 0
for j in range(5):
    rel = orthant_rel(np.random.default_rng(700 + j), 128, 4)
    res = find_sk(rel, SR, 4, TRIES)
    if res is not None:
        assert verify_sk(rel, *res, 4), "witness failed re-verification"
        print(f"      S4 4-orthant seed {700 + j}: a = {res[0]}, "
              f"b = {res[1]} (re-verified)")
        pos4 += 1
check("W1a: S4 found in iid 4-orthant", pos4 == 5, f"{pos4}/5")

neg3 = sum(1 for j in range(5)
           if find_sk(orthant_rel(np.random.default_rng(800 + j), 128, 3),
                      SR, 4, TRIES) is not None)
check("W1b: S4 absent on iid 3-orthant (dim <= 3, theorem)", neg3 == 0,
      f"{neg3}/5")

c2s4 = 0
for j in range(5):
    chiV, r2 = web_chiv(20261420 + j, 2)
    for _ in range(2):
        idx = np.sort(r2.choice(np.arange(768, 1280), 128, replace=False))
        if find_sk(rel_win(idx, chiV, 2), SR, 4, TRIES) is not None:
            c2s4 += 1
check("W1c: S4 absent on C = 2 windows (dim <= 3, weak Lemma)", c2s4 == 0,
      f"{c2s4}/10")

pos3 = 0
for j in range(5):
    rel = orthant_rel(np.random.default_rng(800 + j), 128, 3)
    res = find_sk(rel, SR, 3, TRIES)
    if res is not None:
        assert verify_sk(rel, *res, 3), "witness failed re-verification"
        print(f"      S3 3-orthant seed {800 + j}: a = {res[0]}, "
              f"b = {res[1]} (re-verified)")
        pos3 += 1
check("W1d: S3 found in iid 3-orthant", pos3 == 5, f"{pos3}/5")

neg2 = sum(1 for j in range(5)
           if find_sk(orthant_rel(np.random.default_rng(900 + j), 128, 2),
                      SR, 3, TRIES) is not None)
check("W1e: S3 absent on iid 2-orthant (dim <= 2, theorem)", neg2 == 0,
      f"{neg2}/5")

searcher_ok = (pos4 == 5 and neg3 == 0 and c2s4 == 0 and pos3 == 5
               and neg2 == 0)

# ---- W2: the certification (pinned seeds; tries frozen; <= 6 draws) ----
def certify(C, k, label):
    hits = 0
    for sd in range(20260960, 20260965):
        chiV, r2 = web_chiv(sd, C)
        got = False
        for draw in range(6):
            idx = np.sort(r2.choice(np.arange(768, 1280), 128,
                                    replace=False))
            rel = rel_win(idx, chiV, C)
            res = find_sk(rel, SR, k, TRIES)
            if res is not None:
                A, B = res
                assert verify_sk(rel, A, B, k), \
                    "witness failed re-verification"
                print(f"      {label} seed {sd} draw {draw}: "
                      f"a = {[int(idx[a]) for a in A]}, "
                      f"b = {[int(idx[b]) for b in B]} "
                      f"(commit indices; re-verified)")
                got = True
                break
        if got:
            hits += 1
        else:
            print(f"      {label} seed {sd}: NO witness in 6 draws at "
                  f"tries = {TRIES} (refusal recorded; tries frozen)")
    return hits

s4h = certify(3, 4, "S4 (C = 3)")
check("W2a: S4 witnesses in Delta = 512 windows of the pinned C = 3 seeds",
      s4h == 5, f"{s4h}/5")
s3h = certify(2, 3, "S3 (C = 2)")
check("W2b: S3 witnesses in the pinned seeds' C = 2 windows",
      s3h == 5, f"{s3h}/5")

print()
if searcher_ok and s4h == 5 and s3h == 5:
    print("WITNESS CERTIFICATION: CERTIFIED — searcher validated with zero "
          "false positives (S4 and S3); S4 on 5/5 pinned C = 3 seeds; S3 "
          "on 5/5 C = 2 — the S_{C+1} lower bound is receipt-carried")
else:
    print(f"WITNESS CERTIFICATION: REFUSED — validation "
          f"{'held' if searcher_ok else 'FAILED'}; S4 {s4h}/5; S3 {s3h}/5")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0
      else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)
