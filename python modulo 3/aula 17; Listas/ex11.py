from random import randint

sorteios = list()

jogos = int(input('Quantos jogos voce quer que eu sorteie: '))


contador = 0
while contador < jogos:
    sorteios = []
    while len(sorteios) < 6:
        numeros = randint(1, 60)
        if numeros not in sorteios:
            sorteios.append(numeros)
    
    print(sorteios)

    contador += 1

