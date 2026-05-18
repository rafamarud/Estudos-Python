#lista = [ ]

#for i in range(0, 3):
    #pessoas = {'nome': 'Rafael', 'sexo': 'M', 'idade': 20}
    #lista.append(pessoas)



#print(lista)

#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#pessoas = {'nome': 'Rafael', 'sexo': 'M', 'idade': 20}
#lista.append(pessoas)
#pessoas ['nome'] = 'Leandro'
#pessoas['peso'] = 98.5
#for k, v in pessoas.items():
    #print(f'{k} = {v}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigra'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    
for e in brasil:
    for v in e.values():
        print(v, end = ' ')
    print() 