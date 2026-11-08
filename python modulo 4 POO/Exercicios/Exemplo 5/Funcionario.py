from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = " "
        self.setor = " "

    def bater_ponto(self):
        print(f"O funcionário {self.nome} bateu ponto")

    def estudar(self):
        print(f"O funcionario {self.nome} se especializa em {self.setor}.")
