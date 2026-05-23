def linha():
    print('-='*30)

def mensagem(texto):
    print('-----------------------')
    print(f'       {texto}        ')
    print('-----------------------')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

def somar(a, b,c = 0):
    print('Soma com valores opcionais')
    s = a + b + c
    print('A soma vale: ', s)
    

def contador(*num):
    print(f'Recebi os valores {num}')
    print(f'Ao todo são {len(num)} numeros')

def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1
    print(f'Lista com valores dobrados: {lst}')

def somavalores(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}')

## MAIN
valores = [6, 3 , 9, 1, 0, 2]
frase = str(input('Digite uma frase: '))

mensagem(frase)


soma(4, 5)
soma(b = 4, a = 5)

print()

contador(4, 3 ,2 ,1)
linha()
contador(2, 3)
linha()
contador(1)

print ()

dobrar(valores)

print()

somavalores(4, 3, 2, 1, 5, 10)

print()

somar(3, 4)
