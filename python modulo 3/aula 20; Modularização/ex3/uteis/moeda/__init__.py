def metade(n, format):
    if format == False:
       return n/2
    if format == True:
        total = n/2
        return f'R${total:.2f}'.replace('.', ',')

def dobro(n, format):
    if format == False:
        return n*2
    if format == True:
        total = n*2
        return f'R${total:.2f}'.replace('.', ',')

def aumentar(n, a, format):
    if format == False:
        aumento = n * (a / 100)
        return n - diminuir
    if format == True:
        aumento = n * (a / 100)
        total = n + aumento
        return f'R${total:.2f}'.replace('.', ',')

def diminuir(n, d, format):
    if format == False:
        diminuir = n * (d / 100)
        return n - diminuir
    if format == True:
        diminuir = n * (d / 100)
        total = n - diminuir
        return f'R${total:.2f}'.replace('.', ',')