#simple interest
    #I = prt
    #Interest = principal x rate x time

#compound interest
    #A = P(1+(r/n))^nt
    #Amount = principal x (1+(rate/number of times interest applied per t))^((number of times interest applied per t)x time in years)


from time import sleep as p
from os import system as s

def cls():
    s('cls')

print('Please note that the variable TIME is acceptable only in YEARS. You may enter a decimal.')
p()
while True:
    while True:
        while True:
            typeInt = input('Choose which type of interest do you want to calculate.\n\nType 1 for simple interest.\nType 2 for compound interest.\n\n')
            try:
                typeInt = int(typeInt)
                break
            except ValueError:
                print('Not an integer.')
                cls()
        if typeInt == 1 or typeInt == 2:
            break

    if typeInt == 1:

        cls()
        print('SIMPLE INTEREST\n\nThe formula of simple interest is I = Prt\nI = interest\nP = principal\nr = rate\nt = time\n\n\nCALCULATE SIMPLE INTEREST\n')
        
        while True:
            p = input('Enter the principal: ')
            input()

            if not p.isdigit():
                print('Not a number.')
                cls()

            else:
                while True:
                    r = input('Enter the rate of interest (per year): ')
                    if not r.isdigit():
                        print('Not a number.')
                        cls()

                    else:
                        while True:
                            t = input('Enter the time (in years): ')
                            if not t.isdigit():
                                print('Not a number.')
                                cls()

                            else:
                                break
                        break
                break

        cls()
        print(f'Principal = {p}\nRate = {r}\nTime = {t}\n\nThe simple interest is prt = {p*r*t}.')
        break


    elif typeInt == 2:

        cls()
        print('COMPOUND INTEREST\n\nThe formula of simple interest is A = P(1+(r/n))^nt\nA = total amount\nP = principal\nr = rate\nn = number of times interest is compounded, per t unit\nt = time\n\n\nCALCULATE COMPOUND INTEREST (variable A)\n')
        while True:
            p = input('Enter the principal: ')
            input()

            if not p.isdigit():
                print('Not a number.')
                cls()

            else:
                while True:
                    r = input('Enter the rate of interest (per year): ')
                    if not r.isdigit():
                        print('Not a number.')
                        cls()

                    else:
                        while True:
                            t = input('Enter the time (in years): ')
                            if not t.isdigit():
                                print('Not a number.')
                                cls()

                            else:
                                while True:
                                    n = input('Enter the number of times interest is compounded per year: ')
                                    if not n.isdigit():
                                        print('Not a number.')
                                        cls()

                                    else:
                                        break
                                break
                        break
                break

        print(f'Principal = {p}\nRate = {r}\nTime = {t}\nNumber of times interest compounded = {n}\n\nThe simple interest is P(1+(r/n))^nt = {p*(1+(r/n))**n*t}.')
        break

    else:
        print('Error, please type 1 or 2.')
