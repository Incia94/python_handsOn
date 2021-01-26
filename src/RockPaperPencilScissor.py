import random

game = "Y"
string_list = ["ROCK", "PAPER", "PENCIL", "SCISSOR"]
print("*************  Welcome to Rock Paper Pencil Scissor Game Simulation  *************")
print("\n")
player1_name = input("Enter Name Player 1:")
player2_name = input("Enter Name Player 2:")
while game == 'Y'or game == 'y' or game == 'Y' or game == 'y':
    print("{}, Its Your Turn".format(player1_name))
    player1_output = random.choice(string_list)
    print("You Get: {}".format(player1_output))
    print("\n")
    print("{}, Its Your turn".format(player2_name))
    player2_output = random.choice(string_list)
    print("You Get: {}".format(player2_output))
    print("\n")
    if ((player1_output == "ROCK" and player2_output == "ROCK") or
        (player1_output == "PAPER" and player2_output == "PAPER") or
        (player1_output == "PENCIL" and player2_output == "PENCIL") or
        (player1_output == "SCISSOR" and player2_output == "SCISSOR")):
        print("Its a Tie. Play another round")
    if player1_output == "ROCK" and player2_output == "PENCIL":
        print("{} wins the round".format(player1_name))
    elif player2_output == "ROCK" and player1_output == "PENCIL":
        print("{} wins the round".format(player2_name))
    if player1_output == "ROCK" and player2_output == "PAPER":
        print("{} wins the round".format(player2_name))
    elif player1_output == "PAPER" and player2_output == "ROCK":
        print("{} wins the round".format(player1_name))
    if player1_output == "PAPER" and player2_output == "SCISSOR":
        print("{} wins the round".format(player2_name))
    elif player1_output == "SCISSOR" and player2_output == "PAPER":
        print("{} wins the round".format(player1_name))
    if player1_output == "ROCK" and player2_output == "SCISSOR":
        print("{} wins the round".format(player1_name))
    elif player1_output == "SCISSOR" and player2_output == "ROCK":
        print("{} wins the round".format(player2_name))
    if player1_output == "SCISSOR" and player2_output == "PENCIL":
        print("{} wins the round".format(player1_name))
    elif player1_output == "PENCIL" and player2_output == "SCISSOR":
        print("{} wins the round".format(player2_name))
    if player1_output == "PAPER" and player2_output == "PENCIL":
        print("{} wins the round".format(player2_name))
    elif player1_output == "PENCIL" and player2_output == "PAPER":
        print("{} wins the round".format(player1_name))
    game = input("PRESS Y TO PLAY AGAIN or N TO EXIT")
