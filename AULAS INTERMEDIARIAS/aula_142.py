lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Carlos'},]

# for item in lista:
#     print(item, isinstance(item, set))

# for item in lista:
#     if isinstance(item, set):
#         item.add('SHOW')
#         print(item)

# for item in lista:
#     if isinstance(item, str):
#         print(item.upper(), isinstance(item, set))

for item in lista:
    if isinstance(item, (int, float)):
        print('VAMOS DOBRAR O VALOR')
        print(item, item * 2)