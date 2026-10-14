# Projeto Alunos (padrão MVT)

Projeto de console em Python que gerencia alunos, organizado no padrão **MVT**
(Model - View - Template), o mesmo usado no Django, mas aqui aplicado a uma
aplicação de terminal.

## Estrutura de arquivos

| Arquivo      | Camada      | Responsabilidade                                          |
|--------------|-------------|-----------------------------------------------------------|
| `model.py`   | **Model**   | Classe `Aluno` + persistência (leitura/escrita no `.txt`) |
| `template.py`| **Template**| Formatação da saída (títulos, tabela, mensagens)          |
| `view.py`    | **View**    | Interação com o usuário (menu, inputs) e orquestração     |
| `main.py`    | Entry point | Inicia a aplicação                                        |
| `Alunos.txt` | Dados       | Base em texto com 20 alunos iniciais                     |

## Formato do `Alunos.txt`

Cada linha representa um aluno no formato: `id;nome;ano;turma`
Linhas que começam com `#` são comentários e são ignoradas na leitura.

## Como executar

Abra o terminal dentro da pasta do projeto e rode:

```
py main.py
```

## Funcionalidades

- Listar todos os alunos (carregados do `Alunos.txt`)
- Adicionar aluno (id gerado automaticamente)
- Editar aluno (deixe o campo em branco para manter o valor atual)
- Excluir aluno (com confirmação)

Todas as alterações são salvas automaticamente no `Alunos.txt`.
