from random import randint

numeros = []

for i in range(10):
    numero = randint(1, 10)
    print(numero, end=' ')
    numero *= numero
    numeros.append(numero)

print(numeros)
print(sum(numeros))

