salario = float(input('Qual seu salario: '))

if salario < 1250:
    aumento = salario * 0.15
    novosalario = salario + aumento
    print(f'Novo salario: {novosalario}')
else:
    aumento = salario * 0.1
    novosalario = salario + aumento
    print(f'Novo salario: {novosalario}')