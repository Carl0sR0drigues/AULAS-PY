import os
os.system('cls')

compras = []

compras.append('ARROZ')
compras.append('FEIJÃO')
compras.append('CARNE')
compras.append('AÇUCAR')
compras.append('CAFÉ')
compras.append('TOMADA')
compras.append('CEBOLA')
compras.append('ALFA')
compras.append('VINAGRE')
compras.append('BANANA')
compras.append('FARINHA')
compras.append('ESFIRA')
compras.append('DANONE')
compras.append('PÃO DE FORMA')
compras.pop()
compras.insert(-1, 'CERVEJA')
compras.sort()


print(*compras)