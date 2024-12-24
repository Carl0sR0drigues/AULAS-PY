import limpar
import math

opposite_leg = float(input('Opposite leg length: '))
adjacent_leg = float(input('Length of adjacent leg: '))

hypotenuse1 = (opposite_leg**2) + (adjacent_leg**2)
hypotenuse2 = (opposite_leg**2 + adjacent_leg**2) ** (1/2)
hypotenuse3 = math.hypot(opposite_leg, adjacent_leg)

print('')
print(f'1 - The hypotenuse will measure {math.sqrt(hypotenuse1):.2f}')
print(f'2 - The hypotenuse will measure {hypotenuse2:.2f}')
print(f'3 - The hypotenuse will measure {hypotenuse3:.2f}')
print('')
