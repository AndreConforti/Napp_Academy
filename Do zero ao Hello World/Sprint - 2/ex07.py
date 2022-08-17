# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números

from ast import Mult
from random import randint

numeros = []
soma = 0
multiplica = 1

for i in range(5):
    numeros.append(randint(1, 9))

for n in numeros:
    soma += n
    multiplica *= n

print(numeros)
print(soma)
print(multiplica)