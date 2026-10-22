#!/usr/bin/env python3
"""Compute nearby stationary saddles and straight-path force from public (2,1) PES.

Usage: python3 derive_kc_barrier_replay.py /path/to/public-dataset.zip
Read only X/Y/Z text; no archived source code is executed. This is a
fixed-height conventional simulation comparison, not measured friction.
"""
import hashlib,io,json,math,sys,zipfile
import numpy as np
from scipy.optimize import root
sha='b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875'
with open(sys.argv[1],'rb') as h:assert hashlib.file_digest(h,'sha256').hexdigest()==sha
with zipfile.ZipFile(sys.argv[1]) as z:
    def read(q):
        n=next(s for s in z.namelist() if '/data/pes21_' in s and s.endswith('/'+q+'.txt'))
        return np.loadtxt(io.BytesIO(z.read(n)))
    grids={q:read(q) for q in 'XYZ'}
xy=np.column_stack([grids['X'].ravel(),grids['Y'].ravel()]);Z=grids['Z'].ravel()
a=math.sqrt(3)*1.42;g=math.sqrt(7)*4*math.pi/(math.sqrt(3)*a)
G=np.array([[math.cos(math.pi/6),math.sin(math.pi/6)],
            [math.cos(5*math.pi/6),math.sin(5*math.pi/6)]])*g
T=2*math.pi*np.linalg.inv(G)
area_atom=math.sqrt(3)*a*a/4
meV_per_A3_to_MPa=1.602176634e2
out={"source_archive_sha256":sha,"dataset_doi":"10.17632/svnpzbjc3t.1","height_A":3.46,"status":"NUMERICAL_CONVENTIONAL_STATIC_ONLY","path_note":"Three nearest translations and local saddle roots; straight-path force is not a separately optimized curved MEP force.","models":[]}
for ns in ([1],[1,3]):
    vectors=[]
    for p in range(-2,3):
        for q in range(-2,3):
            norm=p*p+q*q-p*q
            if norm in ns and (p>0 or p==0 and q>0):vectors.append(p*G[0]+q*G[1])
    vectors=np.array(vectors);P=xy@vectors.T
    F=np.column_stack([np.ones(len(Z))]+[fn(P[:,j]) for j in range(len(vectors)) for fn in (np.cos,np.sin)])
    coef=np.linalg.lstsq(F,Z,rcond=None)[0];C=coef[1::2];S=coef[2::2]
    def energy(x):
        ph=vectors@x;return coef[0]+C@np.cos(ph)+S@np.sin(ph)
    def gradient(x):
        ph=vectors@x;return vectors.T@(-C*np.sin(ph)+S*np.cos(ph))
    def hessian(x):
        ph=vectors@x;return vectors.T@np.diag(-C*np.cos(ph)-S*np.sin(ph))@vectors
    seedphase=[]
    for v in G:
        j=np.argmin(np.linalg.norm(vectors-v,axis=1))
        seedphase.append(math.atan2(-S[j],C[j]))
    translation=np.linalg.solve(G,np.array(seedphase)+math.pi)
    minsol=root(gradient,-translation)
    assert minsol.success and min(np.linalg.eigvalsh(hessian(minsol.x)))>0
    m={"norm_classes":ns,"minimum_energy_stored_meV_per_atom":float(energy(minsol.x)),"directions":[]}
    for d in (T[:,0],T[:,1],T[:,0]-T[:,1]):
        saddle=root(gradient,minsol.x+d/2)
        assert saddle.success
        eig=np.linalg.eigvalsh(hessian(saddle.x));assert eig[0]<0<eig[1]
        t=np.linspace(0,1,10001)
        direction=d/np.linalg.norm(d)
        slopes=np.array([abs(gradient(minsol.x+u*d)@direction) for u in t])
        m['directions'].append({"period_A":float(np.linalg.norm(d)),
          "nearby_saddle_barrier_microeV_per_atom":float(1000*(energy(saddle.x)-energy(minsol.x))),
          "saddle_hessian_eigen_meV_per_A2_per_atom":[float(v) for v in eig],
          "straight_path_max_force_meV_per_A_per_atom":float(max(slopes)),
          "straight_path_max_shear_strength_MPa":float(max(slopes)/area_atom*meV_per_A3_to_MPa)})
    out['models'].append(m)
assert 80.9<out['models'][0]['directions'][0]['nearby_saddle_barrier_microeV_per_atom']<81.1
assert 78.1<out['models'][1]['directions'][0]['nearby_saddle_barrier_microeV_per_atom']<78.4
print(json.dumps(out,indent=2))
