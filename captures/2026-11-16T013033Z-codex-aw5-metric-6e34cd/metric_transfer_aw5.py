"""Exact chain retraction, diagonal-weight obstruction and Whitney AW5 check."""
from itertools import combinations
from pathlib import Path
import sys

from sympy import Matrix, Rational as Q, eye, zeros

sys.dont_write_bytecode = True
captures = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(captures/"2026-11-16T004932Z-codex-aw5-heat-729e4b"))
sys.path.insert(0, str(captures/"2026-11-16T011802Z-codex-aw5-refine-1dd290"))
from refine_aw5 import faces_ext, harmonic, refine
from heat_trace_aw5 import LEAVES, face_laplacian


def boundary_matrix(lower, upper):
    index = {s: i for i,s in enumerate(lower)}
    D = zeros(len(lower), len(upper))
    for j, s in enumerate(upper):
        for k in range(len(s)):
            D[index[s[:k]+s[k+1:]],j] = (-1)**k
    return D


def split_metric_check():
    coarse = face_laplacian(LEAVES)[0]
    first_leaf = LEAVES[0]
    fine = face_laplacian(refine(LEAVES, 1))[0]
    S, R, M = [], [], []
    for old, new in zip(coarse, fine):
        s, r = zeros(len(new),len(old)), zeros(len(old),len(new))
        for j, simplex in enumerate(old):
            if simplex == first_leaf:
                for i in range(4):
                    child = simplex[:i]+simplex[i+1:]+(8,)
                    s[new.index(child),j] = (-1)**(i+3)
            else:
                s[new.index(simplex),j] = 1
        for j, simplex in enumerate(new):
            image = tuple(first_leaf[0] if v == 8 else v for v in simplex)
            if len(set(image)) == len(image):
                inversions = sum(a > b for a,b in combinations(image,2))
                r[old.index(tuple(sorted(image))),j] = (-1)**inversions
        assert r*s == eye(len(old))
        q = eye(len(new))-s*r
        m = r.T*r+q.T*q
        assert s.T*m*s == eye(len(old)) and s.T*m == r
        S.append(s)
        R.append(r)
        M.append(m)
    for k in range(1,4):
        bc = boundary_matrix(coarse[k-1],coarse[k])
        bf = boundary_matrix(fine[k-1],fine[k])
        assert bf*S[k] == S[k-1]*bc
        assert bc*R[k] == R[k-1]*bf
    h, exterior = harmonic(LEAVES)
    h_f = S[2]*h
    drive = zeros(len(coarse[2]),1)
    for simplex,value in zip(faces_ext,exterior):
        drive[coarse[2].index(simplex)] = value
    drive_f = S[2]*drive
    assert (drive_f.T*M[2]*h_f)[0]**2/((drive_f.T*M[2]*drive_f)[0]*(h_f.T*M[2]*h_f)[0]) == Q(1,4)
    raw = zeros(len(fine[2]),1)
    for simplex,value in zip(faces_ext,exterior):
        raw[fine[2].index(simplex)] = value
    raw_residue = (raw.dot(h_f))**2/((raw.T*M[2].inv(method="DM")*raw)[0]*(h_f.T*M[2]*h_f)[0])
    print("chain split metric: transferred residue 1/4; raw exterior covector normalized residue",raw_residue)


COORDINATES = list(map(Matrix, (
    [0,0,0], [1,0,0], [0,1,0], [0,0,1], [1,1,1], [-1,0,0], [0,-1,0], [0,0,-1],
)))
COORDINATES.append(sum((COORDINATES[i] for i in LEAVES[0]),zeros(3,1))/4)


def whitney_mass(cells, faces):
    mass = zeros(len(faces))
    for tet in cells:
        coords = [COORDINATES[i] for i in tet]
        gradients = Matrix([[1,*v] for v in coords]).inv()[1:,:]
        volume = abs(Matrix.hstack(*(v-coords[0] for v in coords[1:])).det())/6
        moment = volume*(eye(4)+Matrix.ones(4))/20
        fields = []
        for i,j,k in combinations(range(4),3):
            field = zeros(3,4)
            for a,b,c in [(i,j,k),(j,k,i),(k,i,j)]:
                field[:,a] = 2*gradients[:,b].cross(gradients[:,c])
            fields.append((faces.index(tuple(tet[x] for x in (i,j,k))),field))
        for i,F in fields:
            for j,G in fields:
                mass[i,j] += (F*moment*G.T).trace()
    return mass


def check_whitney():
    _, exterior = harmonic(LEAVES)
    answers = []
    for name, cells in (("coarse", LEAVES), ("one leaf refined", refine(LEAVES,1))):
        basis,B2,B3,_ = face_laplacian(cells)
        faces = basis[2]
        mass = whitney_mass(cells, faces)
        null = B3.T.col_join(B2*mass).nullspace()
        assert len(null) == 1
        h = null[0]
        load = zeros(len(faces),1)
        for f,c in zip(faces_ext,exterior):
            load[faces.index(f)] = c
        fixed = load.dot(h)**2/(h.T*mass*h)[0]
        unit = fixed/(load.T*mass.inv(method="DM")*load)[0]
        answers.append((fixed,unit))
        print(f"Whitney {name}: fixed exterior load residue {fixed}; unit-dual residue {unit}")
    assert answers[0][1] != answers[1][1]


if __name__ == "__main__":
    split_metric_check()
    check_whitney()
