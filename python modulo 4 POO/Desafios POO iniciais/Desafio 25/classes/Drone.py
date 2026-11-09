from classes.Transporte import Transporte

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.5
        
    def calcular_frete(self):
        if self.distancia > 10:
            return f"Distância máxima = 10km"
        else:
            self.frete = self.fator * self.distancia
            return f"R${self.frete}"