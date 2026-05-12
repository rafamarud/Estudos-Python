t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

count = 1

termo = t

while count <= 10:
    print(termo, end = ' -> ')
    termo += r
    count += 1

opcao = 2
while opcao != 0:
    opcao = (int(input('\nQuanto termos a mais voce quer ver: ')))
    if(opcao >= 0):
        count = 0
        while(count < opcao):
            print(termo, end = ' -> ')
            termo += r
            count += 1
    else:
        print('\nVoce pode digitar apenas numeros positivos!!!!')
print('\nPrograma encerrado.')


    