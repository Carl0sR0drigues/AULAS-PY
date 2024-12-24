# condicao = True
# while condicao:
#     nome = input('Seu nome:\n')
#     print(nome)
#     if nome == 'sair':
#         break

# conta = 0
# while conta < 50:
#     conta = conta + 1
#     print(conta)
# print('CABO')

# calcular = int(input('vamos calcular: '))
# resulta = (f'{calcular}= resu')
# print(resulta)

nome = 'Antonio Carlos'
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)


