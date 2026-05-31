def leiaInt(n):
    while True:
        try:
            return int(input(n))
        except ValueError:
            print('ERRO!! Digite um numero inteiro.')


def linha(tam = 42):
   return '-'*tam

def cabeçalho(txt):
   print(linha())
   print(txt.center(42))
   print(linha())

def menu(lista):
   cabeçalho('MENU PRINCIPAL')
   c = 1
   for item in lista:
      print(f'{c} -- {item}')
      c += 1
   print(linha())
   opc = leiaInt('Sua opção: ')
   return opc