"""Three-page A4 manuscript of the scoped energy-clock-support theorem."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,PageBreak,Table,TableStyle,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
H=Path(__file__).resolve().parent
for name,file in [('Serif','DejaVuSerif.ttf'),('Bold','DejaVuSerif-Bold.ttf'),('Sans','DejaVuSans.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
body=ParagraphStyle('body',fontName='Serif',fontSize=10,leading=14.3,spaceAfter=9)
head=ParagraphStyle('head',fontName='Bold',fontSize=12,leading=17,spaceBefore=10,spaceAfter=8)
title=ParagraphStyle('title',fontName='Bold',fontSize=19,leading=24,spaceAfter=14)
small=ParagraphStyle('small',fontName='Sans',fontSize=8,leading=11,spaceAfter=8)
math=ParagraphStyle('math',fontName='Sans',fontSize=10,leading=17,alignment=1,spaceAfter=11,spaceBefore=4)
story=[]
def p(s):story.append(Paragraph(s,body))
def h(s):story.append(Paragraph(s,head))
def e(s):story.append(Paragraph(s,math))
def page():story.append(PageBreak())
story.append(Paragraph('Same-carrier energy,<br/>clock and support',title))
story.append(Paragraph('Theorem manuscript v0.1 · 21 October 2026 · Benjamin Walker Mayes<br/>AI-assisted constructor proof: Codex · Independent review pending',small))
p('<b>Abstract.</b> On the declared filled-tetrahedron active sector, energy and a primitive signed state recurrence identify A<sub>0</sub> times the native support a, rather than A<sub>0</sub> alone. We prove a normalization ambiguity preserving the apparatus trajectory, energy and clock. We also show why quadratic readouts can report half the state period, then give a finite action interval once independent support and clock certificates are supplied.')
p('<b>Status.</b> EXACT CONDITIONAL. Development - no registry entry. No apparatus or dataset is admitted; physical promotion remains 0.')
h('1. Declared same-carrier map')
p('On the nonzero active sector let A=2J, J<super>T</super>=-J and J<super>2</super>=-I. Native evolution is dx/ds=Ax, with a=‖x‖<super>2</super>&gt;0. Let z=Mx for injective M, physical time t=τ<sub>0</sub>s, and measured subsystem energy E(z)=z<super>T</super>Gz/2 with a calibrated baseline. The proposed physical map must satisfy both')
e('KM = MA/τ<sub>0</sub>, &nbsp; M<super>T</super>GM = (2A<sub>0</sub>/τ<sub>0</sub>)I.')
p('Here dz/dt=Kz on the invariant image. These conditions are hypotheses; matching spectra or units does not verify them. The source native energy H=a gives E=(A<sub>0</sub>/τ<sub>0</sub>)a under this map.')
h('2. Product identification and ambiguity')
p('<b>Theorem 1.</b> The primitive full-state recurrence is T<sub>state</sub>=πτ<sub>0</sub>, and')
e('A<sub>0</sub>a = E T<sub>state</sub>/π.')
p('Without an independent support scale, A<sub>0</sub> is not identified in the map class admitting, for every c&gt;0,')
e('x′=cx, &nbsp; M′=M/c, &nbsp; a′=c<super>2</super>a, &nbsp; A′<sub>0</sub>=A<sub>0</sub>/c<super>2</super>.')
p('<b>Proof.</b> The flow is cos(2s)I+sin(2s)J, so nonzero real x first returns at s=π. The energy pullback gives E=(A<sub>0</sub>/τ<sub>0</sub>)a. Multiplication proves the product identity. Substitution preserves both map equations and M′x′=Mx while A′<sub>0</sub>a′=A<sub>0</sub>a. Thus every observation of the unchanged physical trajectory and energy is preserved while A<sub>0</sub> varies. Additional independently justified amplitude constraints may remove this ambiguity. □')

h('Constructive matrix calibration')
p('Given an independently calibrated absolute M and left inverse L with LM=I, verify KM=M(LKM), LKM=γA and M<super>T</super>GM=λI, with γ,λ&gt;0. These conditions reconstruct the map and give τ<sub>0</sub>=1/γ and A<sub>0</sub>=λ/(2γ). This target-blind extraction still requires the absolute amplitude map; spectra or energy alone do not establish it.')
page();h('3. Why measured energy is not E₀')
p('The earlier monomial-anchor theorem remains valid: independently known E<sub>0</sub>=A<sub>0</sub>/τ<sub>0</sub> and τ<sub>0</sub> determine A<sub>0</sub>. But measured total energy is E=E<sub>0</sub>a. An unknown a is an unknown calibration factor. In log variables (A<sub>0</sub>,τ<sub>0</sub>,a), energy and state period constrain exponent rows (1,-1,1) and (0,1,0). The action target (1,0,0) is outside their row span. The ambiguity vector (-1,0,1) preserves both anchors; an independent norm row (0,0,1) closes the rank condition.')
h('4. Readout parity and the clock')
p('<b>Theorem 2.</b> Every even readout f(-x)=f(x) repeats within half a state cycle, or is constant. A nonconstant homogeneous quadratic readout along this orbit has primitive period T<sub>state</sub>/2. A nonzero signed linear orbit projection has period T<sub>state</sub>.')
p('<b>Proof.</b> At s=π/2 the flow is -I. A quadratic form along cos(2s)x+sin(2s)Jx contains only a constant and sine/cosine terms of frequency 4. If nonconstant, its primitive period is π/2. A nonzero linear projection has frequency 2 and primitive period π. More general even readouts can repeat faster; no universal primitive period is asserted for them. □')
p('For example, x<sub>1</sub>=cos(2s) has period π, x<sub>1</sub><super>2</super> has period π/2, and the conserved energy has no nonconstant period. A sign-blind or projective readout cannot certify the signed state recurrence without an appropriate reference. No physical spinor or quantum phase identity is inferred.')
h('5. Finite action interval')
p('Certify ρ=T<sub>read</sub>/T<sub>state</sub> for the actual readout. Then A<sub>0</sub>=E T<sub>read</sub>/(πρa). For jointly valid positive intervals in E, T<sub>read</sub>, ρ and a, monotonicity gives')
e('E<sub>−</sub>T<sub>−</sub>/(πρ<sub>+</sub>a<sub>+</sub>) ≤ A<sub>0</sub> ≤ E<sub>+</sub>T<sub>+</sub>/(πρ<sub>−</sub>a<sub>−</sub>).')
p('Correlated errors are allowed if joint coverage is certified. Algebra supplies no statistical coverage. If a positive lower support bound cannot be established, this argument supplies no finite upper action bound.')
p('Given an independently calibrated absolute reconstruction with ‖x-x̂‖≤δ, the triangle inequalities give')
e('max(0,‖x̂‖−δ)<super>2</super> ≤ a ≤ (‖x̂‖+δ)<super>2</super>.')
p('Map error, readout error and unobserved-mode leakage belong in δ. Choosing a unit ray representative is not independent physical support calibration.')

page();h('6. Exact verification and its limits')
p('The verifier constructs all 15 oriented nonempty simplices of the filled tetrahedron and the boundary d. Exact rational checks give d<super>2</super>=0, A=d-d<super>T</super>, A<super>3</super>=-4A and active projector P=-A<super>2</super>/4 of rank 14. Hence J=A/2 has J<super>2</super>=-P, becoming -I on the active sector.')
p('A synthetic rational two-plane apparatus fixture checks the intertwiner, energy pullback and energy conservation. Five positive rescalings preserve the physical trajectory and energy while changing A<sub>0</sub>. Rank controls exhibit the missing norm anchor; exact quarter-cycle points distinguish signed and quadratic readouts. Interval corner checks validate the monotone bound. These are constructor mathematical controls, not measurements.')
h('7. Proposed measurement entry requirements')
data=[['Required record','Purpose'],['Carrier and active-state domain','Exclude harmonic/unobserved-sector substitution'],['Energy G and baseline certificate','Identify the measured subsystem energy'],['Intertwiner and clock map','Connect the actual apparatus to the native flow'],['Readout law and signed reference','Certify primitive period and ratio ρ'],['Absolute map or independent support law','Fix a rather than choosing its convention'],['Joint errors and leakage bounds','Establish positive support and finite action interval'],['Frozen rule and non-constructor review','Permit a later target-blind empirical score']]
tab=Table([[Paragraph(v,small) for v in row] for row in data],colWidths=[222,276]);tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8edf1')),('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#bdc7d0')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),4)]));story.append(tab);story.append(Spacer(1,10))
p('Record all target dependencies in the calibration chain. Circuit action Φ<sub>0</sub>Q<sub>0</sub> and native A<sub>0</sub> remain distinct until their map is demonstrated. QPB1’s identification ℏ=A<sub>0</sub>/2 and prediction η<sub>A</sub>=2/1 remain quarantined. No physical apparatus, dataset, independent norm anchor or empirical score is admitted here. These are proposed requirements, not a preregistered experiment.')
h('8. Provenance and status')
p('Source: recovered coefficient ledger v0.85, especially Q282-Q288 and O54-O55. SHA-256:')
story.append(Paragraph('8845ca23e178e043ef0c7bac01be3afba<br/>9cabbefd866c366921387a8ca843aec',small))
p('Prior proof: native action identifiability, capture 2026-10-21T160300Z-codex-action-identifiability-32b8a1d4. Its known-anchor premise is retained. This manuscript isolates the support factor and clock requirements needed to apply it. Non-constructor review is pending; EXIT-03 remains HOLD; physical promotion is 0.')
def foot(c,d):
 c.setFont('Sans',7);c.setFillColor(colors.HexColor('#425466'));c.drawString(48,27,'UD energy-clock-support theorem v0.1 | EXACT CONDITIONAL | Physical promotion 0');c.drawRightString(A4[0]-48,27,str(d.page))
pdf=H/'UD_ENERGY_CLOCK_SUPPORT_v0.1.pdf'
SimpleDocTemplate(str(pdf),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=42,bottomMargin=48,title='Same-carrier energy, clock and support',author='Benjamin Walker Mayes; AI-assisted constructor proof').build(story,onFirstPage=foot,onLaterPages=foot)
print(pdf)
