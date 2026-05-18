dados = list()
pessoas = list()

maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar [S ou N]: ')).upper()
    if opcao == 'N':
        break

contador = 0
for p in pessoas:
    if contador == 0:
        maior = menor = p[1]
        maiornome = menornome = p[0]
    else:
        if p[1] > maior:
            maior = p[1]
            maiornome = p[0]
        if p[1] < menor:
            menor = p[1]
            menornome = p[0]
    contador += 1

print(f'Ao todo, voce cadastrou {len(pessoas)} pessoas.')



print(f'O maior peso foi de {maior}Kg. Peso de {maiornome} ')
print(f'O menor peso foi de {menor}Kg. Peso de {menornome} ')