from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto, salario = 0, sal_min = 1612, inss = 7.5):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss
        
       
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        equivale = self.salario / self.sal_min 
        return print(f"O salário de {self.nome} ({type(Funcionario).__name__}) é de {self.salario} e corresponde a {equivale:.2f} salários mínimos")