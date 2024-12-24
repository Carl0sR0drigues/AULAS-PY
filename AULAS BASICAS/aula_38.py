while True:
    primeiro_valor = input('valor 1\n')
    segundo_valor = input('valor 2\n')

    if primeiro_valor > segundo_valor:
        print(f'Primeiro_valor= {primeiro_valor} é maior que o segundo_valor={segundo_valor}')
    else:
        print(f'Segundo_valor= {segundo_valor} é maior que o primeiro_valor={primeiro_valor}')

    fechar = input('close\n')
    if fechar == 'close':
        break