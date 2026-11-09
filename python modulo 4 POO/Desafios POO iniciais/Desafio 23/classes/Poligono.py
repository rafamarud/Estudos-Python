from abc import ABC, abstractclassmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractclassmethod
    def perimetro():
        pass

    @abstractclassmethod
    def area():
        pass