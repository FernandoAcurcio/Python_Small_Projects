# other users are unable to see the other user input
from getpass import getpass as input

print("E P I C   R O C K   P A P E R   S C I S S O R S   B A T T L E ")
print()
print("Select your move (R, P or S)")
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")

answer = ""

while answer != "yes":
    if (player1 == player2):
        print("Both players selected" + player1 + ". It's a tie!")
    elif (player1.upper() == "R"):
        if (player2.upper() == "P"):
            print("Player 2 paper covers player 1 rock! Player 2 wins!")
        else:
            print("Player 1 rock smashes player 2 scissors! Player 1 wins!")
    elif (player1.upper() == "P"):
        if (player2.upper() == "R"):
            print("Player 1 paper covers player 2 rock! Player 1 wins!")
        else:
            print("Player 2 scissors cuts player 1 paper! Player 2 wins!")
    elif (player1.upper() == "S"):
        if (player2.upper() == "R"):
            print("Player 2 rock smashes player 1 scissors! Player 2 wins!")
        else:
            print("Player 1 scissors cuts player 2 paper! Player 1 wins!")
    answer = input("Do you want to exit? yes or no")