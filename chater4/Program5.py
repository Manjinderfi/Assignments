def login():
    correct_username = "python"
    correct_password = "rules"

    attempts = 0

    while attempts < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Welcome!")
            break  # Stop the loop if the login is correct
        else:
            print("Incorrect username or password. Try again.")
            attempts += 1  # Increase the attempt count

        if attempts == 5:
            print("Access denied.")


login()
