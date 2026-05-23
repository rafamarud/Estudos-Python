def teste():
    global x
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função tetste, x vale {x}')

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

# MAIN]
n = 2
x = 3
print(f'No programa principal, n vale {n}')

print(f'No programa principal, x vale {x}')

teste()

print()

print('Soma com valores opcionais')
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(4)

print(f'Os resultados foram {r1}, {r2} e {r3}')

