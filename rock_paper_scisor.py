import random

choices = ('r' , 'p', 's')
emoji = {
    'r':'🪨',
    's':'✂️',
    'p':'📃'
}


while True:

    user_choice = input("rock ,paper or scissor?(r/p/s)").lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue


    pc_choice = random.choice(choices)

    print(f"you chose {emoji[user_choice]}")
    print(f"pc chose {emoji[pc_choice]}")

    if user_choice == pc_choice:
        print("Tie")
    elif \
        (user_choice == 'r' and pc_choice == 's') or \
        (user_choice == 's' and pc_choice=='p') or\
        (user_choice == 'p' and pc_choice == 'r'):
        print("You win")
    else:
        print("You lose")
        
        
    should_continue = input("Comtinue(y/n): ")

    if should_continue == 'n':
        break
    