contador_sexo = contador_mulheres = contador_idade = 0

while True:
    sexo = str(input('Sexo(M ou f): ')).upper().strip()
    while sexo not in 'MF':
         sexo = str(input('Sexo(M ou f): ')).upper().strip()
    idade = int(input('Idade: '))

    if sexo == 'M':
        contador_sexo += 1
    if idade > 18:
        contador_idade += 1
    if sexo == 'F' and idade < 20:
        contador_mulheres += 1

    opcao = str(input('Deseja continuar?(S ou N): ')).upper().strip()
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar?(S ou N): ')).upper().strip()

    if opcao == 'N':
        print('Quantidade de homens: ',contador_sexo)
        print('Quantidade de pessoas com mais de 18 anos: ',contador_idade)
        print('Quantidade de mulheres com menos de 20 anos: ',contador_mulheres)
        break
    