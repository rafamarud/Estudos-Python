class Produto:

    def __init__(self):
        self.nome = " "
        self.preco = " "
        self.codigo = " "

    def __repr__(self):
        return f"Produto(Nome: {self.nome}, Preço: {self.preco}, Código: {self.codigo})"

    