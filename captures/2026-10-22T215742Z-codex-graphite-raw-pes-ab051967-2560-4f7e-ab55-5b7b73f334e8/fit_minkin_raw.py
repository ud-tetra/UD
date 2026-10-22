#!/usr/bin/env python3
"""Reproduce finite-height (2,1) Fourier fit from Minkin et al. raw public PES.

Usage: python3 fit_minkin_raw.py /path/to/dataset.zip
Reads only X/Y/Z text data from the archive, never executes archived scripts.
"""
import hashlib, io, json, math, sys, zipfile
import numpy as np
from scipy.optimize import least_squares

EXPECTED_SHA='b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875'
archive=sys.argv[1]
with open(archive,'rb') as h:
    digest=hashlib.file_digest(h,'sha256').hexdigest()
assert digest==EXPECTED_SHA, 'Unexpected archive bytes; review provenance before fitting'
with zipfile.ZipFile(archive) as f:
    names=f.namelist()
    def read(q):
        target=next(n for n in names if '/data/pes21_' in n and n.endswith('/'+q+'.txt'))
        return np.loadtxt(io.BytesIO(f.read(target)))
    grids={q:read(q) for q in 'XYZ'}
assert all(v.shape==(128,129) for v in grids.values())
X,Y,Z=(grids[q].ravel() for q in 'XYZ')
a=1.42*math.sqrt(3) # Angstrom, source bond length
magnitude=math.sqrt(7)*4*math.pi/(math.sqrt(3)*a)
G=np.array([[math.cos(math.pi/6),math.sin(math.pi/6)],
            [math.cos(5*math.pi/6),math.sin(5*math.pi/6)]])*magnitude
G3=-sum(G)
assert np.isclose(np.linalg.norm(G3),np.linalg.norm(G[0]))
xy=np.column_stack([X,Y]); phases=np.column_stack([xy@v for v in (*G,G3)])
A=np.column_stack([np.ones(Z.size)]+[fn(phases[:,j]) for j in range(3) for fn in (np.cos,np.sin)])
coefs=np.linalg.lstsq(A,Z,rcond=None)[0]
lin_res=Z-A@coefs
amplitudes=[math.hypot(coefs[1+2*j],coefs[2+2*j]) for j in range(3)]
angle=[math.atan2(-coefs[2+2*j],coefs[1+2*j]) for j in range(3)]
phase_closure=((sum(angle)-math.pi+math.pi)%(2*math.pi)-math.pi)
translation=np.linalg.solve(G,np.array(angle[:2])+math.pi)
def predict(params):
    offset,amp,tx,ty=params
    return offset+amp*np.cos(phases+np.array([*(G@np.array([tx,ty])),G3@np.array([tx,ty])])).sum(axis=1)
fit=least_squares(lambda p:predict(p)-Z,[coefs[0],-np.mean(amplitudes),*translation],max_nfev=100)
constraint_res=Z-predict(fit.x)
# Common reciprocal-lattice shells: |p G1+q G2|^2/g^2 = p^2+q^2-pq.
fields={}
for p in range(-4,5):
    for q in range(-4,5):
        n=p*p+q*q-p*q
        if n in (1,3,4,7) and (p>0 or (p==0 and q>0)):
            phase=xy@(p*G[0]+q*G[1]);fields[(p,q,n)]=np.column_stack([np.cos(phase),np.sin(phase)])
r,c=np.indices(grids['Z'].shape)
holdout=((r+3*c)%4==0).ravel()
models=[]
for ns in ([1],[1,3],[1,3,4],[1,3,4,7]):
    keys=[key for key in fields if key[2] in ns]
    F=np.column_stack([np.ones(Z.size)]+[fields[k][:,i] for k in keys for i in (0,1)])
    beta=np.linalg.lstsq(F[~holdout],Z[~holdout],rcond=None)[0]
    model={'norm_classes':ns,'basis_wavevectors':len(keys)}
    for mask,label in ((~holdout,'train'),(holdout,'holdout')):
        res=Z[mask]-F[mask]@beta
        model[label+'_rms_microeV_per_atom']=float(1000*np.sqrt(np.mean(res**2)))
    model['amplitudes_microeV_per_atom']={str(n):[float(1000*math.hypot(beta[1+2*j],beta[2+2*j])) for j,k in enumerate(keys) if k[2]==n] for n in ns}
    models.append(model)
assert 0.9<1000*np.sqrt(np.mean(lin_res**2))<1.0
assert -20.5<1000*fit.x[1]<-20.0
assert 0.41<models[1]['holdout_rms_microeV_per_atom']<0.44
assert abs(phase_closure)<0.002
output={
 'status':'NUMERICAL_CONVENTIONAL_RAW_PES',
 'archive_sha256':digest,
 'dataset_doi':'10.17632/svnpzbjc3t.1',
 'dataset_subfolder':'data/pes21_10x10_Rc=16_lz=3.46',
 'grid_shape':list(grids['Z'].shape),
 'separation_A':3.46,
 'stored_Z_range':float(np.ptp(Z)),
 'stored_Z_units':'meV per upper-layer carbon atom, inferred from supplied plotting script multiplying Z-min(Z) by 1000 to label microeV',
 'energy_range_microeV_per_atom':float(1000*np.ptp(Z)),
 'first_shell_unconstrained_amplitudes_microeV_per_atom':[float(1000*v) for v in amplitudes],
 'first_shell_phase_closure_error_radians':float(phase_closure),
 'first_shell_unconstrained_rms_microeV_per_atom':float(1000*np.sqrt(np.mean(lin_res**2))),
 'first_shell_unconstrained_rms_over_range':float(np.sqrt(np.mean(lin_res**2))/np.ptp(Z)),
 'symmetric_three_cosine_amplitude_microeV_per_atom':float(1000*fit.x[1]),
 'symmetric_three_cosine_rms_microeV_per_atom':float(1000*np.sqrt(np.mean(constraint_res**2))),
 'cross_validated_shell_models':models,
 'holdout_definition':'(row+3*col) mod 4 == 0; spatially interlaced points from same fixed-height simulation, not an independent potential or experiment',
 'raw_script_execution':False,
 'physical_promotion':0
}
print(json.dumps(output,indent=2))
