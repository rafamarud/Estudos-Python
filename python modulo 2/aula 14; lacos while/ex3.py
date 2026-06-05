v1 = float(input('Digite um numero: '))
v2 = float(input('Digite outro numero: '))

opcao = 0

while opcao != 5:
    print('MENU DE OPERAÇÕES: ')
    print('\n')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Comparar valores')
    print('[4] Inserir novos valores')
    print('[5] Sair do programa')

    print('\n')

    opcao = int(input('Escolha uma opção: '))


    match opcao:
            case 1:
                print(f'Soma = {v1+v2}')

            case 2:
                print(f'Multiplicação = {v1*v2}')
            
            case 3:
                if(v1 >v2):
                    print(f'O primeiro numero ({v1}) é maior que o segundo ({v2}).')
                else:
                    print('O segundo valor ({v2}) é maior que o primeiro ({v1}).')
            case 4:
                print('Insira os novos valores: ')

                print('\n')

                v1 = float(input('Digite um numero: '))
                v2 = float(input('Digite outro numero: '))

            case 5:
                print('Saindo... ')
            case _:
                print('Opção inválida!!!')

