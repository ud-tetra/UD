#!/usr/bin/env python3
"""Render the authored M13 source and package reproducible release files."""
import hashlib, json, subprocess, zipfile
from pathlib import Path
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
NAME='UD_M13_COUPLED_POINTER_RETENTION_v0.1'
receipt=subprocess.run(['python3',str(ROOT/'replay/verify_coupled_pointer.py')],capture_output=True,text=True,check=True).stdout
(ROOT/'audit/REPLAY_RECEIPT.json').write_text(receipt)
r=json.loads(receipt)
(ROOT/'audit/WBS_DISPOSITIONS.json').write_text(json.dumps({'basis':'M13 executed constructor receipt','work_packages':r['wbs_status'],'full_controller_status':'OPEN','physical_promotion':0},indent=2)+'\n')
body=subprocess.run(['pandoc',str(ROOT/'source/COUPLED_POINTER_RETENTION.md'),'--from=markdown+tex_math_single_backslash','--to=html5','--mathml','--shift-heading-level-by=1'],capture_output=True,text=True,check=True).stdout
style='body{max-width:980px;margin:2rem auto;padding:0 1.2rem;color:#182230;background:white;font:18px/1.6 system-ui,sans-serif}h1,h2{line-height:1.25}h1{font-size:2rem}h2{font-size:1.55rem}table{display:block;overflow:auto;border-collapse:collapse;font-size:16px}td,th{border:1px solid #bac6d3;padding:.6rem;text-align:left}th{background:#edf3f8}math[display=block]{display:block;overflow-x:auto;padding:.6rem 0}a{color:#075a9c}code{overflow-wrap:anywhere}@media(max-width:600px){body{font-size:17px;margin:1rem auto}h1{font-size:1.65rem}}'
header=f'<header><h1>UD M13: coupled pointer and finite retention certificate</h1><p>5 October 2026 · Development addendum 0.1 · Independent review pending · Physical promotion 0</p><p>Fresh checks: {r["exact_checks"]} exact and {r["numerical_checks"]} numerical. Coupled pair-qubit toy window certified analytically; enormous finite clocks, full controller open.</p></header>'
standalone=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UD M13 — Coupled pointer and finite retention certificate</title><style>{style}</style></head><body>{header}{body}</body></html>'
(ROOT/(NAME+'.html')).write_text(standalone)
(ROOT/'audit/SITE_FRAGMENT.html').write_text(header+body)
d=html.fromstring(standalone)
assert len(d.xpath('//h2'))==6
assert len(d.xpath('//math'))>=25
assert not d.xpath('//script')
assert '380' in d.text_content() and 'pointer' in d.text_content()
assert '\\[' not in d.text_content()
assert '$$' not in d.text_content()
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts)
manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(ROOT/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2)+'\n')
out=ROOT.parent/(NAME+'_RELEASE.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for p in files+[ROOT/'SHA256SUMS.json']:
        info=zipfile.ZipInfo(NAME+'/'+str(p.relative_to(ROOT)),date_time=(2026,10,5,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(info,p.read_bytes())
print(json.dumps({'status':'PASS','exact_checks':r['exact_checks'],'numerical_checks':r['numerical_checks'],'html_math_elements':len(d.xpath('//math')),'release_files':len(files)+1,'archive':str(out),'archive_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
