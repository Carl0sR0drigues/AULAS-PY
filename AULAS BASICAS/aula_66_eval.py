# while True:
#     calcular = input('Vamos calcular: ')

#     if calcular.lower() == 'sair':
#             break
#     try:
#         resultado = eval(calcular)  # Avalia a expressão digitada pelo usuário
#         print(f'{calcular} = {resultado}')
#     except  Exception as erro:
#          print(f'Voce digitou um valor invalido "{erro}", digite valores validos ou sair para encerar!!!\n')


# import ast

# calcular = input('Vamos calcular: ')

# try:
#     # Avalia a expressão de forma segura
#     resultado = ast.literal_eval(calcular)
#     print(resultado)
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# calcular = input('Vamos calcular: ')
# resultado = eval(calcular)
# print(resultado)

import operator

# Dicionário com as operações matemáticas permitidas
operacoes = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
}

# Função para avaliar expressões simples
def calcular_expressao(expr):
    for operador, funcao in operacoes.items():
        if operador in expr:
            a, b = expr.split(operador)
            return funcao(float(a), float(b))
    raise ValueError("Operação não suportada.")

calcular = input('Vamos calcular: ')

try:
    resultado = calcular_expressao(calcular)
    print(f"O resultado é: {resultado}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



