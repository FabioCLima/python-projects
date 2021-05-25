from random import randint

random_number = randint(0, 9)
user_input = input("Would like to play: (Y/n) \n")

while user_input != "n":
    user_number = int(input("Guess our number:  "))
    if user_number == random_number:
        print(f"You guessed correctly!, {user_number}")
    elif abs(random_number - user_number) == 1:
        print("You were off by one.")
    else:
        print(f"Sorry, it's wrong!, magic number:{random_number}, your guess:{user_number}")

    user_input = input("Would like to play: (Y/n) \n")
