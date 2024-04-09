#Bianka Varsanyi
#09.04.2024
#Gelos Login 

import string, random
import sys, time

# Initialize the username variable (String manipulation - initializing a string)
username = ""

while True:  # Loop construct to keep the program running
    print("Welcome user to the Gelos Enterprise")
    print("\nWhat would you like to do:")

    if username == "":  # Conditional construct - checks if username is empty
        # Display options for unauthenticated users
        print("A. Login")
        print("B. Signup")
        print("C. Exit")

        choice = input("Choose which one you would like: ").lower()  # Input and string manipulation (lowercase conversion)

        if choice == 'a':  # Conditional operator - checking user choice
            login_user = input("Enter your username: ")  # Input operation
            login_pass = input("Enter your password: ")  # Input operation

            with open('accounts.txt', 'r') as file:  # File reading operation
                accounts = file.read().split('\n')  # String manipulation (splitting string by newline)
                for account in accounts:  # Loop construct to iterate through accounts
                    # String concatenation is happening implicitly in the startswith and endswith methods
                    if account.startswith(login_user) and account.endswith(login_pass):  # String manipulation & conditional operators
                        username = login_user  # String assignment
                if username == "":  # Conditional operator
                    print('Login Unsuccessful')  # Output operation
                
        elif choice == 'b':  # Conditional operator
            login_user = input("Enter your username: ")  # Input operation

            auto_generate = input("Would you like to auto generate a password (Yes - Y, No - N)? ").lower()  # Input and string manipulation

            if auto_generate == 'n':  # Conditional operator
                password = input("\nEnter your password: ")  # Input operation
            elif auto_generate == 'y':  # Conditional operator
                chosen_characters = input("\nChoose your options [A - Numbers, B - Uppercase, C - Lowercase, D - Symbols]: ")  # Input operation

                character_set = {  # Dictionary initialization
                    'A': "0123456789",
                    'B': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    'C': "abcedfghijklmnopqrstuvwxyz",
                    'D': "@#$%&"
                }

                # String concatenation and manipulation with join and conditional expressions
                selected_chars = ''.join([
                    character_set['A'] if 'A' in chosen_characters else '',
                    character_set['B'] if 'B' in chosen_characters else '',
                    character_set['C'] if 'C' in chosen_characters else '',
                    character_set['D'] if 'D' in chosen_characters else ''
                ])

                length = input("How long would you like the length of your password to be? ")  # Input operation

                # String concatenation in password generation with a for loop and random choice
                password = ''.join(random.choice(selected_chars) for _ in range(int(length)))  # String manipulation and loop construct

            print("Above is your password! ", password)  # Output operation

            with open('accounts.txt', 'a') as file:  # File writing operation
                account = "\n" + login_user + " " + password  # String concatenation
                file.write(account)  # Writing string to file
                
        elif choice == 'c':  # Conditional operator
            print("3")
            time.sleep(2)  # Pause operation with sleep function
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("Bye!")
            sys.exit()  # Exit operation
    else:
        print("A. View Users")
        print("B. Logout")

        choice = input("Choose which one you would like: ").lower()  # Input and string manipulation

        if choice == 'a':  # Conditional operator
            if username == "Admin":  # Conditional operator
                with open('accounts.txt', 'r') as file:  # File reading operation
                    accounts = file.read().split('\n')  # String manipulation (splitting string by newline)
                    for account in accounts:  # Loop construct
                        print(account + '\n')  # Output operation with string concatenation
            else:
                print('Sorry only Admins can do that')  # Output operation
                
        elif choice == 'b':  # Conditional operator
            username = ""  # String manipulation (clearing a string)
