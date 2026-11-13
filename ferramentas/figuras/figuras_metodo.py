import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import math, sys
B='#2B2B2B'; F='#E9E9E9'; T='#1A1A1A'; A='#555555'
plt.rcParams['font.family']='Inter'
def box(ax,x,y,w,h,txt,fs=11,fill=F,ec=B,bold=False,sub=None):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0.02,rounding_size=0.08",fc=fill,ec=ec,lw=1.6))
    if sub:
        ax.text(x,y+h*0.14,txt,ha='center',va='center',fontsize=fs,color=T,weight='bold' if bold else 'normal')
        ax.text(x,y-h*0.2,sub,ha='center',va='center',fontsize=fs-3,color=T)
    else:
        ax.text(x,y,txt,ha='center',va='center',fontsize=fs,color=T,weight='bold' if bold else 'normal')
def arrow(ax,p,q,c=B,ls='-',rad=0.0):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=14,color=c,lw=1.5,linestyle=ls,connectionstyle=f"arc3,rad={rad}"))
out=sys.argv[1]
# Fig 1 DUPLA
fig,ax=plt.subplots(figsize=(7,5.2));ax.set_xlim(-3.6,3.6);ax.set_ylim(-2.9,2.6);ax.axis('off')
names=[('Definir','resultado e limites'),('Unificar','contexto e autoridade'),('Planejar','passos e autonomia'),('Ler evidências','alegação e prova'),('Acompanhar','produção e aprendizado')]
R=2.0;pts=[]
for i,(n,s) in enumerate(names):
    a=math.pi/2-2*math.pi*i/5;x,y=R*math.cos(a)*1.25,R*math.sin(a);pts.append((x,y));box(ax,x,y,1.9,0.8,n,12,bold=True,sub=s)
for i in range(4):
    (x1,y1),(x2,y2)=pts[i],pts[i+1]
    arrow(ax,(x1+(x2-x1)*0.28,y1+(y2-y1)*0.28),(x1+(x2-x1)*0.72,y1+(y2-y1)*0.72),rad=-0.15)
(x1,y1),(x2,y2)=pts[4],pts[0]
arrow(ax,(x1+(x2-x1)*0.28,y1+(y2-y1)*0.28),(x1+(x2-x1)*0.72,y1+(y2-y1)*0.72),c=A,ls='--',rad=-0.15)
ax.text(0,0.05,'Método\nDUPLA',ha='center',va='center',fontsize=15,color=B,weight='bold')
ax.text(-2.95,1.35,'o aprendizado\nvolta ao início',ha='center',fontsize=8.5,color=A)
fig.savefig(out+'/fig1-dupla.png',dpi=440,bbox_inches='tight');plt.close()
# Fig 2 encaixe
fig,ax=plt.subplots(figsize=(7.4,4.6));ax.set_xlim(0,10);ax.set_ylim(0,6.2);ax.axis('off')
ax.add_patch(FancyBboxPatch((0.2,0.2),9.6,5.8,boxstyle="round,pad=0.02,rounding_size=0.15",fc='white',ec=B,lw=1.8))
ax.text(5,5.65,'Método DUPLA — o método da equipe, do pedido à operação',ha='center',fontsize=10.5,color=B,weight='bold')
for i,n in enumerate(['Definir','Unificar','Planejar','Ler evidências','Acompanhar']):
    box(ax,1.2+i*1.9,5.0,1.7,0.5,n,9.5)
ax.add_patch(FancyBboxPatch((1.0,0.6),8.0,3.6,boxstyle="round,pad=0.02,rounding_size=0.12",fc=F,ec=B,lw=1.4))
ax.text(5,3.9,'Ciclo de trabalho agentivo — como a equipe conduz uma tarefa (Cap. 4)',ha='center',fontsize=9.5,color=T,weight='bold')
for i,n in enumerate(['Linha de base','Investigação','Plano','Execução','Verificação']):
    box(ax,1.85+i*1.58,3.25,1.36,0.48,n,7.6,fill='white')
    if i<4: arrow(ax,(1.85+i*1.58+0.70,3.25),(1.85+(i+1)*1.58-0.70,3.25))
ax.add_patch(FancyBboxPatch((4.4,1.0),3.8,1.4,boxstyle="round,pad=0.02,rounding_size=0.12",fc='white',ec=A,lw=1.4))
ax.text(6.3,2.12,'Laço do agente (Cap. 2)',ha='center',fontsize=9,color=A,weight='bold')
ax.text(6.3,1.45,'observar → escolher → agir\n→ avaliar → continuar ou parar',ha='center',fontsize=8.5,color=T)
arrow(ax,(6.59,2.98),(6.59,2.44),c=A)
ax.text(2.5,1.55,'o laço se repete\na cada ação\nda execução',ha='center',fontsize=8.5,color=A)
fig.savefig(out+'/fig2-encaixe.png',dpi=440,bbox_inches='tight');plt.close()
# Fig 3 escada autonomia
fig,ax=plt.subplots(figsize=(7.4,4.2));ax.set_xlim(0,12.4);ax.set_ylim(0,7);ax.axis('off')
lv=[('0','Responder'),('1','Propor'),('2','Experimentar'),('3','Preparar\nmudança'),('4','Executar com\naprovação'),('5','Operar por\npolítica')]
for i,(n,m) in enumerate(lv):
    x=0.3+i*2.0;h=1.0+i*0.95
    ax.add_patch(FancyBboxPatch((x,0.4),1.8,h,boxstyle="round,pad=0.02,rounding_size=0.08",fc=F,ec=B,lw=1.5))
    ax.text(x+0.9,0.4+h-0.32,'Nível '+n,ha='center',fontsize=9,color=B,weight='bold')
    ax.text(x+0.9,0.4+h/2-0.12 if i>0 else 0.75,m,ha='center',va='center',fontsize=8.5,color=T)
arrow(ax,(0.4,6.6),(12.1,6.6),c=A)
ax.text(6.2,6.75,'mais efeito possível exige mais controle externo: ambiente, orçamento, aprovação e monitoramento',ha='center',fontsize=8.3,color=A)
fig.savefig(out+'/fig3-autonomia.png',dpi=440,bbox_inches='tight');plt.close()
# Fig 4 cadeia
fig,ax=plt.subplots(figsize=(7.6,2.6));ax.set_xlim(0,12.6);ax.set_ylim(0,3);ax.axis('off')
st=[('Alegação','o que se afirma'),('Risco','o que a\ntornaria falsa'),('Evidência','procedimento\ncapaz de\ncontradizê-la'),('Limite','o que não foi\nverificado'),('Decisão','aceitar, ampliar,\nlimitar ou bloquear')]
for i,(n,s) in enumerate(st):
    x=1.2+i*2.55;box(ax,x,1.5,2.15,1.7,n,11,bold=True,sub=s)
    if i<4: arrow(ax,(x+1.1,1.5),(x+1.45,1.5))
fig.savefig(out+'/fig4-cadeia.png',dpi=440,bbox_inches='tight');plt.close()
print('ok')
