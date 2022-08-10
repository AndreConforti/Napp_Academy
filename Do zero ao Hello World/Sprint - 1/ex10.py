# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre a temperatura em graus Fahrenheit.

cel = float(input('Digite a temperatura em ° Celsius: '))

far = (cel * 9/5) + 32

print(f'{cel:.2f}° Celsius equivalem a {far:.2f}° Fahrenheit')