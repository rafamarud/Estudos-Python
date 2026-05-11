import random

numero = random.randint(1,5)

numero1 = int(input('Digite um numero de 1 a 5: '))

if numero1 == numero:
    print('Voce ganhou!!!')
else:
    print(f'Voce perdeu, o numero sorteado foi {numero}.')