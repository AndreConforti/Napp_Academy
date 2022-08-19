'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
'''
from audioop import avg, reverse

numeros = []


while True:
    valor = int(input('Digite um valor: '))
    if valor < 0:
        break
    else:
        numeros.append(valor)

print(numeros)
print(f'''
a - Quantidade de valores que foram lidos : {len(numeros)}
b - Valores que foram informados..........: {numeros}''')
numeros.reverse()
print(f'''c - Valores na ordem inversa..............: {numeros}
d - Soma dos valores......................: {sum(numeros)}
e - Média dos valores.....................: {avg(numeros)}
f - Quantidade de valores acima da média..: {len(list(filter(lambda x: x > (sum(numeros) / len(numeros)), numeros)))}
g - Quantidade de valores abaixo de 7.....: {len(list(filter(lambda x: x < 7, numeros)))}
''')
