frase =str(input('Digite uma frase: '))

frase.lower()

print(f'A letra A aperece {frase.count('a')} vezes na frase.')


print(f'A primeira letra A apareceu na posicao {frase.lower().find('a')+1}')

print(f'A ultima letra A apareceu na posicao {frase.lower().rfind('a')+1}')

