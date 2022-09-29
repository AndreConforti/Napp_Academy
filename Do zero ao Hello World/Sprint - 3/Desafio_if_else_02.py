# Desafio 02: Escreva um programa que leia dois números inteiros e compare-os.
#           mostrando na tela uma mensagem:
#             - O primeiro valor é maior
#             - O segundo valor é maior
#             - Não existe valor maior, os dois são iguais

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 > num2:
    print(f'O PRIMEIRO número, "{num1}", é MAIOR')
elif num2 > num1:
    print(f'O SEGUNDO número, "{num2}", é MAIOR')
else:
    print('Não existe valor maior, os dois são iguais')
