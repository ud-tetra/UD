from pathlib import Path
import json,hashlib
root=Path(__file__).parent;fine=passed=failed=0;details=[]
for p in sorted(root.glob('*/ENERGY_CHECK.json')):
 s=json.loads(p.read_text());assert hashlib.sha256(p.with_name('energy.log').read_bytes()).hexdigest()==s['log_sha256']
 for r in s['checks']:
  h=r['h_A'];ep,e0,em=r['raw_energies_eV'];ke=(ep-2*e0+em)/(h*h);assert ke==r['K_energy']
  assert r['K_passes']==(abs(ke-r['K_force'])<=1e-5+1e-4*abs(r['K_force']))
  assert r['first_passes']==(abs((ep-em)/(2*h)-r['first_force'])<=2e-7)
  checks=[('K',r['K_passes']),('first',r['first_passes'])]
  for g in r['mixed']:
   pp,pm,mp,mm=g['raw_energies_eV'];v=(pp-pm-mp+mm)/(4*h*h);assert v==g['energy_mixed']
   assert g['passes']==(abs(v-g['force_mixed'])<=2e-5+1e-3*abs(g['force_mixed']))
   checks.append(('mixed_'+str(g['axis']),g['passes']))
  if h<=.001:
   fine+=len(checks)
   for label,ok in checks:
    if ok:passed+=1
    else:failed+=1;details.append({'case':s['case'],'direction':r['direction'],'h_A':h,'check':label})
summary=json.loads((root/'SUMMARY.json').read_text());assert summary['status']=='HOLD_SCOPED_FAILURE' if failed else True
result={'status':'VERIFICATION_PASS__SCIENTIFIC_GATE_HOLD' if failed else 'VERIFICATION_PASS','fine_energy_controls':fine,'passed':passed,'failed':failed,'failed_controls':details,'cutoff_pass_cases':sum(x['cutoff_gate_pass'] for x in summary['cases']),'cutoff_total_cases':len(summary['cases']),'physical_promotion':0,'scope':'constructor recalculation of saved arithmetic and hashes; no independent review'}
(root/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
