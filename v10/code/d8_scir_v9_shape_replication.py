#!/usr/bin/env python3
"""Fresh 24-seed strict-shape replication of the pinned V9 diffusion builder.

The V9 source is read-only, hash-gated, and executed with only its frozen seed
range replaced. The legacy two-check verdict is ignored; this wrapper computes
the stricter two-convention t-style threshold requested by the V9 review.

Run with the bundled workspace Python because the frozen V9 source uses numpy.
"""

from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
from statistics import fmean, stdev


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "v9" / "code" / "dimwall_diffusion_d.py"
EXPECTED_SHA256 = "aff9525110f6fd209332badccf1a5353c011be9eb8461a4db50063bf0670d81a"
OLD = "range(20264500, 20264510)"
NEW = "range(20268000, 20268024)"

source_bytes = SOURCE.read_bytes()
assert sha256(source_bytes).hexdigest() == EXPECTED_SHA256
source = source_bytes.decode("utf-8")
assert source.count(OLD) == 1
source = source.replace(OLD, NEW)

namespace = {"__name__": "__main__", "__file__": str(SOURCE)}
captured_out = StringIO()
captured_err = StringIO()
with redirect_stdout(captured_out), redirect_stderr(captured_err):
    exec(compile(source, str(SOURCE), "exec"), namespace)

fd = [float(x) for x in namespace["Fd"]]
fm = [float(x) for x in namespace["Fm"]]
wf = [float(x) for x in namespace["wf"]]
assert len(fd) == len(fm) == len(wf) == 24


def mean_se(values):
    return fmean(values), stdev(values) / len(values) ** 0.5


fd_mean, fd_se = mean_se(fd)
fm_mean, fm_se = mean_se(fm)
t_dom = (fd_mean - 1.236) / fd_se
t_m4 = (fm_mean - 1.212) / fm_se
strict_shape = t_dom <= -2.33 and t_m4 <= -2.33
d_pinned = namespace["d_of"](fmean(wf))
rf = int(namespace["rf"])
s4c = int(namespace["s4c"])

# The old code's volume estimator was found nonstationary/instrument-suspect;
# it is printed but deliberately excluded from this wrapper's grade.
assert rf >= 20
assert s4c >= 8

print("D8 SCIR / V9 DIFFUSION 24-SEED REPLICATION")
print(f"source_sha256={EXPECTED_SHA256}")
print(f"fresh_seeds={NEW}")
print(f"F_dom={fd_mean:.12f} se={fd_se:.12f} t={t_dom:+.6f}")
print(f"F_m4={fm_mean:.12f} se={fm_se:.12f} t={t_m4:+.6f}")
print(f"strict_shape_bar=-2.33 both_conventions")
print(f"strict_shape_pass={strict_shape}")
print(f"d_pinned_instrument_suspect={d_pinned:.12f}")
print(f"dimension_refusals={rf}/24")
print(f"S4_witnesses={s4c}/24")
payload = "|".join([
    EXPECTED_SHA256, NEW, f"{fd_mean:.15f}", f"{fd_se:.15f}",
    f"{fm_mean:.15f}", f"{fm_se:.15f}", str(strict_shape),
    f"{d_pinned:.15f}", str(rf), str(s4c),
])
print(f"receipt_sha256={sha256(payload.encode('ascii')).hexdigest()}")

