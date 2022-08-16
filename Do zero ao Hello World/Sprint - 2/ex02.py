# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

from random import randint

numeros = []

for i in range(10):
    numeros.append(randint(0, 9))

numeros.sort(reverse=True)

print(numeros)