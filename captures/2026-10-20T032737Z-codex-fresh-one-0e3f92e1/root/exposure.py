"""Bounded pre-fit exposure check, committed public UD text metadata only."""
from pathlib import Path
import argparse,hashlib,json,subprocess
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check(repo,token,base):
 if type(token)is not str or len(token)!=64 or any(c not in '0123456789abcdef'for c in token):raise ValueError('record digest required')
 run=subprocess.run(['git','grep','-n','-I','-F',token,base,'--','*.json','*.md','*.py'],cwd=repo,text=True,capture_output=True)
 if run.returncode not in(0,1):raise RuntimeError('metadata scan failed')
 hits=run.stdout.splitlines()
 return {'status':'HOLD_RECORD_DIGEST_ALREADY_LOCATED_IN_CHECKED_METADATA'if hits else 'NO_RECORD_DIGEST_MATCH_IN_CHECKED_COMMITTED_TEXT','base_commit':base,'record_sha256':token,'matching_lines':hits,'scope':'Committed JSON/Markdown/Python metadata at this pinned UD main only; no unmerged branches, unexported chats/private sources or global absence claim','blind_or_independent_physical_freshness_claimed':False}
def main():
 a=argparse.ArgumentParser();a.add_argument('--repo',required=True);a.add_argument('--data-freeze',required=True);a.add_argument('--out',required=True);v=a.parse_args();f=json.loads((P/'FREEZE.json').read_text());assert sha(P/'exposure.py')==f['code_sha256'];data=json.loads(Path(v.data_freeze).read_text());row=data['record'];assert row['case']==f['candidate_case'];result=check(Path(v.repo),row['record_sha256'],f['base_commit']);result.update(data_freeze_sha256=sha(v.data_freeze),root_recipe_selector='Negate oldtop1 alternating onequantum perturbation; exposed baseline/selector/targets disclosed; no outcome-dependent replacement',new_estimator_calls=0,physical_promotion=0);out=Path(v.out);assert not out.exists()
 with out.open('x')as stream:json.dump(result,stream,indent=2);stream.write('\n')
 print(json.dumps({'status':result['status'],'matching_lines':len(result['matching_lines'])}))
if __name__=='__main__':main()
