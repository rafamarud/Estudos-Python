matriz = []
soma = 0
soma1 = 0
maior = 0
for i in range(1, 4):
    linha = []
    for j in range(1, 4):
        valor = int(input(f'[{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

print('\n')

for linha in matriz:
    for valor in linha:
        print(f'[{valor}]', end='')
    print()

for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            soma += valor
print('Valor da soma dos pares: ', soma)


for i in range(3):
    soma1 += matriz[i][2]
print('Valor da soma da terceira coluna: ', soma1)


for j in range(3):
    if matriz[1][j] > maior:
        maior = matriz[1][j]

print('Maior valor da segunda linha: ', maior)

    