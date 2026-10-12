"""Independent finite audit of the declared K4 comparison transition.

No imports from the candidate verifier. The packed state uses per-pair
two-edge cells rather than the candidate's six-edge ordering internally.
"""
from itertools import permutations, product

PAIR_EDGES = ((0, 5), (1, 4), (2, 3))
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}


def evolve(s):
    # s = (theta[3], closure[6], integrity[6], toggle[3],
    #      closure_stock[6], failure_stock[6], reset_stock[6], phase)
    th, cl, tr, bt, bc, bf, br, phase = s
    nt, nc, ni = list(th), list(cl), list(tr)
    ft, fc, ff, fr = list(bt), list(bc), list(bf), list(br)
    count = 0
    if phase == 0:
        for p, (u, v) in enumerate(PAIR_EDGES):
            failures = [bf[e] and tr[e] and th[p] for e in (u, v)]
            resets = [br[e] and not tr[e] for e in (u, v)]
            change = bool(bt[p] and tr[u] and tr[v]
                          and not any(failures))
            if change:
                nt[p] ^= 1
                ft[p] -= 1
                count += 1
            for e, failure, reset in zip((u, v), failures, resets):
                closure = bool(bc[e] and tr[e] and not failure)
                if closure:
                    nc[e] ^= 1
                    fc[e] -= 1
                    count += 1
                if failure:
                    ni[e] = 0
                    ff[e] -= 1
                    count += 1
                if reset:
                    ni[e] = 1
                    fr[e] -= 1
                    count += 1
    return (tuple(nt), tuple(nc), tuple(ni), tuple(ft), tuple(fc),
            tuple(ff), tuple(fr), 1 - phase), count


def budget(s):
    return sum(map(sum, s[3:7]))


def admissible(s):
    return all(s[0][p] or (s[2][u] and s[2][v])
               for p, (u, v) in enumerate(PAIR_EDGES))


def permute(s, vmap):
    emap = [EDGE_ID[tuple(sorted((vmap[a], vmap[b])))] for a, b in EDGES]
    edge_sets = [frozenset(EDGES[i] for i in pair) for pair in PAIR_EDGES]
    pmap = [edge_sets.index(frozenset(EDGES[emap[i]] for i in pair))
            for pair in PAIR_EDGES]
    def move(values, mapping):
        result = [None] * len(mapping)
        for source, target in enumerate(mapping):
            result[target] = values[source]
        return tuple(result)
    return (move(s[0], pmap), move(s[1], emap), move(s[2], emap),
            move(s[3], pmap), move(s[4], emap), move(s[5], emap),
            move(s[6], emap), s[7])


def local_state(spec, fuels, phase):
    t, x, y, c, d = spec
    bt, cu, cv, fu, fv, ru, rv = fuels
    cl = [1] * 6
    tr = [1] * 6
    stocks = [[0] * 6 for _ in range(3)]
    cl[0], cl[5] = c, d
    tr[0], tr[5] = x, y
    for register, u, v in zip(stocks, (cu, fu, ru), (cv, fv, rv)):
        register[0], register[5] = u, v
    return ((t, 1, 1), tuple(cl), tuple(tr), (bt, 0, 0),
            *(tuple(register) for register in stocks), phase)


def check():
    cases = 0
    for t, x, y in ((0, 1, 1), (1, 0, 0), (1, 0, 1),
                    (1, 1, 0), (1, 1, 1)):
        for c, d in product((0, 1), repeat=2):
            for fuels in product((0, 1), repeat=7):
                for phase in (0, 1):
                    initial = local_state((t, x, y, c, d), fuels, phase)
                    nxt, pulse_count = evolve(initial)
                    assert admissible(initial) and admissible(nxt)
                    assert budget(initial) - budget(nxt) == pulse_count
                    history = []
                    current = initial
                    for _ in range(2 * (budget(initial) + 1)):
                        current, count = evolve(current)
                        history.append(count)
                    later, count = evolve(current)
                    later2, count2 = evolve(later)
                    assert current[:3] == later[:3] == later2[:3]
                    assert count == count2 == 0
                    assert sum(history) <= budget(initial)
                    cases += 1
    assert cases == 5120

    # Broader mixed-pair tests, with independent field patterns for each pair.
    patterns = ((0, 1, 1), (1, 0, 0), (1, 0, 1),
                (1, 1, 0), (1, 1, 1))
    permutations_checked = 0
    for combo in product(patterns, repeat=3):
        th = tuple(x[0] for x in combo)
        tr = [0] * 6
        for (_, a, b), (u, v) in zip(combo, PAIR_EDGES):
            tr[u], tr[v] = a, b
        for seed in range(8):
            # A different modular pattern from the candidate's four fixtures.
            fields = [tuple(((seed * m + j * k + j // 2) >> (j % 3)) & 1
                            for j in range(n))
                      for n, m, k in ((6, 31, 11), (3, 13, 7),
                                      (6, 41, 5), (6, 17, 13),
                                      (6, 29, 19))]
            state = (th, fields[0], tuple(tr), fields[1],
                     fields[2], fields[3], fields[4], seed % 2)
            updated, _ = evolve(state)
            for sigma in permutations(range(4)):
                relabeled = permute(state, sigma)
                relabeled_updated, _ = evolve(relabeled)
                assert admissible(relabeled_updated)
                assert relabeled_updated == permute(updated, sigma)
                permutations_checked += 1

    base = ((1, 1, 1), (1,) * 6, (1,) * 6, (0,) * 3,
            (0,) * 6, (0,) * 6, (0,) * 6, 0)
    outputs = {}
    for selection in product((0, 1), repeat=6):
        state = base[:4] + (selection,) + base[5:]
        next_state, _ = evolve(state)
        output = tuple(a & b for a, b in zip(next_state[1], next_state[2]))
        assert output not in outputs
        outputs[output] = selection
        assert output == tuple(1 ^ bit for bit in selection)
    assert len(outputs) == 64
    print({'local_cases': cases, 'S4_checks': permutations_checked,
           'distinct_masks': len(outputs), 'status': 'PASS'})


if __name__ == '__main__':
    check()
