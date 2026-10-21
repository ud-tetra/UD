#!/usr/bin/env python3
"""
OSCAR EXECUTION — H_MULTI-REBUILD v1.1
Same repaired operator (R1+R3). Fixed eigensolve strategy:
search BOTH ρ-block and Θ-block spectral regions separately,
then merge and analyze channel weights.

The single sigma=0 approach only found Θ-block modes.
Now we:
1. Diagonalize H_ρρ alone → get its spectral range
2. Diagonalize H_ΘΘ alone → get its spectral range  
3. Use shift-invert at each block's minimum eigenvalue
4. Merge and analyze the full 2-channel eigenstates
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
import json
import datetime
import sys
import time

ETA = 185.0 / 192.0
ETA2 = ETA ** 2
ETA4 = ETA ** 4
LAMBDA_RHO = 7.0 / 192.0
LAMBDA_THETA = ETA * (1.0 - ETA)
NU = ETA2 * (1.0 - ETA)


def site_to_address(idx, level):
    addr = []
    s = idx
    for _ in range(level):
        addr.append(s % 4)
        s //= 4
    return tuple(reversed(addr))


def get_variable_depth(idx, level):
    addr = site_to_address(idx, level)
    for k in range(level):
        if addr[k] != 0:
            return k + 1
    return level


def compute_parity(idx, level):
    addr = site_to_address(idx, level)
    return (-1) ** (sum(addr) % 2)


def build_connectivity(N, level):
    addresses = [site_to_address(i, level) for i in range(N)]
    parent_groups = {}
    for i in range(N):
        pk = addresses[i][:level-1]
        if pk not in parent_groups:
            parent_groups[pk] = []
        parent_groups[pk].append(i)

    sibling_pairs = []
    for pk, members in parent_groups.items():
        for a in range(len(members)):
            for b in range(a+1, len(members)):
                sibling_pairs.append((members[a], members[b]))

    cousin_pairs = []
    if level >= 2:
        gp_groups = {}
        for i in range(N):
            gpk = addresses[i][:level-2]
            if gpk not in gp_groups:
                gp_groups[gpk] = []
            gp_groups[gpk].append(i)
        for gpk, members in gp_groups.items():
            sub = {}
            for i in members:
                pid = addresses[i][:level-1]
                if pid not in sub:
                    sub[pid] = []
                sub[pid].append(i)
            plist = list(sub.values())
            for a in range(len(plist)):
                for b in range(a+1, len(plist)):
                    for i in plist[a]:
                        for j in plist[b]:
                            cousin_pairs.append((i, j))

    return sibling_pairs, cousin_pairs


def build_blocks_and_full(N, level):
    """Build H_ρρ, H_ΘΘ separately AND H_multi full."""
    sibling_pairs, cousin_pairs = build_connectivity(N, level)
    depths = np.array([get_variable_depth(i, level) for i in range(N)])
    parities = np.array([compute_parity(i, level) for i in range(N)])

    # H_rho (N×N)
    r_r, r_c, r_v = [], [], []
    sib_deg = np.zeros(N)
    for i, j in sibling_pairs:
        r_r.append(i); r_c.append(j); r_v.append(-ETA2)
        r_r.append(j); r_c.append(i); r_v.append(-ETA2)
        sib_deg[i] += 1; sib_deg[j] += 1
    for i in range(N):
        h = depths[i]
        r_r.append(i); r_c.append(i)
        r_v.append(ETA2 * sib_deg[i] + LAMBDA_RHO * (1 - ETA**h))
    H_rho = sparse.csr_matrix((r_v, (r_r, r_c)), shape=(N, N))

    # H_theta (N×N)
    t_r, t_c, t_v = [], [], []
    cous_deg = np.zeros(N)
    for i, j in cousin_pairs:
        t_r.append(i); t_c.append(j); t_v.append(-ETA4)
        t_r.append(j); t_c.append(i); t_v.append(-ETA4)
        cous_deg[i] += 1; cous_deg[j] += 1
    for i in range(N):
        h = depths[i]
        t_r.append(i); t_c.append(i)
        t_v.append(ETA4 * cous_deg[i] + LAMBDA_THETA * (ETA**h - ETA**(2*h)))
    H_theta = sparse.csr_matrix((t_v, (t_r, t_c)), shape=(N, N))

    # Full 2N×2N
    f_r, f_c, f_v = [], [], []
    # Copy H_rho to upper-left
    for i, j, v in zip(r_r, r_c, r_v):
        f_r.append(i); f_c.append(j); f_v.append(v)
    # Copy H_theta to lower-right
    for i, j, v in zip(t_r, t_c, t_v):
        f_r.append(N+i); f_c.append(N+j); f_v.append(v)
    # Cross-coupling
    for i in range(N):
        h = depths[i]
        X = 1.0 - ETA**h
        Y = ETA**h - ETA**(2*h)
        c = parities[i] * NU * X * Y
        if abs(c) > 1e-18:
            f_r.append(i); f_c.append(N+i); f_v.append(c)
            f_r.append(N+i); f_c.append(i); f_v.append(c)
    H_full = sparse.csr_matrix((f_v, (f_r, f_c)), shape=(2*N, 2*N))

    return H_rho, H_theta, H_full, depths, parities


def analyze_mode(eigvec, N):
    psi_rho = eigvec[:N]
    psi_theta = eigvec[N:]
    W_rho = float(np.sum(psi_rho**2))
    W_theta = float(np.sum(psi_theta**2))
    IPR_rho = float(np.sum(psi_rho**4) / max(W_rho**2, 1e-30))
    IPR_theta = float(np.sum(psi_theta**4) / max(W_theta**2, 1e-30))
    return {
        "W_rho": W_rho, "W_Theta": W_theta,
        "IPR_rho": IPR_rho, "IPR_Theta": IPR_theta,
        "F_rho": IPR_rho * N, "F_Theta": IPR_theta * N,
    }


def run_level(level, N):
    print(f"\n{'='*70}", file=sys.stderr)
    print(f"H={level}, N={N}", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)

    H_rho, H_theta, H_full, depths, parities = build_blocks_and_full(N, level)

    # Step 1: Find spectral edges of each block
    k_probe = min(5, N-2)

    print(f"  Probing H_rho spectrum...", file=sys.stderr)
    eigs_rho_lo = eigsh(H_rho, k=k_probe, which='SM', return_eigenvectors=False)
    eigs_rho_hi = eigsh(H_rho, k=k_probe, which='LM', return_eigenvectors=False)
    rho_min = float(np.min(eigs_rho_lo))
    rho_max = float(np.max(eigs_rho_hi))
    print(f"    H_rho spectrum: [{rho_min:.6f}, {rho_max:.6f}]", file=sys.stderr)

    print(f"  Probing H_theta spectrum...", file=sys.stderr)
    eigs_theta_lo = eigsh(H_theta, k=k_probe, which='SM', return_eigenvectors=False)
    eigs_theta_hi = eigsh(H_theta, k=k_probe, which='LM', return_eigenvectors=False)
    theta_min = float(np.min(eigs_theta_lo))
    theta_max = float(np.max(eigs_theta_hi))
    print(f"    H_theta spectrum: [{theta_min:.6f}, {theta_max:.6f}]", file=sys.stderr)

    # Step 2: Find eigenstates of FULL H near each block's minimum
    n_per = 10
    all_eigs = []
    all_vecs = []

    for sigma_target, label in [(rho_min, "rho_min"), (theta_min, "theta_min")]:
        print(f"  Full H eigsh near σ={sigma_target:.6f} ({label})...", file=sys.stderr)
        try:
            evals, evecs = eigsh(H_full, k=n_per, sigma=sigma_target, which='LM')
            all_eigs.extend(evals.tolist())
            for j in range(evecs.shape[1]):
                all_vecs.append(evecs[:, j])
        except Exception as e:
            print(f"    Failed: {e}", file=sys.stderr)

    # Also probe near the midpoint between blocks
    mid = (rho_min + theta_min) / 2
    print(f"  Full H eigsh near σ={mid:.6f} (midpoint)...", file=sys.stderr)
    try:
        evals, evecs = eigsh(H_full, k=n_per, sigma=mid, which='LM')
        all_eigs.extend(evals.tolist())
        for j in range(evecs.shape[1]):
            all_vecs.append(evecs[:, j])
    except Exception as e:
        print(f"    Failed: {e}", file=sys.stderr)

    # Deduplicate by eigenvalue (within tolerance)
    modes = []
    seen_eigs = set()
    for idx in range(len(all_eigs)):
        e_round = round(all_eigs[idx], 6)
        if e_round in seen_eigs:
            continue
        seen_eigs.add(e_round)
        md = analyze_mode(all_vecs[idx], N)
        modes.append({
            "eigenvalue": float(all_eigs[idx]),
            "W_rho": round(md["W_rho"], 6),
            "W_Theta": round(md["W_Theta"], 6),
            "F_rho": round(md["F_rho"], 4),
            "F_Theta": round(md["F_Theta"], 4),
        })

    # Sort by |E|
    modes.sort(key=lambda m: abs(m["eigenvalue"]))

    # Report
    print(f"\n  Top modes (sorted by |E|):", file=sys.stderr)
    rho_dom_count = 0
    theta_dom_count = 0
    for i, m in enumerate(modes[:20]):
        dom = "ρ-dom" if m["W_rho"] > 0.6 else ("Θ-dom" if m["W_Theta"] > 0.6 else "mixed")
        if m["W_rho"] > 0.6: rho_dom_count += 1
        if m["W_Theta"] > 0.6: theta_dom_count += 1
        f_diff = abs(m["F_rho"] - m["F_Theta"]) / max(m["F_rho"], 0.01)
        print(f"    {i+1:>3}: E={m['eigenvalue']:.6e} | "
              f"W_ρ={m['W_rho']:.4f} W_Θ={m['W_Theta']:.4f} | "
              f"F_ρ={m['F_rho']:.2f} F_Θ={m['F_Theta']:.2f} | "
              f"ΔF={f_diff:.2%} | {dom}", file=sys.stderr)

    # Metrics
    defact = rho_dom_count > 0 and theta_dom_count > 0
    f_differs = sum(1 for m in modes[:20]
                    if abs(m["F_rho"] - m["F_Theta"]) / max(m["F_rho"], 0.01) > 0.05)

    # Find σ₁ (ρ-dominated) and σ₂ (Θ-dominated)
    sigma1 = next((m for m in modes if m["W_rho"] > 0.6), None)
    sigma2 = next((m for m in modes if m["W_Theta"] > 0.6), None)

    print(f"\n  ρ-dominated modes: {rho_dom_count}", file=sys.stderr)
    print(f"  Θ-dominated modes: {theta_dom_count}", file=sys.stderr)
    print(f"  F differs (>5%): {f_differs}/{min(20, len(modes))}", file=sys.stderr)
    print(f"  Defactorized: {defact}", file=sys.stderr)
    if sigma1:
        print(f"  σ₁ candidate: F_ρ={sigma1['F_rho']:.2f}, W_ρ={sigma1['W_rho']:.4f}", file=sys.stderr)
    if sigma2:
        print(f"  σ₂ candidate: F_Θ={sigma2['F_Theta']:.2f}, W_Θ={sigma2['W_Theta']:.4f}", file=sys.stderr)

    # C2 evaluation
    if not defact:
        c2 = "STILL-FACTORIZED"
    elif sigma2 and sigma2["F_Theta"] < 2.0:
        c2 = "C2-ARTIFACT"
    elif sigma2 and sigma2["F_Theta"] >= 5.0:
        c2 = "C2-REAL"
    elif sigma2:
        c2 = "C2-AMBIGUOUS"
    else:
        c2 = "INCOMPLETE"

    print(f"  C2: {c2}", file=sys.stderr)

    return {
        "level": level, "N": N,
        "rho_spectrum": [rho_min, rho_max],
        "theta_spectrum": [theta_min, theta_max],
        "modes_top20": modes[:20],
        "sigma1": sigma1, "sigma2": sigma2,
        "rho_dom_count": rho_dom_count,
        "theta_dom_count": theta_dom_count,
        "f_differs_count": f_differs,
        "defactorized": defact,
        "C2": c2,
    }


def main():
    levels = [(5, 1024), (6, 4096), (7, 16384)]
    all_results = []

    for level, N in levels:
        result = run_level(level, N)
        all_results.append(result)

    # Final summary
    print(f"\n{'='*70}", file=sys.stderr)
    print("DUAL-SIGMA REPAIRED H_MULTI SUMMARY", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)
    print(f"{'H':>3} {'N':>6} {'ρ-dom':>6} {'Θ-dom':>6} {'Defact':>7} {'F_σ₁^ρ':>10} {'F_σ₂^Θ':>10} {'C2':>18}", file=sys.stderr)
    for r in all_results:
        s1f = r['sigma1']['F_rho'] if r['sigma1'] else 0
        s2f = r['sigma2']['F_Theta'] if r['sigma2'] else 0
        print(f"{r['level']:>3} {r['N']:>6} {r['rho_dom_count']:>6} {r['theta_dom_count']:>6} "
              f"{'YES' if r['defactorized'] else 'NO':>7} "
              f"{s1f:>10.2f} {s2f:>10.2f} {r['C2']:>18}", file=sys.stderr)

    # Serialize (handle numpy types)
    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (np.integer,)): return int(obj)
            if isinstance(obj, (np.floating,)): return float(obj)
            if isinstance(obj, (np.bool_,)): return bool(obj)
            if isinstance(obj, np.ndarray): return obj.tolist()
            return super().default(obj)

    ts = datetime.datetime.now(datetime.timezone.utc)
    output = {
        "schema": "Hmulti_A_repaired_v1.1",
        "run_id": f"OSCAR-HMULTI-R1R3-DUAL-{ts.strftime('%Y%m%dT%H%M%SZ')}",
        "timestamp": ts.isoformat(),
        "executor": "Oscar (dual-sigma eigensolve)",
        "repair": "R1 (cousin topology) + R3 (parity coupling)",
        "method": "dual-sigma shift-invert at rho_min and theta_min",
        "results": all_results,
    }
    print(json.dumps(output, indent=2, cls=NpEncoder))


if __name__ == "__main__":
    main()
