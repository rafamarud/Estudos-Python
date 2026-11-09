from .Poligono import Poligono

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def area(self):
        pi = 3.14
        area = pi * (self.raio * self.raio)
        return f"A area do circulo é {area}"

    def perimetro(self):
        pi = 3.14
        perimetro = 2 * pi * self.raio
        return f"O perimetro do circulo é {perimetro}"