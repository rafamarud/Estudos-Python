"""
Camada MODEL (Modelo)
---------------------
Responsável pelos DADOS e pelas regras de persistência.

Define a entidade `Aluno` e a classe `AlunoModel`, que gerencia a lista de
alunos em memória e faz a leitura/escrita no arquivo `Alunos.txt`.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Aluno:
    """Entidade que representa um aluno."""
    id: int
    nome: str
    ano: str
    turma: str


class AlunoModel:
    """
    Gerencia a coleção de alunos e a persistência em arquivo texto.

    Formato de cada linha no arquivo:  id;nome;ano;turma
    Linhas iniciadas com '#' são comentários e são ignoradas.
    """

    SEPARADOR = ";"
    # O arquivo de dados fica na mesma pasta deste módulo.
    CAMINHO_ARQUIVO = Path(__file__).with_name("Alunos.txt")

    def __init__(self):
        self._alunos = []
        self.carregar()

    # ------------------------------------------------------------------
    # Persistência
    # ------------------------------------------------------------------
    def carregar(self):
        """Lê o Alunos.txt e popula a lista interna de alunos."""
        self._alunos = []
        if not self.CAMINHO_ARQUIVO.exists():
            return

        with self.CAMINHO_ARQUIVO.open("r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha or linha.startswith("#"):
                    continue
                partes = linha.split(self.SEPARADOR)
                if len(partes) != 4:
                    continue  # ignora linhas mal formatadas
                id_, nome, ano, turma = (p.strip() for p in partes)
                self._alunos.append(Aluno(int(id_), nome, ano, turma))

    def salvar(self):
        """Grava a lista atual de alunos de volta no Alunos.txt."""
        linhas = ["# Formato: id;nome;ano;turma"]
        for aluno in self._alunos:
            linhas.append(
                self.SEPARADOR.join(
                    [str(aluno.id), aluno.nome, aluno.ano, aluno.turma]
                )
            )
        self.CAMINHO_ARQUIVO.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    # ------------------------------------------------------------------
    # Operações (CRUD)
    # ------------------------------------------------------------------
    def listar(self):
        """Retorna uma cópia da lista de alunos."""
        return list(self._alunos)

    def proximo_id(self):
        """Gera o próximo id (maior id atual + 1)."""
        if not self._alunos:
            return 1
        return max(a.id for a in self._alunos) + 1

    def buscar_por_id(self, id_):
        """Retorna o aluno com o id informado ou None."""
        for aluno in self._alunos:
            if aluno.id == id_:
                return aluno
        return None

    def adicionar(self, nome, ano, turma):
        """Adiciona um novo aluno e persiste no arquivo."""
        aluno = Aluno(self.proximo_id(), nome, ano, turma)
        self._alunos.append(aluno)
        self.salvar()
        return aluno

    def remover(self, id_):
        """Remove o aluno pelo id. Retorna True se removeu, False se não achou."""
        aluno = self.buscar_por_id(id_)
        if aluno is None:
            return False
        self._alunos.remove(aluno)
        self.salvar()
        return True

    def editar(self, id_, nome=None, ano=None, turma=None):
        """
        Edita os campos informados do aluno (None mantém o valor atual).
        Retorna o aluno editado ou None se não existir.
        """
        aluno = self.buscar_por_id(id_)
        if aluno is None:
            return None
        if nome is not None:
            aluno.nome = nome
        if ano is not None:
            aluno.ano = ano
        if turma is not None:
            aluno.turma = turma
        self.salvar()
        return aluno
