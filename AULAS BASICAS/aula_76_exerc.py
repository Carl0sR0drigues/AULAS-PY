"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Definindo a palavra secreta e o progresso das letras fora do loop

import getpass
import time

while True:
    palavra_secreta = getpass.getpass('QUAL A PALAVRA SECRETA? ').lower()
    i = 0
    qt = len(palavra_secreta)
    print(f'A PALAVRA SECRETETA TEM {qt} LETRAS, QUAL A PALAVRA? ')
    letras_adivinhadas = ['*' for _ in palavra_secreta]

    while ''.join(letras_adivinhadas) != palavra_secreta:
        
        letra = input('DIGITE UMA LETRAA!!! \n').lower()
        
        if letra in palavra_secreta:
            # Atualiza as letras adivinhadas com a letra correta
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_adivinhadas[i] = letra
            
            # Mostra o progresso da palavra
            print(f'Boa! A palavra agora está assim: {" ".join(letras_adivinhadas)}\n')
        elif len(letra) > 1:
            print('DIGITE APENAS UM LETRA')
        else:
            print('Essa letra não está na palavra. Tente novamente.')

    # Parabeniza o usuário quando ele adivinhar todas as letras
    print(f'Parabéns! Você completou a palavra: {palavra_secreta}\n')
    
    close = input('MAIS UMA VEZ? 1 PARA CONTINUAR E 0 PARA SAIR \n')
    if close == '0':

        print("\nEncerrando🖐️🖐️🖐️🖐️🖐️...")
        print("\nContagem regressiva de 5 segundos...")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)  # Deve esperar 1 segundo
        print("\nBy by by!!!")
        time.sleep(1)
        break
    elif close == '1':
        print('\nVamos lá 😁😁😁😁😁😁...')

 