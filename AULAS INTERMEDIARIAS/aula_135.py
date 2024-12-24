import os
os.system('cls')

a, b = 1, 2
b, a = 1, 2
# print(a, b)

pessoa = {
    'nome': 'ALINE',
    'sobrenome': 'SOUZA',
}

dados_pessoa = {
    'idade': 25,
    'altura': 1.50,
}

c, d = pessoa.values()
# print(c, d)

(c1, c2), (d1, d2) = pessoa.items()
# print(c2, d2)

# for chave, valor in pessoa.items():
#     print('------------------------------------')

dados_completo = {**pessoa, **dados_pessoa}
# print('------------------------------------')
# print(f'{dados_completo}')
# print('------------------------------------')

def mostra_argumentos(*args, **kwargs):
    # print('NÃO NOMEADOS:\n', args)
    
    for chave, valor in kwargs.items():
        print(f'Nomeados:', chave, valor)


carro_pecas = {
    'Pneu':'PIRELLY',
    'Oleo':'Mobil',
    'Freio':'Ceramico',
}

mostra_argumentos(**carro_pecas)





