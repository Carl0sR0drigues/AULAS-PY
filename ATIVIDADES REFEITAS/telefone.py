# PRECISO ENCONTRAR UM NUMERO DE TELEFONE EM UMA LISTA TELEFONICA
import os
os.system('cls')

telefonica = {
    'JOÃO':['9145-3546'],
    'PEDRO':['8145-8798'],
    'ANTONIO':['9265-9743'],
    'JOSE':['9255-6478'],
    'KAROL':['8589-4667'],
    'CARLOS':['9129-4667'],
    'MARCELO':['9129-8721']
}

def telefones(nome):
    if nome in telefonica:
        return telefonica[nome]
    return 'NÃO CONSTA NA LISTA'


while True:
    nomes = input('DIGITE O NOME: ').upper()
    numero = telefones(nomes)
    print(f' {nomes}\n',*numero)
    sair = input(' ').upper()
    if sair == 'S':
        break