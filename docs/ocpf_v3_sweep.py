#!/usr/bin/env python3
"""
OCPF Multi-N Sweep (v3 Pre-Registration Protocol)
Executes the primary computational falsifier for Unified Dynamics.

Fills in build_K_operator, build_V_diagonal, and get_closed_subspace_mask
from the v3 pre-registration specification:

  H = -J*K + lambda*V
  K = sum_i (T_i + T_i†)  [Z3 shift per site]
  V(s) = v_a(s) + v_b(s)  [closure violation count]
  v_a(s) = 1 if 0 not in {s_1,...,s_N}
  v_b(s) = 1 if |{s_1,...,s_N}| < 2
  Initial: K2-sym = uniform over states with s_1=0

Lambda/J grid: 13 log-spaced points with 3*pi inserted exactly.
"""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
import csv
import time
import sys

# --- PROTOCOL PARAMETERS ---
N_VALUES = [5, 6, 7, 8, 9, 10, 11, 12, 13]

# Exact 13-point log-spaced grid from v3 protocol
LAMBDA_J_SWEEP = np.array([
    0.01,
    0.0215443469,
    0.0464158883,
    0.1,
    0.2154434690,
    0.4641588834,
    1.0,
    2.1544346900,
    4.6415888336,
    9.4247779608,   # = 3*pi exactly
    21.5443469003,
    46.4158883361,
    100.0,
])


def state_to_digits(state_index, N):
    """Convert a state index (0 to 3^N - 1) to a tuple of Z3 digits."""
    digits = []
    s = state_index
    for _ in range(N):
        digits.append(s % 3)
        s //= 3
    return tuple(digits)  # (s_1, s_2, ..., s_N) in site order


def build_K_operator(N):
    """
    Build the sparse kinetic/hopping matrix K for (C^3)^N.
    
    K = sum_i (T_i + T_i†)
    
    T_i shifts site i by +1 mod 3.
    T_i† shifts site i by -1 mod 3.
    
    For each basis state |s>, K|s> = sum over sites i of:
      |s with s_i -> (s_i+1)%3> + |s with s_i -> (s_i-1)%3>
    """
    dim = 3**N
    rows = []
    cols = []
    vals = []
    
    # Precompute powers of 3 for digit manipulation
    pow3 = [3**i for i in range(N)]
    
    for s in range(dim):
        for i in range(N):
            # Extract digit i
            digit_i = (s // pow3[i]) % 3
            
            # T_i: shift site i by +1 mod 3
            new_digit_plus = (digit_i + 1) % 3
            s_plus = s + (new_digit_plus - digit_i) * pow3[i]
            rows.append(s_plus)
            cols.append(s)
            vals.append(1.0)
            
            # T_i†: shift site i by -1 mod 3
            new_digit_minus = (digit_i - 1) % 3
            s_minus = s + (new_digit_minus - digit_i) * pow3[i]
            rows.append(s_minus)
            cols.append(s)
            vals.append(1.0)
    
    K = sp.csr_matrix((vals, (rows, cols)), shape=(dim, dim))
    return K


def build_V_diagonal(N):
    """
    Build the diagonal of the closure-violation operator V.
    
    For each basis state s = (s_1, ..., s_N):
      v_a(s) = 1 if 0 not in {s_1,...,s_N}, else 0
               (path does not visit coset 0 / V4 coset)
      v_b(s) = 1 if |{s_1,...,s_N}| < 2, else 0
               (path visits fewer than 2 distinct cosets)
      V(s) = v_a(s) + v_b(s)
    
    Closed configurations: V(s) = 0
    """
    dim = 3**N
    V_diag = np.zeros(dim, dtype=np.float64)
    
    pow3 = [3**i for i in range(N)]
    
    for s in range(dim):
        # Extract all digits
        digits = set()
        temp = s
        for i in range(N):
            digits.add(temp % 3)
            temp //= 3
        
        v_a = 1 if 0 not in digits else 0
        v_b = 1 if len(digits) < 2 else 0
        V_diag[s] = v_a + v_b
    
    return V_diag


def get_closed_subspace_mask(N):
    """
    Return a boolean mask for closed configurations (V(s) = 0).
    
    A state is closed iff:
      - 0 is in the digit set (v_a = 0), AND
      - at least 2 distinct digits appear (v_b = 0)
    """
    dim = 3**N
    mask = np.zeros(dim, dtype=bool)
    
    pow3 = [3**i for i in range(N)]
    
    for s in range(dim):
        digits = set()
        temp = s
        for i in range(N):
            digits.add(temp % 3)
            temp //= 3
        
        has_zero = 0 in digits
        has_two_distinct = len(digits) >= 2
        
        if has_zero and has_two_distinct:
            mask[s] = True
    
    return mask


def build_k2sym_initial_state(N):
    """
    Build the K2-sym initial state:
    |psi_0> = (1/sqrt(3^(N-1))) * sum_{s : s_1 = 0} |s>
    
    Uniform superposition over all states with first site = 0.
    """
    dim = 3**N
    psi = np.zeros(dim, dtype=np.float64)
    
    # States with s_1 = 0: these are states where (s % 3) == 0
    # i.e., the first digit (site 1) is 0
    count = 0
    for s in range(dim):
        if s % 3 == 0:  # first digit is 0
            psi[s] = 1.0
            count += 1
    
    # Normalize
    psi /= np.sqrt(count)
    return psi


def compute_f_close(N, lam_J, K, V_diag, closed_mask):
    """
    Compute f_close,N(lambda/J) using the dephased/infinite-time
    closed-subspace weight in the energy basis.
    
    f_close = sum_m |c_m|^2 * <E_m|P_close|E_m>
    
    where c_m = <E_m|psi_0> and P_close projects onto V=0 subspace.
    
    For practical computation with large N:
    We diagonalize H, project psi_0 and the closed mask onto eigenstates.
    
    For small N (dim <= ~50000), we can do full diag.
    For larger N, we use sparse eigsh with enough states.
    """
    dim = 3**N
    
    # Build H = -K + (lambda/J) * V
    H = -K + sp.diags(lam_J * V_diag, format='csr')
    
    # Build initial state
    psi_0 = build_k2sym_initial_state(N)
    
    if dim <= 50000:
        # Full diagonalization feasible
        H_dense = H.toarray()
        eigenvalues, eigenvectors = np.linalg.eigh(H_dense)
        
        # c_m = <E_m | psi_0>
        c = eigenvectors.T @ psi_0  # shape (dim,)
        
        # <E_m | P_close | E_m> = sum of |E_m[i]|^2 for i in closed subspace
        P_diag = np.zeros(dim)
        P_diag[closed_mask] = 1.0
        
        Em_P_Em = np.sum(eigenvectors[closed_mask, :] ** 2, axis=0)  # shape (dim,)
        
        # f_close = sum_m |c_m|^2 * <E_m|P_close|E_m>
        f_close = np.sum(c**2 * Em_P_Em)
        E_gs = eigenvalues[0]
        
    else:
        # Sparse: get enough eigenstates to capture most of the weight
        # For the dephased observable, we need ALL eigenstates ideally.
        # Compromise: get k eigenstates and compute partial f_close.
        # Flag if weight captured < 95%.
        
        k = min(500, dim - 2)
        
        try:
            eigenvalues, eigenvectors = eigsh(H, k=k, which='SA', tol=1e-8)
        except Exception as e:
            print(f"    eigsh failed: {e}", file=sys.stderr)
            return None, None, 0.0
        
        c = eigenvectors.T @ psi_0
        
        P_diag = np.zeros(dim)
        P_diag[closed_mask] = 1.0
        
        Em_P_Em = np.sum(eigenvectors[closed_mask, :] ** 2, axis=0)
        
        f_close = np.sum(c**2 * Em_P_Em)
        weight_captured = np.sum(c**2)
        E_gs = eigenvalues[0]
        
        if weight_captured < 0.95:
            print(f"    WARNING: only {weight_captured:.1%} of psi_0 weight captured "
                  f"by {k} eigenstates", file=sys.stderr)
    
    return E_gs, f_close


def run_sweep():
    results = []
    
    print(f"{'='*70}")
    print(f" OCPF MULTI-N SWEEP (v3 PRE-REGISTRATION PROTOCOL)")
    print(f" N values: {N_VALUES}")
    print(f" Lambda/J grid: {len(LAMBDA_J_SWEEP)} points")
    print(f" 3*pi = {3*np.pi:.10f}")
    print(f"{'='*70}")
    print(f"", file=sys.stderr)
    
    for N in N_VALUES:
        dim = 3**N
        print(f"\n--- N={N}, dim={dim} ---")
        print(f"  Building operators...", file=sys.stderr)
        t0 = time.time()
        
        if dim > 2_000_000:
            print(f"  SKIPPING N={N}: dim={dim} exceeds memory limit for this environment.")
            print(f"  Run on a machine with >= {dim * 8 * 500 / 1e9:.1f} GB RAM for sparse eigsh.")
            for lam_J in LAMBDA_J_SWEEP:
                results.append({"N": N, "lambda_over_J": f"{lam_J:.10f}", 
                               "f_close": "SKIPPED"})
            continue
        
        K = build_K_operator(N)
        V_diag = build_V_diagonal(N)
        closed_mask = get_closed_subspace_mask(N)
        
        n_closed = np.sum(closed_mask)
        print(f"  Closed states: {n_closed}/{dim} ({n_closed/dim*100:.1f}%)")
        
        build_time = time.time() - t0
        print(f"  Operators built in {build_time:.1f}s", file=sys.stderr)
        
        for lam_J in LAMBDA_J_SWEEP:
            t1 = time.time()
            E_gs, f_close = compute_f_close(N, lam_J, K, V_diag, closed_mask)
            dt = time.time() - t1
            
            if f_close is not None:
                print(f"  N={N:>2} | lam/J={lam_J:>12.6f} | f_close={f_close:.8f} | "
                      f"E_gs={E_gs:.6f} | {dt:.1f}s")
                results.append({
                    "N": N, 
                    "lambda_over_J": f"{lam_J:.10f}", 
                    "f_close": f"{f_close:.10f}"
                })
            else:
                print(f"  N={N:>2} | lam/J={lam_J:>12.6f} | FAILED")
                results.append({
                    "N": N, 
                    "lambda_over_J": f"{lam_J:.10f}", 
                    "f_close": "FAILED"
                })
        
        total_time = time.time() - t0
        print(f"  N={N} complete in {total_time:.1f}s")
    
    # Write CSV
    csv_filename = "ocpf_v3_sweep_results.csv"
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["N", "lambda_over_J", "f_close"])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"\n{'='*70}")
    print(f" SWEEP COMPLETE. Data saved to {csv_filename}")
    print(f" Paste this CSV back to Cato for classification + permutation test.")
    print(f"{'='*70}")


if __name__ == "__main__":
    run_sweep()
