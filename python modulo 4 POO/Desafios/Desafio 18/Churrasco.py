class Churrasco:

    def __init__(self):
        self.pessoas = 0

    def analisar(self):
        peso = self.pessoas * 400
        pesokg = peso / 1000
        
        preco = self.pessoas * 82.4

        print(f"Quantidade de carne: {peso}G ou {pesokg}KG") 
        print(f"Total a se pagar: R${preco:.2f}")  