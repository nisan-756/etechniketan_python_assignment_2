import random

print("Welcome to the Simple Coin Toss Game!")

while True:
    while True:
        guess = input("Guess 'heads' or 'tails': ").lower()

        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input! Please enter 'heads' or 'tails'.")

    toss = random.choice(["heads", "tails"])

    print("Coin shows:", toss)

    if guess == toss:
        print("You guessed it right!")
    else:
        print("Wrong guess!")

    choice = input("Do you want to play again? (yes/no): ").lower()

    if choice == "no":
        print("Thanks for playing!")
        break