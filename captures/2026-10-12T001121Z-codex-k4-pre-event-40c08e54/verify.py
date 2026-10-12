#!/usr/bin/env python3
"""Exact bounded K4 comparison automaton; no physical or UD-native claim."""
from itertools import permutations, product
import json

EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
PAIRS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
EI = {e: i for i, e in enumerate(EDGES)}
PI = {frozenset(p): i for i, p in enumerate(PAIRS)}
EP = tuple(PI[next(frozenset(p) for p in PAIRS if e in p)] for e in EDGES)


def bits(n, length):
    return tuple((n >> i) & 1 for i in range(length))


def state(theta, closure, transport, pair_fuel, closure_fuel,
          fail_fuel, reset_fuel, phase):
    return (tuple(theta), tuple(closure), tuple(transport),
            tuple(pair_fuel), tuple(closure_fuel), tuple(fail_fuel),
            tuple(reset_fuel), phase)


def valid(s):
    th, c, t, fp, fc, ff, fr, z = s
    return (len(th) == len(fp) == 3 and
            all(len(x) == 6 for x in (c, t, fc, ff, fr)) and
            z in (0, 1) and
            all(v in (0, 1) for x in s[:-1] for v in x) and
            all(th[p] or (t[EI[a]] and t[EI[b]])
                for p, (a, b) in enumerate(PAIRS)))


def step(s):
    """Deterministic total transition on the declared admissible domain."""
    assert valid(s)
    th, c, t, fp, fc, ff, fr, z = s
    on = 1 - z
    fail = tuple(on * ff[e] * t[e] * th[EP[e]] for e in range(6))
    reset = tuple(on * fr[e] * (1 - t[e]) for e in range(6))
    ct = tuple(on * fc[e] * t[e] * (1 - fail[e]) for e in range(6))
    pt = tuple(on * fp[p] * t[EI[a]] * t[EI[b]] *
               (1 - fail[EI[a]]) * (1 - fail[EI[b]])
               for p, (a, b) in enumerate(PAIRS))
    nxt = state(tuple(th[p] ^ pt[p] for p in range(3)),
                tuple(c[e] ^ ct[e] for e in range(6)),
                tuple(t[e] - fail[e] + reset[e] for e in range(6)),
                tuple(fp[p] - pt[p] for p in range(3)),
                tuple(fc[e] - ct[e] for e in range(6)),
                tuple(ff[e] - fail[e] for e in range(6)),
                tuple(fr[e] - reset[e] for e in range(6)), 1 - z)
    assert valid(nxt)
    return nxt, (pt, ct, fail, reset)


def mask(s):
    return tuple(a * b for a, b in zip(s[1], s[2]))


def permute(s, perm):
    ep = tuple(EI[tuple(sorted((perm[a], perm[b])))] for a, b in EDGES)
    pp = tuple(PI[frozenset(tuple(sorted((perm[a], perm[b])))
                            for a, b in pair)] for pair in PAIRS)
    def push(x, order):
        y = [None] * len(order)
        for i, j in enumerate(order):
            y[j] = x[i]
        return tuple(y)
    return state(push(s[0], pp), push(s[1], ep), push(s[2], ep),
                 push(s[3], pp), push(s[4], ep), push(s[5], ep),
                 push(s[6], ep), s[7])


def fuel(s):
    return sum(sum(x) for x in s[3:7])


def local_cases():
    count = 0
    # Each pair has two edges; all admissible theta/transport states,
    # both closure bits, seven fuel bits and two phases: 5*4*128*2=5120.
    for th, t0, t1 in ((0, 1, 1), (1, 0, 0), (1, 0, 1),
                       (1, 1, 0), (1, 1, 1)):
        for c0, c1 in product((0, 1), repeat=2):
            for bs in product((0, 1), repeat=7):
                fp, fc0, fc1, ff0, ff1, fr0, fr1 = bs
                for z in (0, 1):
                    t = (t0, t1, 1, 1, 1, 1)
                    s = state((th, 1, 1), (c0, c1, 1, 1, 1, 1),
                              t, (fp, 0, 0), (fc0, fc1, 0, 0, 0, 0),
                              (ff0, ff1, 0, 0, 0, 0),
                              (fr0, fr1, 0, 0, 0, 0), z)
                    # Edge order 01,02,03,12,13,23: A edges are 01,23.
                    # Reassign second local edge to 23, not index 1.
                    c = list(s[1]); c[5], c[1] = c[1], 1
                    t = list(s[2]); t[5], t[1] = t[1], 1
                    fld = [list(x) for x in s[4:7]]
                    for q in fld:
                        q[5], q[1] = q[1], 0
                    s = state(s[0], c, t, s[3], *fld, z)
                    assert valid(s)
                    nxt, pulses = step(s)
                    assert fuel(s) - fuel(nxt) == sum(sum(x) for x in pulses)
                    if z == 1 or fuel(s) == 0:
                        assert nxt[:3] == s[:3]
                    start_budget = fuel(s)
                    cur = s
                    for _ in range(2 * (start_budget + 1)):
                        cur, _ = step(cur)
                    stable, _ = step(cur)
                    stable2, _ = step(stable)
                    assert stable[:3] == stable2[:3] == cur[:3]
                    assert fuel(cur) <= start_budget
                    count += 1
    return count


def run():
    local = local_cases()
    assert local == 5120
    perms = tuple(permutations(range(4)))
    covariance = 0
    # Cross-pair simultaneous/boundary fixtures plus every theta/T
    # admissible combination, transformed by all S4 vertex relabelings.
    options = ((0, 1, 1), (1, 0, 0), (1, 0, 1),
               (1, 1, 0), (1, 1, 1))
    for triple in product(options, repeat=3):
        th = tuple(x[0] for x in triple)
        t = [0] * 6
        for p, (_, a, b) in enumerate(triple):
            e, f = PAIRS[p]
            t[EI[e]], t[EI[f]] = a, b
        for seed in (0, 1, 2, 3):
            s = state(th, bits(17 * seed, 6), t,
                      bits(5 * seed, 3), bits(11 * seed, 6),
                      bits(23 * seed, 6), bits(37 * seed, 6), seed & 1)
            after, _ = step(s)
            for perm in perms:
                ps = permute(s, perm)
                got, _ = step(ps)
                assert got == permute(after, perm)
                assert mask(ps) == permute(state((0, 0, 0), mask(s),
                       (1,) * 6, (0,) * 3, (0,) * 6,
                       (0,) * 6, (0,) * 6, 0), perm)[1]
                covariance += 1
    assert covariance == 12000
    null = state((1, 1, 1), (1,) * 6, (1,) * 6,
                 (0,) * 3, (0,) * 6, (0,) * 6, (0,) * 6, 0)
    same, pp = step(null)
    assert same[:3] == null[:3] and sum(sum(x) for x in pp) == 0
    pair = state((1, 1, 1), (1,) * 6, (1,) * 6,
                 (1, 1, 0), (0,) * 6, (0,) * 6, (0,) * 6, 0)
    both, pulses = step(pair)
    assert pulses[0] == (1, 1, 0) and both[0] == (0, 0, 1)
    masks = set()
    for n in range(64):
        s = state((1,) * 3, (1,) * 6, (1,) * 6,
                  (0,) * 3, bits(n, 6), (0,) * 6, (0,) * 6, 0)
        y, _ = step(s)
        masks.add(mask(y))
    assert len(masks) == 64
    one = state((1,) * 3, (1,) * 6, (1,) * 6,
                (1, 0, 0), (0,) * 6, (0,) * 6, (0,) * 6, 0)
    hold = state((1,) * 3, (1,) * 6, (1,) * 6,
                 (0,) * 3, (0,) * 6, (0,) * 6, (0,) * 6, 0)
    assert one[:3] == hold[:3] and step(one)[0][0] != step(hold)[0][0]
    # Failure of a currently open pair is suppressed; a closed pair can
    # fail, then a separate supplied reset fuel can restore integrity.
    fail = state((1,) * 3, (1,) * 6, (1,) * 6,
                 (0,) * 3, (0,) * 6, bits(1, 6), bits(1, 6), 0)
    f1, _ = step(fail); f2, _ = step(f1); f3, _ = step(f2)
    assert f1[2][0] == 0 and f3[2][0] == 1
    # A pair toggle and failure in the same pair: pair toggle holds.
    collision = state((1,) * 3, (1,) * 6, (1,) * 6,
                      (1, 0, 0), (0,) * 6, bits(1, 6), (0,) * 6, 0)
    z, pulse = step(collision)
    assert pulse[0][0] == 0 and pulse[2][0] == 1 and z[0][0] == 1
    return {'status':'PASS', 'local_admissible_cases':local,
            'local_multistep_termination_cases':local,
            'S4_covariance_checks':covariance,
            'distinct_one_step_edge_masks':len(masks),
            'fixed_structure_null':'PASS',
            'symmetry_tie_batch':'PASS',
            'reduced_state_ambiguity':'PASS',
            'failure_reset':'PASS',
            'same_pair_collision_hold':'PASS',
            'physical_promotion':0}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
