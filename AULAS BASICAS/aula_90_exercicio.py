lista = []

while True:
    escolhas = input('O que deseja fazer? [i]nserir [a]pagar [l]ista:')
    if escolhas == 'a':
        ind = int(input('Numero do iten?'))
        lista.pop(ind)
    elif escolhas == 'i':
        print()
        novo_iten = str(input('Iten: '))
        lista.append(novo_iten)
    elif escolhas == 'l':
        for i, e in enumerate(lista):
            print(f'{i + 0}:{e}')