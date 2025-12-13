star_max = 5
for i in range(star_max):
    for j in range(i+1):
        print('*', end=" ")
    print()
for k in range(star_max,0,-1):
    for l in range(k):
        print('*', end=" ")
    print()
