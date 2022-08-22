'''
. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O
vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor
que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos
seguintes intervalos de valores:
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados
'''
from itertools import count

intervalos = ['a', 200, 'b', 300, 'c', 400, 'd', 500, 'e', 600, 'f', 700, 'g', 800, 'h', 900, 'i', 1000]
salarios = []
while True:

    venda_bruta = float(input('Valor total de vendas do funcionário: R$ '))
    if venda_bruta < 0:
        break

    salario = (200 + (venda_bruta * 9 / 100))
    
    print(f'Salário = R$ {salario}')

    for i, v in enumerate(intervalos):
        if i % 2 == 0:
            continue
        else:
            if v < salario < v + 100:
                print(intervalos[i-1])
                salarios.append(intervalos[i - 1])
            elif salario > v + 1000:
                print(intervalos[i - 1])
                salarios.append(intervalos[i - 1])
            

print(f'''
Resumo do salários dos vendedores:
a. $200 - $299 : {salarios.count('a')}
b. $300 - $399 : {salarios.count('b')}
c. $400 - $499 : {salarios.count('c')}
d. $500 - $599 : {salarios.count('d')}
e. $600 - $699 : {salarios.count('e')}
f. $700 - $799 : {salarios.count('f')}
g. $800 - $899 : {salarios.count('g')}
h. $900 - $999 : {salarios.count('h')}
i. $1000 em diante : {salarios.count('i')}
''')
print(salarios)

