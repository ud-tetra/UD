"""Source-bound dyadic96 actions for the fixed weighted UD observation map.

Requires the separately built c30_action.cpp executable and regenerated OPERATOR.txt.
This is a slow reference oracle, not a claim of full8192-decoder execution.
"""
from pathlib import Path
import hashlib,subprocess,tempfile
OPERATOR_SHA256='cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950'
class SourceActions:
 def __init__(self,operator,executable):
  self.operator=Path(operator).resolve();self.executable=Path(executable).resolve()
  if hashlib.sha256(self.operator.read_bytes()).hexdigest()!=OPERATOR_SHA256:raise ValueError('operator differs from certified source bytes')
 def _apply(self,mode,values,n,radius):
  values=list(values)
  if len(values)!=n or any(type(x)is not int for x in values):raise ValueError('wrong dyadic96 dimensions/type')
  if sum(x*x for x in values)>(radius*2**96)**2:raise ValueError('input outside certified domain')
  with tempfile.TemporaryDirectory(prefix='ud-action-')as d:
   a=Path(d)/'input.txt';b=Path(d)/'output.txt';a.write_text(''.join(str(x)+'\n'for x in values))
   subprocess.run([str(self.executable),str(self.operator),mode,str(a),str(b)],check=True,stdout=subprocess.DEVNULL)
   out=list(map(int,b.read_text().split()))
  if len(out)!=(253952 if mode=='forward' else 2640):raise ValueError('incorrect output shape')
  return out
 def forward(self,x):return self._apply('forward',x,2640,2048)
 def adjoint(self,y):return self._apply('adjoint',y,253952,2049)
 def normal(self,x):return self.adjoint(self.forward(x))
