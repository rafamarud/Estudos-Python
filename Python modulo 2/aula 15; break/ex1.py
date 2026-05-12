numero = soma = contador = 0


while numero != 999:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    contador += 1
    soma += numero

print('Programa encerrado!')

print('\n')

print(f'Total de numeros: {contador}')
print(f'Soma dos numeros: {soma}')