nota1 = nota10 = nota20 = nota50 = 0



while True:
    valor = float(input('Quanto voce deseja sacar: '))
    nota50 = valor // 50
    valor %= 50

    nota20 = valor // 20
    valor %= 20

    nota10 = valor // 10
    valor %= 10

    nota1 = valor // 1
    valor %= 1

    print('Voce recebeu: \n')

    print('Notas de 50 reais: ',int(nota50))
    print('Notas de 20 reais: ',int(nota20))
    print('Notas de 10 reais: ',int(nota10))
    print('Notas de 1 real: ',int(nota1))

    opcao = str(input('Deseja realizar um novo saque?(S ou N): ')).upper().strip()
    if opcao == 'N':
        break
