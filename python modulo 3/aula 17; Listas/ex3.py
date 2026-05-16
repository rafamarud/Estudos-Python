lista = []

while True:
    valor = int(input('Digite um valor: '))
    if len(lista) == 0:
        print('Adicionado ao final da lista...')
        lista.append(valor)
    else:
        for i in lista:
            if valor <= i:
                indice = lista.index(i)
                lista.insert(indice, valor)
                print(f'Adicionado na posição {indice}')
                break
        else:   
            lista.append(valor)
            print(f'Valor adicionado na posica {len(lista) - 1}')      
            

    print(lista)

