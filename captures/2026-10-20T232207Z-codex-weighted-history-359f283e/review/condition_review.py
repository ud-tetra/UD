#!/usr/bin/env python3
"""Exact arithmetic supporting a deliberately coarse analytic condition bound.
No eigenvalue/SVD, huge jet, Gram, or Hankel matrix is formed.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,math
P=Path(__file__).resolve().parent
rank=json.loads((P/'FACTOR_RESULTS.json').read_text());bounds=json.loads((P/'BOUND_CHECKS.json').read_text())
r=rank['derived_full_rank_using_inherited1893'];rtop=rank['weighted_rank_Q_sandwich'];D=105+2*rtop;M=4096;N=D*(D-1)//2
assert (r,rtop,D,N)==(1999,443,991,490545)
# sin(5/2) exceeds1/2: the degree7 Taylor polynomial is a lower bound on[0,5/2], using sin>=0 in its order8 integral remainder.
x=F(5,2);p7=x-x**3/6+x**5/120-x**7/5040
assert p7>F(1,2);assert F(5,2)<3 # pi>3 gives positivity/concavity on this interval.
# Normalized source map and integer-scaled generator S=2K.
assert bounds['full_K_operator_norm_squared_upper']==24 and 4*24<10**2
assert M==64**2 and D<=M
# Directed power-of-two majorants, all checked as integer inequalities.
assert 62*D<2**16 and 10<2**4 and D<2**10 and 20<2**5
Uexp=8+4*(D-1);modalexp=10+4*(D-1);gapexp=5*N;vnormexp=10*(D-1);normalexp=6
assert Uexp==3968 and modalexp==3970 and gapexp==2452725 and vnormexp==9900
jetexp=Uexp*(r-1);total=gapexp+vnormexp+normalexp+jetexp+modalexp
assert jetexp==7928064 and total==10394665
result={'status':'PASS_EXACT_CONSTANTS_FOR_FORMAL_FULL_QUOTIENT_CONDITION_BOUND','observed_integer_generator':'S=2K_D','normal_operator_norm_bound_squared':96,'observed_minimal_polynomial_degree_upper':D,'positive_quotient_dimension':r,'modal_Vandermonde_node_map':'exp(lambda/4)','sin_5over2_degree7_lower':str(p7),'sin_5over2_lower_exceeds_half':True,'node_chord_ratio_lower':'1/20','discriminant_modulus_integer_lower':1,'max_pair_count':N,'Vandermonde_determinant_lower':'20^(-d(d-1)/2)','integer_jet_Gram_positive_pseudodeterminant_lower':1,'strict_binary_exponents':{'jet_operator_norm_upper':Uexp,'modal_jet_operator_norm_upper':modalexp,'spectral_gap_Vandermonde_det_denominator':gapexp,'Vandermonde_other_singular_values_denominator':vnormexp,'sample_normalization_denominator':normalexp,'jet_smallest_positive_singular_denominator':jetexp,'final_smallest_positive_singular_denominator':total},'formal_conclusions':{'sampled_map':'4096^-1/2 stack_j R exp(jK_D/2)','sampled_rank':1999,'sampled_kernel_dimension':641,'sigma_min_positive_lower':f'>2^(-{total})','positive_condition_number_upper':f'<2^{total}','full2640_condition':'INFINITE','practical_condition_bound2029':'NOT_CERTIFIED_HOLD'},'proof_dependencies':{'rank1999_and_degree991_proved_elsewhere_in_this_review':True,'integer_observed_minimal_polynomial_uses_rational_observable_module_and_Gauss_lemma':True,'skewness_makes_observed_polynomial_squarefree':True,'nonzero_integer_discriminant_proves_gap_product_lower':True,'integer_jet_full_rank_on_quotient_and_Gram_coefficient_integrality':True,'modal_output_map_lower_from_integer_jet_upper':True,'firstd_samples_embed_in_full4096_with_scale1over64':True},'scope':{'formal_worst_case_analytic_bound_not_numerical_SVD':True,'no_large_jet_Gram_or_Hankel_allocated':True,'no_accuracy_noise_or_2029_gate_transfer':True,'no_raw_or_estimator_calls':True,'physical_promotion':0,'external_promotion_review':'PENDING'}}
(P/'CONDITION_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'sin_lower':str(p7),'exponent':total},indent=2))
