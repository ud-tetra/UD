"""Exact boundary-fixed stellar refinement control for AW5."""
import sys
from pathlib import Path
from fractions import Fraction
from itertools import combinations

from sympy import Matrix, zeros

sys.dont_write_bytecode = True
prior = Path(__file__).resolve().parents[1]/"2026-11-16T004932Z-codex-aw5-heat-729e4b"
sys.path.insert(0, str(prior))
from heat_trace_aw5 import HUB, LEAVES, boundary, face_laplacian

faces_ext = sorted(boundary([HUB]+LEAVES))
faces_shell = set(combinations(HUB, 3))


def refine(original, count):
    cells = original[count:]
    for i, leaf in enumerate(original[:count]):
        cells += [face+(8+i,) for face in combinations(leaf,3)]
    return cells


def harmonic(cells):
    basis, B2, B3, L = face_laplacian(cells)
    faces = basis[2]
    z = zeros(len(faces), 1)
    for j in range(4):
        z[faces.index(HUB[:j]+HUB[j+1:])] = (-1)**j
    assert B2*z == zeros(B2.rows, 1)
    gram = B3.T*B3
    h = z-B3*gram.inv(method="DM")*B3.T*z
    assert h != zeros(h.rows, 1) and L*h == zeros(h.rows, 1)
    assert L.rows-L.to_DM().rank() == 1
    ext = Matrix([h[faces.index(face)] for face in faces_ext])
    return h, ext


def square(v):
    return v.dot(v)


def residue(q, h, exterior):
    return q.dot(exterior)**2/(square(q)*square(h))


h0, q = harmonic(LEAVES)
for count in range(5):
    cells = refine(LEAVES, count)
    assert boundary(cells) == set(faces_ext)|faces_shell
    h, exterior = harmonic(cells)
    print(f"leaves={count} norm²={square(h)} fixed={residue(q,h,exterior)} "
          f"optimal={square(exterior)/square(h)}")
    assert square(h) == Fraction(3*(20-count),20)
    assert residue(q,h,exterior) == Fraction(20-count,80)
    assert square(exterior)/square(h) == Fraction(100-9*count,20*(20-count))
    if count == 1:
        print("exterior:", list(exterior))
        assert square(exterior)/square(h)-residue(q,h,exterior) == Fraction(3,1520)
