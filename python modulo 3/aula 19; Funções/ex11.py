def InteractiveHelp(funcao):
    texto = f"Acessando o manual do comando '{funcao}'"
    tamanho = len(texto) + 4
    
    print('=' * tamanho)
    print(f'  {texto}  ')
    print('=' * tamanho)
    
    
    help(funcao)

def titulo():
    texto = 'SISTEMA DE AJUDA PYHELP'
    tamanho = len(texto) + 4
    print('=' * tamanho)
    print(f'  {texto}  ')
    print('=' * tamanho)

# MAIN
titulo()
while True:
    funcao = str(input('Função ou Biblioteca > ')).strip().lower()
    if funcao == 'fim':  
        break
    InteractiveHelp(funcao)