"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
try:
    num_int = int(input('DIGITE UM NUMERO INTEIRO.\n'))
    if (num_int % 2) == 0:
        print('Você digitou um numero par')
    elif (num_int % 2) != 0:
        print('Você digitou um numero impar')
except:
    print('Você não digitou um numero inteiro')

horario = float(input('Digite o horario com numeros\n'))
if horario >= 0 and horario <= 11.59:
    print('Bom dia')
elif horario >= 12 and horario <= 17.59:
    print('Boa tarde')
elif horario >= 18 and horario <= 23.59:
    print('Boa noite')
else:
    print('Você digitou um horario invalido')

nome = input('Digite seu primeiro nome ')
num_nome = len(nome)

if num_nome > 1:
    if num_nome <= 4:
        print('Seu nome é curto')

    elif num_nome >=5 and num_nome <=6:
        print('Seu nome é normal')

    elif num_nome >6:
        print('Seu nome é muito grande')
else:
    print('Escreva mais de uma letra')

