from datetime import date

def voto(ano):
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade < 18:
        print(f'Com {idade} anos: VOTO NEGADO!')
    if idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')

# main

ano = int(input('Em que ano voce nasceu: '))

voto(ano)