from pathlib import Path
import json,hashlib,subprocess,tempfile,shutil
C=Path(__file__).parent;R=C.parents[1]
for x in json.loads((C/'SOURCE_INVENTORY.json').read_text()):
 b=(R/x['path']).read_bytes();assert len(b)==x['size_bytes'] and hashlib.sha256(b).hexdigest()==x['sha256']
receipt=json.loads((C/'FREEZE_RECEIPT.json').read_text())
assert receipt['sha256']==hashlib.sha256((C/'FROZEN_OPERATORS.json').read_bytes()).hexdigest()
with tempfile.TemporaryDirectory() as tmp:
 t=Path(tmp);shutil.copyfile(C/'freeze_operators.py',t/'freeze_operators.py')
 subprocess.run(['python3',str(t/'freeze_operators.py')],check=True,capture_output=True)
 for name in ('FROZEN_OPERATORS.json','FREEZE_RECEIPT.json'):assert (C/name).read_bytes()==(t/name).read_bytes()
g=json.loads((C/'GRAPH_CONNECTIVITY_CHECKS.json').read_text())
assert [r['components'] for r in g['explicit_graph_checks']]==[1,4,16]
assert [r['component_uniform_F'] for r in g['versionB_comparison']]==['16','64','256','1024']
a=json.loads((C/'AUDIT_RESULTS.json').read_text());assert a['source_files']==221 and a['capital_Docs_files']==51 and a['OCPF_literal_CSV_JSON_matches']==39
p=json.loads((C/'SIMULATION_PROVENANCE_MAP.json').read_text());assert len(p['families'])==9 and not p['per_probe_output_json_hits']
print(json.dumps({'status':'PASS_SCOPED','source_hashes':221,'operator_freeze_replay':'BYTE_IDENTICAL','graph_witness':'PASS; recovered connectedness claim FALSIFIED','OCPF_transcription_matches':39,'imported_code_executed':False,'independent_review':'PENDING','physical_promotion':0},indent=2))
