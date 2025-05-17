from random import randint
print('welcome to lotery bot')
print('pick a number, then the bot will pick a number, if it is the same, you win.')
print('pick from 1 - 100')
r = randint(1,100)
print(r)
print(type(r))
n = input()
while True:
    try:
        n = int(n)
        break
    except:
        input('Not a whole number. Press ENTER.')
print(type(n))

if n == r:
    print('That is the lottery! YOU WIN!!')
else:
    print('That is not the lottery. The number was',r,'.')
