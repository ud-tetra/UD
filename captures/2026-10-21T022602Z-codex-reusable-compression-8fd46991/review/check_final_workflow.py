"""Bind final sources and fresh partial workflow without re-executing producer scripts."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;W=P.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
frozen=json.loads((W/'c32_FINAL_FREEZE.json').read_text());sources=['c32_certify.py','c32_construct.py','c32_partial_solve.py','c32_reproduce.py','c32_THEOREM.md'];assert set(frozen['files'])==set(sources)
for name in sources:assert sha(W/name)==frozen['files'][name]
mathchecks=[]
for name in ['RESULT.json','CONTROLS.json','SOURCE_BINDINGS.json','TRIAL_SLICE.json','OPERATOR.txt']:
 a=W/'c32_math_final'/name;b=W/'c32_math_replay'/name;c=W/'c32_workflow_replay/math'/name;assert a.read_bytes()==b.read_bytes()==c.read_bytes();mathchecks.append({'file':name,'sha256':sha(a)})
base=W/'c32_partial_final';fresh=W/'c32_workflow_replay/frame';again=W/'c32_workflow_replay/frame_replay';replay=[]
for p in fresh.iterdir():
 assert p.is_file() and p.read_bytes()==(again/p.name).read_bytes();replay.append(p.name)
assert len(replay)==17
for p in base.glob('row_*.i128.gz'):assert p.read_bytes()==(fresh/p.name).read_bytes()
b=json.loads((base/'PARTIAL_FRAME.json').read_text());f=json.loads((fresh/'PARTIAL_FRAME.json').read_text());base_build=b.pop('build_receipt_sha256');fresh_build=f.pop('build_receipt_sha256');assert b==f
build=W/'c32_workflow_replay/BUILD_RECEIPT.json';bj=json.loads(build.read_text());assert sha(build)==fresh_build and bj['source_sha256']==sha(W/'c31_action.cpp') and bj['executable_sha256']==sha(W/'c32_workflow_replay/native_action')
bs=W/'c32_solve_final';fs=W/'c32_workflow_replay/solve';s=json.loads((bs/'PARTIAL_SOLVE.json').read_text());t=json.loads((fs/'PARTIAL_SOLVE.json').read_text());base_frame=s.pop('frame_receipt_sha256');fresh_frame=t.pop('frame_receipt_sha256');assert s==t and base_frame==sha(base/'PARTIAL_FRAME.json') and fresh_frame==sha(fresh/'PARTIAL_FRAME.json')
assert (bs/'LIFT.i128.gz').read_bytes()==(fs/'LIFT.i128.gz').read_bytes()
assert frozen['partial_frame_sha256']==sha(base/'PARTIAL_FRAME.json') and frozen['partial_solve_sha256']==sha(bs/'PARTIAL_SOLVE.json')
for name in ['PARTIAL_SOLVE.json','LIFT.i128.gz']:assert (W/'c32_solve'/name).read_bytes()==(bs/name).read_bytes()
active_scalar=json.loads((P/'SCALAR_BINDING_CHECKS_final.json').read_text());assert active_scalar['root_RESULT_sha256']==sha(W/'c32_math_final/RESULT.json') and active_scalar['root_SOURCE_BINDINGS_sha256']==sha(W/'c32_math_final/SOURCE_BINDINGS.json')
root_replay=json.loads((W/'c32_REPLAY_RECEIPT.json').read_text());assert len(root_replay['byte_checks'])==24
for check in root_replay['byte_checks']:
 name=check['path'];target=(W/'c32_math_final'/name)if '/'not in name else (base/name.split('/',1)[1]if name.startswith('frame/')else bs/name.split('/',1)[1]);assert sha(target)==check['sha256'] and check['byte_identical'] is True
report={'status':'PASS','source_hashes':frozen['files'],'root_theorem_sha256':frozen['files']['c32_THEOREM.md'],'math_source_files_three_way_byte_identical':mathchecks,'fresh_internal_frame_replay_files':17,'fresh_all16_row_bytes_match_primary':True,'fresh_lift_bytes_match_primary':True,'fresh_metadata_differs_only_expected_parent_build_or_frame_receipt_hashes':True,'root24bytecheck_hashes_independently_bound':True,'partial_frame_sha256':sha(base/'PARTIAL_FRAME.json'),'partial_solve_sha256':sha(bs/'PARTIAL_SOLVE.json'),'fresh_workflow_build_receipt_sha256':sha(build),'fresh_workflow_executable_sha256':bj['executable_sha256'],'scope':{'root_fresh_workflow_receipts_and_source_bindings_checked_not_rerun_by_reviewer':True,'source_authentication_not_statistical_independence':True,'full_frame_construction_status':'NOT_RUN_HOLD','full_solve_status':'NOT_RUN_HOLD','physical_promotion':0,'external_review':'PENDING'}}
(P/'FINAL_WORKFLOW_CHECKS.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n');print('PASS5sourcefiles,5threewaymathreplays,17freshframefiles,16rows,partialsolve and24rootbindings')
