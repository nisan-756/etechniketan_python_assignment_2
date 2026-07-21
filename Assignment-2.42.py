password = "python123"

attempts = 3

while attempts > 0:
    user_password = input("Enter password: ")

    if user_password == password:
        print("Access granted")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Access denied")
        else:
            print("Wrong password! Attempts left:", attempts)