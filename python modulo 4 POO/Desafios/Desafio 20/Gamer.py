

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list = []

    def add_favoritos(self, game):
        self.favoritos.append(game)

    def status(self):
        print(f"\nJogador:")
        print(f"Nome: {self.nome}")
        print(f"Nick: {self.nick}")
        print(f"Lista de jogos favoritos: {self.favoritos}")