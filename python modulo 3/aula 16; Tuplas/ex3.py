from random import randint

numeros = tuple(randint(0,50) for x in range(10))

maior = menor  = numeros[0]

for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(numeros)

print('\n')

print('Maior numero: ',maior)
print('Menor numero: ',menor)


