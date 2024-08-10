import getpass

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
    return True

def main():
    #the main function we need for this password project
    global users
    users = {}

    while True:
        print("\nChoose an option:")
        print("1. Create a new user")
        print("2. Login")
        print("3. Exit")

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
            print("Exiting...")
            break
        else:
            print("Wrong choice.")

if __name__ == "__main__":
    main()
