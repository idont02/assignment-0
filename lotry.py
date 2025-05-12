from random import randint
def checkint():
   while True:
    n = input()
    try:
      int(n)
      break
    except:
      print('Error, try again.\nDISCLAIMER: This failure is caused by an ERROR.')
    finally:
      input('Press ENTER to proceed.')
def main(r):
   while True:
      print('Pick a number between 1 -',r2)
      checkint()
      input('Press ENTER to proceed.')
    lot = randint(1,r2)
    if n == lot:
      print('That is a lottery! You win!')
    else:
      print('That is not the number. You lose.')
    print('The number was',lot,'\nType 1 to retry\nType 0 to exit')
    while True:
      re = input()
      checkint()
      if re == 1 or re == 0:
        pass
      else:
        print('Please type 0 or 1.')
    if re == 0:
      break
input('welcome to the lottery bot\nThe rules are simple: You and the bot will guess a number. If it matches, you win!\nPress ENTER\n')
print('Select difficulty:\n\nPossible\nVery Easy\nEasy\nNormal\nHard\nVery Hard\nActually a lottery\nImpossible\n')
d = input()
d=d.lower()
if d == 'possible':
  main(10)
elif d == 'very easy':
  main(30)
  
  
      
