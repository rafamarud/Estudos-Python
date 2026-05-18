lista = [[], []]
for i in range(0, 7):

    numeros = int(input('Digite um numero: '))

    if numeros % 2 == 0:
        lista[0].append(numeros)
    if numeros % 2 != 0:
        lista[1].append(numeros)


print(f'Os valores pares adicionados foram {lista[0]}')
print(f'Os valores impares adicionados foram {lista[1]}')

print('')

print(f'Lista com pares e impares {lista}')
