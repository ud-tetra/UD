"""Small reviewer-controlled fixtures; no estimator/model or actual factors."""
from pathlib import Path
import copy,hashlib,io,json,zipfile
import numpy as np
P=Path(__file__).resolve().parent;BASE=P/'fixtures'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write_json(p,j):p.write_text(json.dumps(j,indent=2,sort_keys=True)+'\n')
def build(name,N,s,Vt,U,bZ=0,expected='CERTIFIED',expected_bounds=None):
 d=BASE/name;d.mkdir(parents=True,exist_ok=False)
 np.save(d/'N.npy',np.asarray(N),allow_pickle=False)
 np.savez_compressed(d/'SVD_META.npz',singular=np.asarray(s),right_transpose=np.asarray(Vt))
 chunks=[]
 for start,row in enumerate(np.asarray(U)):
  file='U_'+str(start)+'.npz';np.savez_compressed(d/file,basis=np.asarray([row]));chunks.append({'path':file,'sha256':sha(d/file),'start':start,'stop':start+1})
 j={'schema_version':'1.0','record':{'path':'N.npy','sha256':sha(d/'N.npy'),'payload_sha256':hashlib.sha256(np.asarray(N).astype(np.asarray(N).dtype.newbyteorder('<')).tobytes()).hexdigest(),'dyadic_exponent':bZ},'svd':{'path':'SVD_META.npz','sha256':sha(d/'SVD_META.npz')},'left_chunks':chunks}
 write_json(d/'manifest.json',j)
 return {'case':name,'manifest':str((d/'manifest.json').relative_to(P)),'expected':expected,'expected_bounds':expected_bounds or {}}
def mutate(name,change,expected='INTAKE_HOLD'):
 N=np.array([[2,0],[0,0]],dtype='<i8');s=np.array([2.,0.]);V=np.eye(2);U=np.array([[1.],[0.]])
 row=build(name,N,s,V,U,expected=expected);d=BASE/name;j=json.loads((d/'manifest.json').read_text());change(d,j);write_json(d/'manifest.json',j);return row
def svd(d,j,s=None,V=None):
 with np.load(d/'SVD_META.npz',allow_pickle=False)as z:
  old_s=z['singular'];old_v=z['right_transpose']
 np.savez_compressed(d/'SVD_META.npz',singular=old_s if s is None else s,right_transpose=old_v if V is None else V);j['svd']['sha256']=sha(d/'SVD_META.npz')
def Nfile(d,j,x):
 np.save(d/'N.npy',x,allow_pickle=False);j['record']['sha256']=sha(d/'N.npy');j['record']['payload_sha256']=hashlib.sha256(np.asarray(x).tobytes()).hexdigest()
def chunk(d,j,index,x):
 f=d/j['left_chunks'][index]['path'];np.savez_compressed(f,basis=x);j['left_chunks'][index]['sha256']=sha(f)
def malformed_header(d,j):
 h=repr({'descr':'<f8','fortran_order':False,'shape':(10**9,)}).encode();padding=(64-((10+len(h)+1)%64))%64;h+=b' '*padding+b'\n';npy=b'\x93NUMPY'+bytes([1,0])+len(h).to_bytes(2,'little')+h
 valid=io.BytesIO();np.save(valid,np.eye(2),allow_pickle=False)
 with zipfile.ZipFile(d/'SVD_META.npz','w',compression=zipfile.ZIP_DEFLATED)as z:z.writestr('singular.npy',npy);z.writestr('right_transpose.npy',valid.getvalue())
 j['svd']['sha256']=sha(d/'SVD_META.npz')
def main():
 BASE.mkdir(exist_ok=False);rows=[]
 n=np.array([[2,0],[0,0]],dtype='<i8');s=np.array([2.,0.]);v=np.eye(2);u=np.array([[1.],[0.]])
 rows.append(build('exact_q1',n,s,v,u,expected_bounds={'full_error':[0,1],'condition':[1,1]}))
 rows.append(build('exact_q2',np.diag([4,2,0]).astype('<i8'),np.array([4.,2.,0.]),np.eye(3),np.array([[1.,0.],[0.,1.],[0.,0.]]),expected_bounds={'full_error':[0,1],'condition':[2,1]}))
 rows.append(build('small_tail',np.diag([2**49,1]).astype('<i8'),s,v,u,bZ=48,expected_bounds={'full_error':[1,2**48],'condition':[1,1]}))
 rows.append(build('small_retained_residual',np.diag([2**49+1,0]).astype('<i8'),s,v,u,bZ=48,expected_bounds={'full_error':[1,2**47]}))
 rows.append(build('int64_min',np.array([[-2**63,0],[0,0]],dtype='<i8'),np.array([float(2**63),0.]),v,-u,expected_bounds={'full_error':[0,1],'condition':[1,1]}))
 rows.append(build('large_tail',np.diag([2,1]).astype('<i8'),s,v,u,expected='NUMERICAL_HOLD'))
 rows.append(build('zero_record_wrong_spectrum',np.zeros((2,2),dtype='<i8'),s,v,u,expected='NUMERICAL_HOLD'))
 rows.append(mutate('record_hash_mismatch',lambda d,j:j['record'].__setitem__('sha256','0'*64)))
 rows.append(mutate('payload_hash_mismatch',lambda d,j:j['record'].__setitem__('payload_sha256','0'*64)))
 rows.append(mutate('wrong_N_float_dtype',lambda d,j:Nfile(d,j,n.astype(np.float64))))
 rows.append(mutate('wrong_N_vector_shape',lambda d,j:Nfile(d,j,np.array([2,0],dtype='<i8'))))
 rows.append(mutate('factor_NaN',lambda d,j:svd(d,j,V=np.array([[float('nan'),0.],[0.,1.]]))))
 rows.append(mutate('singular_Inf',lambda d,j:svd(d,j,s=np.array([float('inf'),0.]))))
 rows.append(mutate('singular_unsorted',lambda d,j:svd(d,j,s=np.array([0.,2.]))))
 rows.append(mutate('singular_negative',lambda d,j:svd(d,j,s=np.array([2.,-1.]))))
 rows.append(mutate('singular_exact_cutoff_tie',lambda d,j:svd(d,j,s=np.array([2.,2.**-24]))))
 rows.append(mutate('q_zero',lambda d,j:svd(d,j,s=np.array([0.,0.]))))
 rows.append(mutate('q_equals_n',lambda d,j:svd(d,j,s=np.array([2.,1.]))))
 rows.append(mutate('right_wrong_shape',lambda d,j:svd(d,j,V=np.ones((1,2)))))
 rows.append(mutate('right_complex_dtype',lambda d,j:svd(d,j,V=np.eye(2,dtype=np.complex128))))
 rows.append(mutate('right_object_dtype',lambda d,j:svd(d,j,V=np.array([['1','0'],['0','1']],dtype=object))))
 rows.append(mutate('U_wrong_columns',lambda d,j:chunk(d,j,0,np.array([[1.,0.]]))))
 rows.append(mutate('U_wrong_declared_extent',lambda d,j:j['left_chunks'][0].__setitem__('stop',2)))
 rows.append(mutate('U_overlap',lambda d,j:j['left_chunks'][1].__setitem__('start',0)))
 rows.append(mutate('U_gap',lambda d,j:j['left_chunks'][1].__setitem__('start',2)))
 rows.append(mutate('U_boolean_extent',lambda d,j:j['left_chunks'][0].__setitem__('start',False)))
 rows.append(mutate('negative_denominator_exponent',lambda d,j:j['record'].__setitem__('dyadic_exponent',-1)))
 rows.append(mutate('boolean_denominator_exponent',lambda d,j:j['record'].__setitem__('dyadic_exponent',False)))
 rows.append(mutate('missing_manifest_field',lambda d,j:j.pop('svd')))
 rows.append(mutate('unknown_claim_field',lambda d,j:j.__setitem__('certified',True)))
 rows.append(mutate('truncated_oversized_header',malformed_header))
 def escape(d,j):
  target=d.parent/'controlled_escape.npy';target.write_bytes((d/'N.npy').read_bytes());j['record']['path']='../controlled_escape.npy';j['record']['sha256']=sha(target)
 rows.append(mutate('relative_path_escape',escape))
 def symfile(d,j):
  (d/'link_N.npy').symlink_to('N.npy');j['record']['path']='link_N.npy'
 rows.append(mutate('symlink_input_file',symfile))
 def symparent(d,j):
  (d/'real').mkdir();(d/'real'/'N.npy').write_bytes((d/'N.npy').read_bytes());(d/'link').symlink_to('real',target_is_directory=True);j['record']['path']='link/N.npy'
 rows.append(mutate('symlink_input_ancestor',symparent))
 # Output-path attacks use valid inputs, and will be configured by the driver.
 rows.append(mutate('existing_output_sentinel',lambda d,j:None,expected='OUTPUT_REJECTION'))
 rows.append(mutate('output_is_input_directory',lambda d,j:None,expected='OUTPUT_REJECTION'))
 rows.append(mutate('output_is_input_file',lambda d,j:None,expected='OUTPUT_REJECTION'))
 rows.append(mutate('wrong_U_numerical',lambda d,j:chunk(d,j,0,np.array([[0.]])),expected='NUMERICAL_HOLD'))
 j={'status':'BUILT_SMALL_EXACT_REVIEW_FIXTURES','cases':rows,'count':len(rows),'new_fits':0,'actual_saved_inputs_copied':False,'physical_promotion':0}
 write_json(P/'FIXTURES.json',j);print(json.dumps({'status':j['status'],'count':len(rows)}))
if __name__=='__main__':main()
