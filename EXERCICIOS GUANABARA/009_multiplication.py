import os
os.system("cls")

number = int(input('Enter a number to see your multiplication table: '))

print("-------------")
for multiplication in range(11):
    print(f'{number} x {multiplication} = {number*multiplication}')
print("-------------")
print("-------------")
# # for multiplication in range(101):
# #     print(f'{number} + {multiplication} = {number+multiplication}')
# # print("-------------")
# # # print('')

# print("-------------")
# print('{} x {} = {}'.format(number,1, number*1))
# print('{} x {} = {}'.format(number,2, number*2))
# print('{} x {} = {}'.format(number,3, number*3))
# print('{} x {} = {}'.format(number,4, number*4))
# print('{} x {} = {}'.format(number,5, number*5))
# print('{} x {} = {}'.format(number,6, number*6))
# print('{} x {} = {}'.format(number,7, number*7))
# print('{} x {} = {}'.format(number,8, number*8))
# print('{} x {} = {}'.format(number,9, number*9))
# print('{} x {} = {}'.format(number,10, number*10))
# print("-------------")


