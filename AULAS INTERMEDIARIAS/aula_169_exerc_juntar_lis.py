import limpador

# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
sigla = ['BA', 'SP', 'MG', 'RJ']
cidade_sigla = []

for cid, sig  in zip(cidade, sigla):
    cidade_sigla.append(cid)
    cidade_sigla.append(sig)

# juntas.extend(numero[len(letras):])
# juntas.extend(letras[len(numero):])

print(list(zip(cidade, sigla)))
print(list(zip_longest(cidade, sigla)))
print(list(zip_longest(cidade, sigla, fillvalue='NOT CID')))
# print(cidade_sigla)


