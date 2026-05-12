maioridade = 0

for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    if(ano > 2008):
        maioridade += 1


print(f'{maioridade} pessoas não atingiram a maioridade')