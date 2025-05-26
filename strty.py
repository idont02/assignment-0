up = lo = dg = sp = 0
print('Type anything: ')
st = input()
for i in st:
  if i.isupper():
    up+=1
  elif i.islower():
    lo+=1
  elif i.isdigit():
    dg+=1
  else:
    sp+=1
print('\nUppercase letters:',up,'\nLowercase letters:',lo,'\nNumbers/digits:',dg,'\nSpecial characters:',sp)

