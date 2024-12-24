from functools import reduce
import limpador

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


tota = sum([p['preco'] for p in produtos])

total = 0
for p in produtos:
    total += p['preco']

def funcao_do_reduce(acumulador, produto):
    return acumulador + produto['preco']

tot = reduce(funcao_do_reduce,produtos,0)

to = reduce(lambda acu, pro: acu + pro['preco'],produtos,0)

print(f'TOTAL: {total:.2f}')
print()
print(f'TOTA: {tota:.2f}')
print()
print(f'TOT: {tot:.2f}')
print()
print(f'TO: {to:.2f}')
print()

