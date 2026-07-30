class Pessoa:
    """
    Essa classe cria uma pessoa, que tem nome e idade.

    Para cirar uma nova pessoa, use 

    variavel = Pessoa(nome, idade)
    """
    def __init__(self, nome="vazio", idade = 0): # Método Construtor
        self.nome = nome
        self.idade = idade

    # Métodos de Insttância
    def aniversario(self):
        self.idade += 1
    
    
    def __str__(self):
        return f"{self.nome} é uma pessoa e tem {self.idade} anos de idade"
    # Dunder Method

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"