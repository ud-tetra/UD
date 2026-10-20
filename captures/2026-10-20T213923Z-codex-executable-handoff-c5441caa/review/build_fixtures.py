#!/usr/bin/env python3
"""Small explicit spectral proposals; no estimator, acquisition or root-source edits."""
import hashlib,json,os
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent;D=P/'fixtures';D.mkdir(exist_ok=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,N,S=(2.,0.)):
 d=D/name;d.mkdir();np.save(d/'N.npy',np.array(N,dtype='<i8'));np.savez(d/'SVD_META.npz',singular=np.array(S),right_transpose=np.eye(2));np.savez(d/'U.npz',basis=np.array([[1.],[0.]]))
 m={'schema_version':'1.0','record':{'path':'N.npy','sha256':sha(d/'N.npy'),'payload_sha256':hashlib.sha256(np.array(N,dtype='<i8').tobytes()).hexdigest(),'dyadic_exponent':0},'svd':{'path':'SVD_META.npz','sha256':sha(d/'SVD_META.npz')},'left_chunks':[{'path':'U.npz','sha256':sha(d/'U.npz'),'start':0,'stop':2}]}
 (d/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');return d,m
base,m=save('exact_q1',[[2,0],[0,0]])
save('distinct_exact_q1',[[3,0],[0,0]],(3.,0.))
save('numerical_hold',[[2,0],[0,1]])
for name,mut in [('hash_mismatch',lambda x:x['record'].update(sha256='0'*64)),('missing_field',lambda x:x.pop('svd')),('unknown_field',lambda x:x.update(physical_promotion=1)),('relative_escape',lambda x:x['record'].update(path='../exact_q1/N.npy'))]:
 d,mm=save(name,[[2,0],[0,0]]);mut(mm);(d/'manifest.json').write_text(json.dumps(mm,indent=2)+'\n')
# Explicit symlink record and ancestor; no generated fixtures are included in capture.
d,mm=save('symlink_record',[[2,0],[0,0]]);(d/'N.npy').unlink();(d/'N.npy').symlink_to(base/'N.npy');(d/'manifest.json').write_text(json.dumps(mm,indent=2)+'\n')
(D/'existing_output').mkdir();(D/'existing_output'/'sentinel').write_bytes(b'PRESERVE_C22_SENTINEL\n')
index={'synthetic_inputs_only':True,'no_estimator_calls':0,'expected':[{'name':'exact_q1','state':'NUMERICAL_PASS_PROVENANCE_HOLD','audit':True},{'name':'distinct_exact_q1','state':'NUMERICAL_PASS_PROVENANCE_HOLD','audit':True},{'name':'numerical_hold','state':'HOLD_NUMERICAL','audit':False},*({'name':n,'state':'PREOUTPUT_REJECT','audit':False} for n in ['hash_mismatch','missing_field','unknown_field','relative_escape','symlink_record','existing_output','output_is_input','source_pin_changed'])]}
(P/'FIXTURES.json').write_text(json.dumps(index,indent=2)+'\n')
rows=[]
for f in sorted(D.rglob('*')):
 if f.is_symlink():rows.append({'path':str(f.relative_to(P)),'symlink':os.readlink(f)})
 elif f.is_file():rows.append({'path':str(f.relative_to(P)),'sha256':sha(f),'bytes':f.stat().st_size})
(P/'FIXTURE_FREEZE.json').write_text(json.dumps({'status':'FROZEN_BEFORE_RUNNER_EXECUTION','builder_sha256':sha(Path(__file__)),'index_sha256':sha(P/'FIXTURES.json'),'rows':rows,'physical_promotion':0},indent=2)+'\n')
print(json.dumps({'fixture_file_or_link_count':len(rows),'expectations':len(index['expected'])}))
