class Pessoa:
    def __init__(self): # Método Construtor
        self.nome = ""
        self.idade = 0

    # Métodos de Insttância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é uma pessoa e tem {self.idade} anos de idade"
    

