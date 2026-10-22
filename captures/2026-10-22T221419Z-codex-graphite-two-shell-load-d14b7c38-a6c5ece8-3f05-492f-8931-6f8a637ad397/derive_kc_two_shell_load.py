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
data = []
for cutoff in (14, 16, 18):
    vals = pair_fields(3.46, cutoff)
    coefs = np.linalg.lstsq(F, vals, rcond=None)[0]  # rows: basis; columns: E, Ez, Ezz
    def coeffs(dz):
        return coefs[:, 0] + dz * coefs[:, 1] + 0.5 * dz**2 * coefs[:, 2]
    def spectrum(x, dz):
        c = coeffs(dz)
        ph = vectors @ x
        cos, sin = np.cos(ph), np.sin(ph)
        energy = c[0] + c[1::2] @ cos + c[2::2] @ sin
        grad = vectors.T @ (-c[1::2] * sin + c[2::2] * cos)
        hess = vectors.T @ np.diag(-c[1::2] * cos - c[2::2] * sin) @ vectors
        return energy, grad, hess
    def ez(x, dz):
        c = coefs[:, 1] + dz * coefs[:, 2]
        ph = vectors @ x
        return c[0] + c[1::2] @ np.cos(ph) + c[2::2] @ np.sin(ph)
    def stationarity(v, load):
        _, gx, _ = spectrum(v[:2], v[2] - 3.46)
        return np.r_[gx, ez(v[:2], v[2] - 3.46) + load]
    # Minimize near the first-shell negative branch; construct three index-neighbor saddles.
    first = [np.argmin(np.linalg.norm(vectors - v, axis=1)) for v in G]
    phases = [math.atan2(-coefs[1 + 2 * j, 0], coefs[2 + 2 * j, 0]) for j in first]
    shift = np.linalg.solve(G, np.array(phases) + math.pi)
    minxy = root(lambda x: spectrum(x, 0)[1], -shift, tol=1e-11)
    assert minxy.success and min(np.linalg.eigvalsh(spectrum(minxy.x, 0)[2])) > 0
    load0 = -ez(minxy.x, 0)
    min0 = root(stationarity, np.r_[minxy.x, 3.46], args=(load0,), tol=1e-10)
    assert np.linalg.norm(stationarity(min0.x, load0)) < 1e-7
    minimum_energy = spectrum(min0.x[:2], min0.x[2] - 3.46)[0]
    saddles = []
    for d in (T[:, 0], T[:, 1], T[:, 0] - T[:, 1]):
        x0 = root(lambda x: spectrum(x, 0)[1], minxy.x + d / 2, tol=1e-11)
        assert np.linalg.norm(spectrum(x0.x, 0)[1]) < 1e-7
        eig = np.linalg.eigvalsh(spectrum(x0.x, 0)[2])
        assert eig[0] < 0 < eig[1]
        sol = root(stationarity, np.r_[x0.x, 3.46], args=(load0,), tol=1e-10)
        assert np.linalg.norm(stationarity(sol.x, load0)) < 1e-7
        def barrier(pressure):
            l = load0 + pressure * force_per_mpa
            m = root(stationarity, min0.x, args=(l,), tol=1e-10)
            s = root(stationarity, sol.x, args=(l,), tol=1e-10)
            assert np.linalg.norm(stationarity(m.x, l)) < 1e-6 and np.linalg.norm(stationarity(s.x, l)) < 1e-6
            em = spectrum(m.x[:2], m.x[2] - 3.46)[0]
            es = spectrum(s.x[:2], s.x[2] - 3.46)[0]
            return 1000 * (es - em + l * (s.x[2] - m.x[2]))
        slope = (barrier(5) - barrier(-5)) / 10
        envelope = 1000 * force_per_mpa * (sol.x[2] - min0.x[2])
        assert abs(slope - envelope) < 5e-6
        saddles.append(dict(barrier_microeV_per_atom=barrier(0),
                            saddle_minus_min_height_A=float(sol.x[2] - min0.x[2]),
                            slope_microeV_per_atom_per_MPa=float(slope),
                            envelope_slope_microeV_per_atom_per_MPa=float(envelope),
                            height_at_saddle_A=float(sol.x[2])))
    data.append(dict(cutoff_A=cutoff, reference_height_A=3.46,
                     reference_load_meV_per_A_per_atom=float(load0),
                     mean_energy_offset_from_archive_meV_per_atom=float(np.mean(vals[:, 0] - Z)),
                     sampled_grid_centered_rms_microeV_per_atom=float(1000 * np.std(vals[:, 0] - Z)),
                     normal_curvature_min_meV_per_A2_per_atom=float(
                         coefs[0, 2] + coefs[1::2, 2] @ np.cos(vectors @ min0.x[:2])
                         + coefs[2::2, 2] @ np.sin(vectors @ min0.x[:2])),
                     saddles=saddles))
assert all(70 < s['barrier_microeV_per_atom'] < 90 for row in data for s in row['saddles'])
print(json.dumps(dict(status="NUMERICAL_CONDITIONAL_TWO_SHELL_KC_EQUILIBRIUM_LOAD",
                      source_archive_sha256=ARCHIVE_SHA,
                      source="Minkin et al. SI PRB 108 085411 (2023) Eq S1/Table S1; Mendeley Data 10.17632/svnpzbjc3t.1 coordinates",
                      approximation="first+norm3 common reciprocal shells, second-order vertical Taylor expansion at 3.46 Angstrom, local nearby saddles; rigid planar sheets, spherical pair cutoff",
                      reference_load_note="L0 chosen so first-shell plus second-shell stationary minimum has z=3.46 Angstrom; it is not a calibrated laboratory contact pressure",
                      pressure_unit="force_per_atom_per_MPa = area_atom*1000/160217.6634 meV/Angstrom",
                      sampled_points=len(xy), results=data, physical_promotion=0), indent=2))
