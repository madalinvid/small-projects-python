import random

choices = ('r' , 'p', 's')
user_choice = input("rock ,paper or scissor?(r/p/s)").lower()
if user_choice not in choices:
    print("Invalid choice")

emoji = {
    'r':'🪨',
    's':'✂️',
    'p':'📃'
}

pc_choice = random.choice(choices)


print(f"you chose {emoji[user_choice]}")
print(f"pc chose {emoji[pc_choice]}")