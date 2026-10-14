"""
Camada VIEW
-----------
Responsável pela INTERAÇÃO com o usuário.

Captura as entradas (input), chama as operações do Model e usa os Templates
para exibir as informações na tela.
"""

import templates as t
from model import AlunoModel


class AlunoView:
    def __init__(self):
        self.model = AlunoModel()

    # ------------------------------------------------------------------
    # Menus e leitura de dados
    # ------------------------------------------------------------------
    def mostrar_menu(self):
        print(t.titulo("SISTEMA DE ALUNOS"))
        print("1. Listar alunos")
        print("2. Adicionar aluno")
        print("3. Editar aluno")
        print("4. Excluir aluno")
        print("0. Sair")

    def _ler_inteiro(self, prompt):
        while True:
            valor = input(prompt).strip()
            if valor.isdigit():
                return int(valor)
            print(t.erro("Digite um número válido."))

    # ------------------------------------------------------------------
    # Ações (chamam o Model)
    # ------------------------------------------------------------------
    def listar(self):
        print(t.titulo("LISTA DE ALUNOS"))
        print(t.tabela_alunos(self.model.listar()))

    def adicionar(self):
        print(t.titulo("ADICIONAR ALUNO"))
        nome = input("Nome: ").strip()
        while not nome:
            print(t.erro("O nome não pode ser vazio."))
            nome = input("Nome: ").strip()
        ano = input("Ano: ").strip()
        turma = input("Turma: ").strip()
        aluno = self.model.adicionar(nome, ano, turma)
        print(t.sucesso(f"Aluno '{aluno.nome}' adicionado com ID {aluno.id}."))

    def editar(self):
        print(t.titulo("EDITAR ALUNO"))
        print(t.tabela_alunos(self.model.listar()))
        id_ = self._ler_inteiro("ID do aluno a editar: ")
        aluno = self.model.buscar_por_id(id_)
        if aluno is None:
            print(t.erro("Aluno não encontrado."))
            return
        print(t.info(f"Editando '{aluno.nome}' (deixe em branco para manter)."))
        nome = input(f"Nome [{aluno.nome}]: ").strip() or None
        ano = input(f"Ano [{aluno.ano}]: ").strip() or None
        turma = input(f"Turma [{aluno.turma}]: ").strip() or None
        self.model.editar(id_, nome, ano, turma)
        print(t.sucesso("Aluno atualizado com sucesso."))

    def excluir(self):
        print(t.titulo("EXCLUIR ALUNO"))
        print(t.tabela_alunos(self.model.listar()))
        id_ = self._ler_inteiro("ID do aluno a excluir: ")
        aluno = self.model.buscar_por_id(id_)
        if aluno is None:
            print(t.erro("Aluno não encontrado."))
            return
        confirma = input(f"Confirma excluir '{aluno.nome}'? (s/n): ").strip().lower()
        if confirma == "s":
            self.model.remover(id_)
            print(t.sucesso("Aluno excluído com sucesso."))
        else:
            print(t.info("Operação cancelada."))

    # ------------------------------------------------------------------
    # Loop principal
    # ------------------------------------------------------------------
    def executar(self):
        acoes = {
            "1": self.listar,
            "2": self.adicionar,
            "3": self.editar,
            "4": self.excluir,
        }
        while True:
            self.mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "0":
                print(t.sucesso("Saindo... até mais!"))
                break
            acao = acoes.get(opcao)
            if acao:
                acao()
            else:
                print(t.erro("Opção inválida."))
            input("\nPressione ENTER para continuar...")
