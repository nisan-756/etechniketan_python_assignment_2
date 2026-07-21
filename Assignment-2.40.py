print("Welcome to the grade checker program!")

while True:
    marks = float(input("Enter your marks (0-100): "))

    if 90 <= marks <= 100:
        print("Your grade is A+")
    elif 80 <= marks <= 89:
        print("Your grade is A")
    elif 70 <= marks <= 79:
        print("Your grade is B")
    elif 60 <= marks <= 69:
        print("Your grade is C")
    elif 50 <= marks <= 59:
        print("Your grade is D")
    else:
        print("Your grade is Fail")

    choice = input("Do you want to check the grade for another marks? (yes/no): ").lower()

    if choice == "no":
        print("Thank you!")
        break