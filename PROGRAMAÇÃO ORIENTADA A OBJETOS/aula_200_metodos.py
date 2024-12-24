import os
os.system('cls')

class Car:
    def __init__(self, name):
        self.name = name
        print(f'{self.name}')

    def accelerate(self):
        print(f'{self.name} be accelerate...')



fusca = Car('Fusca')
# print(fusca.name)
Car.accelerate(fusca)
print('')
celta = Car(name='Celta')
# print(celta.name)
Car.accelerate(celta)

print('')
