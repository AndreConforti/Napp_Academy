nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))
nota3 = float(input('3ª Nota: '))
nota4 = float(input('4ª Nota: '))

notas = [nota1, nota2, nota3, nota4]

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'As notas apresentadas foram: {notas} e a média foi de: {media:.1f}')