"""Prospective nextafter boundary addendum; no actual factors or estimator."""
import argparse,json,os
from pathlib import Path
import numpy as np
from common import P,freeze,sha,need,guard,write_new
import exact_math as e

def run():
 freeze();f=json.loads((P/'RANK_BOUNDARY_FREEZE.json').read_text());need(sha(P/'rank_boundary_controls.py')==f['code_sha256'],'boundary source changed');cutoff=2.**-24;rows=[]
 for name,value,expected in [('immediate_binary64_above',np.nextafter(cutoff,np.inf),1),('immediate_binary64_below',np.nextafter(cutoff,-np.inf),0)]:
  s=np.zeros(321,dtype=np.float64);s[0]=value;need(e.saved_rank(s)==expected,'boundary '+name);rows.append({'id':name,'pass':True})
 s=np.zeros(321,dtype=np.float64);s[0]=cutoff
 try:e.saved_rank(s);hold=False
 except ValueError:hold=True
 need(hold,'exact equality must HOLD');rows.append({'id':'exact_equality_HOLD_excluded_from_admission','pass':True});freeze();return {'status':'PASS_PROSPECTIVE_SAVED_RANK_BOUNDARIES','rows':rows,'new_raw_records':0,'new_estimator_calls':0,'actual_output_checks':0}
if __name__=='__main__':
 q=argparse.ArgumentParser();q.add_argument('--repo',required=True);q.add_argument('--out',required=True);a=q.parse_args();os.environ['UD_REPO']=str(Path(a.repo).resolve());out=guard(a.out);out.mkdir(parents=True,exist_ok=False);write_new(out/'CONTROLS.json',run())
