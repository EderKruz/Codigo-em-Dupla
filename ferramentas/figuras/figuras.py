import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, math
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse, Rectangle, Polygon, Arc
plt.rcParams['font.family']='Inter'
INK='#1A1A1A'; DARK='#3D3D3D'; MID='#7A7A7A'; L1='#E9E9E9'; L2='#CFCFCF'; L3='#A8A8A8'; BG='#F4F4F4'
WIN=4.69
def canvas(pxw,pxh):
    Hu=100*pxh/pxw
    fig=plt.figure(figsize=(WIN,WIN*pxh/pxw),dpi=pxw/WIN)
    ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,100); ax.set_ylim(0,Hu); ax.axis('off')
    return fig,ax,Hu
STY={'h':dict(fc='white',ec=INK,lw=1.6,ls='-'),   # humano / decisão
     'a':dict(fc=L1,ec=DARK,lw=0.9,ls='-'),        # agente / técnico
     'e':dict(fc=L2,ec=INK,lw=1.6,ls='-'),         # ênfase / gargalo
     'd':dict(fc='white',ec=DARK,lw=1.0,ls=(0,(3,2))), # incerto / externo
     'w':dict(fc='white',ec=DARK,lw=0.9,ls='-')}
def box(ax,x,y,w,h,t,st='a',fs=8,bold=True,sub=None,sfs=6.3,z=3,r=1.2):
    s=STY[st]
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle=f"round,pad=0,rounding_size={r}",fc=s['fc'],ec=s['ec'],lw=s['lw'],ls=s['ls'],zorder=z))
    ax.text(x,y,t,ha='center',va='center',fontsize=fs,color=INK,weight='bold' if bold else 'normal',zorder=z+1,linespacing=1.15)
    if sub: ax.text(x,y-h/2-(3.9 if '\n' in sub else 2.6),sub,ha='center',va='center',fontsize=sfs,color=DARK,zorder=z+1)
def arr(ax,p,q,rad=0,ls='-',c=DARK,lw=1.0,head=True,z=2):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>' if head else '-',mutation_scale=7,color=c,lw=lw,ls=ls,shrinkA=0,shrinkB=0,connectionstyle=f"arc3,rad={rad}",zorder=z))
def txt(ax,x,y,t,fs=7.5,bold=False,it=False,c=INK,ha='center'):
    ax.text(x,y,t,ha=ha,va='center',fontsize=fs,color=c,weight='bold' if bold else 'normal',style='italic' if it else 'normal')
def save(fig,name): fig.savefig(name,dpi=fig.dpi,facecolor='white'); plt.close(fig)
def row(ax,xs,y,names,w,h,sty,subs=None,fs=8):
    for i,(x,n) in enumerate(zip(xs,names)):
        box(ax,x,y,w,h,n,sty[i],fs=fs,sub=subs[i] if subs else None)
    for a,b in zip(xs,xs[1:]): arr(ax,(a+w/2+0.6,y),(b-w/2-0.6,y))

# ---------- P1 (image1)
fig,ax,H=canvas(2786,1229)
txt(ax,50,39,'Contexto explícito transforma capacidade em colaboração',fs=9,bold=True)
ax.add_patch(Circle((17,27.5),3.6,fc='white',ec=INK,lw=1.6)); ax.add_patch(Arc((17,17.5),15,13,theta1=20,theta2=160,ec=INK,lw=1.6))
txt(ax,17,10,'intenção, decisão\ne responsabilidade',fs=7)
box(ax,50,22,22,12,'CONTRATO\nDA DUPLA','h',fs=9.5)
hx=[(83+6.5*math.cos(math.radians(a)),22+6.5*math.sin(math.radians(a))) for a in range(30,390,60)]
ax.add_patch(Polygon(hx,closed=True,fc=L1,ec=DARK,lw=1.0))
pts=[(83,25),(80.5,20.5),(85.5,20.5)]
for p,q in [(0,1),(1,2),(2,0)]: ax.plot([pts[p][0],pts[q][0]],[pts[p][1],pts[q][1]],color=DARK,lw=0.9)
for p in pts: ax.add_patch(Circle(p,0.9,fc=DARK,ec=DARK))
txt(ax,83,10,'investigação, geração\ne verificação',fs=7)
arr(ax,(25.5,22),(38.5,22),lw=1.2); arr(ax,(76,22),(61.5,22),lw=1.2)
save(fig,'image1.png')

# ---------- P2 (image2)
fig,ax,H=canvas(2771,1229)
xs=[12,31,50,69,88]
for x in xs:
    ax.plot([x,x],[20,13],color=MID,lw=0.8,zorder=1)
    ax.add_patch(Circle((x,32),1.3,fc=INK,ec=INK)); txt(ax,x,36.3,'evidência',fs=6.5,c=DARK)
ax.plot([12,88],[13,13],color=INK,lw=1.4)
row(ax,xs,24,['Plano','Mudança','Testes','Revisão','Produção'],15,7.5,['a','a','a','a','h'])
txt(ax,50,6.5,'a confiança é construída ao longo do fluxo',fs=8.5,bold=True)
save(fig,'image2.png')

# ---------- P3 (image3)
fig,ax,H=canvas(2771,1229)
c=(50,24.5)
nodes=[('Aprendizagem',50,38.5,'a'),('Operação',82,32,'a'),('Organização',82,17,'h'),('Consequências',50,10.5,'h'),('Usuários',18,17,'a'),('Equipe',18,32,'h')]
for n,x,y,s in nodes: ax.plot([c[0],x],[c[1],y],color=MID,lw=0.9,zorder=1)
ax.add_patch(Ellipse(c,20,11,fc=L2,ec=INK,lw=1.6,zorder=3)); txt(ax,50,24.5,'SOFTWARE',fs=9,bold=True)
for n,x,y,s in nodes: box(ax,x,y,19,6,n,s,fs=7.5)
txt(ax,50,3,'valor, custo e impacto pertencem ao mesmo sistema',fs=8.5,bold=True)
save(fig,'image3.png')

# ---------- P4 (image4)
fig,ax,H=canvas(2771,1229)
cx,cy,r=21,20,12
ax.add_patch(Arc((cx,cy),2*r,2*r,theta1=55,theta2=180,ec=L3,lw=5))
ax.add_patch(Arc((cx,cy),2*r,2*r,theta1=0,theta2=55,ec=INK,lw=5))
a=math.radians(118); ax.plot([cx,cx+9*math.cos(a)],[cy,cy+9*math.sin(a)],color=INK,lw=1.8); ax.add_patch(Circle((cx,cy),1.3,fc=INK))
txt(ax,cx,10.5,'AUTONOMIA\nPROPORCIONAL',fs=8,bold=True)
txt(ax,cx+15,33,'mais risco', fs=6.3, c=DARK); txt(ax,cx-15,13.5,'', fs=6)
xs=[50,63.5,77,90.5]
row(ax,xs,27,['Decidir','Autorizar','Executar','Observar'],12,6.5,['h','a','a','a'],fs=7.5)
arr(ax,(90.5,23.5),(50,23.5),rad=-0.35)
txt(ax,70,7,'decisões, efeitos e aprendizagem fecham o ciclo',fs=8,bold=True)
save(fig,'image4.png')

# ---------- F2 (image5)
fig,ax,H=canvas(2771,1399)
xs=[12,31,50,69,88]
row(ax,xs,30,['Pedido','Regra','Limite','Evidência','Solução'],15,9,['d','a','a','a','h'],subs=['o que foi\ndito','o que deve\nvaler','o que não\npode mudar','como\nprovar','o que\nconstruir'],fs=8.5)
txt(ax,50,9,'Cada etapa reduz uma suposição antes que ela vire código',fs=8,it=True)
save(fig,'image5.png')

# ---------- F3 (image6)
fig,ax,H=canvas(2771,1399)
ax.add_patch(Circle((50,29),8.5,fc=L2,ec=INK,lw=1.6,zorder=3)); txt(ax,50,29,'AGENTE',fs=9,bold=True)
for n,s,x,y in [('Contexto','fontes e instruções',14,41),('Memória','histórico selecionado',14,18),('Ferramentas','ações disponíveis',86,41),('Estado','situação da tarefa',86,18)]:
    box(ax,x,y,20,7.5,n,'w',fs=8,sub=s)
    dx,dy=50-x,29-y; d=math.hypot(dx,dy); ex,ey=50-dx/d*9,29-dy/d*9
    arr(ax,(x+(10.5 if x<50 else -10.5),y),(ex,ey))
box(ax,50,8,24,6,'Efeito observável','h',fs=8)
arr(ax,(50,20.3),(50,11.3))
save(fig,'image6.png')

# ---------- F4 (image7)
fig,ax,H=canvas(2771,1399)
ys=[44,35,26,17,8]; ws=[82,70,58,46,34]
names=['INTENÇÃO','REGRAS E DECISÕES','EXEMPLOS E BORDAS','CONTRATOS E INVARIANTES','CRITÉRIOS VERIFICÁVEIS']
st=['d','w','a','w','e']
for i,(y,w,n) in enumerate(zip(ys,ws,names)):
    box(ax,50,y,w,6,n,st[i],fs=7.5,r=0.8)
    if i<4: arr(ax,(50,y-3.1),(50,ys[i+1]+3.1))
save(fig,'image7.png')

# ---------- F6 (image8)
fig,ax,H=canvas(2771,1399)
cx,cy=50,25.5
ax.add_patch(Circle((cx,cy),9.5,fc='white',ec=INK,lw=1.6)); txt(ax,cx,cy,'MUDANÇA\nCONTROLADA',fs=6.8,bold=True)
names=['Linha de base','Investigação','Plano','Execução','Verificação']
angs=[90,18,-54,-126,162]; P=[(cx+31*math.cos(math.radians(a)),cy+18.5*math.sin(math.radians(a))) for a in angs]
for i in range(5):
    p,q=P[i],P[(i+1)%5]
    arr(ax,(p[0]+(q[0]-p[0])*0.28,p[1]+(q[1]-p[1])*0.28),(p[0]+(q[0]-p[0])*0.72,p[1]+(q[1]-p[1])*0.72),rad=-0.15)
for i,(n,p) in enumerate(zip(names,P)): box(ax,p[0],p[1],19,6.3,n,'h' if i==0 else 'a',fs=7.8)
txt(ax,50,2.5,'pequenos lotes tornam o trabalho interrompível e revisável',fs=7.5,it=True)
save(fig,'image8.png')

# ---------- F8 (image9)
fig,ax,H=canvas(2771,1399)
ys=[45,36.5,28,19.5,11]; ws=[34,46,58,70,82]
for i,(y,w,n) in enumerate(zip(ys,ws,['Código','Regra','Contrato','Jornada','Produção'])):
    box(ax,50,y,w,6.5,n,['w','a','w','a','e'][i],fs=8,r=0.8)
txt(ax,50,3,'nenhuma camada, sozinha, demonstra o comportamento do sistema',fs=7.5,it=True)
save(fig,'image9.png')

# ---------- F9 (image10)
fig,ax,H=canvas(2771,1399)
ax.add_patch(FancyBboxPatch((21,7),77,40,boxstyle="round,pad=0,rounding_size=1.5",fc=BG,ec=INK,lw=1.4))
txt(ax,23,44,'AMBIENTE CONTROLADO',fs=6.8,bold=True,ha='left')
ax.add_patch(FancyBboxPatch((27,11),50,29,boxstyle="round,pad=0,rounding_size=1.2",fc='white',ec=DARK,lw=1.0,ls=(0,(3,2))))
txt(ax,29,37,'SANDBOX DO AGENTE',fs=6.5,bold=True,ha='left',c=DARK)
box(ax,54,24.5,22,9,'Agente\nidentidade própria','a',fs=7.8)
box(ax,88.5,33,15,6,'Ferramenta','w',fs=7.3); box(ax,88.5,17,15,6,'Dados','w',fs=7.3)
arr(ax,(65.5,26.5),(80.7,32)); arr(ax,(65.5,22.5),(80.7,18))
box(ax,9.5,24.5,14,7,'Segredos','d',fs=7.8)
ax.plot([16.8,24.2],[24.5,24.5],color=INK,lw=1.2); ax.plot([24.2,24.2],[21.5,27.5],color=INK,lw=2.4)
txt(ax,9.5,18.5,'acesso bloqueado',fs=6,c=DARK)
txt(ax,50,2.5,'privilégio mínimo · ferramenta estreita · efeito auditável',fs=7.8,bold=True)
save(fig,'image10.png')

# ---------- F10 (image11)
fig,ax,H=canvas(2771,1399)
for x0,t,st,items in [(3,'PESSOA','h',['formular o problema','julgar consequências','assumir decisões','explicar o raciocínio']),(63,'AGENTE','a',['pesquisar padrões','gerar alternativas','executar verificações','comparar evidências'])]:
    s=STY[st]; ax.add_patch(FancyBboxPatch((x0,8),34,38,boxstyle="round,pad=0,rounding_size=1.5",fc=s['fc'],ec=s['ec'],lw=s['lw']))
    txt(ax,x0+17,41.5,t,fs=9,bold=True)
    for k,it in enumerate(items): txt(ax,x0+17,33-k*6.5,it,fs=7.5)
ax.plot([37,63],[27,27],color=MID,lw=0.9,zorder=1)
box(ax,50,27,21,10,'APRENDER\nEM CONJUNTO','w',fs=8,z=3)
txt(ax,50,2.8,'delegar produção não significa terceirizar compreensão',fs=8,bold=True)
save(fig,'image11.png')

# ---------- F11 (image12)
fig,ax,H=canvas(2771,1399)
rs=[5,6.5,8,9.5,11]; gap=3.2; x=4; cs=[]
for rr in rs: cs.append(x+rr); x+=2*rr+gap
off=(100-(x-gap))/2-4+4; cs=[c+off-4 for c in cs]
names=['Código','Interface','Pessoa','Atendimento','Operação']
for i,(c,rr,n) in enumerate(zip(cs,rs,names)):
    s=STY['h' if n=='Pessoa' else ('w' if i%2==0 else 'a')]
    ax.add_patch(Circle((c,27),rr,fc=s['fc'],ec=s['ec'],lw=s['lw'])); txt(ax,c,27,n,fs=7.3,bold=True)
for i in range(4): arr(ax,(cs[i]+rs[i]+0.4,27),(cs[i+1]-rs[i+1]-0.4,27))
txt(ax,50,7,'cada fronteira pode criar trabalho, exclusão ou recuperação',fs=7.8,it=True)
save(fig,'image12.png')

# ---------- F12 (image13)
fig,ax,H=canvas(2771,1399)
y=27
box(ax,9,y,14,11,'Geração','a',fs=8)
for k in range(3): ax.add_patch(Circle((19+k*2.2,y),0.9,fc=INK))
txt(ax,21.2,y+5,'fila',fs=6.5,bold=True)
ax.plot([16.2,18],[y,y],color=DARK,lw=1.0)
arr(ax,(24.2,y),(25.6,y))
box(ax,35,y,19,16,'Revisão\n(gargalo)','e',fs=8.5)
box(ax,55.5,y,16,11,'Integração','a',fs=8); box(ax,74,y,15,11,'Operação','a',fs=8); box(ax,91,y,12,8,'Valor','h',fs=8)
arr(ax,(44.7,y),(47.3,y)); arr(ax,(63.7,y),(66.3,y)); arr(ax,(81.7,y),(84.8,y))
txt(ax,50,6,'produtividade é a capacidade do sistema de concluir trabalho relevante',fs=7.6,it=True)
save(fig,'image13.png')

# ---------- F14 (image14)
fig,ax,H=canvas(2771,1399)
levels=['0 Responder','1 Propor','2 Experi-\nmentar','3 Preparar\nmudança','4 Executar\ncom aprovação','5 Operar por\npolítica']
risks=['Muito baixo','Baixo','Médio','Alto','Muito alto']; mx=[5,4,3,2,1]
x0,x1,y0,y1=20,97,15,44; cw=(x1-x0)/6; rh=(y1-y0)/5
for ri,(rn,m) in enumerate(zip(risks,mx)):
    yy=y0+ri*rh
    txt(ax,x0-1.5,yy+rh/2,rn,fs=6.5,ha='right')
    for li in range(6):
        if li<m: fc,h='white',None
        elif li==m: fc,h=L2,None
        else: fc,h=L3,'////'
        ax.add_patch(Rectangle((x0+li*cw,yy),cw,rh,fc=fc,ec=INK,lw=0.6,hatch=h))
plt.rcParams['hatch.color']=DARK
for li,l in enumerate(levels): txt(ax,x0+li*cw+cw/2,y0-3.6,l,fs=5.9)
txt(ax,4,(y0+y1)/2,'RISCO DA AÇÃO',fs=6.8,bold=True); ax.texts[-1].set_rotation(90)
txt(ax,(x0+x1)/2,47.5,'nível de autonomia →',fs=7,bold=True)
for k,(fc,h,lab) in enumerate([('white',None,'adequado'),(L2,None,'com controles reforçados'),(L3,'////','evitar')]):
    lx=[20,40,74][k]
    ax.add_patch(Rectangle((lx,2),3,2.4,fc=fc,ec=INK,lw=0.6,hatch=h)); txt(ax,lx+4,3.2,lab,fs=6.5,ha='left')
save(fig,'image14.png')

# ---------- F15 (image15)
fig,ax,H=canvas(2771,1399)
xs=[11,30.5,50,69.5,89]
row(ax,xs,31,['Objetivo','Proxy','Regra','Resultado','Impacto'],15,8,['a','a','a','h','h'],fs=8)
box(ax,50,11,36,7,'Contestação e reparação','d',fs=8)
arr(ax,(89,27),(68.3,11),rad=-0.25); arr(ax,(31.7,11),(11,27),rad=-0.25)
txt(ax,50,45,'tornar a cadeia visível permite revisar valores e consequências',fs=7.5,it=True)
save(fig,'image15.png')

# ---------- F16 (image16)
fig,ax,H=canvas(2771,1399)
xs=[12,31,50,69,88]
ax.plot([12,88],[38,38],color=MID,lw=1.0)
for x in xs: ax.plot([x,x],[38,28.5],color=MID,lw=0.8); ax.add_patch(Circle((x,38),1.3,fc=INK))
row(ax,xs,24,['Definir','Unificar','Planejar','Ler evidências','Acompanhar'],17,8,['h','a','a','a','h'],subs=['resultado\ne limites','fontes e\nautoridade','fatias e\nriscos','alegações\ne provas','efeitos e\naprendizagem'],fs=7.4)
txt(ax,50,5,'cada entrega devolve aprendizagem ao próximo ciclo',fs=7.8,it=True)
save(fig,'image16.png')
print('ok')
