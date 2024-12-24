# import os

# os.system('cls')

# bitola = str(input('qual o cabo? '))

# cabo = {}

# cabo['2,5'] = 'cabo pvc 2,50mm²'
# cabo['6,0'] = 'cabo pvc 6,00mm²'
# cabo['4,0'] = 'cabo pvc 4,00mm²'
# cabo['10,0'] = 'cabo pvc 10,0mm²'
# cabo['16,0'] = 'cabo pvc 16,0mm²'
# cabo['25,0'] = 'cabo pvc 25,0mm²'

# if cabo.get(bitola) is None:
#     print('ISSO NÃO EXISTE')

# else:
# print(list(cabo.keys()))
# print(list(cabo.items()))

# for chave, valor in cabo.items():

# cabo.setdefault('60,0', 'não existe')
# print(cabo['10,0'])


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# acertos = 0
# # if cabo.get(bitola) is None:

# perguntando1 = int(input('Pergunta: Quanto é 2+2?\n Opções:\n0) 1\n1) 3\n2) 4\n3) 5\nEscolha uma opção: '))
# retorno = perguntas[0]['Opções'][perguntando1]
# if retorno == '4':
#     print('Acertou 👏👏👏👏👏')
#     acertos += 1
# else:
#     print('Você errou 😒😒😒😒😒')


# perguntando2 = int(input('Pergunta: Quanto é 5*5?\n Opções:\n0) 25\n1) 55\n2) 10\n3) 51\nEscolha uma opção: '))
# retorno = perguntas[1]['Opções'][perguntando2]
# if retorno == '25':
#     print('Acertou 👏👏👏👏👏')
#     acertos += 1
# else:
#     print('Você errou 😒😒😒😒😒')

# perguntando3 = int(input('Pergunta: Quanto é 10/2?\n Opções:\n0) 4\n1) 5\n2) 2\n3) 1\nEscolha uma opção: '))
# retorno = perguntas[2]['Opções'][perguntando3]
# if retorno == '5':
#     print('Acertou 👏👏👏👏👏')
#     acertos += 1
# else:
#     print('Você errou 😒😒😒😒😒')

# print(f'\nVocê acertou: {acertos} de 3 perguntas.')


# if perguntas.get(['Resposta'['5']]) is None:
#     print('ISSO NÃO EXISTE')
acertos = 0
for pergunta in perguntas:
    print(f'Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)
    
    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qta_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qta_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print('Acertou 👏👏👏👏👏')
    else:
        print('Errou ❌❌❌❌❌') 


    # for ok in acertou:
    if acertou == True:
        acertos += 1
    print(f'Você acertou {acertos} de 3')