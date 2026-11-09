from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia, frete = 0):
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass