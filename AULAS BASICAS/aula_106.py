import os

os.system('cls')

def soma(x, y, z= None):
    if z is not None:
        resultado = x * y * z
        print(f'{x= } {y= } {z=}', '|', 'x*y*z=', x * y * z)
    else:
        resultado = x * y
        print(f'{x= } {y= }', '|', 'x*y=', x * y)

    return resultado

soma1 = soma(250, 1, 2)
soma2 = soma(z=5, y=3, x=10)
soma3 = soma(1, 50)

total = soma1 + soma2 + soma3

print(total)




