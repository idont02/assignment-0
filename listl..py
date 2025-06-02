from random import *

n = randint(1,20)
print('Please find the length of the list!')

a = []
for i in range(n):
  a.append(randint(1,1000))
print(a)

input = input('\n')
try:
  input = int(input)
except:
  print('ERROR')
if n == input:
  print('CORRECT')
else:
  print('WRONG')
b = a[0]
a[0] = a[-1]
a[-1] = b
del b

print('This is the list with the first and last element swapped:\n',a)
