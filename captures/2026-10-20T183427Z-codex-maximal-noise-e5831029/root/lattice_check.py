"""Independent generating-function count and exact encoded-radius bounds."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,itertools
P=Path(__file__).resolve().parent
# |z_j|>=2 alone costs >=4 >9/4; otherwise every active coordinate costs1.
assert Q(9,4)<4 and Q(9,4)<3 and Q(9,4)>=2
coeff=[1,0,0]
for _ in range(62):coeff=[coeff[0],coeff[1]+2*coeff[0],coeff[2]+2*coeff[1]]
assert coeff==[1,124,7564] and sum(coeff)==7689
assert Q(2)*Q(1,2**48)**2/Q(3,2**49)**2==Q(8,9)
assert Q(4)*Q(1,2**48)**2/Q(3,2**49)**2==Q(16,9)>1
for z in itertools.product(range(-2,3),repeat=4):
 n=sum(x*x for x in z);rule=all(abs(x)<=1 for x in z)and sum(x!=0 for x in z)<=2
 assert(n<=Q(9,4))==rule
out={'status':'PASS_EXACT_LATTICE_CLASSIFICATION_AND_MAXIMAL_ENCODED_RADIUS','domain':'integer multiples of q relative to encoded computational nominal; not unknown true physical signal','dimension':62,'quantum':[1,2**48],'source_radius':[3,2**49],'squared_norm_integer_max':2,'counts_by_squared_norm':coeff,'pointwise_alphabet_size':7689,'max_encoded_radius_squared':[2,2**96],'max_radius_squared_fraction':[8,9],'single_two_quantum_coordinate_fraction':[16,9],'history_vector_count':303067,'all_pointwise_admissible_histories_count':'7689^303067','whole_history_estimator_success_claimed':False,'external_promotion_review':'PENDING','physical_promotion':0,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
with(P/'LATTICE_CHECK.json').open('x')as f:json.dump(out,f,indent=2);f.write('\n')
print(out['status'])
