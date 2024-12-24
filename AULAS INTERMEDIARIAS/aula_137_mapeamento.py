import os
os.system('cls')

produtos = [
    {'nome':'prod1', 'preco': 10, },
    {'nome':'prod2', 'preco': 20, },
    {'nome':'prod3', 'preco': 30, },
    {'nome':'prod4', 'preco': 40, },
]

produtos_alterados = [{'nome': produto ['nome'], 'preco': produto['preco']} for produto in produtos]
print(*produtos_alterados,  sep='\n')


novo_produto = [ {**prodution} for prodution in produtos]
print(*novo_produto, sep='\n')

novo_produto = [ {**produt, 'preco': produt['preco'] * 2} for produt in produtos]
print(*novo_produto, sep='\n')

novo_produto = [{**produt, 'preco': produt['preco'] * 2} if produt['preco'] > 20 else {**produt} for produt in produtos]
print(*novo_produto, sep='\n')

