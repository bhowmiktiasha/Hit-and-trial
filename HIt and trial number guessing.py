import random
number=random.randint(1,10)
trials=1
username =input("Hello,what is your name?")
print('Hello',username)
query = input("Would you like to play a game with me? [Y/N] ")
if query == 'n':
    print("Its Fine.No worries")
if query == 'y':
    print("Well,I'm thinking of a number between 1 to 10")
    guess=int(input("Guess What: "))
    if guess>number:
        print("Well,Ah guess lower..")
        if guess<number:
            print("Umm,guess higher...")
        while guess!=number:
            trials+=1    
            guess=int(input("Try Again..."))
            if guess<number:
               print("Guess Higher")
        if guess==number:
            print("Wohooah great**You WIN *** So The number was",number,"and it was just with only",trials,"trials!")
