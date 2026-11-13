import re,sys,zipfile,unicodedata
src_docx,pdftxt,dst=sys.argv[1:4]
mk=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'termos_indice.py')).read()
T=eval(mk[mk.index('T=[')+2:mk.index('def key')].strip())
RX=dict(T)
txt=open(pdftxt).read().split('\f')
start=next(i for i,p in enumerate(txt) if re.search(r'^CAPÍTULO 1\s*$',p,re.M))
end=next(i for i,p in enumerate(txt) if i>start+50 and re.search(r'^Glossário\s*$',p,re.M))
def norm(p): return re.sub(r'\s+',' ',re.sub(r'(\w)-\n(\w)',r'\1\2',p))
pages={}; inref=False
for i in range(start,end):
    keep=[]
    for ln in txt[i].split('\n'):
        if re.match(r'^Referências( do capítulo)?\s*$',ln): inref=True; continue
        if re.match(r'^(CAPÍTULO \d+|Parte [IV]+ —|PARTE [IV]+|Conclusão|Apêndice A)',ln): inref=False
        if not inref: keep.append(ln)
    pages[i+1]=norm('\n'.join(keep))
def pg(name):
    rx=RX.get(name, re.escape(name))
    cs=0 if rx in (r'\bDORA\b',r'\bMETR\b',r'\bMCP\b|Model Context Protocol',r'\bLGPD\b') else re.I
    hits={p:len(re.findall(rx,t,cs)) for p,t in pages.items()}; hits={p:c for p,c in hits.items() if c}
    if not hits: return None
    sel=sorted(sorted(hits,key=lambda p:-hits[p])[:8]); rs=[];a=b=sel[0]
    for p in sel[1:]:
        if p==b+1: b=p
        else: rs.append((a,b)); a=b=p
    rs.append((a,b)); return ', '.join(f'{x}' if x==y else f'{x}–{y}' for x,y in rs)
z=zipfile.ZipFile(src_docx); files={n:z.read(n) for n in z.namelist()}
d=files['word/document.xml'].decode()
i=d.rfind('>Índice remissivo<'); j=d.find('>Sobre o autor<',i)
seg=d[i:j]; miss=[]; n=0
def fix(m):
    global n
    name,nums=m.group(1),m.group(2)
    new=pg(name)
    if new is None: miss.append(name); return m.group(0)
    n+=1; return f'<w:t>{name}, {new}</w:t>'
seg2=re.sub(r'<w:t>([^<,]+(?:, [^<0-9][^<,]*)?), ([0-9][0-9–, ]*)</w:t>',fix,seg)
d=d[:i]+seg2+d[j:]
files['word/document.xml']=d.encode()
with zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED) as o:
    for k in z.namelist(): o.writestr(k,files[k])
print('atualizadas',n,'sem ocorrência',miss)
