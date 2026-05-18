alunos = list()
dados = list()

media = 0
nota1 = 0
nota2 = 0

while True:
    dados = []
    dados.append(str(input("Nome: "))) 
    dados.append(int(input("Nota1: "))) 
    dados.append(int(input("Nota2: "))) 
    alunos.append(dados)

    opcao = str(input('Deseja continuar[S ou N]: ')).upper()
    if opcao == 'N':
        break
    

for i in range(0, len(alunos)):
    print(f'{i} {alunos[i]}', end= ' Media = ')
    nota1 = alunos[i][1]
    nota2 = alunos[i][2]

    media = (nota1 + nota2) / 2

    print(media)
    print()

while True:
    opcao2 = int(input('Mostar notas de qual aluno(999 para encerrar): '))
    if opcao2 == 999:
        break
    if 0 <= opcao < len(alunos):
        print(f'Notas de {alunos[opcao2][0]}: {alunos[opcao2][1:3]}')
    else:
        print('Nenhum aluno encontrado com esse indice.')