peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(metros):'))

imc = peso/ (altura * altura)

if imc < 18.5:
    print(f'IMC = {imc:.2f}. Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f'IMC = {imc:.2f}.Peso ideal!')
elif imc >= 25 and imc < 30:
    print(f'IMC = {imc:.2f}.Sobrepeso!')
elif imc >= 30 and imc < 40:
    print(f'IMC = {imc:.2f}.Obesidade')
else:
    print(f'IMC = {imc:.2f}.Obesidade morbida')