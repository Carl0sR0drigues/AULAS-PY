# frase = 'aaaa                          oooo'

# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''

# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue

#     qtd_atual = frase.count(letra_atual)

#     if qtd_apareceu_mais_vezes <= qtd_atual:
#         qtd_apareceu_mais_vezes = qtd_atual
#         letra_apareceu_mais_vezes = letra_atual

#     i += 1

# print(
#     'A letra que apareceu mais vezes foi '
#     f'"{letra_apareceu_mais_vezes}" que apareceu '
#     f'{qtd_apareceu_mais_vezes}x'
# )

# palavra = 'pora do caralho'

# i = 0
# pala_tama = len(palavra)

# while i < pala_tama:
#     print(palavra[i], i)
#     i += 1

# print(i)

import time

print("Contagem regressiva de 5 segundos...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)  # Deve esperar 1 segundo
print("Tempo finalizado!")

