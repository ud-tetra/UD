"""Replay pinned descriptive raw analysis with unchanged frozen checker; never acquire data."""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parent
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def need(v,msg):
 if not v:raise ValueError(msg)
def output_guard(out,package):
 package=Path(package).resolve();out=Path(out).resolve()
 protected=next((q for q in [package,*package.parents] if (q/'MANIFEST.json').is_file()),package)
 need(not out.is_relative_to(protected) and not protected.is_relative_to(out),'OUTPUT_MUST_BE_EXTERNAL_TO_IMMUTABLE_CAPTURE_OR_PACKAGE')
 return protected
def main():
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True,type=Path);a.add_argument('--raw',required=True,type=Path);a.add_argument('--out',required=True,type=Path);x=a.parse_args()
 repo=x.repo.resolve();raw=x.raw.resolve();out=x.out.resolve()
 need(not out.exists() and not x.out.is_symlink(),'NEW_OUTPUT_DIRECTORY_REQUIRED')
 output_guard(out,P)
 f=json.loads((P/'REPLAY_FREEZE_v0.2.json').read_text())
 for n,h in f['files'].items():need(sha(P/n)==h,'PACKAGE_HASH_MISMATCH:'+n)
 e=json.loads((P/'EXECUTION_FREEZE.json').read_text())
 for n,h in e['source_files'].items():need(sha(repo/n)==h,'REPOSITORY_DEPENDENCY_HASH_MISMATCH:'+n)
 need(raw.is_file() and raw.stat().st_size==e['raw']['size_bytes'] and sha(raw)==e['raw']['sha256'],'RAW_IDENTITY_MISMATCH')
 out.mkdir(parents=True,exist_ok=False)
 r=subprocess.run([sys.executable,str(P/'reference_checker_v2.py'),'--raw',str(raw),'--output',str(out/'COMPONENT_RESULT.json')],text=True,capture_output=True)
 (out/'stdout.log').write_text(r.stdout);(out/'stderr.log').write_text(r.stderr)
 need(r.returncode==0,'CHECKER_PROCESS_FAILURE');need(sha(raw)==e['raw']['sha256'],'RAW_CHANGED')
 need(sha(out/'COMPONENT_RESULT.json')==sha(P/'COMPONENT_RESULT.json'),'SCIENTIFIC_JSON_NOT_BYTE_IDENTICAL')
 for n,h in f['files'].items():need(sha(P/n)==h,'PACKAGE_CHANGED:'+n)
 result={'status':'PASS_PINNED_RAW_REPLAY_BYTE_IDENTICAL','raw_sha256':e['raw']['sha256'],'result_sha256':sha(out/'COMPONENT_RESULT.json'),'raw_executions_this_replay':1,'native_estimator_fits':0,'physical_promotion':0,'scope':'Descriptive nominal-unit raw replay, not interval numerical or calibrated physical certificate'}
 (out/'REPLAY_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
