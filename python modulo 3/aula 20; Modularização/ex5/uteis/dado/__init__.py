def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')

        if entrada == '' or not entrada.replace('.', '', 1).isdigit():
            print(f'Aviso!!! {entrada} é um valor inválido.')
        else:
            return float(entrada)
            break
        
    