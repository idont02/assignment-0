def area(l,b):
  print('AREA')
  print(f'The area of the rectangle is l x b which is {l*b}.')
def perim(l,b):
  print('PERIMETER')
  print(f'The perimeter of the rectangle is 2l+2b which is {(2*l)+(2*b)}.')
print('calculating the area/perimeter of the rectangle')
print('Type the length and breadth/width of the rectangle.')
while True:
  l = input('Length: ')
  try:
    l = int(l)
  except:
    print('Error try again.')
while True:
  b = input('Breadth: ')
  try:
    b = int(b)
  except:
    print('Error try again.')
while True:
  opt = input('Please type if you want to calculate the area or the perimeter of the rectangle!\nType 1 for area.\nType 2 for perimeter.')
  try:
    opt = int(opt)
    break
  except:
    print('Error try again.')
if opt == 1:
  area(l,b)
elif opt == 2:
  perim(l,b)
else:
  print('Type 1 or 2.')
  
