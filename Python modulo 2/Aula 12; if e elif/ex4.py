from datetime import date

ano = int(input('Digite seu ano de alistamento: '))

anoatual = date.today().year
idade = anoatual - ano

passou = idade - 18
falta = 18 - idade

if idade == 18:
    print('Deve se alistar.')
elif idade > 18:
    print(f'Ja se passaram {passou} anos do tempo do alistamento.')
else:
    print(f'Ainda falta {falta} anos para o alistamento')