from .Transporte import Transporte

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.2
        

    def calcular_frete(self):
      if self.distancia < 50:
        return f"Distancia mínima = 50km"
      else:
        self.frete = self.distancia * self.fator
        return f"R${self.frete}"