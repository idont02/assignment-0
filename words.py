from random import *
import os
import time as t
import wordlist
database = 'dbgame.txt'
userdata = {}
def dataread():
    file = open(database,'r')
    for data in file:
        data = data.strip()
        user,passw = data.split(',')
        userdata[user] = passw

def login_proc():
    print('===LOGIN===')
    username = input("Enter Username:")
    password = input("Enter password:")
    if username in userdata: # type: ignore
        if password == userdata[username]: # type: ignore
            print(f'Login successful! Welcome, {username}')
            return True
        else:
            print('Wrong password.')
            return False
    else:
        print('username not found')
        return False

def register_proc():
    print('===REGISTER===')
    while True:
        usernamed = input('choose a username: ')
        passwords = input('choose a password: ')
        if ',' in usernamed or ',' in passwords:
            print('Comma not accepted in username or password!!')
        else:
            break
    files = open(database,'a')
    files.write(f'{usernamed},{passwords}\n')
    dataread()
    print('user registration successful!!!!!!!!!!!!!!!!!')

def show_users():
    print('===USER LIST===')
    no = 1
    for user in userdata.keys():
        print(no,user)
        no +=1

def playGame():
    print('WELCOME')
    word = choice(wordlist.wordlist)
    chances = 8
    guessed_letters=''
    print(f'The word is {len(word)} letters long.\nSTART GUESSING')

    while chances >0:
        guess=input('\nGuess a letter of the word: ')
        t.sleep(1)
        os.system('cls')
        guessed_letters+=guess
        wrong=False
        for letter in word:
            if letter in guessed_letters:
                print(letter)
            else:
                print('_')
                wrong=True
        if wrong==False:
            print('Congrats! You guessed the word.\nThe word is',word.upper())
            break
        if guess not in word:
            chances-=1
            print('WRONG GUESS\nYou have',chances,'more chances to guess the word.')
            if chances==0:
                print(f'GAME OVER!\nThe word was {word.upper()}. Thanks for playing!')

def login():
    login_status = False
    while login_status == False:
        print('===MENU===\n1 login\n2 register\n3 show users\n4 exit')
        choice = int(input('choose an option: '))
        if choice == 1:
            login_status = login_proc()
        elif choice == 2:
            register_proc()
            login_status = login_proc()
        elif choice == 3:
            show_users()
        elif choice == 4:
            print('\nGoodbye')
            break
        else:
            print('invalid')
    if login_status == True:
        playGame()
dataread()
login()
