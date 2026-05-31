lista = list()


while True:
    dados = dict()
    gols = list()
    total_gols = 0
    dados['Nome'] = str(input('Nome do Jogador: '))

    dados['partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

    for i in range(0, dados['partidas']):
        gol = int(input(f'Quantos gols na partida {i + 1}: '))
        gols.append(gol)
        total_gols += gol
    dados['Gols'] = gols

    dados['Total'] = total_gols

    lista.append(dados)
    
    opcao = str(input('Quer continuar(S ou N): ')).upper().strip()

    if opcao == 'N':
        break

print()

print(lista)

print()


for i in range(0, len(lista)):
    print(f'Jogaodr {i}  Nome:{lista[i]["Nome"]}  Gols:{lista[i]["Gols"]}  Total de gols:{lista[i]["Total"]}')
    print('='*50)

print() 

while True:
    codigo = int(input('Mostrar dados de qual jogador(999 para encerar):  '))
    if codigo == 999:
        break
    
    if codigo >= len(lista) or codigo < 0:
        print(f'ERRO! Não existe jogador com código {codigo}!')

    else:
        print(f'Levanamento do jogador {lista[codigo]["Nome"]}: ')
    
        for i in range(0, lista[codigo]['partidas']):
            print(f'Na partida {i + 1}, fez {lista[codigo]["Gols"][i]} gol(s)')
        print(f'Foi um total de {lista[codigo]["Total"]} gol(s).')


