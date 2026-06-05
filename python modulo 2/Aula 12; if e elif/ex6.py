from datetime import date

ano = int(input('Ano de nascimento: '))

anoatual = date.today().year

idade = anoatual - ano

if idade <= 9:
    print('Sua categoria: Mirim')
elif idade <= 14:
    print('Sua categoria: Infantil')
elif idade <= 19:
    print('Sua categoria: Junior')
elif idade == 20:
    print('Sua categoria: Senior')
else:
    print('Sua categoria: Master')