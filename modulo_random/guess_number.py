from random import randint

user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":
    magic_number = randint(0, 9)
    user_number = int(input("Guess our number:  "))
    if user_number == magic_number:
        print(f"You guessed correctly!, {user_number}")
    elif magic_number - user_number in (1, -1):
        print("You were off by one")
    else:
        print(f"Sorry, it's wrong!, magic number is {magic_number}, your guess was {user_number}")
