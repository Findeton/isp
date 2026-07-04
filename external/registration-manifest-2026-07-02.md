# Registration manifest — third-party timestamping bundle (prepared 2026-07-02)

**Purpose.** The two registered-prediction documents below have so far been
registered *locally only* ("internal discipline only; not posted or submitted
anywhere"). For the registrations to carry evidential weight against JUNO's
future releases, they need a third-party timestamp **before** the relevant data
lands. This manifest freezes the exact file states and lists the deposit steps.
**Nothing has been deposited by this manifest** — depositing is the (user)
action item; this file only prepares it.

## The frozen files (SHA-256, states as of 2026-07-02)

| file | sha256 |
|---|---|
| `registered-prediction-neutrino-step.md` | `c3ec9c2656df2e32a9b4ab7e68872d5019331689336d4f361b668faa0aed2b48` |
| `registered-prediction-lepton-mixing-cp.md` | `2bb105f73497804a26889e311f8a86a36c8bdca1d3b2d4dad406e41d8a12ce66` |

Re-verify at any time with:
`shasum -a 256 registered-prediction-neutrino-step.md registered-prediction-lepton-mixing-cp.md`

**Content notes carried with the freeze (honesty guards, from the files
themselves):** the neutrino-step document's registered claim is the *undressed*
spectrum point, exact evaluation `S = 0.1754721` (the ≥ 10-digit-ε rule of its
Precision Note 4); JUNO first data (59.1 days, arXiv:2511.14593) is already
reflected in its status updates, so the timestamp protects the claim against
*future* JUNO releases, not the first one; the dressed-base observation is a
post-diction with counted look-elsewhere cost, registered as derivation target
O35.1 only. The lepton-mixing document carries its own 2026-06-11 withdrawals
(P-MIX and P-CPV are WITHDRAWN as mechanism-derived claims) — the deposit must
include the withdrawal text, not a cleaned version: the registration's value is
its honesty trail.

## Deposit steps (user action; either or both routes)

1. **Zenodo** (fastest, DOI-issuing): create a deposition titled "SHARD
   registered predictions — neutrino-sector fingerprint (frozen 2026-07-02)";
   upload the two `.md` files byte-exact + this manifest; license CC-BY-4.0 (or
   restricted with open metadata — the *timestamp* is what matters); publish →
   DOI + immutable datetime.
2. **arXiv** (slower, needs an endorsable category): bundle as ancillary files
   of a short registration note (physics.data-an or hep-ph); the arXiv v1
   datetime is the timestamp.
3. After deposit: record the DOI/identifier + datetime in this file and in
   `v8/LEDGER.md` (a one-line addendum to the paper-10 status line), and do NOT
   edit the two prediction files again — subsequent updates go in new files that
   cite the frozen ones.

## Why now

JUNO's oscillation-parameter precision improves with exposure; every month
without a third-party timestamp is a month in which the registration's
evidential value decays toward a post-diction. The corpus's own empirical
bottom line (v8 paper 6 §4) names the neutrino-sector fingerprint as the one
surviving narrow face — this bundle is the cheapest action that protects it.
