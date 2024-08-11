import getpass
import random
import string

import hashlib

#hashes the password, keeping the value safe
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(username, password):
    # Creates a user with username and password

    # Check if the username is already in use
    if username in users:
        print("Username already exists.")
        return False

    # Keep the new user's information with hashed password
    users[username] = hash_password(password)
    print("User created!")
    return True

def login(username, password):
    # Logins in with given username and password

    # Check if the username doesn't exist
    if username not in users:
        print("Username not found.")
        return False

    # Check if the password matches the stored password
    if users[username] != hash_password(password):
        print("Wrong password.")
        return False

    print(f"Welcome, {username}!")

    # Display custom message based on username
    if username == "admin":
        print("Welcome, Admin!")
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
        "Stop worrying so much, and start enjoying.",
        "Don't waste your time chasing someone else's dream. You can be who YOU want to.",
        "Life is 100x harder than you imagine and things won't go your way. That's the beauty of it.",
    ]
    random_quote = random.choice(quotes)
    print("Random Quote:", random_quote)

    # Add a feature to view account info
    view_info = input("Would you like to see your account info? (yes/no): ")
    if view_info.lower() == 'yes':
        if username in users:
            print("\nAccount Information:")
            print(f"Username: {username}")
            # Note: Displaying password is removed for security reasons
        else:
            print("Account not found.")

    # Add a feature to allow users to change their password
    if username in users:
        change_password = input("Do you want to change your password? (yes/no): ")
        if change_password.lower() == 'yes':
            new_password = getpass.getpass("Enter new password: ")
            confirm_password = getpass.getpass("Confirm new password: ")
            if new_password == confirm_password:
                users[username] = hash_password(new_password)
                print("Password changed!")
            else:
                print("Passwords do not match.")

    # Add custom info for admin
    if username == "admin":
        print("\nAdmin Dashboard:")
        print("--------------------")
        # Example chart (replace with actual data or code)
        print("Users: 5")
        print("Active Users: 3")
        print("Pending Requests: 2")
        print("--------------------")
    elif username == "guest":
        print("\nGuest Access:")
        print("Exclusive information available.")

    # Chance to show the normal screen after login
    chance = random.randint(1, 10)
    if chance == 5:
        print("You got lucky! Returning to main menu...")
        return True

    return True

def generate_password(length=12):
    # Generate a random password using a custom character set and digits
    genrandom = [
        'a', 'b', 'd', 'c', 'e', 'f', 'g', 'd', 't', 'r', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'G', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J', 'V', 'L', 'S', 'N', 'T', 'F', 'Q', 'R', 'S', 'k', 'X',
        'A', 'H', 'X', 'H', 'Z', 'J', 'BA', "TA", 'RA', 'FA', 'TAC', 'Sa', 'Ja', 'La',
        'Fa', 'Me', 'So', "kS", 'Fs', 'Ra', 'Cha', 'tA', 'Be', 'Eb', 'Sd'
    ]

    if length < 6:
        print("Password length must be at least 6 characters.")
        return None

    # Start with 6 random characters from genrandom
    password = ''.join(random.sample(genrandom, 6))

    # Add digits to the password for the remaining length
    for i in range(length - 6):
        password += random.choice(string.digits)  # Append a random digit to the password

    return password

def main():
    # The main function we need for this password project
    global users
    users = {}  # Initialize the users dictionary

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
            length = int(input("Enter password length (minimum 6): "))
            password = generate_password(length)
            if password:
                print("Generated Password:", password)
        elif choice == '4':
            print("Exiting")
            break
        else:
            print("Error! Please select a valid option.")

if __name__ == "__main__":
    main()
