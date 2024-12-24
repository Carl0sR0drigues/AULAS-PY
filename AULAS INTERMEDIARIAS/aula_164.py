import os 
os.system('cls')
# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

###########################################################

# def concatenar(string_inicial):
#     valor_final = string_inicial

#     def interna(valor_a_concatenar=''):
#         nonlocal valor_final
#         valor_final += valor_a_concatenar
#         return valor_final
#     return interna


# c = concatenar('a')
# print(c('b'))
# print(c('c'))
# print(c('d'))
# final = c()
# print(final)

###########################################################

def palavra1(frase):
    frase_final = frase
    def palavra2(frase_formando):
        nonlocal frase_final
        frase_final += frase_formando
        return frase_final
    return palavra2


palavra = palavra1('Eu ' )
print(palavra('não '))
print(palavra('estou '))
print(palavra('legal, '))
print(palavra('preciso '))
print(palavra('fazer '))
print(palavra('alguma coisa para mudar isso.'))
###########################################################
print(palavra('1'))
print(palavra('2'))
print(palavra('3'))
print(palavra('4'))
print(palavra('5'))
print(palavra('6'))
print(palavra('7'))
print(palavra('8'))
print(palavra('9'))
print(palavra('10'))
