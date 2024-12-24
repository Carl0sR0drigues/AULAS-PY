import os

os.system('cls')
while True:
    fazer = int(input('fazer o que: '))

    if fazer == 1:
        def multi(*args):
            total = 1
            for num in args:
                total *= num
            return total

        valores1 = input('valores1: ')
        valores = [int(num) for num in valores1.split()]
        multiplicacao = multi(*valores)
        print(multiplicacao)

    else:
        def par_inpar(a):
            a = int(input('digite os valores: '))
            ret = a % 2
            if ret == 0:
                print('Par')
            else:
                print('Impar')

        valor = par_inpar(a=3)
    sair = input('').lower()
    if sair == 's':
        break


