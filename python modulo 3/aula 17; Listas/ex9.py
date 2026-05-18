matriz = []

for i in range(1, 4):
    linha = []
    for j in range(1, 4):
        valor = int(input(f'[{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        print(f'[{valor}]', end='')
    print()