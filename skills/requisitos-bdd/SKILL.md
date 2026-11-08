---
name: requisitos-bdd
description: Converte regras de negócio confirmadas em requisitos verificáveis (RF/RNF), critérios de aceitação em formato Dado/Quando/Então e matriz de rastreabilidade. Use depois que as regras foram validadas e antes de planejar a implementação.
---

# Requisitos e critérios de aceitação

Baseado no Capítulo 3 de *Código em Dupla* e na etapa de Engenharia de Requisitos da Esteira de Desenvolvimento ByteCod3. Rastreabilidade recomendada: RN → RF/RNF → AC → TC.

## Entradas
Regras confirmadas (RN-XXX), glossário, atores e, quando houver, a origem no processo (ATV, DEC).

## Passos
1. **Escreva histórias de usuário** apenas quando ajudarem a expressar valor.
2. **Especifique RF-XXX e RNF-XXX** sem ambiguidade, cada um apontando para a RN de origem.
3. **Crie critérios de aceitação AC-XXX** no formato Dado / Quando / Então.
4. **Cubra** caminho feliz, validações, limites, proibições, exceções, repetição (idempotência) e concorrência quando aplicáveis.
5. **Monte a matriz de rastreabilidade:** cada RN tem pelo menos um RF; cada RF tem pelo menos um AC.

## Regras
- Não invente metas mensuráveis ausentes: marque como lacuna.
- Requisitos devem ser testáveis e, quando possível, independentes da solução.
- Critério de aceitação descreve comportamento observável, não implementação.
- RNF precisa de condição, medida e forma de verificação.

## Saída
Histórias | RF | RNF | AC em Dado/Quando/Então | Dependências | Lacunas | Matriz de rastreabilidade.
