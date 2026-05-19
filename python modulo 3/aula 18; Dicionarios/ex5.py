dados = dict()
lista = list()
mulheres = list()
idade_acima_media = list()
soma = 0

while True:
    
    dados = dict()

    dados['Nome'] = str(input('Nome: '))

    
    dados['Sexo'] = str(input('Sexo: [M;F] ')).upper().strip()


    dados['Idade'] = int(input('Idade: '))
    
    lista.append(dados)
    
    opcao = str(input('Quer continuar(S ou N): ')).upper().strip()
    if opcao == 'N':
        break

print(f'O grupo tem {len(lista)} pessoas')

for i in lista:
    soma += i['Idade']

media = soma / len(lista)
print(f'A média de idade é de {media} anos.')

for i in lista:
    if i['Sexo'] == 'F':
        mulheres.append(i['Nome'])
print(f'As mulheres cadastradas foram:{mulheres}')

for i in lista:
    if i['Idade'] > media:
        idade_acima_media.append(i)

print(f'Lista das pessoas com idade acima da média: {idade_acima_media} ')



