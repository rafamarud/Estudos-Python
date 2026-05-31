def leiaInt(n):
    while True:
        try:
            return int(input(n))
        except ValueError:
            print('ERRO!! Digite um numero inteiro.')
        
        

def leiaFloat(n):
    while True:
        try:
            return float(input(n))
        except ValueError:
            print('ERRO!! Digite um numero real.')


inteiro = leiaInt('Digite um inteiro: ')
real = leiaFloat('Digite um numero real: ')

print(f'Inteiro = {inteiro}')
print(f'Real: {real}')
