"""Explicitly reviewed fixed source function only; never import a source runner."""
import ast,hashlib,json
from pathlib import Path
import numpy as np
import certify_v2 as c
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(repo):
    f=json.loads((P/'SAME_SKETCH_PROBE_FREEZE.json').read_text());assert sha(P/'same_sketch_probe.py')==f['probe_sha256'];c.binding(repo)
    p=repo/f['source_path'];assert sha(p)==f['source_sha256']=='7f07f4c76fcb9e446fe7665ff7747bdd07515013eeb1eb32b4da9d4573ebfb7b'
    parent=json.loads((repo/f['parent_freeze_path']).read_text());assert parent['code_sha256']['sketch.py']==f['source_sha256'];assert sha(P/'inputs/NULL_VECTOR.json')==parent['code_sha256']['inputs/NULL_VECTOR.json']
    parsed=ast.parse(p.read_text());functions=[z for z in parsed.body if isinstance(z,ast.FunctionDef)];assert len(functions)==1 and functions[0].name=='sketch'
    # Only this pinned, fully read pure sketch() is executed. P points at the SAME frozen null bytes.
    module=ast.Module(body=functions,type_ignores=[]);scope={'P':P,'np':np,'json':json};exec(compile(module,str(p),'exec'),scope);original=scope['sketch']()
    old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64);current=np.column_stack((2*old,v,2*new));assert np.array_equal(original,current)
    gramsha=hashlib.sha256((current.T@current).astype('<i8').tobytes()).hexdigest();assert gramsha==c.sketch_power_bounds()['Gram_int64le_sha256']
    return {'status':'PASS_EXACT_SAME_SKETCH_FUNCTION_ARRAY_AND_GRAM_BINDING','source_sha256':f['source_sha256'],'source_path':f['source_path'],'source_ast_scope':'Only the reviewed fixed sketch() function; no runner/bindings or archivedscript import','same_null_vector_sha256':sha(P/'inputs/NULL_VECTOR.json'),'int64le_array_sha256':hashlib.sha256(current.astype('<i8').tobytes()).hexdigest(),'same_exact_Gram_sha256':gramsha,'matrix_entries_compared':int(current.size),'new_estimator_calls':0,'physical_promotion':0}
if __name__=='__main__':
    import argparse
    a=argparse.ArgumentParser();a.add_argument('--repo',required=True);args=a.parse_args();print(json.dumps(run(Path(args.repo).resolve())),flush=True)
