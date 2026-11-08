# Código em Dupla — material de apoio

Repositório que acompanha o livro *Código em Dupla: Engenharia de Software com Agentes de IA*, de Ederson da Cruz.

Aqui estão, em formato editável, os artefatos que o livro apresenta. A ideia é copiar para o projeto da equipe e adaptar: cortar o que não altera nenhuma decisão e acrescentar o que o contexto exige.

## Conteúdo

| Pasta | O que tem | Onde aparece no livro |
|---|---|---|
| `modelos/` | Os dez modelos do Apêndice A, de A.1 (página de enquadramento) a A.10 (plano de adoção em trinta dias) | Apêndice A |
| `checklists/` | O checklist de cada capítulo, com caixas de marcação | Final de cada capítulo |
| `AGENTS.md` | Exemplo de instruções persistentes para um repositório | Capítulo 2 |
| `skills/` | Cinco habilidades no formato aberto Agent Skills: `discovery-regras`, `requisitos-bdd`, `validacao-pares`, `contrato-de-tarefa` e `dossie-de-evidencias` | Capítulos 2 a 5 |

## Sequência sugerida das skills

`discovery-regras` → `requisitos-bdd` → `validacao-pares` → `contrato-de-tarefa` → (implementação) → `dossie-de-evidencias`

As três primeiras vêm da Esteira de Desenvolvimento ByteCod3, que cobre o que acontece antes do código: processo, regras e requisitos.

## Como usar

1. **Modelos:** copie o arquivo para a pasta de documentação do projeto ou para o modelo de issue/PR da sua plataforma.
2. **AGENTS.md:** copie para a raiz do repositório e substitua cada trecho entre colchetes. Mantenha curto, com dono e data de revisão.
3. **Skills:** copie a pasta da habilidade para o diretório de skills da ferramenta de agente usada pela equipe. Leia o `SKILL.md` antes de instalar; uma habilidade é contexto com autoridade e merece a mesma revisão de qualquer dependência (Capítulo 6).
4. **Checklists:** use na revisão de PR ou cole na descrição da tarefa.

## Correções e atualizações

Referências datadas (padrões, estudos, legislação) mudam entre edições. As correções conhecidas ficam registradas em `ERRATA.md` e nas *issues* deste repositório.

## Licença

Este material está licenciado sob a [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br). Você pode copiar, adaptar e usar inclusive comercialmente, desde que atribua a fonte: *Código em Dupla*, de Ederson da Cruz. Veja `LICENSE`.
