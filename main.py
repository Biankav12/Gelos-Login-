import sys, time
import string, random

username = ""

while True:
    print("Welcome user to the Gelos Enterprise")
    print("\nWhat would you like to do:")

    if username == "":
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

        choice = int(input("Choose which one you would like: "))

        if choice == 1:
            login_user = input("Enter your username: ")
            login_pass = input("Enter your password: ")

            with open('accounts.txt', 'r') as file:
                accounts = file.read().split('\n')
                for account in accounts:
                    if account.startswith(login_user) and account.endswith(login_pass):
                        username = login_user
                if username == "":
                    print('Login Unsuccessful')
                
        elif choice == 2:
            login_user = input("Enter your username: ")

            auto_generate = int(input("Would you like to auto generate a password (Yes - 1, No - 2)? "))

            if auto_generate == 2:
                password = input("\nEnter your password: ")
            elif auto_generate == 1:
                chosen_characters = input("\nChoose your options [A - Numbers, B - Uppercase, V - Lowercase, Q - Symbols]: ")

                character_set={
                    'A':"0123456789",
                    'B':"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    'V':"abcedfghijklmnopqrstuvwxyz",
                    'Q':"@#$%&"
                }

                selected_chars = ''.join([character_set['A'] if 'A' in  chosen_characters else '',
                            character_set['B'] if 'B' in chosen_characters else '',
                            character_set['V'] if 'V' in chosen_characters else '',
                            character_set['Q'] if 'Q' in chosen_characters else ''
                ])

                length = input("How long would you like the length of your password to be? ")


                password = ''.join(random.choice(selected_chars) for _ in range(int(length)))

            print("Above is your password! ", password)

            with open('accounts.txt', 'a') as file:
                account = "\n" + login_user + " " + password
                file.write(account)
        else:
            print("3")
            time.sleep(2)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("Bye!")
            sys.exit()
    else:
        print("1. View Users")
        print("2. Logout")

        choice = int(input("Choose which one you would like: "))

        if choice == 1:
            if username == "Admin":
                with open('accounts.txt', 'r') as file:
                    accounts = file.read().split('\n')
                    for account in accounts:
                        print(account + '\n')
            else:
                print('Sorry only Admins can do that')
        else:
            username = ""
