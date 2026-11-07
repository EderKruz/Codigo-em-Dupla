---
name: contrato-de-tarefa
description: Escreve um contrato de tarefa (objetivo, escopo, fontes, invariantes, comandos, condições de parada) antes de alterar código. Use no início de qualquer tarefa que vá modificar arquivos, ou quando o pedido for vago.
---

# Contrato de tarefa

Baseado no Capítulo 4 e no modelo A.3 de *Código em Dupla*. O objetivo é tornar explícito o que será feito, dentro de quais limites e como se saberá que terminou, **antes** de qualquer edição.

## Quando usar
- Antes de alterar código em qualquer tarefa que não seja trivial e reversível.
- Quando o pedido couber em uma frase e não disser o que conta como pronto.

## Passos
1. **Releia o pedido** e escreva o resultado esperado como comportamento observável, não como solução técnica.
2. **Mapeie antes de propor.** Leia os arquivos relevantes, os testes existentes e as instruções persistentes (`AGENTS.md`). Separe fatos (vistos no código ou na documentação), hipóteses e perguntas.
3. **Preencha o contrato** com os campos abaixo e mostre à pessoa responsável.
4. **Pare e pergunte** se houver pergunta aberta que afete comportamento, ou se a tarefa exigir tocar área sensível.
5. Só comece a editar depois que o contrato for aceito. Se a investigação mudar o plano, atualize o contrato e avise.

## Formato do contrato

```
Objetivo: [resultado observável]
Escopo: [arquivos e módulos que podem mudar]
Fora do escopo: [o que não será tocado]
Fontes com autoridade: [especificação, ADRs, contratos]
Invariantes: [o que deve continuar verdadeiro]
Comandos de verificação: [testes rápidos, suíte completa, análise]
Nível de autonomia: [0–5, conforme a escala do livro]
Condições de parada: [quando interromper e pedir decisão]
Entregáveis: [diff, testes, relatório de entrega]
Perguntas abertas: [o que falta decidir e quem decide]
```

## Não fazer
- Não preencher "Perguntas abertas" com suposições: se é pergunta, fica como pergunta.
- Não ampliar o escopo durante a execução sem atualizar o contrato.
