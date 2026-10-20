from pathlib import Path
import ast,hashlib,json,shutil,datetime,subprocess
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';src=R/'captures/2026-10-20T133845Z-codex-three-noise-f72a62fa/baseline_recovery';out=P/'c15_baseline_recovery';out.mkdir(exist_ok=False);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n in ['recover_baseline.py','RECOVERY_FREEZE.json','REFERENCE_PROPOSAL.npz']:
 shutil.copyfile(src/n,out/n)
f=json.loads((out/'RECOVERY_FREEZE.json').read_text())
assert sha(out/'recover_baseline.py')==f['recovery_source_sha256'];assert sha(out/'REFERENCE_PROPOSAL.npz')==f['reference_proposal_sha256']
for n,h in f['repository_sources'].items():assert sha(R/n)==h,n
source=(out/'recover_baseline.py').read_text();old=(R/'captures/2026-10-18T172041Z-codex-floating-timing-2f6a91ce/make_records.py').read_text();oldproof=(R/'captures/2026-10-18T172041Z-codex-floating-timing-2f6a91ce/proof_math.py').read_text()
a=source[source.index('BITS=96'):source.index('def main():')];b=old[old.index('BITS=96'):old.index('def generate(')];assert a==b
function=lambda s,name:ast.get_source_segment(s,next(x for x in ast.parse(s).body if isinstance(x,ast.FunctionDef) and x.name==name))
assert function(source,'nearest')==function(oldproof,'nearest')
tree=ast.parse(source);imports=[]
for node in ast.walk(tree):
 if isinstance(node,ast.Import):imports.extend(a.name for a in node.names)
 elif isinstance(node,ast.ImportFrom):imports.append(node.module)
 elif isinstance(node,ast.Call):
  if isinstance(node.func,ast.Name):assert node.func.id not in ['exec','eval','compile','__import__']
  elif isinstance(node.func,ast.Attribute):assert node.func.attr not in ['estimate','svd','lstsq','eig','eigvals','inv']
assert not any('estimator'in m or'proposer'in m for m in imports)
review={'status':'PASS_FRESH_BASELINE_SOURCE_PINS_FORMULA_IDENTITY_AND_STATIC_SCOPE','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_main':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),'source_capture':'2026-10-20T133845Z-codex-three-noise-f72a62fa/baseline_recovery','recovery_source_sha256':sha(out/'recover_baseline.py'),'recovery_freeze_sha256':sha(out/'RECOVERY_FREEZE.json'),'repository_source_pins_verified':f['repository_sources'],'reference_proposal_sha256':sha(out/'REFERENCE_PROPOSAL.npz'),'phase_timing_matrix_evaluation_slice_byte_identical':True,'nearest_function_byte_identical':True,'imports':imports,'estimator_or_dynamic_execution_found':False,'archived_code_executed':False,'new_estimator_calls_authorized':0,'original_recipe_expected_sha256':f['expected_original_generation_row']['record_sha256'],'original_record_bytes':150321232,'new_recovery_attempt':1,'physical_promotion':0,'external_review':'PENDING'}
(out/'RECOVERY_PRECHECK.json').write_text(json.dumps(review,indent=2)+'\n')
(out/'README.md').write_text('''# Exact nominal baseline recovery for boundary campaign

Development — no registry entry; Physical Promotion=0; external promotion review PENDING.

This is one fresh execution of the byte-identical reviewed PR269 standalone recovery source, after scratch maintenance removed the prior raw baseline. It reconstructs the same computational nominal record, not new physical measurements. RECOVERY_PRECHECK.json freshly verifies every original repository/source/reference pin, exact formula and rounding identity, and absence of estimator or dynamic-code execution. The original source freeze is retained unchanged as source authority; its source_main field is the historical source anchor, not a claim about the current execution.

Only recover_baseline.py, RECOVERY_FREEZE.json and REFERENCE_PROPOSAL.npz were copied before execution. No old execution receipt was copied. The new RECOVERY_RECEIPT.json will be emitted exclusively by this new run. The raw is 150321232 bytes of little-endian int64, shape37x8191x62, made read-only after its SHA exactly matches25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59. Zero estimator calls, no archived code executed.

Repeat only in a new external directory with its parent containing ud-repo and the pinned repository sources. Run `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python recover_baseline.py`. Never overwrite prior evidence. The raw may remain external to Git capture; the explicit output inventory excludes it.
''')
print(json.dumps({'status':review['status'],'source_sha256':review['recovery_source_sha256'],'freeze_sha256':review['recovery_freeze_sha256']}))
