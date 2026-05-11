velocidade = int(input('Velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) 
    print('Veiculo multado!!')
    print(f'Valor da multa: R${multa*7:.2f}')
else:
    print('Velocidade permitida')

