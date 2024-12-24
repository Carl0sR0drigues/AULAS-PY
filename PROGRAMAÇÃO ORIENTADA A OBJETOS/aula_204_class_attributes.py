import limpar

class Person:
    current_year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age_birth(sef):
        return Person.current_year - sef.age


p1 = Person('Carlos',37)
p2 = Person('Karol',33)

print(f'Current year: {Person.current_year}')
print('')
print(f'Year of birth: {p1.get_age_birth()}')
print(f'Year of birth: {p2.get_age_birth()}')
print('')
