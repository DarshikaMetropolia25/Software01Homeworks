import random
Random_number = random.randint(1,10)
user_input = int(input("Guess a number between 1 and 10 : "))
while user_input != Random_number:
    if user_input > Random_number:
        print("Too High")
        user_input = int(input("Try again : "))
    else:
        print("Too Low")
        user_input = int(input("Try again : "))
print("Correct")
