totalgasto = produtos1000 = 0

maisbarato = 9999999

nomebarato = ''

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))

    produto = nome and preco

    totalgasto += preco

    if preco < maisbarato:
        maisbarato = preco
        nomebarato = nome

    if preco > 1000:
        produtos1000 += 1

    

    opcao = str(input('Deseja continuar?(S ou N): ')).upper().strip()
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar?(S ou N): ')).upper().strip()
    
    if opcao == 'N':
        print('Total gasto: R$ ', totalgasto)
        print('Quantidade de produtos acima de R$1000: ', produtos1000)
        print(f'Produto mais barato: {nomebarato}, custa R$ {maisbarato} ')
        break
    