from classes.Funcionario import Funcionario

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto, salario = 0, sal_min=1612, inss=7.5):
        super().__init__(nome, sal_bruto, salario, sal_min, inss)
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss

    def calc_sal(self):
        desconto = self.sal_bruto * self.inss / 100
        self.salario = self.sal_bruto - desconto
        return f"R${self.salario}"

    