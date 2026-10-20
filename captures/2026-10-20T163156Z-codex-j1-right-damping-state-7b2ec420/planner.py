"""Budgeted exact adaptive complete rectangle and frozen-grid next-state diagnostic."""
import sys
sys.dont_write_bytecode=True
import json,hashlib,copy
from pathlib import Path
from fractions import Fraction as F
import kernel as K
from rounding import bits,frombits,round64
HERE=Path(__file__).resolve().parent
def word_domain(lo,hi):
 first,last=bits(round64(lo)),bits(round64(hi))
 while F.from_float(frombits(first))<lo:first+=1
 while F.from_float(frombits(last))>hi:last-=1
 assert F.from_float(frombits(first-1))<lo<=F.from_float(frombits(first))<=F.from_float(frombits(last))<=hi<F.from_float(frombits(last+1))
 return first,last

def split_axis(box,words):
 wl,wu,gl,gu=box;wf,wt,gf,gt=words
 sw=4*(wu*wu+gu*gu)*(wu-wl)**2 if wf<wt else F(-1)
 sg=4*wu*wu*(gu-gl)**2 if gf<gt else F(-1)
 return 'omega' if sw>=sg else 'gamma'

def create_cover(contract):
 wl,wu=map(F,contract['complete_cover_domain']['omega']);gl,gu=map(F,contract['complete_cover_domain']['gamma']);wf,wt=word_domain(wl,wu);gf,gt=word_domain(gl,gu)
 nodes=[];leaves=[];budget=contract['finite_algorithm_budget'];target=F(contract['target']);calls=0
 def visit(box,words,depth):
  nonlocal calls
  idx=len(nodes);nodes.append(None)
  certificates=[K.certificate(sid,box) for sid in sorted(K.BANK)];calls+=len(certificates)
  cert=min(certificates,key=lambda x:(F(x['total_radius']),x['state']));node={'proof_box':list(map(str,box)),'word_box':list(words),'depth':depth}
  if F(cert['total_radius'])<=target:
   assert len(leaves)<budget['max_leaves'],'leaf budget exceeded'
   node.update(kind='leaf',certificate=cert);nodes[idx]=node;leaves.append(idx)
  else:
   assert depth<budget['max_depth'],'unresolved cell at depth budget'
   assert len(leaves)<budget['max_leaves'],'leaf budget exceeded'
   axis=split_axis(box,words);wl,wu,gl,gu=box;wf,wt,gf,gt=words
   if axis=='omega':
    assert wf<wt;cut=(wf+wt)//2;q=F.from_float(frombits(cut));assert wl<=q<wu
    left=visit((wl,q,gl,gu),(wf,cut,gf,gt),depth+1);right=visit((q,wu,gl,gu),(cut+1,wt,gf,gt),depth+1)
   else:
    assert gf<gt;cut=(gf+gt)//2;q=F.from_float(frombits(cut));assert gl<=q<gu
    left=visit((wl,wu,gl,q),(wf,wt,gf,cut),depth+1);right=visit((wl,wu,q,gu),(wf,wt,cut+1,gt),depth+1)
   node.update(kind='split',axis=axis,cut_word=cut,cut_rational=str(q),left=left,right=right);nodes[idx]=node
  return idx
 root=visit((wl,wu,gl,gu),(wf,wt,gf,gt),0)
 assert root==0 and len(leaves)<=budget['max_leaves'] and len(nodes)==2*len(leaves)-1
 count=sum((nodes[i]['word_box'][1]-nodes[i]['word_box'][0]+1)*(nodes[i]['word_box'][3]-nodes[i]['word_box'][2]+1) for i in leaves);assert count==(wt-wf+1)*(gt-gf+1)
 maxr=max(F(nodes[i]['certificate']['total_radius']) for i in leaves);assert maxr<=target
 return {'status':'PASS','classification':'DERIVED_CONDITIONAL_ADAPTIVE_FROZEN_STATE_COVER','domain':contract['complete_cover_domain'],'root':root,'nodes':nodes,'leaf_indices':leaves,'certification_calls':calls,'maximum_depth':max(nodes[i]['depth'] for i in leaves),'leaf_count':len(leaves),'accepted_pair_count':count,'uniform_total_radius':str(maxr),'target':str(target),'bank_sha256':hashlib.sha256((HERE/'BANK.json').read_bytes()).hexdigest(),'contract_sha256':hashlib.sha256((HERE/'CONTRACT.json').read_bytes()).hexdigest(),'physical_promotion':0}

def save_or_compare(name,result):
 p=HERE/name
 if p.exists():assert json.loads(p.read_text())==result;print('read-only replay matches '+name,flush=True)
 else:p.write_text(json.dumps(result,indent=2)+'\n')

def placement(contract):
 wl,wu=map(F,contract['placement_probe_domain']['omega']);gl,gu=map(F,contract['placement_probe_domain']['gamma']);rows=[]
 for i in range(9):
  w=wl+(wu-wl)*i/8
  for j in range(1,9):
   g=gl+(gu-gl)*j/8;bounds={sid:K.point_formula_bounds(sid,w,g) for sid in sorted(K.BANK)};score=min(x[0] for x in bounds.values());upper=min(x[1] for x in bounds.values())
   rows.append({'omega':str(w),'gamma':str(g),'formula_lower_by_state':{sid:str(v[0]) for sid,v in bounds.items()},'minimum_formula_lower':str(score),'minimum_model_upper':str(upper),'all_nine_transported_formulas_above_target':score>F(contract['target'])})
 selected=min(rows,key=lambda x:(-F(x['minimum_formula_lower']),F(x['omega']),F(x['gamma'])))
 return {'status':'PASS','classification':'CANDIDATE_PLACEMENT_WITH_SCOPED_FORMULA_DIAGNOSTIC','probe_count':len(rows),'rows':rows,'recommended_new_state':selected,'claim':'Finite-grid ranking of nine particular transported-upper formulas with fixed norm budgets. A formula lower above target obstructs these sufficient formulas, not actual accuracy or alternate certificates. No global optimum or new-state precision presumed.','physical_promotion':0}

def main():
 contract=json.loads((HERE/'CONTRACT.json').read_text());repo=HERE.parents[1]
 for d in contract['source_dependencies']:
  p=repo/d['path'];assert p.stat().st_size==d['size_bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==d['sha256']
 cover=create_cover(contract);save_or_compare('COVER.json',cover);probe=placement(contract);save_or_compare('PLACEMENT_RESULTS.json',probe)
 q=probe['recommended_new_state'];print('PASS complete rectangle cells='+str(cover['leaf_count'])+' radius='+str(float(F(cover['uniform_total_radius'])))+' next=('+q['omega']+','+q['gamma']+')',flush=True)

if __name__=='__main__':main()
