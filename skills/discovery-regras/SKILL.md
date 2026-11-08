---
name: discovery-regras
description: Extrai e formaliza regras de negócio a partir de material bruto (atas, processos, documentos, código), separando o que foi identificado, inferido e proposto. Use quando uma demanda chega sem regras claras, antes de escrever requisitos ou código.
---

# Discovery de regras de negócio

Baseado no Capítulo 3 de *Código em Dupla* e na etapa de Discovery da Esteira de Desenvolvimento ByteCod3. O objetivo é transformar observações em regras formais e rastreáveis, sem transformar hipótese em regra.

## Passos
1. **Identifique a linguagem do domínio:** termos, atores e conceitos, como o negócio os usa.
2. **Liste as regras observadas como candidatas (RN-CAND-XXX)**, cada uma com a fonte de onde veio (documento, trecho de código, fala registrada).
3. **Classifique cada afirmação:** IDENTIFICADO (visto em fonte localizável), INFERIDO (deduzido, não confirmado) ou PROPOSTO (sugestão sua).
4. **Formalize as regras confirmadas (RN-XXX)** com declaração, condição, exceção, origem e impacto. Preserve o vínculo com a candidata de origem (RN-CAND-007 → RN-012).
5. **Classifique por tipo:** invariante, validação, cálculo, política, temporal, autorização, elegibilidade ou priorização.
6. **Registre lacunas como perguntas objetivas** para quem tem autoridade de decidir.

## Regras
- Não promova RN-CAND para RN sem evidência ou confirmação de quem decide.
- Não invente SLA, limite, cálculo, prazo ou base legal.
- Não misture regra de negócio com detalhe técnico de implementação.
- Toda RN confirmada indica sua fonte.

## Saída
Glossário | Atores | RN confirmadas | RN-CAND promovidas e rejeitadas | Lacunas e perguntas | Resumo para a etapa de requisitos.
