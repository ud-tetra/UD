"""Fresh rational witnesses for a typed conditional theorem, not source admission."""
from fractions import Fraction as Q
import json

def ident(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]

def transpose(a):
    return [list(x) for x in zip(*a)]

def mul(a, b):
    assert len(a[0]) == len(b), 'matrix-domain mismatch'
    return [[sum((x*y for x, y in zip(row, col)), Q(0)) for col in zip(*b)] for row in a]

def chain(*args):
    out = args[0]
    for a in args[1:]:
        out = mul(out, a)
    return out

def diag(values):
    return [[v if i == j else Q(0) for j in range(len(values))] for i, v in enumerate(values)]

def neg(a):
    return [[-x for x in row] for row in a]

def typed_compose(outer, inner):
    assert outer['domain'] == inner['codomain'], 'typed carrier mismatch'
    return {'domain': inner['domain'], 'codomain': outer['codomain']}

def run():
    i6, i15 = ident(6), ident(15)
    v = [Q(k) for k in range(1, 16)]
    norm = sum(x*x for x in v)
    householder = [[i15[i][j] - 2*v[i]*v[j]/norm for j in range(15)] for i in range(15)]
    w = [row[:6] for row in householder]
    t = transpose(w)
    assert mul(t, w) == i6
    r = diag([Q(1)]*3 + [Q(-1)]*3)
    j = [[Q(1) if col == row+3 else Q(-1) if row == col+3 else Q(0)
          for col in range(6)] for row in range(6)]
    swap = [[Q(col == (row+3) % 6) for col in range(6)] for row in range(6)]
    theta = chain(w, r, t)
    projector = mul(w, t)
    jh = chain(w, j, t)
    assert mul(theta, theta) == projector and projector != i15
    assert chain(theta, theta, w) == w
    assert mul(t, theta) == mul(r, t)
    assert chain(r, j, r) == neg(j)
    assert chain(theta, jh, theta) == neg(jh)
    assert chain(swap, r, swap) == neg(r)
    assert chain(swap, j, swap) == neg(j)
    checked = []
    for c in [Q(1, 3), Q(1), Q(5, 2)]:
        ic = diag([c]*3 + [1/c]*3)
        f = mul(w, ic)
        assert mul(r, ic) == mul(ic, r)
        assert mul(theta, f) == mul(f, r)
        assert chain(t, theta, w, ic) == mul(r, ic) == mul(ic, r)
        assert chain(transpose(ic), j, ic) == j
        assert chain(t, jh, w) == j
        checked.append(str(c))
    w_type = {'domain': 'event', 'codomain': 'selected_Hodge'}
    t_type = {'domain': 'selected_Hodge', 'codomain': 'event'}
    theta_type = {'domain': 'selected_Hodge', 'codomain': 'selected_Hodge'}
    ic_type = {'domain': 'retained', 'codomain': 'event'}
    f_type = typed_compose(w_type, ic_type)
    assert typed_compose(t_type, typed_compose(theta_type, f_type)) == {'domain': 'retained', 'codomain': 'event'}
    controls = []
    for label, operation in [
        ('omitted embedding: typed carriers', lambda: typed_compose(theta_type, ic_type)),
        ('omitted embedding: rectangular matrices', lambda: chain(t, theta, diag([Q(1)]*6))),
    ]:
        try:
            operation()
        except AssertionError:
            controls.append(label)
        else:
            raise AssertionError('invalid composition was accepted')
    assert mul(theta, theta) != i15
    controls.append('ambient involution rejected')
    assert chain(swap, j, swap) != j
    controls.append('copy swap as same symplectic branch rejected')
    return {'status': 'PASS', 'arithmetic': 'exact rational', 'ambient_dimension': 15,
            'selected_dimension': 6, 'c_values': checked,
            'checks': ['two basic identities', 'repaired typed composition', 'selected-sector involution',
                       'Darboux pullback', 'anti-symplectic parity', 'copy-swap sign qualifications'],
            'rejection_controls': controls,
            'scope': 'constructed rational witnesses; general proof written separately; native W admission open',
            'independent_review': False, 'physical_promotion': 0}

if __name__ == '__main__':
    print(json.dumps(run()))
