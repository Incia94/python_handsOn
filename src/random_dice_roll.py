import random

keyboard_input = 'yes'
while keyboard_input == 'Y' or keyboard_input == 'Yes' or keyboard_input == 'y' or keyboard_input == 'YES' or keyboard_input == 'yes':
    num = random.randint(1, 6)
    print("************ Roll the dice **************")
    print("\n")
    print("*********** The Number on the Dice is ***********")
    if num == 1:
        print("1")
    if num == 2:
        print("2")
    if num == 3:
        print("3")
    if num == 4:
        print("4")
    if num == 5:
        print("5")
    if num == 6:
        print("6")
    keyboard_input = input("Press Y to roll again and N to exit:")

