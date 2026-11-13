# Ferramentas do livro

Scripts usados para produzir as figuras e manter sumário e índice do livro. Ficam aqui porque o livro defende o mesmo princípio para qualquer artefato gerado com apoio de agentes: o resultado precisa ser reproduzível e revisável.

## Figuras (`figuras/`)
Requisitos: Python 3, matplotlib e a fonte Inter instalada.

| Script | O que gera |
|---|---|
| `figuras.py` | As aberturas de parte e as figuras 2, 3, 4, 6, 8 a 12 e 15 a 17, em tons de cinza, nas proporções usadas no livro |
| `figura_fitkruz.py` | Figura 14, fluxo de proposta do Treinador do FitKruz |
| `figuras_metodo.py` | Figuras 1, 5, 7 e 13 (Método DUPLA, encaixe dos modelos, cadeia de evidência e escala de autonomia). Uso: `python3 figuras_metodo.py <pasta-de-saída>` |

Convenção visual (pensada para impressão em cinza): borda grossa e fundo branco indicam pessoa ou decisão; fundo cinza-claro, agente ou etapa técnica; cinza-médio com borda grossa, ênfase; tracejado, algo incerto ou externo.

## Livro (`livro/`)
Requisitos: Python 3, LibreOffice e poppler-utils (`pdftotext`).

| Script | Uso |
|---|---|
| `gerar_pdf.py` | Abre o .docx no LibreOffice, atualiza sumário e índices e exporta o PDF: `python3 gerar_pdf.py livro.docx livro.pdf` |
| `indice_remissivo.py` | Recalcula as páginas do índice remissivo a partir do PDF: `pdftotext livro.pdf livro.txt` e depois `python3 indice_remissivo.py livro.docx livro.txt saida.docx` |
| `termos_indice.py` | Lista de termos e padrões de busca do índice |
| `sumario_campo.py` | Converte um sumário escrito à mão em campo de sumário do Word |
| `miolo_cinza.py` | Converte cores de texto, fundos e bordas do .docx para tons de cinza |

Fluxo recomendado depois de qualquer mudança no texto: gerar o PDF, recalcular o índice, gerar o PDF de novo e conferir se o índice não mudou (se mudou, repetir uma vez).
