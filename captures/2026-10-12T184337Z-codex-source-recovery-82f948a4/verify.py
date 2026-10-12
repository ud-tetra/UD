#!/usr/bin/env python3
"""Exact finite witnesses for the packet-to-visible event-source dependency gate.

These are constructed conditional kernels, not inferred UD dynamics or data.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


states = tuple((hidden, theta) for hidden in (0, 1) for theta in (0, 1))
rate = (Q(1, 4), Q(1, 2))


def transition(renew_hidden):
    matrix = [[Q(0) for _ in states] for _ in states]
    for i, (hidden, theta) in enumerate(states):
        next_hidden = 1 - hidden if renew_hidden else hidden
        matrix[i][states.index((next_hidden, theta))] += 1 - rate[hidden]
        matrix[i][states.index((next_hidden, 1 - theta))] += rate[hidden]
    return matrix


def killed(matrix):
    return [[matrix[i][j] if states[i][1] == states[j][1] else Q(0)
             for j in range(len(states))] for i in range(len(states))]


def strict_null(matrix, initial, attempts):
    vector = [Q(int(s == initial)) for s in states]
    null = killed(matrix)
    for _ in range(attempts):
        vector = [sum(vector[i] * null[i][j] for i in range(len(states)))
                  for j in range(len(states))]
    return sum(vector)


def visible_distribution(matrix, initial):
    i = states.index(initial)
    return tuple(sum(matrix[i][j] for j, (_, bit) in enumerate(states) if bit == b)
                 for b in (0, 1))


def main():
    fixed = transition(False)
    renewed = transition(True)
    assert all(sum(row) == 1 and all(x >= 0 for x in row) for matrix in (fixed, renewed) for row in matrix)
    # Same visible 0, different hidden states: no universal Theta-only Markov kernel.
    assert visible_distribution(fixed, (0, 0)) == (Q(3, 4), Q(1, 4))
    assert visible_distribution(fixed, (1, 0)) == (Q(1, 2), Q(1, 2))
    # Identical first-attempt visible switch rate, different subsequent null history.
    assert visible_distribution(fixed, (0, 0)) == visible_distribution(renewed, (0, 0))
    assert strict_null(fixed, (0, 0), 3) == Q(27, 64)
    assert strict_null(renewed, (0, 0), 3) == Q(9, 32)
    result = {
        'status': 'PASS',
        'scope': 'constructed four-state hidden/visible kernel; not a UD packet source',
        'same_visible_theta_0_next_distribution_hidden_0': ['3/4', '1/4'],
        'same_visible_theta_0_next_distribution_hidden_1': ['1/2', '1/2'],
        'first_attempt_distribution_start_hidden_0': ['3/4', '1/4'],
        'strict_three_attempt_null_fixed_hidden': '27/64',
        'strict_three_attempt_null_renewed_hidden': '9/32',
        'packet_to_Theta_map': 'NOT_SOURCED',
        'independent_endpoint_score': 'NOT_RUN',
        'physical_promotion': 0,
    }
    Path(__file__).with_name('results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
