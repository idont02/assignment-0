print('Type anything: ')
st = str(input()
for i in st:
  if st[i].isupper():
    up+=1
  elif st[i].islower():
    lo+=1
  elif st[i].isdigit():
    dg+=1
  else:
    sp+=1
print('\nUppercase letters:',up,'\nLowercase letters:',lo,'\nNumbers/digits:',dg,'\nSpecial characters:',sp)
