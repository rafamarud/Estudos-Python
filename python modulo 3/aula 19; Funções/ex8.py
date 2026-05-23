def ficha(nome = 'Não informado ', gols = 0):
    print('Ficha do jogador: ')
    print(f'Nome: {nome}')
    if gols == 0:
        print('Gols: 0 (ou não informados)')
    else:
        print(f'Gols: {gols}')

print('-' * 30)

nome = str(input('Nome do Jogador: '))
gols = int(input('Número de Gols: '))

ficha(nome, gols)

print()

ficha()