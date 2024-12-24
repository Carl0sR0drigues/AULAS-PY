#produtos = 

palavra = { 
    'João':[10], 
    'Carlos':[19], 
    'Karol':[100], 
    'Kar':[50], 
    'rol':[2], 
    'Larol':[12], 
}

# valor_maximo = max(valor[0] for valor in palavra.values())

# valor_minimo = min(valor[0] for valor in palavra.values())

# valores_entre = [valor[0] for valor in palavra.values() if valor_minimo < valor[0] < valor_maximo]

def lista_de_produto(dicionario):

    valor_max = max(dicionario.values())
    valor_min = min(dicionario.values())
    valor_med = []

    for valor in dicionario.values():
        if valor_min < valor < valor_max:
            valor_med.append(valor)
    print(f'MAXIMO',valor_max)
    print(f'MEDIO', valor_med)
    print(f'MANIMO', valor_min)


compras = lista_de_produto(palavra)

