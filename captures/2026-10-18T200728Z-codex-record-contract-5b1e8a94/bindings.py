from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def freeze():
 f=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
 for n,h in f['code_sha256'].items():assert sha(P/n)==h,'HOLD: frozen code changed'
 for n,h in f['inputs_sha256'].items():assert sha(P/'inputs'/n)==h,'HOLD: frozen input changed'
 return f
def entry(n):return next(e for e in freeze()['cases'] if e['case']==n)
def basis(n):
 import numpy as np
 with np.load(P/'inputs'/n/'BASIS_A.npz',allow_pickle=False) as z:a=z['basis']
 with np.load(P/'inputs'/n/'BASIS_B.npz',allow_pickle=False) as z:b=z['basis']
 return np.r_[a,b]
