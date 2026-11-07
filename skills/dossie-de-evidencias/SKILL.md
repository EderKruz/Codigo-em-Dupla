---
name: dossie-de-evidencias
description: Monta um dossiê de evidências antes de declarar uma tarefa concluída - decompõe a entrega em alegações verificáveis e liga cada uma a uma evidência e a uma limitação. Use ao terminar qualquer alteração de código, antes de abrir ou atualizar um PR.
---

# Dossiê de evidências

Baseado no Capítulo 5 e no modelo A.5 de *Código em Dupla*. "Todos os testes passaram" não é conclusão: é uma evidência entre outras, que pode ou não alcançar o comportamento alterado.

## Passos
1. **Liste as alegações** da entrega: frases específicas e verificáveis sobre o comportamento ("conta alheia não recebe dados do pedido"), e não sobre o esforço ("implementei a correção").
2. **Para cada alegação, escolha a evidência adequada**: teste funcional, teste negativo, teste de contrato, análise estática, inspeção do diff ou observação em ambiente.
3. **Teste os testes.** Para cada teste novo, verifique se ele falha diante do defeito que deveria detectar (reverta a correção ou introduza a mutação). Teste que continua verde não protege nada.
4. **Revise o diff** procurando alterações fora do escopo do contrato, segredos, dados pessoais e regras de análise desativadas.
5. **Registre o que não foi verificado** e por quê. Suíte que não rodou não é suíte que passou.
6. **Entregue o dossiê** no formato abaixo, junto com o relatório de entrega.

## Formato

```
| Alegação | Evidência | Resultado | Limitação |
|---|---|---|---|
| [...] | [comando, teste ou inspeção] | [passou/falhou/não executado] | [o que a evidência não cobre] |

Não verificado: [itens e motivo]
Risco residual: [o que continua possível e quem deve saber]
Versão e ambiente: [commit, ambiente, data]
```

## Não fazer
- Não declarar a tarefa concluída sem o dossiê.
- Não usar linguagem ambígua ("deve funcionar", "provavelmente") no lugar de "não verificado".
- Não revisar o próprio trabalho como se fosse verificação independente: em mudança de risco, indique quem deve revisar.
