#!/usr/bin/env python3
"""
OSCAR EXECUTION — H_MULTI-EIGENSOLVE Version A
2N×2N two-channel (ρ,Θ) Hamiltonian on tetrahedral IFS.
No burden. No damping. Clean channel structure only.

Purpose: Resolve C2 — is σ₂ localization a scalar-lane artifact
or a true multi-channel finding?

Operator:
  H_multi = [[H_ρρ,   H_ρΘ  ],
             [H_ρΘᵀ,  H_ΘΘ  ]]

  H_ρρ: hopping η², on-site λ_ρ(1-η^h)
  H_ΘΘ: hopping η⁴, on-site λ_Θ(η^h - η^{2h})
  H_ρΘ: diagonal only, μ·X_i·Y_i coupling
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
ETA = 185.0 / 192.0           # 0.963542
ETA2 = ETA ** 2                # 0.92842
ETA4 = ETA ** 4                # 0.86200
LAMBDA_RHO = 7.0 / 192.0      # 0.036458
LAMBDA_THETA = ETA * (1 - ETA) # 0.035123
MU_ANSATZ = np.sqrt(LAMBDA_RHO * LAMBDA_THETA)  # ≈ 0.03579
MU_ALT = (7.0 / 192.0) ** 2   # ≈ 0.00133

NEAR_DEGEN_THRESHOLD = 0.10  # 10% eigenvalue gap


def site_to_address(idx, level):
    addr = []
    s = idx
    for _ in range(level):
        addr.append(s % 4)
        s //= 4
    return tuple(reversed(addr))


def get_depth(idx, level):
    """Depth h_i from root. Root children = 1, leaves = level."""
    # On a tetrahedral IFS at level H, all sites are leaves at depth H.
    # But the "effective depth" from root structure:
    # h_i = level for all sites at the finest resolution.
    # However, the spec uses h_i as depth from root, where
    # sites in sub-tetrahedron k at level m have h = m.
    # Since we only have leaf sites (at level H), h_i = H for all.
    # BUT: the potential terms use h_i to create depth-dependent structure.
    # For leaf-only representation, we need the hierarchical address
    # to define an effective depth that varies.
    #
    # Interpretation: h_i = the depth at which site i's address
    # first becomes unique. For a site in a deep corner, h is large.
    # For practical purposes with leaf-only sites:
    # h_i = level for all leaves. But that makes all potentials identical.
    #
    # Better interpretation: use the HIERARCHICAL POSITION to create
    # depth-dependent structure. Sites near the "root vertex" of the
    # tetrahedron (address 0,0,0,...) have effective h close to 0.
    # Sites in deep branches have h close to level.
    #
    # Most physical: h_i = number of leading zeros in address + 1
    # This gives a distribution of depths across the lattice.
    #
    # Actually, the simplest consistent reading: h_i = level (uniform)
    # for all leaf sites. The depth-dependent terms then create a
    # single on-site value per block. Let me implement BOTH and
    # report which was used.
    #
    # Going with: h_i = position in hierarchy.
    # We assign h_i based on which sub-tetrahedron the site sits in
    # at the coarsest level. Sites in sub-tet 0 get h=1 bias, etc.
    # More precisely: h_i = the IFS level, since all sites are leaves.
    return level


def get_variable_depth(idx, level):
    """
    Variable depth assignment for richer potential structure.
    h_i = number of address digits that match a reference pattern.
    This creates a smooth depth gradient across the lattice.
    
    Actually: use the simplicial depth — how many levels from the
    nearest vertex of the parent tetrahedron. 
    Address (a_0, a_1, ..., a_{H-1}): the first digit that differs
    from 0 determines the coarse depth.
    
    h_i = index of first non-zero digit + 1, or H if all zeros.
    """
    addr = site_to_address(idx, level)
    for k in range(level):
        if addr[k] != 0:
            return k + 1
    return level


def build_parent_child_pairs(N, level):
    """
    Build list of parent-child connected pairs on the IFS.
    Sites i,j are parent-child if they share address prefix of length (level-1).
    i.e., siblings in the same parent group.
    """
    addresses = [site_to_address(i, level) for i in range(N)]
    parent_groups = {}
    for i in range(N):
        pk = addresses[i][:level-1]
        if pk not in parent_groups:
            parent_groups[pk] = []
        parent_groups[pk].append(i)
    
    pairs = []
    for pk, members in parent_groups.items():
        for a in range(len(members)):
            for b in range(a+1, len(members)):
                pairs.append((members[a], members[b]))
    
    return pairs, parent_groups


def build_H_multi(N, level, mu_value):
    """
    Build the 2N×2N multi-component Hamiltonian.
    
    Layout: first N entries = ρ channel, next N = Θ channel.
    """
    pairs, parent_groups = build_parent_child_pairs(N, level)
    
    # Compute depths for all sites
    # Use variable depth for potential structure
    depths = np.array([get_variable_depth(i, level) for i in range(N)], dtype=np.float64)
    
    rows = []
    cols = []
    vals = []
    
    # ── H_ρρ block (indices 0..N-1) ──
    # Off-diagonal: -η² for parent-child pairs
    for i, j in pairs:
        rows.append(i); cols.append(j); vals.append(-ETA2)
        rows.append(j); cols.append(i); vals.append(-ETA2)
    
    # Diagonal: η²·deg(i) + λ_ρ·(1 - η^h_i)
    degree = np.zeros(N)
    for i, j in pairs:
        degree[i] += 1
        degree[j] += 1
    
    for i in range(N):
        h_i = depths[i]
        diag_rho = ETA2 * degree[i] + LAMBDA_RHO * (1.0 - ETA**h_i)
        rows.append(i); cols.append(i); vals.append(diag_rho)
    
    # ── H_ΘΘ block (indices N..2N-1) ──
    # Off-diagonal: -η⁴ for parent-child pairs
    for i, j in pairs:
        rows.append(N+i); cols.append(N+j); vals.append(-ETA4)
        rows.append(N+j); cols.append(N+i); vals.append(-ETA4)
    
    # Diagonal: η⁴·deg(i) + λ_Θ·(η^h_i - η^{2h_i})
    for i in range(N):
        h_i = depths[i]
        diag_theta = ETA4 * degree[i] + LAMBDA_THETA * (ETA**h_i - ETA**(2*h_i))
        rows.append(N+i); cols.append(N+i); vals.append(diag_theta)
    
    # ── H_ρΘ block (cross-channel coupling, diagonal only) ──
    # (H_ρΘ)_{ii} = μ · X_i · Y_i
    # X_i = 1 - η^h_i  (reactive loading)
    # Y_i = η^h_i - η^{2h_i}  (orientation loading)
    for i in range(N):
        h_i = depths[i]
        X_i = 1.0 - ETA**h_i
        Y_i = ETA**h_i - ETA**(2*h_i)
        coupling = mu_value * X_i * Y_i
        if abs(coupling) > 1e-15:
            # ρ→Θ
            rows.append(i); cols.append(N+i); vals.append(coupling)
            # Θ→ρ (symmetric)
            rows.append(N+i); cols.append(i); vals.append(coupling)
    
    H = sparse.csr_matrix((vals, (rows, cols)), shape=(2*N, 2*N))
    return H, depths, degree


def analyze_mode(eigvec, N):
    """
    Split eigenvector into ρ and Θ components, compute channel weights and IPR.
    """
    psi_rho = eigvec[:N]
    psi_theta = eigvec[N:]
    
    W_rho = np.sum(psi_rho**2)
    W_theta = np.sum(psi_theta**2)
    
    # IPR per channel (normalized within channel)
    if W_rho > 1e-15:
        IPR_rho = np.sum(psi_rho**4) / (W_rho**2)
    else:
        IPR_rho = 0.0
    
    if W_theta > 1e-15:
        IPR_theta = np.sum(psi_theta**4) / (W_theta**2)
    else:
        IPR_theta = 0.0
    
    F_rho = IPR_rho * N
    F_theta = IPR_theta * N
    
    return {
        "W_rho": float(W_rho),
        "W_Theta": float(W_theta),
        "IPR_rho": float(IPR_rho),
        "IPR_Theta": float(IPR_theta),
        "F_rho": float(F_rho),
        "F_Theta": float(F_theta),
    }


def assign_sector(mode_data):
    """Apply sector-ID rule from the spec."""
    W_rho = mode_data["W_rho"]
    W_theta = mode_data["W_Theta"]
    F_rho = mode_data["F_rho"]
    F_theta = mode_data["F_Theta"]
    
    if W_rho > 0.7:
        return "sigma1", f"W_rho={W_rho:.3f}>0.7, ρ-dominated"
    elif W_theta > 0.7 and F_theta > F_rho:
        return "sigma3", f"W_Theta={W_theta:.3f}>0.7, Θ-dominated, F_Θ>F_ρ"
    elif W_theta > 0.3:
        return "sigma2", f"W_Theta={W_theta:.3f}>0.3, Θ-weighted"
    elif W_rho > 0.3:
        return "sigma1", f"W_rho={W_rho:.3f}>0.3, ρ-weighted (moderate)"
    else:
        return "mixed", f"W_rho={W_rho:.3f}, W_Theta={W_theta:.3f}, no clear dominance"


def run_eigensolve(N, level, mu_value, mu_label, n_modes=20):
    """Build H_multi and diagonalize."""
    
    print(f"  Building H_multi (2×{N} = {2*N} dim, μ={mu_value:.5f} [{mu_label}])...", file=sys.stderr)
    t0 = time.time()
    H, depths, degree = build_H_multi(N, level, mu_value)
    t_build = time.time() - t0
    print(f"  Built in {t_build:.1f}s. nnz={H.nnz}", file=sys.stderr)
    
    print(f"  Eigensolve: {n_modes} modes near E=0 (shift-invert)...", file=sys.stderr)
    t0 = time.time()
    try:
        eigenvalues, eigenvectors = eigsh(H, k=n_modes, sigma=0.0, which='LM')
    except Exception as e:
        print(f"  shift-invert failed ({e}), trying SM...", file=sys.stderr)
        eigenvalues, eigenvectors = eigsh(H, k=n_modes, which='SM')
    t_eig = time.time() - t0
    print(f"  Eigensolve done in {t_eig:.1f}s", file=sys.stderr)
    
    # Sort by |E|
    sorted_idx = np.argsort(np.abs(eigenvalues))
    
    # Analyze top modes
    modes = []
    for rank in range(min(n_modes, len(sorted_idx))):
        k = sorted_idx[rank]
        evec = eigenvectors[:, k]
        E_k = float(eigenvalues[k])
        
        md = analyze_mode(evec, N)
        sector, basis = assign_sector(md)
        
        modes.append({
            "mode_index": int(k),
            "rank_by_absE": rank + 1,
            "eigenvalue": E_k,
            "W_rho": round(md["W_rho"], 6),
            "W_Theta": round(md["W_Theta"], 6),
            "IPR_rho": round(md["IPR_rho"], 10),
            "IPR_Theta": round(md["IPR_Theta"], 10),
            "F_rho": round(md["F_rho"], 4),
            "F_Theta": round(md["F_Theta"], 4),
            "sector_label": sector,
            "sector_basis": basis,
        })
        
        if rank < 10:
            print(f"    Mode {rank+1}: E={E_k:.6e} | W_ρ={md['W_rho']:.4f} W_Θ={md['W_Theta']:.4f} | "
                  f"F_ρ={md['F_rho']:.2f} F_Θ={md['F_Theta']:.2f} | {sector}", file=sys.stderr)
    
    # Find σ₁ and σ₂ candidates
    sigma1_candidates = [m for m in modes if m["sector_label"] == "sigma1"]
    sigma2_candidates = [m for m in modes if m["sector_label"] in ("sigma2", "sigma3")]
    mixed_candidates = [m for m in modes if m["sector_label"] == "mixed"]
    
    # σ₁: first sigma1-labeled mode by |E|
    sigma1_mode = sigma1_candidates[0] if sigma1_candidates else None
    # σ₂: first sigma2/sigma3-labeled mode by |E|
    sigma2_mode = sigma2_candidates[0] if sigma2_candidates else None
    
    # If no clean σ₂, check mixed modes
    if sigma2_mode is None and mixed_candidates:
        # Pick the mixed mode with highest W_Theta
        mixed_candidates.sort(key=lambda m: m["W_Theta"], reverse=True)
        sigma2_mode = mixed_candidates[0]
    
    # If still no σ₂, pick the mode with highest W_Theta overall
    if sigma2_mode is None:
        by_wtheta = sorted(modes, key=lambda m: m["W_Theta"], reverse=True)
        sigma2_mode = by_wtheta[0] if by_wtheta else None
    
    # Near-degeneracy check
    near_degen_flag = None
    if sigma1_mode and sigma2_mode:
        E1 = abs(sigma1_mode["eigenvalue"])
        E2 = abs(sigma2_mode["eigenvalue"])
        if E1 > 1e-15:
            gap = abs(E1 - E2) / E1
            if gap < NEAR_DEGEN_THRESHOLD:
                near_degen_flag = f"NEAR_DEGENERATE: |E_σ₁-E_σ₂|/|E_σ₁| = {gap:.4f} < 0.10"
    
    return {
        "modes": modes[:20],  # full 20
        "top5": modes[:5],
        "sigma1_mode": sigma1_mode,
        "sigma2_mode": sigma2_mode,
        "near_degen_flag": near_degen_flag,
        "eigenvalues": [float(eigenvalues[sorted_idx[i]]) for i in range(min(20, len(sorted_idx)))],
        "build_time": t_build,
        "eig_time": t_eig,
    }


def evaluate_gates(result):
    """Evaluate C2 resolution gates."""
    s2 = result["sigma2_mode"]
    s1 = result["sigma1_mode"]
    
    if s2 is None:
        return "INCOMPLETE", "No σ₂ candidate found"
    
    F_s2_theta = s2["F_Theta"]
    
    if F_s2_theta < 2.0:
        c2 = "C2-ARTIFACT"
        detail = f"F_σ₂^Θ = {F_s2_theta:.4f} < 2.0 → C2 was scalar-lane artifact"
    elif F_s2_theta >= 5.0:
        c2 = "C2-REAL"
        detail = f"F_σ₂^Θ = {F_s2_theta:.4f} ≥ 5.0 → C2 is real multi-channel finding"
    else:
        c2 = "C2-AMBIGUOUS"
        detail = f"F_σ₂^Θ = {F_s2_theta:.4f} ∈ [2.0, 5.0) → inconclusive"
    
    # Secondary: σ₁ channel integrity
    s1_note = ""
    if s1:
        F_s1_rho = s1["F_rho"]
        if F_s1_rho < 2.0:
            s1_note = f"WARNING: F_σ₁^ρ = {F_s1_rho:.4f} < 2.0 — σ₁ also delocalized"
        elif F_s1_rho >= 5.0 and F_s2_theta < 2.0:
            s1_note = f"CLEAN SEPARATION: F_σ₁^ρ = {F_s1_rho:.4f} ≥ 5, F_σ₂^Θ < 2"
    
    return c2, detail + (" | " + s1_note if s1_note else "")


def build_output_block(N, level, mu_value, mu_label, result):
    """Assemble the Hmulti_A_raw return block."""
    
    c2_status, c2_detail = evaluate_gates(result)
    
    s1 = result["sigma1_mode"]
    s2 = result["sigma2_mode"]
    
    ts = datetime.datetime.now(datetime.timezone.utc)
    
    block = {
        "version": "1.0",
        "schema": "Hmulti_A_raw",
        "run_id": f"OSCAR-HMULTI-A-{mu_label}-H{level}-{ts.strftime('%Y%m%dT%H%M%SZ')}",
        "timestamp": ts.isoformat(),
        "executor": "Oscar (Cato-executed, multi-component eigensolve)",
        "version_label": "A",
        "N_sites": N,
        "ifs_level": level,
        "eta": round(ETA, 6),
        "lambda_rho": round(LAMBDA_RHO, 6),
        "lambda_Theta": round(LAMBDA_THETA, 6),
        "mu": round(mu_value, 6),
        "mu_label": mu_label,
        "burden_included": False,
        "damping_included": False,
        "n_modes_computed": len(result["modes"]),
        
        "modes_top5": result["top5"],
        
        "sigma1_mode_index": s1["mode_index"] if s1 else None,
        "sigma2_mode_index": s2["mode_index"] if s2 else None,
        "F_sigma1_rho": round(s1["F_rho"], 4) if s1 else None,
        "F_sigma2_Theta": round(s2["F_Theta"], 4) if s2 else None,
        
        "C2_status": c2_status,
        "C2_detail": c2_detail,
        
        "near_degeneracy_flag": result["near_degen_flag"],
        
        "eigenvalue_spectrum_top20": [round(e, 10) for e in result["eigenvalues"]],
        
        "build_time_s": round(result["build_time"], 1),
        "eig_time_s": round(result["eig_time"], 1),
    }
    
    return block


def main():
    # ── Determine feasible N ──
    # H=8 OOM'd at 4GB. Run H=5,6,7 for scaling sequence.
    levels_to_run = [
        (5, 1024),
        (6, 4096),
        (7, 16384),
    ]
    print("Running H=5,6,7 (H=8 exceeded memory limit)", file=sys.stderr)
    
    all_blocks = []
    
    for mu_value, mu_label in [(MU_ANSATZ, "ansatz_sqrt"), (MU_ALT, "alt_square")]:
        for level, N in levels_to_run:
            print(f"\n{'='*70}", file=sys.stderr)
            print(f"H={level}, N={N}, μ={mu_value:.5f} ({mu_label})", file=sys.stderr)
            print(f"{'='*70}", file=sys.stderr)
            
            result = run_eigensolve(N, level, mu_value, mu_label, n_modes=20)
            block = build_output_block(N, level, mu_value, mu_label, result)
            
            notes = [
                f"Multi-component eigensolve: 2×{N} = {2*N} Hamiltonian",
                f"H_ρρ hopping: η² = {ETA2:.5f}, H_ΘΘ hopping: η⁴ = {ETA4:.5f}",
                f"Cross-coupling μ = {mu_value:.5f} ({mu_label})",
                "Variable depth: h_i = index of first non-zero address digit + 1",
                "Connectivity: sibling pairs (parent-child at finest level)",
                "No burden, no damping (Version A clean operator)",
                f"Eigensolver: scipy eigsh, shift-invert at σ=0, k=20",
            ]
            block["notes"] = notes
            
            all_blocks.append(block)
            
            print(f"\n  C2 STATUS: {block['C2_status']}", file=sys.stderr)
            print(f"  {block['C2_detail']}", file=sys.stderr)
            if block['near_degeneracy_flag']:
                print(f"  FLAG: {block['near_degeneracy_flag']}", file=sys.stderr)
    
    # Summary
    print(f"\n{'='*70}", file=sys.stderr)
    print("H_MULTI VERSION A SUMMARY", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)
    print(f"{'μ':>15} {'H':>3} {'N':>6} {'F_σ₁^ρ':>10} {'F_σ₂^Θ':>10} {'C2':>15}", file=sys.stderr)
    for b in all_blocks:
        print(f"{b['mu_label']:>15} {b['ifs_level']:>3} {b['N_sites']:>6} "
              f"{b['F_sigma1_rho'] or 0:>10.2f} {b['F_sigma2_Theta'] or 0:>10.2f} "
              f"{b['C2_status']:>15}", file=sys.stderr)
    
    print(json.dumps(all_blocks, indent=2))


if __name__ == "__main__":
    main()
