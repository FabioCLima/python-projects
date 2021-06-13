# %%
from random import randint


def computer_number(min_num: int, max_num: int) -> int:
    """[function that generates a random number based on the range pass as args]

    Args:
        min_num (int): [minimum int number]
        max_num (int): [maximum int number]

    Returns:
        int: [a random int number between min_num and max_number]
    """

    return randint(min_num, max_num)

# %%


def player_guess(min_num: int, max_num: int) -> int:
    """[Function that asks the player for a number]

    Args:
        min_num ([int]): [minimum int number]
        max_num ([int]): [minimum int number]

    Returns:
        [int]: [random number]
    """
    try:
        user_input = int(input(f"Guess a number between {min_num} \
        and {max_num}:\n"))
        return user_input
    except ValueError:
        print(f"Try a valid integer number.")
        user_input = 0
        return user_input 
# %%


def play():
    """[The function to interact with player]
    """

    #! define high and low guessing range
    low, high = 0, 10

    #! get input from computer and player
    computer_choice = computer_number(low, high)
    player_choice = player_guess(low, high)

    #! loop until player guesses the number
    while player_choice != computer_choice:
        if player_choice > computer_choice:
            player_choice = int(input("Number is too high, try again:\n"))
        elif player_choice < computer_choice:
            player_choice = int(input("Number is too low, try again:\n"))

    print(f"Congratulation! You managed to guess the number {computer_choice}")


play()
