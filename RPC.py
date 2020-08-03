
from random import randint

#create a list of play options
t = ["ROCK", "PAPER", "SCISSORS"]

#assign a random play to the computer


#set player to False
player = False

while player == False:
#set player.upper() to True
    computer = t[randint(0,2)]
    player = input("ROCK, PAPER, SCISSORS? or enter 'E' to exit ")
    if player.upper() == 'E':
        break
    if player.upper().upper() == computer:
        print("Tie!")
    elif player.upper().upper() == "ROCK":
        if computer == "PAPER":
            print("You lose!", computer, "covers", player.upper().upper())
        else:
            print("You win!", player.upper(), "smashes", computer)
    elif player.upper() == "PAPER":
        if computer == "SCISSORS":
            print("You lose!", computer, "cut", player.upper())
        else:
            print("You win!", player.upper(), "covers", computer)
    elif player.upper() == "SCISSORS":
        if computer == "ROCK":
            print("You lose...", computer, "smashes", player.upper())
        else:
            print("You win!", player.upper(), "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False


