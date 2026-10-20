"""Reviewer-controlled small identity fixtures; no acquisition or large copies."""
from pathlib import Path
import hashlib,json,os
import numpy as np
from oracle import canonical_fraction
P=Path(__file__).resolve().parent;D=P/'fixtures'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,j):p.write_text(json.dumps(j,indent=2,sort_keys=True)+'\n')
def main():
 D.mkdir(exist_ok=False);A=[[2,-4],[0,6]];base=canonical_fraction(A,1);zero=canonical_fraction([[0,0,0]],0)
 catalog={'schema_version':'1.0','identity_format':'UD_DYADIC_MATRIX_V1','coverage':'Controlled synthetic two-fingerprint review catalog; no acquisition assertions','records':[{'record_id':'A','fingerprint_sha256':base['fingerprint'],'source_reference':'review_fixture_A'},{'record_id':'zero','fingerprint_sha256':zero['fingerprint'],'source_reference':'review_zero_fixture'}]};write(D/'known.json',catalog);rows=[]
 def positive(name,N,b,order='C',known='known.json',matches=None):
  array=np.array(N,dtype='<i8',order=order);file=D/(name+'.npy');np.save(file,array,allow_pickle=False);expected=canonical_fraction(array.tolist(),b);cat=json.loads((D/known).read_text());match=[r['record_id']for r in cat['records']if r['fingerprint_sha256']==expected['fingerprint']]
  rows.append({'case':name,'record':str(file.relative_to(P)),'bits':str(b),'known':str((D/known).relative_to(P)),'expected':'VALID','expected_fingerprint':expected['fingerprint'],'expected_bbar':expected['bbar'],'expected_removed':b-expected['bbar'],'expected_all_zero':not any(x for row in array.tolist()for x in row),'expected_shape':list(array.shape),'expected_matches':match,'expected_relation':'LISTED_FINGERPRINT'if match else'UNLISTED_FINGERPRINT'})
 def negative(name,N=None,b='1',known='known.json',dtype='<i8',expected='INTAKE'):
  file=D/(name+'.npy');np.save(file,np.array(A if N is None else N,dtype=dtype),allow_pickle=True);rows.append({'case':name,'record':str(file.relative_to(P)),'bits':str(b),'known':str((D/known).relative_to(P)),'expected':expected})
 positive('base_C',A,1);positive('base_Fortran',A,1,'F');positive('scaled_alias',[[4,-8],[0,12]],2);positive('reduced_alias',[[1,-2],[0,3]],0)
 positive('denominator_only_change',A,2);positive('integer_even_saturation',A,0);positive('one_entry_change',[[3,-4],[0,6]],1);positive('negative_matrix',[[-2,4],[0,-6]],1);positive('different_shape',[[2,-4,0,6]],1)
 positive('zero_b0',[[0,0,0]],0);positive('zero_b256',[[0,0,0]],256);positive('zero_other_shape',[[0,0],[0,0]],0)
 positive('INT64_MIN_b63',[[-2**63]],63);positive('minus_one_b0',[[-1]],0);positive('INT64_MIN_b256',[[-2**63]],256);positive('INT64_MIN_b64',[[-2**63]],64);positive('minus_one_b1',[[-1]],1)
 positive('INT64_MIN_and_odd',[[-2**63,1]],64);positive('negative_even_pair',[[-8,-4]],4);positive('positive_even_pair',[[8,4]],4)
 replica=json.loads(json.dumps(catalog));replica['records'].insert(1,{'record_id':'A_replica','fingerprint_sha256':base['fingerprint'],'source_reference':'may_be_an_independent_replication_not_decided_by_this_screen'});write(D/'known_duplicate_fingerprint.json',replica);positive('duplicate_fingerprint_allowed',A,1,known='known_duplicate_fingerprint.json')
 empty=dict(catalog);empty['records']=[];empty['coverage']='Empty controlled catalog; unlisted means no acquisition verdict';write(D/'known_empty.json',empty);positive('empty_catalog_unlisted',A,1,known='known_empty.json')
 negative('float_dtype',dtype='<f8');negative('int32_dtype',dtype='<i4');negative('object_dtype',dtype=object);negative('vector_not_matrix',N=[1,2]);negative('empty_dimension',N=[[]]);negative('negative_bits',b=-1);negative('above_profile_bits',b=257);negative('invalid_bits_syntax',b='True',expected='ARGUMENT_ERROR')
 def badcatalog(name,change):
  obj=json.loads(json.dumps(catalog));change(obj);write(D/(name+'.json'),obj);negative(name,known=name+'.json')
 badcatalog('catalog_duplicate_ID',lambda j:j['records'].__setitem__(1,dict(j['records'][1],record_id='A')))
 badcatalog('catalog_bad_digest',lambda j:j['records'][0].__setitem__('fingerprint_sha256','X'*64))
 badcatalog('catalog_bad_ID',lambda j:j['records'][0].__setitem__('record_id','bad id'))
 badcatalog('catalog_unknown_claim',lambda j:j.__setitem__('fresh_preparation',True))
 badcatalog('catalog_empty_coverage',lambda j:j.__setitem__('coverage',''))
 badcatalog('catalog_empty_source',lambda j:j['records'][0].__setitem__('source_reference',''))
 # Preserve a repeated JSON key directly rather than serializing through a dict.
 (D/'catalog_duplicate_JSON.json').write_text(json.dumps(catalog)[:-1]+',"coverage":"duplicate"}')
 negative('catalog_duplicate_JSON',known='catalog_duplicate_JSON.json')
 for name,shape in [('oversize_rows',(8192,1)),('oversize_columns',(1,322)),('truncated_payload',(2,2))]:
  h=repr({'descr':'<i8','fortran_order':False,'shape':shape}).encode();pad=(64-(10+len(h)+1)%64)%64;h+=b' '*pad+b'\n';file=D/(name+'.npy');file.write_bytes(b'\x93NUMPY'+bytes([1,0])+len(h).to_bytes(2,'little')+h);rows.append({'case':name,'record':str(file.relative_to(P)),'bits':'1','known':str((D/'known.json').relative_to(P)),'expected':'INTAKE'})
 (D/'link.npy').symlink_to('base_C.npy');rows.append({'case':'symlink_record','record':str((D/'link.npy').relative_to(P)),'bits':'1','known':str((D/'known.json').relative_to(P)),'expected':'INTAKE'})
 (D/'real').mkdir();np.save(D/'real'/'N.npy',np.array(A,dtype='<i8'),allow_pickle=False);(D/'linkdir').symlink_to('real',target_is_directory=True);rows.append({'case':'symlink_record_ancestor','record':str((D/'linkdir/N.npy').relative_to(P)),'bits':'1','known':str((D/'known.json').relative_to(P)),'expected':'INTAKE'})
 (D/'known_link.json').symlink_to('known.json');negative('symlink_catalog',known='known_link.json')
 for name in ['existing_output_sentinel','output_is_record_file','output_is_input_directory']:negative(name,expected='OUTPUT_REJECTION')
 rows.append({'case':'missing_record','record':str((D/'absent.npy').relative_to(P)),'bits':'1','known':str((D/'known.json').relative_to(P)),'expected':'INTAKE'})
 write(P/'FIXTURES.json',{'status':'BUILT_CONTROLLED_IDENTITY_FIXTURES','cases':rows,'count':len(rows),'new_acquisitions':0,'large_record_copies':0,'physical_promotion':0})
 frozen=[]
 for p in sorted(D.rglob('*')):
  if p.is_symlink():frozen.append({'path':str(p.relative_to(P)),'symlink_target':os.readlink(p)})
  elif p.is_file():frozen.append({'path':str(p.relative_to(P)),'sha256':sha(p),'bytes':p.stat().st_size})
 write(P/'FIXTURE_FREEZE.json',{'status':'FROZEN_BEFORE_REVIEWER_SCREEN_EXECUTION','generator_sha256':sha(P/'build_fixtures.py'),'fixture_index_sha256':sha(P/'FIXTURES.json'),'rows':frozen,'physical_promotion':0})
 print(json.dumps({'cases':len(rows),'frozen_entries':len(frozen)}))
if __name__=='__main__':main()
