print('Type a number')
a = input()
try:
  int(a)
except:
  print('Error, try again.')
c = a
l=len(a)
for i in range(l):
  rm=a%10
  r=r*10+rm
  a=a//10
if c == r:
  print('It is a palindrome.')
else:
  print('It is NOT a palindrome.')
