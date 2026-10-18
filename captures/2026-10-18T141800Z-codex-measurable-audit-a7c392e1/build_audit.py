"""Generate the authored audit report and mechanically register its Site milestone."""
import hashlib, html, json, re, shutil
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path('/workspace/scratch/1544cec576c6')
CAP=ROOT/'ud-audit-repo/captures/2026-10-18T141800Z-codex-measurable-audit-a7c392e1'
SITE=ROOT/'ud-public/dist'
data=json.loads((CAP/'REPORT_CONTENT_v0.1.json').read_text())
pdfmetrics.registerFont(TTFont('AuditSans','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('AuditBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
body=ParagraphStyle('body',fontName='AuditSans',fontSize=9.2,leading=13.2,textColor=HexColor('#233438'),spaceAfter=9,splitLongWords=True)
head=ParagraphStyle('head',fontName='AuditBold',fontSize=17,leading=22,textColor=HexColor('#174a4a'),spaceAfter=15)
label=ParagraphStyle('label',fontName='AuditBold',fontSize=9.4,leading=13.2,textColor=HexColor('#174a4a'),spaceAfter=3)
small=ParagraphStyle('small',parent=body,fontSize=8,leading=11)
out=CAP/'UD_MEASURABLE_REALIZATION_DATA_AUDIT_v0.1.pdf'
story=[]
for i,page in enumerate(data['pages']):
    if i:story.append(PageBreak())
    story.extend([Paragraph(html.escape(data['subtitle']),small),Paragraph(html.escape(page['heading']),head)])
    if i==0:story.extend([Paragraph(html.escape(data['title']),label),Paragraph(html.escape(data['status']),small),Spacer(1,8)])
    for title,txt in page['blocks']:
        story.append(KeepTogether([Paragraph(html.escape(title),label),Paragraph(html.escape(txt),body)]))
def footer(c,doc):
    c.setStrokeColor(HexColor('#bdcdcb'));c.line(42,39,553,39)
    c.setFont('AuditSans',7);c.setFillColor(HexColor('#526d70'))
    c.drawString(42,27,'UD / MRA v0.1 | Dataset-scoped audit | Independent review pending | Physical promotion 0')
    c.drawRightString(553,27,str(doc.page))
SimpleDocTemplate(str(out),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=37,bottomMargin=50).build(story,onFirstPage=footer,onLaterPages=footer)

dest=SITE/'sources/measurable-audit-v0.1';dest.mkdir(parents=True,exist_ok=True)
for p in [out,CAP/'DATASET_INVENTORY_v0.1.json',CAP/'WAVEFORM_AUDIT_v0.1.json',CAP/'audit_waveform.py']:
    shutil.copy2(p,dest/p.name)
template=(SITE/'evidence/index.html').read_text()
intro='<div class="page-intro"><div class="eyebrow">18 October 2026 UTC / MRA v0.1</div><h1>A measurable bridge candidate.</h1><p class="lede">Rank-one nonlinear circuit emulator selected for development. Published data audited within explicit limits. Physical promotion remains 0.</p></div>'
intro+='<p><a class="text-link" href="/sources/measurable-audit-v0.1/'+out.name+'">Download the six-page audit report →</a></p>'
intro+='<p><a href="/sources/measurable-audit-v0.1/DATASET_INVENTORY_v0.1.json">Dataset inventory</a> · <a href="/sources/measurable-audit-v0.1/WAVEFORM_AUDIT_v0.1.json">Waveform audit</a> · <a href="/sources/measurable-audit-v0.1/audit_waveform.py">Read-only parser</a></p>'
sections=''.join('<section class="chapter"><div class="chapter-label">'+str(i+1).zfill(2)+'</div><div><h2>'+html.escape(p['heading'])+'</h2>'+''.join('<h3>'+html.escape(t)+'</h3><p>'+html.escape(x)+'</p>' for t,x in p['blocks'])+'</div></section>' for i,p in enumerate(data['pages']))
page=re.sub(r'<main id="main">.*?</main>','<main id="main">'+intro+sections+'</main>',template,flags=re.S)
page=page.replace('<title>Evidence · Unified Dynamics</title>','<title>Measurable Realization Audit · Unified Dynamics</title>')
folder=SITE/'evidence/measurable-audit';folder.mkdir(parents=True,exist_ok=True);(folder/'index.html').write_text(page)
card='<article class="claim" id="measurable-audit-v01"><div class="eyebrow">18 October 2026 UTC · Dataset audit 0.1</div><h2>A nonlinear circuit candidate, with the data boundary explicit</h2><p>Selected a rank-one rotor–matter circuit emulator for development. Audited a complete published ten-channel waveform against its deposit checksum and inspected two cold-atom data sources. The published LC device is not the full UD Hamiltonian: its oscillator links differ from unitary rotor links, and its chain lacks the required diamonds.</p><p>No audited record supplies all preparation, energy and source-work gates. A closed-diamond component test and a calibrated measurement contract are the next experimental requirements. Constructor audit; independent review pending; physical promotion 0.</p><a class="text-link" href="/evidence/measurable-audit/">Read selection, dataset audit and experiment requirements →</a></article>'
p=SITE/'updates/index.html';s=p.read_text();assert 'id="measurable-audit-v01"' not in s;s=s.replace('<article class="claim" id="source-work-v01">',card+'<article class="claim" id="source-work-v01">',1);p.write_text(s)
p=SITE/'evidence/index.html';s=p.read_text();assert 'id="measurable-audit-v01"' not in s;s=s.replace('<section class="chapter" id="observation-review-status">',card+'<section class="chapter" id="observation-review-status">',1);p.write_text(s)
p=SITE/'assets/sources.json';sources=json.loads(p.read_text());assert not any(x['id']=='MRA01' for x in sources)
sources.append({'id':'MRA01','title':data['title']+' v0.1','group':'Evidence audits','status':data['status'],'note':'One complete circuit waveform content audit, two atomic-data comparators; no full UD realization or GUT inference.','url':'/evidence/measurable-audit/','local':'/sources/measurable-audit-v0.1/'+out.name,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'size_bytes':out.stat().st_size,'content':'\n\n'.join(p['heading']+'\n'+'\n'.join(t+': '+s for t,s in p['blocks']) for p in data['pages'])});p.write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pdf':str(out),'site_page':'/evidence/measurable-audit/','source_id':'MRA01'}))
