valores = []

contador = 0

while True:
    numero = int(input('Digite um numero: '))
    valores.append(numero)
    if numero == 5:
        contador += 1
    opcao = str(input('Quer continuar [S ou N]: ')).upper()
    if opcao == 'N':
        break
    


print(f'Voce digitou {len(valores)} elementos.')
print(f'Os volores em ordem decrescente são: ', end ='')
valores.sort(reverse = True)
print(valores)
if contador > 0:
    print(f'O numero 5 aparece {contador} vezes.')
if contador == 0:
    print('O numero 5 nao aparece na lista.')
