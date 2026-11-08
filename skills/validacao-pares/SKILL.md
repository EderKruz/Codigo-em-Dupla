---
name: validacao-pares
description: Audita, como revisor independente, um pacote de regras, requisitos e critérios de aceitação antes da arquitetura e da implementação, e emite parecer LIBERADO, LIBERADO COM RESSALVAS ou BLOQUEADO. Use antes de entregar uma especificação a um agente para implementação.
---

# Validação de pares do pacote de especificação

Baseado nos Capítulos 3 e 5 de *Código em Dupla* e no quality gate de validação da Esteira de Desenvolvimento ByteCod3. A revisão vale mais quando não parte das mesmas premissas de quem escreveu: receba o pacote, não a justificativa do autor.

## O que verificar
- Coerência da cadeia: processo → regras → requisitos → critérios de aceitação.
- Requisito sem regra ou objetivo de origem; regra sem requisito ou critério.
- Critério não testável ou dependente de detalhe técnico irrelevante.
- Duplicidades, conflitos, lacunas e pressupostos não declarados.
- Cobertura de exceções e de regras críticas.
- Identificadores quebrados ou usados de forma inconsistente.
- RNF sem medida, ambiente ou responsável.
- Automação sem problema de origem; uso de IA onde uma regra determinística resolveria.
- Decisões ainda não aprovadas tratadas como definidas.

## Regras
- Classifique cada achado por severidade e indique o item afetado pelo identificador.
- Separe o que é bloqueante do que é melhoria.
- Não reescreva o pacote: aponte o problema e a correção recomendada.

## Saída
Achados por severidade | Itens bloqueantes | Correções recomendadas | Matriz de cobertura | Parecer: LIBERADO, LIBERADO COM RESSALVAS ou BLOQUEADO.
