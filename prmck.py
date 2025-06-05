from math import sqrt

while True:
    n = input('Type a number to check if it is prime: ')
    try:
        n = int(n)
        break
    except:
        print('Error, try again.')
composite = False
limit = sqrt(n)
limit = int(limit)
for i in range(2,limit):
    copy_n = n
    copy_n/=i
    print(f'{copy_n}/{i}')
    if copy_n.is_integer():
        composite = True
        break
    else:
        pass

if n == 1 or n == 0:
    print('0 and 1 are neither primes nor composite.')
    composite = None
elif n < 0:
    composite = None
    print('i do not know.')

if composite == False:
    print('The number is prime.')
elif composite == True:
    print('The number is composite.')

print(n)
