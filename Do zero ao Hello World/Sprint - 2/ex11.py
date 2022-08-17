# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores
from random import randint

vetorA = []
vetorB = []
vetorC = []
vetorD = []

for i in range(10):
    valorA = randint(1, 9)
    vetorA.append(valorA)
    vetorD.append(valorA)
    valorB = randint(1, 9)
    vetorB.append(valorB)
    vetorD.append(valorB)
    valorC = randint(1, 9)
    vetorC.append(valorC)
    vetorD.append(valorC)

print(vetorA)
print(vetorB)
print(vetorC)
print(vetorD)