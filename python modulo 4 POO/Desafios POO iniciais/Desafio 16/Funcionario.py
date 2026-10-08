class Funcionario:

    def __init__(self):
        self.nome = " "
        self.setor = " "
        self.cargo = " "

    def apresentar(self):
        print("Apresentação do Funcionario:")
        print(f"Nome: {self.nome}")
        print(f"Setor: {self.setor}")
        print(f"Cargo: {self.cargo}")
        