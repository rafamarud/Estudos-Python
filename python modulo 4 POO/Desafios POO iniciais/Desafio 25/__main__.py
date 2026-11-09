from classes.Transporte import *
from classes.Caminhao import *
from classes.Moto import *
from classes.Drone import *

dist = 100

entrega = Moto(dist)

print(f"Frete de {type(entrega).__name__} em {dist}KM = {entrega.calcular_frete()}")

