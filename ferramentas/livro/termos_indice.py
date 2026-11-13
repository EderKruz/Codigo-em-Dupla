import re, unicodedata, sys
txt=open(sys.argv[1]).read().split('\f')
start=next(i for i,p in enumerate(txt) if re.search(r'^CAPÍTULO 1\s*$',p,re.M))
end=next(i for i,p in enumerate(txt) if i>start+50 and re.search(r'^Glossário\s*$',p,re.M))
def norm(p): return re.sub(r'\s+',' ',re.sub(r'(\w)-\n(\w)',r'\1\2',p))
pages={}; inref=False
for i in range(start,end):
    keep=[]
    for ln in txt[i].split('\n'):
        if re.match(r'^Referências( do capítulo)?\s*$',ln): inref=True; continue
        if re.match(r'^(CAPÍTULO \d+|Parte [IV]+ —|Conclusão|Apêndice A)',ln): inref=False
        if not inref: keep.append(ln)
    pages[i+1]=norm('\n'.join(keep))
T=[('Acessibilidade',r'acessibilidade'),('Agent Skills',r'Agent Skills'),('AGENTS.md',r'AGENTS\.md'),
('Agentes como revisores',r'revisor automático|agente revisor|agentes? como revisor'),('Alegação',r'alegaç(ão|ões)'),
('Aprovação contextual',r'aprovação contextual'),('Autonomia, escala de',r'escala (operacional )?de autonomia'),
('Ciclo de trabalho agentivo',r'ciclo de trabalho'),('Confabulação',r'confabula'),('Confiança calibrada',r'confiança calibrada'),
('Contestação',r'contesta(ção|r)'),('Contexto, engenharia de',r'engenharia de contexto'),('Contexto, janela de',r'janelas? de contexto'),
('Contrato de tarefa',r'contrato de tarefa'),('Critérios de aceitação',r'critérios? de aceitação'),
('Desenvolvimento orientado por especificação',r'orientado por especificação'),('Dívida de especificação',r'dívida de especificação'),
('DORA',r'\bDORA\b'),('Dossiê de evidências',r'dossiê de evidências'),('Envenenamento de ferramenta',r'envenenamento de ferramenta|tool poisoning'),
('Escada de ajuda',r'escada de ajuda'),('Estrangulamento, padrão de',r'estrangulamento'),('Fatias verticais',r'fatias? (verticais|de valor)'),
('FitKruz, caso',r'FitKruz'),('Gargalo de revisão',r'gargalo'),('Horizonte de tempo',r'horizonte de tempo'),('Idempotência',r'idempot'),
('Injeção indireta de instruções',r'injeção indireta'),('Instruções persistentes',r'instruções persistentes'),('Invariante',r'invariante'),
('Laço do agente',r'laço do agente'),('Legado, sistema',r'\blegad[oa]s?\b'),('LGPD',r'\bLGPD\b'),('Linha de base',r'linha de base'),
('Model Context Protocol (MCP)',r'\bMCP\b|Model Context Protocol'),('Memória do agente',r'\bmemória\b'),('Método DUPLA',r'Método DUPLA'),
('METR',r'\bMETR\b'),('Orçamento de ação',r'orçamento de (ação|autonomia)|autonomia cabe em um orçamento'),('Oráculo',r'oráculo'),('Orquestração de agentes',r'orquestra'),
('PL 2.338/2023',r'PL 2\.338'),('Privacidade',r'privacidade'),('Privilégio mínimo',r'privilégio mínimo'),('Proveniência',r'proveniência'),
('Proxy',r'\bprox(y|ies)\b'),('Rastreabilidade',r'rastreabilidade'),('Regra ou IA, escolha entre',r'regra determinística'),('Maturidade do fluxo',r'maturidade'),('Reversão',r'\breversão\b'),('Segredos',r'\bsegredos?\b'),('Sinalizador de recurso',r'sinalizador(es)? de recurso'),
('Sistema sociotécnico',r'sociotécnic'),('Teste de caracterização',r'testes? de caracterização'),('Testes de mutação',r'mutaç'),
('Trabalho deslocado',r'trabalho deslocado|redistribui'),('Vários agentes em paralelo',r'vários agentes|worktrees?'),('Verificação independente',r'independên')]
def key(s): return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().upper()
out=['#H1 Índice remissivo','','As páginas indicam as passagens em que o termo é definido ou discutido com mais detalhe. Termos muito recorrentes listam apenas as ocorrências principais.','']
cur=None
for name,rx in sorted(T,key=lambda x:key(x[0])):
    hits={p:len(re.findall(rx,t,re.I if not rx.isupper() and 'DORA' not in rx and 'METR' not in rx and 'MCP' not in rx and 'LGPD' not in rx else 0)) for p,t in pages.items()}
    hits={p:c for p,c in hits.items() if c}
    if not hits: print('SEM OCORRÊNCIA', name); continue
    sel=sorted(sorted(hits,key=lambda p:-hits[p])[:8])
    # compress ranges
    rs=[];a=b=sel[0]
    for p in sel[1:]:
        if p==b+1: b=p
        else: rs.append((a,b)); a=b=p
    rs.append((a,b))
    L=key(name)[0]
    if L!=cur: out+=['',f'### {L}']; cur=L
    out.append('~ **'+name+'**, '+', '.join(f'{x}' if x==y else f'{x}–{y}' for x,y in rs))
print('\n'.join(out), file=open(sys.argv[2],'w')); print(len(T),'termos')
