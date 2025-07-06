adder = lambda x,y:x+y
n1 = int(input('Type first number: '))
n2 = int(input('Type second number: '))

print('The numbers added are',adder(n1,n2))


a = [9319,8032,9955,6468,1061,3167,1358,7216]
b = list(map(lambda n:n%2,a))
print(b)
