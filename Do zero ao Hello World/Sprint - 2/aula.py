nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))

notas = [nota1, nota2, nota3, nota4]

notas.sort(reverse=True)

print(f'As notas em ordem descrecente foram: {notas}')