# Desafio 01: Escreva um programa para aprovar o empréstimo bancário para a
#           compra de uma casa. Pergunte o valor da casa, o salário do comprador
#           e em quantos anos ele vai pagar. A prestação mensal não pode exceder
#           30% do salário ou então o empréstimo será negado.

casa = float(input('Informe o valor da casa: R% '))
salario = float(input('Informe o salário do comprador: R$ '))
anos = int(input('Anos de financiamento: '))
meses = anos * 12
limite = salario * 30 / 100
prestacao = casa / meses

if prestacao <= limite:
    print('Financiamento ACEITO!!!')
    print(f'A prestação será de R$ {prestacao:.2f}/mês durante {meses} meses.')
else:
    print('Financiamento NEGADO!!!')
    print(f'A prestação de R$ {prestacao:.2f}/mês está acima do limite de 30% do salário')
    print(f'O limite permitido seria de R$ {limite:.2f}/mês')