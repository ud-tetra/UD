from html.parser import HTMLParser
from html import unescape
from pathlib import Path
import re,json,hashlib,unicodedata
class Scan(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.text=[];self.links=[];self.script_tags=[];self.trs=[];self.row=None
 def handle_starttag(self,t,a):
  d=dict(a)
  if t in ('style','script'):self.skip+=1
  if t=='script':self.script_tags.append({'line':self.getpos()[0],**d})
  for k in ('href','src'):
   if k in d:self.links.append({'tag':t,'attribute':k,'value':d[k],'line':self.getpos()[0]})
  if t=='tr':self.row={'line':self.getpos()[0],'text':[]}
 def handle_endtag(self,t):
  if t in ('style','script'):self.skip=max(0,self.skip-1)
  if t=='tr' and self.row is not None:self.trs.append({'line':self.row['line'],'text':' '.join(self.row['text'])});self.row=None
 def handle_data(self,d):
  v=' '.join(d.split())
  if v and not self.skip:self.text.append({'line':self.getpos()[0],'text':v})
  if v and self.row is not None:self.row['text'].append(v)
base=Path(__file__).parent;allout={}
for name in ('UD_v1.5.html','UD-Public_v1.5.html'):
 p=base/'sources'/name;b=p.read_bytes();s=b.decode('utf8');a=Scan();a.feed(s)
 nodes=[]
 for line,raw in enumerate(s.splitlines(),1):
  if re.match(r"\s*\{id:'",raw):
   def field(k):
    m=re.search(r"\b"+k+r":'((?:\\.|[^'])*)'",raw);return m.group(1) if m else None
   dep=re.search(r"depends:\[([^]]*)\]",raw)
   if dep:nodes.append({'id':field('id'),'label':field('label'),'maturity':field('maturity'),'depends':re.findall(r"'([^']*)'",dep.group(1)),'line':line})
 ids={n['id'] for n in nodes}
 norm=unicodedata.normalize('NFKC',unescape(s)).casefold()
 terms={k:[i for i,l in enumerate(norm.splitlines(),1) if re.search(v,l)] for k,v in {'THM534':'534','pentagon':'pentagon','pentachoron':'pentachor','hop_probability':'hop.{0,20}probab','action_unit':'action.{0,8}unit','raw_dataset':r'\.(?:csv|npy|npz|zip|pdf|tex)\b'}.items()}
 d={'source_path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'size_bytes':len(b),'text_records':a.text,'links':a.links,'scripts':a.script_tags,'nodes':nodes,'dangling_dependencies':sorted({x for n in nodes for x in n['depends'] if x not in ids}),'audit_rows':[r for r in a.trs if re.search(r'\bT[23]\.\d+',r['text'])],'literal_scans':terms,'extractor_mode':'static HTML/parser + declarative node regex; no JS or remote assets executed'}
 (base/(name+'.extracted.json')).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n');allout[name]=d
 if nodes:
  assert len(ids)==len(nodes)
  (base/(name+'.graph.json')).write_text(json.dumps({'nodes':nodes,'edges':[{'from':dep,'to':n['id']} for n in nodes for dep in n['depends']]},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({n:{'bytes':d['size_bytes'],'nodes':len(d['nodes']),'dangling':d['dangling_dependencies'],'audit_rows':len(d['audit_rows']),'scan_counts':{k:len(v) for k,v in d['literal_scans'].items()},'nonfragment_links':[x['value'] for x in d['links'] if not x['value'].startswith('#')]} for n,d in allout.items()},indent=2))
