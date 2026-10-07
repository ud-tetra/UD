#!/usr/bin/env python3
"""Render the authored Hasse current/curl audit source and package reproducible release files."""
import hashlib, json, subprocess, zipfile
from pathlib import Path
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
NAME='UD_HASSE_CURRENT_CURL_AUDIT_v0.1'
receipt=subprocess.run(['python3',str(ROOT/'replay/verify_hasse_current_curl.py')],capture_output=True,text=True,check=True).stdout
(ROOT/'audit/REPLAY_RECEIPT.json').write_text(receipt)
r=json.loads(receipt)
(ROOT/'audit/GAP_DISPOSITIONS.json').write_text(json.dumps({'basis':'Exact current/curl constructor receipt','open_system_closure':'OPEN','native_transport_law':'NOT_DERIVED','integer_curl_saturation':'CERTIFIED_ON_FIVE_NAMED_CARRIERS','physical_promotion':0},indent=2)+'\n')
body=subprocess.run(['pandoc',str(ROOT/'source/HASSE_CURRENT_CURL_AUDIT.md'),'--from=markdown+tex_math_single_backslash','--to=html5','--mathml','--shift-heading-level-by=1'],capture_output=True,text=True,check=True).stdout
style='body{max-width:980px;margin:2rem auto;padding:0 1.2rem;color:#182230;background:white;font:18px/1.6 system-ui,sans-serif}h1,h2{line-height:1.25}h1{font-size:2rem}h2{font-size:1.55rem}table{display:block;overflow:auto;border-collapse:collapse;font-size:16px}td,th{border:1px solid #bac6d3;padding:.6rem;text-align:left}th{background:#edf3f8}math[display=block]{display:block;overflow-x:auto;padding:.6rem 0}a{color:#075a9c}code{overflow-wrap:anywhere}@media(max-width:600px){body{font-size:17px;margin:1rem auto}h1{font-size:1.65rem}}'
header=f'<header><h1>UD Hasse current/curl audit: antisymmetry, continuity and invisible circulation</h1><p>5 October 2026 · Development addendum 0.1 · Independent review pending · Physical promotion 0</p><p>Fresh checks: {r["exact_checks"]} exact algebra checks; no floating-point tests. Exact current, curl, Smith-form and identifiability audit; native open-system laws remain open.</p></header>'
standalone=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>UD Hasse current/curl audit — Antisymmetry, continuity and invisible circulation</title><style>{style}</style></head><body>{header}{body}</body></html>'
(ROOT/(NAME+'.html')).write_text(standalone)
(ROOT/'audit/SITE_FRAGMENT.html').write_text(header+body)
d=html.fromstring(standalone)
assert len(d.xpath('//h2'))==6
assert len(d.xpath('//math'))>=25
assert not d.xpath('//script')
assert '14' in d.text_content() and 'circulation' in d.text_content()
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
