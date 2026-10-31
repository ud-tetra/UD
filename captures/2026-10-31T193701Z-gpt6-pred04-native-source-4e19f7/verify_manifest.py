#!/usr/bin/env python3
"""Verify an immutable, versioned UD research capture from its own directory."""
import hashlib,json
from pathlib import Path

def verify(root:Path):
    m=json.loads((root/'MANIFEST.json').read_text())
    assert m['physical_promotion']==0
    names=set()
    for x in m['files']:
        rel=Path(x['path'])
        assert rel.parts[-1] != 'MANIFEST.json'
        name=rel.name
        assert name not in names
        names.add(name)
        data=(root/name).read_bytes()
        assert len(data)==x['size_bytes'], name
        assert hashlib.sha256(data).hexdigest()==x['sha256'],name
    actual={x.name for x in root.iterdir() if x.is_file() and x.name!='MANIFEST.json'}
    assert actual==names, f'undeclared files: {actual^names}'
    return {'status':'PASS','files':len(names),'physical_promotion':0}

if __name__=='__main__':print(json.dumps(verify(Path(__file__).parent)))
