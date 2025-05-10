from math import sqrt, pow
def errmsg():
  print('Error, try again.')
def intcheck(v):
  while True:
    v = input()
    try:
      int(v)
      break
    except:
      errmsg()
print('Type number.')
n=0
intcheck(n)
print('Root or Power?\nType sqrt for root\nType pow for power\n\nNote: If pow is selected, exponent will be asked later.')
choice = input()
if choice == 'sqrt':
  print(sqrt(n))
elif choice == 'pow':
  print('Type exponent')
  exp=0
  intcheck(exp)
  print(pow(n,exp)
else:
  errmsg()
  
