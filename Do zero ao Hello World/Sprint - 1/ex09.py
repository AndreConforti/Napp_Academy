# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

far = float(input('Digite a temperatura em ° Fahrenheit: '))

celsius = 5 * ((far - 32) / 9)

print(f'{far}° Fahrenheit equivalem a {celsius}° Celsius')