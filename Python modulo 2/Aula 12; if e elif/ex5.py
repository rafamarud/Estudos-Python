n = float(input('Primeira nota: '))
n1 = float(input('Segunda nota: '))

media = (n+n1) / 2

if media >= 7:
    print('Aprovado!!!')
elif media < 5:
    print('Reprovado!!!')
else:
    print('Recuperacao')