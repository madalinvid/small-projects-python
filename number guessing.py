# sourcery skip: useless-else-on-loop
import random

top=input("type a number  ")

if top.isdigit():
    top = int(top)
    if top <=0: # type: ignore
        print("entr a larger number  ")
        quit()
else:
    print("please type a number")
    quit()        
guess= input("make a guess")    

r=random.randrange(0,guess)
while True:
    guess= input("make a guess")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please type a number")
        continue
    if guess==r:
        print('you guess the number')
        break

    else:
        print("you got it wrong")    