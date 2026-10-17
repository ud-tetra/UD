"""Exact integer Hankel actions, energy and proof cores; never materialize H.

The record is Y[a,k,c]/data_den; H[(i,c),(j,a)]=Y[a,i+j,c]/(M*data_den).
Python-FLINT polynomial products are exact integer arithmetic, not floating FFTs.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import mmap
import numpy as np
from flint import fmpz_poly,fmpz_mat

def file_sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as s:
  for b in iter(lambda:s.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

class HankelRecord:
 def __init__(self,Y,data_den):
  if len(Y.shape)!=3 or Y.shape[1]%2!=1 or Y.dtype.kind not in 'iu':raise ValueError('Requires integer [preparation,odd time count,channel] array')
  if type(data_den) is not int or data_den<=0:raise ValueError('Positive exact denominator required')
  self.Y=Y;self.p,self.n,self.c=Y.shape;self.M=(self.n+1)//2;self.den=self.M*data_den
  self.rows=self.M*self.c;self.cols=self.M*self.p
 def action(self,vec,transpose=False):
  n_in=self.c if transpose else self.p;n_out=self.p if transpose else self.c
  x=np.asarray(vec)
  if x.shape!=(self.M*n_in,) or x.dtype.kind not in 'iu':raise ValueError('Integer vector shape/dtype mismatch')
  x=x.reshape(self.M,n_in);out=np.empty((self.M,n_out),dtype=object);out.fill(0)
  polys=[]
  for v in range(n_in):
   z=x[:,v]
   polys.append(fmpz_poly([int(t) for t in z[::-1]]) if np.any(z) else None)
  for aa in range(self.p):
   for cc in range(self.c):
    v=cc if transpose else aa;u=aa if transpose else cc
    if polys[v] is None:continue
    data=self.Y[aa,:,cc]
    if not np.any(data):continue
    product=fmpz_poly([int(t) for t in data])*polys[v]
    for i in range(self.M):out[i,u]+=product[i+self.M-1]
  return out.reshape(-1),self.den
 def energy(self):
  total=0
  for k in range(self.n):
   # Python integers avoid int64 squaring/accumulation overflow.
   z=self.Y[:,k,:].reshape(-1).tolist();weight=min(k+1,self.n-k,self.M)
   total+=weight*sum(int(t)*int(t) for t in z)
  return F(total,self.den**2)
 def selector_cores(self,selected):
  """Exact sparse shortcut for coordinate candidates. Dense cases use disk_cores.
  Storage depends on nonzeros of selected columns, not the full Hankel matrix.
  """
  if len(set(selected))!=len(selected) or any(j<0 or j>=self.cols for j in selected):raise ValueError('Invalid coordinate basis')
  r=len(selected);by_row={}
  for jj,index in enumerate(selected):
   j,aa=divmod(index,self.p);z=self.Y[aa,j:j+self.M,:]
   ii,cc=np.nonzero(z)
   for i,c in zip(ii.tolist(),cc.tolist()):by_row.setdefault(i*self.c+c,[]).append((jj,int(z[i,c])))
  gram={}
  for entries in by_row.values():
   for j,x in entries:
    for k,y in entries:
     if j<=k:gram[j,k]=gram.get((j,k),0)+x*y
  # Upper-triangle sparse entries; both Gram matrices are exact.
  return {(i,i):1 for i in range(r)},1,gram,self.den**2

def release_map(array):
 mapped=getattr(array,'_mmap',None)
 if mapped is not None and hasattr(mapped,'madvise'):mapped.madvise(mmap.MADV_DONTNEED)

def gram_rows(nrows,ncols,row_provider,block_rows=64,release=None):
 """Exact integer Gram with bounded row-block storage."""
 G=fmpz_mat(ncols,ncols)
 for start in range(0,nrows,block_rows):
  stop=min(start+block_rows,nrows)
  T=fmpz_mat([row_provider(i) for i in range(start,stop)])
  if release:release()
  G+=T.transpose()*T
 return G

def disk_cores(record,V,c_path,v_den,block_rows=64):
 """Production proof path for a dense candidate right basis.

 V is an int64 memory-mapped [H.cols,r] array representing V/v_den.
 C=H(V/v_den) is written in column order with signed128-bit numerators.
 Exact row-block Gram accumulation keeps RAM independent of H.rows*H.cols.
 The caller supplies a newc_path; existing files are never overwritten.
 """
 if V.ndim!=2 or V.shape[0]!=record.cols or V.dtype.kind!='i' or V.dtype.itemsize!=8:raise ValueError('V must be an int64 candidate array')
 if type(v_den) is not int or v_den<=0:raise ValueError('Positive candidate denominator required')
 r=V.shape[1]
 if r<1:raise ValueError('Empty candidate basis')
 for start in range(0,V.shape[0],512):
  z=V[start:start+512,:]
  if int(z.min())<-(2**60) or int(z.max())>2**60:raise ValueError('Candidate numerator bound exceeded')
  release_map(V)
 if int(record.Y.min())<-(2**49) or int(record.Y.max())>2**49:raise ValueError('Frozen history amplitude bound exceeded')
 # Full frozen dimensions give abs(C numerator)<2^127; enforce independently.
 with Path(c_path).open('xb') as stream:
  for j in range(r):
   column=np.empty(record.cols,dtype=np.int64)
   for start in range(0,record.cols,8192):
    column[start:start+8192]=V[start:start+8192,j];release_map(V)
   nums,den=record.action(column)
   for start in range(0,len(nums),4096):
    # to_bytes raises on overflow; no truncation, saturation or clipping.
    stream.write(b''.join(int(value).to_bytes(16,'little',signed=True) for value in nums[start:start+4096]))
   release_map(record.Y)
 gv=gram_rows(record.cols,r,lambda i:[int(t) for t in V[i,:]],block_rows,lambda:release_map(V))
 C=np.memmap(c_path,dtype='V16',mode='r',shape=(r,record.rows))
 gc=gram_rows(record.rows,r,lambda i:[int.from_bytes(C[j,i].tobytes(),'little',signed=True) for j in range(r)],block_rows,lambda:release_map(C))
 return gv,v_den**2,gc,(record.den*v_den)**2

def upper_entries(G,r):
 if isinstance(G,dict):return G.items()
 return (((i,j),int(G[i,j])) for i in range(r) for j in range(i,r))
