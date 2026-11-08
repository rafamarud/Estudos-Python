from Pessoa import Pessoa
from Funcionario import Funcionario
from Aluno import Aluno
from Professor import Professor
from abc import ABC

def main():

    a1 = Aluno("José", 17, "Informática", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario("Rafael", 21, "Secretário", "Secretaria" )
    f1.fazer_aniversario()
    f1.bater_ponto()

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == "__main__":
    main()