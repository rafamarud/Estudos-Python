quantidade = 1
total = 0
a = 0
b = 1

while quantidade > 0:
    quantidade = int(input('\nQuantos numeros da sequencia de Fibonacci voce deseja ver(digite 0 para encerrar o programa): '))
    while total < quantidade:
        print(a, end = ' -> ')

        proximo = a + b
        a = b
        b = proximo
        total += 1
        
print('Programa encerrado.')
