#!/usr/bin/env python3
"""Independent generated checker; finite algebra and scoped numerical diagnostics.

No imported research archive code is executed. The gate map is reimplemented from
its declared finite-label formula. Mathematical proof obligations are stated
separately from finite checks and floating-point diagnostics.
"""
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np
import scipy.linalg
import sympy as sp

ROOT = Path(__file__).resolve().parent
COUNTS = {}


def require(condition, message, count=None):
    if not condition:
        raise AssertionError(message)
    if count:
        COUNTS[count] = COUNTS.get(count, 0) + 1


def spin_checks():
    out = []
    z = sp.Symbol('z')
    for K in range(1, 9):
        A = sp.zeros(K+1)
        for j in range(K):
            A[j+1, j] = j+1
            A[j, j+1] = K-j
        M = sp.diag(*[math.comb(K, j) for j in range(K+1)])
        require(A.T*M == M*A, 'Exact clock metric adjoint', 'clock_metric_identities')
        expected = sp.prod(z-(K-2*l) for l in range(K+1))
        require(sp.expand(A.charpoly(z).as_expr()-expected) == 0,
                'Exact spin spectrum', 'clock_characteristic_polynomials')
        J = sp.zeros(K+1)
        for j in range(K+1):
            J[K-j, j] = 1
        require(J*J == sp.eye(K+1) and J.T*M*J == M,
                'Exact endpoint reflection metric unitary', 'clock_endpoint_identities')
        # Embedded unnormalized symmetric sums: every weight-j basis string is
        # included once. Count each target coefficient after sum_i X_i.
        for j in range(K+1):
            accumulated = [0]*(1 << K)
            for x in range(1 << K):
                if x.bit_count() == j:
                    for i in range(K):
                        accumulated[x ^ (1 << i)] += 1
            for x, coeff in enumerate(accumulated):
                wt = x.bit_count()
                expected_coeff = j+1 if wt == j+1 else (K-j+1 if wt == j-1 else 0)
                require(coeff == expected_coeff, 'Symmetric spin embedding', 'spin_embedding_coefficients')
            for x in range(1 << K):
                if x.bit_count() == j:
                    require(((x ^ ((1 << K)-1)).bit_count()) == K-j,
                            'All-spin flip endpoint', 'spin_endpoint_basis_actions')
        # The K binary X_i commute and square to identity as exact bit flips.
        for x in range(1 << K):
            for i in range(K):
                require((x ^ (1 << i) ^ (1 << i)) == x,
                        'Spin involution', 'spin_involution_actions')
                for q in range(i+1, K):
                    require((x ^ (1 << i) ^ (1 << q)) ==
                            (x ^ (1 << q) ^ (1 << i)),
                            'Spin commutation', 'spin_commutation_actions')
        out.append({'K': K, 'dimension': K+1,
                    'spectrum': [K-2*l for l in range(K+1)],
                    'metric': [math.comb(K, j) for j in range(K+1)],
                    'exact_checks': 'PASS'})
    return out


def compute_payload(p, inverse=False):
    w, h, r = p
    F = (1, 1)
    rho = (1, 0)
    if inverse:
        return (h, (w-F[h]) % 2, (r-rho[h]) % 2)
    return ((h+F[w]) % 2, w, (r+rho[w]) % 2)


def weighted_path_checks():
    """Exact rational similarity checks for an engineered weighted 1D clock."""
    rows = []
    z = sp.Symbol('z')
    for n in (2, 4, 6, 10):
        M = n//2
        vertices = [sp.Rational(1)]
        edges = []
        for r in range(M):
            e = vertices[-1]/((2*r+1)*(n-2*r))
            edges.append(e)
            vertices.append(e*((2*r+2)*(n-2*r-1)))
        B = sp.zeros(M+1, M)
        for r in range(M):
            B[r, r] = -1
            B[r+1, r] = 1
            require(vertices[r]/edges[r] == (2*r+1)*(n-2*r),
                    'Left weighted incidence square', 'path_edge_square_identities')
            require(vertices[r+1]/edges[r] == (2*r+2)*(n-2*r-1),
                    'Right weighted incidence square', 'path_edge_square_identities')
        Gv, Geinv = sp.diag(*vertices), sp.diag(*[1/e for e in edges])
        # Similarity to the real skew generator via P=diag(sqrt(Gv),sqrt(Ge)):
        # P^-1 A P = [[0, B Ge^-1],[-B.T Gv,0]]. All entries are rational.
        rational = sp.zeros(n+1)
        rational[:M+1, M+1:] = B*Geinv
        rational[M+1:, :M+1] = -B.T*Gv
        expected = sp.prod(z-sp.I*(n-2*l) for l in range(n+1))
        require(sp.expand(rational.charpoly(z).as_expr()-expected) == 0,
                'Exact weighted path Hodge spectrum', 'path_characteristic_polynomials')
        require(len(rational.nullspace()) == 1, 'H0 kernel dimension', 'path_kernel_dimensions')
        exactkernel = sp.Matrix([1/v for v in vertices]+[0]*M)
        require(rational*exactkernel == sp.zeros(n+1, 1),
                'Weighted vertex harmonic vector', 'path_kernel_vectors')
        # Clock-interleaved skew matrix has upper entries -sqrt((j+1)(n-j)).
        # S=diag(i^j): S H_C S-adjoint = i A, with A upper negative.
        for j in range(n):
            require(sp.I**j*sp.conjugate(sp.I**(j+1)) == -sp.I,
                    'Clock phase orientation', 'path_clock_phase_identities')
        rows.append({'hops': n, 'vertices': M+1, 'edges': M,
                     'vertex_metric': [str(v) for v in vertices],
                     'edge_metric': [str(e) for e in edges],
                     'skew_spectrum': [f'i*{n-2*l}' for l in range(n+1)],
                     'kernel_dimension': 1, 'status': 'PASS'})
    for n in (1, 3, 5, 9):
        require(all(n-2*l != 0 for l in range(n+1)),
                'Odd-hop clock invertible', 'odd_clock_invertibility_checks')
    return {'even_hop_cases': rows,
            'odd_hop_full_space_obstruction': 'Odd n gives no clock zero mode. A nonempty ordinary finite graph/simplicial Hodge generator has an H0 kernel, so full-space unitary equivalence is excluded; restrictions/relative/coefficient variants are not addressed.',
            'phase_convention': 'S=diag(i^j), S H_C S-adjoint=i A; A upper diagonal is -sqrt((j+1)(n-j)).',
            'scope': 'New engineered weighted one-dimensional path only, per payload label. Does not derive native unit-metric Delta3 or a sourced UD coupling.'}


def finite_case(B):
    N = 1
    K = (B+1)*N+B
    payloads = list(itertools.product(range(2), repeat=3))
    labels = list(itertools.product(payloads, repeat=B+1))
    lookup = {x: i for i, x in enumerate(labels)}
    P = len(labels)
    actions = ['COMPUTE'] if B == 0 else ['COMPUTE', 'RESET_SWAP', 'COMPUTE']
    gates = []
    for action in actions:
        perm = []
        for x in labels:
            y = list(x)
            if action == 'COMPUTE':
                y[0] = compute_payload(y[0])
                require(compute_payload(y[0], True) == x[0], 'Gate inverse', 'payload_inverse_checks')
            else:
                y[0], y[1] = y[1], y[0]
                require(tuple(reversed(y)) == x, 'Swap inverse', 'payload_swap_inverse_checks')
            perm.append(lookup[tuple(y)])
        require(len(set(perm)) == P, 'Full dirty-register gate permutation', 'gate_permutations')
        gates.append(np.array(perm, dtype=int))
    prefixes = [np.arange(P)]
    for gate in gates:
        prefixes.append(gate[prefixes[-1]])
    D = np.array([j*P+int(prefixes[j][i]) for j in range(K+1) for i in range(P)])
    dim = (K+1)*P
    require(len(set(map(int, D))) == dim, 'Unitary block dressing', 'dressing_permutations')
    # Exact integer entries in the unnormalized symmetric clock basis.
    bare = sp.zeros(dim)
    for j in range(K):
        for p in range(P):
            bare[(j+1)*P+p, j*P+p] = j+1
            bare[j*P+p, (j+1)*P+p] = K-j
    dressed = sp.zeros(dim)
    for i in range(dim):
        for j in range(dim):
            if bare[i, j]:
                dressed[int(D[i]), int(D[j])] = bare[i, j]
    metric = [math.comb(K, j) for j in range(K+1) for _ in range(P)]
    entries = dressed.todok()
    for (i, j), a in entries.items():
        require(metric[i]*a == metric[j]*dressed[j, i],
                'Exact dressed metric self adjoint', 'dressed_metric_entries')
    # Exact edge label map is Q_{j+1} Q_j^{-1} = G_j on all payload labels.
    for j in range(K):
        inv = np.argsort(prefixes[j])
        edge = prefixes[j+1][inv]
        require(np.array_equal(edge, gates[j]), 'Prefix edge identity', 'prefix_edge_identities')
    minus_a = np.array([1, 0, 0, -1, 0, -1, 0, 1], dtype=int)
    minus_b = np.array([0, 1, -1, 0, -1, 0, 1, 0], dtype=int)
    minus = minus_a if B == 0 else (np.kron(minus_a, minus_b)-np.kron(minus_b, minus_a))
    require(np.any(minus), 'Nonzero common-minus payload witness')
    for gate in gates:
        image = np.empty_like(minus)
        image[gate] = minus
        require(np.array_equal(image, -minus), 'Exact common-minus gate eigenvector', 'common_minus_eigenvectors')
    # Similarity becomes ordinary Hermitian in normalized clock coordinates.
    hc = np.zeros((K+1, K+1))
    for j in range(K):
        hc[j+1, j] = hc[j, j+1] = math.sqrt((j+1)*(K-j))
    hbare = np.kron(hc, np.eye(P))
    hp = np.empty_like(hbare)
    hp[np.ix_(D, D)] = hbare
    require(np.array_equal(hp, hp.T), 'Normalized Hermitian Hamiltonian', 'numeric_hermiticity_checks')
    eigenvalues = scipy.linalg.eigvalsh(hp)
    expected_eigenvalues = np.sort(np.repeat(np.arange(-K, K+1, 2), P))
    spectrum_error = float(np.max(np.abs(eigenvalues-expected_eigenvalues)))
    require(spectrum_error < 1e-11, 'Scoped numerical isospectral diagnostic')
    # Correlate the work input to a reference, with fresh memory/records/donors.
    p0 = tuple([(0, 0, 0)]*(B+1))
    p1 = tuple([(1, 0, 0)]+[(0, 0, 0)]*B)
    i0, i1 = lookup[p0], lookup[p1]
    psi = np.zeros((dim, 2), dtype=complex)
    psi[i0, 0] = psi[i1, 1] = 1/math.sqrt(2)
    endpoint_expected = np.zeros_like(psi)
    endpoint_expected[K*P+prefixes[-1][i0], 0] = (-1j)**K/math.sqrt(2)
    endpoint_expected[K*P+prefixes[-1][i1], 1] = (-1j)**K/math.sqrt(2)

    def evolve(clock_t):
        ub = scipy.linalg.expm(-1j*hc*clock_t)
        full = np.empty((dim, dim), dtype=complex)
        full[np.ix_(D, D)] = np.kron(ub, np.eye(P))
        return full @ psi

    T = math.pi/2  # alpha=1 in uncalibrated units; not sourced SI time.
    endpoint = evolve(T)
    return_state = evolve(2*T)
    endpoint_error = float(np.linalg.norm(endpoint-endpoint_expected))
    return_error = float(np.linalg.norm(return_state-((-1)**K)*psi))
    require(endpoint_error < 1e-12 and return_error < 1e-12, 'Endpoint and return diagnostics')
    bare_endpoint = np.kron(scipy.linalg.expm(-1j*hc*T), np.eye(P)) @ psi
    bare_overlap = abs(np.vdot(endpoint_expected, bare_endpoint))
    bare_distance = math.sqrt(max(0.0, 1-float(bare_overlap)**2))
    midpoint = evolve(T/2)
    clock_probs = [float(np.sum(np.abs(midpoint[j*P:(j+1)*P])**2)) for j in range(K+1)]
    binomial_probs = [math.comb(K, j)/(2**K) for j in range(K+1)]
    require(max(abs(a-b) for a, b in zip(clock_probs, binomial_probs)) < 1e-12,
            'Intermediate coherent binomial clock probabilities')
    branch_errors = []
    midpoint_reference = np.zeros_like(midpoint)
    for j in range(K+1):
        amp = math.sqrt(math.comb(K, j))*(-1j)**j/(2**(K/2))
        midpoint_reference[j*P+prefixes[j][i0], 0] = amp/math.sqrt(2)
        midpoint_reference[j*P+prefixes[j][i1], 1] = amp/math.sqrt(2)
        branch_errors.append(float(np.linalg.norm(midpoint[j*P:(j+1)*P]-midpoint_reference[j*P:(j+1)*P])))
    require(max(branch_errors) < 1e-12, 'Coherent complete histories at all midpoint branches')
    # Compare the joint midpoint to any single fixed clock branch (best branch).
    best_single_clock_distance = math.sqrt(1-max(clock_probs))
    operator_gap = float(scipy.linalg.norm(hp-hbare, 2))
    require(operator_gap > 0, 'Gate dressing operator gap must not vanish')
    # Clock itself remains unchanged by a payload-only reset gate at the reset
    # address; the Hamiltonian clock is different from a payload reset resource.
    return {
        'd': 2, 'm': 2, 'N': N, 'B': B, 'K': K,
        'payload_dimension': P, 'joint_dimension': dim,
        'gateword': actions,
        'exact_algebra_scope': 'Entire dirty-register payload and all clock addresses; integer metric-adjoint and permutation identities.',
        'numeric_scope': 'Dense normalized Hamiltonian spectrum and correlated two-reference input evolution, alpha=1.',
        'normalized_hamiltonian_hermitian': True,
        'spectrum_max_abs_error': spectrum_error,
        'endpoint_vector_error': endpoint_error,
        'full_return_vector_error': return_error,
        'bare_clock_endpoint_joint_trace_distance': bare_distance,
        'midpoint_clock_probabilities': clock_probs,
        'midpoint_expected_binomial_probabilities': binomial_probs,
        'midpoint_history_branch_max_vector_error': max(branch_errors),
        'midpoint_best_single_clock_branch_joint_trace_distance': best_single_clock_distance,
        'dressed_vs_bare_operator_norm_gap': operator_gap,
        'operator_gap_exact_alpha_coefficient': 2*K,
        'operator_gap_exact_justification': 'An exact nonzero common-minus payload vector makes H_p=-H_bare on its clock sector; the clock top eigenvalue K attains gap 2K. Triangle norm bound supplies matching upper bound.',
        'T_in_alpha_units': 'pi/2', 'full_return_in_alpha_units': 'pi',
        'endpoint_phase': str((-1j)**K), 'full_return_phase': (-1)**K,
        'full_return_is_projective_not_necessarily_identity': True,
        'restart_resource_claim': 'None. Payload resets export records; full clock recurrence returns the entire coherent joint state including donor/outgoing registers.',
        'status': 'PASS'
    }


def main():
    result = {
        'version': '0.1',
        'role': 'Independent constructor-team AI algebra/code check; not independent human review.',
        'clock_exact_checks': spin_checks(),
        'weighted_path_exact_checks': weighted_path_checks(),
        'cases': [finite_case(0), finite_case(1)],
        'exact_check_counts': COUNTS,
        'proof_scope': [
            'All finite payload gates are permutations; D=sum_j |j><j| tensor Q_j is unitary.',
            'H_p=D(H_C tensor I)D-adjoint is Hermitian and isospectral to bare clock.',
            'The K commuting binary-spin X_i give exp(-i pi sum_i X_i/2)=(-i)^K X_1...X_K on the symmetric sector.',
            'Clock-zero input evolves at T=pi/(2 alpha) to clock-K with gateword Q_K, and at 2T returns projectively to the complete initial state.',
            'Intermediate clock positions are coherent superpositions of complete payload prefixes, not a succession of definite observed states.'
        ],
        'limitations': [
            'No native UD incidence/Hodge derivation, coupling locality, SI timing, energy source, error robustness, or measurement/Born bridge is established.',
            'Finite numerical diagnostics validate only the two explicit d=m=2,N=1,B=0 or 1 examples.',
            'Endpoint exactness is conditional on the prepared gate-dressed Hamiltonian and clock-zero state.',
            'Outgoing registers are retained in the closed joint system; a full recurrence reverses exports as well as computation.',
            'Any resource optimality or permanent absorbing/capture behavior remains unproved.'
        ],
        'physical_promotion': 0,
        'independent_human_review': 'PENDING',
        'overall_status': 'PASS'
    }
    result['checker_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    path = ROOT/'continuous-lift-parallel-results.json'
    path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'output': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                      'exact_check_counts': COUNTS, 'cases': result['cases'], 'status': 'PASS'}, indent=2))


if __name__ == '__main__':
    main()
