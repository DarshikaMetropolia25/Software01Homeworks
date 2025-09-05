import random
user_input = int(input("How many dice to roll? "))
dice_values=[]

for i in range (user_input):
    random1= random.randint(1,6)
    dice_values.append(random1)

print(sum(dice_values))






