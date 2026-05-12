tabela = (
    "Palmeiras",
    "Fluminense",
    "Flamengo",
    "São Paulo",
    "Athletico-PR",
    "Bahia",
    "Coritiba",
    "Botafogo",
    "Bragantino",
    "Vasco",
    "Grêmio",
    "Cruzeiro",
    "Vitória",
    "Corinthians",
    "Atlético-MG",
    "Internacional",
    "Santos",
    "Mirassol",
    "Remo",
    "Chapecoense"
)

print("Primeiros 5 colocados: ")
for i in range(0, 5):
    print(tabela[i])
    i+= 1

print('\n')

print("Ultimos 5 colocados: ")
for i in range(15, 20):
    print(tabela[i])
    i+= 1 

print('\n')

print('Tabela em ordem afabética:')
print(sorted(tabela))

print('\n')

time = str(input('Digite um time para saber sua posicao: ')).capitalize()
print(tabela.index(time)+1)

