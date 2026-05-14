lista = []

while True:
    valor = int(input('Digite um valor: '))
    if len(lista) == 0:
        print('Adicionado ao final da lista...')
        lista.append(valor)
    for i in lista:
        if i < lista:
            print(f'Adicionado na posicao {} da lista.')
            lista.insert(lista.index(valor)-1, i)
        else:
            lista.insert(lista.index(valor)+1, i)
    

