# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Digite um número: '))

if num < 0:
    print('Negativo')
elif num > 0:
    print('Positivo')
else:
    print('0')