"""Exact controls for C06 lease coverage and declared capability transitions."""
from fractions import Fraction as F
from itertools import permutations, product


def coverage(rate, lease, cut_on_tie):
    hit = 1/rate
    return hit < lease or (hit == lease and cut_on_tie)


leases = (F(1,4),F(1,2),F(1),F(2),F(4))
rates = (F(1,4),F(1,2),F(1),F(2))
checks = 0
for rate,lease,tie in product(rates,leases,(False,True)):
    assert coverage(rate,lease,tie) == (rate*lease > 1 or (tie and rate*lease == 1))
    checks += 1
for lease in leases:
    rate = 1/(2*lease)
    assert 1/rate == 2*lease and not coverage(rate,lease,True)

abort_cases = 0
for (a,b),total in product(((1,0),(F(3,5),F(4,5)),(F(5,13),F(12,13))), (F(1),F(2),F(7,3))):
    donor,archive = total*a*a,total*b*b
    assert donor > 0 and donor+archive == total
    assert archive/2 < total/2
    abort_cases += 1


def transition(mode, request):
    if mode != "Armed":
        return mode
    if request == "verified-root":
        return "Held"
    if request == "true-veto":
        return "Aborted"
    return mode


schedules = 0
for order in permutations(("other-owner","old-epoch","verified-root","verified-root","publication")):
    mode, held_count = "Armed", 0
    for request in order:
        new = transition(mode,request)
        held_count += mode != "Held" and new == "Held"
        mode = new
    assert held_count == 1 and mode == "Held"
    schedules += 1
assert transition(transition("Armed","true-veto"),"verified-root") == "Aborted"
assert transition(transition("Armed","verified-root"),"true-veto") == "Held"
print(f"{checks} lifetime/tie controls and {len(leases)} finite slow-hit witnesses passed.")
print(f"{abort_cases} exact partial-abort stock checks and {schedules} labeled reservation schedules passed.")
