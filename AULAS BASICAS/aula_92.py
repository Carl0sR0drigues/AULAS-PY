frase = 'olha ele em, olha ele'
frases_ls = frase.split(', ')

for _, frase in enumerate(frases_ls):
    print(frases_ls[_].strip())



print(frases_ls)

# strip corta os espaços dos dois lados
# rstrip corta os espaços do lado direto
# ltrip corta os espaços do lado esquerdo
#join junta as strigs
# exemplo: frase = ''.join(frases_ls)