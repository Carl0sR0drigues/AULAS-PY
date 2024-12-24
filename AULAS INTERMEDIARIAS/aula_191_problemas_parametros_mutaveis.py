import limpador

# def adicionar_dados(nome, lista=[]):
#     lista.append(nome)
#     return lista

def adicionar_dados(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


sei2 = adicionar_dados('Antonio')
adicionar_dados('Karoline', sei2)
adicionar_dados('Kar', sei2)
sei2.append('João')


# print(*sei2, sep='\n')
print(sei2,)

##################################################################

# lista1 = []
sei = adicionar_dados('Carlos')
adicionar_dados('Karol', sei)


# print(*sei, sep='\n')
print(sei,)