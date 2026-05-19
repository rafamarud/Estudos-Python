from datetime import datetime

dados = dict()

ano_atual = datetime.now().year

dados['Nome']= str(input('Nome: '))
ano_nascimento = int(input('Ano des Nascimento: '))
idade = ano_atual - ano_nascimento
dados['Idade'] = idade

ctps = int(input('Carteira de Trabalho (0 nao tem): '))
if ctps != 0:
    dados['Ctps'] = ctps
    ano_contratacao = int(input('Ano de contratação: '))
    dados['Contratação'] = ano_contratacao
    dados['Salario'] = float(input('Salario: '))

    anos_trabalhados = ano_atual - ano_contratacao

    if anos_trabalhados >= 35:
        dados['Aposentadoria'] = 'Aposentado'
    else:
        idade_aposentadoria = (35 - anos_trabalhados) + dados['Idade']
        
        dados['Aposentadoria'] = idade_aposentadoria

else:
    dados['Ctps'] = 0

print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
        
