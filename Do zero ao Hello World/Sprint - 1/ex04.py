nota1 = str(input('1ª nota: ')).replace(',', '.')
nota2 = str(input('2ª nota: ')).replace(',', '.')
nota3 = str(input('3ª nota: ')).replace(',', '.')
nota4 = str(input('4ª nota: ')).replace(',', '.')

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4

print(f'A média entre as notas informadas é {media:.1f}')