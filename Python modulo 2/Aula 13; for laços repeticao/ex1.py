from time import sleep

c = int(input('Contagem regressiva: '))

for i in range(c, -1, -1):
    print(i)
    sleep(0.5)
print('\n')
print('Acabou')