#!/usr/bin/env python3
"""Recompute Table II (2,1) first-star conventional benchmark; no experimental fit."""
import json, math
U1 = -2.02e-5  # eV / upper carbon atom, Minkin et al. Table II
bond = 1.42  # Angstrom, their methods
N = 7
a = math.sqrt(3)*bond
g = math.sqrt(N)*4*math.pi/(math.sqrt(3)*a)
V_cell = U1  # our 2 V_cell S per 2-atom Bravais cell = their 2 U1 S
range_atom = 9*abs(V_cell)/2
slide_atom = 8*abs(V_cell)/2
rotation_atom = 3*abs(U1)
curvature_atom = 1.5*abs(U1)*g*g
curvature_cell = 2*curvature_atom
amu=1.66053906660e-27; ev=1.602176634e-19; c=299792458
frequency = math.sqrt((curvature_cell*ev*1e20)/(12.011*amu))/(2*math.pi*c*100)
area_atom = math.sqrt(3)*a*a/4  # square Angstrom / C atom
max_force_atom = 4*math.pi*math.sqrt(N)*abs(U1)/a  # eV / Angstrom
shear_MPa = max_force_atom/area_atom*ev*1e24
fit_rms_atom = 0.0104*range_atom
assert V_cell==U1 and math.isclose(slide_atom,80.8e-6)
assert math.isclose(rotation_atom,60.6e-6)
assert math.isclose(range_atom,90.9e-6)
assert abs(frequency-9.153)/9.153 < 0.002
assert abs(shear_MPa-16.7)/16.7 < 0.002
print(json.dumps({'status':'NUMERICAL_CONVENTIONAL_ONLY','g_inv_A':g,'U1_eV_per_atom':U1,'Vstar_eV_per_two_atom_cell':V_cell,'global_range_microeV_per_atom':range_atom*1e6,'sliding_barrier_microeV_per_atom':slide_atom*1e6,'rotation_mean_barrier_microeV_per_atom':rotation_atom*1e6,'curvature_eV_per_A2_per_atom':curvature_atom,'shear_wavenumber_inv_cm':frequency,'ideal_shear_strength_MPa':shear_MPa,'first_star_fit_RMS_microeV_per_atom':fit_rms_atom*1e6},indent=2))
