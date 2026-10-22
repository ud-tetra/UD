#!/usr/bin/env python3
"""Local normal-load derivative of stationary index-seven graphite saddles.

Read-only public data for grid coordinates/validation; SI KC pair law computed
independently. Two Fourier shells and a second-order vertical Taylor model.
Outputs equilibrium enthalpy barriers, not kinetic friction.
"""
import hashlib
import io
import json
import math
import sys
import zipfile

import numpy as np
from scipy.optimize import root

ARCHIVE_SHA = "b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875"
with open(sys.argv[1], "rb") as handle:
    assert hashlib.file_digest(handle, "sha256").hexdigest() == ARCHIVE_SHA
with zipfile.ZipFile(sys.argv[1]) as archive:
    def grid(name):
        path = next(p for p in archive.namelist() if "/data/pes21_" in p and p.endswith("/" + name + ".txt"))
        return np.loadtxt(io.BytesIO(archive.read(path)))
    X, Y, Z = (grid(q) for q in "XYZ")
X, Y, Z = (q[::8, ::8].ravel() for q in (X, Y, Z))

bond = 1.42
a = math.sqrt(3) * bond
phi = math.atan(math.sqrt(3) / 5)
rotation_xy = np.array([[math.cos(phi), -math.sin(phi)],
                        [math.sin(phi), math.cos(phi)]])
basis = np.array([[a, a / 2], [0, a * math.sqrt(3) / 2]])
R = np.array([[8, 3], [-3, 5]]) / 7
supercell = np.array([[2, -1], [1, 3]])
inv_supercell = np.linalg.inv(supercell)
top, bottom = [], []
for p in range(-18, 19):
    for q in range(-18, 19):
        n = np.array([p, q])
        local = inv_supercell @ R @ n
        for atom in (np.zeros(2), np.array([1 / 3, 1 / 3])):
            bottom.append(basis @ (n + atom))
            if np.all(local >= -1e-9) and np.all(local < 1 - 1e-9):
                top.append(basis @ R @ (n + atom))
top, bottom = np.array(top), np.array(bottom)
assert len(top) == 14
xy = np.column_stack([X, Y])
rho2 = []
for point in xy:
    delta = top[:, None, :] + rotation_xy @ point - bottom[None, :, :]
    rho2.append(np.sum(delta * delta, axis=-1))

A, z0, C, C0, C2, C4, delta, lam = 10.238, 3.34, 3.030, 15.71, 12.29, 4.933, 0.578, 3.629
def pair_fields(height, cutoff):
    rows = []
    for lateral2 in rho2:
        r2 = lateral2 + height**2
        valid = r2 < cutoff**2
        radial2 = lateral2[valid]
        r = np.sqrt(r2[valid])
        u = radial2 / delta**2
        dispersion = A * (z0 / r)**6
        rep = (C + 2 * np.exp(-u) * (C0 + C2 * u + C4 * u * u)) * np.exp(-lam * (r - z0))
        e = -dispersion + rep
        ez = 6 * dispersion * height / r**2 - lam * rep * height / r
        ezz = 6 * dispersion * (1 / r**2 - 8 * height**2 / r**4) + rep * (lam**2 * height**2 / r**2 - lam * radial2 / r**3)
        rows.append([np.sum(v) / len(top) for v in (e, ez, ezz)])
    return np.array(rows)

g = math.sqrt(7) * 4 * math.pi / (math.sqrt(3) * a)
G = np.array([[math.cos(math.pi / 6), math.sin(math.pi / 6)],
              [math.cos(5 * math.pi / 6), math.sin(5 * math.pi / 6)]]) * g
T = 2 * math.pi * np.linalg.inv(G)
vectors = []
norms = []
for p in range(-2, 3):
    for q in range(-2, 3):
        norm = p * p + q * q - p * q
        if norm in (1, 3) and (p > 0 or p == 0 and q > 0):
            vectors.append(p * G[0] + q * G[1])
            norms.append(norm)
vectors = np.array(vectors)
phase = xy @ vectors.T
F = np.column_stack([np.ones(len(xy))] + [f(phase[:, j]) for j in range(len(vectors)) for f in (np.cos, np.sin)])
area_atom = math.sqrt(3) * a * a / 4
force_per_mpa = area_atom * 1000 / 160217.6634  # meV/Angstrom/atom per MPa
import contextlib
import io as _io
import runpy
from pathlib import Path
from scipy.optimize import root

ancestors = list(Path(__file__).resolve().parents)
repo = ancestors[2] if len(ancestors) > 2 and (ancestors[2] / "captures").exists() else Path.cwd()
source_path = repo / "captures/2026-10-22T214428Z-codex-graphite-harmonic-source-49d5bb28-64263b7c-7b88-4f45-a8a9-e0cb34f52956/verify_harmonic_source.py"
with contextlib.redirect_stdout(_io.StringIO()):
    src = runpy.run_path(source_path)
K = np.array(src["Ks"], dtype=float)  # seven 2x14 maps in direct a=1 coordinates
# Cart x (Angstrom) = basis @ u; covector transforms by basis^{-T}.
swap = np.array([[0,1],[1,0]])
# Top's coincidence basis has primitive indices (1,2),(-2,3). Swapping
# intrinsic primitives sends its quotient to the carrier's 0,1,5 convention.
Kcart = np.einsum("ij,rjk->rik", np.linalg.inv(basis @ R @ swap).T, K)
physical_rot = (basis @ R @ swap) @ np.array([[-1,-1],[1,0]]) @ np.linalg.inv(basis @ R @ swap)
vertex_permutation = [4*k%7 for k in range(7)] + [7+(4*k-1)%7 for k in range(7)]
constraint = np.zeros((28,28))
for component in range(2):
    for v in range(14):
        row=component*14+v
        constraint[row,component*14+vertex_permutation[v]]=1
        for j in range(2):
            constraint[row,j*14+v]-=physical_rot[component,j]
assert 28-np.linalg.matrix_rank(constraint,tol=1e-9)==8
assert np.max(np.abs(constraint @ Kcart.reshape(7,28).T))<1e-10
labels = []
for p in range(-18, 19):
    for q in range(-18, 19):
        n = np.array([p,q])
        local = inv_supercell @ R @ n
        for site in range(2):
            if np.all(local >= -1e-9) and np.all(local < 1-1e-9):
                labels.append(site*7+(q-2*p)%7)
assert len(labels)==14 and len(set(labels))==14

vals = pair_fields(3.46,16)
coefs = np.linalg.lstsq(F, vals, rcond=None)[0]
def grad(x):
    ph=vectors @ x
    c=coefs[:,0]
    return vectors.T @ (-c[1::2]*np.sin(ph)+c[2::2]*np.cos(ph))
first=[np.argmin(np.linalg.norm(vectors-v,axis=1)) for v in G]
phase0=[math.atan2(-coefs[1+2*j,0],coefs[2+2*j,0]) for j in first]
rootxy=root(grad,-np.linalg.solve(G,np.array(phase0)+math.pi))
assert np.linalg.norm(grad(rootxy.x))<1e-8
cart0=rotation_xy @ rootxy.x

def atom_zforces(cart,cutoff):
    d=top[:,None,:]+cart-bottom[None,:,:]
    rr=np.sum(d*d,axis=-1)
    r2=rr+3.46**2
    valid=r2<cutoff**2
    r=np.sqrt(r2)
    q=rr/delta**2
    D=A*(z0/r)**6
    H=(C+2*np.exp(-q)*(C0+C2*q+C4*q*q))*np.exp(-lam*(r-z0))
    ez=(6*D*3.46/r2-lam*H*3.46/r)
    return np.sum(np.where(valid,ez,0),axis=1)/14

B=Kcart.reshape(7,-1).T
def projection(cutoff,h):
    Ctop=np.empty((2,14))
    for i in range(2):
        dv=np.zeros(2);dv[i]=h
        Ctop[i,:]=(atom_zforces(cart0+dv,cutoff)-atom_zforces(cart0-dv,cutoff))/(2*h)
    Cordered=np.empty_like(Ctop)
    for j,k in enumerate(labels):
        Cordered[:,k]=Ctop[:,j]
    candidate=[]
    for offset in range(7):
        reordered=np.empty_like(Cordered)
        for site in range(2):
            for k in range(7):
                reordered[:,site*7+(k+offset)%7]=Cordered[:,site*7+k]
        target=reordered.reshape(-1)
        coef,*_=np.linalg.lstsq(B,target,rcond=None)
        fit=(B@coef).reshape(2,14)
        residual=float(np.linalg.norm(reordered-fit)/np.linalg.norm(reordered))
        symmetry_residual=float(np.linalg.norm(constraint @ target)/np.linalg.norm(target))
        candidate.append(dict(label_offset=offset,residual_norm=residual,
                              symmetry_residual_norm=symmetry_residual,
                              coefficients=coef.tolist()))
    best=min(candidate,key=lambda x:x["symmetry_residual_norm"])
    assert best["label_offset"]==2
    aligned=np.empty_like(Cordered)
    for site in range(2):
        for k in range(7):
            aligned[:,site*7+(k+2)%7]=Cordered[:,site*7+k]
    def rotate_height_map(matrix):
        out=np.empty_like(matrix)
        for v,pv in enumerate(vertex_permutation):
            out[:,pv]=physical_rot @ matrix[:,v]
        return out
    invariant=(aligned+rotate_height_map(aligned)+rotate_height_map(rotate_height_map(aligned)))/3
    invariant_coef=np.linalg.lstsq(B,invariant.reshape(-1),rcond=None)[0]
    allowed_residual=float(np.linalg.norm(invariant-(B@invariant_coef).reshape(2,14))/np.linalg.norm(invariant))
    symmetry_break=float(np.linalg.norm(aligned-invariant)/np.linalg.norm(aligned))
    assert symmetry_break < .002
    target=Cordered.reshape(-1)
    coef,*_=np.linalg.lstsq(B,target,rcond=None)
    fit=(B@coef).reshape(2,14)
    res=Cordered-fit
    return dict(cutoff_a=cutoff,finite_difference_h_a=h,
                cross_hessian_mev_per_a2_per_upper_atom=Cordered.tolist(),
                coefficient_mev_per_a_per_upper_atom=coef.tolist(),
                fit_rms_mev_per_a2=float(np.sqrt(np.mean(res*res))),
                target_rms_mev_per_a2=float(np.sqrt(np.mean(Cordered*Cordered))),
                relative_residual_norm=float(np.linalg.norm(res)/np.linalg.norm(Cordered)),
                fraction_squared_norm_explained=float(1-np.linalg.norm(res)**2/np.linalg.norm(Cordered)**2),
                uniform_height_cross_hessian_mev_per_a2=np.sum(Cordered,axis=1).tolist(),
                label_offset_scan=[dict(label_offset=c["label_offset"],residual_norm=c["residual_norm"]) for c in candidate],
                symmetry_residual_by_offset=[float(c["symmetry_residual_norm"]) for c in candidate],
                best_label_offset=best["label_offset"],best_offset_residual_norm=best["residual_norm"],
                best_offset_symmetry_break_norm=symmetry_break,
                symmetry_allowed_complement_residual_norm=allowed_residual,
                best_offset_coefficients_mev_per_a_per_atom=best["coefficients"])
checks=[projection(rc,h) for rc,h in ((14,1e-4),(16,1e-3),(16,1e-4),(16,1e-5),(18,1e-4))]
assert max(x["relative_residual_norm"] for x in checks)-min(x["relative_residual_norm"] for x in checks)<.03
print(json.dumps(dict(reference_grid_min_xy_a=rootxy.x.tolist(),reference_cart_translation_a=cart0.tolist(),
                      atom_labels=labels, mapping_note="Intrinsic top primitives swapped to match the carrier edge classes 0,1,5; Cartesian map basis@R@swap. Offset selected by C3 equivariance residual, not by K-span fit.",
                      K_span_rank=int(np.linalg.matrix_rank(B)),
                      C3_allowed_map_dimension=28-int(np.linalg.matrix_rank(constraint,tol=1e-9)),
                      checks=checks),indent=2))
