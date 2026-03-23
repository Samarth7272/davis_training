def login():
    correct_user = "admin"
    correct_pass = "1234"

    attempts = 0

    while attempts < 3:
        user = input("Username: ")
        password = input("Password: ")

        if user == correct_user and password == correct_pass:
            print("Login Successful")
            return
        else:
            print("Wrong credentials")
            attempts += 1

    print("Account Locked")

login()