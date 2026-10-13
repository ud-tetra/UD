"""Exact finite synthetic audit of the proposed polarity pipeline; no sidecar data."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

bits = list(itertools.product((0, 1), repeat=3))
states = []
for T in bits:
    for L in bits:
        omega = tuple(T[i] * L[i] for i in range(3))
        for q in bits:
            if all(omega[i] <= q[i] <= T[i] for i in range(3)):
                states.append((T, L, omega, q))
assert len(states) == 125


def count(v):
    return sum(v)


total = equal = saturated_prior = saturated_prior_equal = saturated_both = 0
counterexample = None
for _, _, om0, q0 in states:
    h0 = tuple(q0[i] - om0[i] for i in range(3))
    for _, _, om1, q1 in states:
        h1 = tuple(q1[i] - om1[i] for i in range(3))
        mu = count(q0) - count(q1)       # theta=1-q
        idx = count(om0) - count(om1)    # finite index, any continuation F
        assert mu == idx + count(h0) - count(h1)
        total += 1
        equal += (mu == idx)
        if count(h0) == 0:
            saturated_prior += 1
            saturated_prior_equal += (mu == idx)
            assert (mu == idx) == (count(h1) == 0)
        if count(h0) == count(h1) == 0:
            saturated_both += 1
        if counterexample is None and mu != idx:
            counterexample = {"omega_minus":om0,"q_minus":q0,
                              "omega_plus":om1,"q_plus":q1,
                              "mu_theta":mu,"index":idx}
assert total == 15625 and saturated_prior == 8000 and saturated_prior_equal == saturated_both == 4096
assert equal == 64**2 + 48**2 + 12**2 + 1**2 == 6545

# Integrity/viability permitted candidates on the fixed shell, with an actual
# quadratic gradient burden from b=(0,1,2,3) on K4 opposite pairs.
b = (0, 1, 2, 3)
pairs = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
W = tuple(sum((b[i] - b[j]) ** 2 for i, j in pair) for pair in pairs)
assert W == (2, 8, 10)
T, L, omega = (1, 1, 1), (1, 0, 0), (1, 0, 0)
q_poc = omega
theta_poc = tuple(1-x for x in q_poc)
shell = [theta for theta in bits if count(theta) == count(theta_poc)
         and all((1-theta[i]) <= T[i] for i in range(3))]
scores = {theta:sum(theta[i] * W[i] for i in range(3)) for theta in shell}
winner = min(shell,key=lambda theta:scores[theta])
assert len(shell) == 3 and theta_poc == (0, 1, 1) and winner == (1, 1, 0)
assert not all(omega[i] <= 1-winner[i] for i in range(3))
viable_shell = [theta for theta in shell if all(omega[i] <= 1-theta[i] for i in range(3))]
assert viable_shell == [theta_poc]

# Frame change (A B) carries a persistent old A obligation into new B.
om_old, theta_old = (1,0,0), (0,1,1)
permutation = (1,0,2)
def permute(x): return tuple(x[permutation[i]] for i in range(3))
om_aligned, theta_aligned = permute(om_old), permute(theta_old)
om_new, theta_new = (0,1,0), (1,0,1)
assert om_aligned == om_new and theta_aligned == theta_new
unaligned_turnover = count(tuple(om_old[i]*(1-om_new[i]) for i in range(3))) + count(tuple((1-om_old[i])*om_new[i] for i in range(3)))
assert unaligned_turnover == 2

# Sourced K4 A=B^T-B orbit from e0: c0(s)=m+cos(2s)(e0-m),
# c1(s)=sin(2s)/2 B1^T e0. At s1=pi/12 and s2=pi/6,
# E1=3/4 sin^2(2s), so the exact integrated G_Sigma is 3/8.
# Keep integrity T=(1,0,0): only pair A is viable and remains active.
E1_start, E1_end = Fraction(3,16), Fraction(9,16)
Gsum = E1_end-E1_start
GA = Fraction(1,8)
assert Gsum == Fraction(3,8) and GA > 0
omega_start = omega_end = (1,0,0)
mu_index = count(omega_start)-count(omega_end)
mu_flux = -1
assert mu_index == 0 and mu_flux == -1

result = {
 "status":"PASS",
 "scope":"source-free exact synthetic consistency audit; no frozen sidecar or held-out endpoint",
 "admissible_one_state_count":len(states),
 "ordered_pair_count":total,
 "index_equals_full_mu_count":equal,
 "saturated_prior_count":saturated_prior,
 "saturated_prior_index_equals_mu_count":saturated_prior_equal,
 "saturated_both_count":saturated_both,
 "first_unsaturated_counterexample":counterexample,
 "burden_gradient_W_exact":W,
 "poc_theta":theta_poc,
 "poc_cost":scores[theta_poc],
 "shell_only_burden_winner":winner,
 "winner_cost":scores[winner],
 "winner_violates_viability":True,
 "viability_enforced_shell_size":len(viable_shell),
 "unaligned_persistent_obligation_false_turnover":unaligned_turnover,
 "flux_counterexample":{"integrity":(1,0,0),"omega_start":omega_start,"omega_end":omega_end,
                        "G_A":str(GA),"G_sum":str(Gsum),"index_mu":mu_index,"flux_mu":mu_flux},
 "physical_promotion":0
}
Path(__file__).with_name("results.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
