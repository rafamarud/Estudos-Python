distancia = float(input('Distancia da viagem: '))

if distancia <= 200:
     passagem = distancia * 0.50
     print(f'Valor da passagem: {passagem}')
else:
     passagem = distancia * 0.45
     print(f'Valor da passagem: {passagem}')