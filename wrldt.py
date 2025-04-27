print("Hi welcome to World Tour Bot")
print("Press 1 to visit Europe")
print("Press 2 to visit Asia")
print("Press 3 to visit South America")

choice=input("please enter your choice: ")

if(choice=="1"):
    print("please enter the country you want to visit in Europe")
    country=input()
    if(country=="Finland"):
        print("Welcome to Finland")
    elif(country=="Germany"):
        print("Welcome to Germany")
    elif(country=="France"):
        print("Welcome to France")
    else:
        print("please select from Finland, Germany and France")
        
elif(choice=="2"):
    print("please enter the country you want to visit in Asia")
    country=input()
    if(country=="India"):
        print("Welcome to India")
    elif(country=="Indonesia"):
        print("Welcome to Indonesiar")
    elif(country=="Japan"):
        print("Welcome to Japan)
    else:
        print("please select from India, Indonesia and Japan")
        
elif(choice=="3"):
    print("please enter the country you want to visit in South America")
    country=input()
    if(country=="Bolivia"):
        print("Welcome to Bolivia")
    elif(country=="Colombia"):
        print("Welcome to Colombia")
    elif(country=="Peru"):
        print("Welcome to Peru")
    else:
        print("please select from Bolivia, Colombia and Peru")

elif(choice=="4"):
    print("please enter the country you want to visit in North America")
    country=input()
    if(country=="Canada"):
        print("Welcome to Canada")
    elif(country=="USA"):
        print("Welcome to USA")
    elif(country=="Mexico"):
        print("Welcome to Mexico")
    else:
        print("please select from Canada, USA and Mexico")
        
else:
    print("please enter the proper input")
  
    
