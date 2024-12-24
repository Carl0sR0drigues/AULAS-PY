import os
os.system('cls')

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [ numero for numero in range(10)]
# print(lista)

numerosX2 = [1,2,3,4,5]

numeral = [numero * 2 for numero in numerosX2]
print(numeral)
