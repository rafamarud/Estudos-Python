expressao = str(input('Digite um expressao: '))

contador1 = 0
contador2 = 0

for i in expressao:
    if '(' in i:
        contador1 += 1
for i in expressao:
    if ')' in i:
        contador2 += 1

if contador1 > contador2 or contador2 > contador1:
    print('Expressao invalida')
else:
    print('Expressao valida!')
