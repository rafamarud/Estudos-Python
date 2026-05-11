import random

jogada = str(input('Pedra, Papel ou Tesoura: ')).lower().strip()

jogadas = ['Pedra', 'Papel', 'Tesoura']

computador = random.choice(jogadas).lower()

print(f'Voce jogou {jogada.capitalize()} e o computador jogou {computador.capitalize()}.')

if jogada == 'pedra' and computador == 'tesoura':
    print('Voce ganhou!!!')
elif jogada == 'tesoura' and computador == 'papel':
    print('Voce ganhou!!!')
elif jogada == 'papel' and computador == 'pedra':
    print('Voce ganhou!!!')
elif jogada == computador:
    print("Empate!!!")
else:
    print('Voce perdeu!!!')



