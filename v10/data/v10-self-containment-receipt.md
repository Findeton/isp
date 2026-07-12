# V10 code self-containment receipt

**Updated through D10:** 2026-07-11

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/v10_self_containment_audit.py
```

Result:

```text
PASS: all v10 investigation executables reside in v10/code
PASS: no duplicate investigation source exists outside v10/code
PASS: exact/core executables are standard-library only; declared D9 numerical instruments use bundled numpy
PASS: no .pyc cache artifact exists under v10
RECEIPT: 4/4 self-containment checks passed
```

Audit source hash:

```text
743b8d93c3baad99981db20e3133cdf36b4fe58486584161205609b4ec5381db  v10/code/v10_self_containment_audit.py
```

Canonical stdout hash:

```text
e2a54d2b8b0b7e442797324080f7bbc63fc4c8ebcdb4c9b9df06214e5c0894f8  audit stdout
```

The audit's source manifest covers every D1–D10 investigation executable in
`v10/code/`. D1–D8 exact/core and all D10 programs require no `.env`, `.venv`,
external source tree, or third-party package. The two declared D9 geometry
instruments use bundled `numpy`; their dependency exception is explicit in the
audit rather than hidden outside `v10`.
