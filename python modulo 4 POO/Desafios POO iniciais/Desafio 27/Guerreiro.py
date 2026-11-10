import random

from Personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de Machado", "Pulo Giratório"]
    
    def curar(self):
        curas = ["Atadura", "Poção de cura", "Bandagem"]

        cura = curas[random.randrange(0, len(curas))]
        fator = random.randint(0, 100)
        self.vida +=  fator
        print(f"{self.nome} utilizou uma {cura} e recuperou {fator} pontos de vida.")