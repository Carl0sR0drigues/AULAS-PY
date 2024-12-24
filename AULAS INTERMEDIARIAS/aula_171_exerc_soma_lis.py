import limpador

l1 = [1,2,3,4,5]
l2 = [1,2,3,7,8,9,5]
soma = [item1 + item2 for item1, item2 in zip(l1, l2)] #list comprehension

print(soma)

################################################################################

l1 = [1,2,3,4,5]
l2 = [1,2,3,7,8,9,5]

soma = []
for a, b in zip(l1, l2):
    soma.append(a + b)

print(soma)

################################################################################

l1 = [1,2,3,4,5]
l2 = [1,2,3,7,8,9,5]
somado = []
for i in range(len(l1)):
    somado.append(l1[i] + l2[i])

print(somado)

################################################################################

l1 = [1,2,3,4,5]
l2 = [1,2,3,7,8,9,5]
somado = []
for i, _ in enumerate(l1): # O _ SERVE PARA DIZER PARA QUE QUEREMOS APENAS OS INDICES E NÃO OS VALORES
    somado.append(l1[i] + l2[i])

print(somado)

################################################################################

