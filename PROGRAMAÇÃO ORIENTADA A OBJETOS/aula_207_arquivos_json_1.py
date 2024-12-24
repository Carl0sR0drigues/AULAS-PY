import limpar
import json

FILE_PATH = 'class_file_js.json'

class Person:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

p1 = Person('Carlos', 37)
p2 = Person('Karol', 33)
p3 = Person('Carlika', 10)
all_person = [vars(p1), p2.__dict__, vars(p3)]

with open(FILE_PATH, 'w') as files:
    json.dump(all_person, files, ensure_ascii=False, indent=2)