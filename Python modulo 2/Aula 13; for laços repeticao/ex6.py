t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

decimo = t + (10 - 1) * r 

for i in range(t,decimo + r,r):
    print(i, end = ' ---> ')
