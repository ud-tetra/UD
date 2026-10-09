"""Exact joint row closure for the Q173 face masks and extended Q167 edge masks."""
import contextlib,functools,io,json,runpy
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    m=runpy.run_path(str(Path(__file__).with_name('verify_lower.py')))
rr=m['rr'];mul=m['mul'];A=m['A'];gate=m['gate'];flat=m['flat'];cells=m['m']['m']['m']['cells']
Z=m['zeros'];add=m['add'];R6=m['m']['m']['R'];R14=m['R'];tr=m['tr'];I=m['I'];ix=m['ix'];Q=m['m']['m']['m']['Q']
faces=[f for f in flat if len(f)==3];edges=[e for e in flat if len(e)==2];verts=[v for v in flat if len(v)==1]
F={f:functools.reduce(add,[gate(f,t) for t in cells if set(f)<set(t)],Z(23,23)) for f in faces}
E={e:functools.reduce(add,[gate(v,e) for v in verts if set(v)<set(e)],Z(23,23)) for e in edges}
checks={}
def ck(name,result):
    checks[name]=bool(result)
    assert result,name
def close(label,gs):
    O,_=rr(R6);seq=[len(O)]
    while True:
        T,_=rr(O+sum([mul(O,g) for g in gs],[]))
        if len(T)==len(O):break
        O=T;seq.append(len(O))
    O,piv=rr(O);hs=[]
    for j,g in enumerate(gs):
        OG=mul(O,g);H=[[row[k] for k in piv] for row in OG]
        ck(label+'_intertwiner_'+str(j),mul(H,O)==OG);hs.append(H)
    return {'ranks':seq,'R':O,'H':hs}
families={'Q173_seven_face_masks':close('faces',[A]+list(F.values())),
          'extended_Q167_nine_edge_masks':close('edges',[A]+list(E.values())),
          'combined_typed_masks':close('combined',[A]+list(F.values())+list(E.values()))}
ck('face_ranks',families['Q173_seven_face_masks']['ranks']==[6,10,14])
ck('edge_ranks',families['extended_Q167_nine_edge_masks']['ranks']==[6,8,16,22])
ck('combined_ranks',families['combined_typed_masks']['ranks']==[6,12,20,22])
ck('face_space_equals_previous14',len(rr(families['Q173_seven_face_masks']['R']+R14)[0])==14)
ones=[[Q(int(len(t)==1))] for t in flat]
ck('uniform_vertex_A_null',mul(A,ones)==Z(23,1))
ck('uniform_vertex_masks_null',all(mul(g,ones)==Z(23,1) for g in list(F.values())+list(E.values())))
O22=families['combined_typed_masks']['R']
ck('uniform_vertex_unseen',mul(O22,ones)==Z(22,1))
ck('uniform_only_missing',len(rr(O22)[0])==22)
# Contrast with a single-end vertex-edge switch. This is a different policy.
Vsingle=gate((0,),(0,1))
ck('single_end_exposes_uniform',mul(O22,mul(Vsingle,ones))!=Z(22,1))
# Each whole-edge mask annihilates uniform vertices, because its two endpoints have opposite signs.
ck('each_edge_mask_annihilates_uniform',all(mul(g,ones)==Z(23,1) for g in E.values()))
ck('seven_face_masks',len(F)==7)
ck('nine_edge_masks',len(E)==9)
out={'status':'development; exact mathematical conditional; no physical promotion',
     'carrier':'<0123,0124>, 23 real coordinates, increasing vertex orientation, A=B^T-B',
     'scope':'all real initial states; all prescribed independent per-face and per-edge mask settings; selected cells and shared face',
     'families':families,'checks':checks,'new_passed':sum(checks.values()),
     'prior_passed':{'baseline':18,'shared':21,'outer':28,'independent_incidence_stress':83},
     'uniform_vertex':ones}
Path(__file__).with_name('results_source_masks.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({'rank_sequences':{k:v['ranks'] for k,v in families.items()},
                  'new_checks':out['new_passed'],'prior_checks':sum(out['prior_passed'].values())},indent=2))
