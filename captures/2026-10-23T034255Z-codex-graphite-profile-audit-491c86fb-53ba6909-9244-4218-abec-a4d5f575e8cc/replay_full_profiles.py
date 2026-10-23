#!/usr/bin/env python3
"""Replay two public 37-point (2,1) rigid lateral scans and AB normal scan.

Source: https://doi.org/10.5281/zenodo.16318186. Treat archives as data.
Usage: python replay_full_profiles.py --source-dir DIR --output-dir DIR
"""
import argparse
import csv
import hashlib
import json
import math
import tarfile
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np

SHA256 = {
    '3.4022': '05e5e995d70ad83a98f8b534addb3dcff51ff3422c8f24dcba25453c3e76e228',
    '3.34': '5d6efcbd67db3093711ed92bd06d7098254fbe21680a869dd941664ad6190443',
    'ab': 'c2c03213386df2e090dd42357d9ab4a3b4ad0e38907fb2265c0515e750d489d8',
}
HARTREE_TO_MICROEV_PER_UPPER = 27211.386245988 * 1000 / 14
HARTREE_TO_MEV_PER_UPPER = 27211.386245988 / 14
A = 2.4660
N_C = 7
PRESSURE_FORCE = (math.sqrt(3)*A*A/4)*1e6*1e-30/(1.602176634e-22)  # meV/A per upper atom per MPa


def files_in_archive(path):
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest==SHA256['ab' if path.name.endswith('-ab.tar.gz') else path.name.split('df3-')[1].split('A-h30A')[0]]
    with tarfile.open(path, 'r:gz') as t:
        names=set(m.name for m in t.getmembers() if m.isfile())
        for name in sorted(n for n in names if n.endswith('/struct.in')):
            root=name[:-len('/struct.in')]
            xmlpath=root+'/pwscf.save/data-file-schema.xml'
            assert root+'/struct.out' in names and xmlpath in names
            assert b'JOB DONE' in t.extractfile(root+'/struct.out').read(), root
            inp=t.extractfile(name).read().decode()
            assert 'nat              = 28' in inp and 'input_dft        = \'vdW-DF3-opt1\'' in inp
            assert '0.0 0.0 30.0' in inp
            atoms=np.asarray([list(map(float,line.split()[1:])) for line in inp.split('ATOMIC_POSITIONS angstrom')[1].splitlines() if line.startswith('C ')])
            assert atoms.shape==(28,3)
            e=float(ET.fromstring(t.extractfile(xmlpath).read()).findtext('.//total_energy/etot'))
            yield root,e,atoms


def profile(path,target_d):
    dct={}
    for root,e,atoms in files_in_archive(path):
        i=int(root.rsplit('/dir_',1)[1]);assert i not in dct
        z=float(np.mean(atoms[14:,2])-np.mean(atoms[:14,2]))
        assert abs(z-target_d)<1e-6
        assert np.max(abs(atoms[14:,:2]-atoms[0:1,:2]))>0
        dct[i]=(e,atoms[14,0:2])
    assert sorted(dct)==list(range(37))
    e=np.array([dct[i][0] for i in range(37)])
    xy=np.array([dct[i][1] for i in range(37)])
    dx=xy[:,0]-xy[0,0];dy=xy[:,1]-xy[0,1]
    # Use the actual archived cell geometry; the published a=2.4660 A is rounded.
    kx=3*math.pi/dx[-1]
    ky=math.pi/dy[-1]
    assert abs(kx/ky-math.sqrt(3))<1e-8
    assert max(abs(kx*dx-np.arange(37)*math.pi/12))<1e-10
    assert max(abs(ky*dy-np.arange(37)*math.pi/36))<1e-10
    # Type-II AB minimum: kx*x0=0, ky*y0=2pi/3, first harmonic f0=-3/2.
    shape=2*np.cos(2*math.pi/3+ky*dy)*np.cos(kx*dx)+np.cos(4*math.pi/3+2*ky*dy)+1.5
    signal=(e-e[0])*HARTREE_TO_MICROEV_PER_UPPER
    u=float(np.dot(signal,shape)/np.dot(shape,shape))
    residual=signal-u*shape
    assert u>0 and abs(shape[12]-4.5)<1e-10 and abs(shape[24])<1e-10
    return {'d_A':target_d,'points':37,'U1_fit_microeV_per_upper':u,
            'rms_residual_microeV_per_upper':float(np.sqrt(np.mean(residual**2))),
            'relative_rms_to_observed_peak':float(np.sqrt(np.mean(residual**2))/max(signal)),
            'observed_max_minus_index0_microeV_per_upper':float(max(signal)),
            'peak_index':int(np.argmax(signal)),'peak_gap_U1_proxy_microeV_per_upper':float(max(signal)/4.5),
            'endpoint_mismatch_microeV_per_upper':float(signal[-1]),
            'tau_from_U1_Pa':float(6.182800612*math.sqrt(N_C)*(u*1e-6*1.602176634e-19)/(A*1e-10)**3)},signal,shape


def ab_pressure(path):
    energies={}
    for root,e,atoms in files_in_archive(path):
        d=round(float(np.mean(atoms[14:,2])-np.mean(atoms[:14,2])),7)
        assert d not in energies
        energies[d]=e
    assert len(energies)==31 and 3.34 in energies
    fits=[]
    for window,degree in ((.02,2),(.04,2),(.04,3),(.06,3),(.08,3)):
        x=np.array([d-3.34 for d in sorted(energies) if abs(d-3.34)<=window+1e-9])
        y=np.array([(energies[round(3.34+v,7)]-energies[3.34])*HARTREE_TO_MEV_PER_UPPER for v in x])
        c=np.polynomial.polynomial.polyfit(x,y,degree)
        fits.append({'window_A':window,'degree':degree,'n':len(x),
                     'energy_slope_meV_per_atom_A':float(c[1]),
                     'compression_pressure_MPa':float(-c[1]/PRESSURE_FORCE)})
    return fits


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    arg=parser.parse_args()
    profiles={};signals={};shape=None
    for label in ('3.4022','3.34'):
        profiles[label],signals[label],shape=profile(arg.source_dir/('qe-21-vdw-df3-'+label+'A-h30A.tar.gz'),float(label))
    pressure_fits=ab_pressure(arg.source_dir/'qe-21-vdw-df3-ab.tar.gz')
    s0=signals['3.4022'];s1=signals['3.34']
    scaling=float(np.dot(s0,s1)/np.dot(s0,s0));res=s1-scaling*s0
    u0=profiles['3.4022']['U1_fit_microeV_per_upper'];u1=profiles['3.34']['U1_fit_microeV_per_upper']
    out={'source':'https://doi.org/10.5281/zenodo.16318186','sha256':SHA256,
         'profiles':profiles,'first_harmonic_shape':'f_i-f_0 = 2 cos(2pi/3+i*pi/36) cos(i*pi/12) + cos(4pi/3+i*pi/18) + 3/2; from source scan displacement and Eq. 2 of Lebedeva et al.',
         'cross_separation':{'U1_ratio_3p34_over_3p4022':u1/u0,
             'secant_dlnU1_dd_per_A':math.log(u1/u0)/(3.34-3.4022),
             'profile_scale_3p34_over_3p4022':scaling,
             'rms_non_scaling_residual_microeV_per_atom':float(np.sqrt(np.mean(res**2))),
             'max_non_scaling_residual_fraction_of_3p34_peak':float(max(abs(res))/max(s1))},
         'pressure_at_3p34_fits':pressure_fits,
         'pressure_at_3p34_nominal_MPa':pressure_fits[2]['compression_pressure_MPa'],
         'finite_ln_static_strength_ratio_per_MPa':math.log(u1/u0)/pressure_fits[2]['compression_pressure_MPa'],
         'scope':'Two discrete spacings constrain a finite rigid static change; they do not determine dU1/dd at 3.4022 A. Pressure at 3.34 A inferred from AB normal-energy scan. No kinetic friction or UD-specific damping.'}
    arg.output_dir.mkdir(parents=True,exist_ok=True)
    (arg.output_dir/'FULL_PROFILE_RESULTS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    with (arg.output_dir/'FULL_PROFILE_SCAN.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['index','first_harmonic_shape','d3p4022_relative_microeV_per_upper','d3p34_relative_microeV_per_upper'])
        for i in range(37):w.writerow([i,f'{shape[i]:.12f}',f'{s0[i]:.9f}',f'{s1[i]:.9f}'])
    print(json.dumps({'profiles':profiles,'cross_separation':out['cross_separation'],'P_3p34_MPa':out['pressure_at_3p34_nominal_MPa']},indent=2))

if __name__=='__main__':main()
