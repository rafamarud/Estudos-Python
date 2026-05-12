t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

count = 1

termo = t

while count <= 10:
    print(termo, end = '->')
    termo += r
    count += 1



