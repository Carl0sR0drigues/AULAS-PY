import importlib

import aula_136

print(aula_136.variavel)

for i in range(10):
    importlib.reload(aula_136)
    print(i)

print('Fim')

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import *
# import aula99_package.modulo
# from aula99_package import modulo
# from aula99_package.modulo import *