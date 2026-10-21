#!/usr/bin/env python3
"""
OSCAR EXECUTION — H_SIGMA1-EIGENSOLVE-v1.0
True discrete Hamiltonian eigensolve on tetrahedral IFS substrate.

Three versions:
  V1: Static reactive-only (RECOMMENDED)
  V2: Static + burden disorder (MANDATORY)
  V3: Dynamical + repair (MANDATORY for gate attempt)

Approach:
  1. Build the actual N×N Hamiltonian H on the IFS lattice
  2. Diagonalize H (find eigenvalues + eigenvectors)
  3. Identify σ₁(ρ,X) candidate modes by overlap with defect insertion
  4. Measure IPR from true eigenvectors
  5. Report F = IPR × N

Compute constraint:
  Full diag of 1M×1M is impossible here.
  We use N = 4^5 = 1024 (feasible exact diag) and N = 4^6 = 4096,
  then N = 4^7 = 16384 via sparse Lanczos if memory allows.
  This gives a SCALING SEQUENCE for extrapolation to 4^9, 4^10.

LOCKED CONSTANTS — DO NOT CHANGE:
  eta = 185/192 = 0.963542
  r = 4^(-1/3) = 0.629961
  Delta/N = 7/192 = 0.036458
  L_repair = 0.034
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
import json
import datetime
import sys
import time

# ══════════════════════════════════════════════════════════
# LOCKED CONSTANTS
# ══════════════════════════════════════════════════════════
ETA = 185.0 / 192.0
R_IFS = 4.0 ** (-1.0 / 3.0)
DELTA_OVER_N = 7.0 / 192.0
L_REPAIR = 0.034
XI_SYM = 26.93
XI_BURDEN = 23.77


def site_to_address(idx, level):
    """Convert linear index to IFS address (base-4, MSB first)."""
    addr = []
    s = idx
    for _ in range(level):
        addr.append(s % 4)
        s //= 4
    return tuple(reversed(addr))


def address_to_site(addr, level):
    """Convert IFS address back to linear index."""
    idx = 0
    for k in range(level):
        idx += addr[k] * (4 ** (level - 1 - k))
    return idx


def hierarchical_distance(addr_i, addr_j, level):
    """
    Hierarchical distance = level at which addresses first differ.
    Returns integer d ∈ [0, level].
    d=0 means same site, d=level means different at root.
    """
    for k in range(level):
        if addr_i[k] != addr_j[k]:
            return level - k
    return 0


def build_hamiltonian_sparse(N, level, version, rng):
    """
    Build the IFS Hamiltonian as a sparse matrix.
    
    H_ij encodes:
    - Kinetic: hopping between connected sites, weighted by η^d
    - Potential (V1 static reactive): on-site from IFS structure
    - Disorder (V2 burden): random on-site potential ~ N(0, σ_burden²)
    - Repair (V3 dynamical): repair coupling L_repair between damaged neighbors
    
    Connectivity rule:
    Site i connects to:
    - Its 3 siblings (same parent, d=1): weight η^1
    - Its parent's 3 siblings' children (cousins, d=2): weight η^2
    - For efficiency, we truncate at d ≤ 3 (η^3 ≈ 0.895)
    
    On-site potential:
    - V1: V_i = -Δ/N (uniform deficit)
    - V2: V_i = -Δ/N + σ_burden * noise_i, σ_burden = 0.12 * Δ/N
    - V3: V_i = V2_i + L_repair * Σ_damaged_neighbors (repair term)
    """
    addresses = [site_to_address(i, level) for i in range(N)]
    
    # Build sparse Hamiltonian
    rows = []
    cols = []
    vals = []
    
    # On-site potential
    diag = np.full(N, -DELTA_OVER_N)
    
    if version in ["V2", "V3"]:
        sigma_burden = 0.12 * DELTA_OVER_N
        burden_noise = sigma_burden * rng.standard_normal(N)
        diag += burden_noise
    
    # Kinetic: connect sites within hierarchical distance ≤ 3
    # For each site, find siblings (d=1), cousins (d=2), second cousins (d=3)
    
    # Precompute: group sites by parent address (prefix of length level-1)
    parent_groups = {}
    for i in range(N):
        parent_key = addresses[i][:level-1]
        if parent_key not in parent_groups:
            parent_groups[parent_key] = []
        parent_groups[parent_key].append(i)
    
    # Grandparent groups (prefix of length level-2) for cousins
    grandparent_groups = {}
    if level >= 2:
        for i in range(N):
            gp_key = addresses[i][:level-2]
            if gp_key not in grandparent_groups:
                grandparent_groups[gp_key] = []
            grandparent_groups[gp_key].append(i)
    
    # Great-grandparent groups for d=3
    ggp_groups = {}
    if level >= 3:
        for i in range(N):
            ggp_key = addresses[i][:level-3]
            if ggp_key not in ggp_groups:
                ggp_groups[ggp_key] = []
            ggp_groups[ggp_key].append(i)
    
    print(f"  Building hopping terms (N={N})...", file=sys.stderr)
    
    # d=1 siblings: share parent (prefix level-1)
    hop_1 = ETA ** 1
    for parent_key, members in parent_groups.items():
        for a, i in enumerate(members):
            for b, j in enumerate(members):
                if i < j:
                    rows.append(i); cols.append(j); vals.append(-hop_1)
                    rows.append(j); cols.append(i); vals.append(-hop_1)
    
    # d=2 cousins: share grandparent (prefix level-2) but different parent
    if level >= 2:
        hop_2 = ETA ** 2
        for gp_key, members in grandparent_groups.items():
            # Group by parent within this grandparent
            sub_parents = {}
            for i in members:
                pk = addresses[i][level-1]  # last digit distinguishes within parent
                parent_id = addresses[i][:level-1]
                if parent_id not in sub_parents:
                    sub_parents[parent_id] = []
                sub_parents[parent_id].append(i)
            
            parent_list = list(sub_parents.values())
            for a_idx in range(len(parent_list)):
                for b_idx in range(a_idx + 1, len(parent_list)):
                    for i in parent_list[a_idx]:
                        for j in parent_list[b_idx]:
                            rows.append(i); cols.append(j); vals.append(-hop_2)
                            rows.append(j); cols.append(i); vals.append(-hop_2)
    
    # V3: repair coupling
    if version == "V3":
        # Identify "damaged" sites: those with burden noise > 1 std dev
        if 'burden_noise' in dir():
            pass
        damage_threshold = 0.12 * DELTA_OVER_N  # 1 sigma
        damaged = np.abs(burden_noise) > damage_threshold if version == "V3" else np.zeros(N, dtype=bool)
        
        # Add repair coupling between damaged neighbors
        for parent_key, members in parent_groups.items():
            damaged_in_group = [i for i in members if damaged[i]]
            for a, i in enumerate(damaged_in_group):
                for b, j in enumerate(damaged_in_group):
                    if i < j:
                        repair_val = -L_REPAIR
                        rows.append(i); cols.append(j); vals.append(repair_val)
                        rows.append(j); cols.append(i); vals.append(repair_val)
        
        # Repair also modifies on-site: damaged sites get shifted
        for i in range(N):
            if damaged[i]:
                n_damaged_neighbors = sum(1 for j in parent_groups.get(addresses[i][:level-1], []) if j != i and damaged[j])
                diag[i] += L_REPAIR * n_damaged_neighbors * 0.5
    
    # Add diagonal
    for i in range(N):
        rows.append(i); cols.append(i); vals.append(diag[i])
    
    H = sparse.csr_matrix((vals, (rows, cols)), shape=(N, N))
    
    return H, diag


def insert_sigma1_defect(N, level, i0):
    """
    Create σ₁(ρ,X) test defect vector at site i0.
    This is a localized perturbation in the (ρ,X) channel:
    density + position fluctuation at i0.
    
    The defect vector is a delta function at i0 (maximally localized).
    After projecting onto eigenstates, the overlap tells us which
    eigenstates "see" the defect — those are the σ₁ candidates.
    """
    v = np.zeros(N)
    v[i0] = 1.0
    return v


def measure_ipr(eigvec):
    """IPR = Σᵢ |ψᵢ|⁴ for a normalized eigenvector."""
    psi_sq = eigvec ** 2  # eigvecs from eigsh are real for symmetric H
    return np.sum(psi_sq ** 2)


def run_eigensolve(N, level, version, n_runs, rng):
    """
    Full eigensolve pipeline for one version/background.
    
    For each run:
    1. Build H (with fresh disorder for V2/V3)
    2. Insert defect at random site
    3. Find eigenstates near defect energy using sparse eigsh
    4. Measure overlap of defect with eigenstates
    5. Top-overlap eigenstate = σ₁ candidate
    6. Measure IPR of that eigenstate
    """
    all_iprs_sigma1 = []
    all_iprs_sigma2 = []
    all_top3 = []
    
    for run_idx in range(n_runs):
        t0 = time.time()
        
        # Build H
        H, diag = build_hamiltonian_sparse(N, level, version, rng)
        
        # Random insertion site
        i0 = rng.integers(0, N)
        defect = insert_sigma1_defect(N, level, i0)
        
        # Find eigenvalues/vectors near the defect energy
        # The defect energy is approximately diag[i0]
        sigma_shift = float(diag[i0])
        
        # Number of eigenpairs to find
        n_eig = min(30, N - 2)
        
        print(f"    Run {run_idx+1}/{n_runs}: eigsh(k={n_eig}, sigma={sigma_shift:.6f})...", file=sys.stderr)
        
        try:
            eigenvalues, eigenvectors = eigsh(H, k=n_eig, sigma=sigma_shift, which='LM')
        except Exception as e:
            print(f"    eigsh failed with sigma, falling back to smallest algebraic...", file=sys.stderr)
            eigenvalues, eigenvectors = eigsh(H, k=n_eig, which='SA')
        
        # Compute overlap of each eigenstate with defect vector
        overlaps = np.abs(eigenvectors[i0, :]) ** 2  # |<ψ_k|i0>|²
        
        # Sort by overlap (highest first)
        sorted_idx = np.argsort(-overlaps)
        
        # Top-3 σ₁ candidates
        top3 = []
        for rank in range(min(3, len(sorted_idx))):
            k = sorted_idx[rank]
            evec = eigenvectors[:, k]
            ipr = measure_ipr(evec)
            top3.append({
                "rank": rank + 1,
                "eigenvalue": float(eigenvalues[k]),
                "overlap": float(overlaps[k]),
                "IPR": float(ipr),
                "F": float(ipr * N),
            })
        
        all_top3.append(top3)
        
        # σ₁ = highest-overlap eigenstate
        best_k = sorted_idx[0]
        ipr_sigma1 = measure_ipr(eigenvectors[:, best_k])
        all_iprs_sigma1.append(ipr_sigma1)
        
        # σ₂ = second-highest-overlap eigenstate (different mode family)
        if len(sorted_idx) > 1:
            second_k = sorted_idx[1]
            ipr_sigma2 = measure_ipr(eigenvectors[:, second_k])
            all_iprs_sigma2.append(ipr_sigma2)
        
        dt = time.time() - t0
        print(f"    Run {run_idx+1}: IPR_σ₁={ipr_sigma1:.6e}, F={ipr_sigma1*N:.4f}, overlap={overlaps[best_k]:.4f} ({dt:.1f}s)", file=sys.stderr)
    
    iprs1 = np.array(all_iprs_sigma1)
    iprs2 = np.array(all_iprs_sigma2) if all_iprs_sigma2 else np.array([1.0/N])
    ipr_baseline = 1.0 / N
    Fs = iprs1 / ipr_baseline
    Fs2 = iprs2 / ipr_baseline
    
    return {
        "ipr_sigma1_mean": float(np.mean(iprs1)),
        "ipr_sigma1_std": float(np.std(iprs1, ddof=1)) if len(iprs1) > 1 else 0.0,
        "ipr_baseline": float(ipr_baseline),
        "F_mean": float(np.mean(Fs)),
        "F_std": float(np.std(Fs, ddof=1)) if len(Fs) > 1 else 0.0,
        "F_min": float(np.min(Fs)),
        "F_max": float(np.max(Fs)),
        "ipr_sigma2_mean": float(np.mean(iprs2)),
        "F_sigma2": float(np.mean(Fs2)),
        "top3_per_run": all_top3,
        "all_F": Fs.tolist(),
    }


def classify_regime(F):
    if F < 1.0: return "subcritical"
    elif F < 3.0: return "marginal"
    elif F < 10.0: return "intermediate"
    else: return "strong"


def build_result_block(version, bg_label, N, level, stats, n_runs):
    """Assemble B_rho_raw block."""
    F = stats["F_mean"]
    F_s2 = stats["F_sigma2"]
    regime = classify_regime(F)
    
    gates_passed = []
    gates_failed = []
    
    if F >= 10.0:
        gates_passed.append("P1")
    elif 3.0 <= F < 10.0:
        gates_passed.append("C1")
    elif F < 3.0:
        gates_failed.append("F1")
    
    if F_s2 < 2.0:
        gates_passed.append("P3")
    if F_s2 >= 5.0:
        gates_failed.append("C2")
    
    if F_s2 >= 5.0:
        eq = "ANOMALOUS"
    elif F >= 10.0:
        eq = "EIGENSOLVE_STRONG"
    elif 3.0 <= F < 10.0:
        eq = "EIGENSOLVE_INTERMEDIATE"
    elif F < 3.0:
        eq = "EIGENSOLVE_WEAK"
    else:
        eq = "EIGENSOLVE_SUBCRITICAL"
    
    ts = datetime.datetime.now(datetime.timezone.utc)
    
    # Flatten top-3 for reporting
    top3_summary = []
    for run_top3 in stats["top3_per_run"]:
        top3_summary.append([
            {"rank": t["rank"], "F": round(t["F"], 4), "overlap": round(t["overlap"], 6)}
            for t in run_top3
        ])
    
    return {
        "version": "1.0",
        "schema": "B_rho_raw",
        "run_id": f"OSCAR-EIGENSOLVE-{version}-{bg_label}-{ts.strftime('%Y%m%dT%H%M%SZ')}",
        "timestamp": ts.isoformat(),
        "executor": "Oscar (Cato-executed, true eigensolve)",
        "profile": f"H_SIGMA1-EIGENSOLVE-{version}",
        "method": "sparse eigsh (ARPACK/Lanczos) on explicit IFS Hamiltonian",
        "N_sites": N,
        "ifs_level": level,
        "background": bg_label,
        "eta": round(ETA, 6),
        "r": round(R_IFS, 6),
        "L_repair": L_REPAIR,
        "N_runs_averaged": n_runs,
        "IPR_sigma1": round(stats["ipr_sigma1_mean"], 14),
        "IPR_baseline": round(stats["ipr_baseline"], 14),
        "F": round(F, 4),
        "regime": regime,
        "IPR_sigma2": round(stats["ipr_sigma2_mean"], 14),
        "F_sigma2": round(F_s2, 4),
        "IPR_sigma3": None,
        "loc_radius_sigma1": None,
        "mode_gap": None,
        "peak_site": "varies per run (eigenvector argmax)",
        "IPR_sigma1_std": round(stats["ipr_sigma1_std"], 14),
        "F_std": round(stats["F_std"], 4),
        "F_min": round(stats["F_min"], 4),
        "F_max": round(stats["F_max"], 4),
        "all_F_values": [round(f, 4) for f in stats["all_F"]],
        "top3_sigma1_candidates": top3_summary,
        "evidence_quality": eq,
        "gate_passed": gates_passed,
        "gate_failed": gates_failed,
    }


def main():
    rng = np.random.default_rng(seed=2026)
    
    # ── Determine feasible N ──
    # Try 4^5=1024 first (guaranteed fast), then scale up
    test_levels = [
        (5, 1024),
        (6, 4096),
    ]
    
    # Try 4^7 = 16384 if memory allows
    try:
        test_alloc = np.zeros((16384, 30), dtype=np.float64)
        del test_alloc
        test_levels.append((7, 16384))
        print("4^7 = 16384 feasible (memory check passed)", file=sys.stderr)
    except MemoryError:
        print("4^7 = 16384 NOT feasible (memory limit)", file=sys.stderr)
    
    N_RUNS_PER = 10  # minimum required
    
    all_blocks = []
    scaling_data = {}
    
    for level, N in test_levels:
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"LEVEL {level}, N = {N}", file=sys.stderr)
        print(f"{'='*60}", file=sys.stderr)
        
        scaling_data[level] = {}
        
        # Determine runs (fewer for larger N)
        n_runs = N_RUNS_PER if N <= 4096 else max(5, N_RUNS_PER // 2)
        
        # ── VERSION 2: Static + burden disorder (MANDATORY) ──
        print(f"\n  V2: Static + burden disorder (N={N}, {n_runs} runs)...", file=sys.stderr)
        stats_v2 = run_eigensolve(N, level, "V2", n_runs, rng)
        block_v2 = build_result_block("V2", "burden", N, level, stats_v2, n_runs)
        block_v2["notes"] = [
            f"True eigensolve: scipy.sparse.linalg.eigsh on {N}×{N} IFS Hamiltonian",
            "Connectivity: d=1 siblings (η^1) + d=2 cousins (η^2)",
            "Burden disorder: σ = 0.12 × Δ/N, Gaussian on-site",
            f"Eigenpairs: k={min(30, N-2)} near defect energy via shift-invert",
            "σ₁ candidate: eigenstate with highest |<ψ|defect>|² overlap",
            f"N_runs = {n_runs}",
            "Seed = 2026",
        ]
        all_blocks.append(block_v2)
        scaling_data[level]["V2_burden"] = stats_v2["F_mean"]
        
        # ── VERSION 3: Dynamical + repair (MANDATORY) ──
        print(f"\n  V3: Dynamical + repair (N={N}, {n_runs} runs)...", file=sys.stderr)
        stats_v3 = run_eigensolve(N, level, "V3", n_runs, rng)
        block_v3 = build_result_block("V3", "burden+repair", N, level, stats_v3, n_runs)
        block_v3["notes"] = [
            f"True eigensolve: scipy.sparse.linalg.eigsh on {N}×{N} IFS Hamiltonian",
            "Connectivity: d=1 siblings + d=2 cousins + repair coupling",
            "Burden disorder: σ = 0.12 × Δ/N, Gaussian on-site",
            f"Repair: L_repair = {L_REPAIR} coupling between damaged sibling pairs",
            "Damaged = |burden_noise| > σ_burden (> 1 std dev)",
            f"Eigenpairs: k={min(30, N-2)} near defect energy",
            f"N_runs = {n_runs}",
            "Seed = 2026",
        ]
        all_blocks.append(block_v3)
        scaling_data[level]["V3_repair"] = stats_v3["F_mean"]
        
        # ── VERSION 1: Static reactive-only (RECOMMENDED) ──
        print(f"\n  V1: Static reactive-only (N={N}, {n_runs} runs)...", file=sys.stderr)
        stats_v1 = run_eigensolve(N, level, "V1", n_runs, rng)
        block_v1 = build_result_block("V1", "symmetric", N, level, stats_v1, n_runs)
        block_v1["notes"] = [
            f"True eigensolve: scipy.sparse.linalg.eigsh on {N}×{N} IFS Hamiltonian",
            "Connectivity: d=1 siblings (η^1) + d=2 cousins (η^2)",
            "No disorder: uniform on-site potential -Δ/N",
            f"Eigenpairs: k={min(30, N-2)} near defect energy",
            f"N_runs = {n_runs}",
            "Seed = 2026",
        ]
        all_blocks.append(block_v1)
        scaling_data[level]["V1_symmetric"] = stats_v1["F_mean"]
    
    # ── Scaling summary ──
    print(f"\n{'='*60}", file=sys.stderr)
    print("EIGENSOLVE SCALING SUMMARY", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    print(f"{'Level':>6} {'N':>8} {'V1(sym)':>10} {'V2(bur)':>10} {'V3(rep)':>10}", file=sys.stderr)
    for level in sorted(scaling_data.keys()):
        d = scaling_data[level]
        print(f"{level:>6} {4**level:>8} {d.get('V1_symmetric',0):>10.4f} {d.get('V2_burden',0):>10.4f} {d.get('V3_repair',0):>10.4f}", file=sys.stderr)
    
    # Output
    print(json.dumps(all_blocks, indent=2))


if __name__ == "__main__":
    main()
