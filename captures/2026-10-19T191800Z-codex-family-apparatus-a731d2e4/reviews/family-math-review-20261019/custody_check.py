"""Read-only exact JSON extraction and source-hash audit; no model evaluation."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;P=ROOT/'family-apparatus-work'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def run():
 fr=load(HERE/'CUSTODY_FREEZE.json')
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 provenance=load(P/'INPUT_PROVENANCE.json');rows=[]
 for r in provenance['sources']:
  source=ROOT/'ud-repo'/r['source_path'];destination=P/r['destination'];assert sha(source)==r['source_sha256'] and sha(destination)==r['destination_sha256']
  capture=r['source_path'].split('/')[1];assert sha(ROOT/'ud-repo/captures'/capture/'MANIFEST.json')==r['source_manifest_sha256']
  original=load(source);actual=load(destination)
  if r['destination']=='inputs/ANCHORS.json':expected={'rows':[{k:row[k] for k in ['case','record_sha256','cutoff']} for row in original['rows']]}
  elif r['destination']=='inputs/BASE_GENERATION.json':expected={'row':next(x for x in original['records'] if x['case']=='ramp_clock_stress')}
  else:expected=original
  assert actual==expected
  rows.append({'destination':r['destination'],'source_sha256':r['source_sha256'],'destination_sha256':r['destination_sha256'],'exact_semantic_extraction_verified':True})
 assert load(P/'inputs/SOURCE_BOUNDS.json')==load(HERE/'SOURCE_BOUNDS.json')
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 q=HERE/'CUSTODY_CHECK.json';assert not q.exists();q.write_text(json.dumps({'status':'PASS_SOURCE_MANIFEST_HASHES_AND_EXACT_DERIVED_JSON_CUSTODY','rows':rows,'independent_source_bounds_receipt_identity':True,'freeze_sha256':sha(HERE/'CUSTODY_FREEZE.json'),'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Same-team pre-run metadata audit only; root certify function not executed. No raw, fitting or apparatus validation.','external_review':'PENDING','physical_promotion':0},indent=2))

if __name__=='__main__':run()
