"""Exact conditional factor-state nonidentifiability on the two-tet register."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json

cells = ((0, 1, 2, 3), (0, 1, 2, 4))
levels = [tuple(sorted({s for c in cells for s in combinations(c, k)})) for k in (1, 2, 3, 4)]
flat = sum((list(level) for level in levels), [])
index = {s: i for i, s in enumerate(flat)}
links = []
for high in flat:
    if len(high) < 2:
        continue
    for j in range(len(high)):
        low = high[:j] + high[j + 1:]
        links.append((index[low], index[high], F((-1) ** j), low, high))
n = len(flat)
edge = (0, 1)


def masks(closure, transport):
    # Q156 product; all other edges and all faces are held open in this test.
    return {e: (closure * transport if e == edge else 1) for e in levels[1]}


def generator(edge_masks):
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, j, b, low, high in links:
        weight = edge_masks[high] if len(low) == 1 else 1
        a[j][i] += b * weight
        a[i][j] -= b * weight
    return a


def act(a, c):
    return [sum(x * y for x, y in zip(row, c)) for row in a]


def jets(a, c, order):
    out = [c]
    for _ in range(order):
        out.append(act(a, out[-1]))
    return out


def current_jets(amplitudes, order):
    # Q166 polynomial directed incidence currents, including degrees 01/12/23.
    return [[2 * b * sum(F(comb(k, r)) * amplitudes[r][i] * amplitudes[k-r][j]
                          for r in range(k+1))
             for i, j, b, _, _ in links] for k in range(order+1)]


checks = {}
def check(name, value):
    checks[name] = bool(value)
    assert value, name

check('register_5_9_7_2', [len(v) for v in levels] == [5, 9, 7, 2])
check('47_native_incidences', len(links) == 47)

# Distinct lawful-looking factor preparations with identical hard product 0.
state_a = (0, 1)
state_b = (0, 0)
pre_a = generator(masks(*state_a))
pre_b = generator(masks(*state_b))
check('distinct_factor_states_same_hard_mask', state_a != state_b and masks(*state_a) == masks(*state_b))
check('identical_pre_event_generator', pre_a == pre_b)
check('skew_pre_event_generator', all(pre_a[i][j] == -pre_a[j][i] for i in range(n) for j in range(n)))

c = [F(0)] * n
c[index[(0,)]] = F(1)
c[index[edge]] = F(1)
pre_jets_a, pre_jets_b = jets(pre_a, c, 8), jets(pre_b, c, 8)
check('all_replayed_amplitude_jets_0_through_8_equal', pre_jets_a == pre_jets_b)
check('all_replayed_native_current_jets_0_through_5_equal',
      current_jets(pre_jets_a, 5) == current_jets(pre_jets_b, 5))

# A declared diagnostic intervention, not an admitted UD event law.
post_a = (1, state_a[1])
post_b = (1, state_b[1])
check('same_closure_repair_divergent_hard_masks',
      masks(*post_a)[edge] == 1 and masks(*post_b)[edge] == 0)
da = act(generator(masks(*post_a)), c)
db = act(generator(masks(*post_b)), c)
check('post_repair_edge_derivatives_diverge', da[index[edge]] - db[index[edge]] == -1)
check('post_repair_vertex_derivatives_diverge', da[index[(0,)]] - db[index[(0,)]] == 1)
check('post_repair_other_endpoint_derivative_diverges', da[index[(1,)]] - db[index[(1,)]] == -1)
check('all_other_derivative_differences_zero',
      all(da[i] == db[i] for i in range(n) if i not in (index[edge], index[(0,)], index[(1,)])))

out = {
    'claim_class': 'EXACT conditional factor-through-product nonidentifiability; event law OPEN; physical promotion 0',
    'carrier': '<0123,0124>', 'register': [len(v) for v in levels],
    'factor_premise': 'pre-event generator and observations factor only through h_e=C_cl,e*T_int,e; all face masks fixed',
    'states': {'A': {'C': 0, 'T': 1}, 'B': {'C': 0, 'T': 0}},
    'intervention': 'hypothetical repair_C sets C_01=1, leaves T_01 fixed',
    'post_edge_mask': {'A': 1, 'B': 0},
    'post_derivative_difference_A_minus_B': {'vertex_0': '1', 'vertex_1': '-1', 'edge_01': '-1'},
    'finite_replay': {'amplitude_jet_max_order': 8, 'current_jet_max_order': 5},
    'checks': checks, 'passed': sum(checks.values())
}
Path(__file__).with_name('results.json').write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
print(json.dumps({'passed': out['passed'], 'post_delta': out['post_derivative_difference_A_minus_B']}))
