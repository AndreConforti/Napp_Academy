# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores
from random import randint

vetorA = []
vetorB = []
vetorC = []

for i in range(10):
    valorA = randint(1, 9)
    vetorA.append(valorA)
    vetorC.append(valorA)
    valorB = randint(1, 9)
    vetorB.append(valorB)
    vetorC.append(valorB)

print(vetorA)
print(vetorB)
print(vetorC)