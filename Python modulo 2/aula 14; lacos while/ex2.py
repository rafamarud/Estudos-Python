from random import randint

computador = randint(0, 10)

numero = int(input('Pensei em um numero, tente advinhar: '))

while numero != computador:
    print('Voce errou!!')
    numero = int(input('Tente novamente: '))

print('Voce acertou!!')
print(f'O numero era {computador}.')