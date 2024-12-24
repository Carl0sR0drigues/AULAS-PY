print('')

text = input('Type something: ')
print(f'The primitive type of this value is', type(text))
print(f'are there only spaces?', text.isspace())
print(f'Its a number?', text.isnumeric())
print(f'Its alphabetical?', text.isalpha())
print(f'Its in capital letters?', text.isupper())
print(f'Its in lowercase letter?', text.islower())
print(f'Is it capitalized?', text.istitle())


print('')