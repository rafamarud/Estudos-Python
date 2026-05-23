def notas(*notas, sit = True):
    dados = {}
    maior = menor = notas[0]
    soma = 0


    dados['total'] = len(notas)

    for i in notas:
        if i < menor:
            menor = i
        if i > maior:
            maior = i

    dados['maior'] = maior
    dados['menor'] = menor

    for i in notas:
        soma += i
    media = soma / len(notas)

    dados['media'] = media
    if sit:
        if dados['media'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['media'] >= 6:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    
    return dados


    
    

# MAIN

resp = notas(5.5, 9.5, 10, 6.5)
print(resp)