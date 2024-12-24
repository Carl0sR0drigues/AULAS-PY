# variavel = 'ola munde'
# print(len(variavel))
# print(variavel[9::-1])

nome = str(input('Digite sue nome. '))
idade = int(input('Digite sua idade. '))
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Digite seu nome e idade')



