"""Six post-known guard controls; only temporary synthetic directories, zero raw reads."""
import argparse,hashlib,importlib.util,json,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    if not __debug__:raise RuntimeError('HOLD optimized runtime')
    parser=argparse.ArgumentParser();parser.add_argument('--out',required=True);args=parser.parse_args();out=Path(args.out);assert not out.exists()
    f=json.loads((HERE/'GUARD_CONTROL_FREEZE_v2.json').read_text());assert sha(HERE/'guard_controls_v2.py')==f['control_sha256'];assert sha(HERE/'WRAPPER_FREEZE.json')==f['wrapper_freeze_sha256'];wf=json.loads((HERE/'WRAPPER_FREEZE.json').read_text());assert sha(HERE/'replay_v2.py')==wf['wrapper_sha256']
    spec=importlib.util.spec_from_file_location('guarded_counterexample',HERE/'replay_v2.py');wrapper=importlib.util.module_from_spec(spec);spec.loader.exec_module(wrapper);rows=[]
    with tempfile.TemporaryDirectory(prefix='quality-guard-controls-') as td:
        t=Path(td);outer=t/'outer';inner=outer/'inner';source=inner/'source';source.mkdir(parents=True);(outer/'MANIFEST.json').write_text('{}');(inner/'MANIFEST.json').write_text('{}');safe=t/'safe';safe.mkdir();(t/'alias').symlink_to(outer,target_is_directory=True);(inner/'escape').symlink_to(safe,target_is_directory=True)
        cases=[('inside_package',source/'new',False),('sibling_under_outer_capture',outer/'sibling',False),('resolved_symlink_into_capture',t/'alias'/'sibling',False),('lexical_capture_symlink_outward',inner/'escape'/'new',False),('ancestor_of_source',t,False),('new_external_directory',safe/'new',True)]
        for name,path,want in cases:
            try:wrapper.guard_output(path,source);got=True;reason='ALLOW_NEW_EXTERNAL'
            except ValueError as e:got=False;reason=str(e)
            assert got==want,(name,got,want);rows.append({'id':name,'observed_allow':got,'expected_allow':want,'reason':reason})
    out.write_text(json.dumps({'status':'PASS_SIX_POST_KNOWN_GUARD_CONTROLS','freeze_sha256':sha(HERE/'GUARD_CONTROL_FREEZE_v2.json'),'rows':rows,'raw_reads':0,'new_estimator_calls':0,'numerical_replay_calls':0,'physical_promotion':0},indent=2)+'\n');print('PASS',len(rows))
if __name__=='__main__':main()
