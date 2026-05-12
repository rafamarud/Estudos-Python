


##numero1 =  int(input("Digite um número: "))
##numero2 =  int(input("Digite outro: "))
##numero3 =  int(input("Digite mais: "))
##numero4 =  int(input("Digite um ulimo numero: "))

##numeros = (numero1, numero2, numero3, numero4)

numeros = tuple(int(input("Digite um número: ")) for _ in range(5))

contador = 0
for i in numeros:
    if i == 9:
        contador += 1
    
print(f'O numero 9 aparece {contador} vezes.')

if 3 in numeros:
    print(f'O numero 3 se encontra na posicao {numeros.index(3)}')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao.')

print('Numeros pares: ')
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
      
       
            


  

