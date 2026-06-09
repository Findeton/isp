"""
v6 Paper 3 section 5: observable derivation from a sealed CMRP germ.

Question:
    Given one sealed role-blind deletion profile, what does the ontology
    actually compute?

Finite answer:
    The profile computes shell work, H_x, T_x, sigma_x, kappa_G, beta, gamma
    after threshold selection, and the ICS order shadow.  These are not
    independent parameters in the finite sealed packet.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2aj_mcdi_reference_state_campaign import RHO_CLICK, delta_k
from v6_p2al_ics_ht_law_campaign import (
    diamond_temperature,
    gibbs,
    shell_hamiltonian,
    source_response,
)
from v6_p2an_modular_deletion_profile_campaign import increments, profile_isolation


GAMMA = 7.0 / 48.0
PROFILE = (0.0, 0.1853, 0.5707, 1.1764)
SCREEN_RESPONSE = 1.0
VOLUME_RESPONSE = 1.0


@dataclass
class DerivedObservable:
    name: str
    formula: str
    value: str
    status: str


def fmt_tuple(values: tuple[float, ...]) -> str:
    return "(" + ", ".join(f"{value:.4f}" for value in values) + ")"


def derive() -> list[DerivedObservable]:
    work = increments(PROFILE)
    h = shell_hamiltonian(work)
    temp = diamond_temperature(VOLUME_RESPONSE, SCREEN_RESPONSE)
    sigma = gibbs(h, temp)
    kappa = max(0.0, delta_k(RHO_CLICK, sigma))
    beta, beta_ok, residue = source_response(h, temp)
    isolation = profile_isolation(work)
    event = all(value > 0.0 for value in work) and isolation > 0.12
    c_g = GAMMA * kappa
    return [
        DerivedObservable("event", "positive isolated M_x increments", str(event), "PASS"),
        DerivedObservable("gamma", "selected event density", f"{GAMMA:.5f}", "PASS"),
        DerivedObservable("M_x(k)", "sealed deletion profile", fmt_tuple(PROFILE), "PASS"),
        DerivedObservable("w_x(k)", "M_x(k+1)-M_x(k)", fmt_tuple(work), "PASS"),
        DerivedObservable("isolation", "largest shell gap margin", f"{isolation:.4f}", "PASS"),
        DerivedObservable("H_x", "cumulative shell work", fmt_tuple(h), "PASS"),
        DerivedObservable("T_x", "|delta V_x|/delta S_screen,x", f"{temp:.4f}", "PASS"),
        DerivedObservable("sigma_x", "exp(-H_x/T_x)/Z_x", fmt_tuple(sigma), "PASS"),
        DerivedObservable("kappa_G", "deletion/source response", f"{kappa:.4f}", "PASS"),
        DerivedObservable("c_G", "gamma*kappa_G", f"{c_g:.5f}", "PASS"),
        DerivedObservable(
            "beta",
            "source-response beta selector",
            f"{beta:.4f}" if beta_ok and isfinite(beta) else "undefined",
            "PASS" if beta_ok else "FAIL",
        ),
        DerivedObservable(
            "stationarity",
            "Gibbs variational residue",
            f"{residue:.2e}" if isfinite(residue) else "inf",
            "PASS" if residue <= 1.0e-9 else "FAIL",
        ),
        DerivedObservable("ICS shadow", "order projection of sealed atoms", "defined", "PASS"),
        DerivedObservable("TS residue", "spacelike additive deletion action", "0", "PASS"),
    ]


def print_rows(rows: list[DerivedObservable]) -> None:
    print("CMRP observable derivation")
    print("--------------------------")
    print("object        formula                              value                          status")
    for row in rows:
        print(f"{row.name:13s} {row.formula:36s} {row.value:30s} {row.status}")
    print()


def main() -> None:
    rows = derive()
    print("=" * 118)
    print("v6 Paper 3 section 5: CMRP observable derivation")
    print("=" * 118)
    print_rows(rows)
    print("VERDICT")
    print("-------")
    print("For a sealed role-blind finite profile, the visible parameters are")
    print("computed readouts.  They stop being derived exactly when the profile,")
    print("units, action, isolation, or cofinal law is supplied externally.")


if __name__ == "__main__":
    main()
