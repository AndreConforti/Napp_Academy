num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número real: '))

itemA = (num1 * 2) * (num2 / 2)
itemB = (num1 * 3) + num3
itemC = num3 ** 3

print(f'O produto do dobro de {num1} com metade de {num2} é: {itemA}')
print(f'A soma do triplo de {num1} com {num3} é: {itemB}')
print(f'{num3} elevado ao cubo é: {itemC}')