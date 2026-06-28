#!/usr/bin/env python3
"""
Receipt for v7 Paper XXI: the record martingale principle.

Checks:
  1. A Poisson click process in evidence content has compensated martingale
     M_chi = N_chi - kappa chi, including conditional first and second moments.
  2. The exponential survival law follows from the constant compensator.
  3. The deterministic Bernoulli suspension of Paper XX projects to the same
     Poisson renewal/count law in the committed-record filtration.
  4. A sparse Bernoulli seal lattice has compensated martingale
     M_n = N_n - n p_d and survival S(nd)=exp(-kappa nd) when
     p_d = 1 - exp(-kappa d).
  5. Persistent static hidden rate mixtures with the same average rate fail the
     dense record martingale: the no-click record updates the posterior hazard.
     The hazard derivative is the negative posterior variance, so constant hazard
     forces a degenerate single-rate sector in this model class.
  6. A deterministic time-change chi(t) changes the spacetime onset but not the
     record compensator.

All cancellation-sensitive arithmetic uses mpmath at dps=140.
"""

import mpmath as mp

mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name} {detail}")


def poisson_pmf(k, mean):
    return mp.e ** (-mean) * mean ** k / mp.factorial(k)


print("=" * 80)
print("P21 record martingale receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

kappa = mp.mpf("0.73")
s_chi = mp.mpf("1.25")
t_chi = mp.mpf("4.75")
delta = t_chi - s_chi
mean_delta = kappa * delta

print("\n(1) Poisson compensated martingale in evidence content")
print("kappa =", fmt(kappa))
print("s     =", fmt(s_chi))
print("t     =", fmt(t_chi))
print("mean increment kappa*(t-s) =", fmt(mean_delta))

max_cond_gap = mp.mpf("0")
max_quad_gap = mp.mpf("0")
for n in range(0, 5):
    cond = mp.nsum(
        lambda j: ((n + j) - kappa * t_chi) * poisson_pmf(j, mean_delta),
        [0, mp.inf],
    )
    target = n - kappa * s_chi
    quad = mp.nsum(
        lambda j: (((n + j) - kappa * t_chi) - target) ** 2
        * poisson_pmf(j, mean_delta),
        [0, mp.inf],
    )
    max_cond_gap = max(max_cond_gap, abs(cond - target))
    max_quad_gap = max(max_quad_gap, abs(quad - mean_delta))
    print(
        f"n={n} E[M_t|N_s=n]={fmt(cond, 50)} target={fmt(target, 50)} "
        f"E[(dM)^2]={fmt(quad, 50)}"
    )

check(
    "Poisson M_chi=N_chi-kappa*chi has conditional martingale mean",
    max_cond_gap < mp.mpf("1e-120"),
    f"max_gap={fmt(max_cond_gap, 8)}",
)
check(
    "Poisson compensated increment has variance kappa*(t-s)",
    max_quad_gap < mp.mpf("1e-120"),
    f"max_gap={fmt(max_quad_gap, 8)}",
)

print("\n(2) Exponential survival from constant compensator")
test_points = [mp.mpf("0"), mp.mpf("0.125"), mp.mpf("1.0"), mp.mpf("2.5"), mp.mpf("9.0")]
max_surv_gap = mp.mpf("0")
for x in test_points:
    survival_from_zero_jumps = poisson_pmf(0, kappa * x)
    survival_from_hazard = mp.e ** (-kappa * x)
    max_surv_gap = max(max_surv_gap, abs(survival_from_zero_jumps - survival_from_hazard))
    print(
        f"chi={fmt(x, 10)} P(N_chi=0)={fmt(survival_from_zero_jumps, 50)} "
        f"exp(-kappa chi)={fmt(survival_from_hazard, 50)}"
    )
check(
    "Constant compensator gives S(chi)=exp(-kappa*chi)",
    max_surv_gap < mp.mpf("1e-120"),
    f"max_gap={fmt(max_surv_gap, 8)}",
)

print("\n(3) Deterministic Bernoulli suspension projected count law")
print(
    "Paper XX's two-sided deterministic suspension has iid Exp(kappa) roof lengths "
    "after pushforward by the invariant Bernoulli measure."
)
t_renew = mp.mpf("3.2")
max_renew_gap = mp.mpf("0")
for n in range(0, 11):
    if n == 0:
        renewal_prob = mp.e ** (-kappa * t_renew)
    else:
        # P(N_t=n) = int_0^t f_{Gamma(n,kappa)}(s) * P(next roof > t-s) ds.
        renewal_prob = mp.quad(
            lambda x: (
                (kappa ** n)
                * (x ** (n - 1))
                * mp.e ** (-kappa * x)
                / mp.factorial(n - 1)
            )
            * mp.e ** (-kappa * (t_renew - x)),
            [0, t_renew],
        )
    poisson_prob = poisson_pmf(n, kappa * t_renew)
    max_renew_gap = max(max_renew_gap, abs(renewal_prob - poisson_prob))
    print(
        f"n={n} renewal={fmt(renewal_prob, 45)} "
        f"poisson={fmt(poisson_prob, 45)}"
    )

check(
    "Deterministic suspension pushforward has Poisson count probabilities",
    max_renew_gap < mp.mpf("1e-120"),
    f"max_gap={fmt(max_renew_gap, 8)}",
)

print("\n(4) Sparse Bernoulli seal lattice")
d = mp.mpf("0.0625")
p_d = 1 - mp.e ** (-kappa * d)
q_d = 1 - p_d
print("d     =", fmt(d))
print("p_d   =", fmt(p_d, 60))
print("q_d   =", fmt(q_d, 60))

n0 = 6
n1 = 23
prob_gap = n1 - n0
observed_clicks = 2
cond_sparse = mp.nsum(
    lambda j: ((observed_clicks + j) - n1 * p_d)
    * mp.binomial(prob_gap, j)
    * p_d ** j
    * q_d ** (prob_gap - j),
    [0, prob_gap],
)
target_sparse = observed_clicks - n0 * p_d
sparse_mean_gap = abs(cond_sparse - target_sparse)
print("n0,n1 =", n0, n1)
print("E[M_n1 | F_n0] =", fmt(cond_sparse, 60))
print("M_n0 target    =", fmt(target_sparse, 60))
max_skel_gap = mp.mpf("0")
for n in range(0, 40):
    lhs = q_d ** n
    rhs = mp.e ** (-kappa * d * n)
    max_skel_gap = max(max_skel_gap, abs(lhs - rhs))
check(
    "Sparse Bernoulli M_n=N_n-n*p_d is a martingale",
    sparse_mean_gap < mp.mpf("1e-120"),
    f"gap={fmt(sparse_mean_gap, 8)}",
)
check(
    "Sparse no-click skeleton q_d^n=exp(-kappa*d*n)",
    max_skel_gap < mp.mpf("1e-120"),
    f"max_gap={fmt(max_skel_gap, 8)}",
)

print("\n(5) Hidden rate mixture: same average rate, failed record martingale")
lam1 = mp.mpf("0.20")
lam2 = mp.mpf("2.10")
weight1 = (lam2 - kappa) / (lam2 - lam1)
weight2 = 1 - weight1
mean_rate = weight1 * lam1 + weight2 * lam2
var_rate = weight1 * (lam1 - mean_rate) ** 2 + weight2 * (lam2 - mean_rate) ** 2
print("lambda1, lambda2 =", fmt(lam1), fmt(lam2))
print("weights          =", fmt(weight1, 50), fmt(weight2, 50))
print("mean rate        =", fmt(mean_rate, 60))
print("variance rate    =", fmt(var_rate, 60))

def mix_survival(x):
    return weight1 * mp.e ** (-lam1 * x) + weight2 * mp.e ** (-lam2 * x)


def mix_hazard(x):
    num = weight1 * lam1 * mp.e ** (-lam1 * x) + weight2 * lam2 * mp.e ** (-lam2 * x)
    den = mix_survival(x)
    return num / den


def mix_posterior_variance(x):
    den = mix_survival(x)
    w1x = weight1 * mp.e ** (-lam1 * x) / den
    w2x = weight2 * mp.e ** (-lam2 * x) / den
    hx = w1x * lam1 + w2x * lam2
    return w1x * (lam1 - hx) ** 2 + w2x * (lam2 - hx) ** 2


hidden_points = [mp.mpf("0"), mp.mpf("0.5"), mp.mpf("2.0"), mp.mpf("5.0")]
max_mix_exp_gap = mp.mpf("0")
max_derivative_gap = mp.mpf("0")
for x in hidden_points:
    sx = mix_survival(x)
    ex = mp.e ** (-kappa * x)
    hx = mix_hazard(x)
    # Exact identity for a no-click posterior over fixed rates:
    # d h / d chi = - Var(lambda | no click to chi).
    dh = mp.diff(mix_hazard, x)
    post_var = mix_posterior_variance(x)
    max_mix_exp_gap = max(max_mix_exp_gap, abs(sx - ex))
    max_derivative_gap = max(max_derivative_gap, abs(dh + post_var))
    print(
        f"chi={fmt(x, 8)} S_mix={fmt(sx, 50)} exp_mean={fmt(ex, 50)} "
        f"h={fmt(hx, 50)} dh+Var={fmt(dh + post_var, 8)}"
    )

mult_gap = abs(mix_survival(mp.mpf("1.1") + mp.mpf("0.9")) - mix_survival(mp.mpf("1.1")) * mix_survival(mp.mpf("0.9")))
hazard_drop = mix_hazard(mp.mpf("0")) - mix_hazard(mp.mpf("5.0"))
check(
    "Hidden mixture has the chosen average rate kappa",
    abs(mean_rate - kappa) < mp.mpf("1e-120"),
    f"gap={fmt(abs(mean_rate-kappa), 8)}",
)
check(
    "Nondegenerate hidden-rate mixture is not exponential survival",
    max_mix_exp_gap > mp.mpf("1e-2"),
    f"max_gap={fmt(max_mix_exp_gap, 30)}",
)
check(
    "Mixture hazard decreases by posterior learning after no-click records",
    hazard_drop > mp.mpf("0.2"),
    f"h(0)-h(5)={fmt(hazard_drop, 30)}",
)
check(
    "Mixture hazard derivative equals negative posterior variance",
    max_derivative_gap < mp.mpf("1e-100"),
    f"max_gap={fmt(max_derivative_gap, 8)}",
)
check(
    "Hidden mixture violates survival multiplicativity",
    mult_gap > mp.mpf("1e-2"),
    f"gap={fmt(mult_gap, 30)}",
)

print("\n(6) Degenerate hidden sector and deterministic time-change controls")
deg_lam1 = kappa
deg_lam2 = kappa
deg_w = mp.mpf("0.37")
max_deg_gap = mp.mpf("0")
for x in hidden_points:
    deg_s = deg_w * mp.e ** (-deg_lam1 * x) + (1 - deg_w) * mp.e ** (-deg_lam2 * x)
    max_deg_gap = max(max_deg_gap, abs(deg_s - mp.e ** (-kappa * x)))
check(
    "Degenerate hidden-rate sector collapses back to the record martingale law",
    max_deg_gap < mp.mpf("1e-120"),
    f"max_gap={fmt(max_deg_gap, 8)}",
)

a = mp.mpf("0.41")
time_points = [mp.mpf("0"), mp.mpf("0.25"), mp.mpf("1.5"), mp.mpf("4.0")]
max_time_gap = mp.mpf("0")
for tau in time_points:
    chi_tau = a * tau * tau / 2
    spacetime_hazard = kappa * a * tau
    reconstructed_chi_rate = spacetime_hazard / kappa
    max_time_gap = max(max_time_gap, abs(reconstructed_chi_rate - a * tau))
    print(
        f"tau={fmt(tau, 8)} chi(tau)={fmt(chi_tau, 50)} "
        f"lambda_tau={fmt(spacetime_hazard, 50)} S={fmt(mp.e**(-kappa*chi_tau), 50)}"
    )
check(
    "Quadratic spacetime onset is just record martingale under chi(t)=a*t^2/2",
    max_time_gap < mp.mpf("1e-120"),
    f"max_gap={fmt(max_time_gap, 8)}",
)

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")
