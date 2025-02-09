print('uses metric system')
print('type 1 for square')
print('type 2 for rectangle')
opt = int(input('type here: '))
if opt == 1:
  s = int(input('type side length: '))
  print('The area of the square is',s**2,'cm^2')
elif opt == 2:
  l = int(input('type length: '))
  b = int(input('type breadth: '))
  print('The area of the rectangle is',l*b,'cm^2')
