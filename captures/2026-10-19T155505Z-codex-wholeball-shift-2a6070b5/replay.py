"""Clean exact-bound and normal-equation replay; parent arrays are hash-pinned inputs."""
import sys
sys.dont_write_bytecode=True
import json,argparse,subprocess,os,datetime
from pathlib import Path
from bounds import P,sha,freeze
from offline_intake import extract,safe_name
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args();f=freeze();rf=json.loads((P/'REPLAY_FREEZE.json').read_text());assert sha(__file__)==rf['code_sha256'];out=args.out.absolute();assert not out.exists();out.mkdir(parents=True)
 receipt={'status':'RUNNING','commands':[],'reviewer_identity':None,'external_review':'PENDING','physical_promotion':0,'new_SVD_fits_raw_generation':0,'scope':'Pinnedparentarraybytes plusnewsourcebound/exactnormal/Pythagorascontrols; no newparentfullfactororrawprojectionexecution.'}
 def go(cmd,tag):
  r=subprocess.run([sys.executable,*cmd],cwd=P,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1'});q=out/(tag+'.log');q.write_bytes(r.stdout);receipt['commands'].append({'tag':tag,'argv':cmd,'exit_code':r.returncode,'log_sha256':sha(q)});assert r.returncode==0 and r.stdout.strip(),tag
 try:
  root=args.repo.resolve()/'captures'/f['evidence_capture']['id'];m=root/'MANIFEST.json';assert sha(m)==f['evidence_capture']['manifest_sha256'];archives=[]
  for row in json.loads(m.read_text())['files']:
   rel=safe_name(row['path']);assert Path(str(rel)).is_relative_to(Path('captures')/root.name);q=args.repo.resolve()/str(rel)
   assert not q.is_symlink() and q.resolve().is_relative_to(root.resolve()) and q.stat().st_size==row['size_bytes'] and sha(q)==row['sha256']
   if q.suffix=='.zip':archives.append(q)
  assert len(archives)==10;receipt['intake']=extract(sorted(archives),out/'evidence')
  go(['bounds.py','--replay'],'apriori-bounds');go(['normal.py','--evidence',str(out/'evidence'),'--replay'],'exact-normal-equations');go(['controls.py'],'exact-controls')
  freeze();receipt.update(status='PASS_CLEAN_APRIORI_NORMAL_AND_CONTROL_REPLAY',normal_cases=3,bound_rows=12,controls=4)
 except Exception as e:receipt.update(status='FAIL',error=type(e).__name__+': '+str(e));raise
 finally:(out/'REPLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
 print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
