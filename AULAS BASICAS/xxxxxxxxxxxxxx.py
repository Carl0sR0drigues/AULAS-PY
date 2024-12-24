import random

gerados = ''
for i in range(9):
    gerados += str(random.randint(0, 9))
print(gerados)