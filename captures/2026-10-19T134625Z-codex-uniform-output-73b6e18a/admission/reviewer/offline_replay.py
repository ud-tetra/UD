"""Offline, hash-pinned constructor replay runner; never self-attests independence."""
import argparse,datetime,hashlib,json,os,shutil,stat,subprocess,sys,zipfile
from pathlib import Path,PurePosixPath
CAPS={
 'rounding':('2026-10-19T132221Z-codex-rounding-replay-82e4a9b7','cd8b68fc18572031cd0818ef78e9a189bab22d4d06fab89a1a33adae95d5aa52','rounding-replay-work'),
 'contract':('2026-10-18T200728Z-codex-record-contract-5b1e8a94','2abff70a6412770971dfecd214e1a4d51b53af44876f2eadd12271f785cd1480','record-contract-work'),
 'generator':('2026-10-18T172041Z-codex-floating-timing-2f6a91ce','5b814cbfe38155f356854b962493aad4bb95982a31cdef66c5a4027005ceb461','floating-timing-work'),
 'cyclic':('2026-10-18T192301Z-codex-uniform-two-step-8a71c9d3','50254410652197465e3e121ac55b35b7f19e6798d4bfedc452a121433a00ce0d','uniform-two-work'),
 'dense':('2026-10-18T184202Z-codex-two-step-noise-c54b7a12','9edbaef931c33f28f30a147591ee0ef9eaacb27c36b8d85cb6edb9d2f52bf945','two-step-noise-work')}
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def safe_name(name):
 if not isinstance(name,str) or not name or '\\' in name or '\x00' in name:raise ValueError('unsafe member name')
 v=PurePosixPath(name)
 if v.is_absolute() or any(x in ('','.','..') for x in name.rstrip('/').split('/')) or ':' in name:raise ValueError('unsafe member path')
 return v

def archive_plan(paths):
 """Validate all members of all ZIPs before writing anything."""
 seen=set();plan=[];total=0
 for path in paths:
  with zipfile.ZipFile(path) as z:
   for i in z.infolist():
    r=safe_name(i.filename);key=str(r)
    if key in seen:raise ValueError('duplicate archive member')
    seen.add(key);kind=stat.S_IFMT(i.external_attr>>16)
    if kind not in (0,stat.S_IFREG,stat.S_IFDIR) or i.flag_bits&1:raise ValueError('unsupported file type/encryption')
    if i.is_dir() and kind==stat.S_IFREG:raise ValueError('inconsistent directory')
    if i.file_size>256*1024**2:raise ValueError('member size limit')
    total+=i.file_size
    if total>2*1024**3:raise ValueError('archive expansion limit')
    plan.append((Path(path),i.filename,key,i.is_dir(),i.file_size))
 return plan

def extract(paths,dest):
 plan=archive_plan(paths);dest=Path(dest);dest.mkdir(exist_ok=False,parents=True)
 for path,name,key,isdir,size in plan:
  target=dest/key
  if isdir:target.mkdir(parents=True,exist_ok=True);continue
  target.parent.mkdir(parents=True,exist_ok=True)
  with zipfile.ZipFile(path) as z,z.open(name) as source,target.open('xb') as out:shutil.copyfileobj(source,out)
  if target.stat().st_size!=size:raise ValueError('member size mismatch')
 return {'archive_count':len(paths),'unique_members':len(plan),'uncompressed_bytes':sum(x[4] for x in plan)}

def intake(repo,key,out):
 cap,digest,folder=CAPS[key];root=repo/'captures'/cap;m=root/'MANIFEST.json'
 if m.is_symlink() or sha(m)!=digest:raise ValueError('pinned root manifest mismatch')
 doc=json.loads(m.read_text());archives=[];files=[]
 for e in doc['files']:
  rel=safe_name(e['path']);prefix=PurePosixPath('captures')/cap
  if not rel.is_relative_to(prefix):raise ValueError('manifest leaves capture')
  q=repo/str(rel)
  if q.is_symlink() or not q.resolve().is_relative_to(root.resolve()) or q.stat().st_size!=e['size_bytes'] or sha(q)!=e['sha256']:raise ValueError('root manifest byte mismatch')
  files.append({'path':str(rel),'sha256':e['sha256'],'size_bytes':e['size_bytes']})
  if q.suffix=='.zip':archives.append(q)
 if not archives:raise ValueError('no retained archives')
 dest=out/folder;summary=extract(sorted(archives),dest)
 return dest,{'capture':cap,'root_manifest_sha256':digest,'files':files,**summary}

def run_command(cwd,args,out,tag,commands):
 log=out/(tag+'.log');cmd=[sys.executable,*args]
 with log.open('xb') as stream:r=subprocess.run(cmd,cwd=cwd,stdout=stream,stderr=subprocess.STDOUT,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
 commands.append({'tag':tag,'cwd_relative_to_output':str(Path(cwd).relative_to(out)),'argv':cmd,'returncode':r.returncode,'log':log.name,'log_sha256':sha(log)})
 if r.returncode:raise RuntimeError('replay command failed: '+tag)

def dense_restore(base,dest,package):
 import numpy as np
 f=json.loads((package/'NOISE_FREEZE.json').read_text());d=json.loads((package/'DATA_FREEZE.json').read_text());row=next(x for x in d['records'] if x['case']=='dense_a0')
 if f['seeds']['dense_sign']!=218209 or sha(base)!=f['baseline_sha256']:raise ValueError('dense recipe/source mismatch')
 pattern=np.random.default_rng(218209).integers(0,2,size=(37,8191,62),dtype=np.int64)*2-1;Y=np.memmap(base,dtype='<i8',mode='r',shape=pattern.shape);dest.parent.mkdir(parents=True,exist_ok=True)
 with dest.open('xb') as s:s.truncate(150321232)
 Z=np.memmap(dest,dtype='<i8',mode='r+',shape=pattern.shape);Z[:]=Y+pattern;Z.flush();del Z
 Z=np.memmap(dest,dtype='<i8',mode='r',shape=pattern.shape);count=0
 for k in range(0,8191,256):
  diff=Z[:,k:k+256]-Y[:,k:k+256]
  if not np.array_equal(diff,pattern[:,k:k+256]) or not np.all(np.sum(diff*diff,axis=-1)==62):raise ValueError('dense raw difference mismatch')
  count+=diff.size
 if count!=18790154 or sha(dest)!=row['record_sha256']:raise ValueError('dense full hash mismatch')
 return {'case':'dense_a0','bytes':dest.stat().st_size,'sha256':sha(dest),'scalar_differences_checked':count,'vector_integer_squared_error_max':62}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);g=p.add_mutually_exclusive_group();g.add_argument('--witness',action='store_true');g.add_argument('--raw',action='store_true');a=p.parse_args();repo=a.repo.resolve();out=a.out.absolute()
 if out.exists():p.error('--out must name a NEW nonexistent directory')
 out.mkdir(parents=True,exist_ok=False);commands=[];inputs=[];work={};receipt={'status':'RUNNING','reviewer_identity':None,'external_nonconstructor_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry','mode':'raw' if a.raw else 'witness','runner_sha256':sha(__file__),'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commands':commands,'intake':inputs,'new_estimator_runs':0,'new_SVD_runs':0}
 try:
  for key in ['rounding','contract']+(['generator','cyclic','dense'] if a.raw else []):work[key],x=intake(repo,key,out);inputs.append(x)
  for key in ['rounding','contract']:run_command(work[key],['replay_entry.py'],out,key+'-witness',commands)
  if a.raw:
   generated=out/'generated-PR195-records';run_command(work['generator'],['make_records.py','--destination',str(generated)],out,'PR195-raw-generation',commands)
   original=json.loads((work['generator']/'DATA_FREEZE.json').read_text());fresh=json.loads((generated/'RAW_REGENERATION_RECEIPT.json').read_text())
   if original['records']!=fresh['records'] or len(fresh['records'])!=4:raise ValueError('PR195 generation rows mismatch')
   for row in fresh['records']:
    q=generated/(row['case']+'.i64le')
    if q.stat().st_size!=150321232 or sha(q)!=row['record_sha256']:raise ValueError('PR195 raw source mismatch')
   base=work['generator']/'records/ramp_clock_stress.i64le';base.parent.mkdir(exist_ok=True);os.link(generated/base.name,base)
   cyclic=work['cyclic']/'records/cyclic_unit.i64le';run_command(work['cyclic'],['make_record.py','--regenerate',str(cyclic)],out,'PR201-cyclic-generation',commands)
   receipt['dense_reconstruction']=dense_restore(base,work['dense']/'records/dense_a0.i64le',work['dense'])
   clone=out/'record-contract-raw-replay';shutil.copytree(work['contract'],clone,ignore=shutil.ignore_patterns('__pycache__','RAW_REPLAY.json','PROJECTION_REPLAY.json'))
   run_command(clone,['project.py','--raw-replay'],out,'PR204-complete-raw-replay',commands)
   for name in ['baseline','cyclic_unit','dense_unit']:
    q=json.loads((clone/'results'/name/'RAW_REPLAY.json').read_text());want=62 if name=='dense_unit' else int(name=='cyclic_unit')
    if q['readings_checked']!=18790154 or q['max_vector_integer_squared_error']!=want:raise ValueError('PR204 raw receipt mismatch')
   run_command(work['rounding'],['raw_verify.py'],out,'PR208-complete-projection-replay',commands)
   q=json.loads((work['rounding']/'RAW_PROJECTION_REPLAY.json').read_text())
   if q['readings_checked']!=18790154 or q['integer_projection_entries_checked']!=2629311:raise ValueError('PR208 raw receipt mismatch')
  receipt['status']='PASS_CONSTRUCTOR_REPLAY_ONLY';receipt['scope']='Saved witness checks plus raw reconstruction/projection' if a.raw else 'Saved witness checks only; no raw reconstruction'
 except Exception as e:
  receipt['status']='FAIL';receipt['error']=type(e).__name__+': '+str(e);raise
 finally:
  receipt['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();(out/'RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
 print(json.dumps({'status':receipt['status'],'external_nonconstructor_review':'PENDING','receipt':str(out/'RUN_RECEIPT.json'),'mode':receipt['mode']}))
if __name__=='__main__':main()
