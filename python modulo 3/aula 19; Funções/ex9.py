def leiaInt(n):
    while True:
        dados = input(n)
        if dados.isdigit():
            return dados
            break
        else:
            print('ERRO!! Digite um inteiro.')

# MAIN
n = leiaInt('Digite um numero: ')


print(f'Voce acabou de digitar o numero {n}')