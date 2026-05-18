dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input('Media: '))

if dados['Media'] < 7:
        dados['Status'] = 'Reprovado'
else:
        dados['Status'] = 'Aprovado'

for k, v in dados.items():
    print(f'O {k} é igual a {v}')

