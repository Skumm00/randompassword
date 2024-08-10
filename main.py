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
        print("Welcome, Level 1 User!")
    else:
        print("Welcome, User!")

    # Display random quote
    quotes = [
        "The only way to do great work is to love what you do.",
        "Your time is limited, so don't waste it doing something you don't want to.",
        "Life is the greatest test with only victors and losers.",
        "Don't let others make decisions for you.",
        "Stop Worrying so much, and start enjoying.",
        "Don't Waste your time chasing someone else's dream. You can be who YOU want to.",
        "Life is 100x harder then you imagine and things wont go your way. Thats the beauty of it",
    ]
    random_quote = random.choice(quotes)
    print("Random Quote:", random_quote)

    # Add a feature to view account info
    view_info = input("Would you like to see your account info? (yes/no): ")
    if view_info.lower() == 'yes':
        if username in users:
            print("\nAccount Information:")
            print(f"Username: {username}")
            print(f"Password: {users[username]}")
            # Option to view password
            view_password = input("Would you like to see your password? (yes/no): ")
            if view_password.lower() == 'yes':
                print(f"Password: {users[username]}")
            else:
                print("Password not here.")
        else:
            print("Account not here.")
    # Add a feature to allow users to change their password
    if username in users:
        change_password = input("Do you want to change your password? (yes/no): ")
        if change_password.lower() == 'yes':
            new_password = getpass.getpass("Enter new password: ")
            confirm_password = getpass.getpass("Confirm new password: ")
            if new_password == confirm_password:
                users[username] = new_password
                print("Password changed!")
            else:
                print("Passwords do not match.")
    return True

def generate_password(length=12):
    # Generate a random password
    genrandom = ['a', 'b', 'd', 'c', 'e', 'f', 'g', 'd', 't', 'r', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'G', 'C', 'D','E', 
                 'F', 'G', 'H', 'I', 'J', 'V', 'L', 'S', 'N', 'T', 'F', 'Q', 'R', 'S', 'k',                     'X', 'A', 'H','X', 'H', 'Z', 'J','BA',"TA",'RA','FA','TAC','Sa','Ja','La'
                'Fa','Me','So',"kS",'Fs','Ra','Cha','tA','Be','Eb','Sd'
                ]
    password = ''.join(random.sample(genrandom, 6))
    for i in range(length - 6):
        password += random.choice(string.digits)
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
            print("Error!")

if __name__ == "__main__":
    main()