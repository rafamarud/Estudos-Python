def contador(i, f, p):
    """Faz uma contagem e mostra na tabela.

    Args:
        i (int): Início da contagem
        f (int): Fim da contagem
        p (int): Intervalos da contagem
    """

    if p == 0:
        
        p = 1
    print(f'Contagem de {i} ate {f} de {p} em {p}:')

    if i < f:
        for i in range (i, f + 1, p): 
            print(i, end = ' ')
    
    if i > f:
        for i in range (i, f - 1, -p): 
            print(i, end = ' ')

    print(' FIM!')

contador(2, 10 ,2)

help(contador)
    

    

