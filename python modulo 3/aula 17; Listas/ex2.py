
valores = []
while True:
    numeros = int(input('Digite um valor: '))
    if numeros in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(numeros)
    
    opcao = str(input('Quer continuar? [S/N]')).upper()
    if opcao == 'N':
        break

print(f'Voce digitou os valores {sorted(valores)}')


    
       
   
    
            
    