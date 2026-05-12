print('IDENTIFICADOR DE PALÍNDROMOS: \n')

inverso = ''

frase = str(input('Digite uma frase: ')).strip().upper()

frasejunta = (frase.replace(' ', ''))


for letra in range(len(frasejunta) - 1, -1, -1):
    inverso += frasejunta[letra]

print(f'Palavra: {frasejunta}')
print(f'Palavra invertida: {inverso}')
if (inverso == frasejunta):
    print('A palavra é um palindromo!')
else:
    print('A palavra nao e um palindromo!')
