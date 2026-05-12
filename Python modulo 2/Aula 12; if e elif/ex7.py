l1 = int(input('Comprimento da reta1: '))
l2 = int(input('Comprimento da reta2: '))
l3 = int(input('Comprimento da reta3: '))

if l1+l2 > l3 and l1+l3 > l2 and l3+l2 > l1:
    print('As retas podem formar um triangulo!!!')
    if l1 == l2 == l3:
        print('Triangulo Equilatero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triangulo Isosceles!')
    else:
        print('Triangulo Escaleno!')
else:
    print('As retas nao podem formar um triangulo!!!')