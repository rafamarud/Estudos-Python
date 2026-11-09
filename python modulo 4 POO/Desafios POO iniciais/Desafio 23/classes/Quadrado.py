from .Poligono import Poligono

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado


    def area(self):
        area = self.lado * self.lado
        return f"A area do quadrado é {area}"


    def perimetro(self):
            perimetro = self.lado * 4
            return f"O perimetro do quadrado é {perimetro}"