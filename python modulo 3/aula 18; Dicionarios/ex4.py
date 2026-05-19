dados = dict()
gols = list()

total_gols = 0
dados['Nome'] = str(input('Nome do Jogador: '))

partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

for i in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {i + 1}: '))
    gols.append(gol)
    total_gols += gol
dados['Gols'] = gols

dados['Total'] = total_gols

print(dados)

print()

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')


print() 

print(f'O jogador {dados["Nome"]}, jogou {partidas} partidas')

for i in range(0, partidas):
    print(f'Na partida {i + 1}, fez {gols[i]} gol(s)')
print(f'Foi um total de {dados['Total']} gol(s).')