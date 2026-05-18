## as alteracoes sao feitas nas duas listas
###teste = list()
##teste.append('Gustavo')
##teste.append(40)
##galera = list()
##galera.append(teste)
##teste[0] = 'Maria'
##teste[1] = 22
##galera.append(teste)
##print(galera)###

##alteracoes apenas feitas nas respectivas copias [:]
##teste = list()
##teste.append('Gustavo')
##teste.append(40)
##galera = list()
##galera.append(teste[:])
##teste[0] = 'Maria'
##teste[1] = 22
##galera.append(teste[:])
##print(galera)

##galera = [['Joao',19],['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
##print(galera[0][0]) ## apenas o nome do joao(indice 0 do indice 0)

##for p in galera:
    ##print(p)

##for p in galera:
    ##print(p[0])    ## apenas os nomes

##for p in galera:
    ##print(p[1])    ## apenas as idades


galera = list()
dado = list()
totmen = totmai = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'Maior idade: ',p[0])
        totmai += 1
    else:
        print(f'Menor idade: ', p[0])
        totmen += 1

print(f'{totmai} maiores de idade e {totmen} menores de idade')
    