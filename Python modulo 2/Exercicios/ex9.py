valor = float(input('Valor do produto: '))

print('Opcoes de pagamento\n')

print('Digite 1 para: A vista (10% de desconto)')
print('Digite 2 para: A vista no cartao (5% de desconto)')
print('Digite 3 para: Em 2x no cartao (sem juros)')
print('Digite 4 para: Em 3x no cartao (20% de juros)')

opcao = int(input('Escolha um metodo de pagamento: '))

if opcao == 1:
    desconto = valor * 0.1
    print(f'Valor total a pagar: {valor - desconto}')
elif opcao == 2:
    desconto = valor * 0.05
    print(f'Valor total a pagar: {valor - desconto}')
elif opcao == 3:
    parcelas = 2
    valorparcelas = valor / parcelas
    print(f'Valor total a pagar: {valor}')
    print(f'Valor das parcelas: {valorparcelas}')
elif opcao == 4:
    parcelas = 3
    acrescimo = valor * 0.2
    valortotal = valor + acrescimo
    print(f'Valor total a pagar: {valortotal}')
    valorparcelas = valortotal / parcelas
    print(f'Valor das parcelas: {valorparcelas}')