# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

from random import randint

numbers = []
even = []
odd = []

for i in range(20):
    number = randint(0, 9)
    numbers.append(number)
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

numbers.sort()
even.sort()
odd.sort()

print(f'Números: {numbers}')
print(f'Pares  : {even}')
print(f'Ímpares: {odd}')