# Capítulo 6 — Segurança e governança

## Checklist de segurança e governança

- [ ] O agente está no modelo de ameaças como componente com identidade, entradas e efeitos.
- [ ] Ativos, fronteiras, dados, ferramentas, integrações e caminhos de saída foram identificados.
- [ ] Conteúdo externo é tratado como dado não confiável e mantém a informação de origem.
- [ ] Instruções textuais não ampliam permissões nem autorizam ações por si mesmas.
- [ ] Os dados enviados ao modelo e às ferramentas são mínimos para a finalidade declarada.
- [ ] Segredos não aparecem em prompts, logs, commits, respostas ou argumentos expostos.
- [ ] Identidades do usuário, do agente, do executor e do pipeline são separadas.
- [ ] Credenciais são temporárias, revogáveis e limitadas por recurso e operação.
- [ ] A rede é bloqueada por padrão e liberada só para destinos e métodos necessários.
- [ ] Ferramentas e conectores têm contratos estreitos, origem verificada e inventário.
- [ ] Ambientes são isolados, efêmeros e não preservam estado não autorizado.
- [ ] A memória tem origem, escopo, finalidade, expiração, correção e exclusão.
- [ ] A proveniência dos artefatos gerados é registrada, e quem integra responde por eles.
- [ ] A auditoria liga identidade, decisão, autorização, execução, alteração e resultado.
- [ ] O plano de incidente contempla contenção, revogação, preservação, recuperação e aprendizado.
