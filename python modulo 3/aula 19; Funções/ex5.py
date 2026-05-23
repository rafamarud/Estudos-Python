from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando os 5 valores da lista...')
    for i in range(5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end = ' ', flush = True )
        sleep(0.3)
    print('PRONTO!!')

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i  
    print(f'Somando os valores pares de {lista}, temos {soma} ')

# MAIN

lista = []

sorteia(lista)

somaPar(lista)