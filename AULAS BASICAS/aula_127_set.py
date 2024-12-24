# p1 = set()

# p1 = {1,1,1,1,2,3,4,4,5,6,6,6,7}

# p2 = {1,1,1,1,2,3,4,4,5,6,6,6,7}

# s2 = set(p2)
# p3 = list(s2)

# # px = 

# print(s2)

s1 = set()

s1.add('CARLOS')
s1.add(1)
s1.update('OLA CARLOS')

s0 = {1,2,3,9}
s2 = {4,5,6}
s3 = {4,8,6,7}
s4 = s2 | s3 | s0
s5 = s2 & s3 
s6 = s2 - s3 
s7 = s2 - s0
print(f'{s5}')
