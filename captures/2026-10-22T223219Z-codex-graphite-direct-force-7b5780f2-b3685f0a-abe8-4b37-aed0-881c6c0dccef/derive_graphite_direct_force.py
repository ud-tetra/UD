#!/usr/bin/env python3
"""Driven straight-path response of a reconstructed index-seven graphite PES.

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
from scipy.optimize import brentq

# The above preamble reconstructs rigid KC E/Ez/Ezz at 3.46 Angstrom and
# defines the same two allowed reciprocal shells as manuscript v13.
vals = pair_fields(3.46, 16)
coefs = np.linalg.lstsq(F, vals, rcond=None)[0]  # basis x [E,Ez,Ezz], meV
def e_grad(x):
    ph = vectors @ x
    c = coefs[:, 0]
    energy = c[0] + c[1::2] @ np.cos(ph) + c[2::2] @ np.sin(ph)
    grad = vectors.T @ (-c[1::2] * np.sin(ph) + c[2::2] * np.cos(ph))
    hess = vectors.T @ np.diag(-c[1::2] * np.cos(ph) - c[2::2] * np.sin(ph)) @ vectors
    return energy, grad, hess
first = [np.argmin(np.linalg.norm(vectors - v, axis=1)) for v in G]
phases = [math.atan2(-coefs[1 + 2*j, 0], coefs[2 + 2*j, 0]) for j in first]
seed = -np.linalg.solve(G, np.array(phases) + math.pi)
minroot = root(lambda x: e_grad(x)[1], seed, tol=1e-11)
assert np.linalg.norm(e_grad(minroot.x)[1]) < 1e-9
assert np.min(np.linalg.eigvalsh(e_grad(minroot.x)[2])) > 0

def field_at(x):
    ph = vectors @ x
    b = np.r_[1., np.column_stack([np.cos(ph), np.sin(ph)]).ravel()]
    return b @ coefs
load0 = -field_at(minroot.x)[1]
area_atom = math.sqrt(3) * a*a/4
force_per_mpa = area_atom * 1000 / 160217.6634 # meV/Angstrom/atom/MPa
to_mpa = 160.2176634 / area_atom # meV/Angstrom/atom -> MPa

def path(pressure, translation, count):
    length = np.linalg.norm(translation)
    direction = translation/length
    t = np.arange(count)/count
    points = minroot.x[None, :] + t[:, None]*translation[None, :]
    ph = points @ vectors.T
    ds_phase = vectors @ direction
    b = np.column_stack([np.ones(count)] + [f(ph[:, j]) for j in range(len(vectors)) for f in (np.cos, np.sin)])
    db = np.column_stack([np.zeros(count)] + [f(ph[:, j])*ds_phase[j] for j in range(len(vectors)) for f in (lambda theta:-np.sin(theta), np.cos)])
    fields = b @ coefs
    derivs = db @ coefs
    load = load0 + pressure*force_per_mpa
    assert np.min(fields[:, 2]) > 100  # meV/Angstrom^2/atom
    dz = -(fields[:, 1] + load)/fields[:, 2]
    eff = fields[:, 0] - (fields[:, 1]+load)**2/(2*fields[:, 2])
    force = derivs[:, 0] + dz*derivs[:, 1] + .5*dz*dz*derivs[:, 2]
    fd = (np.roll(eff, -1)-np.roll(eff, 1))/(2*length/count)
    assert np.max(np.abs(fd-force)) < 2e-5
    assert abs(np.mean(force)) < 1e-8
    return dict(length_a=float(length), critical_mev_per_a=float(np.max(force)),
                min_force_mev_per_a=float(np.min(force)),
                force_mev_per_a=force, max_abs_height_excursion_a=float(np.max(np.abs(dz))))

def drive_force(path_force, target_drag_force):
    threshold = np.max(path_force)
    # Overdamped 1D transport: gamma*v = 1/mean[1/(F-U')].
    def residual(drive):
        return 1/np.mean(1/(drive-path_force)) - target_drag_force
    hi = threshold + max(1, 2*target_drag_force)
    while residual(hi) < 0: hi *= 2
    found = brentq(residual, threshold+1e-12, hi, xtol=1e-12)
    assert abs(residual(found)/target_drag_force) < 1e-9
    return found

directions = (T[:, 0], T[:, 1], T[:, 0]-T[:, 1])
results = []
for index, direction in enumerate(directions):
    count = 8192
    baseline = path(0, direction, count)
    plus = path(5, direction, count)
    minus = path(-5, direction, count)
    fc0 = baseline["critical_mev_per_a"]
    fcprime = (plus["critical_mev_per_a"]-minus["critical_mev_per_a"])/10
    rates = []
    for u in (.1, 1, 10):
        target = u*fc0
        center_force = drive_force(baseline["force_mev_per_a"], target)
        slope = (drive_force(plus["force_mev_per_a"], target) -
                 drive_force(minus["force_mev_per_a"], target))/10
        rates.append(dict(reduced_speed_gamma_v_over_fc=u,
                          drive_force_mev_per_a_per_atom=float(center_force),
                          excess_force_mev_per_a_per_atom=float(center_force-target),
                          pressure_slope_mev_per_a_per_atom_per_mpa=float(slope),
                          pressure_slope_shear_mpa_per_normal_mpa=float(slope*to_mpa),
                          fraction_of_depinning_force_slope=float(slope/fcprime)))
    results.append(dict(path_index=index, path_period_a=baseline["length_a"],
                        reference_depinning_mev_per_a_per_atom=fc0,
                        reference_depinning_shear_mpa=fc0*to_mpa,
                        local_depinning_slope_mev_per_a_per_atom_per_mpa=float(fcprime),
                        vertical_excursion_a=baseline["max_abs_height_excursion_a"],
                        rates=rates))

# Independent grid-density sensitivity for the first path.
grid_check = []
for count in (2048, 4096, 8192):
    minus = path(-5, directions[0], count)
    center = path(0, directions[0], count)
    plus = path(5, directions[0], count)
    speed = center["critical_mev_per_a"]
    dynamic_slope = (drive_force(plus["force_mev_per_a"], speed) -
                     drive_force(minus["force_mev_per_a"], speed))/10
    grid_check.append(dict(samples=count, depinning_mev_per_a_per_atom=center["critical_mev_per_a"],
                           force_slope_at_u1_mev_per_a_per_atom_per_mpa=dynamic_slope))
assert abs(grid_check[0]["force_slope_at_u1_mev_per_a_per_atom_per_mpa"] -
           grid_check[-1]["force_slope_at_u1_mev_per_a_per_atom_per_mpa"]) < 1e-8
pressure_check = []
for h in (1, 2, 5):
    p = path(h, directions[0], 8192)
    m = path(-h, directions[0], 8192)
    reference_drag = results[0]["reference_depinning_mev_per_a_per_atom"]
    slope = (drive_force(p["force_mev_per_a"], reference_drag) -
             drive_force(m["force_mev_per_a"], reference_drag))/(2*h)
    pressure_check.append(dict(halfspan_mpa=h, force_slope_at_u1_mev_per_a_per_atom_per_mpa=slope))
assert abs(pressure_check[0]["force_slope_at_u1_mev_per_a_per_atom_per_mpa"] -
           pressure_check[-1]["force_slope_at_u1_mev_per_a_per_atom_per_mpa"]) < 2e-8
for p in results:
    assert all(0 < r["fraction_of_depinning_force_slope"] < 1.1 for r in p["rates"])

print(json.dumps(dict(status="NUMERICAL_CONDITIONAL_TWO_SHELL_DRIVEN_STRAIGHT_PATH",
                      source_archive_sha256=ARCHIVE_SHA,
                      cutoff_a=16, input_grid_points=len(xy), reference_min_height_a=3.46,
                      reference_load_mev_per_a_per_atom=float(load0),
                      reference_load_equiv_mpa=float(load0/force_per_mpa),
                      model="Rigid KC pair sum -> two-shell x,y Fourier and quadratic-z Taylor -> exact local vertical relaxation on a declared straight periodic path -> deterministic overdamped constant-force transport. Gamma*v fixed in reduced force units; gamma not measured.",
                      pressure_probe_mpa=[-5,0,5],
                      quadrature="uniform periodic trapezoidal quadrature over 1/(F-dUeff/ds); root solve for prescribed gamma*v",
                      paths=results, grid_check=grid_check, pressure_check=pressure_check,
                      source_mismatch_note="Reconstructed PES differs from deposited simulation; finite cutoff and run identity unresolved. Straight path and drive model are not the experimental force estimator.",
                      physical_promotion=0), indent=2))
