import random
def dice_roll():
    dice = random.randint(1, 6)
    return dice

roll_result=0
while roll_result != 6:
    roll_result = dice_roll()
    print(roll_result)

