contador = 0

soma = 0

numero = int(input('Digite um numero(999 para parar): '))

while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um numero(999 para parar): '))

print('Programa encerrado!')
print('\n')

print('Total de numeros: ',contador)
print('Soma dos numeros: ',soma)