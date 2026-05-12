numero = int(input('Digite um numero qualquer: '))

print('MENU:\n')
print('Digite 1: para binario')
print('Digite 2: para octal')
print('Digite 3: para hexadecimal')

opcao = int(input('Selecione uma das opcoes: '))

if opcao == 1:
    print(bin(numero))  
elif opcao == 2:
    print(oct(numero))  
else:
    print(hex(numero))  