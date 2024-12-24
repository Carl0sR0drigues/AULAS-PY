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

# palavra_secreta = 'vamos'
# letras = input('DIGITE UMA LETRA')

matriz1 = [
    [2, 2],
    [2, 2]
]

matriz2 = [
[2, 2],
[2, 2]
]

resultado = [
[0, 0],
[0, 0]
]

for i in range(2):
    for j in range(2):
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]

for linha in resultado:
    print(linha)