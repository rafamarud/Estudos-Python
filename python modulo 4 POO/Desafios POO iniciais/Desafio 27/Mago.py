import random

from Personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio de Luz", "Magia Estática"]

        
    def curar(self):
        curas = ["Poção Mágica", "Ritual de Cura", "Magia de Regeneração"]
        cura = curas[random.randrange(0, len(curas))]
        fator = random.randint(0, 100)
        self.vida +=  fator
        print(f"{self.nome} utilizou uma {cura} e recuperou {fator} pontos de vida.")