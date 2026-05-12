listagem = (
    'Pão', 1.00,
    'Leite', 3.50,
    'Frango', 10.90,
    'Arroz', 22.00,
    'Feijão', 8.50,
    'Macarrão', 4.20,
    'Açúcar', 5.10,
    'Café', 14.30,
    'Manteiga', 7.80,
    'Queijo', 12.40
)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R$ {listagem[i]}')