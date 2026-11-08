from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = " "
        self.nivel = " "

    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula")

    def estudar(self):
        print(f"Prof. {self.nome} é espcialista em {self.especialidade} e esta estudando no {self.nivel}.")
