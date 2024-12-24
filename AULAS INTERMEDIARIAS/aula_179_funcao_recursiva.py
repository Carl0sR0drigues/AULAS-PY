import limpador


# def recursiva(inicio=0, fim=5):
#     print(inicio, fim)
#     if inicio >= fim:
#         return fim
    
    
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva())

def factor(numero):
    if numero <= 1:
        return 1
    return numero * factor(numero - 1)

print(factor(5))
