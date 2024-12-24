# qual vai ser a palavra?
# entrada de letras
# não deixar ser mais de uma letra
# verificar a letra na palavra
# gravar as letras acertadas

palavra = input('DIGITE A PALAVRA SECRETA: ')
letras_corretas = ''
numero_tentativas = 0
while True:
    letra_digitada = input('digite: ')
    numero_tentativas += 1
    print(f'Tentativas: {numero_tentativas}x')


    if len(letra_digitada) > 1:
        print('digite apenas uma letra!!!')
        continue

    if letra_digitada in palavra:
        letras_corretas += letra_digitada

    palavra_completa = ''
    for _ in palavra:
        if _ in letras_corretas:
            palavra_completa += _
        else:
            palavra_completa += '_'
    print(palavra_completa)

    if palavra_completa == palavra:
        break
