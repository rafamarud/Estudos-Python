valor = float(input('Valor da casa: '))

salario = float(input('Salario do comprador: '))

anos = float(input('Em quantos anos ele ira pagar: '))

parcelas = anos * 12

valorparcelas = valor / parcelas

parcelamax = salario * 0.3

if valorparcelas > parcelamax:
    print('Emprestimo negado, parcelas acima de 30% do salario.')
else:
    print('Emprestimo aceito!!')