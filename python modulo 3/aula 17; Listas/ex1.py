lista =[int(input('Digite um numero: '))for _ in range(5)] 

maior = menor = lista[0]

for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print('Maior numero:',+maior)
print('Nas posicoes ', end = '')
for i in range(len(lista)):
    if lista[i] == maior:
        print(f'{i:.<3}', end = '')

print('')

print('Menor numero:',+menor)
print('Nas posicoes:', end = '')

for i in range(len(lista)):
    if lista[i] == menor:
        print(f'{i:.<3}', end = '')


