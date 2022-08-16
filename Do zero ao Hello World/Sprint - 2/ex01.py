from random import randint

numeros = []

for i in range(5):
    numeros.append(randint(0, 10))

numeros.sort()
print(numeros)