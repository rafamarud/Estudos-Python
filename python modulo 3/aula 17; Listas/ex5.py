lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    
    opcao = str(input('Quer conitnuar [S ou N]:')).upper()
    if opcao == 'N':
        break

impares = lista[:]
for i in impares:
    if i % 2 == 0:
        impares.remove(i)

pares = lista[:]    
for i in pares:
    if i % 2 != 0:
        pares.remove(i)


print('Lista: ', lista)

if len(pares) == 0:
    print('Lista pares: [A lista esta vazia.]')
else: 
    print('Lista pares: ', pares)

if len(impares) == 0:
    print('Lista impares: [A lista esta vazia.]')
else:
    print('Lista impares: ', impares)

