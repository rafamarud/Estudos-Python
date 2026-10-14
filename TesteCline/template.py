"""
Camada TEMPLATE
---------------
Responsável por FORMATAR como os dados são exibidos.

Aqui ficam apenas as "máscaras" de saída (títulos, tabelas, mensagens).
Não há regra de negócio nem captura de dados do usuário.
"""


def titulo(texto, largura=52):
    """Retorna um título centralizado com linhas decorativas."""
    linha = "=" * largura
    return f"\n{linha}\n{texto.center(largura)}\n{linha}"


def tabela_alunos(alunos):
    """Retorna uma string com a tabela formatada dos alunos."""
    if not alunos:
        return "Nenhum aluno cadastrado."

    cabecalho = f"{'ID':<5}{'NOME':<28}{'ANO':<6}{'TURMA':<6}"
    separador = "-" * len(cabecalho)
    linhas = [cabecalho, separador]

    for a in alunos:
        nome = a.nome if len(a.nome) <= 27 else a.nome[:24] + "..."
        linhas.append(f"{a.id:<5}{nome:<28}{a.ano:<6}{a.turma:<6}")

    return "\n".join(linhas)


def sucesso(msg):
    return f"[OK] {msg}"


def erro(msg):
    return f"[ERRO] {msg}"


def info(msg):
    return f"[INFO] {msg}"
