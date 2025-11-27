pwd = input("what is teh master password ? ")

def view():
    pass

def add():
    name = input("account name")
    password = input("password: ")
    with open('password.txt','a') as f:
        f.write(name + '|'+ password)


while True:
    mode = input("would you like to ad a new password or view existing ones(view/add) or press q to quit ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid mode')
        continue