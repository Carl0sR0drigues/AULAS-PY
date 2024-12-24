import os

os.system('cls')


# def vai(by):
#     def oi(fulano):
#         return f'{by},{fulano}!!!'
#     return oi

# comprimentar = vai('Vai com Deus')
# bem_vindo = vai('Seja bem-vindo')

# for nome in ['Pedro','Thiago','João']:
#     print(bem_vindo(nome))
#     print(comprimentar(nome))

# CRIE UMA FUNÇÃO QUE DUPLICA, TRIPLICA E QUADRUPLICAM
# O NUMERO RECEBIDO COMO PARÂMENTRO

def multiplos(valor):
    def numeral(mulplicador):
        return mulplicador ** valor
    return numeral

duplicar = multiplos(2)
triplicar = multiplos(3)
quadruplicar = multiplos(4) 
valor1 = int(input('digite o valor 1: '))
valor2 = int(input('digite o valor 2: '))
valor3 = int(input('digite o valor 3: '))

os.system('cls')

print(f'Resposta Valor 1= {duplicar(valor1)}')
print(f'Resposta Valor 2= {triplicar(valor2)}')
print(f'Resposta Valor 3= {quadruplicar(valor3)}\n')
