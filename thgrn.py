print('It\'s three numbers now...')
n1 = int(input('Type first number: '))
n2 = int(input('Type second number: '))
n3 = int(input('Type third number: '))
if n1 > n2:
  if n1 > n3:
    print('The largest number is the first one.')
  elif n1 == n3:
    print('The largest numbers are the first and third ones.')
elif n1 > n3:
  if n1 == n2:
    print('The largest numbers are the first and second ones.')
  if n1 > n2:
    print('The largest number is the first one.')
elif n1 == n2:
    if n1 > n3:
    print('The largest numbers are the first and second ones.')
  elif n1 == n3:
    print('Every number is equal.')
