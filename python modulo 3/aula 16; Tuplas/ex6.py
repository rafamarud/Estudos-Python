palavras = (
    "sol", "lua", "floresta", "rio", "vento",
    "nuvem", "mar", "areia", "fogo", "estrela"
)

for i in range(len(palavras)):
    print(f'\nNa palavra {palavras[i]} vogais:',end = '');
    for v in palavras[i]:
        if v in 'aeiou':
            print(f'{v}' , end= ' ')
    
        
