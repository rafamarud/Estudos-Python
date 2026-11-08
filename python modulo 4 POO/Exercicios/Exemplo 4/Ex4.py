class Pessoa:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = " "
        self.turma = " "

    def fazer_matricula(self):
        print (f"{self.nome} acabou de fazer matrícula")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = " "
        self.nivel = " "

    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = " "
        self.setor = " "

    def bater_ponto(self):
        print(f"O funcionário {self.nome} bateu ponto")



a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
print(a1)

p1 = Professor("Samuesl", 37, "Biologia", "Mestrado")
p1.fazer_aniversario()
p1.dar_aula()

f1 = Funcionario("Rafael", 21, "Secretário", "Secretaria" )
f1.fazer_aniversario()
f1.bater_ponto()