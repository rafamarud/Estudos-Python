numero = int(input('Digite um numero para verificar se ele é primo: '))
tot = 0

for i in range(1, numero + 1):
    if(numero % i == 0):
        tot += 1


if(tot == 2):
    print('O numero é primo.')
else:
    print('O numero não é primo')