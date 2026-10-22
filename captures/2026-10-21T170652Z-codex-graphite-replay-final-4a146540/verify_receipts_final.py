from pathlib import Path
import json,hashlib,re
root=Path(__file__).parent
freeze=json.loads((root/'REPLAY_FREEZE.json').read_text());result=json.loads((root/'REPLAY_RESULTS.json').read_text())
assert len(result['results'])==4
assert [(x['pattern'],x['case']) for x in result['results']]==[tuple(x) for x in freeze['cases']]
for r in result['results']:
 p=root/'selected'/r['pattern']/r['case'];old=(p/'log.lammps').read_text();new=(p/'compatibility.log').read_text()
 def energy(s):return float(re.search(r'Energy initial, next-to-last, final =\s*\n\s*([^\n]+)',s).group(1).split()[-1])
 assert energy(old)==r['archived_final_Epair_eV']
 assert abs(energy(new)-r['replayed_pe_eV'])<=1e-10
 assert abs(r['replayed_pe_eV']-r['archived_final_Epair_eV'])<=freeze['energy_tolerance_eV_per_cell']
 receipt=next(x for x in json.loads((root/'FINAL_LOG_RECEIPTS.json').read_text()) if x['pattern']==r['pattern'] and x['case']==r['case'])
 assert hashlib.sha256((p/'compatibility.log').read_bytes()[:receipt['pre_close_prefix_bytes']]).hexdigest()==r['log_sha256']
 assert hashlib.sha256((p/'compatibility.log').read_bytes()).hexdigest()==receipt['final_sha256']
c=json.loads((root/'CUSTODY_AND_GRID.json').read_text());assert len(c['archive_custody'])==2
files=[]
for p in sorted((root/'selected').rglob('*')):
 if p.is_file():files.append({'path':str(p.relative_to(root)),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'SELECTED_FILES.json').write_text(json.dumps(files,indent=2)+'\n')
print(json.dumps({'status':'PASS_SCOPED','replayed_cases':4,'max_energy_difference_eV_per_cell':max(abs(r['difference_eV']) for r in result['results']),'verified_archives':2,'selected_files_hashed':len(files),'physical_promotion':0}))
