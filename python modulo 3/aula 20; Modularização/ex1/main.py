from uteis import moeda

p = float(input('Digite um preço: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'A dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%: {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%: {moeda.diminuir(p, 13)}')