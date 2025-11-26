# sourcery skip: remove-str-from-fstring, use-fstring-for-concatenation
print("welcome to my little game ")
playing=input("Are you ready? ")
print(playing)
if playing!= "yes":
    quit()
print("ok let's play :)")  
score = 0
answer=input("2+2=? ").lower()
if answer == "4":
    print("correct")
    score+=1
else:
    print('incorect')    
answer=input("2+5=? ")
if answer == "7":
    print("correct")
    score+=1
else:
    print('incorect')    
answer=input("9+2=? ")
if answer == "11":
    print("correct")
    score+=1
else:
    print('incorect. You lose')    
print("you got " + str(score) + " correct answers")    
print("you got " + str((score / 3) * 100) + " %")   

    