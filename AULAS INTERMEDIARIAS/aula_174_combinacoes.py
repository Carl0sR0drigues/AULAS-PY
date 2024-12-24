import limpador
from itertools import combinations
from itertools import permutations, product

def impressao(interador):
    print(*list(interador), sep='\n')
    print('\n')

pessoas = [
    'CARLOS', 'ANTONIO', 'KAROL', 'CARLIKA',
]

roupas = [
    ['calça', 'camisa'],
    ['P', 'M', 'G'],
    ['PRETA', 'MARROM', 'BRANCA'],
    ['MASC.', 'FEM.']
]

# impressao(combinations(pessoas,2))
# impressao(permutations(pessoas,2))
impressao(product(*roupas))