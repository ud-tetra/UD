#!/usr/bin/env python3
"""Replay the exact K4 projection and coefficient identities in SymPy."""

from itertools import combinations

from sympy import I, Matrix, Rational, conjugate, cos, eye, simplify, symbols, zeros


def tetrahedral_chain():
    simplices = [s for degree in range(1, 5)
                 for s in combinations(range(4), degree)]
    index = {simplex: i for i, simplex in enumerate(simplices)}
    boundary = zeros(len(simplices))
    for simplex, column in index.items():
        if len(simplex) > 1:
            for i in range(len(simplex)):
                row = index[simplex[:i] + simplex[i+1:]]
                boundary[row, column] = (-1)**i
    return simplices, boundary


def check_local_mode():
    simplices, boundary = tetrahedral_chain()
    assert len(simplices) == 15 and boundary**2 == zeros(15)
    generator = boundary - boundary.T
    uniform = Matrix([Rational(1, 2) if len(s) == 1 else 0 for s in simplices])
    projector = uniform * uniform.T
    assert generator.T == -generator
    assert uniform.dot(uniform) == 1
    assert projector**2 == projector == projector.T
    assert projector.rank() == 1 and generator.rank() == 14
    assert generator * projector == projector * generator == zeros(15)
    assert sum(x**4 for x in uniform) == Rational(1, 4)

    amplitude = symbols('a')
    vertex_coupling, h = symbols('g_v h', positive=True)
    mode = amplitude * uniform
    force = Matrix([vertex_coupling * value * conjugate(value) * value for value in mode])
    expected = vertex_coupling * amplitude**2 * conjugate(amplitude) / 4
    assert simplify(uniform.dot(force) - expected) == 0
    assert (force - uniform * expected).applyfunc(simplify) == zeros(15, 1)
    envelope = symbols('psi')
    field_force = expected.subs(amplitude, h**Rational(3, 2) * envelope) / h**Rational(3, 2)
    assert simplify(field_force - vertex_coupling*h**3*envelope**2*conjugate(envelope)/4) == 0
    print("Filled K4: 15 coordinates, one harmonic mode, quartic overlap 1/4.")
    print("Coarse field cubic coefficient: g_v*h^3/4, conditional on the vertex interaction.")


def check_dispersion():
    wavevectors = symbols('kx ky kz', real=True)
    hoppings = symbols('Jx Jy Jz', positive=True)
    h = symbols('h', positive=True)
    dispersion = 2 * sum(j * (1 - cos(k*h)) for j, k in zip(hoppings, wavevectors))
    hessian = Matrix([[dispersion.diff(k, ell) for ell in wavevectors] for k in wavevectors])
    assert hessian.subs(dict.fromkeys(wavevectors, 0)) == Matrix.diag(
        *(2*j*h**2 for j in hoppings)
    )
    assert dispersion.diff(wavevectors[0], 4).subs(wavevectors[0], 0) == -2*hoppings[0]*h**4
    print("Exact band Hessian at zero: diag(2*Jx*h^2, 2*Jy*h^2, 2*Jz*h^2).")


def check_memory():
    omega = symbols('omega', real=True)
    generator = Matrix([[0, -omega], [omega, 0]])
    resolved = Matrix([1, 0])
    unresolved = eye(2) - resolved * resolved.T
    g_aq = resolved.T * generator * unresolved
    g_qa = unresolved * generator * resolved
    assert unresolved * generator * unresolved == zeros(2)
    assert g_aq * g_qa == Matrix([[-omega**2]])
    assert g_aq * Matrix([0, 1]) == Matrix([[-omega]])
    assert (I * generator).H == I * generator
    print("Two-mode projection control: kernel -omega^2, unresolved forcing -omega*eta(0).")


if __name__ == '__main__':
    check_local_mode()
    check_dispersion()
    check_memory()
