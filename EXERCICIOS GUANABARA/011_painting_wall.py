height = float(input('Height wall: '))
width = float(input('width wall: '))
area = height*width
print(f'Your wall has a dimesion of {height} x {width} and its area is {area:.2f}m² ')
print(f'To paint this wall, you will need {area/2:.2f}l of paint')