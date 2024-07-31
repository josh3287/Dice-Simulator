# Import random
# Define a function to roll the dice
# Create a dictionary that will hold all dice values

import random

def roll_dice():
    roll = input("Take your chances, roll the dice (Yes/No): ")
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1,6)

        print("dice rolled: {} and {}".format(dice1,dice2))

        roll = input("Roll again?")

roll_dice()