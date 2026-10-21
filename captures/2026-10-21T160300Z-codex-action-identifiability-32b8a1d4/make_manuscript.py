"""Render the scoped theorem manuscript as an A4 report."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

HERE=Path(__file__).resolve().parent
pdfmetrics.registerFont(TTFont('DSerif','/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('DSerifB','/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DSans','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Body',fontName='DSerif',fontSize=10,leading=15,spaceAfter=9))
styles.add(ParagraphStyle(name='TitleUD',fontName='DSerifB',fontSize=19,leading=24,spaceAfter=15))
styles.add(ParagraphStyle(name='HeadUD',fontName='DSerifB',fontSize=12,leading=17,spaceBefore=11,spaceAfter=8))
styles.add(ParagraphStyle(name='Formula',fontName='DSans',fontSize=10,leading=17,alignment=TA_CENTER,spaceBefore=6,spaceAfter=12))
styles.add(ParagraphStyle(name='SmallUD',fontName='DSans',fontSize=8,leading=12,spaceAfter=8))
story=[]
def p(s):story.append(Paragraph(s,styles['Body']))
def h(s):story.append(Paragraph(s,styles['HeadUD']))
def eq(s):story.append(Paragraph(s,styles['Formula']))
def new():story.append(PageBreak())

story.append(Paragraph('Native action identifiability<br/>from monomial anchors',styles['TitleUD']))
story.append(Paragraph('Theorem manuscript v0.1 · 21 October 2026 · Benjamin Walker Mayes<br/>Constructor proof and verification: Codex · Non-constructor review pending',styles['SmallUD']))
p('<b>Abstract.</b> A dimensionally valid native action formula does not, by itself, fix its physical scale. For a declared positive monomial calibration family, we prove an exact criterion for identifying A<sub>0</sub>=B<sub>0</sub>a<sub>0</sub><super>2</super>/τ<sub>0</sub>: its exponent must lie in the row span of independently anchored exponents. We give an explicit ambiguity family when the criterion fails and a deterministic uncertainty bound when it passes. A source-bound action-unit contract verifies 18 transcribed equalities while retaining the separate physical status of candidate bridges.')
p('<b>Status.</b> EXACT CONDITIONAL mathematics. Development - no registry entry. Physical promotion: 0. This theorem concerns an assumed calibration family and establishes no physical correspondence.')
h('1. Declared calibration model')
p('Let u=(B<sub>0</sub>,a<sub>0</sub>,τ<sub>0</sub>) range over all positive triples, represented numerically in fixed external units. A specified same-carrier map supplies positive anchors')
eq('y<sub>j</sub> = k<sub>j</sub>B<sub>0</sub><super>pⱼ</super>a<sub>0</sub><super>qⱼ</super>τ<sub>0</sub><super>rⱼ</super>,<br/>W<sub>j</sub>=(p<sub>j</sub>,q<sub>j</sub>,r<sub>j</sub>), &nbsp; w<sub>A</sub>=(1,2,-1).')
p('Each k<sub>j</sub> is known, positive, and independent of fitting the target action normalization. The model has no additional unrecorded constraints or unknown calibration factors. Matching physical dimensions does not establish the same-carrier map.')
h('2. Action-anchor identifiability theorem')
p('<b>Theorem 1.</b> The action A<sub>0</sub> is constant on every nonempty anchor fiber if and only if w<sub>A</sub> belongs to row(W). Equivalently,')
eq('rank(W) = rank([W; w<sub>A</sub>]).')
p('If c<super>T</super>W=w<sub>A</sub>, the identified value is')
eq('A<sub>0</sub> = ∏<sub>j</sub> (y<sub>j</sub>/k<sub>j</sub>)<super>cⱼ</super>.')

new();h('3. Proof and explicit ambiguity')
p('Set z=log u and b<sub>j</sub>=log(y<sub>j</sub>/k<sub>j</sub>). The anchor fiber is the affine set Wz=b. If w<sub>A</sub>=c<super>T</super>W, then log A<sub>0</sub>=w<sub>A</sub>z=c<super>T</super>b, constant on that fiber.')
p('Conversely, suppose w<sub>A</sub> is outside row(W). The row space is the orthogonal complement of ker W. Hence there is v with Wv=0 and w<sub>A</sub>v≠0. For every real s, the family')
eq('u<sub>i</sub>(s)=u<sub>i</sub>(0) exp(sv<sub>i</sub>)')
p('is positive, preserves every anchor, and multiplies A<sub>0</sub> by exp(sw<sub>A</sub>v). Hence A<sub>0</sub> is not identifiable. Exponentiating the sufficient-case identity gives the product formula. This proves both directions. □')
p('<b>Scope.</b> Necessity uses the unrestricted positive monomial family. Additional physical constraints, nonmonomial maps, unknown coefficients, or discrete admissible sets require a new identifiability argument. Native dimensionless records that do not constrain the dimensional unit map provide no independent rows of W; they cannot fix A<sub>0</sub>/ℏ for fixed external ℏ.')
h('4. Measurement examples')
data=[['Independently mapped anchors','Action identified?'],['Length and time','No: mass scaling remains'],['Native energy E₀ and time τ₀','Yes: A₀=E₀τ₀'],['Direct native action A₀','Yes: one row suffices'],['Mass, length and time','Yes: full rank is sufficient']]
table=Table([[Paragraph(c,styles['SmallUD']) for c in row] for row in data],colWidths=[268,210])
table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8edf1')),('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#bac5cf')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
story.append(table);story.append(Spacer(1,10))
p('For energy and time, the exponent rows (1,2,-2) and (0,0,1) sum to (1,2,-1). This gives a mathematical design requirement, not evidence that a measured circuit energy is the native energy unit. That correspondence remains an independent premise.')
h('5. Bounded-error corollary')
p('Fix c before outcome scoring. If |b̂<sub>j</sub>-b<sub>j</sub>|≤ε<sub>j</sub> and log Â<sub>0</sub>=c<super>T</super>b̂, then the triangle inequality gives')
eq('|log(Â<sub>0</sub>/A<sub>0</sub>)| ≤ Σ<sub>j</sub> |c<sub>j</sub>| ε<sub>j</sub>.')
p('Include coefficient-calibration errors in b. This is a deterministic bound, valid with correlated errors; statistical coverage requires separate measurement evidence. The result does not justify fitting c to QPB1’s predicted value.')

new();h('6. Typed normalization audit')
p('The contract binds 17 source rows from the recovered v0.85 ledger. Eighteen manually transcribed equations pass dimensional typing in the M,L,T basis. The other 706 ledger rows remain outside this contract. Support and lifted phase are declared dimensionless; a<sub>0</sub> and τ<sub>0</sub> are declared length and time. O15 supplies the mass-like B<sub>0</sub> assignment.')
p('The original O13 equality chain equates A<sub>0</sub>, an action, to a dimensionless reciprocal. It is rejected. The proposed correction separates the two identities:')
eq('ξ<sub>native/phys</sub> = 1/ξ<sub>phys/native</sub>,<br/>A<sub>0</sub> = ξ<sub>native/phys</sub> ℏ.')
p('Both corrected identities pass. Negative controls also reject adding energy to action, a dimensional sine argument, and the energy-typed B<sub>0</sub> branch. Exact reciprocal arithmetic and the unit-support one-winding substitution pass.')
p('The rational verifier checks 2,952 anchor banks built from up to three distinct nonzero exponent rows in {-1,0,1}<super>3</super>. It verifies the row-space/kernel criterion and explicit ambiguity witnesses. This finite campaign checks the implementation; the proof in Section 3 establishes the general theorem.')
h('7. Candidate bridge and experimental entry')
p('Q287’s ℏ=A<sub>0</sub>/2 and Q288’s η<sub>A</sub>=2/1 are dimensionally valid but remain quarantined physical bridge claims. Dimension checking cannot select or establish them. The canonical ratio remains η<sub>A</sub>=A<sub>0</sub>/ℏ. No numerical physical constant is fitted or used to calibrate A<sub>0</sub> here.')
p('Before scoring: freeze the same-carrier map, known coefficients, exponent matrix, independent calibration provenance and error bounds; provide c or an ambiguity witness; freeze the estimator and decision rule; and obtain non-constructor review. Record all target dependence in the calibration chain. No experiment is performed.')
h('8. Provenance and limits')
p('Source: recovered coefficient provenance ledger v0.85 (optical noise reconciliation). The original filename and source bytes are retained in the preceding capture. SHA-256:')
story.append(Paragraph('8845ca23e178e043ef0c7bac01be3afba<br/>9cabbefd866c366921387a8ca843aec',styles['SmallUD']))
p('Source rows: G06, O09-O15, Q282-Q288, O54-O55. Correction proposal: capture 2026-10-21T151000Z-codex-exit03-recovery-98dc7b12. Proof and verifier: this capture. Legacy WBS/dashboard URLs were inaccessible during this check; the canonical EXIT-03 specification remains unrecovered.')
p('<b>Governance.</b> Constructor verification is not independent review. EXIT-03 remains HOLD: its acceptance specification and the complete dimensional ledger audit are unresolved. Physical promotion remains 0.')

def footer(c,doc):
 c.setFont('DSans',7);c.setFillColor(colors.HexColor('#425466'))
 c.drawString(48,28,'UD action-anchor theorem v0.1 | EXACT CONDITIONAL | Physical promotion 0')
 c.drawRightString(A4[0]-48,28,str(doc.page))

out=HERE/'UD_ACTION_ANCHOR_IDENTIFIABILITY_v0.1.pdf'
doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=48,leftMargin=48,topMargin=43,bottomMargin=48,title='Native action identifiability from monomial anchors',author='Benjamin Walker Mayes; AI-assisted constructor proof')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(out)
