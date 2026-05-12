numeroextenso = (
    "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

numero = int(input("Digite um numero de 1 a 20: "))


if numero < 1 or numero > 20:
    print('Numero inválido!!!')
       
else:
    print(numeroextenso[numero - 1])
        

