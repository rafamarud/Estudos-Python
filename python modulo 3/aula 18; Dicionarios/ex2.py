from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
for i in range(0, 4):
    nome_jogador = f'Jogador {i+1}'
    jogo[nome_jogador] = randint(1,6)

ranking = list()
print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)