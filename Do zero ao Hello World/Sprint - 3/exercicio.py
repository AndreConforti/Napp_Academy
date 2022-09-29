from telnetlib import DO


lanchonetes = {'Napp Dogão': {'lanche':'Dogão Supremo', 'valor': 24.99,'peso': 500 },

               'Cubo Lanchonete':{'lanche': 'Churrasco de costela', 'valor': 29.99, 'peso' :600},

               'Live Hamburgueria':{'lanche': 'Hambuguer SalesLive', 'valor': 27.99, 'peso': 450},

               'SOS Lanches':{'lanche': 'Catupresunto', 'valor': 18.99, 'peso': 400}}

lanchonetes['Conect Lanches'] = {'lanche': 'Frango Gostoso', 'valor': 23.99, 'peso':400}

# TODO: PRECISO REFAZER ISSO NOVAMENTE

print(f"O lanche mais vendido na lanchonete Napp Dogão: {lanchonetes['Napp Dogão']['lanche']}")
print(f"O lanche mais vendido na lanchonete Napp Dogão: {lanchonetes['Cubo Lanchonete']['lanche']}")
print(f"O lanche mais vendido na lanchonete Napp Dogão: {lanchonetes['Live Hamburgueria']['lanche']}")
print(f"O lanche mais vendido na lanchonete Napp Dogão: {lanchonetes['SOS Lanches']['lanche']}")

print(lanchonetes)