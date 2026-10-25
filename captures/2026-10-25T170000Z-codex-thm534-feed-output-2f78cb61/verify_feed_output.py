#!/usr/bin/env python3
"""Fresh exact port-completion controls; added couplings explicitly nonnative."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import json

SIMPLICES=[s for k in range(1,5) for s in combinations(range(4),k)]
def norm(x):return sum(v*v for v in x)
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def sign(v):return (-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
def boundary(k):
    lo=list(combinations(range(4),k));hi=list(combinations(range(4),k+1));B=[[Q(0)]*len(hi) for _ in lo]
    for j,s in enumerate(hi):
        for i in range(k+1):B[lo.index(s[:i]+s[i+1:])][j]=Q((-1)**i)
    return B
B1=boundary(1);B2=boundary(2);B3=boundary(3)
def generator(h):
    A=[[Q(0)]*15 for _ in range(15)]
    for B,lo,hi in [(B1,0,4),(B2,4,10),(B3,10,14)]:
        for i,row in enumerate(B):
            for j,d in enumerate(row):
                a=d*(h[i] if lo==10 else 1);A[lo+i][hi+j]=-a;A[hi+j][lo+i]=a
    return A
def solve(A,b):
    rows=[list(row)+[v] for row,v in zip(A,b)]
    for k in range(len(b)):
        p=next(i for i in range(k,len(b)) if rows[i][k]);rows[k],rows[p]=rows[p],rows[k]
        d=rows[k][k];rows[k]=[v/d for v in rows[k]]
        for i in range(len(b)):
            if i!=k and rows[i][k]:
                d=rows[i][k];rows[i]=[a-d*v for a,v in zip(rows[i],rows[k])]
    return [row[-1] for row in rows]
def cayley(x,A):
    n=len(x);L=[[Q(i==j)-A[i][j]/2 for j in range(n)] for i in range(n)]
    rhs=[x[i]+sum(A[i][j]*x[j] for j in range(n))/2 for i in range(n)]
    return solve(L,rhs)
def skew_apply(v,w,x):return [a*dot(v,x)-b*dot(w,x) for a,b in zip(w,v)]
def restore(v,w,x):
    N=norm(v);d=dot(v,w);assert N==norm(w)>0 and N+d>0
    Kx=skew_apply(v,w,x);K2x=skew_apply(v,w,Kx)
    return [a+b/N+c/(N*(N+d)) for a,b,c in zip(x,Kx,K2x)]
def native_receipts(x,y,A):
    mid=[(a+b)/2 for a,b in zip(x,y)];delta=[Q(0)]*15
    for i in range(15):
        for j in range(i+1,15):
            J=2*A[j][i]*mid[i]*mid[j];delta[i]-=J;delta[j]+=J
    assert delta==[b*b-a*a for a,b in zip(x,y)]
def reset_receipts(v,w):
    N=norm(v);d=dot(v,w);mid=[(a+b)/2 for a,b in zip(v,w)];delta=[Q(0)]*16
    S=[[2*(w[i]*v[j]-v[i]*w[j])/(N+d) for j in range(16)] for i in range(16)]
    for i in range(16):
        for j in range(i+1,16):
            J=2*S[j][i]*mid[i]*mid[j];delta[i]-=J;delta[j]+=J
    assert delta==[b*b-a*a for a,b in zip(v,w)]
    assert cayley(v,S)==w
    return S
def action(p):
    T=[]
    for s in SIMPLICES:
        v=tuple(p[i] for i in s);T.append((SIMPLICES.index(tuple(sorted(v))),sign(v)))
    return T
def transform(x,T):
    y=[Q(0)]*15
    for i,(j,s) in enumerate(T):y[j]=s*x[i]
    return y

def main():
    completed=0;covariance=0;cycle_controls=0;feed_errors=0;random_controls=0;coupling_gaps=[];examples=[]
    for h in product((0,1),repeat=4):
        k=sum(h)
        if k in (0,4):continue
        u=[sum(B2[i][f]*h[f]*B3[f][0] for f in range(4)) for i in range(6)]
        x=[Q(0)]*4+u+[Q(0)]*5;A=generator(h);y=cayley(x,A);native_receipts(x,y,A)
        c=y[14];p=c*c;N=norm(x);assert p>0 and norm(y)==N
        z=y.copy();z[14]=Q(0);v=z+[c];w=x+[Q(0)]
        assert norm(v)==norm(w)==N
        assert restore(v,w,v)==w;S=reset_receipts(v,w)
        assert norm(z)==N-p and norm(w[:15])-norm(z)==p
        # The restoration generator is not confined to native incidence contacts.
        native_all_open=generator([1]*4)
        missing=[(i,j) for i in range(15) for j in range(i+1,15) if S[i][j] and not native_all_open[i][j]]
        assert missing;coupling_gaps.append(len(missing))
        completed+=1
        for m in (1,2,4,8):
            worker=x.copy();outputs=[];unused_feeds=[c]*m;spent=[]
            for _ in range(m):
                a=cayley(worker,A);out=a[14];a[14]=Q(0)
                b=restore(v,w,a+[unused_feeds.pop()]);worker=b[:15];spent.append(b[15]);outputs.append(out)
                assert worker==x and b[15]==0
            assert norm(worker)+norm(outputs)+norm(spent)==N+m*p
            assert norm(outputs)==m*p and not unused_feeds;cycle_controls+=1
        for error in (-c,Q(1,100),-Q(1,100)):
            wrong=restore(v,w,z+[c+error]);diff=[a-b for a,b in zip(wrong,w)]
            assert norm(diff)==error*error
            if error==-c:assert wrong[:15]!=x and norm(wrong)==N-p
            feed_errors+=1
        for n in range(4):
            q=[Q(((i+2)*(n+3))%11-5,i%3+1) for i in range(17)]
            before=norm(q);field=cayley(q[:15],A);feed=q[15];out=q[16]
            # Proper quarter turn on the native core and abstract output port.
            field[14],out=-out,field[14]
            reset=restore(v,w,field+[feed]);result=reset[:15]+[reset[15],out]
            assert norm(result)==before;random_controls+=1
        for perm in permutations(range(4)):
            T=action(perm);hp=[0]*4
            for i,a in enumerate(h):hp[T[10+i][0]-10]=a
            xp=transform(x,T);yp=cayley(xp,generator(hp));assert yp==transform(y,T)
            cp=yp[14];zp=yp.copy();zp[14]=Q(0)
            assert restore(zp+[cp],xp+[Q(0)],zp+[cp])==xp+[Q(0)]
            assert cp==T[14][1]*c;covariance+=1
        if h==(1,0,0,0):
            assert S[4][12]==Q(-1,3) and native_all_open[4][12]==0
            examples.append({'mask':list(h),'worker_stock':str(N),'feed_amplitude':str(c),'feed_debit_and_output_stock':str(p),
                'reset_generator_edge01_face023_entry':'-1/3; native incidence is zero',
                'nonnative_worker_contact_pairs':[list(pair) for pair in missing]})
    assert completed==14 and covariance==336
    report={'status':'PASS','arithmetic':'exact fractions.Fraction','physical_promotion':0,
      'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING','matched_native_masks':completed,
      'matched_cycle_length_controls':cycle_controls,'signed_covariance_controls':covariance,
      'feed_error_controls':feed_errors,'global_norm_controls_on_generic_inputs':random_controls,
      'minimum_nonnative_worker_contact_pairs':min(coupling_gaps),'examples':examples,
      'added_abstract_ports':2,'source_status':'KINEMATIC_COMPLETION_ONLY; PORT_AND_RESTORATION_GENERATORS_NOT_NATIVE_DERIVED',
      'balance':'worker restored, output stock equals feed debit, feed emptied',
      'limits':['Prepared matched feed and empty output are external resources',
        'Fixed template does not restore every unknown input state',
        'No autonomous mask control, native compilation or record reset supplied',
        'No action, energy or particle bridge']}
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
