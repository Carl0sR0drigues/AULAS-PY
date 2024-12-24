# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy
import os

os.system('cls')

# def chama(dicionarios):
#     for i in dicionarios:
#         print(f'{i}')    

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


produtos_com_aumento = []

for produto in produtos:
    preco10 = produto['preco'] * 1.1
    produtos_com_aumento.append({'nome': produto['nome'], 'preco': preco10})
    
produto_copia_prof_1 = copy.deepcopy(produtos_com_aumento)

for produto in produto_copia_prof_1:
    produto_copia_prof_1_final = (f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
    print(produto_copia_prof_1_final)
print('\nNOVOS PREÇOS\n')

# chama(produtos)


precos_ordenados_nome_des = sorted(produto_copia_prof_1, key=lambda produto: produto['preco'], reverse=True)

for produtos1 in precos_ordenados_nome_des:
    produtos_ordenados_preco = (f"Nome: {produtos1['nome']}, Preço: R${produtos1['preco']:.2f}")
    print(produtos_ordenados_preco)
print('\nORDENADO POR PREÇO DECRESCENTE\n')

# chama(produtos)



produtos_ordenados_por_nome = copy.deepcopy(produto_copia_prof_1)

for produtos2 in sorted(copy.deepcopy(produtos_ordenados_por_nome), key=lambda produto: produto['nome']):
    produtos_ordenados_em_nome = (f"Nome: {produtos2['nome']}, Preço: R${produtos2['preco']:.2f}")
    print(produtos_ordenados_em_nome)
print('\nORDENADO POR NOME CRESCENTE\n')

# chama(produtos) 


produtos_ordenados_por_preco = sorted(produto_copia_prof_1, key=lambda produto: produto['preco'])

for produtos3 in produtos_ordenados_por_preco:
    produtos_ordenados_preco_cres = (f"Nome: {produtos3['nome']}, Preço: R${produtos3['preco']:.2f}")
    print(produtos_ordenados_preco_cres)
print('\nORDENADO POR PREÇO crescente\n')











# for produtos2 in sorted(copy.deepcopy(produtos), key=lambda produto: produto['nome']):



