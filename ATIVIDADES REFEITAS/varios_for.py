import time
import os
os.system('cls')


# animais = ['cachoro','ararra','boi','dragão','formiga','elefante']

# for animal in animais:
#     print(animal.upper())
# print('\n')

# novo_animais = [animal.upper() for animal in animais]
# print(*novo_animais, sep='\n')

# # #############################################################################

# numeros = [1,2,3,4,5,6,7,8,9]
# # soma = 0

# # for numero in numeros:
# #     soma += numero
# #     print(soma)

# soma_acumulada = [sum(numeros[:i+1]) for i in range(len(numeros))]
# print(soma_acumulada)

# #############################################################################

# divos = [10,5,45,32,66,63,100,101,48,79]

# # for num in divos:
# #     if num % 2 == 0:
# #         print(f'{num} = Par')
# #     else:
# #         print(f'{num} = Impar')

# par_impar = ['par' if num % 2 == 0 else 'impar' for num in divos]
# for num,status in zip(divos, par_impar):
#     print(f'{num}', status)

# #############################################################################

# valores = [10,5,45,32,66,63,100,101,48,79]

# for num in valores:
#     if num % 2 == 0:
#         print(f'{num} = Par')
#     else:
#         print(f'{num} = Impar')

# #############################################################################

# salada = {
#     'alface':'R$4.50',
#     'tomate':'R$3.50',
#     'pepino':'R$5.00',
#     'repolho':'R$6.00',
# }

# pedido = input('ESCOLHA SUA VERDURA: ').lower()
# pedidos = ()
# for verdura in salada:
#     pedidos = verdura
#     if pedidos == pedido:
#         print(salada[pedido])
# if pedidos != verdura:
#     print('PRODUTO NÃO CADASTRADO')

# pedidos_2 = [verdura for verdura in salada if verdura == pedido]

# if pedidos_2:
#     print(f'Seu pedido: {pedidos_2[0]} custa {salada[pedidos_2[0]]}')
# else:
#     print('Não temos seu pedido!!!')


#############################################################################

# nume = [1,2,3,4,5,6,7,8,9,10,22]

# somas = [som + 1 for som in nume]

# print(somas)
# print([som + 1 for som in nume])

#############################################################################

# for tempo in range(10, 0, -1):
#     print(f'\rTEMPO: " {tempo} "', end=' ')
#     time.sleep(1)
# print('\nPARABENS KAROLINE\n🎉🎉🎉🎉🎉🎉🎉')

# [print(f'\rTEMPO: "{tempo}"', end=' ') or time.sleep(1) for tempo in range(10, 0, -1)]

# print('\nPARABENS KAROLINE\n🎉🎉🎉🎉🎉🎉🎉')

# #############################################################################

# for num in range(0, 51, 2):
#     print(num)

# print(*[num for num in range(0,51,2)], sep='\n')

#############################################################################

# for nume in range(1, 101):
#     resto = nume % 3
#     if  resto == 0:
#         print(nume)

# print(*[nume for nume in range(1, 101) if nume % 3 == 0], sep='\n')

#############################################################################

# numero = int(input('Digite um numero: '))
# # for n in range(0, 11):
# #     resposta = numero*n
# #     print(f'{numero} x {n} = {resposta}')

# printador = [numero * n for n in range(0, 11)]
# for i, resultado in enumerate(printador):
#     print(f'{numero} x {i} = {resultado}')


#############################################################################

numero = int(input('Digite um numero: '))
for nume in range(0, 7, 2):
    resto = numero % 2
    if  resto == 0:
        soma = numero + nume
        print(soma)

#############################################################################

# numero = int(input('Digite um numero: '))
# resto1 = numero % numero
# resto2 = numero % 1

# if resto1  == 0 and resto2 == 0:
#     print('É nós PRIMO')
# else:
#     print('Nós não é PRIMO')

#############################################################################

# maior_idade = 0
# for i in range(0, 7):
#     ano = int(input('Digite seu ano de nascimento: '))
#     resposta = 2024 - ano
#     if resposta >= 21:
#         maior_idade += 1
#         print('Você é maior de idade!!!')
#     else:
#         print('Você ainda não é maior de idade')

# menor_de_21 = 7 - maior_idade

# print(f'Maiores de idade: {maior_idade}')
# print(f'Menores de idade: {menor_de_21}')

#############################################################################

# pesos = []
# for p in range(5):
#     peso = int(input('Digite seu peso: '))
#     pesos.append(peso)

# maior_peso = max(pesos)
# menor_peso = min(pesos)

# print(f'Maior peso: {maior_peso}')
# print(f'Menor peso: {menor_peso}')

#############################################################################

# idades_total = 0
# maior_idade_m = 0
# mulher_20_mais = 0

# for i in range(1, 5):
#     print(f'-----{i}ª PESSOA -----')
#     pessoa = input("Digite o nome da pessoa: ")
#     idade = int(input("Digite a idade: "))
#     idades_total += idade
#     sexo = input("Digite o sexo (m/f): ").lower()

#     if sexo == 'm' and idade > maior_idade_m:
#             maior_idade_m = idade
#             nomevelho = pessoa

#     if sexo == 'f' and idade < 20:
#           mulher_20_mais += 1

# idade_medio = idades_total / 4

# print(f'A media de idade da pessoas é de {idade_medio}')
# print(f'{mulher_20_mais} mulher tem menos de 20 anos')
# print(f'O homem mais velhor é o {nomevelho}, com {maior_idade_m} anos')

#############################################################################

# lista_preco = [100,500,200,400]

# nova_lista = [preco * 2 for preco in lista_preco]

# impressao_legal.impressao(nova_lista)



