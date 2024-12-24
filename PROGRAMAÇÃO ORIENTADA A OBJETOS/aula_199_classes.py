import os
os.system('cls')
# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


p1 = Pessoa('Luiz', 'Santos')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.name)
print(p1.lastname)

print(p2.name)
print(p2.lastname)