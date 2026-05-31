from uteis import moeda

p = float(input('Digite um preço: '))
print(f'A metade de {p} é {moeda.metade(p, True)}')
print(f'A dobro de {p} é {moeda.dobro(p, False)}')
print(f'Aumentando 10%: {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%: {moeda.diminuir(p, 13, False)}')