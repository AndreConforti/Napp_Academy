'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
o salário bruto.
o quanto pagou ao INSS.
o quanto pagou ao sindicato.
o o salário líquido.
o calcule os descontos e o salário líquido, conforme a tabela abaixo: 
+ Salário Bruto : R$ 
- IR (11%) : R$ 
- INSS (8%) : R$ 
- Sindicato ( 5%) : R$ 
= Salário Liquido : R$
'''

valor_da_hora = float(input('Digite o valor que você ganha por hora: '))
horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_da_hora * horas
irrf = salario_bruto * 0.11
inss = salario_bruto * 0.08
sind = salario_bruto * 0.05
salario_liquido = salario_bruto - (irrf + inss + sind)

print(f'''
-------------------------------
+ Salário Bruto..: R$ {salario_bruto:.2f}
- IR.............: R$ {irrf:.2f}
- INSS...........: R$ {inss:.2f}
- Sindicato......: R$ {sind:.2f}
= Salário Líquido: R$ {salario_liquido:.2f}
-------------------------------
''')




