"""Exact selection/nonselection witnesses using retained freshly generated maps."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import subdivision_metric as sm

ROOT=Path(__file__).resolve().parent
S,R,Q=sm.S,sm.R,sm.add(sm.eye(149),sm.multiply(sm.S,sm.R),-1)
RR=sm.multiply(sm.transpose(R),R);QQ=sm.multiply(sm.transpose(Q),Q)
def scaled(a,c):return [[c*v for v in row] for row in a]
def selection_cases():
    i=sm.NEW.index((3,));cases=[]
    for w in [F(1,2),F(1),F(2)]:
        h=sm.add(RR,scaled(QQ,w));hs=sm.multiply(h,S)
        assert hs==sm.transpose(R)
        assert sm.multiply(sm.transpose(S),hs)==sm.eye(15)
        induced=sm.multiply(sm.transpose(S),h);assert induced==R
        assert sm.multiply(induced,sm.BP)==sm.multiply(sm.B,induced)
        assert sm.add(sm.multiply(sm.transpose(induced),induced),sm.multiply(sm.transpose(Q),sm.multiply(h,Q)))==h
        assert h[i][i]==F(1,2)+w*F(3,2)
        obs=[]
        for lam in [F(0),F(1,2),F(1)]:
            k=sm.add(RR,scaled(QQ,lam*w))
            assert sm.multiply(sm.transpose(S),sm.multiply(k,S))==sm.eye(15)
            # K and H-K are sums of positive Gram matrices for 0<=lambda<=1.
            assert sm.add(h,k,-1)==scaled(QQ,(1-lam)*w)
            value=k[i][i];fraction=value/h[i][i]
            assert value==F(1,2)+lam*w*F(3,2)
            assert sm.multiply(k,Q)==sm.zero(149,149) if lam==0 else any(v for row in sm.multiply(k,Q) for v in row)
            obs.append({'lambda':str(lam),'value':str(value),'fraction':str(fraction),'complement_blind':lam==0})
        cases.append({'complement_weight':str(w),'fine_barycenter_norm_squared':str(h[i][i]),'observable_cases':obs})
    return cases
def verify():
    assert sm.multiply(R,S)==sm.eye(15)
    assert sm.multiply(Q,Q)==Q and sm.multiply(R,Q)==sm.zero(15,149)
    cases=selection_cases()
    # Complete source-region effect partition, with separate retained complement.
    effects=[]
    for row in R:
        k=[[x*y for y in row] for x in row];effects.append(k)
        assert sm.multiply(k,Q)==sm.zero(149,149)
    total=sm.zero(149,149)
    for k in effects:total=sm.add(total,k)
    assert total==RR and sm.add(total,QQ)==sm.add(RR,QQ)
    # A fully prepared code and a complement witness have different receipts.
    vertex=sm.NEW.index((3,));fine=[F(j==vertex) for j in range(149)]
    coarse=[sum(v*x for v,x in zip(row,fine)) for row in R]
    residual=[sum(v*x for v,x in zip(row,fine)) for row in Q]
    assert sum(x*x for x in coarse)==F(1,2) and sum(x*x for x in residual)==F(3,2)
    fractions=[c*c/F(2) for c in coarse]+[sum(z*z for z in residual)/F(2)]
    assert sum(fractions)==1 and fractions[0]==fractions[1]==F(1,8) and fractions[-1]==F(3,4)
    # Universal diagonal-H contradiction follows from disjoint raising supports.
    flag=sm.NEW.index((2,3));old_vertex=sm.OLD.index((0,))
    assert sm.BP[sm.NEW.index((1,))][flag]==0
    coarse_raise=sm.multiply(S,sm.transpose(sm.B));assert coarse_raise[flag][old_vertex]==1
    # Recover each source simplex stock derivative and Hasse signed current.
    a=sm.add(sm.transpose(sm.B),sm.B,-1)
    for oldstate in [[F(k==j) for k in range(15)] for j in range(15)]+[[F(k-7,8) for k in range(15)]]:
        d=[sum(v*x for v,x in zip(row,oldstate)) for row in a]
        rates=[2*c*v for c,v in zip(oldstate,d)];flux=[F(0)]*15
        for lo in range(15):
            for hi in range(15):
                if sm.B[lo][hi]:
                    current=2*sm.B[lo][hi]*oldstate[lo]*oldstate[hi]
                    flux[lo]-=current;flux[hi]+=current
        assert rates==flux and sum(rates)==0
    return {'status':'PASS','version':'0.1','reading_edition':'0.12','physical_promotion':0,
      'scope':'Exact conditional selector/classification; sources do not adopt selector axioms. Constructor-team only.',
      'metric_witnesses':cases,'fixed_carrier_source_metric':'I in declared orthonormal simplex coordinates',
      'cross_refinement_metric_source_selection':'OPEN','full_metric_classification':'Chain retraction plus positive complement pairing',
      'conditional_metric':'H*=R^T G R+Q^T Q, after explicit unit residual calibration and orthogonal split',
      'conditional_observable':'K_U=R^T D_U R, after positive code calibration and complement blindness',
      'complete_effect_count':16,'fine_barycenter_complete_fractions':list(map(str,fractions)),
      'coarse_current_replays':16,'diagonal_metric_no_go':{'old_vertex':0,'fine_flag':[2,3],'weighted_raise_coefficient':'0 for any positive diagonal H','transported_raise_coefficient':'1'},
      'source_selected_axioms':False,'independent_human_review':'PENDING',
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'subdivision_checker_sha256':hashlib.sha256(Path(sm.__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
    receipt=verify();p=ROOT/'dist/sources/metric-selection-v0.1/METRIC_SELECTION_ROOT_VERIFICATION_v0.1.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'metric_witnesses':len(receipt['metric_witnesses']),'complete_effect_count':receipt['complete_effect_count'],'source_selected_axioms':False,'physical_promotion':0}))
