# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês

valor_da_hora = float(input('Digite o valor que você ganha por hora: '))
horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario = valor_da_hora * horas

print(f'Se você trabalhou {horas:.1f} horas a R$ {valor_da_hora:.2f} por hora, seu salário é de R$ {salario:.2f} neste mês.')