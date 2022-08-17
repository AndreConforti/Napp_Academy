import string, random

randomLetters = []
consonantLetters = []
consonants = 0
for i in range(10):
    v = random.choice(string.ascii_letters)
    randomLetters.append(v)
    if v not in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u','U']:
        consonants += 1
        consonantLetters.append(v)

print(randomLetters)
print(f'Foram encontradas {consonants} consoantes. São elas: {consonantLetters}')