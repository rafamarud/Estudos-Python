from random import randint
from time import sleep

computador = randint(0, 10)

jogador = ''

contador_vitoria = 0
contador_derrota = 0

soma = 0



while True:
    opcao = str(input('Voce quer par ou impar(P ou I): ')).upper().strip()
    if opcao != 'P' and opcao != 'I':
        print('Opcao inválida.')
        break

    if opcao == 'P':
        jogador = 'par'
    else:
        jogador = 'impar'
    
    numero = int(input('Digite um numero (maximo 10): '))
    print('\n')
    print('Par')
    sleep(1)
    print('ou')
    sleep(1)
    print('Impar!!!')
    sleep(1)

    print(f'\nVoce jogou: {numero}')
    print(f'\nComputador jogou: {computador} \n')

    soma = numero + computador

    if jogador == 'par' and soma % 2 == 0:
        print('Voce venceu!!')
        print(f'{numero} + {computador} = {numero + computador}')
        contador_vitoria += 1

    elif jogador == 'impar' and soma % 2 == 0:
        print('Voce venceu!!')
        print(f'{numero} + {computador} = {numero + computador}')
        contador_vitoria += 1

    else:
        print('Voce perdeu!!!')
        print(f'{numero} + {computador} = {numero + computador}')
        print('\n')
        print(f'Voce teve {contador_vitoria} vitoria(s) seguidas!!')
        contador_derrota += 1

    if contador_derrota > 0:
        break


    