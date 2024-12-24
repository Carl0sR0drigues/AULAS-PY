
# lista = ['carro', 1987, 91.5, 'Carlos']
# lista[1] = 'XXXXXXXXXXX'
# lista.append('legal')
# lista.append('sei lá')
# lm.pop(0)
# removido = lista.pop()
# del lista[-1]
# lista.insert(-2, 2)
# # print(removido)
# print(lista)

cabos = [2.5,4.0,6.0,10.0]
cabos.pop(0)
print(cabos)

# eletrodutos = ['3/4','1/2','1','1.1/2']
# lm = ['casa', 'predio', 'dosador', 'tanque']
# lm_cabos_condutos = cabos + eletrodutos + lm
# cabos.extend(eletrodutos)








# print(lm_cabos_condutos)


# lm = ['casa', 'predio', 'dosador', 'tanque']

# for indice in enumerate(lm):
#     print(indice)


lm = ['casa', 'predio', 'dosador', 'tanque']
indice = range(len(lm))

for num in indice:
    print(num, lm[num])
