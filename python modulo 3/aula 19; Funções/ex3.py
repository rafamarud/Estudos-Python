from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        
        passo = 1
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}:')

    if inicio < fim:
        for i in range (inicio, fim + 1, passo): 
            print(i, end = ' ')
    
    if inicio > fim:
        for i in range (inicio, fim - 1, -passo): 
            print(i, end = ' ')

    print(' FIM!')

def linha():
    print('=-' * 30)

# MAIN

linha()
contador(1, 10, 1)

linha()
contador(10, 1, 2)

linha()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
intervalo = int(input('Intervalo: '))
contador(inicio, fim, intervalo)
