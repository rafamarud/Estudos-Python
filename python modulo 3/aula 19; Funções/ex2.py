def mensagem(txt):
    print('-' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('-' * (len(txt) + 4))

## MAIN

for i in range(3):
    frase = str(input('Digite uma frase: '))
    mensagem(frase)