"""Frozen operational source binding; scientific PR246 recipes/caps unchanged."""
import sys
sys.dont_write_bytecode=True
import json,hashlib,os,io,zipfile
from pathlib import Path
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
a=lambda x:arb(fmpq(int(x[0]),int(x[1])))
def up(x):
    n=(arb(x.upper())*(1<<180)).ceil().unique_fmpz();assert n is not None;return [int(n),1<<180]
def down(x):
    n=(arb(x.lower())*(1<<180)).floor().unique_fmpz();assert n is not None;return [int(n),1<<180]
def repository():
    if os.environ.get('UD_REPO'):return Path(os.environ['UD_REPO']).resolve()
    for parent in [P,*P.parents]:
        if (parent/'AGENTS.md').exists() and (parent/'scripts/verify_repository.py').exists():return parent
        if (parent/'ud-repo/AGENTS.md').exists():return parent/'ud-repo'
    raise AssertionError('Explicit UD_REPO or --repo required')
def reference_basis():
    import numpy as np
    f=freeze();rows=[]
    for row in f['reference_basis_archives']:
        archive=repository()/row['archive'];assert sha(archive)==row['archive_sha256']
        with zipfile.ZipFile(archive) as z:assert z.namelist().count(row['member'])==1;blob=z.read(row['member'])
        assert hashlib.sha256(blob).hexdigest()==row['sha256']
        with np.load(io.BytesIO(blob),allow_pickle=False) as z:rows.append(z['basis'])
    U=np.vstack(rows);assert U.shape==(8191,209);return U
def freeze():
    f=json.loads((P/'PROTOCOL_FREEZE.json').read_text())
    for n,h in f['files'].items():assert sha(P/n)==h,('code/input',n)
    for n,h in f['repository_sources'].items():assert sha(repository()/n)==h,('repository source',n)
    return f
