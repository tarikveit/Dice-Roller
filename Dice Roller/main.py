import random
print("Welcome to the Dice Roller")

#Choosing the type of dice and number of rolls
side = int(input("How many sides does the dice have? "))
dice_number = int(input("How many times do you want to roll? "))
dice_result = 0

#Printing results
counter = 0
dice_total = 0
for counter in range(0,dice_number,1):
    dice_result = random.randint(1,side)
    print("Roll", counter+1,"-", dice_result)
    dice_total += dice_result
print("The dice total is",dice_total)

wait = input("Press Enter to exit.")