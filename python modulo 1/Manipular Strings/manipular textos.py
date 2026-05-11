frase = 'Curso em Vídeo Python'
print(frase[0:15:2]) ## frase(`condicao de inicio`: `condicao de prada`:`espacos a serem pulados`)

print(frase.count('O')) ## contar caracteres desejados

print(frase.upper().count('O')) ##trnasforma para maiuscula

print(len(frase)) ## quantos caracteres tem(contandoo espacos)

print(frase.replace('Python','Java')) ## troca caracteres desejados
## replace apenas muda temporariamente, a string continua imutavel

print(frase.find('Curso')) #3posicao em que se encontra

print(frase.find('curso'))

print(frase.lower().find('curso'))

print(frase.split())

dividido = frase.split()

print(dividido[0])

print(dividido[2][3]) #pega o elemento 2 e mostra o terceiro caractere