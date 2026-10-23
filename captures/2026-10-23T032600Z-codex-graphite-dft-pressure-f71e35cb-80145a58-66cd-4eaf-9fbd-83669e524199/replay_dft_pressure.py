#!/usr/bin/env python3
"""Read four *data* archives from Zenodo record 16318186; never execute their scripts.

Usage: python replay_dft_pressure.py --source-dir /path/to/archives --output-dir /path/to/results
The source directory must contain the four qe-21-vdw-df3-*.tar.gz files.
"""
import argparse
import csv
import hashlib
import json
import math
import re
import tarfile
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np

SHA256 = {
    'aa': '6abb5cd8064d7f3edbabbafb8d7f2c68f6468b7b5bf8c15e035e0c1efa01e12a',
    'ab': 'c2c03213386df2e090dd42357d9ab4a3b4ad0e38907fb2265c0515e750d489d8',
    'sp': '75a1e5d2a311d45ee8985b17d6567e05f38e7cec17d1dec6dc4d766b580734b4',
    'opt-dist': '1a7e4d6c1ea466448436db2507da75c33216c7b09995547f7fd8a0731f873de0',
}
HARTREE_MEV = 27211.386245988
N_UPPER = 14
A_ANGSTROM = 2.4660
D0 = 3.4022


def read_scan(path, expected_hash):
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash, path
    results = {}
    failures = []
    with tarfile.open(path, 'r:gz') as archive:
        names = {m.name for m in archive.getmembers() if m.isfile()}
        for name in sorted(n for n in names if n.endswith('/struct.in')):
            root = name[:-len('/struct.in')]
            if path.name.endswith('opt-dist.tar.gz') and not root.startswith('qe-21-vdw-df3-opt-dist/qe-twisted-vdw-df3-dist/'):
                continue  # Select the finest AB scan; coarse scans duplicate separations.
            log, xmlpath = root + '/struct.out', root + '/pwscf.save/data-file-schema.xml'
            if log not in names or xmlpath not in names or b'JOB DONE' not in archive.extractfile(log).read():
                failures.append(root)
                continue
            inp = archive.extractfile(name).read().decode()
            assert 'nat              = 28' in inp and 'input_dft        = \'vdW-DF3-opt1\'' in inp
            assert re.search(r'^0\.0 0\.0 30\.0$', inp, re.M), root
            atoms = [list(map(float, line.split()[1:])) for line in inp.split('ATOMIC_POSITIONS angstrom')[1].splitlines() if line.startswith('C ')]
            assert len(atoms) == 28
            z = np.asarray(atoms)[:, 2]
            assert max(z[:14]) - min(z[:14]) < 1e-8 and max(z[14:]) - min(z[14:]) < 1e-8
            d = round(float(np.mean(z[14:]) - np.mean(z[:14])), 7)
            xml = ET.fromstring(archive.extractfile(xmlpath).read())
            e_ha = float(xml.findtext('.//total_energy/etot'))
            # Reject partial/inconsistent completed records, not a source-script energy summary.
            assert math.isfinite(e_ha) and d not in results
            results[d] = e_ha
    return results, failures


def fit_delta(points, window, degree):
    x = np.array([d-D0 for d in sorted(points) if abs(d-3.4) <= window+1e-8])
    y = np.array([points[round(v+D0, 7)] for v in x])
    coeff = np.polynomial.polynomial.polyfit(x, y, degree)
    return {'window_A':window, 'degree':degree, 'n':len(x), 'value_microeV_per_atom':float(coeff[0]),
            'derivative_microeV_per_atom_per_A':float(coeff[1]), 'log_derivative_per_A':float(coeff[1]/coeff[0])}


def fit_stiff(points, window, degree):
    x = np.array([d-D0 for d in sorted(points) if abs(d-D0) <= window+1e-8])
    e_ref = points[D0]
    y = np.array([(points[round(v+D0, 7)]-e_ref)*HARTREE_MEV/N_UPPER for v in x])
    coeff = np.polynomial.polynomial.polyfit(x, y, degree)
    return {'window_A':window, 'degree':degree, 'n':len(x), 'normal_stiffness_meV_per_atom_A2':float(2*coeff[2]),
            'local_energy_slope_meV_per_atom_A':float(coeff[1])}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-dir',type=Path,required=True)
    p.add_argument('--output-dir',type=Path,required=True)
    args=p.parse_args()
    scans={}; failures={}
    for key,digest in SHA256.items():
        scans[key], failures[key] = read_scan(args.source_dir / ('qe-21-vdw-df3-'+key+'.tar.gz'), digest)
    common = sorted(set(scans['aa']) & set(scans['ab']) & set(scans['sp']))
    assert len(common)==31 and all(len(scans[k])==31 and not failures[k] for k in ('aa','ab','sp'))
    delta = {d:(scans['aa'][d]-scans['ab'][d])*HARTREE_MEV*1000/N_UPPER for d in common}
    spdelta = {d:(scans['sp'][d]-scans['ab'][d])*HARTREE_MEV*1000/N_UPPER for d in common}
    # The fine AB minimum scan is restricted to 3.401..3.403 A; coarse scans may have failed jobs.
    fine = {d:e for d,e in scans['opt-dist'].items() if 3.401-1e-8 <= d <= 3.403+1e-8}
    assert len(fine)==21 and D0 in fine
    delta_fits=[fit_delta(delta,w,deg) for w,deg in ((.04,2),(.04,3),(.06,2),(.06,3))]
    stiff_fits=[fit_stiff(fine,w,deg) for w,deg in ((.0005,2),(.0008,2),(.001,2),(.001,3),(.001,4))]
    selected_delta=delta_fits[0]
    selected_stiff=stiff_fits[1]
    area=math.sqrt(3)*A_ANGSTROM*A_ANGSTROM/4
    # MPa * A^3 to meV: 10^6 Pa * 10^-30 m^3 / (1.602176634e-22 J/meV).
    force_per_mpa=area*1e6*1e-30/(1.602176634e-22)
    dd_dp=-force_per_mpa/selected_stiff['normal_stiffness_meV_per_atom_A2']
    log_strength=selected_delta['log_derivative_per_A']*dd_dp
    out={'source':{'record':'https://zenodo.org/records/16318186', 'sha256':SHA256,
                   'energies':'QE XML etot in Hartree; completed JOB DONE records only; rigid 28-atom cells, 14 upper atoms, 30 A vacuum'},
         'complete_counts':{k:len(scans[k]) for k in scans}, 'excluded_incomplete_counts':{k:len(failures[k]) for k in scans},
         'registry_samples_microeV_per_atom':{str(d):{'AA_minus_AB':delta[d], 'SP_minus_AB':spdelta[d]} for d in (3.4,3.5,3.54,3.56)},
         'delta_fits':delta_fits, 'normal_stiffness_fits':stiff_fits,
         'selected':{'at_d_A':D0,'delta_fit':selected_delta,'stiffness_fit':selected_stiff,'area_per_upper_atom_A2':area,
                     'normal_force_meV_per_atom_A_per_MPa':force_per_mpa,'dd_dP_A_per_MPa':dd_dp,
                     'dln_static_strength_dP_per_MPa':log_strength,
                     'dln_rigid_shear_frequency_dP_per_MPa':log_strength/2},
         'assumptions':'Uniform ideal rigid bilayer, fixed in-plane a, compression-positive P, local linear pressure response, type II first harmonic, no contact or relaxation corrections. Static strength and rigid shear frequency only; NOT kinetic friction or UD-specific loss.'}
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'DFT_PRESSURE_RESULTS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    with (args.output_dir/'DFT_REGISTRY_SCAN.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['d_A','AA_minus_AB_microeV_per_upper_atom','SP_minus_AB_microeV_per_upper_atom'])
        for d in common:w.writerow([f'{d:.2f}',f'{delta[d]:.9f}',f'{spdelta[d]:.9f}'])
    print(json.dumps(out['selected'],indent=2))

if __name__=='__main__':main()
