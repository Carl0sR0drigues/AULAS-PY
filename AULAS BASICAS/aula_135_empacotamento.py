import os

os.system('cls')


pessoa = {
    'nome':'Carlos',
    'sobrenome':'Rodrigues'
}

dados_pessoa = {
    'idade': 37,
    'altura': 1.71
}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

def mostro_argumento_nomeados(*args, **kwargs):
    # print('pora nenhuma',args)
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumento_nomeados(**pessoa_completa)