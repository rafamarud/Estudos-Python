def maior(*num):
    maior = 0
    
    for i in num:
        if i > maior:
            maior = i
        
    print('Analisando os valores passados...')
    print(f'{num} Fora informados {len(num)} valores ao todo.')
    print(f'O maior valor inforamdo foi {maior}')

def linha():
    print('=-' * 30)


# MAIN

maior(2, 9, 4, 7, 1)
linha()
maior(4, 7, 0)
linha()
maior(1, 2)
linha()
maior(6)
linha()
maior()