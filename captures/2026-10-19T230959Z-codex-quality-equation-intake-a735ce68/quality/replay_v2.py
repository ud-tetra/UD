"""Append-only guarded entrypoint. Scientific producer and frozen data unchanged."""
import argparse,hashlib,importlib.util,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def guard_output(output,source_dir=HERE):
    if not __debug__:raise RuntimeError('HOLD optimized runtime disables frozen producer assertions')
    source_lex=Path(source_dir).absolute();source_real=source_lex.resolve();protected={source_lex,source_real}
    for source in [source_lex,source_real]:
        for ancestor in [source,*source.parents]:
            if (ancestor/'MANIFEST.json').is_file():protected.update([ancestor.absolute(),ancestor.resolve()])
    lexical=Path(output).absolute();resolved=lexical.resolve()
    for candidate in [lexical,resolved]:
        for frozen in protected:
            if candidate==frozen or frozen in candidate.parents:raise ValueError('HOLD output inside protected package or capture')
            if candidate in frozen.parents:raise ValueError('HOLD output is ancestor of protected source')
    if lexical.exists() or resolved.exists():raise ValueError('HOLD output must be a new directory')
    return resolved

def main():
    if not __debug__:raise RuntimeError('HOLD optimized runtime disables frozen producer assertions')
    parser=argparse.ArgumentParser();parser.add_argument('--repo',required=True);parser.add_argument('--baseline',required=True);parser.add_argument('--out',required=True);args=parser.parse_args()
    f=json.loads((HERE/'WRAPPER_FREEZE.json').read_text())
    if sha(HERE/'replay_v2.py')!=f['wrapper_sha256']:raise ValueError('HOLD wrapper digest')
    if sha(HERE/'FREEZE.json')!=f['old_freeze_sha256']:raise ValueError('HOLD original freeze digest')
    original=json.loads((HERE/'FREEZE.json').read_text())
    if sha(HERE/'counterexample.py')!=f['old_code_sha256'] or original['code_sha256']!=f['old_code_sha256']:raise ValueError('HOLD original code digest')
    guard_output(args.out)
    spec=importlib.util.spec_from_file_location('frozen_quality_counterexample_v1',HERE/'counterexample.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.main()
if __name__=='__main__':main()
