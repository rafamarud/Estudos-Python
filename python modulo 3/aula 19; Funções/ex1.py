def calcularArea(B, H):
    area = B * H
    print(f'A área de um terreno {B}x{H} é de {area}m2.')

#main
print(' Controle de terrenos')
print('-' *30)

largura = float(input('Largora (m): '))

comprimento = float(input('Comprimento (m): '))

calcularArea(largura, comprimento)