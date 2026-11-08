from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = " "
        self.turma = " "

    def fazer_matricula(self):
        print (f"{self.nome} acabou de fazer matrícula")

    def estudar(self):
        print(f"O aluno {self.nome}, da turma {self.turma} está cursando {self.curso}.")