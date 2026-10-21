from pathlib import Path
import json,hashlib,zipfile,math,argparse
from fractions import Fraction as F
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';O=P/'c30_source';O.mkdir(exist_ok=False);H=lambda b:hashlib.sha256(b).hexdigest();arc=R/'captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
assert H(arc.read_bytes())=='d80fc253a77b59b72a387a0db63eb5a60563c2d1f7563e12f9570172d69e087b'
with zipfile.ZipFile(arc)as z:
 raw=z.read('sources/COMPLEX_AND_ACTION.json');assert H(raw)=='1e8a15425fa80e5d500370a51a1b7c8605dfab5befe61824d47c07ec8fb35575';j=json.loads(raw)
 rawm=z.read('modular_results.json');assert H(rawm)=='e7955b36d396b77ab35a97d02af8e1badac6ac031181653dfac682b248647ee5';m=json.loads(rawm)
s=[list(map(tuple,t))for t in j['simplices']];assert list(map(len,s))==[120,720,1200,600];assert all(t==sorted(t)and all(tuple(sorted(v))==v for v in t)for t in s);off=[0,120,840,2040];J=[0,9,227,432,447,582,538,347,332,141];edges=[];B=[]
for k in range(1,4):
 idx={v:i for i,v in enumerate(s[k-1])};bk={}
 for col,v in enumerate(s[k]):
  for r in range(k+1):
   row=idx[v[:r]+v[r+1:]];sign=(-1)**r;w=3 if k==3 and col in J else 2
   edges.append((off[k-1]+row,off[k]+col,-sign*w));edges.append((off[k]+col,off[k-1]+row,sign*w));bk[row,col]=sign
 B.append(bk)
# Exact chain-square products and source bounds, independent of cached K.
for k in [0,1]:
 accum={};right=B[k+1];left=B[k]
 by={}
 for(i,t),v in left.items():by.setdefault(t,[]).append((i,v))
 for(t,col),w in right.items():
  for i,v in by[t]:accum[i,col]=accum.get((i,col),0)+v*w
 assert all(v==0 for v in accum.values())
E={(i,j):w for i,j,w in edges};assert len(E)==len(edges)==14880 and all(E[j,i]==-w for(i,j),w in E.items());rows=[0]*2640
for i,j,w in edges:rows[i]+=abs(w)
assert max(rows)==24
obs=m['observed_indices'];assert len(obs)==len(set(obs))==62
expected=[off[k]+s[k].index(tuple(v))for k in range(3)for v in m['link_simplices'][k]];assert obs==expected
text='2640 62 4096 40 128\n'+' '.join(map(str,obs))+'\n'+str(len(edges))+'\n'+''.join(f'{i} {j} {w}\n'for i,j,w in edges)
(O/'OPERATOR.txt').write_text(text)
tau=F(5,2)**41/F(math.factorial(41))/(1-F(5,84));u=F(52,2**128);r=F(40*13)*u # Sum of propagated rounding errors<40e^(5/2)u<520u.
# All local states<=2^18, so local halfstep error<=tau*2^18+r.
e=tau*2**18+r;glob=4096*e;forward=glob+F(504,2**96);adj=glob+F(52,2**96)
assert tau<F(1,2**109) and glob<F(1,2**77) and forward<F(1,2**68) and adj<F(1,2**68)
# Ideal adjoint Horner prefixes have norm<=sum ||y_j||/64<=||y||<=2049; not64||y||.
# Propagating scaled injections is exact at128bits since data have96bits and /64 uses6.
assert F(2049)+glob<2**18
# Forward data error norm <=maximum state trajectory error: sqrt4096/64=1.
result={'status':'PASS_EXACT_SOURCE_AND_ACTION_ERROR_CONSTANTS','state_dimension':2640,'data_dimension':253952,'channels':62,'samples':4096,'halfstep_Taylor_degree':40,'internal_dyadic_bits':128,'input_output_dyadic_bits':96,'H_nonzero_entries':len(edges),'H_max_absolute_row_sum':max(rows),'halfstep_generator':'H/4=K/2','tau':str(tau),'tau_bound':'<2^-109','rounding_halfstep_error_bound':str(r),'uniform_state_cap':2**18,'accumulated_state_error_bound':str(glob),'forward_error_upper':str(forward),'adjoint_error_upper':str(adj),'forward_error_gate':'<2^-68 absolute on state ball2048','adjoint_error_gate':'<2^-68 absolute on data ball2049','source_operator_sha256':H(text.encode()),'physical_promotion':0,'external_promotion_review':'PENDING'}
(O/'ACTION_CONSTANTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
(O/'SOURCE_BINDINGS.json').write_text(json.dumps({'archive_sha256':H(arc.read_bytes()),'complex_member_sha256':H(raw),'observer_member_sha256':H(rawm),'weights_J':J,'selected_weight':'3/2','operator_sha256':H(text.encode()),'parent_decoder_capture':'2026-10-21T011432Z-codex-finite-decoder-cde7ea74','archived_executable_invocations':0},indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2))
