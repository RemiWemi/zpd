import random

repeat = True

while repeat:
    number = random.randint(1, 100)
    guess = 0
    tries = 0

    while guess != number:
        if guess < number:
            print("too small")
        else:
            print("too biggy")

        guess = int(input("Guess the number: "))
        tries += 1
    else:
        print(f"Bruh stoopid ugly ahh, you took {tries} tries")

    response = input("Do you wanna continue?? y/n: ")
    if response == "y":
        repeat = True
    elif response == "n":
        repeat = False
        print("Stoopid loser bitch")
    else:
        repeat = False
        print("L Bozo")
