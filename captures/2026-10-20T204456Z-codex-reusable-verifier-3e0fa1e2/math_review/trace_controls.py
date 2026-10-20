"""Independent exact rational residuals versus sufficient-statistic expansions."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent

def T(A):return list(map(list,zip(*A)))
def mm(A,B):return [[sum(x*y for x,y in zip(row,col))for col in zip(*B)]for row in A]
def norm2(A):return sum(x*x for row in A for x in row)
def subtract(A,B):return [[x-y for x,y in zip(ar,br)]for ar,br in zip(A,B)]
def scale(A,d):return [[F(x,2**d)for x in row]for row in A]
def diag_right(A,s):return [[x*t for x,t in zip(row,s)]for row in A]
def check_fixture(N,U,V,s,bN,bU,bV,bS):
 M=mm(T(N),N);K=mm(T(N),U);A=mm(T(U),U);B=mm(T(V),V)
 cross=sum(K[i][j]*V[i][j]*s[j]for i in range(len(V))for j in range(len(s)))
 nv=mm(N,V);uS=diag_right(U,s);vS=diag_right(V,s)
 assert cross==sum(x*y for xr,yr in zip(nv,uS)for x,y in zip(xr,yr))
 assert cross==sum(x*y for xr,yr in zip(K,vS)for x,y in zip(xr,yr))
 q=len(s);trace=sum(mm(mm(T(V),M),V)[j][j]for j in range(q))
 assert trace==norm2(nv)
 kF=max(bN+bV,bU+bS);aF=2**(kF-bN-bV);bF=2**(kF-bU-bS)
 kG=max(bN+bU,bV+bS);aG=2**(kG-bN-bU);bG=2**(kG-bV-bS)
 numF=aF*aF*trace-2*aF*bF*cross+bF*bF*sum(s[j]**2*A[j][j]for j in range(q))
 numG=aG*aG*norm2(K)-2*aG*bG*cross+bG*bG*sum(s[j]**2*B[j][j]for j in range(q))
 assert numF>=0 and numG>=0
 directF=subtract(mm(scale(N,bN),scale(V,bV)),diag_right(scale(U,bU),[F(x,2**bS)for x in s]))
 directG=subtract(mm(T(scale(N,bN)),scale(U,bU)),diag_right(scale(V,bV),[F(x,2**bS)for x in s]))
 assert F(numF,2**(2*kF))==norm2(directF)
 assert F(numG,2**(2*kG))==norm2(directG)
 return {'forward_square':[str(norm2(directF).numerator),str(norm2(directF).denominator)],'adjoint_square':[str(norm2(directG).numerator),str(norm2(directG).denominator)],'cross':str(cross),'kF':kF,'kG':kG,'scales':[aF,bF,aG,bG]}

def main():
 freeze=json.loads((P/'TRACE_FREEZE.json').read_text())
 for n,h in freeze['files_sha256'].items():assert hashlib.sha256((P/n).read_bytes()).hexdigest()==h
 N=[[2,-1,3],[0,4,-2],[1,3,1],[-2,0,5]];U=[[1,2],[-1,3],[2,0],[4,-2]];V=[[2,-1],[3,4],[-2,1]];s=[3,2]
 rows=[]
 for bN,bU,bV,bS in [(0,0,0,0),(1,2,3,1),(4,1,0,2),(0,5,2,3),(5,0,4,1)]:
  rows.append({'id':'unequal_signed_q2_'+str((bN,bU,bV,bS)),'pass':True,**check_fixture(N,U,V,s,bN,bU,bV,bS)})
 for n in range(1,5):
  N=[[2,0],[0,0]];U=[[1],[0]];V=[[1],[0]];s=[2]
  rows.append({'id':'exact_diagonal_q1_scale'+str(n),'pass':True,**check_fixture(N,U,V,s,n,n,n,n)})
 # Independent packed symmetric norm accounting.
 M=[[1,2,-3],[2,4,5],[-3,5,6]];packed=sum(M[i][i]**2 for i in range(3))+2*sum(M[i][j]**2 for i in range(3)for j in range(i))
 assert packed==norm2(M)
 rows.append({'id':'symmetric_packed_offdiagonal_weight2','pass':True})
 out={'status':'PASS_INDEPENDENT_TRACE_IDENTITIES_AGAINST_EXPLICIT_RATIONAL_RESIDUALS','rows':rows,'count':len(rows),'new_fits':0,'physical_promotion':0}
 with(P/'TRACE_CONTROLS.json').open('x')as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({'status':out['status'],'count':len(rows)}))
if __name__=='__main__':main()
