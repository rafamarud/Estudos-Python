tempo = int(input('Quantos anos seu carrotem: '))

if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')

##OU

print('Carro novo' if tempo <=3 else 'Carro velho')
