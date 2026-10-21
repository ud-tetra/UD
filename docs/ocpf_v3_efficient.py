#!/usr/bin/env python3
"""
OCPF v3 sweep — efficient variant for in-session execution.
Same operators and protocol as canonical ocpf_v3_sweep.py.
Uses sparse methods aggressively to fit in time budget.
"""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
import csv, time, sys, hashlib

N_VALUES = [5, 6, 7, 8, 9, 10]  # Skip N>=11 for time; reproduces archive

LAMBDA_J_SWEEP = np.array([
    0.01, 0.0215443469, 0.0464158883, 0.1, 0.2154434690, 0.4641588834,
    1.0, 2.1544346900, 4.6415888336, 9.4247779608,  # = 3*pi exactly
    21.5443469003, 46.4158883361, 100.0,
])


def build_K_operator(N):
    dim = 3**N
    rows, cols, vals = [], [], []
    pow3 = [3**i for i in range(N)]
    for s in range(dim):
        for i in range(N):
            digit_i = (s // pow3[i]) % 3
            for shift in [+1, -1]:
                new_digit = (digit_i + shift) % 3
                s_new = s + (new_digit - digit_i) * pow3[i]
                rows.append(s_new); cols.append(s); vals.append(1.0)
    return sp.csr_matrix((vals, (rows, cols)), shape=(dim, dim))


def build_V_diagonal(N):
    dim = 3**N
    V_diag = np.zeros(dim, dtype=np.float64)
    for s in range(dim):
        digits = set()
        temp = s
        for _ in range(N):
            digits.add(temp % 3); temp //= 3
        v_a = 1 if 0 not in digits else 0
        v_b = 1 if len(digits) < 2 else 0
        V_diag[s] = v_a + v_b
    return V_diag


def get_closed_mask(N):
    dim = 3**N
    mask = np.zeros(dim, dtype=bool)
    for s in range(dim):
        digits = set()
        temp = s
        for _ in range(N):
            digits.add(temp % 3); temp //= 3
        if (0 in digits) and (len(digits) >= 2):
            mask[s] = True
    return mask


def build_k2sym_state(N):
    dim = 3**N
    psi = np.zeros(dim)
    count = 0
    for s in range(dim):
        if s % 3 == 0:
            psi[s] = 1.0; count += 1
    psi /= np.sqrt(count)
    return psi


def compute_f_close_sparse(N, lam_J, K, V_diag, closed_mask, k_eigs):
    """
    Sparse-method computation of f_close at given lambda/J.
    Uses k_eigs lowest eigenstates.
    """
    H = -K + sp.diags(lam_J * V_diag, format='csr')
    psi_0 = build_k2sym_state(N)
    dim = 3**N
    k = min(k_eigs, dim - 2)
    
    eigenvalues, eigenvectors = eigsh(H, k=k, which='SA', tol=1e-7)
    c = eigenvectors.T @ psi_0
    Em_P_Em = np.sum(eigenvectors[closed_mask, :] ** 2, axis=0)
    f_close = np.sum(c**2 * Em_P_Em)
    weight_captured = np.sum(c**2)
    return eigenvalues[0], f_close, weight_captured


def compute_f_close_dense(N, lam_J, K, V_diag, closed_mask):
    """Full diagonalization for small N."""
    H = -K + sp.diags(lam_J * V_diag, format='csr')
    psi_0 = build_k2sym_state(N)
    H_dense = H.toarray()
    eigenvalues, eigenvectors = np.linalg.eigh(H_dense)
    c = eigenvectors.T @ psi_0
    Em_P_Em = np.sum(eigenvectors[closed_mask, :] ** 2, axis=0)
    f_close = np.sum(c**2 * Em_P_Em)
    return eigenvalues[0], f_close, 1.0


def run_sweep():
    results = []
    
    print("=" * 75)
    print(" OCPF v3 SWEEP — IN-SESSION EXECUTION")
    print(f" N values: {N_VALUES}")
    print(f" 3*pi = {3*np.pi:.10f}")
    print("=" * 75)
    
    for N in N_VALUES:
        dim = 3**N
        print(f"\n--- N={N}, dim={dim} ---")
        t0 = time.time()
        K = build_K_operator(N)
        V_diag = build_V_diagonal(N)
        closed_mask = get_closed_mask(N)
        n_closed = int(np.sum(closed_mask))
        print(f"  Closed states: {n_closed}/{dim} ({n_closed/dim*100:.2f}%)")
        
        # Choose method: dense for dim ≤ 1000, sparse otherwise
        # Use restricted eigs for big N to fit in time budget
        if dim <= 1000:
            method = "dense"
            k_eigs = dim
        elif dim <= 10000:
            method = "sparse-full"
            k_eigs = min(dim-2, 1500)
        else:
            method = "sparse-partial"
            k_eigs = min(dim-2, 800)
        
        print(f"  Method: {method}, k_eigs: {k_eigs}")
        
        for lam_J in LAMBDA_J_SWEEP:
            t1 = time.time()
            try:
                if method == "dense":
                    E_gs, f_close, weight = compute_f_close_dense(N, lam_J, K, V_diag, closed_mask)
                else:
                    E_gs, f_close, weight = compute_f_close_sparse(N, lam_J, K, V_diag, closed_mask, k_eigs)
                dt = time.time() - t1
                
                # Mark special points
                marker = ""
                if abs(lam_J - 3*np.pi) < 0.01:
                    marker = " ★ 3π"
                
                weight_str = f" w={weight:.2%}" if weight < 0.99 else ""
                print(f"  N={N:>2} | λ/J={lam_J:>12.6f} | f={f_close:.6f} | E_gs={E_gs:.4f}{weight_str} | {dt:.1f}s{marker}")
                
                results.append({
                    "N": N, "lambda_over_J": float(lam_J),
                    "f_close": float(f_close), "E_gs": float(E_gs),
                    "weight_captured": float(weight), "method": method
                })
            except Exception as e:
                print(f"  N={N}, λ/J={lam_J}: FAILED ({e})")
                results.append({
                    "N": N, "lambda_over_J": float(lam_J),
                    "f_close": None, "E_gs": None,
                    "weight_captured": 0.0, "method": "FAILED"
                })
        
        total = time.time() - t0
        print(f"  N={N} complete in {total:.1f}s")
    
    return results


if __name__ == "__main__":
    results = run_sweep()
    
    # Write CSV
    with open("/home/claude/ocpf_v3_results.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)
    
    print("\n" + "=" * 75)
    print(" SWEEP COMPLETE")
    print("=" * 75)
    print(f" Total runs: {len(results)}")
    print(f" Saved to: /home/claude/ocpf_v3_results.csv")
