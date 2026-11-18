"""Exact orbit and declared single-consumption controls."""
from itertools import combinations, permutations, product

edges = tuple(combinations(range(4), 2))
zero = (0, 0, 0)


def gram(s, d):
    return sum(v*v for v in s), sum(v*v for v in d), sum(a*b for a,b in zip(s,d))


def root(w, turn):
    return zero, tuple((-1)**turn*a for a in w)


orbit_cases = 0
for w in product((-1,0,1), repeat=3):
    if w == zero:
        continue
    first, antipode, repeat = (root(w,t) for t in range(3))
    assert gram(*first) == gram(*antipode) == gram(*repeat)
    assert first == repeat and first != antipode
    orbit_cases += 1

x = (1,2,4,-4,-2,-1)
stars = tuple(sum(a for e,a in zip(edges,x) if v in e) for v in range(4))
assert stars == (7,-5,-3,1)
assert sorted(stars) != sorted(-v for v in stars)

# Expected values are logically authenticated in this model.
live = (8, 1, root((1,2,4),0), "source-loader", "frame")
repeated_state = (8, 3, live[2], live[3], live[4])
prior_epoch = (7, 1, live[2], live[3], live[4])
wrong_payload = (8, 1, root((1,2,4),1), live[3], live[4])
wrong_block = (8, 1, live[2], "other-loader", live[4])
wrong_frame = (8, 1, live[2], live[3], "other-frame")


def commit(current, held, request, guard):
    if held is not None or request != current or not guard:
        return held, False
    return request, True


schedules = 0
requests = [(live,True),(live,True),(live,False),
            (repeated_state,True),(prior_epoch,True),(wrong_payload,True),
            (wrong_block,True),(wrong_frame,True)]
for order in permutations(requests):
    held, successes = None, 0
    for request, guard in order:
        held, succeeded = commit(live,held,request,guard)
        successes += succeeded
    assert held == live and successes == 1
    assert commit(live,held,live,True) == (held,False)
    schedules += 1

# If neither decision consumes Ready, both can authorize on the same input.
assert commit(live,None,live,True)[1] and commit(live,None,live,True)[1]
# With no qualifying delivery, at-most-once does not guarantee a commit.
assert commit(live,None,prior_epoch,True) == (None,False)
print(f"{orbit_cases} exact repeated-orbit controls and one S4 sign witness passed.")
print(f"{schedules} request orderings and duplicate, split-Ready and no-delivery controls passed.")
