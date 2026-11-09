from classes.Poligono import Poligono
from classes.Quadrado import Quadrado
from classes.Circulo import Circulo

def main():
    q1 = Quadrado(8)
    print(q1.area())
    print(q1.perimetro())

    c1 = Circulo(5.5)
    print(c1.area())
    print(c1.perimetro())
    
if __name__ == "__main__":
    main()