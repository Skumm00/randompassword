import getpass

import random

import string

def create_user(username, password):

    #creates a user with username and password
    
    # Check if the username is already in use
    if username in users:
        print("Username already exists.")
        return False

    # Keep the new user's information
    users[username] = password
    print("User created successfully!")
    return True

def login(username, password):
    #Logins in with given username and password
    
    # Check if the username exists
    if username not in users:
        print("Username not found.")
        return False

    # Check if the password matches the stored password
    if users[username] != password:
        print("Wrong password.")
        return False

    print(f"Welcome, {username}!")

    
    # Display custom message based on username
    if username == "admin":
        print("Welcome, Administrator!")
    elif username == "guest":
        print("Welcome, Guest!")
    else:
        print("Welcome, User!")
    
    # Display random quote
    quotes = [
        
        "The only way to do great work is to love what you do.",
        "Your time is limited, so don't waste it doing something you don't want to.",
        "Life is the greatest test with only victors and losers.",
        "Don't let others make desicions for you.",
        "Stop Worrying so much, and start enjoying.",
        "Dont Waste your time chasing someone elses dream. You can be who YOU want to.",
        "Life is 100x harder then you imagine and things wont go your way. Thats the bueaty of it",

    ]
    random_quote = random.choice(quotes)
    print("Random Quote:", random_quote)

    return True

def generate_password(length=12):
    # Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    #the main function we need for this password project
    global users
    users = {}

    while True:
        print("\nChoose an option:")
        print("1. Create a new user")
        print("2. Login")
        print("3. Generate Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            create_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            login(username, password)
        elif choice == '3':
            password = generate_password()
            print("Generated Password:", password)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Wrong choice.")

if __name__ == "__main__":
    main()