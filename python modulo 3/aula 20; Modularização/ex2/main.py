from utilidade import moeda

print('Qual moeda voce deseja verificar: ')
print('1: Dolar')
print('2: Real')

opcao = int(input('Digite: '))

if opcao == 1:
    tipo = 'US$'
if opcao == 2:
   tipo = 'R$'

p = float(input(f'Digite um preço:{tipo} '))
print(f'A metade de {moeda.moeda(p, tipo)} é {moeda.moeda(moeda.metade(p))}')
print(f'A dobro de {moeda.moeda(p, tipo)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13%: {moeda.moeda(moeda.diminuir(p, 13))}')