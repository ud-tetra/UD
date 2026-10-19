"""Post-known engineering negative control of actual frozen custody checker."""
import argparse,hashlib,importlib.util,json,os,shutil
from pathlib import Path
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(producer,repo,out):
    producer=Path(producer).resolve();out=Path(out).resolve();freeze=json.loads((P/'CONTROL_FREEZE.json').read_text())
    assert sha(P/'actual_freeze_control.py')==freeze['harness_sha256'];assert sha(producer/'common.py')==freeze['common_sha256'] and sha(producer/'PROTOCOL_FREEZE.json')==freeze['producer_protocol_sha256']
    assert out not in [P,producer] and P not in out.parents and producer not in out.parents and out not in P.parents and out not in producer.parents
    for src in [P,producer]:
        for ancestor in src.parents:
            if (ancestor/'MANIFEST.json').exists():assert out!=ancestor and ancestor not in out.parents
    out.mkdir(parents=True,exist_ok=False);os.environ['UD_REPO']=str(Path(repo).resolve());spec=importlib.util.spec_from_file_location('isolated_frozen_custody',producer/'common.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    original=m.freeze();assert len(original['files'])==25;before={n:sha(producer/n) for n in original['files']};staged=out/'staged';staged.mkdir()
    for n,h in original['files'].items():
        dst=staged/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(producer/n,dst);assert sha(dst)==h
    shutil.copyfile(producer/'PROTOCOL_FREEZE.json',staged/'PROTOCOL_FREEZE.json')
    target=staged/'CONTRACT.json';target.write_bytes(target.read_bytes()+b'\n');assert sha(target)!=original['files']['CONTRACT.json'];m.P=staged;rejected=None
    try:m.freeze()
    except AssertionError as exc:rejected={'type':type(exc).__name__,'args':list(exc.args),'repr':repr(exc)}
    assert rejected is not None and rejected['args']==[('code/input','CONTRACT.json')],rejected
    m.P=producer;m.freeze();after={n:sha(producer/n) for n in original['files']};assert before==after
    result={'status':'PASS_ACTUAL_FROZEN_CHECKER_REFUSES_STAGED_CONTRACT_HASH','utc':datetime.now(timezone.utc).isoformat(),'producer_protocol_sha256':sha(producer/'PROTOCOL_FREEZE.json'),'control_freeze_sha256':sha(P/'CONTROL_FREEZE.json'),'positive_actual_freeze_before_and_after':True,'exception':rejected,'corruption':'One appended newline in COPY of CONTRACT; no scientific values changed and no original file modified.','staged_small_files':len(original['files']),'original_file_hashes_before':before,'original_file_hashes_after':after,'actual_rejection_boundary':'local code/input CONTRACT hash before external source/reference loading','new_raw_records_or_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'scope':'POST-KNOWN engineering control frozen after all4 science outcomes, before this first negative-control invocation. Does not retroactively preregister control or change cases, gates or original predicate-control result.','physical_promotion':0};(out/'ACTUAL_FREEZE_CONTROL_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':result['status'],'receipt_sha256':sha(out/'ACTUAL_FREEZE_CONTROL_RECEIPT.json')}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--producer',required=True);p.add_argument('--repo',required=True);p.add_argument('--out',required=True);x=p.parse_args();run(x.producer,x.repo,x.out)
