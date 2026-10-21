#!/usr/bin/env python3
"""
OSCAR — H_MULTI R6b: Θ potential removed + connected Θ graph

Diagnosis from R6: cousin-only graph is DISCONNECTED (64/256/1024
separate components). F_σ₂ > 1 is a graph-disconnection artifact.

Fix: add d=3 (great-grandparent) hopping at η⁶ to connect components.
This gives the Θ graph a CONNECTED hierarchical structure while
keeping it topologically distinct from the ρ sibling graph.

H_ΘΘ: cousins (d=2, η⁴) + second-cousins (d=3, η⁶) + NO potential
H_ρρ: siblings (d=1, η²) + potential λ_ρ(1−η^h)  [unchanged]
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
import json, datetime, sys, time

ETA = 185.0 / 192.0
ETA2 = ETA ** 2
ETA4 = ETA ** 4
ETA6 = ETA ** 6
LAMBDA_RHO = 7.0 / 192.0
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


def build_all_connectivity(N, level):
    addresses = [site_to_address(i, level) for i in range(N)]

    # d=1: siblings (same parent)
    parent_groups = {}
    for i in range(N):
        pk = addresses[i][:level-1]
        if pk not in parent_groups:
            parent_groups[pk] = []
        parent_groups[pk].append(i)
    sib_pairs = []
    for members in parent_groups.values():
        for a in range(len(members)):
            for b in range(a+1, len(members)):
                sib_pairs.append((members[a], members[b]))

    # d=2: cousins (same grandparent, different parent)
    cousin_pairs = []
    gp_groups = {}
    if level >= 2:
        for i in range(N):
            gpk = addresses[i][:level-2]
            if gpk not in gp_groups:
                gp_groups[gpk] = []
            gp_groups[gpk].append(i)
        for members in gp_groups.values():
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

    # d=3: second-cousins (same great-grandparent, different grandparent)
    sc_pairs = []
    if level >= 3:
        ggp_groups = {}
        for i in range(N):
            ggpk = addresses[i][:level-3]
            if ggpk not in ggp_groups:
                ggp_groups[ggpk] = []
            ggp_groups[ggpk].append(i)
        for members in ggp_groups.values():
            sub_gp = {}
            for i in members:
                gpid = addresses[i][:level-2]
                if gpid not in sub_gp:
                    sub_gp[gpid] = []
                sub_gp[gpid].append(i)
            gplist = list(sub_gp.values())
            for a in range(len(gplist)):
                for b in range(a+1, len(gplist)):
                    # Only sample to keep manageable
                    # Each gp group has 16 sites, so full cross is 16*16=256 per pair
                    # With 6 gp pairs per ggp group, that's 1536 pairs per ggp group
                    for i in gplist[a]:
                        for j in gplist[b]:
                            sc_pairs.append((i, j))

    return sib_pairs, cousin_pairs, sc_pairs


def build_blocks_and_full(N, level):
    sib_pairs, cousin_pairs, sc_pairs = build_all_connectivity(N, level)
    depths = np.array([get_variable_depth(i, level) for i in range(N)])
    parities = np.array([compute_parity(i, level) for i in range(N)])

    # H_rho: siblings only (unchanged)
    r_r, r_c, r_v = [], [], []
    sib_deg = np.zeros(N)
    for i, j in sib_pairs:
        r_r.append(i); r_c.append(j); r_v.append(-ETA2)
        r_r.append(j); r_c.append(i); r_v.append(-ETA2)
        sib_deg[i] += 1; sib_deg[j] += 1
    for i in range(N):
        h = depths[i]
        r_r.append(i); r_c.append(i)
        r_v.append(ETA2 * sib_deg[i] + LAMBDA_RHO * (1 - ETA**h))
    H_rho = sparse.csr_matrix((r_v, (r_r, r_c)), shape=(N, N))

    # H_theta: cousins (η⁴) + second-cousins (η⁶), NO potential
    t_r, t_c, t_v = [], [], []
    theta_deg = np.zeros(N)
    for i, j in cousin_pairs:
        t_r.append(i); t_c.append(j); t_v.append(-ETA4)
        t_r.append(j); t_c.append(i); t_v.append(-ETA4)
        theta_deg[i] += ETA4; theta_deg[j] += ETA4
    for i, j in sc_pairs:
        t_r.append(i); t_c.append(j); t_v.append(-ETA6)
        t_r.append(j); t_c.append(i); t_v.append(-ETA6)
        theta_deg[i] += ETA6; theta_deg[j] += ETA6
    # Diagonal: sum of absolute hopping weights (Laplacian form)
    for i in range(N):
        t_r.append(i); t_c.append(i)
        t_v.append(theta_deg[i])
    H_theta = sparse.csr_matrix((t_v, (t_r, t_c)), shape=(N, N))

    # Full 2N×2N
    f_r, f_c, f_v = [], [], []
    for i, j, v in zip(r_r, r_c, r_v):
        f_r.append(i); f_c.append(j); f_v.append(v)
    for i, j, v in zip(t_r, t_c, t_v):
        f_r.append(N+i); f_c.append(N+j); f_v.append(v)
    for i in range(N):
        h = depths[i]
        X = 1.0 - ETA**h
        Y = ETA**h - ETA**(2*h)
        c = parities[i] * NU * X * Y
        if abs(c) > 1e-18:
            f_r.append(i); f_c.append(N+i); f_v.append(c)
            f_r.append(N+i); f_c.append(i); f_v.append(c)
    H_full = sparse.csr_matrix((f_v, (f_r, f_c)), shape=(2*N, 2*N))

    return H_rho, H_theta, H_full


def analyze_mode(eigvec, N):
    psi_rho = eigvec[:N]
    psi_theta = eigvec[N:]
    W_rho = float(np.sum(psi_rho**2))
    W_theta = float(np.sum(psi_theta**2))
    IPR_rho = float(np.sum(psi_rho**4) / max(W_rho**2, 1e-30))
    IPR_theta = float(np.sum(psi_theta**4) / max(W_theta**2, 1e-30))
    return {"W_rho": W_rho, "W_Theta": W_theta,
            "F_rho": IPR_rho * N, "F_Theta": IPR_theta * N}


def run_level(level, N):
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"R6b: H={level}, N={N}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)

    t0 = time.time()
    H_rho, H_theta, H_full = build_blocks_and_full(N, level)
    print(f"  Built in {time.time()-t0:.1f}s. H_full nnz={H_full.nnz}", file=sys.stderr)

    # Probe spectra
    k_p = min(3, N-2)
    rho_min = float(eigsh(H_rho, k=k_p, which='SM', return_eigenvectors=False).min())
    
    # For theta, the true minimum should be 0 (connected Laplacian)
    # Use shift-invert near 0 to find it
    try:
        theta_eigs = eigsh(H_theta, k=k_p, sigma=0.0, which='LM', return_eigenvectors=False)
        theta_min = float(np.min(np.abs(theta_eigs)))
    except:
        theta_eigs = eigsh(H_theta, k=k_p, which='SM', return_eigenvectors=False)
        theta_min = float(np.min(theta_eigs))
    
    print(f"  H_rho min: {rho_min:.8f}", file=sys.stderr)
    print(f"  H_theta near-zero: {theta_min:.8f}", file=sys.stderr)

    # Find modes from both blocks
    all_eigs, all_vecs = [], []

    for sigma, label in [(rho_min, "rho"), (1e-8, "theta_zero")]:
        print(f"  eigsh σ={sigma:.2e} ({label})...", file=sys.stderr)
        try:
            evals, evecs = eigsh(H_full, k=10, sigma=sigma, which='LM',
                                 maxiter=N*50)
            for j in range(evecs.shape[1]):
                all_eigs.append(float(evals[j]))
                all_vecs.append(evecs[:, j])
            print(f"    Found {len(evals)} modes", file=sys.stderr)
        except Exception as e:
            print(f"    Failed: {e}", file=sys.stderr)

    # Deduplicate and analyze
    modes = []
    seen = set()
    for idx in range(len(all_eigs)):
        e_r = round(all_eigs[idx], 6)
        if e_r in seen:
            continue
        seen.add(e_r)
        md = analyze_mode(all_vecs[idx], N)
        modes.append({"eigenvalue": all_eigs[idx], **md})
    modes.sort(key=lambda m: abs(m["eigenvalue"]))

    # Report
    print(f"\n  Top modes:", file=sys.stderr)
    for i, m in enumerate(modes[:12]):
        dom = "ρ" if m["W_rho"] > 0.6 else ("Θ" if m["W_Theta"] > 0.6 else "mix")
        print(f"    {i+1:>3}: E={m['eigenvalue']:.6e} | "
              f"W_ρ={m['W_rho']:.4f} W_Θ={m['W_Theta']:.4f} | "
              f"F_ρ={m['F_rho']:.2f} F_Θ={m['F_Theta']:.2f} | {dom}",
              file=sys.stderr)

    s1 = next((m for m in modes if m["W_rho"] > 0.6), None)
    s2 = next((m for m in modes if m["W_Theta"] > 0.6), None)

    defact = (s1 is not None) and (s2 is not None)
    if not defact:
        c2 = "NOT-DEFACTORIZED"
    elif s2["F_Theta"] < 2.0:
        c2 = "C2-ARTIFACT"
    elif s2["F_Theta"] >= 5.0:
        c2 = "C2-REAL"
    else:
        c2 = "C2-AMBIGUOUS"

    print(f"\n  σ₁: F_ρ={s1['F_rho']:.2f}" if s1 else "  σ₁: not found", file=sys.stderr)
    print(f"  σ₂: F_Θ={s2['F_Theta']:.2f}" if s2 else "  σ₂: not found", file=sys.stderr)
    print(f"  C2: {c2}", file=sys.stderr)

    return {"level": level, "N": N, "sigma1": s1, "sigma2": s2,
            "defactorized": defact, "C2": c2, "modes": modes[:10]}


def main():
    results = []
    for level, N in [(5, 1024), (6, 4096)]:
        results.append(run_level(level, N))

    # Try H=7 carefully
    try:
        results.append(run_level(7, 16384))
    except Exception as e:
        print(f"H=7 failed: {e}", file=sys.stderr)

    print(f"\n{'='*60}", file=sys.stderr)
    print("R6b SUMMARY (Θ: no potential, connected cousin+second-cousin graph)", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    for r in results:
        s1f = r['sigma1']['F_rho'] if r['sigma1'] else 0
        s2f = r['sigma2']['F_Theta'] if r['sigma2'] else 0
        print(f"  H={r['level']} N={r['N']:>6}: F_σ₁^ρ={s1f:>8.2f}  F_σ₂^Θ={s2f:>8.2f}  C2={r['C2']}", file=sys.stderr)

    class Enc(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, (np.integer,)): return int(o)
            if isinstance(o, (np.floating,)): return float(o)
            if isinstance(o, (np.bool_,)): return bool(o)
            return super().default(o)

    ts = datetime.datetime.now(datetime.timezone.utc)
    print(json.dumps({"schema": "Hmulti_R6b", "timestamp": ts.isoformat(),
                       "repair": "R6b: no Θ potential + connected Θ graph (cousin+second-cousin)",
                       "results": results}, indent=2, cls=Enc))

if __name__ == "__main__":
    main()
