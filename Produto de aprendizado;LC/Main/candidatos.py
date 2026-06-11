def leiaOpcao():
        while True:
            try:
                opcao = int(input("Digite uma opção (1 a 5): "))
                
                if 1 <= opcao <= 5:
                    return opcao
                print("Opção inválida! Digite entre 1 e 5.")
                
            except ValueError:
                print("Digite apenas números!")
                

class candidato:
    def __init__(self, id, nome, idade, exp, tec, ing):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.exp = exp
        self.tec = tec
        self.ing = ing

    def __str__(self):
        return f"Dados do candidato: {self.id}. Nome:{self.nome}. Idade:{self.idade}. Exp:{self.exp}. Técnico:{self.tec}. Inglês:{self.ing}"
    
    