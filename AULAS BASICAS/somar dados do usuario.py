import os
os.system('cls')

cpf_entrada = input('Digite seu CPF: ')
cpf = cpf_entrada.replace('-', '').replace('.', '')

cpf_somado = 0

for i in range(9):
    cpf_somado += int(cpf[i])




print(cpf_somado)
