# nome = ('Carlos')
# sobre_nome = ('Rodrigues')
# idade = 37
# ano_nascimento = 2024 - idade
# altura_metros = 1.71
# maior_idade = idade >= 18

# str(print('Nome:',nome))
# str(print('Sobre nome:',sobre_nome))
# print('Idade',idade)
# print('Ano de nascimento',ano_nascimento)
# print('É maior de idade?',maior_idade)

# lista = []
# while True:
#     novo = input('digite: ')
#     lista.append(novo)
#     for i in lista:
#         print(i)

lista = []
while True:
    novo = input('digite: ')
    lista.append(novo)
    for i in range(len(lista)):
        print(f'{i} {lista[i]}')

lista = []
while True:
    novo = input('digite: ')
    lista.append(novo)
    for i in range(1, len(lista) + 1):
        print(f'{i} {lista[i - 1]}')