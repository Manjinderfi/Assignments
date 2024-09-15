import random


def roll_dice():
    num_of_dice = int(input("How many dice do you want to roll? "))

    total_sum = 0
    for i in range(num_of_dice):
        roll = random.randint(1, 6)  # Roll a die (random number between 1 and 6)
        total_sum += roll  # Add the roll to the total sum

    print(f"The total sum of the dice is: {total_sum}")


# Run the program
roll_dice()
