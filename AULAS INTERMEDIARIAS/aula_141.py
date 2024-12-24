import os
os.system('cls')

produto = {
    'nome': 'Caneta Preta',
    'preco': 'R$ 2,50',
    'categoria': 'Escritorio',
}

# dc = {chave: valor for chave, valor in produto.items()}
# print(*dc, sep='\n')

# dc = {chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in produto.items()}
# print(dc)

# dc = {chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in produto.items() if chave != 'categoria'}
# print(dc)

# s1= {2 * i for i in range(10)}
# print(s1)

s1= {i for i in range(11)}
print(s1)

print(set(range(11)))
