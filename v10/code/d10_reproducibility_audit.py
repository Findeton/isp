#!/usr/bin/env python3
"""Run every D10 executable normally and with -O; require identical output."""

from hashlib import sha256
from pathlib import Path
from subprocess import check_output
from sys import executable


HERE = Path(__file__).resolve().parent
SCRIPTS = (
    HERE / "d10_bloch_lorentz_exact.py",
    HERE / "d10_finite_clock_convergence.py",
    HERE / "d10_relational_scir_packet.py",
)
EXPECTED_STDOUT_SHA256 = {
    "d10_bloch_lorentz_exact.py": "a05b84aa0a94a4a3086c190045fc56e96eb0fde6a00c179073a23944bbebcd5f",
    "d10_finite_clock_convergence.py": "f2e8c45e1a224e4f84ebfdd5a11e9973266879723443508d9f04539fdaa3be27",
    "d10_relational_scir_packet.py": "b5827de1d703ab492563fb1b981a41da477a1627943215ffe4ce660d0feb65eb",
}

rows = []
for script in SCRIPTS:
    normal = check_output([executable, str(script)])
    optimized = check_output([executable, "-O", str(script)])
    if normal != optimized:
        raise AssertionError(f"normal/-O output differs for {script.name}")
    digest = sha256(normal).hexdigest()
    if digest != EXPECTED_STDOUT_SHA256[script.name]:
        raise AssertionError(f"frozen stdout hash mismatch for {script.name}: {digest}")
    rows.append((script.name, len(normal), digest))

print("D10 REPRODUCIBILITY AUDIT")
print(f"scripts={len(rows)}")
print("normal_optimized=BYTE_IDENTICAL")
print("frozen_stdout_hashes=PASS")
for name, size, digest in rows:
    print(f"{name} bytes={size} stdout_sha256={digest}")
summary = "\n".join(f"{name}:{size}:{digest}" for name, size, digest in rows)
print("audit_sha256=" + sha256(summary.encode()).hexdigest())
