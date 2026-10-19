"""Selected source pair errors using direct theta-2omega+2kpi, no arg(exp)."""
import sys
sys.dont_write_bytecode=True
import argparse,hashlib,json
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;P=ROOT/'cutoff-campaign-work'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda p:arb(fmpq(int(p[0]),int(p[1])))

def upper(x):
 n=(x*(1<<180)).ceil().unique_fmpz();assert n is not None
 return [int(n),1<<180]

def run(kind):
 f=load(HERE/('CIRCULAR_'+kind.upper()+'_FREEZE.json'))
 for p,h in f['files'].items():assert sha(ROOT/p)==h,p
 protocol=load(P/'PROTOCOL_FREEZE.json');targets=load(P/'inputs/SOURCE_PHASE.json');target=targets['target_matches'];sep=a(targets['metrics']['minimum_target_chord_lower']);assert len(target)==209
 parent=ROOT/'ud-repo/captures'/protocol['parent_capture']['capture']
 cert=load(P/('PARENT_NUMERIC_CERTIFICATES.json' if kind=='parent' else 'CAMPAIGN_NUMERIC_CERTIFICATES.json'));folder=parent if kind=='parent' else P;rows=[]
 for main in cert['rows']:
  phase=main.get('phase',{});observed=phase.get('observed');row={'case':main['case'],'record_sha256':main['record_sha256'],'main_combined_status_retained':main['status']}
  if observed is None:
   assert main['status'].startswith('HOLD');row['review_status']='HOLD_WITHOUT_OBSERVED_LIST_RETAINED';rows.append(row);continue
  case=folder/'results'/main['case'];run=load(case/'RUN.json')
  for n,h in run['numeric_witnesses'].items():assert sha(case/n)==h,n
  em=np.load(case/'PHASE_PROPOSAL.npz',allow_pickle=False)['two_step_phase'];assert em.shape==(209,) and em.dtype==np.int64
  matches=observed['rows'];assert len(matches)==209 and sorted(m['emitted_index'] for m in matches)==list(range(209));pairrows=[]
  for match in matches:
   i=match['emitted_index'];j=match['target_index'];assert match['target_label']==target[j]['label']
   theta=arb(int(em[i]))/(1<<60);omega=a(target[j]['omega']);assert abs(theta)<arb.pi()+arb(1)/(1<<59) and abs(2*omega)<4*arb.pi()
   direct=theta-2*omega
   distances=[abs(direct+2*k*arb.pi()) for k in range(-4,5)]
   # The exact minimum lies between these independently formed endpoint minima.
   hi=min(z.upper() for z in distances);lo=min(z.lower() for z in distances);bound=upper(arb(hi));assert bound==match['circular_error_upper']
   within=bool(arb(hi)<sep/2)
   assert within==match['unique_and_within_fixed_radius']
   pairrows.append({'emitted_index':i,'target_index':j,'direct_circular_error_upper':bound,'main_exact_grid_bound_match':True,'within_source_half_chord':within})
  bijective=len({m['target_index'] for m in matches})==209;assert bijective==observed['bijective']
  maximum=[max(x['direct_circular_error_upper'][0] for x in pairrows),1<<180];assert maximum==observed['maximum_circular_error_upper']
  passed=bijective and all(x['within_source_half_chord'] for x in pairrows);assert passed==(observed['status']=='CERTIFIED_OBSERVED_TWO_STEP_EMISSION_BIJECTION')
  row.update(review_status='PASS_DIRECT_CIRCULAR_ARITHMETIC_AGREEMENT',main_observed_status_retained=observed['status'],matching_pairs_checked=209,maximum_direct_circular_error_upper=maximum,readable_maximum_direct_circular_error_upper=float(a(maximum).upper()),pairs=pairrows);rows.append(row)
  print(json.dumps({k:row[k] for k in ['case','review_status','main_combined_status_retained','main_observed_status_retained','readable_maximum_direct_circular_error_upper']}),flush=True)
 for p,h in f['files'].items():assert sha(ROOT/p)==h,p
 result={'status':'PASS_DIRECT_CIRCULAR_SOURCE_PAIR_REVIEW','kind':kind,'rows':rows,'source_targets_sha256':sha(P/'inputs/SOURCE_PHASE.json'),'main_certificate_sha256':sha(P/('PARENT_NUMERIC_CERTIFICATES.json' if kind=='parent' else 'CAMPAIGN_NUMERIC_CERTIFICATES.json')),'freeze_sha256':sha(HERE/('CIRCULAR_'+kind.upper()+'_FREEZE.json')),'all_pinned_hashes_before_after_equal':True,'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Same-team alternative expression for every selected pair. No complex exponential/argument, parent helper import, new matching optimization, estimator/SVD or raw writes. Parent combined HOLDs preserved. Source separation proof remains inherited.','external_review':'PENDING','physical_promotion':0}
 out=HERE/('CIRCULAR_'+kind.upper()+'.json');assert not out.exists();out.write_text(json.dumps(result,indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('kind',choices=['parent','new']);run(p.parse_args().kind)
