import random

def dice_roll(sides_of_dice):
    dice = random.randint(1, sides_of_dice)
    return dice

number_of_sides = int(input("How many sides do you want? "))
roll_result=0
while roll_result != number_of_sides:
    roll_result = dice_roll(number_of_sides)
    print(roll_result)