from classes.Transporte import Transporte

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.5
    
    def calcular_frete(self):
        self.frete = self.fator * self.distancia
        return f"R${self.frete}"