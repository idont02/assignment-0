n = input('Type any number, from 1 - 20')
try:
  n = int(n)
except:
  input('Choose an integer/number, try again! (press enter)')
print('\nMultiples of the number until 20:')
i=1
while i <= 20:
  print(n*i)
  i+=1
print('\nDone!')
