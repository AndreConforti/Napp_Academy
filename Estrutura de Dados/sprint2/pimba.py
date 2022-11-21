import pickle 

with open('dados_escolares_nome.bin', 'rb') as file:
    dados_escolares_nome = pickle.load(file)

for i in dados_escolares_nome:
    print(i)