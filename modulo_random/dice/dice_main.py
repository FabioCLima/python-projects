from random import randint
import statistics
# Define the dice rolling function using two inputs.


def roll_many(n: int, x: int):
    rolls = []
    for i in range(x):
        dice_roll = randint(1, n)
        rolls.append(dice_roll)
        print(f"{dice_roll} and {statistics.mean(rolls)}")


if __name__ == "__main__":
    roll_many(6, 4)
