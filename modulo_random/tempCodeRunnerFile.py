from random import randint

magic_number = randint(0, 9)
user_input = input("Enter 'y' if you would like to play: ")

if user_input == "y":
    user_number = int(input("Guess our number:  "))
    if user_number == magic_number:
        print(f"You guessed correctly!, {user_number}")
    else:
        print("Sorry, it's wrong!, magic number:{magic_number}, \
            your guess:{user_number}")