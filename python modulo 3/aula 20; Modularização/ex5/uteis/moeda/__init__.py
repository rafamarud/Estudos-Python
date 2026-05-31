def resumo(n, acrescimo, decrescimo):
    metade = n / 2
    dobro = n * 2

    aumento = n * (acrescimo / 100)
    totalaumento = n + aumento

    diminuir = n * (decrescimo / 100)
    totaldiminuir = n - diminuir

    print('    RESUMO DO VALOR    ')
    
    print(f'Dobro: R${dobro:>.2f}'.replace('.', ','))
    print(f'Metade: R${metade:>.2f}'.replace('.', ','))
    print(f'Acrescimo de {acrescimo}%: R${totalaumento:>.2f}'.replace('.', ','))
    print(f'Decrescimo de {decrescimo}%: R${totaldiminuir:>.2f}'.replace('.', ','))
    
