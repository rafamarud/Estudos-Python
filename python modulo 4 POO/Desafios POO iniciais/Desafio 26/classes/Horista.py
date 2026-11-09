from classes.Funcionario import Funcionario

class Horista(Funcionario):
    def __init__(self, nome, horas_trab, valor_hora, sal_bruto = 0, salario = 0,sal_min = 1612, inss = 7.5):
        super().__init__(nome, sal_bruto)
        self.horas_trab = horas_trab
        self.valor_hora = valor_hora
      
       

    def calc_sal(self):
        self.sal_bruto = self.horas_trab * self.valor_hora
        desconto = self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - desconto
        return f"R${self.salario}"

    