nome = str(input('Digite seu nome: '))

if nome == 'Rafael':
    print('Que nome bonito!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal.')
print(f'Tenha um bom dia, {nome}!')