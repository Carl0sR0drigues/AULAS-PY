while True:
    import os
    import getpass
    import re
    import sys
    import random

    os.system('cls')

    atividade = int(input('GERAR CPF=1\nVALIDAR CPF=2\n'))
    if atividade == 2:
        try:
            while True:
                try:
                    while True:
                        while True:
                            try:
                                cpf1 = input('Digite seu CPF: ').strip()  # Remove espaços e quebras de linha
                                cpfx = re.search(r"[^-.0-9]", cpf1)
                                if cpfx != None:
                                    raise ValueError('Dados invalidas')
                                elif len(cpf1) < 9:
                                    raise ValueError('Dados invalidas')
                            except ValueError:
                                print('Digite seus dados corretamentoe')
                            if cpfx == None: #and cpf1 >= 11:
                                break

                        if not cpf1:  # Verifica se a entrada é vazia após remover espaços
                            print('Por favor, digite seu CPF válido!')
                        else:
                            break  # Sai do loop se a entrada é válida

                    cpf = re.sub(r'[^0-9]','',cpf1)
                    repedidos = cpf == cpf[0] * len(cpf)
                    
                    if repedidos:
                        raise ValueError('Você inseriu numeros invalidos')
                    
                except ValueError as e:
                    print(e)

                if repedidos == False:
                    break  # Sai do loop se o CPF for válido

                        

            cpf_9 = cpf[:9]
            resultado = 0 
            contador = 10

            for digito in cpf_9:
                resultado += int(digito) * contador
                contador -= 1
                resto = resultado * 10 % 11

            if resto > 9:
                resto_final = 'Resultado= 0'
            elif resto <= 9:
                resto_final = resto
                cpf_resto_final = (f'{cpf}{resto_final}')
                print(cpf_resto_final)

            #SEGUNDO NUMERO DO CPF

            cpf_10 = cpf_resto_final[:10]
            resultado_2 = 0 
            contador_11 = 11

            for digito2 in cpf_10:
                resultado_2 += int(digito2) * contador_11
                contador_11 -= 1
                resto2 = resultado_2 * 10 % 11

            if resto2 > 9:
                resto_final2 = 'Resultado= 0'
            elif resto2 <= 9:
                resto_final2 = resto2

                final_cpf = (f'{resto_final}{resto_final2}')

                if cpf[-2:] == final_cpf:
                    print(f'\nCPF: {cpf} Valido')
                else:
                    print(f'\nCPF:{final_cpf} Invalido')
        except ValueError:
            print('VOCE NÃO DIGITOU UM VALOR VALIDO')

            #----------GERADOR DE CPF---------

    else:
            gerado_novo = ''
            for i in range(9):
                gerado_novo += str(random.randint(0, 9))
            gerados = gerado_novo
            cpf_9 = gerados[:9]
            resultado = 0 
            contador = 10

            for digito in cpf_9:
                resultado += int(digito) * contador
                contador -= 1
                resto = resultado * 10 % 11

            if resto > 9:
                resto_final = 'Resultado= 0'
            elif resto <= 9:
                resto_final = resto
                cpf_resto_final = (f'{gerados}{resto_final}')

            #SEGUNDO NUMERO DO CPF

            cpf_10 = cpf_resto_final[:10]
            resultado_2 = 0 
            contador_11 = 11

            for digito2 in cpf_10:
                resultado_2 += int(digito2) * contador_11
                contador_11 -= 1
                resto2 = resultado_2 * 10 % 11

            if resto2 > 9:
                resto_final2 = 'Resultado= 0'
            elif resto2 <= 9:
                resto_final2 = resto2

            print(f'CPF novo gerado = {gerados}{resto_final}{resto_final2}')


    saida = input('').lower()
    if saida == 's':
        break



# 530.708.792-68