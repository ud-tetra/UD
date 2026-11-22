"""Exact exterior-only PB3 and PB5 memory transfer (Physical Promotion = 0)."""
from collections import Counter
from itertools import combinations
import sympy as s

def build_operators(n):
    cells = [tuple(sorted((i,(i+1)%n,n,n+1))) for i in range(n)]
    simplices = sorted({face for cell in cells for k in range(1,5)
                        for face in combinations(cell,k)}, key=lambda face:(len(face),face))
    indices = {face:i for i,face in enumerate(simplices)}
    d = len(simplices)
    boundary = s.zeros(d)
    for j,face in enumerate(simplices):
        if len(face)>1:
            for i in range(len(face)):
                boundary[indices[face[:i]+face[i+1:]],j]=(-1)**i
    avg = s.Matrix([[int(len(face)==1 and face[0] in cell) for cell in cells] for face in simplices])
    v = s.Matrix([1,-1,1])
    whitney = (6*s.eye(3)-v*v.T)/9
    sink = s.zeros(d)
    for face,count in Counter(f for cell in cells for f in combinations(cell,3)).items():
        if count==1:
            edges = [indices[e] for e in combinations(face,2)]
            for i,row in enumerate(edges):
                for j,col in enumerate(edges):
                    sink[row,col] += whitney[i,j]
    assert boundary * boundary == s.zeros(d)
    q=s.eye(d)-avg*(avg.T*avg).inv()*avg.T
    skew=boundary-boundary.T
    return q*skew*q,sink,q*skew*avg

def verify_ring(n, omega_sq, lower, upper):
    skew, sink, forcing = build_operators(n)
    u = s.ones(n, 1)
    uniform = forcing * u
    partner = skew * uniform
    gram = forcing.T * forcing
    assert gram.det() != 0 and gram * u == gram.row(0).dot(u) * u
    assert skew * forcing == partner * u.T / n
    assert skew * partner == -omega_sq * uniform
    assert sink * forcing == s.Rational(4, 3) * forcing
    assert sink * partner == s.zeros(forcing.rows, 1)
    assert forcing.T * partner == s.zeros(n, 1) and partner != s.zeros(forcing.rows, 1)

    z, g = s.symbols("z g")
    d = 4 * g / 3
    uniform_block = s.Matrix([[-d, -omega_sq], [1, 0]])
    pencil = z * s.eye(2) - uniform_block
    quadratic = s.expand(pencil.det())
    assert s.cancel(pencil.inv()[0, 0] - z / quadratic) == 0
    assert s.gcd(z, quadratic, z) == 1
    determinant = (z + d)**(n - 1) * quadratic
    print(f"PB{n} exterior-only determinant = {determinant}")

    # Verify rational bounds on the smaller decay root at g_ext = 4.
    center = s.Rational(8, 3)
    discriminant = center**2 - omega_sq
    assert 0 < lower < upper < center
    assert (center - upper)**2 < discriminant < (center - lower)**2
    rate = center - s.sqrt(discriminant)
    print(f"PB{n} slow rate at g_ext=4 = {rate}, in ({lower}, {upper})")


if __name__ == "__main__":
    verify_ring(3, s.Rational(24, 5), s.Rational("1.146432766"), s.Rational("1.146432767"))
    verify_ring(5, s.Rational(40, 7), s.Rational("1.484792986"), s.Rational("1.484792987"))
