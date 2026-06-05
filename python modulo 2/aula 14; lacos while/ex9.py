opcao = 'S'

soma = 0

numero = 0

contador = 0

maior = -9999

menor = 9999999999

while opcao != 'N':
    numero = float(input('Digite um numero: '))
    opcao = str(input('Deseja continuar?(S ou N): ')).upper().strip()
    soma += numero
    contador += 1

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print('Programa encerrado!')
print('\n')

print(f'A media dos numeros digitados = {soma/contador:.2f}')
print(f'Maior numero = {maior}')
print(f'Menor numero = {menor}')