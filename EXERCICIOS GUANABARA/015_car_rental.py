import limpar
#Exercício Python 015: Escreva um programa que pergunte a 
# quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

days = int(input('How many days rented? '))
kms = float(input('How many km driven? '))
print(f'The total payable is R${(days*60)+(kms*0.15)}')