"""Exact K4 window witness; a prepared lookup, not a native RSP decoder."""
from fractions import Fraction as Q
from itertools import combinations
from dataclasses import asdict
from rsp1 import State,transition,available_stock

def transpose(A):return list(map(list,zip(*A)))
def multiply(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def apply(A,x):return tuple(sum(a*b for a,b in zip(row,x)) for row in A)
def norm2(x):return sum(a*a for a in x)

def k4_generator():
    simplices=[list(combinations(range(4),k+1)) for k in range(4)]
    sizes=list(map(len,simplices));offsets=[0,4,10,14]
    B=[]
    for k in range(1,4):
        matrix=[[Q(0) for _ in simplices[k]] for _ in simplices[k-1]]
        for j,s in enumerate(simplices[k]):
            for i in range(len(s)):matrix[simplices[k-1].index(s[:i]+s[i+1:])][j]=Q((-1)**i)
        B.append(matrix)
    A=[[Q(0) for _ in range(15)] for _ in range(15)]
    for k,matrix in enumerate(B):
        for i in range(sizes[k]):
            for j in range(sizes[k+1]):
                A[offsets[k]+i][offsets[k+1]+j]=-matrix[i][j]
                A[offsets[k+1]+j][offsets[k]+i]=matrix[i][j]
    return A,B

def hd_pair_receipt(x):
    edges=list(combinations(range(4),2))
    edge_witness={e:x[4+j]**2*(x[e[0]]**2+x[e[1]]**2) for j,e in enumerate(edges)}
    pairs=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
    values=tuple(sum(edge_witness[e] for e in pair) for pair in pairs)
    return {'R_HD':[str(v) for v in values],'L_HD':[int(v>0) for v in values]}

def quarter_turn_witness():
    A,B=k4_generator();v=tuple(map(Q,[1,-1]+[0]*13));u=tuple(a/2 for a in apply(A,v))
    assert apply(A,v)==tuple(2*a for a in u) and apply(A,u)==tuple(-2*a for a in v)
    plane=[v,u,tuple(-a for a in v),tuple(-a for a in u)]
    result={'sample_delta':'pi/4 in native parameter','native_period_steps':4,'native_norm2':'2',
      'native_states':[{'label':label,'coordinates':[str(a) for a in x],**hd_pair_receipt(x)} for label,x in zip(['v','u','−v','−u'],plane)],
      'branches':{},'physical_promotion':0,'scope':'Prepared finite-window lookup chosen from an RSP trace. It fails the exact global factor contract at wrap.'}
    for branch in ['C','H']:
        s0=State((1,0,0),(0,0,0),(0,0,0),(1,0,0),branch=branch)
        s1=transition(s0)['state'];s2=transition(s1)['state'];assert transition(s2)['state']==s2
        decoded=[s0,s1,s2,s2];rows=[]
        for i,s in enumerate(decoded):
            desired=transition(s)['state'];decoded_successor=decoded[(i+1)%4]
            rows.append({'native_state':result['native_states'][i]['label'],'native_successor':result['native_states'][(i+1)%4]['label'],
              'decoded_state':asdict(s),'rsp_successor':asdict(desired),'decoded_native_successor':asdict(decoded_successor),
              'intertwines':desired==decoded_successor,'decoded_available_stock':available_stock(s),
              'rsp_response':transition(s)['event']})
        assert [r['intertwines'] for r in rows]==[True,True,True,False]
        result['branches'][branch]=rows
    return result

if __name__=='__main__':
    from pathlib import Path
    import json
    P=Path(__file__).parent/'dist/sources/hodge-rsp-v0.1'
    (P/'HODGE_RSP_QUARTER_TURN_WITNESS_v0.1.json').write_text(json.dumps(quarter_turn_witness(),indent=2)+'\n')
    print('Exact quarter-turn window: three matching edges; wrap mismatch on both branches.')
